import cv2,numpy as np,glob
for i in range(1,8):
    f=glob.glob(f'cap{i}.*')[0];im=cv2.imread(f);H,W=im.shape[:2]
    y0,y1=(420,1880) if i==1 else (560,1880)
    hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV).astype(np.float32);h=hsv[...,0]*2;s=hsv[...,1]/255;v=hsv[...,2]/255
    # letreros (blanco/negro), chinchetas de colores y botones: se tapan y se rellenan con lo de alrededor
    txt=((s<.2)&(v>.78))|(v<.08)
    pin=(s>.45)&(v>.5)&~((h>=150)&(h<=250))&~((h>=20)&(h<=60)&(s<.6))
    m=(txt|pin).astype(np.uint8);m=cv2.dilate(m,np.ones((7,7),np.uint8))
    m[1330:,1000:]=1; m[1470:,30:260]=1          # botones de abajo
    clean=cv2.inpaint(im,m,9,cv2.INPAINT_TELEA)
    clean=cv2.medianBlur(clean,15)
    hsv=cv2.cvtColor(clean,cv2.COLOR_BGR2HSV).astype(np.float32);h=hsv[...,0]*2;s=hsv[...,1]/255;v=hsv[...,2]/255
    water=((h>=160)&(h<=245)&(s>.14))
    land=(~water).astype(np.uint8)[y0:y1]
    land=cv2.morphologyEx(land,cv2.MORPH_OPEN,np.ones((9,9),np.uint8))
    n,l,st,_=cv2.connectedComponentsWithStats(land,connectivity=8);keep=np.zeros_like(land)
    for k in range(1,n):
        if st[k][4]>=2500: keep[l==k]=1
    inv=(1-keep).astype(np.uint8);n2,l2,st2,_=cv2.connectedComponentsWithStats(inv,connectivity=4)
    for k in range(1,n2):
        if st2[k][4]<4000: keep[l2==k]=1
    cv2.imwrite(f'tierra{i}.png',keep*255);cv2.imwrite(f'clean{i}.jpg',cv2.resize(clean[y0:y1],(W//3,(y1-y0)//3)))
    print(i,round(keep.mean(),3))
