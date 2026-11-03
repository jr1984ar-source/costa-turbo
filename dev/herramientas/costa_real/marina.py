# puerto de Portals: espigón (8), pantalanes (9), amarres con barcos (10) y entrada más abierta
def marina(M):
    r0,r1,c0,c1=2985,3775,214,490
    sub=M[r0:r1,c0:c1];land=(sub>0).astype(np.uint8);l2=land.copy();l2[:38,:]=0;l2[:,:14]=0
    n,lab,st,cen=cv2.connectedComponentsWithStats(l2,8)
    win=lab[300:700,150:260];ids,cnt=np.unique(win[win>0],return_counts=True);bw=ids[cnt.argmax()]
    brk=(lab==bw);piers=[]
    for k in range(1,n):
        if k==bw:continue
        L,T,Wd,Hh,A=st[k]
        if L<=16 and T<345 and T+Hh<350 and A<9000:
            ys,xs=np.nonzero(lab==k);piers.append((int(np.median(ys)),int(xs.max())-4));sub[lab==k]=0
    # punta del espigón más corta y redondeada (entrada más abierta)
    tip=brk.copy();tip[:665,:]=False;sub[tip]=0;brk&=~tip
    brk=cv2.morphologyEx(brk.astype(np.uint8),cv2.MORPH_OPEN,cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(9,9)))>0
    sub[(sub==8)]=0;sub[brk]=8
    ys,xs=np.nonzero(brk);ty=ys.max();tx=int(xs[ys>=ty-3].mean());cv2.circle(sub,(tx,ty-3),6,8,-1);brk=sub==8
    # pantalanes rectos desde la orilla, con barcos amarrados por el lado sur
    rr=np.arange(sub.shape[0])[:,None];cc=np.arange(sub.shape[1])[None,:]
    band=np.zeros_like(brk)
    for (rc,xe) in sorted(piers):
        sub[rc-3:rc+4,:xe+1][sub[rc-3:rc+4,:xe+1]==0]=9
        band|=(rr>rc+3)&(rr<=rc+3+17)&(cc<xe-2)
    wat=(sub==0)
    bmin=np.where(brk.any(1),np.argmax(brk,1),9999)
    inside=cc<bmin[:,None]
    band2=(cv2.dilate(brk.astype(np.uint8),cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(33,33)))>0)&inside&(rr>=40)&(rr<540)
    sub[(band|band2)&wat]=10
    # gasolinera: dentro del puerto, junto al espigón cerca de la entrada
    gr=610;ge=int(bmin[gr]);gas=(r0+gr,c0+ge-34,r0+gr,c0+ge)
    return gas
