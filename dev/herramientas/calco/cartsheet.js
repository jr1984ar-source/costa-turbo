const fs=require('fs');const {chromium}=require('playwright');const {tracedHelmet}=require('./tracedHelmet.js');
const K=[['sm5',{brand:'oakley',strap:'#1d2027',lens:'prizm'}],['arai_star',{brand:'100',strap:'#1e3fae',lens:'gold'}]];
const M=[['ink','1 · Dibujo con línea'],['toon','2 · Dibujo sin línea'],['styl','3 · Pintado']];
let rows='';
for(const [k,gg] of K){const J=JSON.parse(fs.readFileSync(k+'.json','utf8'));const T=tracedHelmet(J,gg,'t'+k);const gog=T.body.split('<!--GOG-->')[1]||'';
 for(const [m,n] of M){const src='data:image/png;base64,'+fs.readFileSync('cart/'+k+'_'+m+'.png').toString('base64');
  rows+=`<div class="c"><svg viewBox="-20 -20 ${J.w+40} ${J.h+40}"><defs>${T.defs}</defs><image href="${src}" x="0" y="0" width="${J.w}" height="${J.h}"/>${gog}</svg><p>${n}</p></div>`;}}
fs.writeFileSync('cartsheet.html',`<!doctype html><html><head><meta charset=utf8><style>body{margin:0;font-family:Arial}.w{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;padding:12px;width:1000px;background:#0a1630}.c{background:radial-gradient(ellipse at 50% 35%,#ffffff,#d6dce4 80%);border-radius:14px;padding:6px}.c svg{width:100%;height:250px;display:block}.c p{margin:2px 6px 4px;color:#15171c;font-weight:900;font-size:15px}</style></head><body><div class="w">${rows}</div></body></html>`);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:1024,height:700}})).newPage();await p.goto('file://'+process.cwd()+'/cartsheet.html');await p.waitForTimeout(600);await p.screenshot({path:'cartsheet.png',fullPage:true});await b.close();})();
