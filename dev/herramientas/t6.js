const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 const body=fs.readFileSync('costa-turbo.html','utf8');
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:2,hasTouch:true});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push('PE '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push('CE '+m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.click('#gGo');await p.waitForTimeout(200);await p.click('#mGo');await p.waitForTimeout(3600);
 await p.evaluate(()=>{window.__ct.G.time=.3;});await p.waitForTimeout(2200);await p.screenshot({path:'ct12-fail.png'});
 await p.click('#rGo');await p.waitForTimeout(300);await p.click('#mGo');await p.waitForTimeout(3600);
 await p.evaluate(()=>{const G=window.__ct.G;G.lives=1;G.score=12345;G.time=.3;});await p.waitForTimeout(2600);await p.screenshot({path:'ct13-over.png'});
 await p.fill('#nameIn','jose');await p.click('#nameForm button');await p.waitForTimeout(500);await p.screenshot({path:'ct14-rank.png'});
 console.log(JSON.stringify(errs));await b.close();})();
