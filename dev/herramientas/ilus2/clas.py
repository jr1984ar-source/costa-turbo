import cv2,numpy as np
m=cv2.imread('marcado_reg.png'); c=cv2.imread('limpio.jpg')
hm=cv2.cvtColor(m,cv2.COLOR_BGR2HSV).astype(np.float32); H=hm[...,0]*2;S=hm[...,1]/255;V=hm[...,2]/255
hc=cv2.cvtColor(c,cv2.COLOR_BGR2HSV).astype(np.float32); Hc=hc[...,0]*2;Sc=hc[...,1]/255;Vc=hc[...,2]/255
cut=cv2.imread('../ilus/ilus_cut.png',cv2.IMREAD_UNCHANGED); on=np.zeros(m.shape[:2],bool); on[69:69+668,24:24+1272]=cut[...,3]>100
Lc=(c[...,2]*.299+c[...,1]*.587+c[...,0]*.114)/255
redc=on&(Sc>.4)&((Hc<30)|(Hc>330))
K=np.zeros(m.shape[:2],np.uint8)  # marked class: 0 none,1 blue,2 red,3 green,4 orange,5 purple,7 white/sticker
sat=on&(S>.3)&(V>.25)
K[sat&((H<22)|(H>338))]=2
K[sat&(H>=22)&(H<60)]=4
K[sat&(H>=75)&(H<150)]=3
K[sat&(H>=185)&(H<250)]=1
K[sat&(H>=270)&(H<335)]=5
K[on&(S<.25)&(V>.75)]=7
vis=np.zeros_like(m); COL={1:(255,120,40),2:(40,40,230),3:(40,200,40),4:(0,160,255),5:(200,40,180),7:(255,255,255)}
for k,v in COL.items(): vis[K==k]=v
vis[(K==0)&on]=(60,60,60)
cv2.imwrite('K.png',vis); np.save('K.npy',K); np.save('redc.npy',redc); np.save('on.npy',on)
print({k:int((K==k).sum()) for k in range(8)})
# mirrors: marked red but original dark
mr=(K==2)&~redc&on; print('red over dark',mr.sum())
cv2.imwrite('mirror.png',(mr*255).astype(np.uint8))
