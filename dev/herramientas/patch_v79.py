import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v79.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=78", "const APP_VER=79")
# ---- zonas ----
h = rep(h, "{name:'TORMENTA',alt:1,obj:'time',goal:'Cruza la tormenta de noche antes de que se acabe el tiempo.',",
 "{name:'TORMENTA',alt:1,storm:1,obj:'time',goal:'Cruza la tormenta de noche antes de que se acabe el tiempo. Donde el agua brilla va a caer un rayo: apártate o te frena. El oleaje te empuja de lado. Sigue las boyas de luz.',")
h = rep(h, "goal:'Termina entre los 3 primeros. Esta vez la costa queda a la derecha: calitas, recovecos y acantilados altísimos.',",
 "caves:1,fish:1,goal:'Termina entre los 3 primeros. La costa queda a la derecha, con acantilados altísimos y dos cuevas por las que atajar. Cuidado con las barcas de pescadores y sus redes: si las cruzas, te frenan.',")
# ---- San Telm: bahías con cueva en el acantilado ----
h = rep(h, " if(Z.theme==='open'){shoreU=u=>-(VW>WG?(VW-WG)/2:0);kindU=u=>'open';}\n",
 """ if(Z.theme==='open'){shoreU=u=>-(VW>WG?(VW-WG)/2:0);kindU=u=>'open';}
 const caveAt=Z.caves?[Math.round(len*.36),Math.round(len*.7)]:[];if(caveAt.length){const base=shoreU,bk=kindU;shoreU=u=>{let x=base(u);for(const cu of caveAt){const d=Math.abs(u-cu);if(d<430)x=lerp(x,38+5*n1(u/80),sm(430,260,d));}return x;};kindU=u=>caveAt.some(cu=>Math.abs(u-cu)<330)?'mount':bk(u);}
""")
h = rep(h, " if(Z.island)island(Math.round(len*.45),58,220);\n",
 """ if(Z.island)island(Math.round(len*.45),58,220);
 zone.caves=[];for(const cu of caveAt){const rx=42,ry=205,gap=82;let lim=-1e9;for(let du=-ry;du<=ry;du+=15)lim=Math.max(lim,zone.shore(-(cu+du)));const x=lim+gap+rx;
  add({t:'island',x,y:-cu,rx,ry,seed:(r()*1e6)|0,theme:'cove',cave:1});resv.push([cu-ry-190,cu+ry+190]);zone.caves.push({y:-cu,x0:lim-46,x1:x-rx*.45,h:ry*1.5,s:(r()*1e6)|0});
  for(let du=-ry+30;du<=ry-30;du+=38){if(Math.abs(du)<30)continue;const y=-(cu+du),e=Math.sqrt(Math.max(0,1-(du/ry)*(du/ry)));add({t:'coin',x:(x-(rx+10)*e+zone.shore(y)+11)/2,y});}
  add({t:'can',x:(x-rx-10+zone.shore(-cu)+11)/2,y:-cu});
  const far=Math.min(WG-24,zone.rwall?zone.rwall(-cu):WG-24),near=x+rx+10;for(const[fu,t]of[[-.5,.35],[.25,.7]]){add({t:'rock',x:lerp(near+24,far-24,t),y:-(cu+fu*ry),rad:12+r()*5,v:(r()*3)|0});}}
 if(Z.fish){for(let fu=1300;fu<len-800;fu+=1500+r()*700){if(isRes(fu)||Math.abs(fu-barU)<400)continue;const L=Math.max(24,zone.shore(-fu)+34),R=Math.min(WG-24,zone.rwall?zone.rwall(-fu)-34:WG-24);if(R-L<170)continue;
   const bx=lerp(L+26,R-26,r()),dir=bx<(L+R)/2?1:-1,nl=80+r()*36,nx1=clamp(bx+dir*(16+nl),L,R);add({t:'fboat',x:bx,y:-fu,rot:(r()-.5)*.5,c:['#1e5eff','#e3202b','#1f9e52','#ffd21a','#f4f5f7'][(r()*5)|0],nx1,cx:(bx+nx1)/2,hw:Math.abs(nx1-bx)/2+14});resv.push([fu-140,fu+140]);}}
 if(Z.storm){for(let su=1100;su<len-500;su+=1250+r()*500){if(isRes(su)||Math.abs(su-barU)<350)continue;add({t:'swell',y:-su,h:90,dir:r()<.5?-1:1,f:92});resv.push([su-90,su+90]);}
  for(let bu=420;bu<len-200;bu+=320){const y=-bu,L=Math.max(22,zone.shore(y)+30),R=Math.min(WG-22,zone.rwall?zone.rwall(y)-30:WG-22);add({t:'lbuoy',x:L,y,c:'#ff4d5a'});add({t:'lbuoy',x:R,y,c:'#4dff8a'});}}
""")
# ---- objetos: choques, red y oleaje ----
h = rep(h, "case 'turtle':return Math.hypot(o.x-x,o.y-y)<11+rad;", "case 'turtle':return Math.hypot(o.x-x,o.y-y)<11+rad;case 'fboat':return Math.abs(o.x-x)<9+rad&&Math.abs(o.y-y)<22+rad*.5;")
h = rep(h, "turtle:'¡TORTUGA!',cturn:'¡BOYA!',cboat:'¡BARCO!'}[o.t]", "turtle:'¡TORTUGA!',cturn:'¡BOYA!',cboat:'¡BARCO!',fboat:'¡BARCA!'}[o.t]")
h = rep(h, "   if(o.t==='jelly'){if(c.isP&&!G.demo&&!o.hit",
 """   if(o.t==='lbuoy')continue;
   if(o.t==='swell'){if(c.z<.3&&Math.abs(c.y-o.y)<o.h/2){c.x+=o.dir*o.f*dt;if(c.isP&&!G.demo&&!o.msg){o.msg=1;pop(c.x,c.y-36,'¡OLEAJE!','#9fd8ff');}}continue;}
   if(o.t==='fboat'&&c.z<.3&&!G.demo){const a=Math.min(o.x,o.nx1),b=Math.max(o.x,o.nx1);if(c.x>a+8&&c.x<b-2&&Math.abs(c.x-o.x)>12&&((c.prevY>o.y&&c.y<=o.y)||(c.prevY<o.y&&c.y>=o.y))){c.v*=.45;c.boostT=0;if(c.isP){Snd.miss();buzz(60);G.shake=3;pop(c.x,c.y-36,'¡RED DE PESCA!','#ffb347');}}}
   if(o.t==='jelly'){if(c.isP&&!G.demo&&!o.hit""")
# IA: ignora oleaje y boyas de luz; esquiva barca + red entera
h = rep(h, "o.t==='gate'||o.t==='island'||o.t==='pass'||o.t==='tbuoy'||o.t==='jelly')continue;const w=o.t==='yacht'?34:",
 "o.t==='gate'||o.t==='island'||o.t==='pass'||o.t==='tbuoy'||o.t==='jelly'||o.t==='swell'||o.t==='lbuoy')continue;const ox=o.cx!=null?o.cx:o.x,w=o.hw?o.hw:o.t==='yacht'?34:")
h = rep(h, "if(Math.abs(o.x-c.ai.tx)<w+14||Math.abs(o.x-c.x)<w+12){c.ai.tx=o.x>(L+R)/2?o.x-w-30:o.x+w+30;",
 "if(Math.abs(ox-c.ai.tx)<w+14||Math.abs(ox-c.x)<w+12){c.ai.tx=ox>(L+R)/2?ox-w-30:ox+w+30;")
# ---- rayos (Tormenta) ----
h = rep(h, " // night lightning\n", " // rayos de la tormenta\n if(Zn.Z.storm&&racing&&!G.demo)updateBolts(dt);\n // night lightning\n")
h = rep(h, "G.police=[];G.parts_fx=[];", "G.police=[];G.bolts=[];G.boltT=2.5;G.parts_fx=[];", 2)
h = rep(h, "let nightC=null;\n", """let nightC=null;
function boltPath(b){const pts=[],x0=b.x+(Math.random()-.5)*90,n=9;for(let i=0;i<=n;i++){const t=i/n;pts.push([lerp(x0,b.x,t)+(i&&i<n?(Math.random()-.5)*42:0),lerp(b.y-560,b.y,t)]);}return pts;}
function updateBolts(dt){const P=G.P,Zn=G.zone;G.bolts=G.bolts||[];G.boltT=(G.boltT==null?2.5:G.boltT)-dt;
 if(G.boltT<=0&&P.y>Zn.finishY+700){G.boltT=2.3+Math.random()*1.7;const y=P.y-170-Math.random()*190-Math.max(0,P.v)*.35,L=Math.max(30,Zn.shore(y)+40),R=Math.min(WG-30,Zn.rwall?Zn.rwall(y)-40:WG-30);if(R>L+40)G.bolts.push({x:clamp(P.x+(Math.random()-.5)*150,L,R),y,t:1.25,s:0,life:0});}
 for(const b of G.bolts){if(!b.s){b.t-=dt;if(b.t<=0){b.s=1;b.life=.55;b.path=boltPath(b);G.flash=Math.max(G.flash||0,reduced?.3:.85);Snd.thunder();splash(b.x,b.y,26,200,'#cfe6ff');}}
  else{b.life-=dt;if(!b.hit&&P.z<.5&&Math.hypot(P.x-b.x,P.y-b.y)<44){b.hit=1;P.v*=.3;P.boostT=0;G.shake=9;buzz(110);Snd.crash();pop(P.x,P.y-40,'¡RAYO!','#ffe066');}}}
 G.bolts=G.bolts.filter(b=>!b.s||b.life>0);}
function drawBolts(){const B=G.bolts||[];if(!B.length)return;ctx.save();const tx=x=>(x-camX)*K,ty=y=>(y-camTop)*K;
 for(const b of B){const x=tx(b.x),y=ty(b.y);if(!b.s){const k=1-b.t/1.25,p=1+Math.sin(G.t*18)*.08;ctx.globalCompositeOperation='lighter';const rg=ctx.createRadialGradient(x,y,0,x,y,50*K);rg.addColorStop(0,`rgba(150,195,255,${(.15+k*.35).toFixed(3)})`);rg.addColorStop(1,'rgba(150,195,255,0)');ctx.fillStyle=rg;ctx.beginPath();ctx.arc(x,y,50*K,0,TAU);ctx.fill();ctx.globalCompositeOperation='source-over';
   ctx.strokeStyle=`rgba(255,235,140,${(.45+k*.55).toFixed(3)})`;ctx.lineWidth=2.5*K;ctx.setLineDash([6*K,5*K]);ctx.lineDashOffset=-G.t*30*K;ctx.beginPath();ctx.arc(x,y,42*K*p,0,TAU);ctx.stroke();ctx.setLineDash([]);
   ctx.fillStyle=`rgba(255,228,90,${(.55+k*.45).toFixed(3)})`;ctx.font=`800 ${Math.round(20*K)}px "Saira Condensed",sans-serif`;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('⚡',x,y);}
  else{const a=clamp(b.life/.55,0,1);ctx.globalCompositeOperation='lighter';ctx.lineJoin='round';ctx.beginPath();b.path.forEach((p,i)=>i?ctx.lineTo(tx(p[0]),ty(p[1])):ctx.moveTo(tx(p[0]),ty(p[1])));ctx.strokeStyle=`rgba(170,205,255,${a.toFixed(3)})`;ctx.lineWidth=7*K;ctx.stroke();ctx.strokeStyle=`rgba(255,255,255,${a.toFixed(3)})`;ctx.lineWidth=2.4*K;ctx.stroke();
   const rg=ctx.createRadialGradient(x,y,0,x,y,80*K);rg.addColorStop(0,`rgba(210,228,255,${(.75*a).toFixed(3)})`);rg.addColorStop(1,'rgba(210,228,255,0)');ctx.fillStyle=rg;ctx.beginPath();ctx.arc(x,y,80*K,0,TAU);ctx.fill();ctx.globalCompositeOperation='source-over';}}
 ctx.restore();}
""")
h = rep(h, " if(Zn.Z.tod==='night')drawNight();\n", " if(Zn.Z.tod==='night')drawNight();\n if(Zn.Z.storm)drawBolts();\n")
# luces de la noche: boyas de luz, oleaje y avisos de rayo
h = rep(h, " if(G.zone.ring)light(SX(G.zone.ring.x)*k,(G.zone.ring.y-camTop)*k,80*k,.8);\n",
 """ if(G.zone.ring)light(SX(G.zone.ring.x)*k,(G.zone.ring.y-camTop)*k,80*k,.8);
 if(G.zone.Z.storm){const O=G.zone.objs;for(let i=findStart(O,camTop-120);i<O.length&&O[i].y<camTop+VH+120;i++){const o=O[i];if(o.t==='lbuoy')light(SX(o.x)*k,(o.y-camTop)*k,(46+6*Math.sin(G.t*3+o.y))*k,.8);else if(o.t==='swell')for(let j=0;j<4;j++)light(SX(40+j*105)*k,(o.y-camTop)*k,62*k,.42);}for(const b of G.bolts||[])light(SX(b.x)*k,(b.y-camTop)*k,58*k,.7);}
""")
# ---- dibujo de los objetos nuevos ----
h = rep(h, " case 'island':{if(!o.spr||o.sprK!==K){o.spr=makeIsland(o);o.sprK=K;}",
 """ case 'lbuoy':{const p=.6+.4*Math.sin(G.t*3+o.y*.01);ctx.fillStyle='rgba(0,20,50,.3)';ctx.beginPath();ctx.ellipse(o.x+2,o.y+3,6,4,0,0,TAU);ctx.fill();ctx.fillStyle='#e9eef4';ctx.beginPath();ctx.arc(o.x,o.y,5.5,0,TAU);ctx.fill();ctx.fillStyle=o.c;ctx.beginPath();ctx.arc(o.x,o.y,3.4,0,TAU);ctx.fill();
  ctx.save();ctx.globalCompositeOperation='lighter';const rg=ctx.createRadialGradient(o.x,o.y,0,o.x,o.y,22);rg.addColorStop(0,o.c+'cc');rg.addColorStop(1,o.c+'00');ctx.globalAlpha=p;ctx.fillStyle=rg;ctx.beginPath();ctx.arc(o.x,o.y,22,0,TAU);ctx.fill();ctx.restore();}return;
 case 'swell':{const x0=-40,x1=WG+40,h2=o.h/2;ctx.save();ctx.fillStyle='rgba(180,215,255,.08)';ctx.fillRect(x0,o.y-h2,x1-x0,o.h);ctx.strokeStyle='rgba(235,245,255,.55)';ctx.lineWidth=2;ctx.lineCap='round';
  for(let i=0;i<16;i++){const yy=o.y-h2+8+((i*37)%(o.h-16)),xx=x0+(((i*71+G.t*o.dir*110)%(x1-x0))+(x1-x0))%(x1-x0);ctx.beginPath();ctx.moveTo(xx-o.dir*16,yy-4);ctx.quadraticCurveTo(xx,yy+3,xx+o.dir*16,yy-4);ctx.stroke();}
  ctx.fillStyle='rgba(255,255,255,.75)';ctx.font='800 18px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';for(let j=0;j<3;j++){const xx=70+j*125+((G.t*o.dir*40)%30);ctx.fillText(o.dir>0?'›››':'‹‹‹',xx,o.y);}ctx.restore();}return;
 case 'fboat':{const a=Math.min(o.x,o.nx1),b=Math.max(o.x,o.nx1),dir=o.nx1>o.x?1:-1;ctx.save();ctx.strokeStyle='rgba(240,240,230,.7)';ctx.lineWidth=1.2;ctx.setLineDash([3,3]);ctx.beginPath();ctx.moveTo(o.x+dir*10,o.y);ctx.lineTo(o.nx1,o.y);ctx.stroke();ctx.setLineDash([]);
  for(let x=o.x+dir*18;dir>0?x<o.nx1:x>o.nx1;x+=dir*14){ctx.fillStyle='#ff8c1a';ctx.beginPath();ctx.ellipse(x,o.y,3.2,2.4,0,0,TAU);ctx.fill();}
  ctx.fillStyle='#ff4d1a';ctx.beginPath();ctx.arc(o.nx1,o.y,5,0,TAU);ctx.fill();ctx.strokeStyle='#222';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(o.nx1,o.y);ctx.lineTo(o.nx1,o.y-13);ctx.stroke();ctx.fillStyle='#ffd21a';ctx.fillRect(o.nx1,o.y-13,7,5);
  ctx.translate(o.x,o.y);ctx.rotate(o.rot);ctx.fillStyle='rgba(0,20,50,.28)';ctx.beginPath();ctx.ellipse(3,4,10,23,0,0,TAU);ctx.fill();ctx.fillStyle=o.c;ctx.beginPath();ctx.moveTo(0,-23);ctx.quadraticCurveTo(10,-10,9,12);ctx.quadraticCurveTo(0,22,-9,12);ctx.quadraticCurveTo(-10,-10,0,-23);ctx.fill();
  ctx.fillStyle='#c99a62';ctx.beginPath();ctx.moveTo(0,-17);ctx.quadraticCurveTo(7,-7,6.5,10);ctx.quadraticCurveTo(0,17,-6.5,10);ctx.quadraticCurveTo(-7,-7,0,-17);ctx.fill();ctx.strokeStyle='rgba(120,80,40,.6)';ctx.lineWidth=.8;for(let yy=-10;yy<14;yy+=5){ctx.beginPath();ctx.moveTo(-6,yy);ctx.lineTo(6,yy);ctx.stroke();}
  ctx.fillStyle='#f4f5f7';ctx.fillRect(-4,-6,8,7);ctx.fillStyle='#e8b48c';ctx.beginPath();ctx.arc(0,6,3.4,0,TAU);ctx.fill();ctx.fillStyle='#ffd21a';ctx.beginPath();ctx.arc(0,5,3.8,Math.PI,TAU);ctx.fill();ctx.restore();}return;
 case 'island':{if(!o.spr||o.sprK!==K){o.spr=makeIsland(o);o.sprK=K;}""")
# ---- techo de las cuevas (encima de las motos) ----
h = rep(h, " if(CIRC)drawCircTop(Zn);\n", " for(const cv2 of Zn.caves||[])if(cv2.y+cv2.h/2+30>camTop&&cv2.y-cv2.h/2-30<camTop+VH)drawCave(cv2);\n if(CIRC)drawCircTop(Zn);\n")
h = rep(h, "function makeIsland(o){", """function drawCave(o){if(!o.spr||o.sprK!==K){const w=o.x1-o.x0,hh=o.h;o.spr=sprite(w+20,hh+40,g=>{const q=rng(o.s);
  const body=()=>{g.beginPath();g.moveTo(-w/2,-hh/2-8);for(let i=0;i<=10;i++){const x=-w/2+i/10*w;g.lineTo(x,-hh/2+(q()-.5)*10);}g.lineTo(w/2,hh/2);for(let i=10;i>=0;i--){const x=-w/2+i/10*w;g.lineTo(x,hh/2+(q()-.5)*10);}g.closePath();};
  g.save();g.globalAlpha=.62;g.fillStyle='#4a3d33';body();g.fill();g.restore();
  g.save();body();g.clip();const cols=['#8c877d','#6b665d','#a39e93','#7d786e','#5b564e'];for(let i=0;i<70;i++){g.globalAlpha=.32;g.fillStyle=cols[i%5];g.beginPath();g.ellipse((q()-.5)*w,(q()-.5)*hh,6+q()*12,4+q()*8,q()*3,0,TAU);g.fill();}
   g.globalAlpha=1;for(const s of[-1,1]){const y0=s*hh/2,gg=g.createLinearGradient(0,y0,0,y0-s*34);gg.addColorStop(0,'#3b332c');gg.addColorStop(.55,'#2a241f');gg.addColorStop(1,'rgba(20,16,12,0)');g.fillStyle=gg;g.fillRect(-w/2,s<0?y0:y0-34,w,34);
    for(let i=0;i<8;i++){g.fillStyle=cols[(i+2)%5];g.beginPath();g.ellipse(-w/2+(i+.5)*w/8,y0-s*4,7+q()*4,5+q()*3,0,0,TAU);g.fill();}}g.restore();
  g.strokeStyle='rgba(20,16,12,.55)';g.lineWidth=2;body();g.stroke();});o.sprK=K;}
 ctx.drawImage(o.spr.c,(o.x0+o.x1)/2-o.spr.w/2,o.y-o.spr.h/2,o.spr.w,o.spr.h);
 if(!G.demo){ctx.save();ctx.font='800 12px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillStyle='rgba(255,230,150,.9)';ctx.fillText('CUEVA',(o.x0+o.x1)/2,o.y+o.h/2+14);ctx.restore();}}
function makeIsland(o){""")
open(H, 'w').write(h); print('ok')
# --- ajustes tras probar ---
h = open(H).read()
h = rep(h, "fu+=1500+r()*700){if(isRes(fu)", "fu+=2100+r()*800){if(isRes(fu)")
h = rep(h, "function drawBolts(){const B=G.bolts||[];if(!B.length)return;ctx.save();const tx=x=>(x-camX)*K,ty=y=>(y-camTop)*K;\n",
 """function drawBolts(){const B=G.bolts||[];ctx.save();const tx=x=>(x-camX)*K,ty=y=>(y-camTop)*K;
 {const O=G.zone.objs;for(let i=findStart(O,camTop-80);i<O.length&&O[i].y<camTop+VH+80;i++){const o=O[i];if(o.t!=='swell')continue;const yy=ty(o.y),h2=o.h/2*K,span=WG+80;ctx.save();ctx.fillStyle='rgba(170,205,255,.10)';ctx.fillRect(0,yy-h2,cv.width,h2*2);ctx.strokeStyle='rgba(225,240,255,.6)';ctx.lineWidth=2*K;ctx.lineCap='round';
  for(let j=0;j<18;j++){const ry=yy-h2+8*K+((j*37)%(o.h-16))*K,xx=(-40+((((j*71+G.t*o.dir*110)%span)+span)%span)-camX)*K;ctx.beginPath();ctx.moveTo(xx-o.dir*16*K,ry-4*K);ctx.quadraticCurveTo(xx,ry+3*K,xx+o.dir*16*K,ry-4*K);ctx.stroke();}
  ctx.fillStyle='rgba(232,244,255,.85)';ctx.font=`800 ${Math.round(18*K)}px "Saira Condensed",sans-serif`;ctx.textAlign='center';ctx.textBaseline='middle';for(let j=0;j<3;j++)ctx.fillText(o.dir>0?'›››':'‹‹‹',(70+j*125+((G.t*o.dir*40)%30)-camX)*K,yy);ctx.restore();}}
""")
open(H, 'w').write(h); print('ok ajustes')
