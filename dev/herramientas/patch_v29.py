p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)

rep("{name:'FORMENTERA',obj:'race3',goal:'Termina entre los 3 primeros hasta la punta de Ses Illetes. Agua transparente, muchos barcos fondeados y praderas de posidonia que te frenan.',len:16000,riv:5,bar:null,",
    "{name:'FORMENTERA',obj:'race3',goal:'Termina entre los 3 primeros hasta la punta de Ses Illetes. Agua transparente, muchos barcos fondeados y praderas de posidonia que te frenan. A mitad, el Beso Beach.',len:16000,riv:5,bar:'beso',")
rep("if(Zn.bar==='jj')drawJJTop(g,Zn);else drawRoxyTop(g,Zn);","if(Zn.bar==='jj')drawJJTop(g,Zn);else if(Zn.bar==='beso')drawBesoTop(g,Zn);else drawRoxyTop(g,Zn);")
rep("if(G.zone.bar==='jj'){show('scrJJ');drawJJFront($('#jjCv'));renderJJ();}",
    "if(G.zone.bar==='jj'||G.zone.bar==='beso'){const beso=G.zone.bar==='beso';show('scrJJ');(beso?drawBesoFront:drawJJFront)($('#jjCv'));$('#jjH').innerHTML=beso?'<small>BESO BEACH · FORMENTERA</small>EL CHIRINGUITO':\"<small>JJ'S SPORTS LOUNGE</small>EL BAR DEL PUERTO\";const bb=$('#jjBub');bb.style.left=beso?'4%':'58%';bb.style.top=beso?'8%':'12%';renderJJ();}")
rep("<h3><small>JJ'S SPORTS LOUNGE</small>EL BAR DEL PUERTO</h3>","<h3 id=\"jjH\"><small>JJ'S SPORTS LOUNGE</small>EL BAR DEL PUERTO</h3>")
rep('<div class="bubble" style="left:58%;top:12%">¿Qué te pongo,<br>piloto?</div>','<div class="bubble" id="jjBub" style="left:58%;top:12%">¿Qué te pongo,<br>piloto?</div>')
rep("label(r.x+(r.x>WG-110?-60:62),r.y-4,Zn.bar==='jj'?\"BAR JJ'S\":'BAR ROXY',Zn.bar==='jj'?'VIDAS · GASOLINA':'PIEZAS · GASOLINA');",
    "label(r.x+(r.x>WG-110?-60:62),r.y-4,Zn.bar==='jj'?\"BAR JJ'S\":Zn.bar==='beso'?'BESO BEACH':'BAR ROXY',Zn.bar==='roxy'?'PIEZAS · GASOLINA':'VIDAS · GASOLINA');")
rep("tag(Z.bar==='jj'?\"Bar JJ's a mitad de zona\":Z.bar==='roxy'?","tag(Z.bar==='jj'?\"Bar JJ's a mitad de zona\":Z.bar==='beso'?'Beso Beach a mitad de zona':Z.bar==='roxy'?")

rep("function drawRoxyTop(g,Zn){","""function drawBesoTop(g,Zn){const by=Zn.barY,sx=Zn.shore(by),q=rng(77);g.save();g.translate(sx,by);
 for(const[x,y,R]of[[-118,-58,26],[-104,-6,30],[-122,44,24],[-78,-74,18]]){g.fillStyle='rgba(30,40,20,.25)';g.beginPath();g.arc(x+8,y+7,R,0,TAU);g.fill();const cols=['#2f5a26','#3b6b2c','#4f8a38','#6aa046'];for(let i=0;i<14;i++){const a=q()*TAU,d=q()*R*.6;g.fillStyle=cols[Math.min(3,(i/4)|0)];g.beginPath();g.arc(x+Math.cos(a)*d,y+Math.sin(a)*d,R*(.45+q()*.25)*(1-i/30),0,TAU);g.fill();}}
 g.fillStyle='rgba(60,40,10,.25)';g.fillRect(-88,-34,52,70);g.fillStyle='#cdb58a';g.fillRect(-94,-40,52,70);g.strokeStyle='#b89c6c';g.lineWidth=1;for(let y=-38;y<30;y+=3){g.beginPath();g.moveTo(-94,y);g.lineTo(-42,y+(q()-.5));g.stroke();}
 g.strokeStyle='#a8895a';g.lineWidth=1.2;for(let y=-40;y<=30;y+=2.5){g.beginPath();g.moveTo(-42,y);g.lineTo(-38,y+1);g.stroke();}
 g.fillStyle='#e8d7b0';g.fillRect(-60,-60,12,12);g.fillRect(-58,40,12,12);
 g.save();g.translate(-30,-48);g.fillStyle='#ffffff';g.font='900 18px "Saira Condensed",sans-serif';g.textAlign='center';g.textBaseline='middle';g.fillStyle='rgba(0,0,0,.25)';g.fillText('B',2,2);g.fillStyle='#ffffff';g.fillText('B',0,0);g.restore();
 for(let i=0;i<6;i++){const x=-30+(i%2)*14,y=-30+i*12;g.fillStyle='rgba(60,40,10,.18)';g.fillRect(x+2,y+2,9,13);g.fillStyle='#d9c7a3';g.fillRect(x-1,y-1,11,15);g.fillStyle='#f7f7f4';g.fillRect(x,y,9,13);g.fillStyle=['#bfe3f2','#f6c8d8','#f7f7f4'][i%3];g.fillRect(x+1,y+1,7,3);}
 for(const[x,y]of[[-22,-40],[-8,-6],[-24,28],[-8,44]]){g.fillStyle='rgba(60,40,10,.2)';g.beginPath();g.arc(x+3,y+3,8,0,TAU);g.fill();g.fillStyle='#fbfaf6';g.beginPath();g.arc(x,y,8,0,TAU);g.fill();g.strokeStyle='rgba(0,0,0,.1)';g.lineWidth=.8;for(let k=0;k<8;k++){const a=k/8*TAU;g.beginPath();g.moveTo(x,y);g.lineTo(x+Math.cos(a)*8,y+Math.sin(a)*8);g.stroke();}}
 g.fillStyle='#ff7fae';g.beginPath();g.ellipse(-6,16,6,3,.4,0,TAU);g.fill();
 g.restore();}
function drawBesoFront(cvs){const g=cvs.getContext('2d');g.setTransform(2,0,0,2,0,0);const W=390,H=210,r=rng(9);g.clearRect(0,0,W,H);
 let gg=g.createLinearGradient(0,0,0,130);gg.addColorStop(0,'#3d8fe0');gg.addColorStop(1,'#cbe6f8');g.fillStyle=gg;g.fillRect(0,0,W,140);
 g.fillStyle='rgba(255,255,255,.55)';for(const[x,y,w]of[[40,22,70],[300,16,60],[330,40,40],[150,12,50]]){g.beginPath();g.ellipse(x,y,w/2,5,0,0,TAU);g.fill();}
 const pine=(x,y,cw,ch,tx,ty)=>{g.strokeStyle='#6b5a48';g.lineWidth=4;g.lineCap='round';g.beginPath();g.moveTo(tx,ty);g.quadraticCurveTo((tx+x)/2-8,(ty+y)/2,x,y+ch*.3);g.stroke();g.lineWidth=2.4;g.beginPath();g.moveTo(x,y+ch*.3);g.lineTo(x-cw*.3,y+ch*.2);g.moveTo(x,y+ch*.3);g.lineTo(x+cw*.3,y+ch*.25);g.stroke();
  const cols=['#2f5a26','#3b6b2c','#4f8a38','#6aa046'];for(let i=0;i<26;i++){const a=r()*TAU,d=r();g.fillStyle=cols[Math.min(3,(i/7)|0)];g.beginPath();g.ellipse(x+Math.cos(a)*cw*.42*d,y+Math.sin(a)*ch*.35*d-(i>18?3:0),cw*(.16+r()*.12),ch*(.2+r()*.12),0,0,TAU);g.fill();}};
 g.fillStyle='#3e6a30';g.beginPath();g.moveTo(0,118);for(let x=0;x<=W;x+=10)g.lineTo(x,92-Math.sin(x*.05)*8-r()*8);g.lineTo(W,118);g.closePath();g.fill();
 pine(170,40,150,46,182,118);pine(300,56,140,44,292,118);pine(60,70,90,34,66,118);pine(372,70,70,30,368,118);
 // chiringuito
 g.fillStyle='#3d2e22';g.globalAlpha=.55;g.fillRect(120,100,210,24);g.globalAlpha=1;
 for(let i=0;i<14;i++){const x=128+i*14.5;g.fillStyle=['#e8b48c','#c98d62','#f0c4a0'][i%3];g.beginPath();g.arc(x,110,2.6,0,TAU);g.fill();g.fillStyle=['#ffffff','#1e5eff','#ff3f8e','#ffd21a'][i%4];g.fillRect(x-2.5,112.5,5,6);}
 g.strokeStyle='#cdb58a';g.lineWidth=1;for(let y=116;y<=124;y+=4){g.beginPath();g.moveTo(120,y);g.lineTo(330,y);g.stroke();}
 g.fillStyle='#c9b38a';for(const x of[124,170,220,270,326])g.fillRect(x-1.5,98,3,28);
 const roof=(x0,x1,y)=>{g.fillStyle='#d4bd8f';g.fillRect(x0,y-6,x1-x0,8);g.strokeStyle='#b89c6c';g.lineWidth=1.1;for(let x=x0;x<x1;x+=2){g.beginPath();g.moveTo(x,y);g.lineTo(x+(r()-.5)*1.5,y+5+r()*4);g.stroke();}g.fillStyle='#e3cfa4';g.fillRect(x0,y-7,x1-x0,2);};
 roof(116,334,98);roof(46,104,104);g.fillStyle='#3d2e22';g.globalAlpha=.45;g.fillRect(50,108,50,18);g.globalAlpha=1;g.fillStyle='#c9b38a';g.fillRect(52,104,2.5,22);g.fillRect(98,104,2.5,22);
 // la B
 g.fillStyle='#e9e4da';g.fillRect(118,64,3,62);g.fillStyle='rgba(0,0,0,.25)';g.font='900 34px "Saira Condensed",sans-serif';g.textAlign='center';g.textBaseline='middle';g.fillText('B',121,62);g.fillStyle='#ffffff';g.fillText('B',119,60);
 // arena
 gg=g.createLinearGradient(0,124,0,172);gg.addColorStop(0,'#eadfc8');gg.addColorStop(1,'#d8c6a6');g.fillStyle=gg;g.fillRect(0,124,W,48);for(let i=0;i<260;i++){g.fillStyle=r()>.5?'rgba(160,130,90,.25)':'rgba(255,255,255,.4)';g.fillRect(r()*W,126+r()*44,1,1);}
 g.fillStyle='#e8d7b0';g.fillRect(14,118,22,26);g.fillRect(352,114,20,26);g.fillStyle='#d6c39a';g.fillRect(14,118,22,3);g.fillRect(352,114,20,3);
 const umb=(x,y,w)=>{g.strokeStyle='#e9e6df';g.lineWidth=2;g.beginPath();g.moveTo(x,y-10);g.lineTo(x,y+26);g.stroke();gg=g.createLinearGradient(x-w/2,0,x+w/2,0);gg.addColorStop(0,'#ffffff');gg.addColorStop(1,'#d6d1c4');g.fillStyle=gg;g.beginPath();g.moveTo(x-w/2,y+2);g.quadraticCurveTo(x-w*.22,y-8,x,y-13);g.quadraticCurveTo(x+w*.22,y-8,x+w/2,y+2);g.closePath();g.fill();};
 const bed=(x,y,w,pil)=>{g.fillStyle='#d9c7a3';g.fillRect(x,y+8,w,4);g.fillRect(x+2,y+12,3,5);g.fillRect(x+w-5,y+12,3,5);g.fillStyle='#f7f7f4';g.beginPath();g.roundRect(x,y,w,9,3);g.fill();if(pil){g.fillStyle=pil;g.beginPath();g.roundRect(x+3,y-3,12,5,2);g.fill();}};
 umb(36,124,44);umb(170,128,40);umb(250,126,42);umb(330,122,40);
 bed(20,140,52,'#bfe3f2');bed(92,146,50,null);bed(160,144,56,'#f6c8d8');bed(232,146,50,'#bfe3f2');bed(300,140,58,null);
 g.fillStyle='#ff7fae';g.beginPath();g.ellipse(140,160,13,4,0,0,TAU);g.fill();g.strokeStyle='#ff7fae';g.lineWidth=3;g.lineCap='round';g.beginPath();g.moveTo(150,158);g.quadraticCurveTo(156,146,151,140);g.stroke();g.fillStyle='#ff7fae';g.beginPath();g.arc(151,139,3,0,TAU);g.fill();g.fillStyle='#222';g.beginPath();g.moveTo(153,139);g.lineTo(157,141);g.lineTo(153,141);g.fill();
 g.fillStyle='#1e5eff';g.fillRect(270,158,12,8);g.fillStyle='#ffffff';g.fillRect(270,158,12,2);
 gg=g.createLinearGradient(0,170,0,H);gg.addColorStop(0,'#7fe6e0');gg.addColorStop(1,'#13a6d2');g.fillStyle=gg;g.fillRect(0,170,W,H-170);
 for(let i=0;i<90;i++){const x=r()*W,y=172+r()*36,len=8+r()*18;g.strokeStyle=`rgba(255,255,255,${.12+r()*.15})`;g.lineWidth=.8;g.beginPath();g.moveTo(x,y);g.lineTo(x+len,y+(r()-.5)*2);g.stroke();}
 g.fillStyle='rgba(255,255,255,.8)';for(let x=0;x<W;x+=6){g.beginPath();g.arc(x+(r()*3),171+r()*2,1.4+r(),0,TAU);g.fill();}
 g.save();g.translate(36,152);g.scale(.42,.42);drawJetProfile(g,sideOf(MOTOS[G.moto]));g.restore();}
function drawRoxyTop(g,Zn){""")
open(p,'w').write(s);print('ok')
