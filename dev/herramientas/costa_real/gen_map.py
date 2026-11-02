import cv2,numpy as np,glob,json,base64,io
from PIL import Image
GW=390;VS=2.0;rng=np.random.default_rng(11)
def load(i):
    land=(cv2.imread(f'tierra{i}.png',0)>0).astype(np.uint8)
    clean=cv2.resize(cv2.imread(f'clean{i}.jpg'),(land.shape[1],land.shape[0]))
    hsv=cv2.cvtColor(clean,cv2.COLOR_BGR2HSV).astype(np.float32);h=hsv[...,0]*2;s=hsv[...,1]/255;v=hsv[...,2]/255
    shore=np.array([(np.where(land[r])[0].max() if land[r].any() else 0) for r in range(land.shape[0])])
    med=np.median(shore[shore>0]);shift=int(max(0,med-380))
    def cut(a):
        a=a[:,shift:shift+1206];return np.pad(a,((0,0),(0,1206-a.shape[1]))) if a.shape[1]<1206 else a
    land,h,s,v=cut(land),cut(h),cut(s),cut(v)
    H=int(land.shape[0]*GW/1206*VS);rs=lambda a:cv2.resize(a.astype(np.float32),(GW,H))
    L=rs(land)>.5;h,s,v=rs(h),rs(s),rs(v)
    cls=np.ones((H,GW),np.uint8)                       # 1 roca
    cls[(s<.12)&(v>.45)]=4;cls[(h>=20)&(h<=60)&(s<.42)&(v>.62)]=2;cls[(h>=60)&(h<=170)&(s>.12)]=3
    cls=cv2.medianBlur(cls,9);cls[~L]=0
    sh=np.array([(np.where(L[r])[0].max() if L[r].any() else 0) for r in range(H)])
    ok=np.where(sh<230)[0];cls=cls[ok.min():ok.max()+1]
    cls[:, :20][cls[:, :20]==0]=1                       # siempre algo de costa a la izquierda
    return cls
def shoreOf(cls,row):
    r=np.where(cls[row]>0)[0];return min(190,r.max()) if len(r) else 30
def plain(n,a,b):                                         # tramo de costa de paso (fila 0 = arriba)
    c=np.zeros((n,GW),np.uint8)
    for r in range(n):
        t=1-r/(n-1);t=t*t*(3-2*t);x=int(max(26,b*(1-t)+a*t+9*np.sin(r/31)+5*np.sin(r/9)))
        c[r,:x]=1
        g=rng.random(x)<.35;c[r,:x][g]=3
    return cv2.medianBlur(c,7)
secs=[load(i) for i in range(1,8)]
parts=[plain(700,shoreOf(secs[0],secs[0].shape[0]-1),70)]   # entrada (abajo)
for k,s in enumerate(secs):
    parts.append(s)
    if k<6: parts.append(plain(600,shoreOf(secs[k+1],secs[k+1].shape[0]-1),shoreOf(s,0)))
parts.append(plain(650,70,shoreOf(secs[-1],0)))             # salida (arriba)
M=np.vstack(parts[::-1])                                     # arriba = meta
H=M.shape[0]
# agua sin salida hacia arriba (bahías cerradas): la IA no entra (valor 5)
good=np.zeros_like(M,bool);good[0]=M[0]==0
for r in range(1,H):
    w=M[r]==0;row=np.zeros(GW,bool)
    # tramos de agua de esta fila que tocan agua buena de la fila de arriba
    lab=cv2.connectedComponents(w.astype(np.uint8)[None,:],connectivity=4)[1][0]
    ids=np.unique(lab[w&good[r-1]]);ids=[i for i in ids if i>0 and (lab==i).sum()>=64]
    good[r]=np.isin(lab,ids)&w
M[(M==0)&~good]=5
# ancho del canal más ancho por fila (para revisar)
wid=[]
for r in range(0,H,10):
    w=(M[r]==0).astype(np.int8);runs=np.diff(np.concatenate([[0],w,[0]]));st=np.where(runs==1)[0];en=np.where(runs==-1)[0];wid.append((en-st).max() if len(st) else 0)
wid=np.array(wid);print('alto',H,'canal min',wid.min(),'p5',np.percentile(wid,5),'filas <120:',(wid<120).sum())
small=cv2.resize(M,(GW//2,H//2),interpolation=cv2.INTER_NEAREST)
im=Image.fromarray((small*40).astype(np.uint8),'L');b=io.BytesIO();im.save(b,'PNG',optimize=True)
src='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
json.dump({'w':GW//2,'h':H//2,'H':H,'src':src},open('realmap.json','w'))
vis=np.zeros((H,GW,3),np.uint8);pal=np.array([[30,120,200],[196,124,70],[243,220,174],[86,140,70],[226,220,208],[60,150,220]],np.uint8);vis=pal[M]
Image.fromarray(vis).save('realmap_vis.png');print('png',len(b.getvalue()))
