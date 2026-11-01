const fs=require('fs');const {chromium}=require('playwright');
const src=fs.readFileSync('pilot34.js','utf8')+'\n'+fs.readFileSync('helmetL.js','utf8');
const C=[
 ['Arai MX-V Blanco · 8.000 PTA',{helm:{st:'mx',brand:'Arai',c:'#f4f6f9',c2:'#c9ced6'},gog:{brand:'oakley',strap:'#1d2027',lens:'smoke'}}],
 ['Arai MX-V Estrellas · 16.000 PTA',{helm:{st:'mx',brand:'Arai',c:'#f4f6f9',c2:'#e3202b',c3:'#e6f01a',pat:'stars',chin:'#e6f01a'},gog:{brand:'100',strap:'#1e3fae',lens:'gold'}}],
 ['Arai MX-V Rana · 21.000 PTA',{helm:{st:'mx',brand:'Arai',c:'#1e5eff',c2:'#ff3f8e',c3:'#7be35a',pat:'frog',chin:'#3a2bd0'},gog:{brand:'oakley',strap:'#ff3f8e',lens:'jade'}}],
 ['Arai MX-V Bloques · 28.000 PTA',{helm:{st:'mx',brand:'Arai',c:'#1e5eff',c2:'#e3202b',c3:'#e6f01a',pat:'blocks',chin:'#e6f01a',badge:'#e6f01a'},gog:{brand:'alpinestars',strap:'#1d2027',lens:'red'}}],
];
const html=`<!doctype html><html><head><meta charset=utf8><style>body{margin:0;background:#0a1630;font-family:Arial}.w{display:grid;grid-template-columns:1fr 1fr;gap:14px;padding:16px;width:780px;box-sizing:border-box;background:radial-gradient(ellipse at 50% 0%,#245a94 0%,#0f2d55 45%,#0a1630 80%)}.c{background:radial-gradient(ellipse at 50% 35%,#f4f6f9,#cfd6de 75%);border-radius:16px;padding:6px}.c svg{width:100%;height:auto;display:block}.c p{margin:2px 8px 6px;color:#15171c;font-weight:800;font-size:14px}</style></head><body><div class="w" id="w"></div><script>${src}
const C=${JSON.stringify(C)};document.getElementById('w').innerHTML=C.map(([t,o],i)=>{const h=helmetL(o,'h'+i);return '<div class="c"><svg viewBox="40 0 220 175">'+h.defs+'<ellipse cx="160" cy="168" rx="80" ry="6" fill="rgba(0,0,0,.18)"/>'+h.body+'</svg><p>'+t+'</p></div>';}).join('');</script></body></html>`;
fs.writeFileSync('boceto15.html',html);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:780,height:600}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('file://'+process.cwd()+'/boceto15.html');await p.waitForTimeout(400);await p.screenshot({path:'boceto15.png',fullPage:true});console.log(JSON.stringify(errs));await b.close();})();
