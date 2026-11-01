// Genera la web (../index.html, ../sw.js) y el archivo para descargar desde costa-turbo.html.
// Uso, desde la carpeta del repositorio:  node dev/rebuild.js   (antes, sube APP_VER en costa-turbo.html)
const fs=require('fs'),path=require('path'),D=__dirname,ROOT=path.join(D,'..');
const src=fs.readFileSync(path.join(D,'costa-turbo.html'),'utf8').replace('<meta name="claude:viewport-fit-sides" content="cover">\n','');
const ver=(src.match(/const APP_VER=(\d+)/)||[])[1];if(!ver)throw new Error('falta APP_VER');
const icon='data:image/png;base64,'+fs.readFileSync(path.join(ROOT,'icon-180.png')).toString('base64');
const metas=`<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="description" content="Carreras de motos de agua por la costa."><meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"><meta name="apple-mobile-web-app-title" content="Costa Turbo"><meta name="theme-color" content="#0a1630">`;
const base=`<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style></head><body>`;
fs.writeFileSync(path.join(ROOT,'index.html'),`<!doctype html><html lang="es"><head>${metas}<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-180.png"><link rel="icon" type="image/png" href="icon-192.png">${base}${src}\n<script>if('serviceWorker' in navigator)addEventListener('load',()=>navigator.serviceWorker.register('sw.js').then(r=>{try{r.update();}catch(_){}}).catch(()=>{}));</script>\n</body></html>\n`);
fs.writeFileSync(path.join(D,'costa-turbo-movil.html'),`<!doctype html><html lang="es"><head>${metas}<link rel="apple-touch-icon" href="${icon}"><link rel="icon" href="${icon}">${base}${src}\n</body></html>\n`);
fs.writeFileSync(path.join(ROOT,'sw.js'),`const CACHE='costa-turbo-v${ver}';
const FILES=['./','./index.html','./manifest.webmanifest','./icon-180.png','./icon-192.png','./icon-512.png'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES.map(f=>new Request(f,{cache:'reload'})))).then(()=>self.skipWaiting()));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(n=>n!==CACHE).map(n=>caches.delete(n)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{const q=e.request;if(q.method!=='GET')return;const u=new URL(q.url);if(u.origin!==location.origin)return;
 const doc=q.mode==='navigate'||u.pathname.endsWith('/')||u.pathname.endsWith('.html')||u.pathname.endsWith('.webmanifest');
 e.respondWith(fetch(doc?u.href:q,doc?{cache:'no-store',credentials:'same-origin'}:undefined).then(r=>{if(r&&r.ok){const cp=r.clone();caches.open(CACHE).then(c=>c.put(q,cp)).catch(()=>{});}return r;}).catch(()=>caches.match(q).then(r=>r||caches.match('./index.html'))));});
`);
console.log('ok v'+ver);
