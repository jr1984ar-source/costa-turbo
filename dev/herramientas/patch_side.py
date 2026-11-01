import re
p='costa-turbo.html';s=open(p,encoding='utf-8').read()
# 1) MOTOS
a=s.index('const MOTOS=[');b=s.index('const SHARK=')
MOTOS='''const MOTOS=[
 {id:'brava',name:'BRAVA',colors:'Roja y blanca',pilot:'Toni Marín',bio:'Campeón del puerto. Equilibrada y fiable.',ui:'#e3202b',st:{vel:3,ace:3,giro:4,turbo:3},
  sk:{hull:'#f5f6f8',hullD:'#c3c9d2',acc:'#e3202b',seat:'#1d1f24',vest:'#e3202b',helmet:'#ffffff',hs:'#e3202b',arm:'#e3202b'},
  side:{deck:'#f2f3f5',hood:'#e3202b',hull:'#e3202b',trim:'#1b1d22',seatA:'#f2f3f5',seatB:'#e3202b',seatC:'#1b1d22',stripe:'#1b1d22'},face:{skin:'#e8b48c',hair:'#3a2414',style:'short',glasses:1,vest:'#e3202b'}},
 {id:'inferno',name:'INFERNO',colors:'Roja entera',pilot:'Carla Ruiz',bio:'Pura potencia. Acelera como nadie.',ui:'#ff3b3b',st:{vel:3,ace:5,giro:3,turbo:2},
  sk:{hull:'#e3202b',hullD:'#8f0f17',acc:'#ffffff',seat:'#1d1f24',vest:'#16181d',helmet:'#e3202b',hs:'#ffffff',arm:'#16181d'},
  side:{deck:'#de1a24',hood:'#e8262f',hull:'#cf1820',trim:'#1b1d22',seatA:'#d9161f',seatB:'#b0121a',seatC:'#1b1d22',stripe:'#1b1d22'},face:{skin:'#f0c09a',hair:'#8a1f12',style:'long',vest:'#16181d'}},
 {id:'avispa',name:'AVISPA',colors:'Negra y amarilla',pilot:'El Tito',bio:'Agresivo en las curvas. Pica fuerte.',ui:'#ffd21a',st:{vel:3,ace:3,giro:5,turbo:2},
  sk:{hull:'#25272e',hullD:'#0b0c0f',acc:'#ffd21a',seat:'#121317',vest:'#ffd21a',helmet:'#25272e',hs:'#ffd21a',arm:'#ffd21a'},
  side:{deck:'#2c2f36',hood:'#1c1e23',hull:'#ffd21a',trim:'#15171b',seatA:'#1d1f24',seatB:'#ffd21a',seatC:'#3a3d45',stripe:'#ffd21a'},face:{skin:'#c98d62',hair:'#111111',style:'buzz',beard:1,vest:'#ffd21a'}},
 {id:'oceano',name:'OCÉANO',colors:'Azul entera',pilot:'Sandra Vidal',bio:'La más rápida en recta. Punta máxima.',ui:'#3b82ff',st:{vel:5,ace:2,giro:3,turbo:3},
  sk:{hull:'#1e5eff',hullD:'#0b2c8f',acc:'#ffffff',seat:'#15171c',vest:'#ffffff',helmet:'#1e5eff',hs:'#ffffff',arm:'#1e5eff'},
  side:{deck:'#1e5eff',hood:'#2a6bff',hull:'#1746c4',trim:'#15171b',seatA:'#1e5eff',seatB:'#111827',seatC:'#2b3445',stripe:'#ffffff'},face:{skin:'#f2c6a2',hair:'#e8c35a',style:'pony',glasses:1,vest:'#1e5eff'}},
 {id:'marea',name:'MAREA',colors:'Azul y blanca',pilot:'Lucía Mar',bio:'Reina de las olas. Gira y salta como nadie.',ui:'#4d9bff',st:{vel:3,ace:4,giro:4,turbo:2},
  sk:{hull:'#f5f6f8',hullD:'#c3c9d2',acc:'#1e5eff',seat:'#1d1f24',vest:'#1e5eff',helmet:'#ffffff',hs:'#1e5eff',arm:'#1e5eff'},
  side:{deck:'#f2f4f7',hood:'#1e5eff',hull:'#1e5eff',trim:'#15171b',seatA:'#f2f4f7',seatB:'#1e5eff',seatC:'#15171b',stripe:'#1e5eff'},face:{skin:'#f0c4a0',hair:'#b5562a',style:'pony',vest:'#1e5eff'}},
 {id:'solar',name:'SOLAR',colors:'Amarilla',pilot:'Javi Rubio',bio:'Turbo largo y mucha cabeza.',ui:'#ffd21a',st:{vel:3,ace:3,giro:3,turbo:5},
  sk:{hull:'#ffd21a',hullD:'#c08f00',acc:'#2a2c33',seat:'#2a2c33',vest:'#2a2c33',helmet:'#ffd21a',hs:'#2a2c33',arm:'#2a2c33'},
  side:{deck:'#ffd21a',hood:'#ffd21a',hull:'#2a2c33',trim:'#15171b',seatA:'#2a2c33',seatB:'#3a3d45',seatC:'#ffd21a',stripe:'#2a2c33'},face:{skin:'#efbf98',hair:'#f0d070',style:'curly',vest:'#2a2c33'}},
 {id:'veneno',name:'VENENO',colors:'Verde y negra',pilot:'Nuria Gil',bio:'Ligera y nerviosa. Sale disparada.',ui:'#62d41c',st:{vel:4,ace:4,giro:3,turbo:2},
  sk:{hull:'#5fd31a',hullD:'#2b7d00',acc:'#111317',seat:'#111317',vest:'#111317',helmet:'#5fd31a',hs:'#111317',arm:'#111317'},
  side:{deck:'#1d1f24',hood:'#62d41c',hull:'#1a1c21',trim:'#0e0f12',seatA:'#2a2d33',seatB:'#8d9199',seatC:'#62d41c',stripe:'#62d41c'},face:{skin:'#d9a07a',hair:'#1b1b1b',style:'bob',vest:'#5fd31a'}},
 {id:'sombra',name:'SOMBRA',colors:'Negra entera',pilot:'Marcos León',bio:'Silencioso y frío. No falla una curva.',ui:'#aab3c0',st:{vel:4,ace:3,giro:3,turbo:3},
  sk:{hull:'#26292f',hullD:'#0c0d10',acc:'#5a5f6a',seat:'#4a4e57',vest:'#111317',helmet:'#26292f',hs:'#8d9199',arm:'#111317'},
  side:{deck:'#22252b',hood:'#191b20',hull:'#131519',trim:'#0a0b0d',seatA:'#4a4e57',seatB:'#2a2d33',seatC:'#8d9199',stripe:'#4a4e57'},face:{skin:'#d8a27c',hair:'#2a1a12',style:'short',beard:1,vest:'#26292f'}}
];
'''
s=s[:a]+MOTOS+s[b:]
# 2) replace old side drawing with profile drawing
a=s.index('function drawJetSide(g,s){');b=s.index('function policePath(g,k){')
PROF='''function mixc(h,o,t){const p=x=>[parseInt(x.slice(1,3),16),parseInt(x.slice(3,5),16),parseInt(x.slice(5,7),16)];const A=p(h),B=p(o);return'rgb('+A.map((v,i)=>Math.round(v+(B[i]-v)*t)).join(',')+')';}
function drawJetProfile(g,s){
 g.fillStyle='rgba(0,30,60,.28)';g.beginPath();g.ellipse(152,101,142,6,0,0,TAU);g.fill();
 const hullP=()=>{g.beginPath();g.moveTo(8,66);g.lineTo(236,60);g.quadraticCurveTo(280,55,303,49);g.lineTo(299,57);g.quadraticCurveTo(272,88,216,96);g.lineTo(34,99);g.quadraticCurveTo(12,99,8,90);g.closePath();};
 hullP();let gg=g.createLinearGradient(0,56,0,100);gg.addColorStop(0,mixc(s.hull,'#ffffff',.25));gg.addColorStop(.4,s.hull);gg.addColorStop(1,mixc(s.hull,'#000000',.35));g.fillStyle=gg;g.fill();
 g.save();hullP();g.clip();
  g.fillStyle='rgba(0,0,0,.3)';g.beginPath();g.moveTo(0,91);g.lineTo(214,89);g.quadraticCurveTo(268,82,304,58);g.lineTo(312,112);g.lineTo(0,112);g.closePath();g.fill();
  g.fillStyle=s.stripe;g.globalAlpha=.92;for(const[x,w]of[[150,16],[172,7]]){g.beginPath();g.moveTo(x+18,60);g.lineTo(x+18+w,60);g.lineTo(x+w,96);g.lineTo(x,96);g.closePath();g.fill();}g.globalAlpha=1;
  g.fillStyle='rgba(255,255,255,.35)';g.fillRect(0,67,240,1.2);
 g.restore();
 g.fillStyle=s.trim;g.beginPath();g.moveTo(42,91);g.lineTo(98,89);g.lineTo(104,95);g.lineTo(46,97);g.closePath();g.fill();
 g.fillStyle='#3a3d45';g.fillRect(2,72,9,4);g.fillRect(4,79,6,3);g.fillRect(4,85,6,3);
 const deckP=()=>{g.beginPath();g.moveTo(8,66);g.lineTo(8,56);g.lineTo(74,54);g.lineTo(84,47);g.lineTo(158,43);g.lineTo(178,30);g.lineTo(206,22);g.quadraticCurveTo(258,27,303,49);g.lineTo(236,60);g.closePath();};
 deckP();gg=g.createLinearGradient(0,22,0,66);gg.addColorStop(0,mixc(s.deck,'#ffffff',.3));gg.addColorStop(.5,s.deck);gg.addColorStop(1,mixc(s.deck,'#000000',.25));g.fillStyle=gg;g.fill();
 g.save();deckP();g.clip();
  g.fillStyle=s.stripe;g.globalAlpha=.85;g.beginPath();g.moveTo(96,60);g.lineTo(168,47);g.lineTo(176,49);g.lineTo(104,62);g.closePath();g.fill();g.globalAlpha=1;
  g.fillStyle='rgba(0,0,0,.18)';g.beginPath();g.moveTo(8,62);g.lineTo(236,57);g.lineTo(236,61);g.lineTo(8,67);g.closePath();g.fill();
 g.restore();
 g.fillStyle='#2b2e35';g.beginPath();g.moveTo(10,56);g.lineTo(72,54);g.lineTo(76,52);g.lineTo(12,54);g.closePath();g.fill();
 const hoodP=()=>{g.beginPath();g.moveTo(168,45);g.lineTo(180,30);g.lineTo(206,22);g.quadraticCurveTo(258,27,303,49);g.lineTo(262,55);g.quadraticCurveTo(222,51,196,50);g.closePath();};
 hoodP();gg=g.createLinearGradient(0,22,0,56);gg.addColorStop(0,mixc(s.hood,'#ffffff',.35));gg.addColorStop(.55,s.hood);gg.addColorStop(1,mixc(s.hood,'#000000',.25));g.fillStyle=gg;g.fill();
 g.save();hoodP();g.clip();g.strokeStyle='rgba(0,0,0,.35)';g.lineWidth=1.4;for(const o of[0,7]){g.beginPath();g.moveTo(212+o,31);g.lineTo(266+o,46);g.stroke();}g.strokeStyle='rgba(255,255,255,.45)';g.lineWidth=1;g.beginPath();g.moveTo(206,23);g.quadraticCurveTo(258,28,300,49);g.stroke();g.restore();
 g.fillStyle=s.trim;g.beginPath();g.moveTo(284,47);g.lineTo(303,49);g.lineTo(299,58);g.lineTo(282,56);g.closePath();g.fill();
 g.fillStyle='rgba(20,22,26,.85)';g.beginPath();g.moveTo(246,50);g.lineTo(282,51);g.lineTo(280,54);g.lineTo(250,53);g.closePath();g.fill();
 g.fillStyle='#16181d';g.beginPath();g.moveTo(181,30);g.lineTo(205,23);g.lineTo(212,30);g.lineTo(189,37);g.closePath();g.fill();g.fillStyle='rgba(120,200,255,.35)';g.beginPath();g.moveTo(185,31);g.lineTo(203,25);g.lineTo(206,27);g.lineTo(189,33);g.closePath();g.fill();
 g.fillStyle=s.trim;g.beginPath();g.moveTo(214,26);g.lineTo(228,17);g.lineTo(233,20);g.lineTo(219,29);g.closePath();g.fill();
 const seatP=()=>{g.beginPath();g.moveTo(84,47);g.quadraticCurveTo(84,33,98,32);g.lineTo(124,31);g.quadraticCurveTo(131,31,135,36);g.lineTo(158,37);g.quadraticCurveTo(168,37,172,33);g.lineTo(178,30);g.lineTo(167,45);g.lineTo(158,43);g.closePath();};
 seatP();gg=g.createLinearGradient(0,31,0,47);gg.addColorStop(0,mixc(s.seatA,'#ffffff',.25));gg.addColorStop(1,mixc(s.seatA,'#000000',.2));g.fillStyle=gg;g.fill();
 g.save();seatP();g.clip();g.fillStyle=s.seatB;g.beginPath();g.moveTo(84,48);g.quadraticCurveTo(84,33,98,32);g.lineTo(124,31);g.quadraticCurveTo(131,31,135,36);g.lineTo(128,48);g.closePath();g.fill();
  g.fillStyle=s.seatC;g.fillRect(80,42,100,3);g.fillStyle='rgba(255,255,255,.25)';g.fillRect(90,33,32,1.4);g.fillRect(138,37,20,1.2);g.restore();
 g.strokeStyle=s.trim;g.lineWidth=3;g.lineCap='round';g.beginPath();g.moveTo(85,46);g.quadraticCurveTo(72,40,82,33);g.stroke();
 g.strokeStyle='#1a1c21';g.lineWidth=5;g.beginPath();g.moveTo(198,25);g.lineTo(194,11);g.stroke();g.lineWidth=4;g.beginPath();g.moveTo(184,8);g.lineTo(207,12);g.stroke();g.lineWidth=1.5;g.beginPath();g.moveTo(203,13);g.lineTo(212,17);g.stroke();
 g.fillStyle='rgba(255,255,255,.85)';for(let i=0;i<16;i++){const x=20+i*15+Math.sin(i*2.3)*4;g.beginPath();g.ellipse(x,98+Math.sin(i)*1.2,4+Math.sin(i*1.7)*2,1.4,0,0,TAU);g.fill();}
}
'''
s=s[:a]+PROF+s[b:]
R=[
(".gmoto{height:118px;display:grid;place-items:center;border-radius:14px;background:radial-gradient(ellipse at 50% 55%,#2bb6d3,#0f6db8 70%)}\n.gmoto canvas{width:120px;height:118px;animation:bob 2.4s ease-in-out infinite}",
 ".gmoto{height:128px;display:grid;place-items:center;border-radius:14px;overflow:hidden;background:linear-gradient(#8fd8f6,#d6f2fb 52%,#3cc3dd 53%,#1488c8 78%,#0d63ad)}\n.gmoto canvas{width:min(100%,290px);height:auto;aspect-ratio:580/240;animation:bob 2.4s ease-in-out infinite}"),
("@keyframes bob{50%{transform:translateY(-4px) rotate(2deg)}}","@keyframes bob{50%{transform:translateY(-3px) rotate(-1deg)}}"),
('<canvas id="gMoto" width="240" height="236"></canvas>','<canvas id="gMoto" width="580" height="240"></canvas>'),
("function renderGarage(){const m=MOTOS[G.moto];$('#gCard').style.setProperty('--sc',m.sk.hull==='#25272e'?'#ffd21a':m.sk.hull==='#f5f6f8'?'#e3202b':m.sk.hull);",
 "function renderGarage(){const m=MOTOS[G.moto];$('#gCard').style.setProperty('--sc',m.ui);"),
(" const gc=$('#gMoto'),g=gc.getContext('2d');g.setTransform(2,0,0,2,0,0);g.clearRect(0,0,120,118);g.save();g.translate(64,62);g.rotate(.5);g.scale(1.35,1.35);\n g.save();g.translate(4,6);g.globalAlpha=.35;hullPath(g);g.fillStyle='#00142e';g.fill();g.restore();drawJet(g,m.sk);g.restore();",
 " const gc=$('#gMoto'),g=gc.getContext('2d');g.setTransform(2,0,0,2,0,0);g.clearRect(0,0,290,120);g.save();g.translate(6,4);g.scale(.91,.91);drawJetProfile(g,m.side);g.restore();"),
(" g.save();g.translate(96,184);g.scale(.8,.8);drawJetSide(g,MOTOS[G.moto].sk);g.restore();",
 " g.save();g.translate(40,152);g.scale(.42,.42);drawJetProfile(g,MOTOS[G.moto].side);g.restore();"),
(" if(Z.riv){const pool=MOTOS.filter((_,i)=>i!==G.moto);if(Z.boss)pool[pool.length-1]=SHARK;",
 " if(Z.riv){const rr=rng(Zn.seed+3);let pool=MOTOS.filter((_,i)=>i!==G.moto).map(m=>[rr(),m]).sort((a,b)=>a[0]-b[0]).map(x=>x[1]).slice(0,Z.riv);if(Z.boss)pool[Z.riv-1]=SHARK;"),
("const pool=MOTOS.slice();G.P=craft(pool[0],WG*.5,0,true);","const pool=MOTOS.slice(0,6);G.P=craft(pool[0],WG*.5,0,true);"),
("li.style.setProperty('--sc',m.sk.hull==='#f5f6f8'?'#e3202b':m.sk.hull);","li.style.setProperty('--sc',m.ui);"),
]
for x,y in R:
    assert s.count(x)==1,x[:90]
    s=s.replace(x,y)
open(p,'w',encoding='utf-8').write(s)
print('ok')
