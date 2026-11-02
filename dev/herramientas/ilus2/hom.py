import cv2,numpy as np
lg=cv2.imread('riva_logo.png',cv2.IMREAD_UNCHANGED); print(lg.shape, np.unique(lg[...,3])[:5], (lg[...,3]==0).mean())
a=lg[...,3:4]/255.; flat=(lg[...,:3]*a+255*(1-a)).astype(np.uint8)
m=cv2.imread('mapa_marcado.jpg')  # use the original-resolution marked image
sift=cv2.SIFT_create(4000)
g1=cv2.cvtColor(cv2.resize(flat,(600,int(600*549/1825))),cv2.COLOR_BGR2GRAY); sc=600/1825
k1,d1=sift.detectAndCompute(g1,None)
M=np.load('M.npy')
res={}
for name,(x0,y0,x1,y1) in {'rear':(375,285,537,417),'front':(901,406,1057,550)}.items():
    # bbox in original marked coords
    Mi=cv2.invertAffineTransform(M)
    p=cv2.transform(np.array([[[x0-30,y0-30]],[[x1+30,y1+30]]],np.float32),Mi).reshape(-1,2)
    X0,Y0=p[0].astype(int);X1,Y1=p[1].astype(int)
    crop=m[Y0:Y1,X0:X1]; g2=cv2.cvtColor(cv2.resize(crop,None,fx=3,fy=3,interpolation=cv2.INTER_CUBIC),cv2.COLOR_BGR2GRAY)
    k2,d2=sift.detectAndCompute(g2,None)
    bf=cv2.BFMatcher(); mt=bf.knnMatch(d1,d2,k=2); good=[a for a,b in mt if a.distance<.75*b.distance]
    src=np.float32([k1[g.queryIdx].pt for g in good])/sc
    dst=np.float32([k2[g.trainIdx].pt for g in good])/3+np.float32([X0,Y0])
    Hh,inl=cv2.findHomography(src,dst,cv2.RANSAC,4.0)
    print(name,len(good),int(inl.sum()))
    # compose with M (orig marked -> registered 1307x800)
    A=np.vstack([M,[0,0,1]]); Ht=A@Hh
    res[name]=Ht
    corners=np.float32([[0,0],[1825,0],[1825,549],[0,549]]).reshape(-1,1,2)
    print(np.round(cv2.perspectiveTransform(corners,Ht).reshape(-1,2),1))
np.save('Hrear.npy',res['rear']);np.save('Hfront.npy',res['front'])
