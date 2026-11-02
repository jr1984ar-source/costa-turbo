import json,base64,io,numpy as np,cv2
from PIL import Image
d=json.load(open('realmap3.json'));M=np.array(Image.open(io.BytesIO(base64.b64decode(d['src'].split(',')[1])))).astype(np.int32)
M=np.rint(M/36).astype(np.uint8);H,W=M.shape;M[M==5]=0;M[M==6]=0
rng=np.random.default_rng(42)
def noise(n,scales=((90,1),(37,.45),(13,.18)),seed=0):
    r=np.random.default_rng(seed);t=np.arange(n);out=np.zeros(n)
    for s,a in scales: out+=a*np.sin(t/s*2*np.pi/3+r.random()*6.28)+a*.5*np.sin(t/s*1.7*np.pi/3+r.random()*6.28)
    return out/ (sum(a for _,a in scales)*1.5)
F=7   # bosque (tierra inventada)
inv=np.zeros_like(M,bool)       # tierra inventada
def land(mask):
    m=mask&(M==0);M[m]=F;inv[m]=True
rows=np.arange(H)[:,None];cols=np.arange(W)[None,:]
# costa norte
en=(300+55*noise(W,seed=1)).astype(int)
land(rows<en[None,:])
# costa este
ee=(2050+55*noise(H,seed=2)).astype(int)
land(cols>=ee[:,None])
# costa sur (deja libre la salida a la izquierda)
es=(H-60-18*noise(W,seed=3)).astype(int)
land((rows>=es[None,:])&(cols>420))
def blob(cx,cy,rx,ry,seed,amp=.18):
    a=np.arctan2((rows-cy)/ry,(cols-cx)/rx);rr=np.hypot((rows-cy)/ry,(cols-cx)/rx)
    r=np.random.default_rng(seed);k=1.0
    for f in (2,3,5,8):k=k+amp/f*1.6*np.sin(f*a+r.random()*6.28)
    return rr<k
def carve(mask):M[mask]=0;inv[mask]=False
# faro: península desde la costa norte
e0=en[1700];wob=(9*np.sin(rows/23.0)+5*np.sin(rows/9.0+1.3))
pen=(abs(cols-1700+wob)<72-(rows-e0)*0.13)&(rows<e0+262)&(rows>=e0-20)
pen|=blob(1700,e0+266,46,40,31,.12)
land(pen);faro=(1700,int(e0+284))
# cala escondida en la costa norte (botella)
cn=1350;top=en[cn]
carve((abs(cols-cn)<18)&(rows<top+5)&(rows>top-150))
bulb_n=blob(cn,top-200,75,60,11,.1);carve(bulb_n)
# islas grandes
A=blob(1650,3350,330,700,21);land(A)
B=blob(1650,1250,240,360,22);land(B)
C=blob(1790,4780,170,220,23);land(C)
# cala paradisíaca dentro de la isla A (canal desde el este)
carve((abs(rows-3350)<16)&(cols>1700)&(cols<2000));pc=blob(1700,3350,62,55,31,.08);carve(pc)
# cala en la isla B (desde el norte)
carve((abs(cols-1650)<15)&(rows>820)&(rows<1150));cb=blob(1650,1180,50,45,32,.08);carve(cb)
# ensenadas en la costa este
ens=[]
for r0,L,mw,bw,seed in [(4400,150,20,75,41),(3500,130,18,65,42),(1800,150,20,75,43),(800,120,17,60,44)]:
    x0=ee[r0]-5;carve((abs(rows-r0)<mw)&(cols>=x0-10)&(cols<x0+L));bl=blob(x0+L+50,r0,bw,bw*.8,seed,.1);carve(bl);ens.append((x0+L+50,r0,bw))
# laguna con islita de palmeras y chicas (costa este, entrada estrecha)
lr=2600;x0=ee[lr]-5;carve((abs(rows-lr)<16)&(cols>=x0-10)&(cols<x0+90));lag=blob(x0+200,lr,125,115,51,.08);carve(lag)
islet=blob(x0+200,lr,28,22,52,.05);land(islet);isl=(x0+200,lr)
# arena: playas en calas, islas e islita; urbanizaciones en partes de la costa inventada
dist=cv2.distanceTransform((M==0).astype(np.uint8)^1,cv2.DIST_L2,5)   # distancia de tierra al agua
near=(dist<14)&inv
beachzones=np.zeros_like(M,bool)
for (cx,cy,rr) in [(cn,top-200,110),(1700,3350,90),(1650,1180,80),(isl[0],isl[1],60)]+[(e[0],e[1],e[2]+30) for e in ens]:
    beachzones|=np.hypot(rows-cy,cols-cx)<rr
beachzones|=(A&((rows>3700)|(cols<1450)))|(B&(rows>1450))|C
M[near&beachzones]=2
M[islet]=2
urb=inv&(M==F)&(((cols>2250)&((rows>3800)|((rows>1200)&(rows<1600))))|((rows<330)&(cols<1200))|((rows>H-120)&(cols<1600)))
M[urb]=4
# premios escondidos (coordenadas del mundo)
TOP=520-H*3
def w(c,r):return [int(c*3+1.5),int(TOP+r*3+1.5)]
def water(c,r,m=6):c,r=int(c),int(r);return 0<=r<H and 0<=c<W and (M[max(0,r-m):r+m+1,max(0,c-m):c+m+1]==0).all()
spots={'gear':[],'heart':[],'can':[],'coins':[],'girls':[],'palms':[],'faro':w(*faro)}
def pick(c,r,kind,tries=200,rad=40):
    for t in range(tries):
        R=rad+t;cc=c+rng.integers(-R,R+1) if t else c;rr=r+rng.integers(-R,R+1) if t else r
        if water(cc,rr):spots[kind].append(w(cc,rr));return True
    return False
pick(cn,top-230,'gear')                 # fondo de la cala norte
pick(1700,3350,'gear')                  # cala paradisíaca de la isla A
pick(1650,1170,'gear')                  # cala de la isla B
pick(isl[0]+45,isl[1]+30,'gear')        # junto a la islita
pick(ens[0][0]+40,ens[0][1],'gear')     # fondo de la ensenada sur
pick(ens[3][0]+30,ens[3][1],'gear')     # fondo de la ensenada norte
pick(faro[0]+90,faro[1]-80,'gear')      # detrás del faro
pick(1990,4780,'gear',rad=50)            # detrás de la isla C
for (c,r) in [(cn,top-160),(1700,3300),(ens[1][0]+20,ens[1][1]),(ens[2][0]+20,ens[2][1]),(isl[0]-60,isl[1]),(1990,1250)]:pick(c,r,'heart')
for (c,r) in [(cn-30,top-200),(1740,3380),(ens[0][0],ens[0][1]+30),(ens[2][0],ens[2][1]-30),(1650,1220),(isl[0],isl[1]-60),(faro[0]-90,faro[1]),(1380,3350)]:pick(c,r,'can')
for (c,r) in [(cn,top-120),(1680,3330),(1660,1150),(isl[0]+70,isl[1]),(ens[1][0],ens[1][1]),(ens[3][0],ens[3][1]),(1980,4700),(2000,2000),(1300,2400)]:pick(c,r,'coins')
for k in range(4):a=k/4*6.28+.5;spots['girls'].append(w(isl[0]+np.cos(a)*14,isl[1]+np.sin(a)*10))
for k in range(5):a=k/5*6.28;spots['palms'].append(w(isl[0]+np.cos(a)*20,isl[1]+np.sin(a)*13))
print({k:(len(v) if isinstance(v,list) and v and isinstance(v[0],list) else v) for k,v in spots.items()})
im=Image.fromarray((M*36).astype(np.uint8),'L');b=io.BytesIO();im.save(b,'PNG',optimize=True)
cor=[W*3]*len(d['cor'])
json.dump({'w':W,'h':H,'cor':cor,'spots':spots,'src':'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()},open('realmap4.json','w'))
pal=np.zeros((9,3),np.uint8);pal[0]=[30,120,200];pal[1]=[196,124,70];pal[2]=[243,220,174];pal[3]=[150,190,90];pal[4]=[226,220,208];pal[7]=[70,120,60]
vis=pal[M];sm=cv2.resize(vis,(W//4,H//4),interpolation=cv2.INTER_AREA)
for k,v in spots.items():
    if k in('faro',):v=[v]
    col={'gear':(255,0,255),'heart':(255,60,60),'can':(0,255,255),'coins':(255,215,0),'girls':(255,120,200),'palms':(0,90,0),'faro':(255,255,255)}[k]
    for x,y in v:cv2.circle(sm,(int(x/3/4),int((y-TOP)/3/4)),3,col,-1)
Image.fromarray(sm).save('lake_vis.png');print('png KB',len(b.getvalue())//1024,sm.shape)
