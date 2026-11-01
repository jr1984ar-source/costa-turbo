const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 const body=fs.readFileSync('costa-turbo.html','utf8');
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:2,hasTouch:true});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push('PE '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push('CE '+m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1500);
 await p.click('#bPlay');await p.click('#gGo');await p.waitForTimeout(300);await p.click('#mGo');await p.waitForTimeout(3600);
 await p.evaluate(()=>{const G=window.__ct.G,r=G.zone.ring;G.P.y=r.y+40;G.P.x=r.x;G.P.v=90;});await p.waitForTimeout(800);
 console.log('mode',await p.evaluate(()=>window.__ct.G.mode));await p.screenshot({path:'ct11-jj.png'});
 await p.click('#jjOut2');await p.waitForTimeout(300);
 // chase zone
 await p.evaluate(()=>{const G=window.__ct.G;G.zi=3;});await p.evaluate(()=>{window.__ct.G.mode='x';});
 await p.evaluate(()=>{document.querySelector('#pQuit');});
 await p.evaluate(()=>{const G=window.__ct.G;G.P.y=G.zone.finishY+5;});await p.waitForTimeout(2500);
 await p.evaluate(()=>document.querySelector('#rGo')&&document.querySelector('#rGo').click());await p.waitForTimeout(500);
 await p.evaluate(()=>{const G=window.__ct.G;G.zi=3;});
 // go map for zone 4 by simulating
 await p.evaluate(()=>{const G=window.__ct.G;G.zi=3;});
 await p.evaluate(()=>{document.querySelector('#mGo')});
 await b.close();console.log(JSON.stringify(errs));})();
