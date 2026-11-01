p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
# 1. Sa Calobra: curvas más abiertas
i=s.find("CIRCS.calobra={h0:0,open:1,canyon:1,W:430,segs:[");j=s.find("]};",i)+3;assert i>0
s=s[:i]+"CIRCS.calobra={h0:0,open:1,canyon:1,W:430,segs:[['S',700],['L',30,520],['S',300],['R',55,700],['L',85,520],['S',300],['R',70,800],['L',85,700],['S',500],['R',85,700],['L',30,700],['S',500],['R',70,800],['L',85,600],['S',300],['R',40,520],['S',300],['L',40,700],['R',85,600],['L',70,800],['R',55,700],['S',500],['L',40,800],['R',70,600],['S',500],['L',85,700],['R',70,800],['S',700],['S',700]]};"+s[j:]
# 2. bloque de Bahamas -> versión con estilos (Bahamas / Es Trenc)
i=s.find("BOATK.cat={bw:26");j=s.find("\nfunction buildCircuit(Z,zi,lap,seed){",i);assert 0<i<j
s=s[:i]+open('archi2.js').read().rstrip('\n')+s[j:]
# 3. zonas
rep("{name:'BAHAMAS',water:['#1e74bd','#145a9e'],","{name:'BAHAMAS',water:['#1569b5','#0f509a'],")
rep("{name:'CARRERA ES TRENC',water:['#1fd0df','#0c9ad2'],obj:'race2',goal:'Termina entre los 2 primeros. Hay dos pasos estrechos y dos islas, y las chicas de los flotadores te distraen.',",
    "{name:'CARRERA ES TRENC',water:['#23c6de','#1198d0'],circ:'trenc',laps:1,obj:'race2',goal:'Termina entre los 2 primeros bordeando la playa de Es Trenc. La pantalla gira contigo. Hay 4 pasos estrechos: busca el hueco o salta el banco de arena con la ola. Las chicas de los flotadores te distraen.',")
# 4. playa sólida a la izquierda, saltar bancos de arena
rep("  if(LDS&&(c.isP||!C.archi)&&landIn(LDS,c.x,c.y)){if(c._lx!=null){c.x=c._lx;c.y=c._ly;}c.v*=.3;c.boostT=0;if(c.isP&&!G.demo&&!(c._bumpT>0)){c._bumpT=.7;Snd.bump();G.shake=5;pop(c.x,c.y-36,'¡TIERRA!','#ff4757');}}else{c._lx=c.x;c._ly=c.y;}",
    "  const inL=LDS&&(c.isP||!C.archi)&&landIn(LDS,c.x,c.y);if(inL&&c.air<=0){if(c._lx!=null){c.x=c._lx;c.y=c._ly;}c.v*=.3;c.boostT=0;if(c.isP&&!G.demo&&!(c._bumpT>0)){c._bumpT=.7;Snd.bump();G.shake=5;pop(c.x,c.y-36,'¡TIERRA!','#ff4757');}}else if(!inL){c._lx=c.x;c._ly=c.y;}")
rep("  if(C.archi){const i=c.cs,nx=Math.cos(C.h[i]),ny=Math.sin(C.h[i]),lat=(c.x-C.x[i])*nx+(c.y-C.y[i])*ny,lim=lat>=0?C.wr[i]:C.wl[i];if(Math.abs(lat)>lim&&c.air<=0){",
    "  if(C.archi&&C.beachL){const i=c.cs,nx=Math.cos(C.h[i]),ny=Math.sin(C.h[i]),lat=(c.x-C.x[i])*nx+(c.y-C.y[i])*ny,lim=C.wl[i]-11;if(lat<-lim){c.x=C.x[i]-nx*lim;c.y=C.y[i]-ny*lim;const out=-(Math.sin(c.va)*nx-Math.cos(c.va)*ny);if(out>0){c.v*=1-Math.min(.55,out*.7);let d=c.va-C.h[i];while(d>Math.PI)d-=TAU;while(d<-Math.PI)d+=TAU;const tg=Math.abs(d)<Math.PI/2?C.h[i]:C.h[i]+Math.PI;let e=c.va-tg;while(e>Math.PI)e-=TAU;while(e<-Math.PI)e+=TAU;c.va=c.h=tg+e*.25;if(c.isP&&!G.demo&&!(c._bumpT>0)&&c.v>110){c._bumpT=.5;Snd.bump();G.shake=4;}}}}\n  if(C.archi){const i=c.cs,nx=Math.cos(C.h[i]),ny=Math.sin(C.h[i]),lat=(c.x-C.x[i])*nx+(c.y-C.y[i])*ny,lim=lat>=0?C.wr[i]:(C.beachL?1e9:C.wl[i]);if(Math.abs(lat)>lim&&c.air<=0){")
# 5. la IA busca el hueco de los pasos
rep("const tx=C.x[i]+Math.cos(h)*ln,ty=C.y[i]+Math.sin(h)*ln;","if(C.gaps)for(const q of C.gaps){if(q.i-c.cs<95&&q.i-c.cs>-6)ln=q.lat+(c.lane||0)*.08;}const tx=C.x[i]+Math.cos(h)*ln,ty=C.y[i]+Math.sin(h)*ln;")
# 6. ola (rampa sin rayas) para saltar el banco
rep("case 'cramp':{ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);drawObj({t:'ramp',x:0,y:0,w:o.w,kick:1,Lr:o.Lr,col:o.col});","case 'cramp':{ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);drawObj({t:'ramp',x:0,y:0,w:o.w,kick:o.wave?0:1,Lr:o.Lr,col:o.col});")
rep("const T=Zn.circ.L/228;","const T=Zn.circ.L/238;")
rep("const APP_VER=57;","const APP_VER=58;")
open(p,'w').write(s);print('ok')
