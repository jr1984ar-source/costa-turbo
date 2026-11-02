import json,base64,io,numpy as np,cv2
from PIL import Image
d=json.load(open('realmap3.json'));M=np.array(Image.open(io.BytesIO(base64.b64decode(d['src'].split(',')[1])))).astype(np.int32)
M=np.rint(M/36).astype(np.uint8);H,W=M.shape;M[M==5]=0;M[M==6]=0
# lado derecho: la costa real del lado izquierdo girada 180° (mismo estilo de calles, chalets y calas)
W2=2740;S=M[:,:520][::-1,::-1];M2=np.zeros((H,W2),np.uint8);M2[:,:W]=M;reg=M2[:,W2-520:];reg[S>0]=S[S>0];M=M2;W=W2
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
# costa sur
es=(H-60-18*noise(W,seed=3)).astype(int)
land(rows>=es[None,:])   # cerrado del todo (también junto a la salida)
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
# canal navegable alrededor de las islas
for I in (A,B,C):
    ring=cv2.dilate(I.astype(np.uint8),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(91,91)))>0
    carve(ring&~I&(cols>1500))
landm=M>0
def shoreE(r,c0=2000):
    row=landm[r]
    for c in range(c0,W-30):
        if row[c:c+30].all():return c
def cove(x0,r0,depth,w0,w1,bulb,seed,ang=0.0):
    r=np.random.default_rng(seed);x=float(x0);y=float(r0);a=ang
    mk=np.zeros((H,W),np.uint8);n=int(depth/3)
    for k in range(n+1):
        t=k/max(1,n);wd=w0+(w1-w0)*t
        cv2.circle(mk,(int(x),int(y)),max(2,int(wd/2)),1,-1)
        a=float(np.clip(a+r.normal(0,.14),ang-.7,ang+.7));x+=3*np.cos(a);y+=3*np.sin(a)
    bc=(x+bulb*.55*np.cos(a),y+bulb*.55*np.sin(a))
    bl=blob(bc[0],bc[1],bulb,bulb*r.uniform(.75,1.0),seed+100,.12)
    return bc,(mk>0)|bl,bl
# calas escondidas entre bosques en la costa de la derecha (acaban en playita)
calas=[];woods=np.zeros_like(inv)
for r0,dep,w0,w1,bu,sd,an in [(1000,95,24,15,40,61,.2),(2150,105,24,15,42,63,-.25),(3350,95,26,16,40,64,.25),(4550,100,24,15,40,66,-.2)]:
    e=shoreE(r0)
    if e is None or e+dep+bu*2>W-25:print('cala sin sitio',r0,e);continue
    bc,m,bl=cove(e-25,r0,dep,w0,w1,bu,sd,an);carve(m);calas.append((bc[0],bc[1],bu,bl))
    woods|=(cv2.dilate(m.astype(np.uint8),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(111,111)))>0)
# laguna escondida en la esquina de arriba a la derecha, con islita de palmeras y chicas
cL=2330;e0=int(en[cL]);rr_=np.random.default_rng(81);x=float(cL);y=float(e0+25);a=-np.pi/2
mk=np.zeros((H,W),np.uint8)
for k in range(28):
    cv2.circle(mk,(int(x),int(y)),15,1,-1);a=float(np.clip(a+rr_.normal(0,.13),-np.pi/2-.6,-np.pi/2+.6));x+=3*np.cos(a);y+=3*np.sin(a)
carve(mk>0);lc=(x,y-70);lag=blob(lc[0],lc[1],100,75,51,.08);carve(lag)
islet=blob(lc[0],lc[1],28,22,52,.05);land(islet);isl=(int(lc[0]),int(lc[1]))
woods|=(cv2.dilate((lag|(mk>0)).astype(np.uint8),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(101,101)))>0)
ens=[(c[0],c[1],c[2]) for c in calas]
# bosque alrededor de calas y laguna
M[woods&(M>0)&(M!=2)&~islet]=F
# arena
dist=cv2.distanceTransform((M==0).astype(np.uint8)^1,cv2.DIST_L2,5)
beachzones=np.zeros_like(M,bool)
for (cx,cy,rr) in [(cn,top-200,110),(1700,3350,90),(1650,1180,80),(isl[0],isl[1],60)]:
    beachzones|=np.hypot(rows-cy,cols-cx)<rr
beachzones|=(A&((rows>3700)|(cols<1450)))|(B&(rows>1450))|C
for (cx,cy,bu,bl) in calas:beachzones|=(np.hypot(rows-cy,cols-cx)<bu*1.2)&(cols>cx-bu*.2)
M[(dist<14)&beachzones&(M>0)&((M==F)|inv)]=2
M[islet]=2
urb=inv&(M==F)&(((rows<330)&(cols<1200))|((rows>H-120)&(cols<1600)))
M[urb]=4
# premios escondidos (coordenadas del mundo)
TOP=520-H*3
def w(c,r):return [int(c*3+1.5),int(TOP+r*3+1.5)]
def water(c,r,m=6):c,r=int(c),int(r);return 0<=r<H and 0<=c<W and (M[max(0,r-m):r+m+1,max(0,c-m):c+m+1]==0).all()
spots={'gear':[],'gold':None,'heart':[],'can':[],'coins':[],'girls':[],'palms':[],'faro':w(*faro)}
def pick(c,r,kind,tries=200,rad=40):
    for t in range(tries):
        R=rad+t;cc=c+rng.integers(-R,R+1) if t else c;rr=r+rng.integers(-R,R+1) if t else r
        if water(cc,rr):
            if kind=='gold':spots['gold']=w(cc,rr)
            else:spots[kind].append(w(cc,rr))
            return True
    return False
# distancia navegando desde la salida (para el sitio más escondido)
from collections import deque
wat=cv2.erode((M==0).astype(np.uint8),np.ones((9,9),np.uint8))>0
sc,sr=273,5568
D=np.full((H,W),-1,np.int32);q=deque()
ys,xs=np.nonzero(wat[sr-60:sr+60,sc-60:sc+60]);D[sr-60+ys[0],sc-60+xs[0]]=0;q.append((sr-60+ys[0],sc-60+xs[0]))
while q:
    r,c=q.popleft();dd=D[r,c]+1
    for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
        rr,cc=r+dr,c+dc
        if 0<=rr<H and 0<=cc<W and wat[rr,cc] and D[rr,cc]<0:D[rr,cc]=dd;q.append((rr,cc))
ends=[(cc[0]+cc[2]*.3,cc[1]) for cc in calas]+[(cn,top-230)]
def gd(c,r):
    c,r=int(c),int(r);win=D[max(0,r-25):r+26,max(0,c-25):c+26];return win.max()
far=max(ends,key=lambda e:gd(*e));print('oro en',far,gd(*far))
pick(far[0],far[1],'gold')
rest=[e for e in ends if e!=far]
pick(cn,top-230,'gear') if far!=(cn,top-230) else None
pick(1700,3350,'gear')                  # cala paradisíaca de la isla A
pick(1650,1170,'gear')                  # cala de la isla B
pick(isl[0]+45,isl[1]+30,'gear')        # junto a la islita
pick(faro[0]+90,faro[1]-80,'gear')      # detrás del faro
for e in [e for e in rest if e!=(cn,top-230)][:8-len(spots['gear'])]:pick(e[0],e[1],'gear')
for (c,r) in [(cn,top-160),(1700,3300),(ens[0][0],ens[0][1]),(ens[2][0],ens[2][1]),(isl[0]-50,isl[1]),(1990,1250)]:pick(c,r,'heart')
for (c,r) in [(cn-30,top-200),(1740,3380),(ens[1][0],ens[1][1]),(ens[3][0],ens[3][1]),(1650,1220),(isl[0],isl[1]+50),(faro[0]-90,faro[1]),(1380,3350)]:pick(c,r,'can')
for (c,r) in [(cn,top-120),(1680,3330),(1660,1150),(isl[0]+60,isl[1]),(ens[0][0],ens[0][1]),(ens[1][0],ens[1][1]),(ens[2][0],ens[2][1]),(ens[3][0],ens[3][1]),(1990,4700)]:pick(c,r,'coins')
for k in range(4):a=k/4*6.28+.5;spots['girls'].append(w(isl[0]+np.cos(a)*14,isl[1]+np.sin(a)*10))
for k in range(5):a=k/5*6.28;spots['palms'].append(w(isl[0]+np.cos(a)*20,isl[1]+np.sin(a)*13))
# bares: Roxy en la punta norte, JJ en la costa izquierda al sur (junto a la salida)
def shoreN(c):
    for r in range(int(en[c])-40,H):
        if (M[r:r+12,c]==0).all():return r
rc=800;rr=shoreN(rc);spots['roxy']=[int(rc*3+1.5),int(TOP+rr*3)]
best=None
for r in range(5150,5560,5):
    sc_=[next((c for c in range(0,600) if (M[r2,c:c+15]==0).all()),None) for r2 in range(r-25,r+26,5)]
    if None in sc_:continue
    sd=np.std(sc_);x=int(np.median(sc_))
    if (M[r-25:r+26,max(0,x-60):x-3]>0).mean()<.9:continue
    if best is None or sd<best[0]:best=(sd,r,x)
spots['jj']=[int(best[2]*3),int(TOP+best[1]*3)];print('jj',best)
# ruta del Piri-Piri: vuelta a la isla B
for RB in (91,111,71,61,131,51):
    ringB=cv2.dilate(B.astype(np.uint8),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*RB+1,2*RB+1)))
    cs,_=cv2.findContours(ringB,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE);cn_=max(cs,key=len)[:,0,:]
    step=max(1,len(cn_)//70);pts=cn_[::step];bad=[tuple(p) for p in pts if not water(p[0],p[1],10)]
    print('piri R',RB,'malos',len(bad),bad[:4])
    if not bad:break
path=[w(p[0],p[1]) for p in pts]
spots['piri']=path
print({k:(len(v) if isinstance(v,list) and v and isinstance(v[0],list) else v) for k,v in spots.items() if k!='piri'})
im=Image.fromarray((M*36).astype(np.uint8),'L');b=io.BytesIO();im.save(b,'PNG',optimize=True)
cor=[W*3]*len(d['cor'])
json.dump({'w':W,'h':H,'cor':cor,'spots':spots,'src':'data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()},open('realmap5.json','w'))
pal=np.zeros((9,3),np.uint8);pal[0]=[30,120,200];pal[1]=[196,124,70];pal[2]=[243,220,174];pal[3]=[150,190,90];pal[4]=[226,220,208];pal[7]=[70,120,60]
vis=pal[M];sm=cv2.resize(vis,(W//4,H//4),interpolation=cv2.INTER_AREA)
for k,v in spots.items():
    if k in('faro','gold','roxy','jj'):v=[v]
    col={'gear':(255,0,255),'gold':(255,170,0),'heart':(255,60,60),'can':(0,255,255),'coins':(255,215,0),'girls':(255,120,200),'palms':(0,90,0),'faro':(255,255,255),'roxy':(120,60,20),'jj':(200,0,0),'piri':(255,255,0)}[k]
    for x,y in v:cv2.circle(sm,(int(x/3/4),int((y-TOP)/3/4)),3,col,-1)
Image.fromarray(sm).save('lake_vis5.png');print('png KB',len(b.getvalue())//1024,sm.shape)
