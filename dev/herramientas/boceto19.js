const fs=require('fs');const {chromium}=require('playwright');
const src=fs.readFileSync('jetski3q.js','utf8').replace("if (typeof module","if (false&&typeof module");
// colores de cada moto del juego: casco (hull), cubierta (deck), detalle (acc), asiento
const V=[
 ['BRAVA',{hull:'#e3202b',deck:'#f2f3f5',acc:'#1b1d22',seatA:'#1d1f24',seatB:'#e3202b'}],
 ['INFERNO',{hull:'#cf1820',deck:'#de1a24',acc:'#1b1d22',seatA:'#1d1f24',seatB:'#f2f3f5'}],
 ['AVISPA',{hull:'#ffd21a',deck:'#2c2f36',acc:'#ffd21a',seatA:'#121317',seatB:'#ffd21a'}],
 ['OCÉANO',{hull:'#1746c4',deck:'#1e5eff',acc:'#ffffff',seatA:'#15171c',seatB:'#ffffff'}],
 ['MAREA',{hull:'#1e5eff',deck:'#f2f4f7',acc:'#1e5eff',seatA:'#1d1f24',seatB:'#1e5eff'}],
 ['SOLAR',{hull:'#2a2c33',deck:'#ffd21a',acc:'#2a2c33',seatA:'#2a2c33',seatB:'#ffd21a'}],
 ['VENENO',{hull:'#1a1c21',deck:'#1d1f24',acc:'#62d41c',seatA:'#111317',seatB:'#62d41c'}],
 ['SOMBRA',{hull:'#131519',deck:'#22252b',acc:'#4a4e57',seatA:'#3a3f48',seatB:'#6f7680'}],
 ['TIBURÓN',{hull:'#4a5d72',deck:'#a9bccf',acc:'#e9eef4',seatA:'#1b2028',seatB:'#8fa3b8'}],
];
const html=`<!doctype html><html><head><meta charset=utf8><style>body{margin:0;font-family:Arial}.w{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;padding:12px;width:1200px;box-sizing:border-box;background:#0a1630}.c{border-radius:14px;overflow:hidden;background:linear-gradient(180deg,#9fdcf5 0%,#d8f2fb 46%,#3cc3dd 47%,#1488c8 78%,#0d63ad 100%)}.c svg{width:100%;height:auto;display:block}.c p{margin:0;padding:6px 10px;background:#0f2448;color:#ffc93c;font-weight:900;font-size:15px;letter-spacing:.05em}</style></head><body><div class="w" id="w"></div><script>${src}
const V=${JSON.stringify(V)};document.getElementById('w').innerHTML=V.map(([n,o],i)=>'<div class="c">'+jetSki3q(Object.assign({name:n},o),'m'+i)+'<p>'+n+'</p></div>').join('');</script></body></html>`;
fs.writeFileSync('boceto19.html',html);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:1200,height:700}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('file://'+process.cwd()+'/boceto19.html');await p.waitForTimeout(400);await p.screenshot({path:'boceto19.png',fullPage:true});console.log(JSON.stringify(errs));await b.close();})();
