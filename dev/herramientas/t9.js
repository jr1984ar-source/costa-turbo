const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 let body=fs.readFileSync('costa-turbo.html','utf8');body=body.replace("requestAnimationFrame(frame);\n})();","window.__G=G;requestAnimationFrame(frame);\n})();");
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:2,hasTouch:true});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push('PE '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push('CE '+m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.waitForTimeout(200);await p.click('#gGo');await p.waitForTimeout(300);await p.click('#mGo');await p.waitForTimeout(3600);
 await p.keyboard.down('ArrowUp');await p.waitForTimeout(2500);
 const s0=await p.evaluate(()=>__G.score);
 await p.keyboard.down(' ');await p.keyboard.down('ArrowLeft');await p.waitForTimeout(450);await p.screenshot({path:'ct16-drift.png'});
 const mid=await p.evaluate(()=>({x:__G.P.x|0,h:__G.P.h.toFixed(2),va:__G.P.va.toFixed(2),v:__G.P.v|0,dt:__G.P.driftT.toFixed(2)}));
 await p.waitForTimeout(400);await p.keyboard.up('ArrowLeft');await p.keyboard.up(' ');await p.waitForTimeout(150);
 const after=await p.evaluate(()=>({score:__G.score,boost:__G.P.boostT.toFixed(2)}));
 await p.keyboard.up('ArrowUp');await p.keyboard.down('ArrowDown');await p.waitForTimeout(3500);
 const rev=await p.evaluate(()=>({v:__G.P.v|0}));await p.screenshot({path:'ct17-rev.png'});
 console.log(s0,JSON.stringify(mid),JSON.stringify(after),JSON.stringify(rev),JSON.stringify(errs));await b.close();})();
