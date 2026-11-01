p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
can=open('canyon.js').read()
rep("function buildCircuit(Z,zi,lap,seed){",can+"\nfunction buildCircuit(Z,zi,lap,seed){if(CIRCS[Z.circ].open)return buildCanyon(Z,zi,lap,seed);")
# zona
rep("{name:'SA CALOBRA',water:['#12ab9c','#0a7b88'],obj:'time',goal:'Cruza el cañón del Torrent de Pareis antes de que se acabe el tiempo. Hace curvas todo el rato: las paredes de roca van saliendo por un lado y por el otro.',",
    "{name:'SA CALOBRA',water:['#12ab9c','#0a7b88'],circ:'calobra',laps:1,obj:'time',goal:'Remonta el cañón del Torrent de Pareis hasta la playa de Sa Calobra antes de que se acabe el tiempo. Curvas todo el rato y la pantalla gira contigo. Cada control te da segundos.',")
# dibujo
rep("function drawCircuit(Zn){const C=Zn.circ,","function drawCircuit(Zn){if(Zn.circ.canyon){drawCanyon(Zn);return;}const C=Zn.circ,")
rep("function drawCircTop(Zn){const C=Zn.circ,A=C.arch,t=G.t;if(!A||Math.abs(A.x-G.P.x)>700||Math.abs(A.y-G.P.y)>700)return;const W=C.W;ctx.save();ctx.translate(A.x,A.y);ctx.rotate(A.h);",
    "function drawCircTop(Zn){const C=Zn.circ,t=G.t,W=C.W;for(const A of(C.arches||(C.arch?[Object.assign({txt:'SALIDA · META',col:'#ffc93c'},C.arch)]:[]))){if(Math.abs(A.x-G.P.x)>700||Math.abs(A.y-G.P.y)>700)continue;ctx.save();ctx.translate(A.x,A.y);ctx.rotate(A.h);")
rep("ctx.fillStyle='#ffc93c';ctx.font='800 13px \"Saira Condensed\",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('SALIDA · META',0,.5);",
    "ctx.fillStyle=A.col;ctx.font='800 13px \"Saira Condensed\",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(A.txt,0,.5);")
rep(" ctx.restore();\n ctx.save();ctx.font='800 11px \"Saira Condensed\",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';for(const L of Zn.labels||[])",
    " ctx.restore();}\n ctx.save();ctx.font='800 11px \"Saira Condensed\",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';for(const L of Zn.labels||[])")
# lógica: paredes, meta, controles
rep("function circTick(dt){const C=G.zone.circ,LDS=G.zone.lands;\n for(const c of crafts()){circProg(c);",
    """function circTick(dt){const C=G.zone.circ,LDS=G.zone.lands;
 for(const c of crafts()){circProg(c);
  if(C.canyon){const lim=C.W/2-11;if(c.off>lim){const i=c.cs,nx=Math.cos(C.h[i]),ny=Math.sin(C.h[i]),lat=(c.x-C.x[i])*nx+(c.y-C.y[i])*ny,sg=lat>=0?1:-1;c.x=C.x[i]+nx*sg*lim;c.y=C.y[i]+ny*sg*lim;c.off=lim;
    const out=(Math.sin(c.va)*nx-Math.cos(c.va)*ny)*sg;if(out>0){c.v*=1-Math.min(.55,out*.7);let d=c.va-C.h[i];while(d>Math.PI)d-=TAU;while(d<-Math.PI)d+=TAU;const tg=Math.abs(d)<Math.PI/2?C.h[i]:C.h[i]+Math.PI;let e=c.va-tg;while(e>Math.PI)e-=TAU;while(e<-Math.PI)e+=TAU;c.va=c.h=tg+e*.25;
     if(c.isP&&!G.demo&&!(c._bumpT>0)&&c.v>110){c._bumpT=.5;Snd.bump();G.shake=4;}}}}""")
rep("if(!c.fin&&c.prog>=C.laps*C.L){c.fin=1;","if(C.cps&&c.isP&&!G.demo&&G.mode==='play'&&!c.fin)for(const k of C.cps)if(!k.done&&c.prog>=k.s){k.done=1;const bn=C.bonus||15;G.time+=bn;Snd.check();msg('CONTROL','+'+bn+' SEGUNDOS','var(--lime)');}\n  if(!c.fin&&c.prog>=(C.open?C.finS:C.laps*C.L)){c.fin=1;")
# tiempo del cañón
rep(" G.time=Z.obj==='time'||Z.obj==='slalom'||Z.obj==='jumps'?Math.round(Zn.len/3/((Z.pace||200)*(1+zi*.008)))+9+(Z.giant?6:0):0;",
    " G.time=Z.obj==='time'||Z.obj==='slalom'||Z.obj==='jumps'?Math.round(Zn.len/3/((Z.pace||200)*(1+zi*.008)))+9+(Z.giant?6:0):0;\n if(Zn.circ&&Zn.circ.open){const T=Zn.circ.L/205;G.time=Math.round(T*.5);Zn.circ.bonus=Math.round(T*.27);for(const k of Zn.circ.cps)k.done=0;}")
# HUD distancia a meta
rep("else{setTxt('hlL','META');setTxt('hvL',(Math.max(0,(P.y-Zn.finishY))/1000*.5).toFixed(1)+'<i> km</i>');}",
    "else{setTxt('hlL','META');setTxt('hvL',((Zn.circ?Math.max(0,(Zn.circ.finS||0)-(P.prog||0)):Math.max(0,(P.y-Zn.finishY)))/1000*.5).toFixed(1)+'<i> km</i>');}")
# insignia de la portada: sigue siendo contrarreloj
rep("const t=Z.circ?['CIRCUITO',","const t=Z.circ&&Z.obj!=='time'?['CIRCUITO',")
# mini-mapa con recorrido abierto
rep("g.lineJoin='round';g.beginPath();for(let i=0;i<=C.n;i++){const k=i%C.n;","g.lineJoin='round';g.beginPath();for(let i=0;i<=(C.open?C.n-1:C.n);i++){const k=i%C.n;")
rep(" G._mm={sc,ox,oy,bg:bgc,S0};}"," if(C.open){const ex=C.x[C.n-1]*sc+ox,ey=C.y[C.n-1]*sc+oy;for(let k=0;k<4;k++){g.fillStyle=k%2?'#111':'#fff';g.fillRect(ex-4+(k%2)*4,ey-4+((k/2)|0)*4,4,4);}}\n G._mm={sc,ox,oy,bg:bgc,S0};}")
rep("const C=G.zone.circ,cvm=$('#cmap'),D=DPR||1,S0=112;cvm.width=S0*D;cvm.height=S0*D;","const C=G.zone.circ,cvm=$('#cmap'),D=DPR||1,MW=C.open?72:112,MH=C.open?168:112;cvm.style.width=MW+'px';cvm.style.height=MH+'px';cvm.width=MW*D;cvm.height=MH*D;")
rep("const pad=12,sc=Math.min((S0-pad*2)/(c-a),(S0-pad*2)/(d-b)),ox=(S0-(c-a)*sc)/2-a*sc,oy=(S0-(d-b)*sc)/2-b*sc;const bgc=document.createElement('canvas');bgc.width=S0*D;bgc.height=S0*D;","const pad=10,sc=Math.min((MW-pad*2)/(c-a),(MH-pad*2)/(d-b)),ox=(MW-(c-a)*sc)/2-a*sc,oy=(MH-(d-b)*sc)/2-b*sc;const bgc=document.createElement('canvas');bgc.width=MW*D;bgc.height=MH*D;")
rep(" G._mm={sc,ox,oy,bg:bgc,S0};}"," G._mm={sc,ox,oy,bg:bgc};}")
rep("const APP_VER=54;","const APP_VER=55;")
open(p,'w').write(s);print('ok')
s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
rep("const t=Z.circ&&Z.obj!=='time'?['CIRCUITO',","const t=Z.circ&&CIRCS[Z.circ]&&CIRCS[Z.circ].open?['TRAMO','#46e3c4','#0c8a74','scurve']:Z.circ&&Z.obj!=='time'?['CIRCUITO',")
rep("  else if(t[3]==='flag'){","  else if(t[3]==='scurve'){g.beginPath();g.moveTo(ix-6,iy+8);g.bezierCurveTo(ix+9,iy+5,ix-9,iy-4,ix+5,iy-7);g.stroke();g.beginPath();g.moveTo(ix+8,iy-8);g.lineTo(ix+2,iy-10.5);g.lineTo(ix+3.5,iy-4);g.closePath();g.fill();}\n  else if(t[3]==='flag'){")
open(p,'w').write(s);print('ok3')
