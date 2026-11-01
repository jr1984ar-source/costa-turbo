const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 const body=fs.readFileSync('costa-turbo.html','utf8');
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:2,hasTouch:true});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push('PE '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push('CE '+m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.waitForTimeout(200);
 await p.click('#gPrev');await p.waitForTimeout(100);await p.click('#gGo');await p.waitForTimeout(300);await p.click('#mGo');await p.waitForTimeout(3600);
 await p.keyboard.down('ArrowUp');await p.waitForTimeout(3500);await p.screenshot({path:'ct15-sombra.png'});
 console.log(JSON.stringify(errs));await b.close();})();
