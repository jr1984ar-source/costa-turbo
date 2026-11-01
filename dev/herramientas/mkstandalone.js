const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 const src=fs.readFileSync('costa-turbo.html','utf8');
 const grab=name=>{const a=src.indexOf('function '+name+'(');let i=src.indexOf('{',a),d=0;for(;i<src.length;i++){if(src[i]==='{')d++;else if(src[i]==='}'){d--;if(!d)break;}}return src.slice(a,i+1);};
 const fns=[grab('mixc'),grab('drawJetProfile')].join('\n');
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:180,height:180}});
 await p.setContent(`<canvas id=c width=180 height=180></canvas><script>const TAU=Math.PI*2;${fns}
 const c=document.getElementById('c'),g=c.getContext('2d');
 let gr=g.createLinearGradient(0,0,0,180);gr.addColorStop(0,'#ffb067');gr.addColorStop(.45,'#ff7a1a');gr.addColorStop(.46,'#33c3dd');gr.addColorStop(1,'#0b5cad');g.fillStyle=gr;g.fillRect(0,0,180,180);
 g.fillStyle='rgba(255,255,255,.18)';for(let i=0;i<8;i++){g.fillRect(10+i*21,120+(i%3)*14,14,2);}
 g.save();g.translate(4,46);g.scale(.505,.505);drawJetProfile(g,{deck:'#f2f3f5',hood:'#e3202b',hull:'#e3202b',trim:'#1b1d22',seatA:'#f2f3f5',seatB:'#e3202b',seatC:'#1b1d22',stripe:'#1b1d22'});g.restore();
 g.fillStyle='#fff';g.font='900 30px Arial Black, Arial, sans-serif';g.textAlign='center';g.save();g.translate(90,34);g.transform(1,0,-.15,1,0,0);g.fillText('TURBO',0,0);g.restore();
 </script>`);
 await p.waitForTimeout(300);
 const png=await p.evaluate(()=>document.getElementById('c').toDataURL('image/png'));
 fs.writeFileSync('ct-icon.png',Buffer.from(png.split(',')[1],'base64'));
 const head=`<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes"><meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"><meta name="apple-mobile-web-app-title" content="Costa Turbo"><meta name="theme-color" content="#0a1630"><link rel="apple-touch-icon" href="${png}"><link rel="icon" href="${png}"><style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}[hidden]{display:none!important}</style></head><body>`;
 fs.writeFileSync('costa-turbo-movil.html',head+src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')+'\n</body></html>');
 // smoke test the standalone file
 const q=await b.newPage({viewport:{width:390,height:780}});const errs=[];q.on('pageerror',e=>errs.push(e.message));
 await q.goto('file://'+process.cwd()+'/costa-turbo-movil.html');await q.waitForTimeout(1500);await q.click('#bPlay');await q.click('#gGo');await q.waitForTimeout(300);await q.click('#mGo');await q.waitForTimeout(3700);await q.keyboard.down('ArrowUp');await q.waitForTimeout(1500);
 await q.screenshot({path:'standalone.png'});
 console.log('errors',JSON.stringify(errs),'size',fs.statSync('costa-turbo-movil.html').size);await b.close();})();
