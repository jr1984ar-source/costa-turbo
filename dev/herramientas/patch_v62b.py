H='costa-turbo.html'
h=open(H).read()
def rep(s,a,b,n=1):
    c=s.count(a)
    assert c==n,(c,a[:90])
    return s.replace(a,b)

# ---------------- datos del equipo ----------------
GEARJS=r"""
const GEAR={
 suit:[{id:'s0',n:'Sin neopreno',b:'De serie',p:0},
  {id:'s1',n:'Neopreno negro',b:'Neopreno',p:500,c:'#1d2027',a:'#4a505c'},
  {id:'s2',n:'Neopreno azul océano',b:'Neopreno',p:900,c:'#1e5eff',a:'#0b2c8f'},
  {id:'s3',n:'Neopreno rojo racing',b:'Neopreno',p:1300,c:'#e3202b',a:'#16181d'},
  {id:'s4',n:'Neopreno flúor',b:'Neopreno',p:1800,c:'#b6f01e',a:'#1d2027'},
  {id:'s5',n:'Neopreno camuflaje marino',b:'Neopreno',p:2400,c:'#2f6f8f',a:'#9ed8ea',pat:'camo'},
  {id:'s6',n:'Neopreno carbono y oro',b:'Neopreno',p:3200,c:'#2a2d33',a:'#ffc93c',pat:'carbon'}],
 vest:[{id:'v0',n:'Chaleco de serie',b:'De serie',p:0},
  {id:'v1',n:'Venture',b:'Jet Pilot',p:2500,c:'#ff7a1a',c2:'#1d2027',pat:'band'},
  {id:'v2',n:'Matrix Race',b:'Jet Pilot',p:5000,c:'#1e5eff',c2:'#ffffff',pat:'race'},
  {id:'v3',n:'RX Vault',b:'Jet Pilot',p:8500,c:'#16181d',c2:'#e3202b',pat:'vault'},
  {id:'v4',n:'Cause Neo',b:'Jet Pilot',p:12000,c:'#f4f6f9',c2:'#16a3d6',pat:'race'},
  {id:'v5',n:'F-86 Carbon',b:'Jet Pilot',p:18000,c:'#25282e',c2:'#ffc93c',pat:'carbon'}],
 helm:[{id:'h0',n:'Sin casco',b:'De serie',p:0},
  {id:'h1',n:'S-M3',b:'Alpinestars',p:3000,c:'#1d2027',c2:'#e3202b',st:'mx',pat:'twin'},
  {id:'h2',n:'S-M5 Rover',b:'Alpinestars',p:6000,c:'#f4f6f9',c2:'#1e5eff',st:'mx',pat:'split'},
  {id:'h3',n:'S-M8 Flame',b:'Alpinestars',p:9500,c:'#ffd21a',c2:'#e3202b',st:'mx',pat:'flame'},
  {id:'h4',n:'Supertech M10',b:'Alpinestars',p:14000,c:'#e3202b',c2:'#ffffff',st:'mx',pat:'star'},
  {id:'h5',n:'VX-Pro4',b:'Arai',p:8000,c:'#f4f6f9',c2:'#e3202b',st:'full',pat:'twin'},
  {id:'h6',n:'RX-7V Racing',b:'Arai',p:16000,c:'#1e5eff',c2:'#ffd21a',st:'full',pat:'flame'},
  {id:'h7',n:'Tour-X Carbono',b:'Arai',p:21000,c:'#2a2d33',c2:'#ffc93c',st:'full',pat:'carbon'},
  {id:'h8',n:'Edición Leyenda Cromo',b:'Arai',p:28000,c:'#cfd8e3',c2:'#7a5cff',st:'full',pat:'chrome'}]};
let gearStore=store.get('ct_gear',null);if(!gearStore||typeof gearStore!=='object'||!gearStore.eq||!Array.isArray(gearStore.own))gearStore={own:['s0','v0','h0'],eq:{suit:'s0',vest:'v0',helm:'h0'}};
function saveGear(){store.set('ct_gear',gearStore);}
function gearItem(cat,id){return GEAR[cat].find(x=>x.id===id)||GEAR[cat][0];}
function gearEq(tr){const e=Object.assign({},gearStore.eq,tr||{});return{suit:gearItem('suit',e.suit),vest:gearItem('vest',e.vest),helm:gearItem('helm',e.helm)};}
function gStar(g,x,y,R,r){g.beginPath();for(let k=0;k<10;k++){const a=-Math.PI/2+k*Math.PI/5,d=k%2?r:R;k?g.lineTo(x+Math.cos(a)*d,y+Math.sin(a)*d):g.moveTo(x+Math.cos(a)*d,y+Math.sin(a)*d);}g.closePath();g.fill();}
function gCarbon(g,x0,y0,w,hh,s){g.fillStyle='rgba(255,255,255,.1)';for(let x=x0;x<x0+w;x+=s)for(let y=y0;y<y0+hh;y+=s)if((Math.round((x-x0)/s)+Math.round((y-y0)/s))%2)g.fillRect(x,y,s*.55,s*.55);}
function helmSide(g,hx,hy,R,he){const c=he.c,c2=he.c2,full=he.st==='full',shell=()=>{g.beginPath();if(full)g.arc(hx-1,hy-1,R+3.5,0,TAU);else{g.arc(hx-1,hy-1,R+3,Math.PI*.8,Math.PI*1.97);g.quadraticCurveTo(hx+5,hy-5,hx-5,hy+2);g.quadraticCurveTo(hx-9,hy+8,hx-R+1,hy+11);g.closePath();}};
 shell();let gg=g.createLinearGradient(hx-R,hy-R-4,hx+R,hy+R);if(he.pat==='chrome'){gg.addColorStop(0,'#ffffff');gg.addColorStop(.42,'#8e9aa8');gg.addColorStop(.7,'#f2f6fa');gg.addColorStop(1,'#6f7a88');}else{gg.addColorStop(0,mixc(c,'#ffffff',.38));gg.addColorStop(.55,c);gg.addColorStop(1,mixc(c,'#000000',.28));}g.fillStyle=gg;g.fill();
 g.save();shell();g.clip();g.fillStyle=c2;g.strokeStyle=c2;
 if(he.pat==='twin'){g.lineWidth=2.4;for(const d of[-1.5,2.8]){g.beginPath();g.arc(hx-1,hy-1,R+d,Math.PI*.92,Math.PI*1.92);g.stroke();}}
 else if(he.pat==='split')g.fillRect(hx-R-6,hy-R-6,R+4,2*R+14);
 else if(he.pat==='flame'){for(let k=0;k<3;k++){g.beginPath();g.moveTo(hx+R+4,hy-9+k*6);g.quadraticCurveTo(hx+2,hy-13+k*6,hx-9-k*3,hy-10+k*7);g.quadraticCurveTo(hx-1,hy-7+k*6,hx-4,hy-4+k*6);g.quadraticCurveTo(hx+4,hy-5+k*6,hx+R+4,hy-3+k*6);g.fill();}}
 else if(he.pat==='star')gStar(g,hx-4,hy-5,6,2.6);
 else if(he.pat==='carbon'){gCarbon(g,hx-R-5,hy-R-5,2*R+10,2*R+10,2.6);g.fillStyle=c2;g.fillRect(hx-R-5,hy+1,2*R+10,2.4);}
 else if(he.pat==='chrome'){g.lineWidth=3;g.beginPath();g.arc(hx-1,hy-1,R+.5,Math.PI*1.02,Math.PI*1.8);g.stroke();}
 g.restore();
 if(full){g.fillStyle='#1b2433';g.beginPath();g.moveTo(hx+1,hy-8);g.lineTo(hx+R+3,hy-6);g.quadraticCurveTo(hx+R+5.5,hy-1,hx+R+2.5,hy+3);g.lineTo(hx+1,hy+2);g.closePath();g.fill();g.fillStyle='rgba(140,210,255,.4)';g.fillRect(hx+4,hy-6,R-4,2);}
 else{g.fillStyle=c;g.beginPath();g.moveTo(hx+R-5,hy-R+1);g.lineTo(hx+R+13,hy-R+5);g.lineTo(hx+R+11,hy-R+9);g.lineTo(hx+R-2,hy-R+7);g.closePath();g.fill();g.fillStyle=c2;g.fillRect(hx+R+1,hy-R+5,8,1.6);
  g.fillStyle='#1d2027';g.beginPath();g.roundRect(hx+1,hy-7.5,R+3,7.5,2.5);g.fill();g.fillStyle='rgba(255,170,60,.88)';g.beginPath();g.roundRect(hx+5,hy-6.3,R-2.5,5,2);g.fill();
  g.strokeStyle=c;g.lineWidth=6;g.lineCap='round';g.beginPath();g.moveTo(hx-3,hy+R-1);g.quadraticCurveTo(hx+R+4,hy+R+1,hx+R+7,hy+3);g.stroke();}
 g.strokeStyle='rgba(0,0,0,.25)';g.lineWidth=1;shell();g.stroke();}
function helmFront(g,he){const c=he.c,c2=he.c2,full=he.st==='full',sh=()=>{g.beginPath();g.ellipse(34,30.5,16.5,18.5,0,0,TAU);};
 sh();let gg=g.createLinearGradient(20,12,48,50);if(he.pat==='chrome'){gg.addColorStop(0,'#ffffff');gg.addColorStop(.45,'#8e9aa8');gg.addColorStop(.72,'#f2f6fa');gg.addColorStop(1,'#6f7a88');}else{gg.addColorStop(0,mixc(c,'#ffffff',.35));gg.addColorStop(.6,c);gg.addColorStop(1,mixc(c,'#000000',.28));}g.fillStyle=gg;g.fill();
 g.save();sh();g.clip();g.fillStyle=c2;
 if(he.pat==='twin'){g.fillRect(28.5,10,2.6,40);g.fillRect(36.9,10,2.6,40);}
 else if(he.pat==='split')g.fillRect(16,10,18,42);
 else if(he.pat==='flame'){for(const s of[-1,1]){g.beginPath();g.moveTo(34+s*17,50);g.quadraticCurveTo(34+s*16,34,34+s*6,20);g.quadraticCurveTo(34+s*11,32,34+s*9,34);g.quadraticCurveTo(34+s*14,28,34+s*12,18);g.quadraticCurveTo(34+s*20,32,34+s*17,50);g.fill();}}
 else if(he.pat==='star')gStar(g,34,18,6,2.6);
 else if(he.pat==='carbon'){gCarbon(g,16,10,36,42,2.4);g.fillStyle=c2;g.fillRect(16,38,36,2.4);}
 else if(he.pat==='chrome'){g.fillStyle='rgba(255,255,255,.7)';g.fillRect(22,14,3,22);g.fillStyle=c2;g.fillRect(32.5,10,3,40);}
 g.restore();
 if(full){g.fillStyle='#1b2433';g.beginPath();g.roundRect(22,24,24,11,5);g.fill();g.fillStyle='rgba(140,210,255,.45)';g.fillRect(24.5,26,9,2);}
 else{g.fillStyle='#1d2027';g.beginPath();g.roundRect(21,23.5,26,10,4);g.fill();g.fillStyle='rgba(255,170,60,.9)';g.beginPath();g.roundRect(23.5,25,21,7,3);g.fill();
  g.fillStyle=c;g.beginPath();g.moveTo(17,18);g.lineTo(51,18);g.lineTo(47,11);g.lineTo(21,11);g.closePath();g.fill();g.fillStyle=c2;g.fillRect(24,14,20,1.8);
  g.fillStyle=mixc(c,'#000000',.2);g.beginPath();g.moveTo(27,38);g.lineTo(41,38);g.lineTo(38,48);g.lineTo(30,48);g.closePath();g.fill();g.fillStyle='rgba(0,0,0,.35)';for(let k=0;k<3;k++)g.fillRect(31+k*2.4,41,1.2,5);}
 g.strokeStyle='rgba(0,0,0,.25)';g.lineWidth=.8;sh();g.stroke();}
function vestDeco(g,ve,kind){if(!ve||!ve.c2)return;g.fillStyle=ve.c2;g.strokeStyle=ve.c2;
 if(kind==='front'){if(ve.pat==='band')g.fillRect(6,60,56,5);else if(ve.pat==='race'){g.fillRect(18,52,4,20);g.fillRect(46,52,4,20);}else if(ve.pat==='vault'){g.beginPath();g.moveTo(10,56);g.lineTo(34,66);g.lineTo(58,56);g.lineTo(58,61);g.lineTo(34,71);g.lineTo(10,61);g.closePath();g.fill();}else if(ve.pat==='carbon'){gCarbon(g,6,50,56,22,2.4);g.lineWidth=2;g.beginPath();g.ellipse(34,72,26,20,0,0,TAU);g.stroke();}
  g.fillStyle=ve.pat==='race'&&ve.c.toLowerCase()>'#e'?'#16181d':'#ffffff';g.font='800 4.6px "Saira Condensed",sans-serif';g.textAlign='center';g.fillText('JET PILOT',34,58.5);}}
function gearIcon(g,cat,it){g.save();g.lineJoin='round';g.lineCap='round';const av=(AVATARS[G.avatar|0]||AVATARS[0]).face;
 if(cat==='helm'){if(it.id==='h0'){g.fillStyle=av.skin;g.beginPath();g.arc(22,23,11,0,TAU);g.fill();g.fillStyle=av.hair;g.beginPath();g.arc(21,21,12,Math.PI*.9,Math.PI*1.9);g.closePath();g.fill();}else helmSide(g,20,25,11,it);}
 else if(cat==='vest'){const c=it.c||av.vest;g.fillStyle=c;g.beginPath();g.moveTo(10,10);g.lineTo(17,8);g.quadraticCurveTo(22,14,27,8);g.lineTo(34,10);g.lineTo(35,37);g.quadraticCurveTo(22,40,9,37);g.closePath();g.fill();
  if(it.c2){g.save();g.clip();g.fillStyle=it.c2;if(it.pat==='band')g.fillRect(8,26,28,4);else if(it.pat==='race'){g.fillRect(12,10,3,30);g.fillRect(29,10,3,30);}else if(it.pat==='vault'){g.beginPath();g.moveTo(8,20);g.lineTo(22,27);g.lineTo(36,20);g.lineTo(36,24);g.lineTo(22,31);g.lineTo(8,24);g.closePath();g.fill();}else if(it.pat==='carbon'){gCarbon(g,8,8,28,32,2.2);}g.restore();}
  g.strokeStyle='rgba(0,0,0,.35)';g.lineWidth=1;g.stroke();g.strokeStyle='#c8ccd4';g.lineWidth=1.4;g.beginPath();g.moveTo(22,15);g.lineTo(22,37);g.stroke();}
 else{const c=it.c||av.skin;g.strokeStyle=c;g.lineWidth=5.5;g.beginPath();g.moveTo(14,12);g.lineTo(8,26);g.moveTo(30,12);g.lineTo(36,26);g.moveTo(18,30);g.lineTo(16,41);g.moveTo(26,30);g.lineTo(28,41);g.stroke();g.fillStyle=c;g.beginPath();g.roundRect(13,9,18,23,5);g.fill();
  if(!it.c){g.fillStyle='#1b2a4a';g.fillRect(13,25,18,8);}else{g.strokeStyle=it.a;g.lineWidth=5.5;g.beginPath();g.moveTo(8.6,24.5);g.lineTo(8,26);g.moveTo(35.4,24.5);g.lineTo(36,26);g.stroke();g.fillStyle=it.a;g.fillRect(13,18,18,3);if(it.pat==='camo'){g.fillStyle='rgba(20,40,60,.45)';for(const[x,y,r]of[[17,13,3],[26,16,2.5],[20,26,3],[28,27,2]]){g.beginPath();g.arc(x,y,r,0,TAU);g.fill();}}if(it.pat==='carbon')gCarbon(g,13,9,18,23,2);}}
 g.restore();}
"""
a="const LOCK_SVG="
i=h.index(a);j=h.index("\n",i)
h=h[:j+1]+GEARJS.lstrip("\n")+h[j+1:]

# ---------------- piloto con su equipo (vista de arriba) ----------------
h=rep(h,"function playerSk(){const a=AVATARS[G.avatar|0]||AVATARS[0];return Object.assign({},skOf(MOTOS[G.moto|0]),{vest:a.face.vest,arm:a.face.vest,helmet:'#ffffff',hs:a.face.vest});}",
        "function playerSk(tr){const a=AVATARS[G.avatar|0]||AVATARS[0],q=gearEq(tr),s=Object.assign({},skOf(MOTOS[G.moto|0]),{vest:a.face.vest,arm:a.face.vest,helmet:'#ffffff',hs:a.face.vest});if(q.vest.c){s.vest=q.vest.c;s.v2=q.vest.c2;s.vpat=q.vest.pat;s.arm=q.vest.c;s.hs=q.vest.c;}if(q.suit.c){s.arm=q.suit.c;s.arm2=q.suit.a;}if(q.helm.c){s.helmet=q.helm.c;s.hs=q.helm.c2;s.hpat=q.helm.pat;s.hst=q.helm.st;}return s;}")
h=rep(h," g.fillStyle=s.vest;g.beginPath();g.ellipse(0,5.5,7.6,5.2,0,0,TAU);g.fill();g.fillStyle='rgba(255,255,255,.18)';g.beginPath();g.ellipse(-2,4,4,2.4,0,0,TAU);g.fill();\n",
        " g.fillStyle=s.vest;g.beginPath();g.ellipse(0,5.5,7.6,5.2,0,0,TAU);g.fill();\n if(s.v2){g.save();g.beginPath();g.ellipse(0,5.5,7.6,5.2,0,0,TAU);g.clip();g.fillStyle=s.v2;if(s.vpat==='band')g.fillRect(-8,6.2,16,2.4);else if(s.vpat==='race'){g.fillRect(-6.2,0,1.9,11);g.fillRect(4.3,0,1.9,11);}else if(s.vpat==='vault'){g.beginPath();g.moveTo(-8,3.6);g.lineTo(0,7.6);g.lineTo(8,3.6);g.lineTo(8,6.2);g.lineTo(0,10.2);g.lineTo(-8,6.2);g.closePath();g.fill();}else if(s.vpat==='carbon'){gCarbon(g,-8,0,16,11,1.4);g.strokeStyle=s.v2;g.lineWidth=1.1;g.beginPath();g.ellipse(0,5.5,7,4.6,0,0,TAU);g.stroke();}g.restore();}\n g.fillStyle='rgba(255,255,255,.18)';g.beginPath();g.ellipse(-2,4,4,2.4,0,0,TAU);g.fill();\n")
h=rep(h," g.strokeStyle=s.arm;g.lineWidth=3;g.beginPath();g.moveTo(-6,3.5);g.quadraticCurveTo(-9.2,-1,-9.8,-5.6);g.moveTo(6,3.5);g.quadraticCurveTo(9.2,-1,9.8,-5.6);g.stroke();\n",
        " g.strokeStyle=s.arm;g.lineWidth=3;g.beginPath();g.moveTo(-6,3.5);g.quadraticCurveTo(-9.2,-1,-9.8,-5.6);g.moveTo(6,3.5);g.quadraticCurveTo(9.2,-1,9.8,-5.6);g.stroke();\n if(s.arm2){g.strokeStyle=s.arm2;g.beginPath();g.moveTo(-9.6,-3.4);g.lineTo(-9.85,-5.3);g.moveTo(9.6,-3.4);g.lineTo(9.85,-5.3);g.stroke();}\n if(s.hst==='mx'){g.fillStyle=s.helmet;g.beginPath();g.moveTo(-3.6,-2.6);g.lineTo(3.6,-2.6);g.lineTo(2.8,-7.4);g.lineTo(-2.8,-7.4);g.closePath();g.fill();g.fillStyle=s.hs;g.fillRect(-.7,-7.2,1.4,4.4);}\n")
h=rep(h,"g.fillStyle='#14161c';g.fillRect(-6,-4.6,12,3.1);g.fillStyle=s.hs;g.fillRect(-.9,-1.4,1.8,8);g.restore();",
        "g.fillStyle='#14161c';g.fillRect(-6,-4.6,12,3.1);g.fillStyle=s.hs;{const hp=s.hpat||'stripe';if(hp==='twin'){g.fillRect(-2.5,-1.4,1.4,8);g.fillRect(1.1,-1.4,1.4,8);}else if(hp==='split')g.fillRect(0,-1.6,6,8.4);else if(hp==='flame'){g.beginPath();g.moveTo(-4.4,6.2);g.quadraticCurveTo(-3.4,1,-1.8,-1.5);g.quadraticCurveTo(-.7,2,0,0);g.quadraticCurveTo(.7,2,1.8,-1.5);g.quadraticCurveTo(3.4,1,4.4,6.2);g.closePath();g.fill();}else if(hp==='star')gStar(g,0,2.2,2.8,1.2);else if(hp==='carbon'){gCarbon(g,-6,-1.4,12,8,1.2);g.fillStyle=s.hs;g.fillRect(-.6,-1.4,1.2,8);}else if(hp==='chrome'){g.fillStyle='rgba(255,255,255,.7)';g.fillRect(-3.4,-1.4,1.2,7);g.fillStyle=s.hs;g.fillRect(.9,-1.4,1.5,8);}else g.fillRect(-.9,-1.4,1.8,8);}g.restore();")

# ---------------- piloto de lado (portadas, taller) ----------------
i0=h.index("function drawRiderProfile(g,f,vest){");i1=h.index("function cvSpray(")
RP=r"""function drawRiderProfile(g,f,vest,gr){const sk=f.skin,hr=f.hair,stl=f.style,dk=mixc(sk,'#000000',.18),su=gr&&gr.suit&&gr.suit.c?gr.suit:null,ve=gr&&gr.vest&&gr.vest.c?gr.vest:null,he=gr&&gr.helm&&gr.helm.c?gr.helm:null;g.save();g.lineCap='round';g.lineJoin='round';
 g.strokeStyle=su?mixc(su.c,'#000000',.22):'#121c33';g.lineWidth=15;g.beginPath();g.moveTo(132,30);g.lineTo(176,16);g.stroke();
 g.strokeStyle=su?mixc(su.c,'#000000',.22):dk;g.lineWidth=10;g.beginPath();g.moveTo(178,18);g.lineTo(171,55);g.stroke();
 g.fillStyle=vest;g.beginPath();g.moveTo(121,35);g.bezierCurveTo(118,8,136,-22,160,-33);g.lineTo(180,-26);g.bezierCurveTo(178,-4,168,20,152,37);g.closePath();g.fill();
 if(ve&&ve.pat==='carbon'){g.save();g.clip();gCarbon(g,115,-36,70,76,3);g.restore();}
 g.fillStyle='rgba(0,0,0,.2)';g.beginPath();g.moveTo(121,35);g.bezierCurveTo(119,14,128,-6,142,-19);g.lineTo(147,-15);g.bezierCurveTo(136,0,130,18,133,36);g.closePath();g.fill();
 if(ve){g.strokeStyle=ve.c2;g.fillStyle=ve.c2;if(ve.pat==='band'){g.lineWidth=6;g.beginPath();g.moveTo(124,14);g.lineTo(166,6);g.stroke();}else if(ve.pat==='vault'){g.lineWidth=3.4;g.beginPath();g.moveTo(125,0);g.lineTo(146,10);g.lineTo(168,-6);g.moveTo(124,12);g.lineTo(145,22);g.lineTo(163,8);g.stroke();}else if(ve.pat==='carbon'){g.lineWidth=2.6;g.beginPath();g.moveTo(121,35);g.bezierCurveTo(118,8,136,-22,160,-33);g.lineTo(180,-26);g.stroke();}else{g.lineWidth=3.4;g.beginPath();g.moveTo(127,5);g.lineTo(167,-3);g.moveTo(126,18);g.lineTo(161,12);g.stroke();}
  g.save();g.translate(147,24);g.rotate(-.2);g.fillStyle=ve.c.toLowerCase()>'#e'?'#16181d':'#ffffff';g.font='800 8px "Saira Condensed",sans-serif';g.textAlign='center';g.fillText('JET PILOT',0,0);g.restore();}
 else{g.strokeStyle='rgba(255,255,255,.6)';g.lineWidth=2.2;g.beginPath();g.moveTo(127,5);g.lineTo(167,-3);g.moveTo(126,18);g.lineTo(161,12);g.stroke();}
 g.strokeStyle=su?su.c:'#1b2a4a';g.lineWidth=16;g.beginPath();g.moveTo(140,30);g.lineTo(187,20);g.stroke();
 if(su&&su.pat==='camo'){g.fillStyle='rgba(15,35,55,.4)';for(const[x,y]of[[150,25],[165,21],[178,19],[186,34],[184,48]]){g.beginPath();g.arc(x,y,3.4,0,TAU);g.fill();}}
 g.strokeStyle=su?su.c:sk;g.lineWidth=10;g.beginPath();g.moveTo(189,22);g.lineTo(183,57);g.stroke();
 if(su){g.strokeStyle=su.a;g.lineWidth=10;g.beginPath();g.moveTo(184,51);g.lineTo(183,57);g.stroke();}
 g.strokeStyle=su?su.c:sk;g.lineWidth=8.5;g.beginPath();g.moveTo(167,-22);g.lineTo(190,-6);g.lineTo(207,4);g.stroke();
 if(su){g.strokeStyle=su.a;g.beginPath();g.moveTo(200,-.3);g.lineTo(205.5,3);g.stroke();}
 g.strokeStyle=vest;g.lineWidth=11;g.beginPath();g.moveTo(165,-25);g.lineTo(175,-18);g.stroke();
 g.fillStyle=sk;g.beginPath();g.arc(208,5,5.5,0,TAU);g.fill();
 g.strokeStyle=su?su.c:sk;g.lineWidth=9;g.beginPath();g.moveTo(170,-30);g.lineTo(175,-40);g.stroke();
 const hx=179,hy=-52,R=13;g.fillStyle=hr;
 if(stl==='long'){g.beginPath();g.moveTo(hx-2,hy-R);g.bezierCurveTo(hx-26,hy-10,hx-40,hy+10,hx-34,hy+24);g.bezierCurveTo(hx-24,hy+18,hx-12,hy+14,hx-4,hy+8);g.closePath();g.fill();}
 if(stl==='pony'){g.save();g.translate(hx-14,hy-6);g.rotate(-.25);g.beginPath();g.ellipse(-10,0,14,5,0,0,TAU);g.fill();g.restore();}
 g.fillStyle=sk;g.beginPath();g.arc(hx,hy,R,0,TAU);g.fill();
 g.beginPath();g.moveTo(hx+R-2,hy-3);g.lineTo(hx+R+4,hy+3);g.lineTo(hx+R-2,hy+5);g.fill();
 g.fillStyle=hr;
 if(stl==='buzz'){g.globalAlpha=.85;g.beginPath();g.arc(hx,hy,R+.5,Math.PI*.95,Math.PI*1.85);g.closePath();g.fill();g.globalAlpha=1;}
 else{g.beginPath();g.arc(hx-1,hy-1,R+1.5,Math.PI*.9,Math.PI*1.9);g.closePath();g.fill();g.beginPath();g.arc(hx-3,hy+1,R-1,Math.PI*.5,Math.PI*1.5);g.fill();
  if(stl==='bob'){g.beginPath();g.arc(hx-1,hy+1,R+1.5,Math.PI*.5,Math.PI*1.2);g.lineTo(hx,hy);g.fill();}
  if(stl==='curly')for(let i=0;i<6;i++){const a=Math.PI*(1+i*.16);g.beginPath();g.arc(hx+Math.cos(a)*(R+1),hy+Math.sin(a)*(R+1),4.2,0,TAU);g.fill();}}
 if(f.glasses){g.fillStyle='#14161b';g.beginPath();g.roundRect(hx+2,hy-6,12,6,2);g.fill();g.fillRect(hx-7,hy-4,10,2);}
 else{g.fillStyle='#1b1b1b';g.beginPath();g.arc(hx+8,hy-2,1.9,0,TAU);g.fill();}
 g.strokeStyle='rgba(90,30,20,.75)';g.lineWidth=1.6;g.beginPath();g.arc(hx+6,hy+5,3.5,.15,1.25);g.stroke();
 if(f.beard){g.fillStyle=hr;g.beginPath();g.arc(hx+2,hy+4,R*.78,.05*Math.PI,.9*Math.PI);g.closePath();g.fill();}
 if(he)helmSide(g,hx,hy,R,he);
 g.restore();}
"""
h=h[:i0]+RP+h[i1:]
h=rep(h,"function cvJet(g,q,side,face,vest,x,y,sc,rot,air){g.save();","function cvJet(g,q,side,face,vest,x,y,sc,rot,air,gr){g.save();")
h=rep(h,"drawJetProfile(g,side);if(face)drawRiderProfile(g,face,vest);g.restore();}","drawJetProfile(g,side);if(face)drawRiderProfile(g,face,vest,gr);g.restore();}")
h=rep(h,"const hero=(x,y,sc,rot,air)=>cvJet(g,q,sideOf(me),av,av.vest,x,y,sc,rot,air);","const pg=gearEq(),hero=(x,y,sc,rot,air)=>cvJet(g,q,sideOf(me),av,pg.vest.c||av.vest,x,y,sc,rot,air,pg);")

# ---------------- foto del piloto ----------------
h=rep(h,"function drawPortrait(cvs,m){const g=cvs.getContext('2d'),f=m.face,W=cvs.width;",
        "function drawPortrait(cvs,m,gr){const g=cvs.getContext('2d'),f=m.face,W=cvs.width,ve=gr&&gr.vest&&gr.vest.c?gr.vest:null,su=gr&&gr.suit&&gr.suit.c?gr.suit:null,he=gr&&gr.helm&&gr.helm.c?gr.helm:null;")
h=rep(h," g.fillStyle=f.vest;g.beginPath();g.ellipse(34,72,28,22,0,0,TAU);g.fill();g.fillStyle='rgba(255,255,255,.2)';g.fillRect(31,52,6,20);\n g.fillStyle=f.skin;g.fillRect(29,42,10,10);\n",
        " g.fillStyle=ve?ve.c:f.vest;g.beginPath();g.ellipse(34,72,28,22,0,0,TAU);g.fill();if(ve){g.save();g.beginPath();g.ellipse(34,72,28,22,0,0,TAU);g.clip();vestDeco(g,ve,'front');g.restore();}else{g.fillStyle='rgba(255,255,255,.2)';g.fillRect(31,52,6,20);}\n g.fillStyle=f.skin;g.fillRect(29,42,10,10);if(su){g.fillStyle=su.c;g.fillRect(28,46,12,7);g.fillStyle=su.a;g.fillRect(28,46,12,1.6);}\n")
h=rep(h," g.strokeStyle='#7a3a2a';g.lineWidth=1.4;g.lineCap='round';g.beginPath();g.arc(34,36,4,.25,Math.PI-.25);g.stroke();\n g.restore();}",
        " g.strokeStyle='#7a3a2a';g.lineWidth=1.4;g.lineCap='round';g.beginPath();g.arc(34,36,4,.25,Math.PI-.25);g.stroke();\n if(he)helmFront(g,he);\n g.restore();}")
h=rep(h,"drawPortrait($('#uAv'),AVATARS[G.avatar|0]||AVATARS[0]);","drawPortrait($('#uAv'),AVATARS[G.avatar|0]||AVATARS[0],gearEq());")
h=rep(h,"drawPortrait($('#gPilot'),AVATARS[G.avatar|0]||AVATARS[0]);","drawPortrait($('#gPilot'),AVATARS[G.avatar|0]||AVATARS[0],gearEq());")

# ---------------- pantalla EQUIPO DEL PILOTO ----------------
HOME='<button class="btn ghost sm hm" data-home style="flex:none"><svg class="hm-i" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8 8 2.5 14 8M4 7v6.5h3V10h2v3.5h3V7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>INICIO</button>'
h=rep(h,'<div class="row" style="width:min(100%,440px);flex-wrap:nowrap"><button class="btn" id="sPaint" style="flex:1">PINTAR</button><button class="btn p" id="sMain" style="flex:1.5"></button></div>\n    </section>',
'''<div class="row" style="width:min(100%,440px);flex-wrap:nowrap"><button class="btn" id="sPaint" style="flex:1">PINTAR</button><button class="btn p" id="sMain" style="flex:1.5"></button></div>
      <button class="btn" id="sGear" style="width:min(100%,440px)">EQUIPO DEL PILOTO</button>
    </section>

    <section id="scrGear" class="screen" hidden>
      <div class="head"><button class="btn ghost sm" id="eBack" style="flex:none">‹ ATRÁS</button><h2 class="h">EQUIPO DEL PILOTO</h2>'''+HOME+'''</div>
      <div class="cash"><i class="coin"></i><span class="cashv">0</span>&nbsp;PTA</div>
      <div class="gmoto gearpv"><canvas id="eCv" width="580" height="300"></canvas><canvas id="eTop" width="96" height="164"></canvas></div>
      <div class="etabs" id="eTabs"><button class="btn ghost sm" data-c="helm">CASCO</button><button class="btn ghost sm" data-c="vest">CHALECO</button><button class="btn ghost sm" data-c="suit">NEOPRENO</button></div>
      <div class="slist" id="eList"></div>
    </section>''')
h=rep(h,".slist{width:min(100%,440px);display:grid;gap:6px;text-align:left}",
""".slist{width:min(100%,440px);display:grid;gap:6px;text-align:left}
.gearpv{height:172px;position:relative;width:min(100%,440px);flex:none}
.gearpv #eCv{width:min(100%,300px);aspect-ratio:580/300;height:auto;animation:none}
.gearpv #eTop{position:absolute;right:8px;top:8px;width:48px;height:82px;aspect-ratio:auto;animation:none;background:rgba(8,40,80,.28);border-radius:10px}
.etabs{flex:none;width:min(100%,440px);display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
.etabs .btn{width:100%}.etabs .btn.on{background:var(--orange);color:#fff;border-color:transparent}
.ghd{font-family:var(--cond);font-weight:800;font-size:12px;letter-spacing:.14em;color:var(--dim);margin:6px 2px 0}
.prt.gr{cursor:pointer}.prt.try{border-color:rgba(51,214,255,.65);background:rgba(51,214,255,.09)}.prt.eq{border-color:rgba(255,201,60,.5)}""")
GEARUI=r"""
let gearCat='helm',gearTry=null;
function goGear(){show('scrGear');gearTry=null;renderGear();}
function gearPreview(){const tr=gearTry?{[gearTry.cat]:gearTry.id}:null,q=gearEq(tr),m=MOTOS[G.moto|0],av=(AVATARS[G.avatar|0]||AVATARS[0]).face;
 const c=$('#eCv'),g=c.getContext('2d');g.setTransform(2,0,0,2,0,0);g.clearRect(0,0,290,150);g.save();g.translate(22,54);g.scale(.68,.68);drawJetProfile(g,sideOf(m));drawRiderProfile(g,av,q.vest.c||av.vest,q);g.restore();
 const t=$('#eTop'),k=t.getContext('2d');k.setTransform(1,0,0,1,0,0);k.clearRect(0,0,t.width,t.height);k.setTransform(2.2,0,0,2.2,t.width/2,t.height/2+2);drawJet(k,playerSk(tr));}
function gearDesc(cat,it){if(cat==='helm')return it.id==='h0'?'Sin casco':(it.st==='full'?'Casco integral':'Casco de cross con visera');if(cat==='vest')return it.id==='v0'?'El chaleco de tu piloto':'Chaleco salvavidas de competición';return it.id==='s0'?'Bañador y licra':'Neopreno 3/2 mm';}
function renderGear(){cashUI();gearPreview();
 document.querySelectorAll('#eTabs .btn').forEach(b=>b.classList.toggle('on',b.dataset.c===gearCat));
 const L=$('#eList');L.textContent='';const eq=gearStore.eq[gearCat];let lastB='';
 for(const it of GEAR[gearCat]){if(it.b!==lastB){lastB=it.b;const hd=document.createElement('div');hd.className='ghd';hd.textContent=it.b.toUpperCase();L.append(hd);}
  const own=gearStore.own.includes(it.id),on=eq===it.id,tryOn=!!(gearTry&&gearTry.id===it.id);
  const row=document.createElement('div');row.className='prt gr'+(tryOn?' try':'')+(on?' eq':'');row.append(iconCanvas(g=>gearIcon(g,gearCat,it)));
  const inf=document.createElement('div');inf.innerHTML='<div class="nm"></div><div class="ef"></div>';inf.querySelector('.nm').textContent=(it.b==='De serie'||it.b==='Neopreno'?'':it.b+' ')+it.n;inf.querySelector('.ef').textContent=gearDesc(gearCat,it)+(tryOn&&!own?' · probándolo':'');row.append(inf);
  const b=document.createElement('button');b.className='btn'+(on?' max':own?'':' p');
  if(on){b.textContent='EN USO';b.disabled=true;}else if(own){b.textContent='USAR';}else{b.innerHTML='<i class="coin"></i>'+pts(it.p);b.disabled=G.money<it.p;}
  b.addEventListener('click',e=>{e.stopPropagation();if(on)return;if(!own){if(G.money<it.p)return;G.money-=it.p;gearStore.own.push(it.id);saveWallet();Snd.cash();}else Snd.click();gearStore.eq[gearCat]=it.id;saveGear();gearTry=null;SP.jetP=sprite(32,68,g=>drawJet(g,playerSk()));renderGear();});
  row.addEventListener('click',()=>{gearTry=on?null:{cat:gearCat,id:it.id};Snd.click();renderGear();});row.append(b);L.append(row);}}
on('#sGear',()=>{Snd.click();goGear();});on('#eBack',()=>{Snd.click();show('scrShop');renderShop();});
$('#eTabs').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;gearCat=b.dataset.c;gearTry=null;Snd.click();renderGear();});
"""
h=rep(h,"on('#sPaint',()=>{if(!owns(MOTOS[shopI]))return;Snd.click();goPaint();});\n","on('#sPaint',()=>{if(!owns(MOTOS[shopI]))return;Snd.click();goPaint();});\n"+GEARUI.lstrip("\n"))
open(H,'w').write(h)
print('ok')
