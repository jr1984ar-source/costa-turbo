/* ================= PORTADAS ================= */
const rgbaH=(h,a)=>{const n=parseInt(h.slice(1),16);return`rgba(${n>>16},${n>>8&255},${n&255},${a})`;};
const fontsOK=(document.fonts&&document.fonts.load)?Promise.all([document.fonts.load('800 40px "Saira Condensed"'),document.fonts.load('700 14px "Saira Condensed"')]).catch(()=>{}):Promise.resolve();
const SHARK_SIDE={deck:'#a9bccf',hood:'#8094aa',hull:'#4a5d72',trim:'#1b2028',seatA:'#1b2028',seatB:'#2a3240',seatC:'#e9eef4',stripe:'#e9eef4'};
const COVER=[
 {tag:'CONTRARRELOJ',sky:['#3f9be8','#d4f0ff'],sea:['#9ae0f2','#0b5aa8'],sun:[60,30,'#fffbe8'],land:'port'},
 {tag:'SLALOM DE BOYAS',sky:['#1f86e0','#c4ebff'],sea:['#6ae6e6','#0a62b4'],sun:[200,18,'#ffffff'],land:'cala'},
 {tag:'CARRERA · TOP 3',sky:['#2a8de6','#cdeeff'],sea:['#78dcee','#0a5cae'],sun:[150,22,'#ffffff'],land:'mago'},
 {tag:'CARRERA · TOP 3',sky:['#3f7fd6','#ffdcae'],sea:['#86cfe6','#0b4f98'],sun:[330,40,'#fff2cc'],land:'beach'},
 {tag:'HUYE DE LA POLICÍA',sky:['#3a74c8','#ffd2a0'],sea:['#72c2e2','#0a4790'],sun:[340,46,'#fff0c8'],land:'chase'},
 {tag:'6 SALTOS EN LAS OLAS',sky:['#2e2a6e','#ff7650'],sea:['#3f7cba','#0f2c66'],sun:[110,84,'#ffd27a'],land:'wave'},
 {tag:'CARRERA · TOP 2',sky:['#1ea6f5','#e8faff'],sea:['#a2f4ec','#0896d6'],sun:[70,22,'#ffffff'],land:'trenc'},
 {tag:'CARRERA · TOP 3',sky:['#4579c9','#ffd9a8'],sea:['#64b6da','#0a4a8e'],sun:[110,52,'#fff0c8'],land:'tram'},
 {tag:'CONTRARRELOJ DE NOCHE',sky:['#04081a','#1c2a50'],sea:['#1d3d68','#040d22'],moon:[310,28],land:'storm'},
 {tag:'GANA A EL TIBURÓN',sky:['#2b2f7a','#ffb35a'],sea:['#4a86c0','#0d3270'],sun:[200,88,'#ffd27a'],land:'final'}
];
function drawRiderProfile(g,f,vest){const sk=f.skin,hr=f.hair,stl=f.style,dk=mixc(sk,'#000000',.18);g.save();g.lineCap='round';g.lineJoin='round';
 g.strokeStyle='#121c33';g.lineWidth=15;g.beginPath();g.moveTo(132,30);g.lineTo(176,16);g.stroke();
 g.strokeStyle=dk;g.lineWidth=10;g.beginPath();g.moveTo(178,18);g.lineTo(171,55);g.stroke();
 g.fillStyle=vest;g.beginPath();g.moveTo(121,35);g.bezierCurveTo(118,8,136,-22,160,-33);g.lineTo(180,-26);g.bezierCurveTo(178,-4,168,20,152,37);g.closePath();g.fill();
 g.fillStyle='rgba(0,0,0,.2)';g.beginPath();g.moveTo(121,35);g.bezierCurveTo(119,14,128,-6,142,-19);g.lineTo(147,-15);g.bezierCurveTo(136,0,130,18,133,36);g.closePath();g.fill();
 g.strokeStyle='rgba(255,255,255,.6)';g.lineWidth=2.2;g.beginPath();g.moveTo(127,5);g.lineTo(167,-3);g.moveTo(126,18);g.lineTo(161,12);g.stroke();
 g.strokeStyle='#1b2a4a';g.lineWidth=16;g.beginPath();g.moveTo(140,30);g.lineTo(187,20);g.stroke();
 g.strokeStyle=sk;g.lineWidth=10;g.beginPath();g.moveTo(189,22);g.lineTo(183,57);g.stroke();
 g.strokeStyle=sk;g.lineWidth=8.5;g.beginPath();g.moveTo(167,-22);g.lineTo(190,-6);g.lineTo(207,4);g.stroke();
 g.strokeStyle=vest;g.lineWidth=11;g.beginPath();g.moveTo(165,-25);g.lineTo(175,-18);g.stroke();
 g.fillStyle=sk;g.beginPath();g.arc(208,5,5.5,0,TAU);g.fill();
 g.strokeStyle=sk;g.lineWidth=9;g.beginPath();g.moveTo(170,-30);g.lineTo(175,-40);g.stroke();
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
 g.restore();}
function cvSpray(g,q,x,y,ang,spread,len,n,sz,col){for(let i=0;i<n;i++){const t=Math.pow(q(),.7),a=ang+(q()-.5)*spread,d=t*len;g.fillStyle=col||`rgba(255,255,255,${.35+q()*.6})`;g.beginPath();g.arc(x+Math.cos(a)*d,y+Math.sin(a)*d,sz*(.4+q()*(1-t*.5)),0,TAU);g.fill();}}
function cvJet(g,q,side,face,vest,x,y,sc,rot,air){g.save();
 if(air){g.fillStyle='rgba(0,20,50,.28)';g.beginPath();g.ellipse(x-8,y+air,58*sc/.44,6*sc/.44,0,0,TAU);g.fill();}
 g.translate(x,y);g.rotate(rot);g.scale(sc,sc);g.translate(-175,-70);
 cvSpray(g,q,12,102,Math.PI*1.04,.9,170,air?60:90,9);cvSpray(g,q,40,112,Math.PI*1.25,.7,90,40,7);
 drawJetProfile(g,side);if(face)drawRiderProfile(g,face,vest);g.restore();}
function cvRival(g,q,m,x,y,sc,rot){cvJet(g,q,m===SHARK?SHARK_SIDE:m.side,m===SHARK?{skin:'#cfd6de',hair:'#2a3240',style:'buzz',glasses:1}:m.face,m===SHARK?'#1b2028':(m.face.vest||m.ui),x,y,sc,rot,0);
 if(m===SHARK){g.save();g.translate(x,y);g.rotate(rot);g.scale(sc,sc);g.translate(-175,-70);g.fillStyle='#34475c';g.beginPath();g.moveTo(30,74);g.quadraticCurveTo(40,20,92,-18);g.quadraticCurveTo(78,30,96,72);g.closePath();g.fill();g.fillStyle='rgba(255,255,255,.28)';g.beginPath();g.moveTo(42,70);g.quadraticCurveTo(50,28,86,-10);g.lineTo(72,40);g.closePath();g.fill();g.restore();}}
function cvRidge(g,q,x0,x1,base,amp,rough,col){g.beginPath();g.moveTo(x0,base+40);let y=base;for(let x=x0;x<=x1;x+=4){const e=Math.sin((x-x0)/(x1-x0)*Math.PI);y=base-amp*e*(.55+.45*Math.sin(x*.045+q()*.3))-(q()-.5)*rough;g.lineTo(x,y);}g.lineTo(x1,base+40);g.closePath();g.fillStyle=col;g.fill();}
function cvMount(g,q,x0,x1,base,top,col,col2){const pts=[];let x=x0;while(x<=x1){const t=(x-x0)/(x1-x0);pts.push([x,base-(base-top)*Math.pow(Math.sin(Math.min(1,t*1.15)*Math.PI*.5),.8)*(.7+q()*.3)]);x+=6+q()*10;}
 g.beginPath();g.moveTo(x0,base+2);pts.forEach(([a,b])=>g.lineTo(a,b));g.lineTo(x1+2,top);g.lineTo(x1+2,base+2);g.closePath();g.fillStyle=col;g.fill();
 g.strokeStyle=col2;g.lineWidth=1.2;for(let i=1;i<pts.length-1;i+=1){const[a,b]=pts[i];if(q()<.6){g.beginPath();g.moveTo(a,b+2);g.lineTo(a-6-q()*10,base+1);g.stroke();}}}
function cvCliff(g,q,side,x0,x1,top,base){const L=side<0;g.beginPath();if(L){g.moveTo(0,base+4);g.lineTo(0,top);for(let x=0;x<=x1;x+=5){const t=x/x1;g.lineTo(x,top+Math.pow(t,2.2)*(base-top)+(q()-.5)*4);}g.lineTo(x1,base+4);}else{g.moveTo(400,base+4);g.lineTo(400,top);for(let x=400;x>=x0;x-=5){const t=(400-x)/(400-x0);g.lineTo(x,top+Math.pow(t,2.2)*(base-top)+(q()-.5)*4);}g.lineTo(x0,base+4);}g.closePath();
 const gg=g.createLinearGradient(0,top,0,base);gg.addColorStop(0,'#e3a067');gg.addColorStop(.6,'#b8693a');gg.addColorStop(1,'#7d4224');g.fillStyle=gg;g.fill();
 g.save();g.clip();g.strokeStyle='rgba(80,35,15,.35)';g.lineWidth=1;for(let y=top+6;y<base;y+=5){g.beginPath();g.moveTo(L?0:x0,y+(q()-.5)*2);g.lineTo(L?x1:400,y+(q()-.5)*3);g.stroke();}g.restore();
 for(let i=0;i<10;i++){const x=L?q()*x1*.75:400-q()*(400-x0)*.75,t=L?x/x1:(400-x)/(400-x0),y=top+Math.pow(t,2.2)*(base-top);g.fillStyle=i%2?'#2f6a2c':'#3f7f35';g.beginPath();g.arc(x,y-3,4+q()*4,0,TAU);g.fill();}}
function cvSail(g,x,y,s){g.save();g.translate(x,y);g.scale(s,s);g.fillStyle='#f4f6f9';g.beginPath();g.moveTo(-16,0);g.lineTo(18,0);g.lineTo(14,5);g.lineTo(-13,5);g.closePath();g.fill();g.fillStyle='#2a3a55';g.fillRect(-1,-30,1.6,30);g.fillStyle='rgba(255,255,255,.95)';g.beginPath();g.moveTo(1,-28);g.lineTo(14,-2);g.lineTo(1,-2);g.closePath();g.fill();g.beginPath();g.moveTo(-1,-24);g.lineTo(-13,-2);g.lineTo(-1,-2);g.closePath();g.fill();g.restore();}
function cvPiri(g,x,y,s){g.save();g.translate(x,y);g.scale(s,s);g.fillStyle='#8a5a2b';g.beginPath();g.moveTo(-24,0);g.lineTo(26,0);g.quadraticCurveTo(24,8,16,9);g.lineTo(-18,9);g.closePath();g.fill();g.fillStyle='#f2efe6';g.fillRect(-24,0,50,2.5);g.strokeStyle='#5b3a1e';g.lineWidth=1.6;for(const px of[-18,-6,6,18]){g.beginPath();g.moveTo(px,0);g.lineTo(px,-18);g.stroke();}g.fillStyle='#d9b25a';g.beginPath();g.moveTo(-26,-17);g.lineTo(28,-17);g.lineTo(22,-25);g.lineTo(-20,-25);g.closePath();g.fill();g.strokeStyle='#a9822f';g.lineWidth=.8;for(let i=-24;i<27;i+=3){g.beginPath();g.moveTo(i,-17);g.lineTo(i+1,-13);g.stroke();}g.restore();}
function cvPolice(g,x,y,s,t){g.save();g.translate(x,y);g.scale(s,s);
 g.save();g.globalCompositeOperation='lighter';for(const[c,dx]of[['rgba(255,40,60,.75)',-13],['rgba(40,110,255,.75)',-3]]){const gg=g.createRadialGradient(dx,-42,0,dx,-42,30);gg.addColorStop(0,c);gg.addColorStop(1,'rgba(0,0,0,0)');g.fillStyle=gg;g.fillRect(dx-32,-74,64,64);}g.restore();
 g.fillStyle='#f3f5f8';g.beginPath();g.moveTo(-70,0);g.lineTo(58,0);g.quadraticCurveTo(78,-2,88,-18);g.lineTo(-68,-18);g.closePath();g.fill();
 g.fillStyle='#1e4fd8';g.beginPath();g.moveTo(-68,-11);g.lineTo(86,-11);g.lineTo(82,-6);g.lineTo(-68,-6);g.closePath();g.fill();
 g.fillStyle='#2a3140';g.fillRect(-68,-3,128,3);g.fillStyle='#e9edf2';g.beginPath();g.roundRect(-34,-38,50,20,3);g.fill();g.fillStyle='#1b2a44';g.fillRect(-30,-34,42,8);
 g.fillStyle='#ff2a3a';g.fillRect(-18,-44,10,5);g.fillStyle='#2a5bff';g.fillRect(-8,-44,10,5);
 g.fillStyle='#fff';g.font='800 9px "Saira Condensed",sans-serif';g.textAlign='center';g.textBaseline='middle';g.fillText('POLICÍA',20,-8.5);
 cvSpray(g,rng(9),-66,-2,Math.PI*1.05,.8,70,40,6);g.restore();}
function cvBuoy(g,x,y,r){const gg=g.createRadialGradient(x-r*.35,y-r*.35,1,x,y,r);gg.addColorStop(0,'#ffd1a8');gg.addColorStop(.45,'#ff7a1a');gg.addColorStop(1,'#b8420a');g.fillStyle=gg;g.beginPath();g.arc(x,y,r,0,TAU);g.fill();g.fillStyle='rgba(255,255,255,.7)';g.beginPath();g.ellipse(x,y+r*.9,r*1.4,r*.35,0,0,TAU);g.fill();}
function cvFloat(g,x,y,s,kind,hair,bik){g.save();g.translate(x,y);g.scale(s,s);
 if(kind){g.fillStyle='#ff6fb1';g.beginPath();g.ellipse(0,0,22,8,0,0,TAU);g.fill();g.strokeStyle='#ff6fb1';g.lineWidth=5;g.lineCap='round';g.beginPath();g.moveTo(16,-2);g.quadraticCurveTo(26,-20,18,-30);g.stroke();g.fillStyle='#ff6fb1';g.beginPath();g.arc(18,-31,5,0,TAU);g.fill();g.fillStyle='#222';g.beginPath();g.moveTo(22,-31);g.lineTo(28,-28);g.lineTo(22,-28);g.fill();}
 else{g.fillStyle='#ffffff';g.beginPath();g.ellipse(0,0,22,9,0,0,TAU);g.fill();g.fillStyle='#ff4f6b';for(let i=0;i<6;i++){g.beginPath();g.ellipse(Math.cos(i)*16,Math.sin(i)*6,4,3.5,0,0,TAU);g.fill();}g.fillStyle='rgba(0,90,140,.55)';g.beginPath();g.ellipse(0,0,10,4,0,0,TAU);g.fill();}
 g.fillStyle='#f0c09a';g.beginPath();g.arc(-4,-14,5,0,TAU);g.fill();g.fillStyle=hair;g.beginPath();g.arc(-5,-16,5.4,Math.PI,TAU);g.fill();g.fillRect(-10,-16,4,10);
 g.fillStyle='#f0c09a';g.beginPath();g.roundRect(-8,-9,9,11,3);g.fill();g.fillStyle=bik;g.fillRect(-8,-6,9,3);
 g.strokeStyle='#f0c09a';g.lineWidth=2.4;g.lineCap='round';g.beginPath();g.moveTo(0,-8);g.lineTo(8,-20);g.stroke();g.restore();}
function cvFirework(g,q,x,y,r,col){for(let i=0;i<26;i++){const a=i/26*TAU,d=r*(.75+q()*.3);g.strokeStyle=rgbaH(col,.85);g.lineWidth=1.4;g.beginPath();g.moveTo(x+Math.cos(a)*d*.35,y+Math.sin(a)*d*.35);g.lineTo(x+Math.cos(a)*d,y+Math.sin(a)*d);g.stroke();g.fillStyle='#fff';g.beginPath();g.arc(x+Math.cos(a)*d,y+Math.sin(a)*d,1.1,0,TAU);g.fill();}
 const gg=g.createRadialGradient(x,y,0,x,y,r);gg.addColorStop(0,rgbaH(col,.35));gg.addColorStop(1,rgbaH(col,0));g.fillStyle=gg;g.beginPath();g.arc(x,y,r,0,TAU);g.fill();}
function cvCity(g,q,x0,x1,hz,hmax){const cols=['#f4efe6','#ead9b9','#f2c9a0','#dfe7ee','#f7f3ea','#e7c08e'];let x=x0;while(x<x1){const w=9+q()*16,t=(x-x0)/(x1-x0),h=6+q()*hmax*(1-t*.75);g.fillStyle=cols[(q()*6)|0];g.fillRect(x,hz-h,w-1.2,h);g.fillStyle='rgba(40,60,90,.35)';for(let wy=hz-h+3;wy<hz-3;wy+=5)for(let wx=x+2;wx<x+w-4;wx+=4)if(q()<.7)g.fillRect(wx,wy,1.6,2.2);if(q()<.35){g.fillStyle='#c4683c';g.fillRect(x-.5,hz-h-2,w,2.5);}x+=w;}}
function cvPalm(g,x,y,s){g.save();g.translate(x,y);g.scale(s,s);g.strokeStyle='#6b4a2a';g.lineWidth=3;g.beginPath();g.moveTo(0,0);g.quadraticCurveTo(4,-16,2,-30);g.stroke();g.strokeStyle='#2f8a3a';g.lineWidth=2.6;g.lineCap='round';for(let i=0;i<7;i++){const a=-Math.PI/2+(i-3)*.5;g.beginPath();g.moveTo(2,-30);g.quadraticCurveTo(2+Math.cos(a)*10,-30+Math.sin(a)*10-4,2+Math.cos(a)*18,-30+Math.sin(a)*12+6);g.stroke();}g.restore();}
function drawCover(c,zi){const g=c.getContext('2d'),W=400,H=225,HZ=96,C=COVER[zi],Z=ZONES[zi],q=rng(77+zi*31),T=Date.now()/1000;
 g.setTransform(c.width/W,0,0,c.height/H,0,0);g.clearRect(0,0,W,H);g.lineCap='butt';g.lineJoin='miter';
 let gg=g.createLinearGradient(0,0,0,HZ);gg.addColorStop(0,C.sky[0]);gg.addColorStop(1,C.sky[1]);g.fillStyle=gg;g.fillRect(0,0,W,HZ+1);
 if(C.moon){for(let i=0;i<70;i++){g.fillStyle=`rgba(255,255,255,${.3+q()*.6})`;g.fillRect(q()*W,q()*HZ*.8,1,1);}const[mx,my]=C.moon;gg=g.createRadialGradient(mx,my,0,mx,my,50);gg.addColorStop(0,'rgba(220,235,255,.55)');gg.addColorStop(1,'rgba(220,235,255,0)');g.fillStyle=gg;g.fillRect(0,0,W,HZ);g.fillStyle='#eef4ff';g.beginPath();g.arc(mx,my,11,0,TAU);g.fill();}
 if(C.sun){const[sx,sy,col]=C.sun;gg=g.createRadialGradient(sx,sy,0,sx,sy,90);gg.addColorStop(0,rgbaH(col,1));gg.addColorStop(.13,rgbaH(col,1));gg.addColorStop(.18,rgbaH(col,.5));gg.addColorStop(1,rgbaH(col,0));g.fillStyle=gg;g.fillRect(0,0,W,HZ);
  g.save();g.globalAlpha=.12;g.fillStyle=col;for(let i=0;i<10;i++){const a=i/10*TAU+.2;g.beginPath();g.moveTo(sx,sy);g.lineTo(sx+Math.cos(a)*220,sy+Math.sin(a)*220);g.lineTo(sx+Math.cos(a+.08)*220,sy+Math.sin(a+.08)*220);g.closePath();g.fill();}g.restore();}
 const dark=C.land==='storm';
 for(let i=0;i<(dark?9:4);i++){const x=q()*W,y=8+q()*(dark?40:46),s=10+q()*16;g.fillStyle=dark?`rgba(30,40,70,${.7+q()*.3})`:`rgba(255,255,255,${.22+q()*.3})`;for(let k=0;k<5;k++){g.beginPath();g.ellipse(x+(k-2)*s*.7,y+Math.abs(k-2)*2,s*(1-Math.abs(k-2)*.18),s*.45,0,0,TAU);g.fill();}}
 const L=C.land;
 if(L==='port'||L==='final'){cvRidge(g,q,-20,260,HZ,34,4,L==='final'?'#7a6a7e':'#8fb07c');g.fillStyle=rgbaH(C.sky[1],.35);g.fillRect(0,40,W,HZ-40);cvCity(g,q,0,300,HZ,30);g.fillStyle='#d8d2c4';g.fillRect(250,HZ-4,150,4);g.fillStyle='#ffffff';g.fillRect(352,HZ-34,8,30);g.fillStyle='#e3202b';g.fillRect(352,HZ-28,8,5);g.fillRect(352,HZ-16,8,5);g.fillStyle='#ffe58a';g.fillRect(353,HZ-38,6,4);for(let i=0;i<6;i++){g.fillStyle='#fff';g.fillRect(262+i*14,HZ-7,10,3);}cvPalm(g,30,HZ+2,.8);cvPalm(g,52,HZ+3,.7);
  if(L==='final'){cvFirework(g,q,90,30,22,'#ffd21a');cvFirework(g,q,320,22,26,'#ff3f8e');cvFirework(g,q,215,44,16,'#33d6ff');}}
 if(L==='cala'){cvCliff(g,q,-1,0,130,30,HZ+6);cvCliff(g,q,1,270,400,24,HZ+6);}
 if(L==='mago'){g.fillStyle='#5f8f4a';g.beginPath();g.moveTo(40,HZ);g.quadraticCurveTo(90,HZ-26,150,HZ-6);g.quadraticCurveTo(170,HZ-2,180,HZ);g.closePath();g.fill();g.fillStyle='#e9d3a0';g.fillRect(40,HZ-2,140,2);cvCliff(g,q,1,250,400,14,HZ+8);cvSail(g,230,HZ+3,.55);cvSail(g,205,HZ+6,.7);cvSail(g,258,HZ+10,.8);}
 if(L==='beach'||L==='wave'){cvRidge(g,q,-20,420,HZ-4,30,5,L==='wave'?'#4a3a6e':'#7b93b8');if(L==='beach'){for(let x=0;x<W;x+=22){const h=10+q()*18;g.fillStyle=q()<.5?'#f6f2ea':'#efe0c8';g.fillRect(x,HZ-6-h,18,h);g.fillStyle='rgba(60,90,130,.35)';for(let wy=HZ-6-h+3;wy<HZ-8;wy+=4)g.fillRect(x+2,wy,14,1.2);}g.fillStyle='#f1d9a6';g.fillRect(0,HZ-6,W,7);for(let x=6;x<W;x+=11){g.fillStyle=['#ff4f6b','#33a3ff','#ffd21a','#ffffff'][(q()*4)|0];g.beginPath();g.ellipse(x,HZ-8,4,1.6,0,0,TAU);g.fill();}}}
 if(L==='chase'){cvCliff(g,q,-1,0,150,28,HZ+6);cvRidge(g,q,150,420,HZ,20,3,'#8aa0bf');}
 if(L==='trenc'){g.fillStyle='#bfe7f0';g.beginPath();g.ellipse(300,HZ,40,6,0,Math.PI,TAU);g.fill();g.fillStyle='#9cc58a';g.beginPath();g.ellipse(300,HZ-3,26,5,0,Math.PI,TAU);g.fill();g.fillStyle='#fbf3df';g.beginPath();g.moveTo(-10,HZ+2);for(let x=-10;x<=200;x+=8)g.lineTo(x,HZ-8-Math.sin(x*.05)*5-q()*2);g.lineTo(200,HZ+2);g.closePath();g.fill();g.strokeStyle='#8bb862';g.lineWidth=1;for(let i=0;i<24;i++){const x=q()*190,y=HZ-8-q()*6;g.beginPath();g.moveTo(x,y+4);g.lineTo(x-2,y-2);g.moveTo(x,y+4);g.lineTo(x+2,y-1);g.stroke();}}
 if(L==='tram'){g.fillStyle='#93a3bb';g.beginPath();g.moveTo(0,HZ);g.quadraticCurveTo(30,HZ-22,70,HZ-18);g.quadraticCurveTo(110,HZ-12,140,HZ);g.closePath();g.fill();cvMount(g,q,160,400,HZ,18,'#7d8aa2','rgba(60,70,90,.35)');g.fillStyle=rgbaH(C.sky[1],.25);g.fillRect(160,0,240,HZ);cvMount(g,q,235,400,HZ+4,4,'#5c6372','rgba(30,34,44,.5)');for(let i=0;i<18;i++){const x=250+q()*150,y=HZ-10-q()*30;g.fillStyle=i%2?'#3b5a33':'#2f4b2a';g.beginPath();g.arc(x,y,2+q()*2.5,0,TAU);g.fill();}}
 if(L==='storm'){cvRidge(g,q,-20,420,HZ,40,8,'#111a30');g.strokeStyle='#e8f1ff';g.lineWidth=2.2;g.shadowColor='#9cc8ff';g.shadowBlur=14;g.beginPath();g.moveTo(250,6);g.lineTo(238,34);g.lineTo(252,36);g.lineTo(236,70);g.lineTo(248,72);g.lineTo(232,HZ);g.stroke();g.shadowBlur=0;}
 // mar
 gg=g.createLinearGradient(0,HZ,0,H);gg.addColorStop(0,C.sea[0]);gg.addColorStop(1,C.sea[1]);g.fillStyle=gg;g.fillRect(0,HZ,W,H-HZ);
 if(C.sun&&C.sun[1]>60){const sx=C.sun[0];gg=g.createLinearGradient(sx-30,0,sx+30,0);gg.addColorStop(0,rgbaH(C.sun[2],0));gg.addColorStop(.5,rgbaH(C.sun[2],.45));gg.addColorStop(1,rgbaH(C.sun[2],0));g.fillStyle=gg;g.fillRect(sx-30,HZ,60,H-HZ);}
 for(let i=0;i<170;i++){const t=q(),y=HZ+2+t*t*(H-HZ),w=2+(y-HZ)*.16*q();g.fillStyle=`rgba(255,255,255,${(dark?.12:.22)+q()*.3})`;g.fillRect(q()*W,y,w,.8+(y-HZ)*.012);}
 g.fillStyle='rgba(255,255,255,.75)';g.fillRect(0,HZ,W,.8);
 // escena
 const me=MOTOS[G.moto|0]||MOTOS[0],av=(AVATARS[G.avatar|0]||AVATARS[0]).face,riv=MOTOS.filter(m=>m!==me),rv=i=>riv[(i+zi)%riv.length];
 const hero=(x,y,sc,rot,air)=>cvJet(g,q,sideOf(me),av,av.vest,x,y,sc,rot,air);
 if(L==='cala'){for(let i=0;i<5;i++){const t=i/4,y=HZ+10+Math.pow(t,1.6)*110,x=200+(i%2?1:-1)*(30+t*90);cvBuoy(g,x,y,2+t*7);}hero(250,168,.4,-.12,0);}
 else if(L==='mago'){cvPiri(g,96,HZ+22,.9);cvRival(g,q,rv(0),120,140,.24,-.04);hero(270,162,.42,-.16,0);}
 else if(L==='chase'){cvPolice(g,110,170,.85,T);hero(285,150,.42,-.18,14);}
 else if(L==='wave'){g.save();gg=g.createLinearGradient(0,40,0,H);gg.addColorStop(0,'#5fd2dc');gg.addColorStop(.5,'#1f7fb6');gg.addColorStop(1,'#0c3a74');g.fillStyle=gg;g.beginPath();g.moveTo(90,H);g.bezierCurveTo(180,205,230,120,290,64);g.bezierCurveTo(330,30,385,26,410,52);g.lineTo(410,H);g.closePath();g.fill();
  g.strokeStyle='rgba(255,255,255,.9)';g.lineWidth=6;g.lineCap='round';g.beginPath();g.moveTo(292,62);g.bezierCurveTo(332,30,384,28,406,50);g.stroke();cvSpray(g,q,330,40,-Math.PI*.6,1.6,40,70,3);g.fillStyle='rgba(8,40,80,.35)';g.beginPath();g.ellipse(360,90,34,26,-.3,0,TAU);g.fill();
  g.strokeStyle='rgba(255,255,255,.35)';g.lineWidth=1.4;for(let i=0;i<7;i++){g.beginPath();g.moveTo(150+i*24,215-i*18);g.quadraticCurveTo(200+i*20,190-i*20,240+i*18,150-i*16);g.stroke();}g.restore();hero(240,138,.37,-.36,44);}
 else if(L==='trenc'){cvFloat(g,60,HZ+24,.7,1,'#5a3218','#ff3f8e');cvFloat(g,150,HZ+14,.5,0,'#f2cf63','#22c4ff');cvFloat(g,355,HZ+34,.8,0,'#111111','#ffd21a');cvRival(g,q,rv(0),110,150,.26,-.05);hero(275,165,.42,-.15,0);}
 else if(L==='tram'){cvRival(g,q,rv(0),70,130,.2,-.03);cvRival(g,q,rv(1),150,150,.27,-.06);hero(250,170,.42,-.14,0);}
 else if(L==='storm'){g.strokeStyle='rgba(190,215,255,.28)';g.lineWidth=1;for(let i=0;i<90;i++){const x=q()*W,y=q()*H;g.beginPath();g.moveTo(x,y);g.lineTo(x-5,y+12);g.stroke();}gg=g.createLinearGradient(300,140,400,120);gg.addColorStop(0,'rgba(255,250,210,.4)');gg.addColorStop(1,'rgba(255,250,210,0)');g.fillStyle=gg;g.beginPath();g.moveTo(318,128);g.lineTo(400,96);g.lineTo(400,170);g.closePath();g.fill();hero(250,160,.42,-.18,10);}
 else if(L==='final'){cvRival(g,q,SHARK,150,152,.36,-.08);hero(285,168,.42,-.15,0);}
 else{cvRival(g,q,rv(0),70,128,.2,-.04);cvRival(g,q,rv(1),140,146,.26,-.07);hero(275,168,.42,-.16,0);}
 // velocidad + viñeta
 g.save();g.globalAlpha=.18;g.strokeStyle='#fff';g.lineWidth=1.2;for(let i=0;i<14;i++){const y=110+q()*110,x=q()*160;g.beginPath();g.moveTo(x,y);g.lineTo(x+30+q()*50,y-6);g.stroke();}g.restore();
 gg=g.createRadialGradient(W*.55,H*.5,H*.35,W*.55,H*.5,W*.75);gg.addColorStop(0,'rgba(0,0,0,0)');gg.addColorStop(1,'rgba(0,8,24,.55)');g.fillStyle=gg;g.fillRect(0,0,W,H);
 gg=g.createLinearGradient(0,0,0,74);gg.addColorStop(0,'rgba(5,14,34,.55)');gg.addColorStop(1,'rgba(5,14,34,0)');g.fillStyle=gg;g.fillRect(0,0,W,74);
 // título
 g.save();g.textBaseline='alphabetic';g.textAlign='left';g.lineJoin='round';
 g.font='800 13px "Saira Condensed",sans-serif';const zt='ZONA '+(zi+1),zw=g.measureText(zt).width+16;g.fillStyle='#ff7a1a';g.beginPath();g.roundRect(12,10,zw,19,9.5);g.fill();g.fillStyle='#fff';g.fillText(zt,20,24);
 let nm=Z.name,pre='';if(nm.indexOf('CARRERA ')===0){pre='CARRERA';nm=nm.slice(8);}
 g.translate(14,0);g.transform(1,0,-.16,1,0,0);let fs=44;g.font=`800 ${fs}px "Saira Condensed",sans-serif`;while(g.measureText(nm).width>250&&fs>24){fs-=2;g.font=`800 ${fs}px "Saira Condensed",sans-serif`;}
 let y=31+(pre?14:0)+fs*.8;
 if(pre){g.font='800 16px "Saira Condensed",sans-serif';g.lineWidth=4;g.strokeStyle='#0a1630';g.strokeText(pre,4,44);g.fillStyle='#33d6ff';g.fillText(pre,4,44);g.font=`800 ${fs}px "Saira Condensed",sans-serif`;}
 g.fillStyle='rgba(0,0,0,.4)';g.fillText(nm,4,y+3);g.lineWidth=6;g.strokeStyle='#0a1630';g.strokeText(nm,2,y);gg=g.createLinearGradient(0,y-fs*.8,0,y);gg.addColorStop(0,'#ffffff');gg.addColorStop(.5,'#ffe08a');gg.addColorStop(1,'#ff8a2a');g.fillStyle=gg;g.fillText(nm,2,y);
 g.font='700 12px "Saira Condensed",sans-serif';const tw=g.measureText(C.tag).width+14;g.fillStyle='rgba(8,22,48,.75)';g.beginPath();g.roundRect(2,y+6,tw,17,8.5);g.fill();g.fillStyle='#33d6ff';g.fillText(C.tag,9,y+18.5);
 g.restore();}
