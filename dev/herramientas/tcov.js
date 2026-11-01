const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 let body=fs.readFileSync('costa-turbo.html','utf8');const cov=fs.readFileSync('cover.js','utf8');
 body=body.replace("/* ---- ranking ---- */",cov+"\n/* ---- ranking ---- */").replace("requestAnimationFrame(frame);\n})();","window.__G=G;window.__cov=drawCover;requestAnimationFrame(frame);\n})();");
 fs.writeFileSync('ct-cov.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1"></head><body>'+body+'<div id=cg style="position:fixed;inset:0;z-index:99;background:#000;display:grid;grid-template-columns:1fr 1fr;gap:4px;padding:4px"></div></body></html>');
 const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:900,height:1300},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-cov.html');await p.waitForTimeout(1500);
 await p.evaluate(async()=>{await document.fonts.ready;const cg=document.getElementById('cg');for(let i=0;i<10;i++){const c=document.createElement('canvas');c.width=880;c.height=495;c.style.width='100%';cg.append(c);__cov(c,i);}});
 await p.waitForTimeout(300);await p.screenshot({path:'z-covers.png'});console.log(JSON.stringify(errs));await b.close();})();
