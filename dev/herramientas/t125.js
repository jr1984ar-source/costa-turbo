const fs=require('fs');const {chromium}=require('playwright');
const M=JSON.parse(fs.readFileSync('zonas/ski_map.json','utf8'));const src=fs.readFileSync('skiart.js','utf8');
const P=[{hull:'#e3202b',deck:'#f4f5f7',hood:'#e3202b',stripe:'#f4f5f7',seat:'#16181d'},{hull:'#7b3fe4',deck:'#ff3f8e',hood:'#ff3f8e',stripe:'#f4f5f7',seat:'#7b3fe4'}];
const html=`<!doctype html><html><body style="margin:0;background:#cfd8e3"><div id="w"></div><script>const SKI_MAP=${JSON.stringify(M)};${src}
const P=${JSON.stringify(P)};skiMapLoad(()=>{const t0=performance.now();for(const p of P){const d=skiPaint(p);const c=document.createElement('canvas');c.width=d.width;c.height=d.height;c.getContext('2d').putImageData(d,0,0);c.style.width='560px';document.getElementById('w').append(c);}document.body.dataset.ms=Math.round(performance.now()-t0);document.body.dataset.done=1;});</script></body></html>`;
fs.writeFileSync('t125.html',html);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:600,height:700}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('file://'+process.cwd()+'/t125.html');await p.waitForSelector('body[data-done]');console.log('ms',await p.evaluate(()=>document.body.dataset.ms));await p.screenshot({path:'t125.png',fullPage:true});console.log(JSON.stringify(errs));await b.close();})();
