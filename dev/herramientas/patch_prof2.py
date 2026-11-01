p='costa-turbo.html';s=open(p,encoding='utf-8').read()
a=s.index('function drawJetProfile(g,s){');b=s.index('function policePath(g,k){')
PROF=r'''function drawJetProfile(g,s){
 const L=(c,t)=>mixc(c,'#ffffff',t),Dk=(c,t)=>mixc(c,'#000000',t);let gg;
 g.fillStyle='rgba(0,30,60,.25)';g.beginPath();g.ellipse(172,114,160,6,0,0,TAU);g.fill();
 // tobera
 g.fillStyle='#2a2d33';g.beginPath();g.roundRect(2,97,17,10,3);g.fill();g.fillStyle='#545966';g.fillRect(2,98,4,8);
 // casco
 const hullP=()=>{g.beginPath();g.moveTo(14,82);g.lineTo(232,76);g.bezierCurveTo(280,73,316,66,338,60);g.bezierCurveTo(334,70,318,92,284,104);g.bezierCurveTo(262,111,236,113,206,113);g.lineTo(26,113);g.quadraticCurveTo(18,113,16,106);g.closePath();};
 hullP();gg=g.createLinearGradient(0,74,0,114);gg.addColorStop(0,L(s.hull,.22));gg.addColorStop(.45,s.hull);gg.addColorStop(1,Dk(s.hull,.35));g.fillStyle=gg;g.fill();
 g.save();hullP();g.clip();
  g.fillStyle=s.trim;g.globalAlpha=.9;g.beginPath();g.moveTo(0,104);g.lineTo(206,106);g.bezierCurveTo(250,106,292,96,332,70);g.lineTo(350,70);g.lineTo(350,130);g.lineTo(0,130);g.closePath();g.fill();g.globalAlpha=1;
  g.fillStyle=s.stripe;g.globalAlpha=.92;for(const[x,w]of[[168,20],[194,9]]){g.beginPath();g.moveTo(x+24,76);g.lineTo(x+24+w,76);g.lineTo(x+w,108);g.lineTo(x,108);g.closePath();g.fill();}g.globalAlpha=1;
  g.strokeStyle='rgba(255,255,255,.35)';g.lineWidth=1.2;g.beginPath();g.moveTo(110,99);g.bezierCurveTo(220,98,292,88,334,63);g.stroke();
  g.fillStyle='rgba(255,255,255,.28)';g.beginPath();g.moveTo(14,85);g.lineTo(232,79);g.bezierCurveTo(280,76,316,69,338,63);g.lineTo(338,65);g.bezierCurveTo(316,71,280,78,232,81);g.lineTo(14,87);g.closePath();g.fill();
 g.restore();
 g.fillStyle=s.trim;g.beginPath();g.moveTo(58,103);g.lineTo(150,99);g.lineTo(157,102);g.lineTo(64,107);g.closePath();g.fill();
 g.fillStyle='#3a3d45';g.beginPath();g.roundRect(7,85,12,3,1);g.fill();g.fillRect(9,88,2,15);g.fillRect(16,88,2,15);g.fillRect(8,94,11,2);g.fillRect(8,100,11,2);
 // costado de la cubierta
 const deckP=()=>{g.beginPath();g.moveTo(12,80);g.lineTo(12,72);g.lineTo(76,70);g.lineTo(82,64);g.lineTo(196,59);g.bezierCurveTo(214,52,226,40,240,33);g.bezierCurveTo(274,36,312,48,338,59);g.lineTo(232,75);g.closePath();};
 deckP();gg=g.createLinearGradient(0,33,0,80);gg.addColorStop(0,L(s.deck,.3));gg.addColorStop(.55,s.deck);gg.addColorStop(1,Dk(s.deck,.25));g.fillStyle=gg;g.fill();
 g.save();deckP();g.clip();
  g.strokeStyle='rgba(0,0,0,.28)';g.lineWidth=1.3;g.beginPath();g.moveTo(20,76);g.lineTo(220,69);g.bezierCurveTo(262,66,300,60,330,58);g.stroke();
  g.strokeStyle='rgba(255,255,255,.4)';g.lineWidth=1;g.beginPath();g.moveTo(84,66);g.lineTo(196,61);g.stroke();
  g.fillStyle=s.stripe;g.globalAlpha=.9;g.beginPath();g.moveTo(100,74);g.lineTo(190,64);g.lineTo(201,66);g.lineTo(112,76);g.closePath();g.fill();g.beginPath();g.moveTo(120,77);g.lineTo(196,69);g.lineTo(202,70);g.lineTo(127,78);g.closePath();g.fill();g.globalAlpha=1;
 g.restore();
 g.fillStyle='#2b2e35';g.beginPath();g.moveTo(12,72);g.lineTo(76,70);g.lineTo(79,67);g.lineTo(14,69);g.closePath();g.fill();
 // capó
 const hoodP=()=>{g.beginPath();g.moveTo(206,60);g.bezierCurveTo(216,50,226,40,240,33);g.bezierCurveTo(274,36,312,48,338,59);g.lineTo(300,64);g.bezierCurveTo(266,63,236,63,206,60);g.closePath();};
 hoodP();gg=g.createLinearGradient(0,32,0,64);gg.addColorStop(0,L(s.hood,.4));gg.addColorStop(.5,s.hood);gg.addColorStop(1,Dk(s.hood,.22));g.fillStyle=gg;g.fill();
 g.save();hoodP();g.clip();
  g.strokeStyle='rgba(0,0,0,.35)';g.lineWidth=1.4;g.beginPath();g.moveTo(246,40);g.lineTo(302,52);g.moveTo(254,47);g.lineTo(320,57);g.stroke();
  g.strokeStyle='rgba(255,255,255,.6)';g.lineWidth=1.3;g.beginPath();g.moveTo(240,34.5);g.bezierCurveTo(274,37.5,312,49.5,336,59.5);g.stroke();
  g.fillStyle='rgba(15,16,20,.85)';g.beginPath();g.moveTo(262,56);g.lineTo(298,58);g.lineTo(294,61);g.lineTo(266,60);g.closePath();g.fill();
 g.restore();
 // defensa delantera y luz
 g.fillStyle=s.trim;g.beginPath();g.moveTo(318,58);g.lineTo(339,59);g.lineTo(334,68);g.lineTo(316,64);g.closePath();g.fill();
 g.fillStyle='rgba(225,242,255,.95)';g.beginPath();g.moveTo(300,61.5);g.lineTo(318,62.5);g.lineTo(317,64.2);g.lineTo(301,63.4);g.closePath();g.fill();
 // banda de defensa (gunwale)
 g.strokeStyle=s.trim;g.lineWidth=5.5;g.lineCap='butt';g.beginPath();g.moveTo(12,81);g.lineTo(232,75);g.bezierCurveTo(280,72,316,65,338,59);g.stroke();
 g.strokeStyle='rgba(255,255,255,.5)';g.lineWidth=.9;g.beginPath();g.moveTo(12,84.5);g.lineTo(232,78.5);g.bezierCurveTo(280,75.5,316,68.5,336,62.5);g.stroke();
 // soporte del manillar
 g.fillStyle='#1b1d22';g.beginPath();g.moveTo(190,58);g.bezierCurveTo(198,48,206,38,220,32);g.lineTo(240,33);g.bezierCurveTo(228,40,216,50,206,60);g.closePath();g.fill();
 g.fillStyle='rgba(255,255,255,.15)';g.beginPath();g.moveTo(206,44);g.lineTo(220,34);g.lineTo(226,34);g.lineTo(210,46);g.closePath();g.fill();
 // espejo
 g.fillStyle=s.trim;g.beginPath();g.moveTo(252,36);g.lineTo(268,23);g.lineTo(277,25);g.lineTo(262,38);g.closePath();g.fill();g.fillStyle='rgba(160,210,255,.55)';g.beginPath();g.moveTo(259,32);g.lineTo(268,25.5);g.lineTo(272,26.5);g.lineTo(263,33);g.closePath();g.fill();
 // manillar
 g.lineCap='round';g.strokeStyle='#15171b';g.lineWidth=7;g.beginPath();g.moveTo(223,33);g.lineTo(216,18);g.stroke();
 g.lineWidth=5.5;g.beginPath();g.moveTo(203,15);g.lineTo(233,19.5);g.stroke();
 g.fillStyle='#2a2d33';g.beginPath();g.arc(203,15,4.4,0,TAU);g.fill();g.fillStyle='rgba(255,255,255,.3)';g.beginPath();g.arc(202,14,1.6,0,TAU);g.fill();
 g.strokeStyle='#15171b';g.lineWidth=1.6;g.beginPath();g.moveTo(213,20);g.lineTo(227,25);g.stroke();
 // asiento
 const seatP=()=>{g.beginPath();g.moveTo(80,66);g.bezierCurveTo(78,52,80,44,90,41);g.bezierCurveTo(100,38,112,38,124,40);g.bezierCurveTo(132,41,136,46,144,47);g.lineTo(178,47);g.bezierCurveTo(188,47,194,42,200,36);g.lineTo(206,40);g.bezierCurveTo(200,48,196,54,192,59);g.lineTo(84,64);g.closePath();};
 seatP();gg=g.createLinearGradient(0,36,0,66);gg.addColorStop(0,L(s.seatA,.28));gg.addColorStop(1,Dk(s.seatA,.22));g.fillStyle=gg;g.fill();
 g.save();seatP();g.clip();
  gg=g.createLinearGradient(0,36,0,66);gg.addColorStop(0,L(s.seatB,.25));gg.addColorStop(1,Dk(s.seatB,.22));g.fillStyle=gg;g.beginPath();g.moveTo(70,70);g.lineTo(70,30);g.lineTo(136,30);g.lineTo(128,70);g.closePath();g.fill();
  g.fillStyle=s.seatC;g.beginPath();g.moveTo(78,58);g.lineTo(198,52);g.lineTo(198,56.5);g.lineTo(78,63);g.closePath();g.fill();
  g.setLineDash([3,2]);g.strokeStyle='rgba(255,255,255,.4)';g.lineWidth=.8;g.beginPath();g.moveTo(86,46);g.bezierCurveTo(100,42.5,112,42.5,124,44.5);g.bezierCurveTo(132,45.5,136,50,144,51);g.lineTo(178,51);g.stroke();g.setLineDash([]);
  g.fillStyle='rgba(255,255,255,.25)';g.beginPath();g.ellipse(106,41.5,15,2,0,0,TAU);g.ellipse(162,48.5,15,1.7,0,0,TAU);g.fill();
 g.restore();
 g.strokeStyle='rgba(0,0,0,.35)';g.lineWidth=1;seatP();g.stroke();
 g.strokeStyle=s.trim;g.lineWidth=4;g.lineCap='round';g.beginPath();g.moveTo(84,60);g.bezierCurveTo(68,58,66,44,80,42);g.stroke();
 // agua
 g.save();hullP();g.clip();g.fillStyle='rgba(20,120,180,.38)';g.fillRect(0,108,350,30);g.restore();
 g.fillStyle='rgba(255,255,255,.88)';for(let i=0;i<20;i++){const x=22+i*15+Math.sin(i*2.3)*4;g.beginPath();g.ellipse(x,109+Math.sin(i)*1.2,4+Math.sin(i*1.7)*2,1.5,0,0,TAU);g.fill();}
}
'''
s=s[:a]+PROF+s[b:]
def rep(x,y):
    global s
    assert s.count(x)==1,x[:90]
    s=s.replace(x,y)
rep("g.save();g.translate(8,10);g.scale(.9,.9);drawJetProfile(g,m.side);g.restore();","g.save();g.translate(2,4);g.scale(.836,.836);drawJetProfile(g,m.side);g.restore();")
rep(" g.save();g.translate(40,152);g.scale(.42,.42);drawJetProfile(g,MOTOS[G.moto].side);g.restore();"," g.save();g.translate(36,152);g.scale(.42,.42);drawJetProfile(g,MOTOS[G.moto].side);g.restore();")
open(p,'w',encoding='utf-8').write(s)
print('ok')
