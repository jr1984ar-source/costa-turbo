const fs=require('fs');const {chromium}=require('playwright');
const src=fs.readFileSync('jetski3q.js','utf8');
const V=[{hull:'#e6f01a',deck:'#26292f',acc:'#e6f01a',seatA:'#1d2027',seatB:'#e6f01a',name:'BRAVA'},
 {hull:'#d81e28',deck:'#f2f4f7',acc:'#d81e28',seatA:'#f2f4f7',seatB:'#2a2d33',name:'INFERNO'},
 {hull:'#1b1d22',deck:'#2a2d33',acc:'#6f7680',seatA:'#3a3f48',seatB:'#8b929c',name:'SOMBRA'}];
const html=`<!doctype html><html><head><meta charset=utf8><style>body{margin:0}.w{display:grid;grid-template-columns:1fr;gap:10px;padding:14px;width:760px;background:#e9edf2}.w svg{width:100%;height:auto;display:block;background:radial-gradient(ellipse at 50% 40%,#ffffff,#dfe5ec 75%);border-radius:14px}</style></head><body><div class="w" id="w"></div><script>${src}
document.getElementById('w').innerHTML=${JSON.stringify(V)}.map((o,i)=>jetSki3q(o,'k'+i)).join('');</script></body></html>`;
fs.writeFileSync('boceto12.html',html);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:788,height:600}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('file://'+process.cwd()+'/boceto12.html');await p.waitForTimeout(400);await p.screenshot({path:'boceto12.png',fullPage:true});console.log(JSON.stringify(errs));await b.close();})();
