import cv2,numpy as np,json,math
GW=390
KIND={1:'prom',2:'cliff',3:'mount',4:'prom',5:'beach',6:'cliff',7:'beach'}
segs=[];isles=[]
comp=lambda raw:24+150*math.tanh(max(0,raw)/220)
for i in range(1,8):
    land=(cv2.imread(f'tierra{i}.png',0)>0).astype(np.uint8);H,W=land.shape;sx=GW/W
    n,l,st,_=cv2.connectedComponentsWithStats(land,connectivity=8)
    big=set(k for k in range(1,n) if (l[:,0]==k).any() or (st[k][0]+st[k][2]/2)<W*.2 or (i==4 and st[k][3]>H*.35) or st[k][4]>200000)
    mainmask=np.isin(l,list(big))
    raw=np.array([ (np.where(mainmask[r])[0].max()*sx if mainmask[r].any() else 0) for r in range(H)])
    raw=np.convolve(np.pad(raw,6,mode='edge'),np.ones(13)/13,mode='valid')     # suavizar dientes
    g=np.array([comp(x) for x in raw])
    segs.append({'cap':i,'H':H,'raw':raw[::-1].tolist(),'g':g[::-1].tolist(),'kind':KIND[i]})   # de abajo arriba
    for k in range(1,n):
        if k in big or st[k][4]<1500: continue
        x,y,w,h,a=st[k]
        if x+w>=W-2 and w<70: continue
        r=int(y+h/2);sr=raw[min(H-1,r)];sg=comp(sr);cx=(x+w/2)*sx
        if cx<sr+20: continue
        f=(390-sg)/max(60,390-sr)
        isles.append({'cap':i,'r':(H-1-r)/H,'x':sg+(cx-sr)*f,'rx':max(16,w/2*sx*f),'ryp':h/H})
print([(s['cap'],round(max(s['g']))) for s in segs]);print([(d['cap'],round(d['x']),round(d['rx']),round(d['ryp'],2)) for d in isles])
json.dump({'segs':segs,'isles':isles},open('coast.json','w'))
