import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v80.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=79", "const APP_VER=80")

# ===== 1. GRAN CARRERA: dos caminos largos =====
i0 = h.index(" if(Z.cuts&&Z.alt){"); i1 = h.index(" if(Z.islands){island(", i0)
h = h[:i0] + """ if(Z.cuts&&Z.alt){const sl=len/5;for(const[f,side]of CUTS_AT){const cu=Math.round(f*sl),half=CUT_HALF,N=3,rx=34,gap=86,wallAt=y=>side<0?zone.shore(y):zone.rwall(y);
   let lim=side<0?-1e9:1e9;for(let du=-half-80;du<=half+80;du+=20){const w=wallAt(-(cu+du));lim=side<0?Math.max(lim,w):Math.min(lim,w);}
   const x=side<0?lim+gap+rx:lim-gap-rx,seg=2*half/N,ry=seg/2+42,grp=(r()*1e6)|0;
   for(let k=0;k<N;k++)add({t:'island',x,y:-(cu-half+seg*(k+.5)),rx,ry,seed:(r()*1e6)|0,theme:'cay',cut:side,grp});
   resv.push([cu-half-220,cu+half+220]);
   const chX=y=>{const w=wallAt(y);return side<0?(w+11+x-rx-10)/2:(w-11+x+rx+10)/2;};
   const r1=cu-half*.45,r2=cu+half*.35;
   for(let du=-half+60;du<=half-60;du+=40){const uu=cu+du;if(Math.abs(uu-r1)<90||Math.abs(uu-r2)<90||Math.abs(du)<40)continue;add({t:'coin',x:chX(-uu),y:-uu});}
   for(const uu of[r1,r2]){add({t:'ramp',x:chX(-uu),y:-uu,w:56,Lr:36,col:'#ffd21a',sz:'s',kick:1});for(let i=0;i<4;i++)add({t:'coin',x:chX(-uu),y:-uu-RAMP_D.s*(.2+.6*i/3)*.7,air:1});}
   add({t:'can',x:chX(-cu),y:-cu});
   const near=side<0?x+rx+10:x-rx-10,far=side<0?(zone.rwall?Math.min(WG-24,zone.rwall(-cu)):WG-24):Math.max(24,zone.shore(-cu)+11);let t=0;
   for(let du=-half+170;du<=half-170;du+=280){const uu=cu+du,xx=lerp(near+30,far-30,[.25,.75,.5,.2,.8,.4,.65][t%7]);t++;const k=r();
    if(k<.3)add({t:'sail',x:xx,y:-uu,rot:(r()-.5)*.5});else if(k<.5)add({t:'motor',x:xx,y:-uu,rot:(r()-.5)*.4});else{add({t:'rock',x:xx,y:-uu,rad:12+r()*5,v:(r()*3)|0});if(r()<.6)add({t:'rock',x:clamp(xx+(r()-.5)*44,near+16,far-16),y:-uu-30,rad:9+r()*4,v:(r()*3)|0});}}
   for(let du=-half+320;du<=half-320;du+=560)for(let i=0;i<5;i++)add({t:'coin',x:lerp(near,far,.5)+Math.sin(i*.8)*22,y:-(cu+du)-140-i*28});}}
""" + h[i1:]
# la costa se aparta un poco en los tramos de los dos caminos (para que quepan los dos)
h = rep(h, " let altPres=null,altBase=null;if(Z.alt){",
 " const cutK=(u,sd)=>{if(!Z.cuts)return 0;let k=0;const sl=len/5;for(const[f,s2]of CUTS_AT)if(s2===sd)k=Math.max(k,sm(CUT_HALF+320,CUT_HALF+80,Math.abs(u-f*sl)));return k;};\n let altPres=null,altBase=null;if(Z.alt){")
h = rep(h, "  shoreU=u=>lerp(-90,base(u),altPres(u,0));}", "  shoreU=u=>lerp(-90,base(u)-42*cutK(u,-1),altPres(u,0));}")
h = rep(h, "zone.rwall=y=>{const u=-y;return lerp((VW>WG?WG+(VW-WG)/2:WG)+600,(VW>WG?WG+(VW-WG)/2:WG)-altBase(u)*.92,altPres(u,1));};}",
 "zone.rwall=y=>{const u=-y;return lerp((VW>WG?WG+(VW-WG)/2:WG)+600,(VW>WG?WG+(VW-WG)/2:WG)-altBase(u)*.92+42*cutK(u,1),altPres(u,1));};}")
h = rep(h, "function buildZone(zi,lap){", "const CUTS_AT=[[1.5,1],[4.5,-1]],CUT_HALF=1000,JJC=110,JJP=-40;\nfunction buildZone(zi,lap){")
h = rep(h, "goal:'Termina entre los 3 primeros. Hay dos atajos: canales estrechos detrás de las islas de arena, uno pegado a cada costa.',",
 "goal:'Termina entre los 3 primeros. Dos veces el mar se parte en dos caminos largos: uno estrecho pegado a la costa, con rampas y monedas, y otro ancho con barcos y rocas.',")
# la IA mantiene el lado en toda la lengua de arena
h = rep(h, "if(c.ai.isl!==o){c.ai.isl=o;c.ai.side=Math.random()<.5?-1:1;}", "if(c.ai.isl!==o){const keep=o.grp&&c.ai.isl&&c.ai.isl.grp===o.grp;c.ai.isl=o;if(!keep)c.ai.side=Math.random()<.5?-1:1;}")
# más palmeras en islas largas
h = rep(h, "for(let i=0;i<5;i++){const x=(q()-.5)*o.rx*.8,y=(q()-.5)*o.ry*1.1;", "for(let i=0,np=Math.max(5,Math.round(o.ry/70));i<np;i++){const x=(q()-.5)*o.rx*.8,y=(q()-.5)*o.ry*1.1;")

# ===== 2. COPAS =====
i0 = h.index(" {id:'costa',n:'COPA COSTA'"); i1 = h.index(" {id:'final',n:'LA FINAL'")
h = h[:i0] + """ {id:'costa',n:'COPA COSTA',nm:'Copa Costa',ic:'🏁',d:'La costa de Mallorca',z:[2,8,9,10,11,13],zs:'Al Mago · San Telm · Formentor · Sa Calobra · Cabrera · Tormenta',c:'#ff9a3c'},
 {id:'paraiso',n:'COPA PARAÍSO',nm:'Copa Paraíso',ic:'🌴',d:'Islas y playas de ensueño',z:[7,15,16,17,18],zs:'Es Trenc · Formentera · Bahamas · Australia · Es Vedrà',c:'#3fe0d0'},
 {id:'circuitos',n:'COPA CIRCUITOS',nm:'Copa Circuitos',ic:'🔄',d:'Circuitos cerrados',z:[14,19,20],zs:'Carrera de Boyas · Bahía de Palma · Bahía de Alcúdia',c:'#b18cff'},
 {id:'retos',n:'COPA RETOS',nm:'Copa Retos',ic:'⚡',d:'Contrarreloj, slalom, saltos y policía',z:[0,1,4,5,6,12],zs:'El Puerto · La Cala · Persecución · Olas Gigantes · Las Rampas · Portals',c:'#ffd21a'},
""" + h[i1:]
h = rep(h, "let cupStore=store.get('ct_cups',null);if(!cupStore||typeof cupStore!=='object')cupStore={};",
 "let cupStore=store.get('ct_cups',null);if(!cupStore||typeof cupStore!=='object')cupStore={};\n"
 "if(!cupStore.retos&&(cupStore.crono||cupStore.accion)){const a=cupStore.crono||{},b=cupStore.accion||{},t={};for(let l=1;l<=5;l++){const x=(a.t||{})[l],y=(b.t||{})[l];if(x||y)t[l]={n:((x&&x.n)|0)+((y&&y.n)|0),best:Math.max((x&&x.best)|0,(y&&y.best)|0),moto:(x&&x.moto)||(y&&y.moto)||'',at:(x&&x.at)||(y&&y.at)||Date.now()};}cupStore.retos={won:Math.max(a.won|0,b.won|0),t};store.set('ct_cups',cupStore);}")
h = rep(h, "b.querySelector('small').textContent=C.d+(C.fin?'':' · 5 carreras');", "b.querySelector('small').textContent=C.d+(C.fin?'':' · '+C.z.length+' carreras');")

# ===== 3. SAN TELM sin cuevas =====
h = rep(h, "caves:1,fish:1,goal:'Termina entre los 3 primeros. La costa queda a la derecha, con acantilados altísimos y dos cuevas por las que atajar. Cuidado con las barcas de pescadores y sus redes: si las cruzas, te frenan.',",
 "fish:1,goal:'Termina entre los 3 primeros. La costa queda a la derecha, con acantilados altísimos. Cuidado con las barcas de pescadores y sus redes: si las cruzas, te frenan.',")

# ===== 4. BAR JJ: puerto con pantalán, barcos y calita =====
h = rep(h, "if(Z.bar){const d=Math.abs(u-barU);x+=(Z.bar==='jj'?28:16)*(1-sm(110,150,d));}return x;};",
 "if(Z.bar==='jj'){const d=Math.abs(u-(barU+JJC));x+=46*sm(500,250,d)-84*sm(175,70,d);}else if(Z.bar){const d=Math.abs(u-barU);x+=16*(1-sm(110,150,d));}return x;};")
h = rep(h, "if(Z.bar==='jj'){const k=Math.floor(barU/SEG);zone.kind=y=>{const u=-y;return Math.abs(u-barU)<240?'prom':kindU(u);};}",
 "if(Z.bar==='jj'){zone.kind=y=>{const d=-y-barU;return d>JJP+30&&d<JJC+190?'beach':Math.abs(d)<260?'prom':kindU(-y);};}")
h = rep(h, "zone.swimX=y=>zone.kind(y)==='beach'?zone.shore(y)+38:null;",
 "zone.swimX=y=>{if(Z.bar==='jj'){const d=-y-barU;if(d>JJP-80&&d<JJC+280)return null;}return zone.kind(y)==='beach'?zone.shore(y)+38:null;};")
h = rep(h, "const bar={x:zone.shore(-barU)+(Z.bar==='jj'?84:72),y:-barU+(Z.bar==='jj'?50:30)};zone.ring=Z.bar?bar:null;",
 "const bar=Z.bar==='jj'?{x:zone.shore(-(barU+JJC))+58,y:-(barU+JJC)}:{x:zone.shore(-barU)+72,y:-barU+30};zone.ring=Z.bar?bar:null;\n"
 " zone.pier=null;if(Z.bar==='jj'){const pu=barU+JJP,sx=zone.shore(-pu),x0=sx-8,x1=sx+140;zone.pier={x0,x1,y:-pu,h:18};add({t:'pier',x:(x0+x1)/2,cx:(x0+x1)/2,hw:(x1-x0)/2+8,x0,x1,y:-pu,h:18});for(let bx=sx+28;bx<x1-14;bx+=30)add({t:'motor',x:bx,y:-pu-31,rot:(r()-.5)*.12,moored:1});}")
h = rep(h, "case 'turtle':return Math.hypot(o.x-x,o.y-y)<11+rad;", "case 'turtle':return Math.hypot(o.x-x,o.y-y)<11+rad;case 'pier':return x>o.x0-rad&&x<o.x1+rad&&Math.abs(y-o.y)<o.h/2+rad*.5;")
h = rep(h, "cboat:'¡BARCO!',fboat:'¡BARCA!'}[o.t]", "cboat:'¡BARCO!',fboat:'¡BARCA!',pier:'¡PANTALÁN!'}[o.t]")
h = rep(h, " case 'lbuoy':{", """ case 'pier':{const x0=o.x0,x1=o.x1,y0=o.y-o.h/2;ctx.fillStyle='rgba(0,20,50,.28)';ctx.fillRect(x0+4,y0+5,x1-x0,o.h);ctx.fillStyle='#bdb6aa';ctx.fillRect(x0,y0,x1-x0,o.h);ctx.strokeStyle='rgba(90,80,70,.4)';ctx.lineWidth=1;for(let x=x0+5;x<x1;x+=7){ctx.beginPath();ctx.moveTo(x,y0+1);ctx.lineTo(x,y0+o.h-1);ctx.stroke();}
  ctx.fillStyle='#8f877b';ctx.fillRect(x0,y0,x1-x0,2.5);ctx.fillRect(x0,y0+o.h-2.5,x1-x0,2.5);for(let x=x0+14;x<x1;x+=32){ctx.fillStyle='#5b4a3a';ctx.beginPath();ctx.arc(x,y0-1,2.6,0,TAU);ctx.arc(x,y0+o.h+1,2.6,0,TAU);ctx.fill();}ctx.fillStyle='#e9e4da';ctx.fillRect(x1-6,y0,6,o.h);}return;
 case 'lbuoy':{""")
# rivales que paran: rodean el pantalán
h = rep(h, "else{const want=clamp(Math.atan2(px-c.x,Math.max(40,dy)),-.8,.8),turn=",
 "else{const pr=Zn.pier,wp=pr&&c.y>pr.y-40,tx=wp?pr.x1+34:px,ty=wp?pr.y-48:ring.y,want=clamp(Math.atan2(tx-c.x,Math.max(40,c.y-ty)),-.8,.8),turn=")
# edificio, pasarela y palmeras del Bar JJ
h = rep(h, "function drawJJTop(g,Zn){const by=Zn.barY,sx=Zn.shore(by),L=sx-100;\n g.save();g.translate(L,by-116);",
 """function drawJJTop(g,Zn){const by=Zn.barY,py=by-JJP,cy=by-JJC,spx=Zn.shore(py);
 // pasarela de madera junto a la calita
 g.save();for(let y=py+10;y>cy-150;y-=5){const x=Math.min(spx,Zn.shore(y))-16;g.fillStyle=((y/5)|0)%2?'#b88a5a':'#a77a4c';g.fillRect(x-9,y-5,18,5.4);}
 g.strokeStyle='#6e4a2a';g.lineWidth=1.6;for(const dx of[-9,9]){g.beginPath();for(let y=py+10;y>cy-150;y-=6){const x=Math.min(spx,Zn.shore(y))-16+dx;y===py+10?g.moveTo(x,y):g.lineTo(x,y);}g.stroke();}g.restore();
 // palmeras en la arena de la calita
 {const q=rng(4321);for(const[dx,dy]of[[-40,-205],[-90,-160],[-30,-60],[-110,-250]]){const y=cy+dy+40,x=Zn.shore(y)+dx;g.save();g.globalAlpha=.2;for(let k=0;k<8;k++)leaf(g,x+6,y+5,k/8*TAU+.2,15,'#203018');g.restore();for(let k=0;k<8;k++)leaf(g,x,y,k/8*TAU+q()*.3,13+q()*4,k%2?'#2f8f3f':'#46aa4a');}}
 const sx=spx,L=sx-132;
 g.save();g.translate(L,py-62);""")
h = rep(h, " g.fillStyle='rgba(0,30,60,.25)';g.fillRect(104,162,64,11);g.fillStyle='#d8dce2';g.beginPath();g.roundRect(100,158,64,11,2);g.fill();g.strokeStyle='#aeb5be';g.lineWidth=1;g.stroke();\n g.restore();}", " g.restore();}")
open(H, 'w').write(h); print('ok')
h = open(H).read()
h = rep(h, "const free=u=>Math.abs(u-barU)>300&&u>420&&u<len-260&&!isRes(u);", "const free=u=>(Z.bar==='jj'?(u<barU+JJP-650||u>barU+JJC+330):Math.abs(u-barU)>300)&&u>420&&u<len-260&&!isRes(u);")
h = rep(h, "for(const f of(Array.isArray(Z.giant)?Z.giant:[.2,.34,.48,.62,.85,.88,.91])){const cu=Math.round(len*f),", "for(const f of(Array.isArray(Z.giant)?Z.giant:[.2,.34,.48,.62,.85,.88,.91])){let cu=Math.round(len*f);if(Z.bar&&cu>barU-500&&cu<barU+720)cu=barU+720;const ")
open(H, 'w').write(h); print('ok free/olas')
h = open(H).read()
h = rep(h, "zone.swimX=y=>{if(Z.bar==='jj'){", "zone.swimX=y=>{if(Z.cuts&&cutK(-y,-1)>0)return null;if(Z.bar==='jj'){")
open(H, 'w').write(h); print('ok swim')
