const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 let body=fs.readFileSync('costa-turbo.html','utf8');body=body.replace("requestAnimationFrame(frame);\n})();","window.__G=G;window.__goMap=goMap;window.__T={zoneWin,gameOver,goShop,goFree,openBar,startRace,renderShop,get best(){return best},set best(v){best=v}};requestAnimationFrame(frame);\n})();");
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body>'+body+'</body></html>');
 const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2,hasTouch:true,isMobile:true});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const S=async n=>{await p.waitForTimeout(350);await p.screenshot({path:'v12-'+n+'.png'});};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1500);await S('01-title');
 await p.tap('#bShop');await S('02-shop');await p.tap('#sNext');await p.tap('#sNext');await S('03-shop-avispa');await p.tap('#sNext');await p.tap('#sNext');await S('04-shop-lock');
 await p.tap('#sBack');await p.waitForTimeout(200);
 await p.tap('#bPlay');await S('05-pilot');await p.tap('#aGo');await p.tap('#gNext');await S('06-garage-lock');await p.tap('#gPrev');await p.tap('#gGo');await S('07-map-champ');
 await p.evaluate(()=>{__G.zi=2;__goMap();});await S('08-map-mago');await p.tap('#mGo');await p.waitForTimeout(3800);await p.keyboard.down('ArrowUp');await p.waitForTimeout(1500);await S('09-race-mago');
 const x0=await p.evaluate(()=>__G.P.x);await p.keyboard.down('ArrowRight');await p.waitForTimeout(600);await p.keyboard.up('ArrowRight');const x1=await p.evaluate(()=>__G.P.x);await p.keyboard.up('ArrowUp');
 // champ win zone 5 -> unlocks
 await p.evaluate(()=>{__G.zi=4;__G.P.rank=1;__T.zoneWin();});await p.waitForTimeout(400);await S('10-result-unlock');
 // roxy locks: zone 2 (la cala) bar roxy
 await p.evaluate(()=>{__T.best=1;__G.zi=1;__goMap();__T.startRace();});await p.waitForTimeout(500);await p.evaluate(()=>{__G.money=9000;__T.openBar();});await S('11-roxy');
 // free race
 await p.evaluate(()=>{document.querySelector('#rxOut').click();});await p.waitForTimeout(300);await p.evaluate(()=>{__T.goFree();});await S('12-free');
 await p.evaluate(()=>{document.querySelectorAll('.fz')[6].click();});await S('13-map-free');
 await p.evaluate(()=>{__G.P.rank=1;__T.zoneWin();});await p.waitForTimeout(300);await S('14-free-win');await p.tap('#rGo');await S('15-back-free');
 // paint
 await p.evaluate(()=>{__T.best=1;__T.goShop('title');});await S('16-shop-own');await p.tap('#sPaint');await S('17-paint');
 const st=await p.evaluate(()=>({money:__G.money,wallet:localStorage.getItem('ct_wallet'),best:localStorage.getItem('ct_best'),own:localStorage.getItem('ct_own')}));
 console.log(JSON.stringify({x0,x1,st}),JSON.stringify(errs));
 // landscape pilot
 const p2=await (await b.newContext({viewport:{width:844,height:390},deviceScaleFactor:2,hasTouch:true,isMobile:true})).newPage();await p2.goto('file://'+process.cwd()+'/ct-wrapped.html');await p2.waitForTimeout(1200);await p2.screenshot({path:'v12-18-land-title.png'});await p2.tap('#bPlay');await p2.waitForTimeout(400);await p2.screenshot({path:'v12-19-land-pilot.png'});
 await b.close();})();
