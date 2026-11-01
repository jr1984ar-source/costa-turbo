"""Piezas de la Yamaha roja y blanca: 1 casco abajo, 2 casco arriba, 3 tapa delantera, 4 detalles, 5 asiento, 6 negro fijo."""
import numpy as np, cv2
from masks import load, classes, polymask, below
SEAT=[(112,30),(118,6),(140,2),(172,14),(205,30),(240,46),(262,62),(266,86),(240,94),(200,90),(165,80),(135,64),(116,50)]
HOOD=[(318,96),(360,80),(400,74),(440,78),(470,108),(500,148),(530,190),(545,232),(520,246),(470,236),(420,214),(370,180),(330,140),(312,114)]
BAR=[(258,36),(300,30),(350,18),(372,16),(382,24),(372,40),(362,80),(330,92),(300,80),(270,52)]
DECK=[(60,82),(110,40),(200,62),(300,88),(334,98),(334,150),(250,138),(150,116),(80,112)]
RAIL=[(5,105),(100,145),(200,190),(260,212),(330,232),(420,252),(480,262),(540,268),(560,280)]
def build():
    rgba=load('brava');C,on=classes(rgba);sh=on.shape
    rgb=rgba[...,:3].astype(np.uint8);hsv=cv2.cvtColor(rgb,cv2.COLOR_RGB2HSV).astype(np.float32)
    S=hsv[...,1]/255;V=hsv[...,2]/255;Hh=hsv[...,0]*2
    red=on&(S>.38)&((Hh<28)|(Hh>320))&(V>.14)
    white=on&(S<.32)&(V>.58)
    black=on&(V<.3)&(S<.45)&~red
    seat=polymask(SEAT,sh);hood=polymask(HOOD,sh);low=below(RAIL,sh);bar=polymask(BAR,sh)
    lab=np.zeros(sh,np.uint8)
    lab[black]=6
    lab[low&red]=1
    lab[~low&red&~hood]=2
    lab[white&~seat]=4
    lab[polymask(DECK,sh)&white&~seat]=2
    lab[hood&(red|white)]=3
    lab[seat&on]=5
    sf=np.load('seat_front.npy').astype(np.int32);sfm=np.zeros(sh,np.uint8);cv2.fillPoly(sfm,[cv2.convexHull(sf)],1)
    lab[(sfm>0)&on&~black]=5
    lab[bar&on]=6
    from userblack import user_black
    UB=user_black()
    lab[UB]=6
    # píxeles sin pieza: toman la pieza más cercana
    unk=(lab==0)&on
    d,l=cv2.distanceTransformWithLabels((lab==0).astype(np.uint8),cv2.DIST_L2,3,labelType=cv2.DIST_LABEL_PIXEL)
    ys,xs=np.where(lab>0);lut=np.zeros(l.max()+1,np.uint8);lut[l[ys,xs]]=lab[ys,xs];lab[unk]=lut[l[unk]]
    st=np.stack([cv2.GaussianBlur((lab==v).astype(np.float32),(0,0),1.6) for v in range(7)],0)
    out=np.argmax(st,0).astype(np.uint8);out[UB]=6
    # correcciones del usuario sobre el ejemplo rosa y morado
    pk=np.load('mark_pink.npy').astype(np.uint8);gr=np.load('mark_green.npy').astype(np.uint8)
    hh,ww=pk.shape;xx=np.arange(ww)[None,:];yy=np.arange(hh)[:,None]
    pk[(yy>222)&(xx<445)]=0                      # quitar la flecha
    n,l,stt,_=cv2.connectedComponentsWithStats(pk)
    for i in range(1,n):
        if stt[i,4]<40: pk[l==i]=0
    pk=cv2.morphologyEx(pk,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8));pk=cv2.dilate(pk,np.ones((3,3),np.uint8))
    near=np.zeros(out.shape,np.uint8)
    d3=cv2.distanceTransform((out!=3).astype(np.uint8),cv2.DIST_L2,3);d2=cv2.distanceTransform((out!=2).astype(np.uint8),cv2.DIST_L2,3)
    tgt=np.where(d3<d2,3,2).astype(np.uint8)
    m=(pk>0)&on;out[m]=tgt[m]
    n,l,stt,_=cv2.connectedComponentsWithStats(cv2.dilate(gr,np.ones((3,3),np.uint8)))
    gm=np.zeros(out.shape,np.uint8)
    for i in range(1,n):
        if stt[i,4]<6: continue
        cs,_=cv2.findContours((l==i).astype(np.uint8),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cv2.fillPoly(gm,[cv2.convexHull(np.vstack(cs))],1)
    out[(gm>0)&on]=4
    out[~on]=0
    return rgba,out
