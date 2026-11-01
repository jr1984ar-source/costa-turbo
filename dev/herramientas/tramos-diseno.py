import math,random,json,sys
from canyon import trace,clear
def gen(seed,target,angs,rads,strs,pstr,mincl,maxh,minArc):
    rnd=random.Random(seed);segs=[['S',700]];side=1 if rnd.random()<.5 else -1;tot=700
    while tot<target:
        ang=rnd.choice(angs);r=rnd.choice(rads);segs.append(['R' if side>0 else 'L',ang,r]);tot+=math.radians(ang)*r
        if rnd.random()<pstr:
            s=rnd.choice(strs);segs.append(['S',s]);tot+=s
        side=-side
        pts=trace(segs)
        if abs(math.degrees(pts[-1][2]))>maxh:return None
        if clear(pts,minArc)<mincl:return None
    segs.append(['S',700]);return segs
kind=sys.argv[1]
if kind=='calobra':P=dict(target=18300,angs=[30,40,55,70,85],rads=[520,600,700,800],strs=[300,500,700],pstr=.6,mincl=950,maxh=100,minArc=1800)
else:P=dict(target=19500,angs=[20,30,40,55],rads=[700,850,1000,1200],strs=[500,800,1100],pstr=.7,mincl=1300,maxh=70,minArc=2200)
for sd in range(1,40000):
    s=gen(sd,**P)
    if s:break
p=trace(s);L=(len(p)-1)*4;xs=[q[0] for q in p];ys=[q[1] for q in p]
print('seed',sd,'L',L,'clear',int(clear(p,P['minArc'])),'bbox',int(min(xs)),int(min(ys)),int(max(xs)),int(max(ys)),len(s))
print(json.dumps(s).replace('"',"'"))
