const fs=require('fs');const {chromium}=require('playwright');
const src=['../pilot_svg.js','tracedHelmet.js','pilotT.js'].map(f=>fs.readFileSync(f,'utf8').replace("if (typeof module","if (false&&typeof module")).join('\n');
const cat=JSON.parse(fs.readFileSync('catalog.json','utf8'));const by=n=>cat.find(c=>c.n===n);
const V=[
 [by('Alpinestars S-M5 Rojo'),{vest:{c:'#16181d',c2:'#e3202b',pat:'vault',name:'RX Vault'},suit:{c:'#1d2027',a:'#e3202b'},glove:'#1d2027',gloveA:'#e3202b'}],
 [by('Arai MX-V Estrellas'),{vest:{c:'#1e5eff',c2:'#ffffff',pat:'race',name:'Matrix Race'},suit:{c:'#1e5eff',a:'#0b2c8f'},glove:'#f4f6f9',gloveA:'#1e5eff'}],
 [by('Alpinestars S-M7 Negro'),{vest:{c:'#25282e',c2:'#ffc93c',pat:'carbon',name:'F-86 Carbon'},suit:{c:'#2a2d33',a:'#ffc93c',pat:'carbon'},glove:'#16181d',gloveA:'#ffc93c'}],
];
const data=V.map(([c,o])=>Object.assign({},o,{gog:c.g,J:c.J}));
const html=`<!doctype html><html><head><meta charset=utf8><style>body{margin:0;background:#0a1630}.w{display:flex;width:1200px;height:760px;background:radial-gradient(ellipse at 50% 0%,#245a94 0%,#0f2d55 45%,#0a1630 80%)}.c{flex:1;position:relative}.c svg{position:absolute;left:50%;top:20px;width:320px;height:725px;transform:translateX(-50%)}.pod{position:absolute;left:50%;bottom:22px;width:300px;height:56px;transform:translateX(-50%);border-radius:50%;background:radial-gradient(ellipse at 50% 40%,#3a6aa0,#14315a 70%);box-shadow:0 0 0 3px rgba(51,214,255,.55),0 0 30px rgba(51,214,255,.35)}</style></head><body><div class="w" id="w"></div><script>${src}
const D=${JSON.stringify(data)};document.getElementById('w').innerHTML=D.map((o,i)=>'<div class="c"><div class="pod"></div>'+pilotTSVG(o,o.J,'p'+i)+'</div>').join('');</script></body></html>`;
fs.writeFileSync('boceto22.html',html);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:1200,height:760}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('file://'+process.cwd()+'/boceto22.html');await p.waitForTimeout(500);await p.screenshot({path:'boceto22.png'});console.log(JSON.stringify(errs));await b.close();})();
