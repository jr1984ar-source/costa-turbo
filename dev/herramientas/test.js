const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 const body=fs.readFileSync('alerta-galactica.html','utf8');
 fs.writeFileSync('wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:700},deviceScaleFactor:2,hasTouch:true,isMobile:true});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/wrapped.html');await p.waitForTimeout(800);
 await p.screenshot({path:'s1.png'});
 await p.click('#btnPlay');await p.waitForTimeout(400);await p.screenshot({path:'s2.png'});
 await p.click('#btnLaunch');await p.waitForTimeout(2000);
 await p.keyboard.down(' ');await p.keyboard.down('ArrowLeft');await p.waitForTimeout(1200);await p.keyboard.up('ArrowLeft');
 await p.keyboard.press('b');await p.waitForTimeout(300);await p.screenshot({path:'s3.png'});
 await p.waitForTimeout(2500);await p.keyboard.up(' ');
 const st=await p.evaluate(()=>document.querySelector('#bombCount').textContent);
 await p.screenshot({path:'s4.png'});
 // landscape
 console.log('bombs',st,'errors',JSON.stringify(errs));const p2=await (await b.newContext({viewport:{width:844,height:390},deviceScaleFactor:2,hasTouch:true,isMobile:true})).newPage();p2.on('pageerror',e=>errs.push(e.message));await p2.goto('file://'+process.cwd()+'/wrapped.html');await p2.waitForTimeout(500);await p2.evaluate(()=>document.querySelector('#btnPlay').click());await p2.waitForTimeout(300);await p2.evaluate(()=>document.querySelector('#btnLaunch').click());await p2.waitForTimeout(2500);await p2.screenshot({path:'s5.png'});
 console.log('bombs',st,'errors',JSON.stringify(errs));await b.close();})();
