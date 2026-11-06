p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)

# ================= ZONAS =================
rep("{name:'TORMENTA',","""{name:'FORMENTOR',obj:'race3',goal:'Termina entre los 3 primeros hasta el faro de Formentor. Acantilados enormes y el islote de Es Colomer, que puedes rodear por los dos lados.',len:16000,riv:5,bar:null,theme:'tram',tod:'golden',skill:.92,island:1,isleTheme:'cove',faro:1,finish:'FARO DE FORMENTOR'},
 {name:'SA CALOBRA',obj:'time',goal:'Cruza el cañón del Torrent de Pareis antes de que se acabe el tiempo. Paredes de roca a los dos lados y muy poco sitio.',len:13000,riv:0,bar:null,theme:'tram',tod:'noon',pace:185,canyon:1,finish:'SA CALOBRA'},
 {name:'CABRERA',obj:'race3',goal:'Termina entre los 3 primeros por el parque nacional de Cabrera. No entres en las zonas protegidas de boyas amarillas: multa de 500 PTA.',len:16000,riv:5,bar:null,theme:'cove',tod:'afternoon',skill:.9,cab:1,finish:'CABRERA'},
 {name:'PORTALS',obj:'time',goal:'Cruza el puerto de Portals antes de que se acabe el tiempo esquivando los superyates que entran y salen.',len:14000,riv:0,bar:null,theme:'port',tod:'afternoon',pace:195,supers:1,finish:'PORTALS'},
 {name:'TORMENTA',""")
rep("let best=Math.max(0,Math.min(15,","let best=Math.max(0,Math.min(19,")
s=s.replace("'ct_ghost_'+G.zi","'ct_ghost_'+ZONES[G.zi].name").replace("'ct_ghost_'+zi","'ct_ghost_'+ZONES[zi].name")
rep("add({t:'island',x:(L+RX)/2+4,y:-cu,rx,ry,seed:(r()*1e6)|0,theme:Z.theme});","add({t:'island',x:(L+RX)/2+4,y:-cu,rx,ry,seed:(r()*1e6)|0,theme:Z.isleTheme||Z.theme});")
# cañón (pared derecha)
rep("zone.cliffK=y=>","zone.rwall=null;if(Z.canyon){const nw=noise1(seed+21);zone.rwall=y=>{const u=-y,k=sm(500,1000,u)*sm(len-300,len-800,u),w=125+28*nw(u/380)+10*nw(u/90);return zone.shore(y)+lerp(560,w,k);};}\n zone.cliffK=y=>")
rep("const L=zone.shore(-u)+36,R=WG-24;let k=pick();","const L=zone.shore(-u)+36,R=Math.min(WG-24,zone.rwall?zone.rwall(-u)-30:999);let k=pick();")
rep("const ex=(VW>WG?WG+(VW-WG)/2:WG)-11;if(c.x>ex){c.x=ex;",
    "if(Zn.rwall){const rw=Zn.rwall(c.y)-11;if(c.x>rw){c.x=rw;if(c.h>0)c.h=-Math.abs(c.h)*.4;c.va=c.h;if(c.v>120&&c.air<=0){c.v*=.55;if(c.isP){Snd.bump();G.shake=4;}}}}\n const ex=(VW>WG?WG+(VW-WG)/2:WG)-11;if(c.x>ex){c.x=ex;")
rep("function aiCtl(c,dt){const Zn=G.zone,L=Zn.shore(c.y-120)+30,R=WG-26;","function aiCtl(c,dt){const Zn=G.zone,L=Zn.shore(c.y-120)+30,R=Math.min(WG-26,Zn.rwall?Zn.rwall(c.y-120)-30:999);")
rep(" // bar ring",""" if(Zn.rwall){const xr=(VW>WG?WG+(VW-WG)/2:WG)+40,y0=camTop-20,y1=camTop+VH+20;
  ctx.save();for(let y=Math.floor(y0/6)*6;y<y1;y+=6){const x=Zn.rwall(y);if(x>xr)continue;const gg=ctx.createLinearGradient(x-60,0,x,0);gg.addColorStop(0,'rgba(8,24,40,0)');gg.addColorStop(1,'rgba(8,24,40,.45)');ctx.fillStyle=gg;ctx.fillRect(x-60,y,61,6.5);}
  ctx.beginPath();ctx.moveTo(xr,y0);for(let y=y0;y<=y1;y+=5)ctx.lineTo(Math.min(xr,Zn.rwall(y)),y);ctx.lineTo(xr,y1);ctx.closePath();const rg=ctx.createLinearGradient(0,0,80,0);ctx.fillStyle='#8c877d';ctx.fill();ctx.clip();
  for(let cy=Math.floor(y0/26);cy<=Math.floor(y1/26);cy++)for(let k=0;k<5;k++){const h=hash2(cy,k,Zn.seed),x=Zn.rwall(cy*26)+4+h*120,y=cy*26+hash2(k,cy,3)*26,sz=6+hash2(cy+k,k,5)*12;ctx.fillStyle=['#a39e93','#7d786e','#b8b3a8','#6b665d','#948f84'][(hash2(cy,k,7)*5)|0];ctx.globalAlpha=.85;ctx.beginPath();ctx.ellipse(x,y,sz,sz*.6,hash2(k,cy,9)*3,0,TAU);ctx.fill();}
  ctx.globalAlpha=1;for(let y=Math.floor(y0/5)*5;y<y1;y+=5){const x=Zn.rwall(y);const gg=ctx.createLinearGradient(x,0,x+26,0);gg.addColorStop(0,'rgba(28,24,20,.65)');gg.addColorStop(1,'rgba(28,24,20,0)');ctx.fillStyle=gg;ctx.fillRect(x,y,27,5.5);}
  for(let cy=Math.floor(y0/40);cy<=Math.floor(y1/40);cy++){const h=hash2(cy,11,Zn.seed);if(h<.5)continue;const x=Zn.rwall(cy*40)+30+h*70,y=cy*40;ctx.fillStyle=h>.75?'#2f5a26':'#3f7f35';ctx.beginPath();ctx.arc(x,y,4+h*4,0,TAU);ctx.fill();}
  ctx.restore();ctx.fillStyle='rgba(255,255,255,.7)';for(let y=Math.floor(y0/3)*3;y<y1;y+=3){const x=Zn.rwall(y),h=hash2(Math.round(y),5,Zn.seed);if(x>xr)continue;ctx.beginPath();ctx.arc(x-1-h*3,y,1+h*1.4,0,TAU);ctx.fill();}}
 // bar ring""")
# Cabrera: islotes y zonas protegidas ; castillo
rep(" if(Z.island)island(Math.round(len*.45),58,220);",""" if(Z.cab){for(let cu=1400;cu<len-1000;cu+=1500+r()*500){const L=zone.shore(-cu);if(r()<.5){const rx=30+r()*14,ry=60+r()*40,x=lerp(L+rx+80,RX-rx-80,r());add({t:'island',x,y:-cu,rx,ry,seed:(r()*1e6)|0,theme:'cove'});resv.push([cu-ry-150,cu+ry+150]);}else{const rx=46+r()*20,ry=80+r()*50,x=lerp(L+rx+70,RX-rx-70,r());add({t:'nozone',x,y:-cu,rx,ry,fined:0,s:(r()*1e6)|0});resv.push([cu-ry-120,cu+ry+120]);}}}
 if(Z.faro){add({t:'faro',x:zone.shore(-(len-160))-34,y:-(len-160)});}
 if(Z.supers){for(let su=1200;su<len-700;su+=850+r()*450){const dir=r()<.5?1:-1;M.push({t:'super',x:dir>0?-140-r()*200:WG+140+r()*200,y:-su,vx:dir*(32+r()*16),vy:0,flash:0});resv.push([su-90,su+90]);}}
 if(Z.island)island(Math.round(len*.45),58,220);""")
rep("zone.big=zone.objs.filter(o=>o.t==='island'||o.t==='pass');","zone.big=zone.objs.filter(o=>o.t==='island'||o.t==='pass'||o.t==='nozone');")
rep("for(const o of Zn.big||[]){const ext=o.t==='island'?o.ry+40:o.h;","for(const o of Zn.big||[]){const ext=o.ry?o.ry+40:o.h;")
rep("if(o.t!=='island'&&o.t!=='pass')drawObj(o);","if(o.t!=='island'&&o.t!=='pass'&&o.t!=='nozone')drawObj(o);")
rep("   if(o.t==='island'||o.t==='pass')continue;","   if(o.t==='island'||o.t==='pass'||o.t==='nozone')continue;")
rep("if(Math.abs(c.y-o.y)>(o.ry||o.h)+30)continue;","if(Math.abs(c.y-o.y)>(o.ry||o.h)+30)continue;\n   if(o.t==='nozone'){if(c.isP&&!G.demo&&!o.fined&&c.z<.3){const dx=(c.x-o.x)/o.rx,dy=(c.y-o.y)/o.ry;if(dx*dx+dy*dy<1){o.fined=1;pop(c.x,c.y-50,'¡ZONA PROTEGIDA!','#ffd21a');fine();}}continue;}")
rep(" D.sort((a,b)=>a.y-b.y);"," if(Z.cab){const cu=Math.round(len*.22);D.push({t:'castle',x:zone.shore(-cu)-44,y:-cu,s:3});}\n D.sort((a,b)=>a.y-b.y);")
rep(" // movers\n for(const o of Zn.movers){"," for(const o of Zn.movers)if(o.t==='super'){if(o.vx<0&&o.x<-260)o.x=WG+260;else if(o.vx>0&&o.x>WG+260)o.x=-260;}\n // movers\n for(const o of Zn.movers){")
rep("case 'croc':return","case 'super':return Math.abs(o.x-x)<80+rad*.5&&Math.abs(o.y-y)<22+rad;case 'croc':return")
rep("crash(c,{patrol:'¡CHOQUE!',","crash(c,{super:'¡SUPERYATE!',patrol:'¡CHOQUE!',")
rep("Z.aus?{coins:3,ramp:6,surfer:2,coral:1.4,croc:.8,rocks:.4}:","Z.aus?{coins:3,ramp:6,surfer:2,coral:1.4,croc:.8,rocks:.4}:Z.canyon?{coins:3.4,rocks:2.4,ramp:.8,kayak:.8,boat:.4}:Z.cab?{coins:3,rocks:1.4,boat:1,yacht:.5,kayak:.6,ramp:1}:Z.supers?{coins:3,yacht:1.6,boat:1.4,ramp:1,kayak:.5,rocks:.3}:")
# castillo (decoración)
rep("function drawDeco(g,d){const q=rng(d.s||((d.x*31+d.y*17)|0));","""function drawDeco(g,d){const q=rng(d.s||((d.x*31+d.y*17)|0));
 if(d.t==='castle'){g.save();g.translate(d.x,d.y);g.fillStyle='rgba(40,20,0,.3)';g.fillRect(-12,-12,32,32);g.fillStyle='#b9a27e';g.fillRect(-16,-16,32,32);g.fillStyle='#9c8461';for(let i=0;i<4;i++){g.fillRect(-16+i*9,-19,5,4);g.fillRect(-16+i*9,15,5,4);g.fillRect(-19,-16+i*9,4,5);g.fillRect(15,-16+i*9,4,5);}g.fillStyle='#cdb892';g.fillRect(-10,-10,20,20);g.strokeStyle='#5b3a22';g.lineWidth=1.5;g.beginPath();g.moveTo(6,-6);g.lineTo(6,-24);g.stroke();g.fillStyle='#e3202b';g.fillRect(6,-24,10,6);g.fillStyle='#ffd21a';g.fillRect(6,-22,10,2);g.restore();return;}""")
# dibujo: zona protegida, faro, superyate
rep(" case 'posi':{",""" case 'nozone':{const q=rng(o.s||7);ctx.save();ctx.translate(o.x,o.y);ctx.fillStyle='rgba(120,240,200,.18)';ctx.beginPath();ctx.ellipse(0,0,o.rx,o.ry,0,0,TAU);ctx.fill();ctx.strokeStyle='rgba(20,90,60,.35)';ctx.lineWidth=1.2;for(let i=0;i<22;i++){const a=q()*TAU,d=Math.sqrt(q())*.8,x=Math.cos(a)*o.rx*d,y=Math.sin(a)*o.ry*d,sw=Math.sin(t*1.5+i)*2;ctx.beginPath();ctx.moveTo(x,y+4);ctx.quadraticCurveTo(x+sw,y,x+sw*1.5,y-5);ctx.stroke();}
  const n=Math.round((o.rx+o.ry)/7);for(let i=0;i<n;i++){const a=i/n*TAU,x=Math.cos(a)*o.rx,y=Math.sin(a)*o.ry;ctx.fillStyle='#ffd21a';ctx.beginPath();ctx.arc(x,y,3.4,0,TAU);ctx.fill();ctx.fillStyle='rgba(255,255,255,.6)';ctx.beginPath();ctx.arc(x-1,y-1,1.1,0,TAU);ctx.fill();}
  ctx.fillStyle='rgba(8,22,48,.72)';ctx.beginPath();ctx.roundRect(-46,-9,92,18,8);ctx.fill();ctx.fillStyle='#ffd21a';ctx.font='800 11px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('ZONA PROTEGIDA',0,1);ctx.restore();}return;
 case 'faro':{ctx.save();ctx.translate(o.x,o.y);ctx.fillStyle='rgba(0,0,0,.25)';ctx.fillRect(-22,-10,30,26);ctx.fillStyle='#ece7dc';ctx.fillRect(-26,-14,28,26);ctx.fillStyle='#c4683c';ctx.fillRect(-26,-14,28,5);
  ctx.fillStyle='rgba(0,0,0,.25)';ctx.beginPath();ctx.arc(12,4,12,0,TAU);ctx.fill();ctx.fillStyle='#ffffff';ctx.beginPath();ctx.arc(8,0,11,0,TAU);ctx.fill();ctx.strokeStyle='#cfc9bc';ctx.lineWidth=1.5;ctx.stroke();ctx.fillStyle='#2a3140';ctx.beginPath();ctx.arc(8,0,6.5,0,TAU);ctx.fill();ctx.fillStyle='#ffe58a';ctx.beginPath();ctx.arc(8,0,3.6,0,TAU);ctx.fill();
  const a=t*1.1;ctx.globalCompositeOperation='lighter';const gg=ctx.createRadialGradient(8,0,4,8,0,240);gg.addColorStop(0,'rgba(255,240,170,.5)');gg.addColorStop(1,'rgba(255,240,170,0)');ctx.fillStyle=gg;ctx.beginPath();ctx.moveTo(8,0);ctx.arc(8,0,240,a-.16,a+.16);ctx.closePath();ctx.fill();ctx.globalCompositeOperation='source-over';ctx.restore();}return;
 case 'super':{const d=o.vx>0?1:-1;ctx.save();ctx.translate(o.x,o.y);ctx.rotate(d>0?Math.PI/2:-Math.PI/2);
  ctx.fillStyle='rgba(0,20,50,.28)';ctx.beginPath();ctx.ellipse(6,8,24,84,0,0,TAU);ctx.fill();for(let i=0;i<12;i++){ctx.globalAlpha=.55;ctx.drawImage(SP.dot.c,Math.sin(i*1.7+t*5)*14-4,80+i*7-4,8,8);}ctx.globalAlpha=1;
  ctx.fillStyle='#f7f8fa';ctx.beginPath();ctx.moveTo(0,-84);ctx.bezierCurveTo(18,-62,22,-20,22,10);ctx.lineTo(21,72);ctx.quadraticCurveTo(20,80,0,80);ctx.quadraticCurveTo(-20,80,-21,72);ctx.lineTo(-22,10);ctx.bezierCurveTo(-22,-20,-18,-62,0,-84);ctx.fill();ctx.strokeStyle='#1b2a44';ctx.lineWidth=2;ctx.stroke();
  ctx.fillStyle='#e3e7ec';ctx.beginPath();ctx.roundRect(-15,-42,30,92,10);ctx.fill();ctx.fillStyle='#1b2a44';ctx.beginPath();ctx.roundRect(-12,-36,24,10,4);ctx.fill();ctx.fillStyle='#c9a77a';ctx.fillRect(-15,54,30,20);ctx.fillStyle='#33a3ff';ctx.beginPath();ctx.roundRect(-8,58,16,10,3);ctx.fill();
  ctx.strokeStyle='#ff7a1a';ctx.lineWidth=1.6;ctx.beginPath();ctx.arc(0,-6,10,0,TAU);ctx.stroke();ctx.fillStyle='#ff7a1a';ctx.font='800 11px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('H',0,-5);ctx.restore();}return;
 case 'posi':{""")

# ================= PORTADAS =================
rep(" {tag:'CONTRARRELOJ DE NOCHE',",""" {tag:'CARRERA · TOP 3',sky:['#3b4fa8','#ffb874'],sea:['#4f8fc6','#0d3a78'],sun:[300,72,'#ffd27a'],land:'formentor'},
 {tag:'CONTRARRELOJ',sky:['#2f8de6','#c9ecff'],sea:['#3fb4d8','#0a4f9e'],sun:[200,8,'#ffffff'],land:'calobra'},
 {tag:'CARRERA · TOP 3',sky:['#3a7fd0','#ffd9a8'],sea:['#5ab8dc','#0a4a8e'],sun:[330,46,'#fff0c8'],land:'cabrera'},
 {tag:'CONTRARRELOJ',sky:['#3f7fd6','#ffdcae'],sea:['#6fc3e2','#0b4f98'],sun:[60,40,'#fff2cc'],land:'portals'},
 {tag:'CONTRARRELOJ DE NOCHE',""")
rep("function drawCover(c,zi){","""function cvSuper(g,x,y,s){g.save();g.translate(x,y);g.scale(s,s);g.fillStyle='rgba(255,255,255,.7)';g.beginPath();g.ellipse(0,2,96,5,0,0,TAU);g.fill();
 g.fillStyle='#f7f8fa';g.beginPath();g.moveTo(-90,0);g.lineTo(80,0);g.quadraticCurveTo(100,-4,108,-22);g.lineTo(-88,-22);g.closePath();g.fill();g.fillStyle='#1b2a44';g.fillRect(-86,-12,186,4);
 g.fillStyle='#eef1f5';g.beginPath();g.moveTo(-70,-22);g.lineTo(70,-22);g.lineTo(58,-38);g.lineTo(-60,-38);g.closePath();g.fill();g.fillStyle='#1b2a44';g.fillRect(-56,-33,108,6);
 g.fillStyle='#e3e7ec';g.beginPath();g.moveTo(-40,-38);g.lineTo(40,-38);g.lineTo(30,-50);g.lineTo(-34,-50);g.closePath();g.fill();g.fillStyle='#1b2a44';g.fillRect(-30,-46,58,5);g.fillStyle='#9aa6b5';g.fillRect(-4,-62,3,12);g.restore();}
function drawCover(c,zi){""")
rep(" if(L==='storm'){cvRidge(g,q,-20,420,HZ,40,8,'#111a30');",""" if(L==='formentor'){cvMount(g,q,-10,250,HZ+2,8,'#5c5550','rgba(30,26,22,.5)');g.fillStyle=rgbaH(C.sky[1],.18);g.fillRect(0,0,260,HZ);g.fillStyle='#ffffff';g.fillRect(232,4,7,18);g.fillStyle='#c4683c';g.fillRect(231,2,9,4);g.save();g.globalCompositeOperation='lighter';const lg=g.createRadialGradient(235,6,0,235,6,70);lg.addColorStop(0,'rgba(255,240,170,.7)');lg.addColorStop(1,'rgba(255,240,170,0)');g.fillStyle=lg;g.beginPath();g.moveTo(235,6);g.arc(235,6,70,-.25,.25);g.closePath();g.fill();g.restore();cvRidge(g,q,300,370,HZ,18,3,'#6a6158');}
 if(L==='calobra'){for(const side of[-1,1]){g.beginPath();if(side<0){g.moveTo(0,H);g.lineTo(0,0);for(let y=0;y<=HZ+20;y+=6)g.lineTo(150-y*.15+(q()-.5)*8+(y>HZ?0:0),y);g.lineTo(170,H);}else{g.moveTo(400,H);g.lineTo(400,0);for(let y=0;y<=HZ+20;y+=6)g.lineTo(250+y*.15+(q()-.5)*8,y);g.lineTo(230,H);}g.closePath();const wg=g.createLinearGradient(side<0?0:400,0,side<0?170:230,0);wg.addColorStop(0,'#5f574d');wg.addColorStop(1,'#8c847a');g.fillStyle=wg;g.fill();g.strokeStyle='rgba(40,34,28,.4)';g.lineWidth=1.2;for(let i=0;i<14;i++){const x=side<0?q()*140:260+q()*140;g.beginPath();g.moveTo(x,q()*40);g.lineTo(x+(q()-.5)*20,HZ+30+q()*80);g.stroke();}}
  for(let i=0;i<8;i++){g.fillStyle=i%2?'#3b5a33':'#2f4b2a';g.beginPath();g.arc(q()<.5?20+q()*90:300+q()*90,10+q()*60,3+q()*3,0,TAU);g.fill();}}
 if(L==='cabrera'){cvCliff(g,q,-1,0,150,40,HZ+6);g.fillStyle='#b9a27e';g.fillRect(36,22,22,22);for(let i=0;i<4;i++)g.fillRect(36+i*6,18,4,4);g.fillStyle='#e3202b';g.fillRect(50,8,9,5);g.fillStyle='#5b3a22';g.fillRect(49,8,1.5,14);cvRidge(g,q,230,330,HZ,14,3,'#a8774c');cvRidge(g,q,340,400,HZ,10,3,'#b07f52');}
 if(L==='portals'){cvRidge(g,q,-20,420,HZ-2,26,4,'#8fa86f');cvCity(g,q,0,400,HZ,22);g.fillStyle='#d8d2c4';g.fillRect(0,HZ-3,400,3);for(let i=0;i<10;i++){g.fillStyle='#ffffff';g.fillRect(10+i*38,HZ-6,24,4);g.fillStyle='#9aa6b5';g.fillRect(20+i*38,HZ-18,1.4,12);}cvPalm(g,30,HZ+2,.7);cvPalm(g,370,HZ+2,.7);}
 if(L==='storm'){cvRidge(g,q,-20,420,HZ,40,8,'#111a30');""")
rep(" else if(L==='form'){",""" else if(L==='formentor'){cvRival(g,q,rv(0),140,140,.24,-.05);cvRival(g,q,rv(1),210,154,.28,-.06);hero(295,172,.42,-.15,0);}
 else if(L==='calobra'){for(let i=0;i<3;i++){g.fillStyle='#8d8577';g.beginPath();g.ellipse(170+i*40,HZ+20+i*12,8,4,0,0,TAU);g.fill();}hero(205,170,.4,-.12,0);}
 else if(L==='cabrera'){for(let i=0;i<9;i++){g.fillStyle='#ffd21a';g.beginPath();g.arc(170+i*24,HZ+28+Math.sin(i)*3,2.6+i*.2,0,TAU);g.fill();}cvRival(g,q,rv(0),150,146,.26,-.05);hero(290,172,.42,-.15,0);}
 else if(L==='portals'){cvSuper(g,170,HZ+34,.8);hero(285,172,.42,-.15,0);}
 else if(L==='form'){""")
open(p,'w').write(s);print('ok')
