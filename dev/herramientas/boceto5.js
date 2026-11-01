const {pilotSideSVG}=require('./pilot_side.js');const fs=require('fs');const {chromium}=require('playwright');
const base={vest:{c:'#16181d',c2:'#e3202b',pat:'vault'},suit:{c:'#b6f01e',a:'#1d2027'}};
const C=[
 ['Oakley Airbrake MX · goma roja · lente Prizm',{helm:{st:'mx',c:'#ffd21a',c2:'#e3202b',pat:'flame'},gog:{brand:'oakley',strap:'#e3202b',lens:'prizm'}}],
 ['100% Armega · goma blanca · iridium azul',{helm:{st:'mx',c:'#f4f6f9',c2:'#1e5eff',pat:'split'},gog:{brand:'100',strap:'#ffffff',lens:'blue',frame:'#f4f6f9'}}],
 ['Alpinestars Supertech · goma negra · oro',{helm:{st:'mx',c:'#e3202b',c2:'#ffffff',pat:'star'},gog:{brand:'alpinestars',strap:'#1d2027',lens:'gold'}}],
 ['100% Strata 2 · goma amarilla · jade',{helm:{st:'mx',c:'#1d2027',c2:'#e3202b',pat:'twin'},gog:{brand:'100',strap:'#ffd21a',lens:'jade'}}],
];
const html=`<!doctype html><html><head><meta charset=utf8><style>body{margin:0;background:#0a1630;font-family:Arial}.w{display:grid;grid-template-columns:1fr 1fr;gap:14px;padding:16px;width:780px;box-sizing:border-box;background:radial-gradient(ellipse at 50% 0%,#245a94 0%,#0f2d55 45%,#0a1630 80%)}.c{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.12);border-radius:16px;padding:8px}.c svg{width:100%;height:auto;display:block}.c p{margin:4px 6px 6px;color:#ffc93c;font-weight:800;font-size:15px}</style></head><body><div class="w">${C.map(([t,o],i)=>`<div class="c">${pilotSideSVG(Object.assign({},base,o),'z'+i).replace('viewBox="0 0 300 640"','viewBox="92 10 166 132"')}<p>${t}</p></div>`).join('')}</div></body></html>`;
fs.writeFileSync('boceto5.html',html);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:780,height:600}})).newPage();await p.goto('file://'+process.cwd()+'/boceto5.html');await p.waitForTimeout(300);await p.screenshot({path:'boceto5.png',fullPage:true});await b.close();})();
