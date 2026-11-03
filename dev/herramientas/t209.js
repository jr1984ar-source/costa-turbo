// dibuja la moto del taller con pegatinas a tamaño completo (usa el código del juego)
const {chromium}=require('playwright');const fs=require('fs');
const cfg=JSON.parse(process.argv[2]||'{}'),out=process.argv[3]||'logo_full.png',extra=process.argv[4]?fs.readFileSync(process.argv[4],'utf8'):'';
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1500);
 const u=await p.evaluate(async([cfg,extra])=>{await new Promise(r=>__ski.load(r));const m=__ski.MOTOS[cfg.moto||0];const pp=Object.assign(__ski.paintOf(m),cfg);const d=__ski.paint(pp);const cv=document.createElement('canvas');cv.width=d.width;cv.height=d.height;const g=cv.getContext('2d');g.putImageData(d,0,0);
  if(extra){const mixc=(h,o,t)=>h;eval(extra);window.__alt(g,pp,__ski.D,m);}else __ski.decor(g,m,pp);
  const c2=document.createElement('canvas');c2.width=d.width;c2.height=d.height;const g2=c2.getContext('2d');g2.fillStyle='#22345a';g2.fillRect(0,0,c2.width,c2.height);g2.drawImage(cv,0,0);return c2.toDataURL();},[cfg,extra]);
 fs.writeFileSync(out,Buffer.from(u.split(',')[1],'base64'));console.log('errs',JSON.stringify(errs));await b.close();})();
