import cv2,numpy as np
from scipy import ndimage as ndi
c=cv2.imread('limpio.jpg');K=np.load('K.npy');on=np.load('on.npy')
H_,W_=K.shape
hc=cv2.cvtColor(c,cv2.COLOR_BGR2HSV).astype(np.float32); Hc=hc[...,0]*2;Sc=hc[...,1]/255
L=(c[...,2]*.299+c[...,1]*.587+c[...,0]*.114)/255
redh=(Hc<30)|(Hc>330)
strong=(on&redh&(Sc>.45)).astype(np.float32)
frac=cv2.blur(strong,(7,7))
redc=on&redh&(Sc>.25)&(L>.05)&((strong>0)|(frac>.15))   # piel roja (incluye bordes suaves, sin motas sueltas)
dark0=(on&~redc&(L<.11)).astype(np.uint8)
thick=cv2.morphologyEx(dark0,cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7)))
thick=cv2.dilate(thick,np.ones((3,3),np.uint8))>0
line=(dark0>0)&~thick
nl,ll,stl,_=cv2.connectedComponentsWithStats(line.astype(np.uint8),connectivity=8)
small=np.zeros(nl,bool); small[1:]=stl[1:,4]<40
line&=~small[ll]
np.save('line.npy',line)
lg=cv2.imread('riva_logo.png',cv2.IMREAD_UNCHANGED); al=(lg[...,3]>0).astype(np.uint8)*255
LG=np.zeros((H_,W_),np.uint8)
for n in ['rear','front']:
    LG|=cv2.warpPerspective(al,np.load('H%s.npy'%n),(W_,H_))
LG=cv2.dilate(LG,np.ones((7,7),np.uint8))>0
PL=np.zeros((H_,W_),np.uint8)
cv2.fillPoly(PL,[np.array([[301,415],[546,536],[542,583],[303,462]],np.int32)],1)
PL=cv2.dilate(PL,np.ones((7,7),np.uint8))>0
SM=(LG|PL)&on
lab=np.zeros((H_,W_),np.uint8)
# piel roja: 1 si marcado azul, si no 2
lab[redc]=np.where(K[redc]==1,1,2)
lab[redc&LG]=2
lab[redc&PL]=1
# piezas oscuras
dk=on&~redc&~line
kd=K[dk]; v=np.full(kd.shape,6,np.uint8)
for k in (2,3,4,5): v[kd==k]=k
lab[dk]=v
lab[line]=6
lab[dk&SM]=0
# piel roja: cada zona cerrada del dibujo entera a casco abajo o arriba
nr,cr=cv2.connectedComponents(redc.astype(np.uint8),connectivity=4)
rs=redc&~SM
c1=np.bincount(cr[rs],weights=(K[rs]==1).astype(float),minlength=nr); ct=np.bincount(cr[rs],minlength=nr)
f1=c1/np.maximum(ct,1)
whole1=(f1>=.6)&(ct>0); whole2=(f1<=.25)&(ct>0); whole1[0]=whole2[0]=False
lab[redc&whole1[cr]]=1; lab[redc&whole2[cr]&~PL]=2
mix=redc&~whole1[cr]&~whole2[cr]&~SM
r1=cv2.GaussianBlur((lab==1).astype(np.float32),(0,0),2); r2=cv2.GaussianBlur((lab==2).astype(np.float32),(0,0),2)
lab[mix]=np.where(r1[mix]>r2[mix],1,2)
print('red comps',nr,'mixed px',int(mix.sum()))
# ajustar las piezas oscuras a las zonas cerradas del dibujo
reg=on&~line
n,cc=cv2.connectedComponents(reg.astype(np.uint8),connectivity=4)
dsel=dk&~SM&(lab>0)
cnt=np.zeros((n,8),np.int64); np.add.at(cnt,(cc[dsel],lab[dsel]),1)
tot=cnt[:,2:7].sum(1); best=cnt[:,2:7].argmax(1)+2; share=cnt[:,2:7].max(1)/np.maximum(tot,1)
ok=(tot>0)&(share>=.8); ok[0]=False
T=np.where(ok,best,0).astype(np.uint8)
sn=dk&ok[cc]; lab[sn]=T[cc[sn]]
# huecos: vecino más cercano
src=lab>0
d,(iy,ix)=ndi.distance_transform_edt(~src,return_indices=True)
m0=on&(lab==0); lab[m0]=lab[iy[m0],ix[m0]]
# bordes rojizos que quedarían rojos fijos: a la pieza roja más cercana
rd=on&((Hc<30)|(Hc>330))&(Sc>.18)&(hc[...,2]/255>.12)&(lab==6)&(frac>.15)
srcr=np.isin(lab,[1,2])&~rd
d,(iy,ix)=ndi.distance_transform_edt(~srcr,return_indices=True)
rd&=d<6; lab[rd]=lab[iy[rd],ix[rd]]
print('fringe fixed',int(rd.sum()))
# piezas oscuras pintadas de rojo: solo los dos retrovisores (zonas grandes)
m2=((lab==2)&~redc).astype(np.uint8)
n2,l2,st2,_=cv2.connectedComponentsWithStats(m2,connectivity=8)
big=np.zeros(n2,bool); big[1:]=st2[1:,4]>=1000
lab[(m2>0)&~big[l2]]=6
print('mirrors',int(big.sum()))
lab[~on]=0
np.save('lab.npy',lab); np.save('LG.npy',LG); np.save('PL.npy',PL)
print('snapped',int(ok.sum()),{k:int((lab==k).sum()) for k in range(7)})
vis=c.astype(np.float32).copy()
COL={1:(255,120,40),2:(40,40,230),3:(40,200,40),4:(0,160,255),5:(200,40,180),6:(70,70,70)}
for k,col in COL.items():
    mm=lab==k; vis[mm]=vis[mm]*.25+np.array(col)*.75
cv2.imwrite('lab_vis.png',vis.astype(np.uint8))
