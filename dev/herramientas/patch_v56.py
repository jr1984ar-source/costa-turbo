p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
i=s.find("CIRCS.calobra={");j=s.find("function rockTile(",i);assert 0<i<j
s=s[:i]+open('canyon2.js').read()+s[j:]
rep("if(C.canyon){const lim=C.W/2-11;if(c.off>lim){const i=c.cs,nx=Math.cos(C.h[i]),ny=Math.sin(C.h[i]),lat=(c.x-C.x[i])*nx+(c.y-C.y[i])*ny,sg=lat>=0?1:-1;c.x=C.x[i]+nx*sg*lim;",
    "if(C.canyon){const i=c.cs,nx=Math.cos(C.h[i]),ny=Math.sin(C.h[i]),lat=(c.x-C.x[i])*nx+(c.y-C.y[i])*ny,sg=lat>=0?1:-1,lim=(sg>0?C.wr[i]:C.wl[i])-11;if(Math.abs(lat)>lim){c.x=C.x[i]+nx*sg*lim;")
rep("  if(c.off>C.W/2+8&&c.air<=0){c.v*=1-1.8*dt;","  if(!C.canyon&&c.off>C.W/2+8&&c.air<=0){c.v*=1-1.8*dt;")
rep("const T=Zn.circ.L/205;","const T=Zn.circ.L/228;")
rep("const APP_VER=55;","const APP_VER=56;")
open(p,'w').write(s);print('ok')
