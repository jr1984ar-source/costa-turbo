// Genera la web (../index.html) y el archivo para descargar (costa-turbo-movil.html) a partir de costa-turbo.html.
// Uso, desde la carpeta del repositorio:  node dev/rebuild.js
// Después, sube la versión de caché en sw.js (costa-turbo-vNN) para que la app instalada se actualice.
const fs=require('fs'),path=require('path'),D=__dirname,ROOT=path.join(D,'..');
const src=fs.readFileSync(path.join(D,'costa-turbo.html'),'utf8').replace('<meta name="claude:viewport-fit-sides" content="cover">\n','');
const icon='data:image/png;base64,'+fs.readFileSync(path.join(ROOT,'icon-180.png')).toString('base64');
const metas=`<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="description" content="Carreras de motos de agua por la costa."><meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"><meta name="apple-mobile-web-app-title" content="Costa Turbo"><meta name="theme-color" content="#0a1630">`;
const base=`<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style></head><body>`;
fs.writeFileSync(path.join(ROOT,'index.html'),`<!doctype html><html lang="es"><head>${metas}<link rel="manifest" href="manifest.webmanifest"><link rel="apple-touch-icon" href="icon-180.png"><link rel="icon" type="image/png" href="icon-192.png">${base}${src}\n<script>if('serviceWorker' in navigator)addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));</script>\n</body></html>\n`);
fs.writeFileSync(path.join(D,'costa-turbo-movil.html'),`<!doctype html><html lang="es"><head>${metas}<link rel="apple-touch-icon" href="${icon}"><link rel="icon" href="${icon}">${base}${src}\n</body></html>\n`);
console.log('ok');
