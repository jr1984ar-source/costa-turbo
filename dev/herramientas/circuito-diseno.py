import math,sys,json
from PIL import Image,ImageDraw
W=340
def trace(segs,h0):
    x=y=0.0;h=h0;pts=[(x,y,h)];ds=4.0
    for sg in segs:
        if sg[0]=='S':
            n=max(1,int(sg[1]/ds))
            for i in range(n):x+=math.sin(h)*sg[1]/n;y-=math.cos(h)*sg[1]/n;pts.append((x,y,h))
        else:
            sgn=1 if sg[0]=='R' else -1;a=math.radians(sg[1]);r=sg[2];L=a*r;n=max(1,int(L/ds))
            for i in range(n):
                h+=sgn*a/n/2;x+=math.sin(h)*L/n;y-=math.cos(h)*L/n;h+=sgn*a/n/2;pts.append((x,y,h))
    return pts
def solve(segs,h0,ia,ib):
    # adjust lengths of straights ia (affects x/y) and ib to close loop: Newton on 2 vars
    segs=[list(s) for s in segs]
    for it in range(30):
        p=trace(segs,h0);ex,ey=p[-1][0],p[-1][1]
        if math.hypot(ex,ey)<.5:break
        J=[]
        for k in (ia,ib):
            segs[k][1]+=10;q=trace(segs,h0);segs[k][1]-=10;J.append(((q[-1][0]-ex)/10,(q[-1][1]-ey)/10))
        a,c=J[0];b,d=J[1];det=a*d-b*c
        da=(-ex*d+ey*b)/det;db=(ex*c-ey*a)/det
        segs[ia][1]+=da;segs[ib][1]+=db
    return segs
def check(segs,h0,name):
    p=trace(segs,h0);L=(len(p)-1)*4
    n=len(p);mind=1e9;where=None
    for i in range(0,n,3):
        for j in range(i+1,n,3):
            arc=min(j-i,n-(j-i))*4
            if arc<1300:continue
            d=math.hypot(p[i][0]-p[j][0],p[i][1]-p[j][1])
            if d<mind:mind=d;where=(i*4,j*4)
    xs=[q[0] for q in p];ys=[q[1] for q in p]
    print(name,'L=%d'%L,'minClear=%d'%mind,where,'end=(%.1f,%.1f) h=%.1f'%(p[-1][0],p[-1][1],math.degrees(p[-1][2]-h0)),'bbox',int(min(xs)),int(min(ys)),int(max(xs)),int(max(ys)))
    sc=.18;mx=min(xs)-400;my=min(ys)-400;im=Image.new('RGB',(int((max(xs)-mx+400)*sc),int((max(ys)-my+400)*sc)),(20,90,170));d=ImageDraw.Draw(im)
    P=[((q[0]-mx)*sc,(q[1]-my)*sc) for q in p]
    d.line(P,fill=(80,150,210),width=int(W*sc),joint='curve')
    for q in p[::30]:
        for sd in(-1,1):
            nx,ny=math.cos(q[2]),math.sin(q[2]);d.ellipse([((q[0]+nx*sd*W/2-mx)*sc)-2,((q[1]+ny*sd*W/2-my)*sc)-2,((q[0]+nx*sd*W/2-mx)*sc)+2,((q[1]+ny*sd*W/2-my)*sc)+2],fill=(255,200,0) if sd<0 else (255,120,20))
    d.line(P,fill=(255,255,255),width=1)
    d.ellipse([P[0][0]-5,P[0][1]-5,P[0][0]+5,P[0][1]+5],fill=(255,0,0))
    im.save(name+'.png');return p
if __name__=='__main__':
    D=json.load(open(sys.argv[1]))
    for name,c in D.items():
        segs=c['segs'];h0=math.radians(c['h0'])
        if 'solve' in c:segs=solve(segs,h0,*c['solve']);c['segs']=[[s[0],round(s[1],1)]+s[2:] for s in segs]
        check(segs,h0,name);print(json.dumps(c['segs']))
