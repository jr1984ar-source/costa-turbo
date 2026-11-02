import cv2,numpy as np,glob
from PIL import Image,ImageDraw,ImageFont,ImageFilter
GW=390;VS=1.25;rng=np.random.default_rng(7)
NAMES={1:"SALIDA · Bar JJ's (Son Matías)",2:'Punta Negra',3:'Cap des Gegant',4:'Puerto Portals',5:'Portals Nous',6:'Illa de sa Torre',7:'META · Platja de Illetes'}
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',14)
def load(i):
    f=glob.glob(f'cap{i}.*')[0];land=(cv2.imread(f'tierra{i}.png',0)>0).astype(np.uint8)
    clean=cv2.resize(cv2.imread(f'clean{i}.jpg'),(land.shape[1],land.shape[0]))
    hsv=cv2.cvtColor(clean,cv2.COLOR_BGR2HSV).astype(np.float32);h=hsv[...,0]*2;s=hsv[...,1]/255;v=hsv[...,2]/255
    shore=np.array([(np.where(land[r])[0].max() if land[r].any() else 0) for r in range(land.shape[0])])
    med=np.median(shore[shore>0]);shift=int(max(0,med-400))
    def cut(a):
        a=a[:,shift:shift+1206];return np.pad(a,((0,0),(0,1206-a.shape[1]))) if a.shape[1]<1206 else a
    land,h,s,v=cut(land),cut(h),cut(s),cut(v)
    H=int(land.shape[0]*GW/1206*VS);rs=lambda a:cv2.resize(a.astype(np.float32),(GW,H))
    L=rs(land)>.5;h,s,v=rs(h),rs(s),rs(v)
    cls=np.zeros((H,GW),np.uint8)                      # 0 roca 1 arena 2 verde 3 casas
    cls[(s<.12)&(v>.45)]=3;cls[(h>=20)&(h<=60)&(s<.42)&(v>.62)]=1;cls[(h>=60)&(h<=170)&(s>.12)]=2
    cls=cv2.medianBlur(cls,7)
    sh=np.array([(np.where(L[r])[0].max() if L[r].any() else 0) for r in range(L.shape[0])])
    ok=np.where(sh<230)[0]
    if len(ok):L,cls=L[ok.min():ok.max()+1],cls[ok.min():ok.max()+1]
    L[:, :24]=True
    return L,cls
def paint(L,cls):
    H=L.shape[0];img=np.zeros((H,GW,3),np.float32)
    d=cv2.distanceTransform((~L).astype(np.uint8),cv2.DIST_L2,5)
    t=np.clip(d/38,0,1)[...,None];tt=np.clip((d-38)/140,0,1)[...,None]
    img[:]=(np.array([140,236,226])*(1-t)+np.array([22,150,200])*t)*(1-tt)+np.array([14,104,176])*tt
    pal=np.array([[196,124,70],[243,220,174],[96,150,74],[226,220,208]],np.float32)
    lc=pal[cls]+rng.normal(0,7,(H,GW,1));dl=cv2.distanceTransform(L.astype(np.uint8),cv2.DIST_L2,5)
    lc[(dl<6)&(cls!=1)]=pal[0]*.85                  # borde de roca
    img[L]=lc[L]
    edge=cv2.morphologyEx(L.astype(np.uint8),cv2.MORPH_GRADIENT,np.ones((3,3),np.uint8))>0;img[edge&~L]=255
    out=Image.fromarray(np.clip(img,0,255).astype(np.uint8)).filter(ImageFilter.SMOOTH);dr=ImageDraw.Draw(out)
    for c,n in ((2,60),(3,22)):
        ys,xs=np.where((cls==c)&L&(dl>8))
        if not len(ys):continue
        for k in rng.choice(len(ys),min(len(ys),n),replace=False):
            x,y=xs[k],ys[k]
            if c==2:r=4+rng.random()*4;dr.ellipse([x-r+2,y-r+2,x+r+2,y+r+2],fill=(40,60,30));dr.ellipse([x-r,y-r,x+r,y+r],fill=(58,112,52))
            else:w=9+rng.random()*12;dr.rectangle([x,y,x+w,y+w*.8],fill=[(217,119,90),(242,239,232),(201,167,122)][k%3],outline=(150,140,130))
    return out
def transition(La,Lb,n=260):
    def sh(L,row):r=np.where(L[row])[0];return min(190,r.max()) if len(r) else 24
    a=sh(La,0);b=sh(Lb,Lb.shape[0]-1);L=np.zeros((n,GW),bool)
    for r in range(n):
        t=r/(n-1);t=t*t*(3-2*t);x=b*(1-t)+a*t+10*np.sin(r/23)
        L[r,:int(max(24,x))]=True
    cls=np.where(rng.random((n,GW))<.5,0,2).astype(np.uint8);cls=cv2.medianBlur(cls,9)
    return L,cls
secs=[load(i) for i in range(1,8)]
blocks=[]
for k,(L,c) in enumerate(secs):
    p=paint(L,c);d=ImageDraw.Draw(p);tw=d.textlength(NAMES[k+1],font=F)
    d.rounded_rectangle([GW-tw-18,8,GW-6,30],6,fill=(8,22,48));d.text((GW-tw-12,11),NAMES[k+1],fill=(255,225,77),font=F)
    p.tag=k+1;blocks.append(p)
    if k<6:
        Lt,ct=transition(secs[k][0],secs[k+1][0]);blocks.append(paint(Lt,ct))
# la meta arriba: el primer bloque va abajo
order=blocks[::-1];H=sum(b.size[1] for b in order);full=Image.new('RGB',(GW,H));y=0
for b in order: full.paste(b,(0,y));y+=b.size[1]
full.save('estilo_full.png')
import json;pos={};yy=0
for b in order:
    if getattr(b,'tag',None):pos[b.tag]=[yy,yy+b.size[1]]
    yy+=b.size[1]
json.dump(pos,open('pos.json','w'))
W,H=full.size;n=4;h=(H+n-1)//n;o=Image.new('RGB',(W*n+12*(n-1),h),'white')
for k in range(n):o.paste(full.crop((0,H-(k+1)*h,W,H-k*h)),(k*(W+12),0))
o.resize((o.size[0]//2,o.size[1]//2)).save('estilo_cols.png');print(full.size)
