const fs=require('fs');const {chromium}=require('playwright');
const src=fs.readFileSync('pilot34.js','utf8')+'\n'+fs.readFileSync('helmetL.js','utf8');
const C=[
 ['Alpinestars S-M5 · rojo como la foto · Oakley goma negra, Prizm',{helm:{st:'mx',c:'#c8141c',c2:'#ff5a2a'},gog:{brand:'oakley',strap:'#1d2027',lens:'prizm'}}],
 ['Alpinestars S-M8 Flame · 100% goma roja, iridium rojo',{helm:{st:'mx',c:'#ffd21a',c2:'#e3202b',pat:'flame'},gog:{brand:'100',strap:'#e3202b',lens:'red'}}],
 ['Alpinestars S-M5 Rover · Alpinestars goma blanca, iridium azul',{helm:{st:'mx',c:'#f4f6f9',c2:'#1e5eff',pat:'split'},gog:{brand:'alpinestars',strap:'#ffffff',lens:'blue',frame:'#f4f6f9'}}],
 ['Alpinestars Supertech M10 · Oakley goma amarilla, oro',{helm:{st:'mx',c:'#1d2027',c2:'#ffd21a',pat:'star'},gog:{brand:'oakley',strap:'#ffd21a',lens:'gold'}}],
 ['Arai RX-7V Racing',{helm:{st:'full',c:'#1e5eff',c2:'#ffd21a',pat:'flame'}}],
 ['Arai Edición Leyenda Cromo',{helm:{st:'full',c:'#cfd8e3',c2:'#7a5cff',pat:'chrome'}}],
];
const html=`<!doctype html><html><head><meta charset=utf8><style>body{margin:0;background:#0a1630;font-family:Arial}.w{display:grid;grid-template-columns:1fr 1fr;gap:14px;padding:16px;width:780px;box-sizing:border-box;background:radial-gradient(ellipse at 50% 0%,#245a94 0%,#0f2d55 45%,#0a1630 80%)}.c{background:radial-gradient(ellipse at 50% 35%,#f4f6f9,#cfd6de 75%);border-radius:16px;padding:6px}.c svg{width:100%;height:auto;display:block}.c p{margin:2px 8px 6px;color:#15171c;font-weight:800;font-size:13px}</style></head><body><div class="w" id="w"></div><script>${src}
const C=${JSON.stringify(C)};document.getElementById('w').innerHTML=C.map(([t,o],i)=>{const h=helmetL(o,'h'+i);return '<div class="c"><svg viewBox="40 0 220 175">'+h.defs+'<ellipse cx="160" cy="168" rx="80" ry="6" fill="rgba(0,0,0,.18)"/>'+h.body+'</svg><p>'+t+'</p></div>';}).join('');</script></body></html>`;
fs.writeFileSync('boceto9.html',html);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:780,height:600}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('file://'+process.cwd()+'/boceto9.html');await p.waitForTimeout(400);await p.screenshot({path:'boceto9.png',fullPage:true});console.log(JSON.stringify(errs));await b.close();})();
