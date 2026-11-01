import math,random,json,sys
from PIL import Image,ImageDraw
W=260
def trace(segs,h0=0):
    x=y=0.0;h=h0;pts=[(x,y,h)];ds=4.0
    for sg in segs:
        if sg[0]=='S':
            n=max(1,int(sg[1]/ds))
            for i in range(n):x+=math.sin(h)*sg[1]/n;y-=math.cos(h)*sg[1]/n;pts.append((x,y,h))
        else:
            sgn=1 if sg[0]=='R' else -1;a=math.radians(sg[1]);r=sg[2];L=a*r;n=max(1,int(L/ds))
            for i in range(n):h+=sgn*a/n/2;x+=math.sin(h)*L/n;y-=math.cos(h)*L/n;h+=sgn*a/n/2;pts.append((x,y,h))
    return pts
def clear(pts,minArc=1000):
    n=len(pts);m=1e9
    for i in range(0,n,4):
        for j in range(i+int(minArc/4),n,4):
            d=math.hypot(pts[i][0]-pts[j][0],pts[i][1]-pts[j][1])
            if d<m:m=d
    return m
def gen(seed,target=14000):
    rnd=random.Random(seed);segs=[['S',500]];side=1 if rnd.random()<.5 else -1;tot=500
    while tot<target:
        ang=rnd.choice([60,75,90,110,130,150,160]);r=rnd.choice([205,215,230,250]);segs.append(['R' if side>0 else 'L',ang,r]);tot+=math.radians(ang)*r
        if rnd.random()<.55:
            s=rnd.choice([120,180,250,320]);segs.append(['S',s]);tot+=s
        side=-side
        pts=trace(segs)
        # net heading drift: keep heading within +-100deg of north to avoid coming back
        hdeg=math.degrees(pts[-1][2])
        if abs(hdeg)>110:
            return None
        if clear(pts,900)<W+170: return None
    segs.append(['S',400]);return segs
best=None
for sd in range(1,4000):
    s=gen(sd)
    if s:
        p=trace(s);c=clear(p,900)
        best=(sd,s,c);break
sd,segs,c=best;p=trace(segs);L=(len(p)-1)*4
xs=[q[0] for q in p];ys=[q[1] for q in p]
print('seed',sd,'L',L,'clear',int(c),'bbox',int(min(xs)),int(min(ys)),int(max(xs)),int(max(ys)),'nsegs',len(segs))
print(json.dumps(segs))
sc=.06;mx=min(xs)-400;my=min(ys)-400;im=Image.new('RGB',(int((max(xs)-mx+400)*sc),int((max(ys)-my+400)*sc)),(140,135,125));d=ImageDraw.Draw(im)
P=[((q[0]-mx)*sc,(q[1]-my)*sc) for q in p];d.line(P,fill=(18,171,156),width=int(W*sc),joint='curve');d.line(P,fill=(255,255,255),width=1)
im.save('canyon.png')
