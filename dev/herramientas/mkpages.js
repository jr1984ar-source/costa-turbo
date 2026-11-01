const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 const src=fs.readFileSync('costa-turbo.html','utf8');
 const grab=name=>{const a=src.indexOf('function '+name+'(');let i=src.indexOf('{',a),d=0;for(;i<src.length;i++){if(src[i]==='{')d++;else if(src[i]==='}'){d--;if(!d)break;}}return src.slice(a,i+1);};
 const fns=[grab('mixc'),grab('drawJetProfile')].join('\n');
 const b=await chromium.launch();
 for(const N of [180,192,512]){const p=await b.newPage({viewport:{width:N,height:N}});
  await p.setContent(`<canvas id=c width=${N} height=${N}></canvas><script>const TAU=Math.PI*2;${fns}
  const c=document.getElementById('c'),g=c.getContext('2d');g.scale(${N}/180,${N}/180);
  let gr=g.createLinearGradient(0,0,0,180);gr.addColorStop(0,'#ffb067');gr.addColorStop(.45,'#ff7a1a');gr.addColorStop(.46,'#33c3dd');gr.addColorStop(1,'#0b5cad');g.fillStyle=gr;g.fillRect(0,0,180,180);
  g.fillStyle='rgba(255,255,255,.18)';for(let i=0;i<8;i++){g.fillRect(10+i*21,120+(i%3)*14,14,2);}
  g.save();g.translate(${N===512?'20,52':'4,46'});g.scale(${N===512?'.41,.41':'.505,.505'});drawJetProfile(g,{deck:'#f2f3f5',hood:'#e3202b',hull:'#e3202b',trim:'#1b1d22',seatA:'#f2f3f5',seatB:'#e3202b',seatC:'#1b1d22',stripe:'#1b1d22'});g.restore();
  g.fillStyle='#fff';g.font='900 ${N===512?26:30}px Arial Black, Arial, sans-serif';g.textAlign='center';g.save();g.translate(90,${N===512?40:34});g.transform(1,0,-.15,1,0,0);g.fillText('TURBO',0,0);g.restore();</script>`);
  await p.waitForTimeout(200);const png=await p.evaluate(()=>document.getElementById('c').toDataURL('image/png'));fs.writeFileSync('ghp/icon-'+N+'.png',Buffer.from(png.split(',')[1],'base64'));await p.close();}
 const head=`<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="description" content="Carreras de motos de agua por la costa."><meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"><meta name="apple-mobile-web-app-title" content="Costa Turbo"><meta name="theme-color" content="#0a1630"><link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-180.png"><link rel="icon" type="image/png" href="icon-192.png"><style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style></head><body>`;
 const tail=`\n<script>if('serviceWorker' in navigator)addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));</script>\n</body></html>\n`;
 fs.writeFileSync('ghp/index.html',head+src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')+tail);
 fs.writeFileSync('ghp/manifest.webmanifest',JSON.stringify({name:'Costa Turbo',short_name:'Costa Turbo',description:'Carreras de motos de agua por la costa.',lang:'es',start_url:'./',scope:'./',display:'fullscreen',orientation:'any',background_color:'#0a1630',theme_color:'#0a1630',icons:[{src:'icon-192.png',sizes:'192x192',type:'image/png'},{src:'icon-512.png',sizes:'512x512',type:'image/png',purpose:'any'},{src:'icon-180.png',sizes:'180x180',type:'image/png'}]},null,2)+'\n');
 fs.writeFileSync('ghp/sw.js',`const CACHE='costa-turbo-v1';
const FILES=['./','./index.html','./manifest.webmanifest','./icon-180.png','./icon-192.png','./icon-512.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting()));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(n=>n!==CACHE).map(n=>caches.delete(n)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;e.respondWith(fetch(e.request).then(r=>{const cp=r.clone();caches.open(CACHE).then(c=>c.put(e.request,cp)).catch(()=>{});return r;}).catch(()=>caches.match(e.request).then(r=>r||caches.match('./index.html'))));});
`);
 fs.writeFileSync('ghp/.nojekyll','');
 fs.writeFileSync('ghp/README.md','# Costa Turbo\n\nCarreras de motos de agua por la costa, para jugar en el móvil.\n\nPara instalarlo en el iPhone: ábrelo en Safari, pulsa Compartir y elige «Añadir a pantalla de inicio».\n');
 const q=await b.newPage({viewport:{width:390,height:780}});const errs=[];q.on('pageerror',e=>errs.push(e.message));
 await q.goto('file://'+process.cwd()+'/ghp/index.html');await q.waitForTimeout(1200);await q.click('#bPlay');await q.click('#gGo');await q.waitForTimeout(300);await q.click('#mGo');await q.waitForTimeout(3700);
 console.log('errors',JSON.stringify(errs));await b.close();})();
