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
