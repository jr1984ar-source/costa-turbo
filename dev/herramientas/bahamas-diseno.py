import math,random,json
from canyon import trace,clear
def gen(seed,target=20500):
    rnd=random.Random(seed);segs=[['S',700]];side=1 if rnd.random()<.5 else -1;tot=700
    while tot<target:
        ang=rnd.choice([35,50,65,80,100]);r=rnd.choice([480,560,640,720]);segs.append(['R' if side>0 else 'L',ang,r]);tot+=math.radians(ang)*r
        if rnd.random()<.7:
            s=rnd.choice([300,500,700,900]);segs.append(['S',s]);tot+=s
        side=-side
        pts=trace(segs)
        if abs(math.degrees(pts[-1][2]))>95:return None
        if clear(pts,1800)<1300:return None
    segs.append(['S',700]);return segs
for sd in range(1,30000):
    s=gen(sd)
    if s:break
p=trace(s);L=(len(p)-1)*4;xs=[q[0] for q in p];ys=[q[1] for q in p]
print('seed',sd,'L',L,'clear',int(clear(p,1800)),'bbox',int(min(xs)),int(min(ys)),int(max(xs)),int(max(ys)),len(s))
print(json.dumps(s))
