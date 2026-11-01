import math,random,json
from canyon import trace,clear
def gen(seed,target=18300):
    rnd=random.Random(seed);segs=[['S',600]];side=1 if rnd.random()<.5 else -1;tot=600
    while tot<target:
        ang=rnd.choice([45,60,80,100,120,140]);r=rnd.choice([330,360,400,440]);segs.append(['R' if side>0 else 'L',ang,r]);tot+=math.radians(ang)*r
        if rnd.random()<.6:
            s=rnd.choice([150,250,350,450]);segs.append(['S',s]);tot+=s
        side=-side
        pts=trace(segs)
        if abs(math.degrees(pts[-1][2]))>100:return None
        if clear(pts,1400)<800:return None
    segs.append(['S',600]);return segs
for sd in range(1,20000):
    s=gen(sd)
    if s:break
p=trace(s);L=(len(p)-1)*4;xs=[q[0] for q in p];ys=[q[1] for q in p]
print('seed',sd,'L',L,'clear',int(clear(p,1400)),'bbox',int(min(xs)),int(min(ys)),int(max(xs)),int(max(ys)),len(s))
print(json.dumps(s))
