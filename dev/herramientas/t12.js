const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 let body=fs.readFileSync('costa-turbo.html','utf8');body=body.replace("requestAnimationFrame(frame);\n})();","window.__G=G;window.__goMap=goMap;requestAnimationFrame(frame);\n})();");
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.click('#gGo');await p.waitForTimeout(200);
 await p.evaluate(()=>{__G.zi=1;__goMap();});await p.waitForTimeout(300);
 const info=await p.evaluate(()=>({len:__G.zone.len,gates:__G.zone.gatesTotal,time:__G.time,check:Math.round(__G.zone.len/3/170)+3}));
 await p.click('#mGo');await p.waitForTimeout(3600);await p.keyboard.down('ArrowUp');await p.waitForTimeout(3000);await p.screenshot({path:'cala2.png'});
 console.log(JSON.stringify(info),JSON.stringify(errs));await b.close();})();
