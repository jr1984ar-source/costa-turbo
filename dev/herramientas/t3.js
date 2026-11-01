const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 const body=fs.readFileSync('costa-turbo.html','utf8');
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:2,hasTouch:true});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push('PE '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push('CE '+m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(2500);await p.screenshot({path:'ct1-title.png'});
 await p.click('#bPlay');await p.waitForTimeout(400);await p.screenshot({path:'ct2-garage.png'});
 await p.click('#gGo');await p.waitForTimeout(600);await p.screenshot({path:'ct3-map.png'});
 await p.click('#mGo');await p.waitForTimeout(3600);
 await p.keyboard.down('ArrowUp');await p.waitForTimeout(2500);await p.keyboard.down('ArrowLeft');await p.waitForTimeout(500);await p.keyboard.up('ArrowLeft');
 await p.keyboard.press('x');await p.waitForTimeout(2500);await p.screenshot({path:'ct4-race.png'});
 const st=await p.evaluate(()=>{const G=window.__ct.G;return {mode:G.mode,y:G.P.y|0,v:G.P.v|0,money:G.money,fuel:G.fuel|0,rank:G.P.rank,time:G.time|0}});console.log(JSON.stringify(st));
 // jump to near bar
 await p.evaluate(()=>{const G=window.__ct.G,r=G.zone.ring;G.P.y=r.y+260;G.P.x=r.x;G.P.v=150;});
 await p.keyboard.up('ArrowUp');await p.waitForTimeout(400);await p.screenshot({path:'ct5-nearbar.png'});
 await p.waitForTimeout(2500);console.log('mode after',await p.evaluate(()=>window.__ct.G.mode));await p.screenshot({path:'ct6-jj.png'});
 await p.evaluate(()=>{if(window.__ct.G.mode==='bar')document.querySelector('#jjOut').click();});await p.waitForTimeout(300);
 // jump to finish
 await p.keyboard.down('ArrowUp');await p.evaluate(()=>{const G=window.__ct.G;G.P.y=G.zone.finishY+300;G.P.x=200;});await p.waitForTimeout(2500);await p.screenshot({path:'ct7-result.png'});
 console.log('mode',await p.evaluate(()=>window.__ct.G.mode));
 await p.keyboard.up('ArrowUp');
 await p.evaluate(()=>document.querySelector('#rGo').click());await p.waitForTimeout(600);await p.screenshot({path:'ct8-map2.png'});
 await p.click('#mGo');await p.waitForTimeout(3600);await p.keyboard.down('ArrowUp');await p.waitForTimeout(3000);await p.screenshot({path:'ct9-cala.png'});
 await p.evaluate(()=>{const G=window.__ct.G,r=G.zone.ring;G.P.y=r.y+60;G.P.x=r.x;G.P.v=100;});await p.keyboard.up('ArrowUp');await p.waitForTimeout(1200);await p.screenshot({path:'ct10-roxy.png'});
 console.log(JSON.stringify(errs.slice(0,10)));await b.close();})();
