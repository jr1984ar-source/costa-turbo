# ---- zonas del lago: 1 agua profunda, 2 tropical (tipo Bahamas), 3 pueblo ----
zr=np.random.default_rng(401)
tro=blob(1950,4950,430,560,401,.15)
wdist=cv2.distanceTransform((M==0).astype(np.uint8),cv2.DIST_L2,5)
cays=[]
for t in range(400):
    if len(cays)>=6:break
    c=int(1950+zr.uniform(-330,330));r=int(4950+zr.uniform(-430,430))
    if not tro[r,c] or wdist[r,c]<70:continue
    if any(np.hypot(c-a,r-b)<170 for a,b,_ in cays):continue
    rad=int(zr.uniform(10,17));m=blob(c,r,rad*1.3,rad,410+t,.2)&(M==0);M[m]=2;cays.append((c,r,rad))
pigc=max(cays,key=lambda q:q[2])
wdist=cv2.distanceTransform((M==0).astype(np.uint8),cv2.DIST_L2,5)
sb=[]
for t in range(600):
    if len(sb)>=9:break
    c=int(1950+zr.uniform(-380,380));r=int(4950+zr.uniform(-480,480))
    if not tro[r,c] or wdist[r,c]<55:continue
    if any(np.hypot(c-q[0],r-q[1])<120 for q in sb):continue
    sb.append((c,r,zr.uniform(22,42),zr.uniform(12,22),zr.uniform(0,3.14)))
deep=(wdist>115)&(rows<3300)&~tro
town=(M==4)&(rows<420)&(cols>250)&(cols<1350)
ZN=np.zeros((H,W),np.uint8);ZN[deep]=1;ZN[tro&(M==0)]=2;ZN[town]=3
S8=8;Hz=(H+S8-1)//S8;Wz=(W+S8-1)//S8;pad=np.zeros((Hz*S8,Wz*S8),np.uint8);pad[:H,:W]=ZN
blocks=pad.reshape(Hz,S8,Wz,S8).transpose(0,2,1,3).reshape(Hz,Wz,S8*S8)
cnt=np.stack([(blocks==k).sum(-1) for k in range(4)],-1);ZS=cnt.argmax(-1).astype(np.uint8)
zim=Image.fromarray((ZS*60).astype(np.uint8),'L');zb=io.BytesIO();zim.save(zb,'PNG',optimize=True)
