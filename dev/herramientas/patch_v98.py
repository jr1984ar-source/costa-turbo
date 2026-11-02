import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v98.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=97", "const APP_VER=98")
# cámara que gira con la moto (como en Bahamas) en la pantalla de costa real
h = rep(h, "const CIRC=!!(Zn.circ&&G.P);let sv=null;if(CIRC){const RR=Math.hypot(VW*.5/CZ,VH*.75/CZ)+80;",
 "const CIRC=!!((Zn.circ||Zn.realMap)&&G.P),CZr=Zn.realMap?1:CZ;let sv=null;if(CIRC){const RR=Math.hypot(VW*.5/CZr,VH*.75/CZr)+80;")
h = rep(h, "ctx.translate(sv[0]/2+sx,sv[1]*.73+sy);ctx.scale(CZ,CZ);ctx.rotate(-(G.camA||0));", "ctx.translate(sv[0]/2+sx,sv[1]*.73+sy);ctx.scale(CZr,CZr);ctx.rotate(-(G.camA||0));")
h = rep(h, "hw=sv[0]/2/CZ,ht=sv[1]*.73/CZ,hb=sv[1]*.27/CZ,", "hw=sv[0]/2/CZr,ht=sv[1]*.73/CZr,hb=sv[1]*.27/CZr,")
h = rep(h, " if(CIRC)drawCircTop(Zn);", " if(CIRC&&Zn.circ)drawCircTop(Zn);")
h = rep(h, " if(Zn.circ){let d=(P.va||0)-(G.camA||0);while(d>Math.PI)d-=TAU;while(d<-Math.PI)d+=TAU;G.camA=(G.camA||0)+d*Math.min(1,dt*3.2);}else{\n",
 " if(Zn.circ||Zn.realMap){let d=(P.va||0)-(G.camA||0);while(d>Math.PI)d-=TAU;while(d<-Math.PI)d+=TAU;G.camA=(G.camA||0)+d*Math.min(1,dt*3.2);}if(!Zn.circ){\n")
# giro libre (sin volver solo al centro ni límite), como en los circuitos
h = rep(h, "if(!ctl.turn&&!Zn.circ)c.h*=1-2.4*dt;}", "if(!ctl.turn&&!Zn.circ&&!(Zn.realMap&&c.isP&&!G.demo))c.h*=1-2.4*dt;}")
h = rep(h, "   if(!Zn.circ){if(drifting)c.h=clamp(c.h,-1.25,1.25);", "   if(!Zn.circ&&!(Zn.realMap&&c.isP&&!G.demo)){if(drifting)c.h=clamp(c.h,-1.25,1.25);")
# más trozos en memoria (con la cámara girada se ven más)
h = rep(h, "if(chunks.size>18){for(const kk of chunks.keys())", "if(chunks.size>28){for(const kk of chunks.keys())")
h = rep(h, "chunks.delete(kk);if(chunks.size<=14)break;", "chunks.delete(kk);if(chunks.size<=22)break;")
open(H, 'w').write(h); print('ok')
