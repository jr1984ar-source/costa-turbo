import cv2,numpy as np,glob,json,base64,io
from PIL import Image
U=3.9                     # unidades del juego por metro (pantalla de 390 = 100 m)
MW={1:126,2:263,3:275,4:520,5:520,6:455,7:445}   # metros de ancho de cada captura (barra de escala)
CELL=3;rng=np.random.default_rng(11)
def load(i):
    land=(cv2.imread(f'tierra{i}.png',0)>0).astype(np.uint8)
    clean=cv2.resize(cv2.imread(f'clean{i}.jpg'),(land.shape[1],land.shape[0]))
    hsv=cv2.cvtColor(clean,cv2.COLOR_BGR2HSV).astype(np.float32);h=hsv[...,0]*2;s=hsv[...,1]/255;v=hsv[...,2]/255
    k=MW[i]*U/1206/CELL                      # celdas por píxel
    W=int(1206*k);H=int(land.shape[0]*k)
    rs=lambda a:cv2.resize(a.astype(np.float32),(W,H),interpolation=cv2.INTER_LINEAR)
    L=cv2.GaussianBlur(rs(land),(0,0),1.2)>.5;h,s,v=rs(h),rs(s),rs(v)
    cls=np.ones((H,W),np.uint8);cls[(s<.12)&(v>.45)]=4;cls[(h>=20)&(h<=60)&(s<.42)&(v>.62)]=2;cls[(h>=60)&(h<=170)&(s>.12)]=3
    cls=cv2.medianBlur(cls,5);cls[~L]=0
    # orilla principal (la tierra que toca la izquierda), para alinear las capturas
    n,l=cv2.connectedComponents(L.astype(np.uint8));left=set(np.unique(l[:,0]))-{0}
    main=np.isin(l,list(left)) if left else L
    sh=np.array([(np.where(main[r])[0].max() if main[r].any() else 0) for r in range(H)])
    return cls,sh
secs=[load(i) for i in range(1,8)]
X0=40                                          # dónde queda la orilla de referencia (celdas)
def place(cls,sh):
    off=X0-int(np.median(sh[sh>0])) if (sh>0).any() else 0     # mover para que la orilla quede en X0
    return cls,sh,off
P=[place(*s) for s in secs]
minoff=min(p[2] for p in P);
WMAX=max(p[0].shape[1]+p[2]-minoff for p in P)+20
def put(cls,off):
    out=np.zeros((cls.shape[0],WMAX),np.uint8);x=off-minoff
    if x>=0: w=min(cls.shape[1],WMAX-x);out[:,x:x+w]=cls[:,:w]
    else: out[:,:cls.shape[1]+x]=cls[:,-x:]
    xe=max(1,x if x>0 else 1)
    fill=np.where(rng.random((cls.shape[0],xe))<.45,3,1).astype(np.uint8);fill=cv2.medianBlur(fill,5)
    blk=out[:,:xe];blk[blk==0]=fill[blk==0]
    xs=max(1,X0-minoff-30);b2=out[:,:xs];b2[b2==0]=1
    return out
def shoreRow(c,row):
    r=np.where(c[row]>0)[0];return r.max() if len(r) else 0
def plain(n,a,b):
    c=np.zeros((n,WMAX),np.uint8)
    for r in range(n):
        t=1-r/(n-1);t=t*t*(3-2*t);x=int(max(8,b*(1-t)+a*t+4*np.sin(r/19)+2*np.sin(r/6)))
        c[r,:x]=np.where(rng.random(x)<.35,3,1)
    return cv2.medianBlur(c,5)
blocks=[put(p[0],p[2]) for p in P]
ref=X0-minoff
parts=[plain(300,shoreRow(blocks[0],blocks[0].shape[0]-1),ref)]
for k,b in enumerate(blocks):
    parts.append(b)
    if k<6: parts.append(plain(240,shoreRow(blocks[k+1],blocks[k+1].shape[0]-1),shoreRow(b,0)))
parts.append(plain(280,ref,shoreRow(blocks[-1],0)))
M=np.vstack(parts[::-1]);H,W=M.shape
# pasillo de carrera: hasta 230 celdas (≈177 m) mar adentro desde la orilla principal suavizada
main=np.array([shoreRow(M,r) for r in range(H)]).astype(float)
n,l=cv2.connectedComponents((M>0).astype(np.uint8));left=set(np.unique(l[:,0]))-{0}
mm=np.isin(l,list(left));ms=np.array([(np.where(mm[r])[0].max() if mm[r].any() else 0) for r in range(H)]).astype(float)
ms=np.convolve(np.pad(ms,150,mode='edge'),np.ones(301)/301,mode='valid')
lm=np.zeros(H)
for r in range(H):
    xs=np.where((M[r]>0)&(M[r]<5))[0];xs=xs[xs<ms[r]+450];lm[r]=xs.max() if len(xs) else 0
raw=np.maximum(ms+170,lm+120)
from scipy.ndimage import maximum_filter1d,uniform_filter1d
cor=np.clip(uniform_filter1d(maximum_filter1d(raw,201),151),0,W-1).astype(int)
for r in range(H): M[r,cor[r]:]=np.where(M[r,cor[r]:]==0,6,M[r,cor[r]:])
# agua sin salida hacia arriba (la IA no entra): 5
good=np.zeros_like(M,bool);good[0]=M[0]==0
for r in range(1,H):
    w=M[r]==0;lab=cv2.connectedComponents(w.astype(np.uint8)[None,:],connectivity=4)[1][0]
    ids=np.unique(lab[w&good[r-1]]);ids=[i for i in ids if i>0 and (lab==i).sum()>=22]
    good[r]=np.isin(lab,ids)&w
M[(M==0)&~good]=5
wid=[]
for r in range(0,H,8):
    w=(M[r]==0).astype(np.int8);d=np.diff(np.concatenate([[0],w,[0]]));st=np.where(d==1)[0];en=np.where(d==-1)[0];wid.append((en-st).max()*CELL if len(st) else 0)
wid=np.array(wid);print('celdas',W,'x',H,'=> unidades',W*CELL,'x',H*CELL,'canal min',wid.min(),'filas<150u',(wid<150).sum())
im=Image.fromarray((M*36).astype(np.uint8),'L');b=io.BytesIO();im.save(b,'PNG',optimize=True)
json.dump({'w':W,'h':H,'cell':CELL,'cor':(cor*CELL).tolist()[::4],'src':'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()},open('realmap2.json','w'))
pal=np.array([[30,120,200],[196,124,70],[243,220,174],[86,140,70],[226,220,208],[60,150,220],[10,60,120]],np.uint8)
Image.fromarray(pal[M]).save('realmap2_vis.png');print('png KB',len(b.getvalue())//1024)
