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
    r,c=q.popleft();d=D[r,c]+1
    for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
        rr,cc=r+dr,c+dc
        if 0<=rr<H and 0<=cc<W and wat[rr,cc] and D[rr,cc]<0:D[rr,cc]=d;q.append((rr,cc))
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
for (c,r) in [(cn,top-160),(1700,3300),(ens[1][0],ens[1][1]),(ens[3][0],ens[3][1]),(isl[0]-60,isl[1]),(bays[1][0],bays[1][1])]:pick(c,r,'heart')
for (c,r) in [(cn-30,top-200),(1740,3380),(ens[0][0],ens[0][1]),(ens[2][0],ens[2][1]),(1650,1220),(isl[0],isl[1]-60),(faro[0]-90,faro[1]),(ens[5][0],ens[5][1])]:pick(c,r,'can')
for (c,r) in [(cn,top-120),(1680,3330),(1660,1150),(isl[0]+70,isl[1]),(bays[0][0],bays[0][1]),(bays[2][0],bays[2][1]),(ens[4][0],ens[4][1]),(ens[6][0],ens[6][1]),(1990,4700)]:pick(c,r,'coins')
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
ringB=cv2.dilate(B.astype(np.uint8),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(181,181)))
cs,_=cv2.findContours(ringB,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE);cn_=max(cs,key=len)[:,0,:]
step=max(1,len(cn_)//70);path=[w(p[0],p[1]) for p in cn_[::step]]
okp=all(water(p[0],p[1],10) for p in cn_[::step]);print('piri ok',okp,len(path))
spots['piri']=path
