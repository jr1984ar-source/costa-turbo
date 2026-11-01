const fs=require('fs');const {chromium}=require('playwright');
const src=fs.readFileSync('pilot34.js','utf8')+'\n'+fs.readFileSync('helmetL.js','utf8');
const C=[
 ['Alpinestars S-M3 Radium · 3.000 PTA',{helm:{st:'mx',c:'#c8141c',c2:'#ff5a2a'},gog:{brand:'oakley',strap:'#1d2027',lens:'prizm'}}],
 ['Alpinestars S-M3 Jettson · 4.500 PTA',{helm:{st:'mx',c:'#a3abb8',c2:'#7b5cff',peak:'#7b5cff',chin:'#7b5cff',pat:'jettson'},gog:{brand:'100',strap:'#7b5cff',lens:'silver'}}],
 ['Alpinestars S-M3 Azul · 6.000 PTA',{helm:{st:'mx',c:'#1e4fd8',c2:'#ffffff',peak:'#1e4fd8',pat:'yam'},gog:{brand:'alpinestars',strap:'#ffffff',lens:'blue',frame:'#f4f6f9'}}],
 ['Alpinestars S-M3 Force · 7.500 PTA',{helm:{st:'mx',c:'#1b1d24',c2:'#ff3f8e',peak:'#1b1d24',chin:'#1b1d24',pat:'force'},gog:{brand:'oakley',strap:'#ff7a1a',lens:'prizm'}}],
 ['Alpinestars S-M7 Negro · 9.500 PTA',{helm:{st:'mx',c:'#1b1d24',c2:'#f4f6f9',peak:'#1b1d24',chin:'#1b1d24',pat:'bigstar'},gog:{brand:'100',strap:'#f4f6f9',lens:'smoke'}}],
 ['Alpinestars S-M7 Blaster · 12.000 PTA',{helm:{st:'mx',c:'#f4f6f9',c2:'#5b2bb8',c3:'#c6ff1a',peak:'#f4f6f9',chin:'#5b2bb8',pat:'blaster'},gog:{brand:'oakley',strap:'#ff3f8e',lens:'red'}}],
 ['Alpinestars Supertech Flúor · 14.000 PTA',{helm:{st:'mx',c:'#ff6a1a',c2:'#ff3f8e',peak:'#ff6a1a',chin:'#1b1d24',pat:'fluor'},gog:{brand:'100',strap:'#7be35a',lens:'jade'}}],
 ['Alpinestars S-M8 Flame · 16.000 PTA',{helm:{st:'mx',c:'#ffd21a',c2:'#e3202b',pat:'flame'},gog:{brand:'100',strap:'#e3202b',lens:'red'}}],
];
const html=`<!doctype html><html><head><meta charset=utf8><style>body{margin:0;background:#0a1630;font-family:Arial}.w{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:14px;width:780px;box-sizing:border-box;background:radial-gradient(ellipse at 50% 0%,#245a94 0%,#0f2d55 45%,#0a1630 80%)}.c{background:radial-gradient(ellipse at 50% 35%,#f4f6f9,#cfd6de 75%);border-radius:16px;padding:6px}.c svg{width:100%;height:auto;display:block}.c p{margin:2px 8px 6px;color:#15171c;font-weight:800;font-size:13px}</style></head><body><div class="w" id="w"></div><script>${src}
const C=${JSON.stringify(C)};document.getElementById('w').innerHTML=C.map(([t,o],i)=>{const h=helmetL(o,'h'+i);return '<div class="c"><svg viewBox="40 0 220 175">'+h.defs+'<ellipse cx="160" cy="168" rx="80" ry="6" fill="rgba(0,0,0,.18)"/>'+h.body+'</svg><p>'+t+'</p></div>';}).join('');</script></body></html>`;
fs.writeFileSync('boceto16.html',html);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:780,height:600}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('file://'+process.cwd()+'/boceto16.html');await p.waitForTimeout(400);await p.screenshot({path:'boceto16.png',fullPage:true});console.log(JSON.stringify(errs));await b.close();})();
