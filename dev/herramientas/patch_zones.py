p='costa-turbo.html';s=open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:120])
    s=s.replace(a,b)
# ---------- DATA
a=s.index('const ZONES=[');b=s.index('];',a)+2
s=s[:a]+'''const ZONES=[
 {name:'EL PUERTO',obj:'time',goal:'Llega a la meta antes de que se acabe el tiempo.',len:15000,riv:5,bar:'jj',theme:'port',tod:'morning',skill:.84,pace:205,piri:1},
 {name:'LA CALA',obj:'slalom',goal:'Pasa por dentro de las boyas. Cada una que falles te quita 1 segundo.',len:11000,riv:0,bar:'roxy',theme:'cove',tod:'noon',pace:170},
 {name:'CARRERA AL MAGO',obj:'race3',goal:'Llega a El Mago entre los 3 primeros. La isla la puedes rodear por los dos lados y antes de la meta hay muchos barcos fondeados.',len:16000,riv:5,bar:null,theme:'cove',tod:'noon',skill:.88,piri:1,island:1,anchored:1,finish:'EL MAGO'},
 {name:'GRAN CARRERA',obj:'race3',goal:'Termina entre los 3 primeros.',len:16000,riv:5,bar:'jj',theme:'beach',tod:'afternoon',skill:.9,piri:1},
 {name:'PERSECUCIÓN',obj:'chase',goal:'Llega a la meta sin que la policía te pille 3 veces.',len:14000,riv:0,bar:'roxy',theme:'cove',tod:'afternoon'},
 {name:'OLAS GIGANTES',obj:'jumps',goal:'Haz 6 saltos en las olas y llega antes de que se acabe el tiempo.',len:15000,riv:0,bar:'jj',theme:'beach',tod:'sunset',pace:200,piri:1},
 {name:'CARRERA ES TRENC',obj:'race2',goal:'Termina entre los 2 primeros. Hay dos pasos estrechos y dos islas, y las chicas de los flotadores te distraen.',len:16000,riv:5,bar:null,theme:'trenc',tod:'tropical',skill:.9,piri:1,islands:2,passes:2,floats:1,finish:'ES TRENC',shallowW:250},
 {name:'TORMENTA',obj:'time',goal:'Cruza la tormenta de noche antes de que se acabe el tiempo.',len:14000,riv:0,bar:'roxy',theme:'cove',tod:'night',pace:195},
 {name:'LA FINAL',obj:'win',goal:'Gana a El Tiburón: tienes que llegar el primero.',len:17000,riv:5,bar:null,theme:'port',tod:'golden',skill:.95,boss:1}
];
const AVATARS=[
 {id:'alex',name:'Álex',face:{skin:'#e8b48c',hair:'#4a2a14',style:'short',vest:'#ff7a1a'}},
 {id:'dani',name:'Dani',face:{skin:'#c98d62',hair:'#111111',style:'curly',vest:'#33d6ff'}},
 {id:'marc',name:'Marc',face:{skin:'#f2c6a2',hair:'#e8c35a',style:'short',glasses:1,vest:'#7be35a'}},
 {id:'leo',name:'Leo',face:{skin:'#a8714a',hair:'#1b1b1b',style:'buzz',beard:1,vest:'#e3202b'}},
 {id:'lucia',name:'Lucía',face:{skin:'#f0c09a',hair:'#5a3218',style:'long',vest:'#ff3f8e'}},
 {id:'sara',name:'Sara',face:{skin:'#f2c6a2',hair:'#f2cf63',style:'pony',glasses:1,vest:'#1e5eff'}},
 {id:'nerea',name:'Nerea',face:{skin:'#d9a07a',hair:'#111111',style:'bob',vest:'#ffd21a'}},
 {id:'vega',name:'Vega',face:{skin:'#efbf98',hair:'#b5402a',style:'long',vest:'#7b3fe4'}}
];
const MOTO_DESC={brava:'Equilibrada y fiable.',inferno:'Pura potencia. Acelera como nadie.',avispa:'Agresiva en las curvas. Pica fuerte.',oceano:'La más rápida en recta.',marea:'Gira y salta como nadie.',solar:'Turbo largo y mucha cabeza.',veneno:'Ligera y nerviosa. Sale disparada.',sombra:'Silenciosa y fría en las curvas.'};'''+s[b:]
rep(" golden:{deep:'#1679b8',deep2:'#0c4f94',tint:'rgba(255,190,80,.13)'}"," golden:{deep:'#1679b8',deep2:'#0c4f94',tint:'rgba(255,190,80,.13)'},\n tropical:{deep:'#0cb8e4',deep2:'#0a80d8',tint:null}")
# ---------- ZONE BUILD
rep("const len=Math.round(Z.len*(1+lap*.08)),SEG=Z.theme==='port'?1500:Z.theme==='beach'?1700:1900;","const len=Math.round(Z.len*(1+lap*.08)),SEG=Z.theme==='port'?1500:Z.theme==='beach'?1700:Z.theme==='trenc'?2000:1900;")
rep("const kindOf=k=>{k=Math.max(0,k);if(Z.theme==='port')","const kindOf=k=>{k=Math.max(0,k);if(Z.theme==='trenc')return 'beach';if(Z.theme==='port')")
rep("kind==='beach'?70+15*n1(u/260)+4*n2(u/90):","kind==='beach'?(Z.theme==='trenc'?64+5*n1(u/700):70+15*n1(u/260)+4*n2(u/90)):")
rep(" const free=u=>Math.abs(u-barU)>300&&u>420&&u<len-260;",
""" const resv=[],isRes=u=>resv.some(([a,b])=>u>a&&u<b);
 const free=u=>Math.abs(u-barU)>300&&u>420&&u<len-260&&!isRes(u);
 const RX=WG;
 const island=(cu,rx,ry)=>{const L=zone.shore(-cu);add({t:'island',x:(L+RX)/2+4,y:-cu,rx,ry,seed:(r()*1e6)|0,theme:Z.theme});resv.push([cu-ry-170,cu+ry+170]);};
 if(Z.island)island(Math.round(len*.45),58,220);
 if(Z.islands){island(Math.round(len*.27),50,150);island(Math.round(len*.63),52,150);}
 if(Z.passes){for(const f of[.45,.8]){const cu=Math.round(len*f),L=zone.shore(-cu);add({t:'pass',y:-cu,gx:lerp(L+70,RX-70,.2+r()*.6),gw:76,h:110});resv.push([cu-260,cu+220]);}}
 if(Z.anchored){resv.push([len-1750,len+10]);for(let au=len-1650;au<len-250;au+=130+r()*40){const L=zone.shore(-au)+20,R=RX-18,gap=lerp(L+50,R-50,r()),xs=[];for(let k=0;k<12&&xs.length<3;k++){const x=lerp(L,R,r());if(Math.abs(x-gap)<58||xs.some(v=>Math.abs(v-x)<46))continue;xs.push(x);}for(const x of xs)add({t:r()<.6?'sail':'motor',x,y:-au+(r()-.5)*30,rot:(r()-.5)*.8});}}
 if(Z.piri){let pu=Math.round(len*.3);while(isRes(pu)||Math.abs(pu-barU)<400)pu+=300;const L=zone.shore(-pu),x=lerp(L+60,RX-110,r());add({t:'piri',x,y:-pu,rx:x+52,gift:0});resv.push([pu-200,pu+200]);}""")
rep("Z.obj==='chase'?{coins:3,ramp:1.4,rocks:2,boat:1.4,yacht:.7,kayak:.7,patrol:.4}:{coins:3.5,ramp:1.5,rocks:1.6,boat:1.2,yacht:.8,kayak:.8,patrol:1};",
    "Z.obj==='chase'?{coins:3,ramp:1.4,rocks:2,boat:1.4,yacht:.7,kayak:.7,patrol:.4}:Z.floats?{coins:3,ramp:1.2,rocks:.6,boat:.6,yacht:1.2,kayak:.5,patrol:.6,float:3.4}:{coins:3.5,ramp:1.5,rocks:1.6,boat:1.2,yacht:.8,kayak:.8,patrol:1};")
rep("  else if(k==='kayak'){M.push(","  else if(k==='float'){add({t:'float',x:lerp(L+30,R-30,r()),y:-u,kind:r()<.5?0:1,hair:['#f2cf63','#5a3218','#111111','#b5402a'][(r()*4)|0],bik:['#ff3f8e','#22c4ff','#ffd21a','#7be35a','#ff7a1a'][(r()*5)|0],rot:(r()-.5)*1.2,dist:0,wave:0,txt:''});u+=170;}\n  else if(k==='kayak'){M.push(")
rep(" zone.objs.sort((a,b)=>a.y-b.y);zone.gatesTotal=zone.objs.filter(o=>o.t==='gate').length;",
    " zone.objs.sort((a,b)=>a.y-b.y);zone.gatesTotal=zone.objs.filter(o=>o.t==='gate').length;zone.big=zone.objs.filter(o=>o.t==='island'||o.t==='pass');")
rep("  else if(kd==='beach'){const v=dr();if(v<.3)D.push({t:'umb'","  else if(kd==='beach'&&Z.theme==='trenc'&&dr()<.24){if(dr()<.55)D.push({t:'girl',x:sx-10-dr()*30,y,hair:['#f2cf63','#5a3218','#111111','#b5402a'][(dr()*4)|0],bik:['#ff3f8e','#22c4ff','#ffd21a','#ff7a1a'][(dr()*4)|0],ph:dr()*6});else D.push({t:'grass',x:sx-58-dr()*40,y,s:(dr()*1e6)|0});}\n  else if(kd==='beach'){const v=dr();if(v<.3)D.push({t:'umb'")
rep("for(let y=y0-2;y<y1+2;y+=2){const sx=sh(y);g.drawImage(SP.shallow,sx-4,y,150,2.4);}","const shW=Zn.Z.shallowW||150;for(let y=y0-2;y<y1+2;y+=2){const sx=sh(y);g.drawImage(SP.shallow,sx-4,y,shW,2.4);}")
rep(" else if(d.t==='ybuoy'){"," else if(d.t==='girl'){g.fillStyle='rgba(60,40,10,.18)';g.beginPath();g.ellipse(d.x+3,d.y+9,5,2.4,0,0,TAU);g.fill();drawGirl(g,d.x,d.y,d.hair,d.bik,true,d.ph);}\n else if(d.t==='grass'){for(let i=0;i<9;i++){const a=-Math.PI/2+(q()-.5)*2.2,l=4+q()*6;g.strokeStyle=i%2?'#7aa04a':'#9bbf5a';g.lineWidth=1.2;g.beginPath();g.moveTo(d.x,d.y);g.lineTo(d.x+Math.cos(a)*l,d.y+Math.sin(a)*l);g.stroke();}}\n else if(d.t==='ybuoy'){")
# ---------- sprites
rep(" SP.kayak=sprite(30,48,g=>drawKayak(g));"," SP.kayak=sprite(30,48,g=>drawKayak(g));\n SP.motor=sprite(26,58,g=>drawMotor(g));\n SP.piri=sprite(60,80,g=>drawPiri(g));\n SP.jetP=sprite(32,68,g=>drawJet(g,playerSk()));")
rep("function drawKayak(g){","""function drawMotor(g){const p=()=>{g.beginPath();g.moveTo(0,-26);g.bezierCurveTo(8,-22,10,-8,10,4);g.lineTo(9,22);g.quadraticCurveTo(9,26,5,26);g.lineTo(-5,26);g.quadraticCurveTo(-9,26,-9,22);g.lineTo(-10,4);g.bezierCurveTo(-10,-8,-8,-22,0,-26);g.closePath();};
 p();g.fillStyle='#f6f7f9';g.fill();g.strokeStyle='rgba(0,0,0,.25)';g.lineWidth=.8;g.stroke();g.fillStyle='#1e5eff';g.fillRect(-9.6,6,1.6,16);g.fillRect(8,6,1.6,16);
 g.fillStyle='#22324a';g.beginPath();g.moveTo(-7,-4);g.quadraticCurveTo(0,-9,7,-4);g.lineTo(7,-1);g.lineTo(-7,-1);g.closePath();g.fill();g.fillStyle='#d9cfbd';g.beginPath();g.roundRect(-6,3,12,8,3);g.roundRect(-6,14,12,8,3);g.fill();g.fillStyle='#2b2f38';g.fillRect(-4,24,8,3);}
function drawPiri(g){g.fillStyle='rgba(0,20,50,.25)';g.beginPath();g.ellipse(4,6,16,34,0,0,TAU);g.fill();
 const hull=()=>{g.beginPath();g.moveTo(0,-36);g.bezierCurveTo(12,-30,15,-14,15,4);g.lineTo(14,28);g.quadraticCurveTo(13,34,7,34);g.lineTo(-7,34);g.quadraticCurveTo(-13,34,-14,28);g.lineTo(-15,4);g.bezierCurveTo(-15,-14,-12,-30,0,-36);g.closePath();};
 hull();g.fillStyle='#8a5a2b';g.fill();g.strokeStyle='#5e3a18';g.lineWidth=2;g.stroke();g.save();hull();g.clip();g.strokeStyle='rgba(60,30,10,.35)';g.lineWidth=.8;for(let x=-14;x<15;x+=3.5){g.beginPath();g.moveTo(x,-36);g.lineTo(x,34);g.stroke();}g.restore();
 g.fillStyle='#3a2210';for(const[x,y]of[[-17,-17],[17,-17],[-17,17],[17,17]]){g.beginPath();g.arc(x,y,2.6,0,TAU);g.fill();}
 const q=rng(5);g.fillStyle='rgba(0,0,0,.2)';g.fillRect(-20,-18,44,42);
 g.fillStyle='#d9b25a';g.beginPath();for(let i=0;i<=48;i++){const t=i/48*4,side=Math.floor(t)%4,f=t-Math.floor(t),j=(q()-.5)*2.4;let x,y;if(side===0){x=-21+42*f;y=-21+j;}else if(side===1){x=21+j;y=-21+42*f;}else if(side===2){x=21-42*f;y=21+j;}else{x=-21+j;y=21-42*f;}i?g.lineTo(x,y):g.moveTo(x,y);}g.closePath();g.fill();
 g.strokeStyle='#b8913a';g.lineWidth=.9;for(let i=0;i<70;i++){const a=q()*TAU,l=4+q()*20;g.beginPath();g.moveTo(Math.cos(a)*2,Math.sin(a)*2);g.lineTo(Math.cos(a)*l,Math.sin(a)*l);g.stroke();}
 g.strokeStyle='#efd18a';g.lineWidth=1;g.beginPath();g.moveTo(-21,-21);g.lineTo(21,21);g.moveTo(21,-21);g.lineTo(-21,21);g.stroke();g.fillStyle='#8a5a2b';g.beginPath();g.arc(0,0,3,0,TAU);g.fill();
 g.fillStyle='#ff3f8e';g.beginPath();g.moveTo(0,-2);g.lineTo(8,-6);g.lineTo(0,-9);g.closePath();g.fill();}
function drawFloat(g,o,t){g.save();g.translate(o.x,o.y);g.rotate(o.rot);g.fillStyle='rgba(0,20,50,.22)';g.beginPath();g.ellipse(3,4,15,15,0,0,TAU);g.fill();
 if(o.kind===0){g.strokeStyle='#ff7eb6';g.lineWidth=8;g.beginPath();g.arc(0,0,11,0,TAU);g.stroke();g.strokeStyle='rgba(255,255,255,.5)';g.lineWidth=2;g.beginPath();g.arc(0,0,12,-2.4,-1.2);g.stroke();
  g.strokeStyle='#ff7eb6';g.lineWidth=4;g.lineCap='round';g.beginPath();g.moveTo(0,-13);g.quadraticCurveTo(-2,-22,4,-24);g.stroke();g.fillStyle='#ff7eb6';g.beginPath();g.arc(5,-24,3.2,0,TAU);g.fill();g.fillStyle='#ffd21a';g.beginPath();g.moveTo(7,-25);g.lineTo(11,-23);g.lineTo(7,-22);g.fill();g.fillStyle='#111';g.beginPath();g.arc(5.5,-25,.8,0,TAU);g.fill();}
 else{g.strokeStyle='#f4c27a';g.lineWidth=8;g.beginPath();g.arc(0,0,11,0,TAU);g.stroke();g.strokeStyle='#ff6fae';g.lineWidth=5;g.beginPath();g.arc(0,0,11,.2,TAU-.4);g.stroke();for(let i=0;i<12;i++){const a=i*.52;g.fillStyle=['#fff','#33d6ff','#ffd21a','#7be35a'][i%4];g.fillRect(Math.cos(a)*11-.8,Math.sin(a)*11-.4,1.6,.8);}}
 g.restore();drawGirl(ctx,o.x,o.y-2,o.hair,o.bik,true,t*7+o.x);}
function drawKayak(g){""")
# ---------- hitObj
rep(" case 'kayak':return Math.abs(o.x-x)<20+rad*.5&&Math.abs(o.y-y)<7+rad;}return false;}",
    " case 'kayak':return Math.abs(o.x-x)<20+rad*.5&&Math.abs(o.y-y)<7+rad;case 'motor':return Math.abs(o.x-x)<9+rad&&Math.abs(o.y-y)<24+rad*.5;case 'piri':return Math.abs(o.x-x)<20+rad&&Math.abs(o.y-y)<34+rad*.5;case 'float':return Math.hypot(o.x-x,o.y-y)<14+rad;}return false;}")
# ---------- collisions
rep("   if(c.air>.0&&c.z>.35&&o.t!=='yacht')continue;",
"""   if(o.t==='island'){const ex=o.rx+10,ey=o.ry+10,dx=(c.x-o.x)/ex,dy=(c.y-o.y)/ey,d=Math.hypot(dx,dy);if(d<1&&c.z<.5){const k=1/(d||1);c.x=o.x+dx*k*ex;c.y=o.y+dy*k*ey;c.v*=1-4*dt;if(c.isP&&!G.demo&&!(c._isl>0)&&c.v>90){c._isl=.7;Snd.bump();G.shake=4;}}continue;}
   if(o.t==='pass'){if(c.z<.5&&Math.abs(c.y-o.y)<o.h/2+6){const gl=o.gx-o.gw/2,gr=o.gx+o.gw/2;if(c.x<gl+9||c.x>gr-9){if(c.prevY>=o.y+o.h/2-1){c.y=o.y+o.h/2+6;c.v*=.4;}else c.x=clamp(c.x,gl+9,gr-9);if(c.isP&&!G.demo&&!(c._isl>0)){c._isl=.7;Snd.bump();G.shake=5;pop(c.x,c.y-30,'¡ARENA!','#ff4757');}}}continue;}
   if(o.t==='piri'&&c.isP&&!G.demo&&!o.gift&&Math.hypot(c.x-o.rx,c.y-o.y)<38){o.gift=1;G.lives=Math.min(6,G.lives+1);G.turbo=Math.min(5,G.turbo+2);livesUI();turboUI();Snd.cash();Snd.pickup();msg('¡PIRI-PIRI!','+1 VIDA · +2 TURBOS','var(--gold)');}
   if(o.t==='float'&&c.isP&&!G.demo&&!o.dist&&Math.abs(c.y-o.y)<70&&Math.abs(c.x-o.x)<120){o.dist=1;o.wave=2.6;o.txt=['¡Guapo!','¡Holaaa!','¡Ven aquí!','¡Qué moto!','¡Llévame!'][(Math.random()*5)|0];c.distract=.8;c.distractDir=Math.sign(o.x-c.x)||1;Snd.girls();msg('¡TE DISTRAES!','','var(--pink)');}
   if(c.air>.0&&c.z>.35&&o.t!=='yacht')continue;""")
rep(" c.prevY=c.y;if(c.inv>0)c.inv-=dt;"," c.prevY=c.y;if(c.inv>0)c.inv-=dt;if(c._isl>0)c._isl-=dt;if(c.distract>0){c.distract-=dt;c.h+=c.distractDir*1.4*dt;}")
rep("for(const o of Zn.objs)if(o.t==='yacht'&&o.wave>0)o.wave-=dt;","for(const o of Zn.objs)if((o.t==='yacht'||o.t==='float')&&o.wave>0)o.wave-=dt;")
# ---------- AI
rep(" const O=Zn.objs,s=findStart(O,c.y-240);for(let i=s;i<O.length&&O[i].y<c.y-20;i++){const o=O[i];if(o.t==='coin'||o.t==='check'||o.t==='finish'||o.t==='ramp'||o.t==='can'||o.t==='fuel'||o.t==='gate')continue;const w=o.t==='yacht'?34:o.t==='sail'?20:o.t==='rock'?o.rad+14:14;",
""" let bigDone=false;for(const o of Zn.big||[]){if(o.t==='pass'){if(o.y<c.y-20&&o.y>c.y-520){c.ai.tx=o.gx;c.ai.re=Math.max(c.ai.re,.3);bigDone=true;break;}}else if(o.y+o.ry>c.y-560&&o.y-o.ry<c.y+20){if(c.ai.isl!==o){c.ai.isl=o;c.ai.side=Math.random()<.5?-1:1;}c.ai.tx=clamp(c.ai.side<0?o.x-o.rx-42:o.x+o.rx+42,L+8,R-8);c.ai.re=Math.max(c.ai.re,.3);bigDone=true;break;}}
 const O=Zn.objs,s=findStart(O,c.y-240);if(!bigDone)for(let i=s;i<O.length&&O[i].y<c.y-20;i++){const o=O[i];if(o.t==='coin'||o.t==='check'||o.t==='finish'||o.t==='ramp'||o.t==='can'||o.t==='fuel'||o.t==='gate'||o.t==='island'||o.t==='pass')continue;const w=o.t==='yacht'?34:o.t==='sail'?20:o.t==='rock'?o.rad+14:o.t==='piri'?30:o.t==='float'?20:o.t==='motor'?16:14;""")
# ---------- render
rep(" const s=findStart(Zn.objs,camTop-90);for(let i=s;i<Zn.objs.length;i++){const o=Zn.objs[i];if(o.y>camTop+VH+170)break;drawObj(o);}",
    " for(const o of Zn.big||[]){const ext=o.t==='island'?o.ry+40:o.h;if(o.y+ext>camTop&&o.y-ext<camTop+VH)drawObj(o);}\n const s=findStart(Zn.objs,camTop-90);for(let i=s;i<Zn.objs.length;i++){const o=Zn.objs[i];if(o.y>camTop+VH+170)break;if(o.t!=='island'&&o.t!=='pass')drawObj(o);}")
rep(" case 'kayak':ctx.save();ctx.translate(o.x,o.y);",
""" case 'island':{if(!o.spr||o.sprK!==K){o.spr=makeIsland(o);o.sprK=K;}ctx.drawImage(o.spr.c,o.x-o.spr.w/2,o.y-o.spr.h/2,o.spr.w,o.spr.h);}return;
 case 'pass':{const gl=o.gx-o.gw/2,gr=o.gx+o.gw/2,x0=G.zone.shore(o.y)-12,x1=WG+(VW>WG?(VW-WG)/2:0)+30,h=o.h;
  const bar=(a,b)=>{ctx.fillStyle='rgba(120,240,230,.45)';ctx.beginPath();ctx.roundRect(a-10,o.y-h/2-10,b-a+20,h+20,30);ctx.fill();ctx.fillStyle='#e6c88a';ctx.beginPath();ctx.roundRect(a,o.y-h/2,b-a,h,24);ctx.fill();ctx.fillStyle='#f3dcae';ctx.beginPath();ctx.roundRect(a+5,o.y-h/2+5,b-a-10,h-10,20);ctx.fill();
   const q=rng(Math.round(a+o.y));for(let i=0;i<5;i++){ctx.fillStyle=['#8d8577','#a39a8b','#6f685d'][i%3];ctx.beginPath();ctx.ellipse(lerp(a+14,b-14,q()),o.y+(q()-.5)*h*.6,5+q()*6,4+q()*4,q()*3,0,TAU);ctx.fill();}
   for(let i=0;i<40;i++){const x=lerp(a,b,i/39);ctx.fillStyle='rgba(255,255,255,.75)';ctx.beginPath();ctx.arc(x,o.y+h/2+2+Math.sin(i+G.t*3)*1.5,1.6,0,TAU);ctx.fill();ctx.beginPath();ctx.arc(x,o.y-h/2-2+Math.cos(i+G.t*3)*1.5,1.6,0,TAU);ctx.fill();}};
  bar(x0,gl);bar(gr,x1);for(const x of[gl,gr])ctx.drawImage(SP.buoy.c,x-9,o.y+h/2-9,18,18);
  ctx.fillStyle='rgba(8,22,48,.72)';ctx.beginPath();ctx.roundRect(o.gx-38,o.y+h/2+14,76,18,8);ctx.fill();ctx.fillStyle='#ffc93c';ctx.font='800 11px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('PASO ESTRECHO',o.gx,o.y+h/2+23.5);}return;
 case 'motor':ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.rot);ctx.fillStyle='rgba(0,20,50,.25)';ctx.beginPath();ctx.ellipse(4,6,10,26,0,0,TAU);ctx.fill();ctx.drawImage(SP.motor.c,-13,-29,26,58);ctx.restore();return;
 case 'piri':{ctx.drawImage(SP.piri.c,o.x-30,o.y-40,60,80);
  if(!o.gift){const p=1+Math.sin(t*5)*.08,rg=ctx.createRadialGradient(o.rx,o.y,4,o.rx,o.y,30);rg.addColorStop(0,'rgba(255,201,60,.4)');rg.addColorStop(1,'rgba(255,201,60,0)');ctx.fillStyle=rg;ctx.beginPath();ctx.arc(o.rx,o.y,30,0,TAU);ctx.fill();ctx.setLineDash([5,4]);ctx.lineDashOffset=-t*20;ctx.strokeStyle='#ffe28a';ctx.lineWidth=2.2;ctx.beginPath();ctx.arc(o.rx,o.y,20*p,0,TAU);ctx.stroke();ctx.setLineDash([]);ctx.fillStyle='#ff4757';ctx.font='800 15px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('♥',o.rx,o.y+1);}
  label(o.x,o.y-54,'PIRI-PIRI',o.gift?'¡GRACIAS!':'VIDA · TURBOS');}return;
 case 'float':{drawFloat(ctx,o,t);if(o.wave>0){const a=clamp(o.wave,0,1);ctx.globalAlpha=a;ctx.font='800 13px "Saira Condensed",sans-serif';const w=ctx.measureText(o.txt).width+18,bx=o.x-w/2,by=o.y-50;ctx.fillStyle='#fff';ctx.beginPath();ctx.roundRect(bx,by,w,24,12);ctx.fill();ctx.beginPath();ctx.moveTo(o.x-6,by+22);ctx.lineTo(o.x,by+32);ctx.lineTo(o.x+6,by+22);ctx.fill();ctx.fillStyle='#0d1b33';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(o.txt,o.x,by+12.5);
  for(let k=0;k<3;k++){const hy=o.y-24-((t*30+k*14)%34),hx=o.x-12+k*12;ctx.fillStyle='#ff3f8e';ctx.beginPath();ctx.moveTo(hx,hy+3);ctx.bezierCurveTo(hx-5,hy-1,hx-2,hy-5,hx,hy-2);ctx.bezierCurveTo(hx+2,hy-5,hx+5,hy-1,hx,hy+3);ctx.fill();}ctx.globalAlpha=1;}}return;
 case 'kayak':ctx.save();ctx.translate(o.x,o.y);""")
rep("ctx.fillText(fin?'META':'CONTROL',cx,o.y-16);","ctx.fillText(fin?(G.zone.Z.finish||'META'):'CONTROL',cx,o.y-16);")
rep("ctx.drawImage(SP.jet[c.id].c,-16,-34,32,68);ctx.restore();","ctx.drawImage((c.isP&&!G.demo&&SP.jetP?SP.jetP:SP.jet[c.id]).c,-16,-34,32,68);ctx.restore();")
# island maker (before drawDeco)
rep("function drawDeco(g,d){","""function makeIsland(o){const W=(o.rx+40)*2,H=(o.ry+40)*2,cove=o.theme==='cove';return sprite(W,H,g=>{const q=rng(o.seed);
 g.save();g.scale(1,(o.ry+34)/(o.rx+34));let gg=g.createRadialGradient(0,0,o.rx*.7,0,0,o.rx+34);gg.addColorStop(0,'rgba(130,245,232,.9)');gg.addColorStop(1,'rgba(130,245,232,0)');g.fillStyle=gg;g.beginPath();g.arc(0,0,o.rx+34,0,TAU);g.fill();g.restore();
 for(let i=0;i<160;i++){const a=i/160*TAU,j=q();g.fillStyle=`rgba(255,255,255,${.45+j*.5})`;g.beginPath();g.arc(Math.cos(a)*(o.rx+5+j*4),Math.sin(a)*(o.ry+5+j*4),1+q()*1.8,0,TAU);g.fill();}
 const off=[];for(let i=0;i<36;i++)off.push(1+(q()-.5)*.07);const blob=(sx,sy)=>{g.beginPath();for(let i=0;i<=36;i++){const a=i/36*TAU,j=off[i%36];g.lineTo(Math.cos(a)*o.rx*sx*j,Math.sin(a)*o.ry*sy*j);}g.closePath();};
 g.fillStyle='#dcbc7c';blob(1,1);g.fill();g.fillStyle='#f3dcae';blob(.9,.94);g.fill();for(let i=0;i<260;i++){const a=q()*TAU,rr=Math.sqrt(q())*.85;g.fillStyle=q()>.5?'rgba(180,140,80,.3)':'rgba(255,255,255,.4)';g.fillRect(Math.cos(a)*o.rx*rr,Math.sin(a)*o.ry*rr,1,1);}
 if(cove){g.save();blob(.66,.76);g.clip();g.fillStyle='#c47a44';g.fillRect(-o.rx,-o.ry,o.rx*2,o.ry*2);const cols=['#d98f57','#b9693a','#e7a46b','#a75d31'];for(let i=0;i<90;i++){g.fillStyle=cols[i%4];g.beginPath();g.ellipse((q()-.5)*o.rx*1.4,(q()-.5)*o.ry*1.6,5+q()*9,4+q()*6,q()*3,0,TAU);g.fill();}g.restore();
  for(let i=0;i<9;i++){const x=(q()-.5)*o.rx*.9,y=(q()-.5)*o.ry*1.2,R=8+q()*8;g.fillStyle='rgba(40,20,0,.25)';g.beginPath();g.arc(x+5,y+4,R,0,TAU);g.fill();const pc=['#2a5a2a','#36722f','#4b8a3c','#5f9e48'];for(let k=0;k<10;k++){const a=q()*TAU,d=q()*R*.6;g.fillStyle=pc[Math.min(3,(k/3)|0)];g.beginPath();g.arc(x+Math.cos(a)*d,y+Math.sin(a)*d,R*(.45+q()*.3)*(1-k/24),0,TAU);g.fill();}}}
 else{for(let i=0;i<5;i++){const x=(q()-.5)*o.rx*.8,y=(q()-.5)*o.ry*1.1;g.save();g.globalAlpha=.2;for(let k=0;k<8;k++)leaf(g,x+6,y+5,k/8*TAU+.2,15,'#203018');g.restore();for(let k=0;k<8;k++)leaf(g,x,y,k/8*TAU+q()*.3,13+q()*4,k%2?'#2f8f3f':'#46aa4a');}
  for(let i=0;i<3;i++){const x=(q()-.5)*o.rx*.9,y=(q()-.5)*o.ry*1.2;g.fillStyle='#fbfaf6';g.fillRect(x-7,y-7,14,14);g.strokeStyle='rgba(0,0,0,.08)';g.strokeRect(x-7,y-7,14,14);}}
 for(let i=0;i<6;i++){const a=q()*TAU;g.fillStyle=['#8d8577','#a39a8b','#6f685d'][i%3];g.beginPath();g.ellipse(Math.cos(a)*o.rx*.95,Math.sin(a)*o.ry*.95,4+q()*5,3+q()*4,q()*3,0,TAU);g.fill();}});}
function drawDeco(g,d){""")
# ---------- player sprite helper
rep("function motoName(m){return paintOf(m).name||m.name;}","function motoName(m){return paintOf(m).name||m.name;}\nfunction playerSk(){const a=AVATARS[G.avatar|0]||AVATARS[0];return Object.assign({},skOf(MOTOS[G.moto|0]),{vest:a.face.vest,arm:a.face.vest,helmet:'#ffffff',hs:a.face.vest});}\nfunction pilotName(){return G.pname||(AVATARS[G.avatar|0]||AVATARS[0]).name.toUpperCase();}")
rep("SP.jet[m.id]=sprite(32,68,g=>drawJet(g,skOf(m)));Snd.cash();goGarage();","SP.jet[m.id]=sprite(32,68,g=>drawJet(g,skOf(m)));SP.jetP=sprite(32,68,g=>drawJet(g,playerSk()));Snd.cash();goGarage();")
rep("moto:clamp(store.get('ct_moto',0)|0,0,MOTOS.length-1),","moto:clamp(store.get('ct_moto',0)|0,0,MOTOS.length-1),avatar:clamp(store.get('ct_av',0)|0,0,7),pname:String(store.get('ct_pname','')||'').slice(0,12),")
rep(" camTop=G.P.y-VH*.7;camX=-(VW-WG)/2;if(camX>0)camX=0;\n buildTrack();"," camTop=G.P.y-VH*.7;camX=-(VW-WG)/2;if(camX>0)camX=0;\n SP.jetP=sprite(32,68,g=>drawJet(g,playerSk()));\n buildTrack();")
rep("if(Z.riv){const rr=rng(Zn.seed+3);","if(Z.riv){const rr=rng(Zn.seed+3);")
rep("d.style.background=skOf(c.m).hull;c._dot=d;","d.style.background=c.isP?playerSk().hull:skOf(c.m).hull;c._dot=d;")
# ---------- flow
rep(" if(Z.obj==='race3'&&rank>3){ok=false;why='Has llegado el '+rank+'º. Tenías que quedar entre los 3 primeros.';}",
    " if(Z.obj==='race3'&&rank>3){ok=false;why='Has llegado el '+rank+'º. Tenías que quedar entre los 3 primeros.';}\n if(Z.obj==='race2'&&rank>2){ok=false;why='Has llegado el '+rank+'º. Tenías que quedar entre los 2 primeros.';}")
rep("if(retry)G.fuel=Math.max(G.fuel,70);if(G.zi===ZONES.length-1)G.fuel=100;","if(retry)G.fuel=Math.max(G.fuel,70);if(!ZONES[G.zi].bar)G.fuel=Math.max(G.fuel,G.zi===ZONES.length-1?100:85);")
rep(" tag(Z.bar==='jj'?\"Bar JJ's a mitad de zona\":Z.bar==='roxy'?'Bar Roxy a mitad de zona':'Sin bar: depósito lleno para la final');",
    " tag(Z.bar==='jj'?\"Bar JJ's a mitad de zona\":Z.bar==='roxy'?'Bar Roxy a mitad de zona':Z.boss?'Sin bar: depósito lleno para la final':'Sin bar: sales con el depósito al 85 %');if(Z.piri)tag('Piri-Piri: vida y turbos','gold');")
rep(" const P=ZONES.map((_,i)=>[30+i*50,84+Math.sin(i*1.3)*30+(i%2)*20]);"," const NZ=ZONES.length,P=ZONES.map((_,i)=>[22+i*(316/(NZ-1)),84+Math.sin(i*1.3)*30+(i%2)*20]);")
rep("g.fillText(b==='jj'?\"JJ'S\":'ROXY',x,y+21);}});","g.fillText(b==='jj'?\"JJ'S\":'ROXY',x,y+21);}if(ZONES[i].piri){g.fillStyle='#d9b25a';g.beginPath();g.arc(x+11,y-11,5,0,TAU);g.fill();g.strokeStyle='#8a5a2b';g.lineWidth=1.2;g.stroke();}});")
# garage card uses avatar
rep('<div class="gtop"><canvas id="gPilot" width="136" height="136"></canvas><div><small>PILOTO</small><b id="gPilotName"></b><p id="gBio"></p></div></div>',
    '<div class="gtop"><canvas id="gPilot" width="136" height="136"></canvas><div><small>TU PILOTO</small><b id="gPilotName"></b><p id="gBio"></p></div></div>')
rep("drawPortrait($('#gPilot'),m);$('#gPilotName').textContent=m.pilot;$('#gBio').textContent=m.bio;",
    "drawPortrait($('#gPilot'),AVATARS[G.avatar|0]||AVATARS[0]);$('#gPilotName').textContent=pilotName();$('#gBio').textContent=MOTO_DESC[m.id]||'';")
# pilot screen
rep('    <section id="scrGarage" class="screen" hidden>','''    <section id="scrPilot" class="screen" hidden>
      <div class="head"><button class="btn ghost sm" id="aBack" style="flex:none">‹ VOLVER</button><h2 class="h">TU PILOTO</h2><span style="width:70px"></span></div>
      <div class="avs" id="avGrid"></div>
      <div class="pname"><label for="aName">TU NOMBRE</label><input id="aName" maxlength="12" autocomplete="off" autocapitalize="characters" spellcheck="false" enterkeyhint="done" placeholder="Escribe tu nombre"></div>
      <div class="menu"><button class="btn p" id="aGo">SIGUIENTE: ELEGIR MOTO</button></div>
    </section>

    <section id="scrGarage" class="screen" hidden>''')
rep("/* taller */","""/* piloto */
.avs{width:min(100%,440px);display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.av{display:flex;flex-direction:column;align-items:center;gap:4px;padding:8px 4px;border-radius:14px;border:1px solid rgba(255,255,255,.14);background:rgba(255,255,255,.06);color:#fff;font-family:var(--cond);font-weight:700;font-size:14px}
.av canvas{width:min(64px,100%);height:auto;aspect-ratio:1;border-radius:50%}
.av.on{border:2px solid var(--orange);background:rgba(255,122,26,.16)}
#aName{font-family:var(--cond);font-weight:800;font-size:20px;text-transform:uppercase;padding:8px 12px;border-radius:12px;border:1px solid rgba(255,255,255,.3);background:rgba(0,0,0,.3);color:#fff;outline:none;user-select:text;-webkit-user-select:text}
#aName:focus{border-color:var(--orange)}
/* taller */""")
rep("$('#app').classList.toggle('nopads',id==='scrJJ'||id==='scrRoxy'||id==='scrPaint');","$('#app').classList.toggle('nopads',id==='scrJJ'||id==='scrRoxy'||id==='scrPaint'||id==='scrPilot');")
rep("function goGarage(){show('scrGarage');renderGarage();Music.play('menu');}","""function goGarage(){show('scrGarage');renderGarage();Music.play('menu');}
function goPilot(){show('scrPilot');renderPilot();Music.play('menu');}
function renderPilot(){const grid=$('#avGrid');grid.textContent='';AVATARS.forEach((a,i)=>{const b=document.createElement('button');b.className='av'+(i===G.avatar?' on':'');const cv=document.createElement('canvas');cv.width=136;cv.height=136;drawPortrait(cv,a);const sp=document.createElement('span');sp.textContent=a.name;b.append(cv,sp);
 b.addEventListener('click',()=>{G.avatar=i;Snd.click();grid.querySelectorAll('.av').forEach((x,j)=>x.classList.toggle('on',j===i));});grid.append(b);});$('#aName').value=G.pname||'';}""")
rep("on('#bPlay',()=>{Snd.click();goGarage();});","on('#bPlay',()=>{Snd.click();goPilot();});\non('#aBack',()=>{Snd.click();goTitle();});\non('#aGo',()=>{store.set('ct_av',G.avatar);store.set('ct_pname',G.pname);if(G.pname)store.set('ct_name',G.pname);Snd.click();goGarage();});\n$('#aName').addEventListener('input',e=>{G.pname=e.target.value.toUpperCase().replace(/[^A-Z0-9ÁÉÍÓÚÜÑ .\\-_]/g,'').trim().slice(0,12);});")
rep("on('#gBack',()=>{Snd.click();goTitle();});","on('#gBack',()=>{Snd.click();goPilot();});")
rep("on('#oAgain',()=>{Snd.click();goGarage();});","on('#oAgain',()=>{Snd.click();goPilot();});")
rep("function menuNav(d){if(!$('#scrGarage').hidden)changeMoto(d);}","function menuNav(d){if(!$('#scrGarage').hidden)changeMoto(d);}")
rep("function menuOk(){if(!$('#scrTitle').hidden){Snd.click();goGarage();}","function menuOk(){if(!$('#scrTitle').hidden){Snd.click();goPilot();}")
rep("const f=$('#nameForm');f.hidden=!qualifies(G.score);if(!f.hidden)$('#nameIn').value=store.get('ct_name','');","const f=$('#nameForm');f.hidden=!qualifies(G.score);if(!f.hidden)$('#nameIn').value=G.pname||store.get('ct_name','');")
open(p,'w',encoding='utf-8').write(s)
print('ok')
