const fs=require('fs');const {chromium}=require('playwright');const {tracedHelmet}=require('./tracedHelmet.js');const {recolor}=require('./recolor.js');
const ld=k=>JSON.parse(fs.readFileSync(k+'.json','utf8'));const sm5=ld('sm5');
const C=[
 ['Alpinestars S-M5 Rojo',3000,sm5,{brand:'oakley',strap:'#1d2027',lens:'prizm'}],
 ['Alpinestars S-M5 Azul',4500,recolor(sm5,{h:222,k:.6,s:1.05,l:1.05}),{brand:'100',strap:'#ffffff',lens:'blue',frame:'#f4f6f9'}],
 ['Alpinestars S-M5 Amarillo',5500,recolor(sm5,{h:48,k:.5,s:1.1,l:1.25,lp:.08}),{brand:'oakley',strap:'#1d2027',lens:'red'}],
 ['Alpinestars S-M5 Morado',6500,recolor(sm5,{h:272,k:.6,l:1.05}),{brand:'alpinestars',strap:'#ff3f8e',lens:'prizm'}],
 ['Alpinestars S-M5 Verde Flúor',7500,recolor(sm5,{h:82,k:.4,s:1.1,l:1.2,lp:.06}),{brand:'100',strap:'#1d2027',lens:'jade'}],
 ['Alpinestars S-M5 Negro',8500,recolor(sm5,{gray:.42,acc:22}),{brand:'oakley',strap:'#ff7a1a',lens:'gold'}],
 ['Alpinestars S-M7 Negro',9500,ld('alp_black'),{brand:'100',strap:'#f4f6f9',lens:'smoke'}],
 ['Alpinestars Supertech M10 Rojo',14000,ld('alp_red'),{brand:'alpinestars',strap:'#1d2027',lens:'gold'}],
 ['Alpinestars Supertech Flúor',16000,ld('alp_monster'),{brand:'100',strap:'#7be35a',lens:'silver'}],
 ['Arai MX-V Blanco',8000,ld('arai_white'),{brand:'oakley',strap:'#1d2027',lens:'smoke'}],
 ['Arai MX-V Estrellas',16000,ld('arai_star'),{brand:'100',strap:'#1e3fae',lens:'gold'}],
 ['Arai MX-V Rana',21000,ld('arai_frog'),{brand:'oakley',strap:'#ff3f8e',lens:'jade'}],
 ['Arai MX-V Bloques',28000,ld('arai_blocks'),{brand:'alpinestars',strap:'#1d2027',lens:'red'}]];
fs.writeFileSync('catalog.json',JSON.stringify(C.map(([n,p,J,g])=>({n,p,J,g}))));
const cards=C.map(([n,p,J,gg],i)=>{const H=tracedHelmet(J,gg,'t'+i);
 return `<div class="c"><svg viewBox="-20 -20 ${H.w+40} ${H.h+40}"><defs>${H.defs}</defs><ellipse cx="${H.w*.55}" cy="${H.h+6}" rx="${H.w*.38}" ry="12" fill="rgba(0,0,0,.2)"/>${H.body}</svg><p>${n} · ${p.toLocaleString('de-DE')} PTA</p></div>`;}).join('');
fs.writeFileSync('sheet21.html',`<!doctype html><html><head><meta charset=utf8><style>body{margin:0;font-family:Arial}.w{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:14px;width:1000px;background:radial-gradient(ellipse at 50% 0%,#245a94 0%,#0f2d55 45%,#0a1630 80%)}.c{background:radial-gradient(ellipse at 50% 35%,#ffffff,#d6dce4 80%);border-radius:16px;padding:8px}.c svg{width:100%;height:240px;display:block}.c p{margin:4px 6px;color:#15171c;font-weight:800;font-size:14px}</style></head><body><div class="w">${cards}</div></body></html>`);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:1028,height:800}})).newPage();await p.goto('file://'+process.cwd()+'/sheet21.html');await p.waitForTimeout(500);await p.screenshot({path:'sheet21.png',fullPage:true});await b.close();})();
