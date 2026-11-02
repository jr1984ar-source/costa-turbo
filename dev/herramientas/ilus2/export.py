import cv2,numpy as np,json,base64,io
from PIL import Image
OX,OY=24,69
lab0=np.load('lab.npy')
rgba=cv2.cvtColor(cv2.imread('../ilus/ilus_cut.png',cv2.IMREAD_UNCHANGED),cv2.COLOR_BGRA2RGBA)
H,W=rgba.shape[:2]
lab=lab0[OY:OY+H,OX:OX+W].copy(); lab[rgba[...,3]<=100]=0
rgb=rgba[...,:3].astype(np.float32); L=(rgb[...,0]*.299+rgb[...,1]*.587+rgb[...,2]*.114)/255
# suavizar el ruido del jpg fuera de las líneas
line=np.load('line.npy')[OY:OY+H,OX:OX+W]
Ls=cv2.medianBlur((L*255).astype(np.uint8),3).astype(np.float32)/255
L=np.where(line,L,Ls)
F=np.ones((H,W),np.float32); ref={}
for v in range(1,6):
    m=lab==v; md=float(np.median(L[m])); ref[v]=round(md,4); F[m]=L[m]/max(md,.02)
F=np.clip(F*90,0,255)
mp=np.dstack([(lab*36).astype(np.uint8),F.astype(np.uint8),np.zeros((H,W),np.uint8),np.full((H,W),255,np.uint8)])
out={'w':W,'h':H,'ref':ref}
b=io.BytesIO(); Image.fromarray(mp,'RGBA').save(b,'PNG',optimize=True); out['map']='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
b=io.BytesIO(); Image.fromarray(rgba,'RGBA').save(b,'WEBP',quality=88,method=6); out['img']='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
json.dump(out,open('ski_map2.json','w'))
# logo pequeño + transformaciones afines (coordenadas del recorte)
lg=Image.open('riva_logo.png').convert('RGBA'); LW,LH=456,137
lgs=lg.resize((LW,LH),Image.LANCZOS); b=io.BytesIO(); lgs.save(b,'PNG',optimize=True)
logo='data:image/png;base64,'+base64.b64encode(b.getvalue()).decode()
aff={}
for n in ['rear','front']:
    Hm=np.load('H%s.npy'%n)
    src=np.float32([[0,0],[1825,0],[1825,549],[0,549]]).reshape(-1,1,2)
    dst=cv2.perspectiveTransform(src,Hm).reshape(-1,2)-np.float32([OX,OY])
    s2=np.float32([[0,0],[LW,0],[LW,LH],[0,LH]])
    A,_=cv2.estimateAffine2D(s2,dst,method=cv2.LMEDS)
    aff[n]=[round(float(A[0,0]),4),round(float(A[1,0]),4),round(float(A[0,1]),4),round(float(A[1,1]),4),round(float(A[0,2]),1),round(float(A[1,2]),1)]
    print(n,np.round(dst,1).tolist(),aff[n])
json.dump({'logo':logo,'aff':aff},open('riva2.json','w'))
print('ref',ref,'map',len(out['map']),'img',len(out['img']),'logo',len(logo))
