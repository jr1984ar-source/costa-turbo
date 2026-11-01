const fs=require('fs');const {chromium}=require('playwright');
const M=fs.readFileSync('ilus/ilus_map.json','utf8');const src=fs.readFileSync('skiart2.js','utf8');
const P=[['Original (tu dibujo)',{hull:'#d42a2a',deck:'#d42a2a',hood:'#2b2d33',stripe:'#2b2d33',seat:'#2b2d33'}],
 ['Roja y blanca',{hull:'#e3202b',deck:'#f4f5f7',hood:'#e3202b',stripe:'#e3202b',seat:'#16181d'}],
 ['Negra y amarilla',{hull:'#ffd21a',deck:'#2c2f36',hood:'#ffd21a',stripe:'#ffd21a',seat:'#ffd21a'}],
 ['Azul y blanca',{hull:'#1e5eff',deck:'#f4f5f7',hood:'#1e5eff',stripe:'#1e5eff',seat:'#f4f5f7'}],
 ['Verde y negra',{hull:'#1f9e52',deck:'#62d41c',hood:'#16181d',stripe:'#f4f5f7',seat:'#16181d'}],
 ['Rosa y morada',{hull:'#7b3fe4',deck:'#ff3f8e',hood:'#ff3f8e',stripe:'#f4f5f7',seat:'#7b3fe4'}]];
const html=`<!doctype html><html><head><meta charset=utf8><style>body{margin:0;background:#0a1630;font-family:Arial}.w{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;padding:10px;width:1180px}.c{background:radial-gradient(ellipse at 50% 30%,#1f5a9c,#0b2550 75%);border-radius:14px;padding:8px}.c canvas{width:100%;display:block}.c p{margin:4px 4px 0;color:#ffc93c;font-weight:900;font-size:15px}</style></head><body><div class="w" id="w"></div><script>const SKI_MAP=${M};${src}
const P=${JSON.stringify(P)};skiMapLoad(()=>{const t0=performance.now();for(const[n,p]of P){const d=skiPaint(p);const c=document.createElement('canvas');c.width=d.width;c.height=d.height;c.getContext('2d').putImageData(d,0,0);const box=document.createElement('div');box.className='c';box.append(c);const q=document.createElement('p');q.textContent=n;box.append(q);document.getElementById('w').append(box);}document.body.dataset.ms=Math.round(performance.now()-t0);document.body.dataset.done=1;});</script></body></html>`;
fs.writeFileSync('t128.html',html);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:1200,height:700}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('file://'+process.cwd()+'/t128.html');await p.waitForSelector('body[data-done]');console.log('ms',await p.evaluate(()=>document.body.dataset.ms));await p.screenshot({path:'t128.png',fullPage:true});console.log(JSON.stringify(errs));await b.close();})();
