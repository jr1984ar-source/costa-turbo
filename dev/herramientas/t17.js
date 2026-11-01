const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 let body=fs.readFileSync('costa-turbo.html','utf8');body=body.replace("requestAnimationFrame(frame);\n})();","window.__G=G;window.__goMap=goMap;requestAnimationFrame(frame);\n})();");
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.waitForTimeout(300);
 await p.click('#aGo');await p.waitForTimeout(300);await p.click('#gGo');await p.waitForTimeout(300);
 await p.evaluate(()=>{__G.zi=7;__goMap();});await p.waitForTimeout(400);await p.screenshot({path:'z-map-telm.png'});
 await p.click('#mGo');await p.waitForTimeout(800);await p.screenshot({path:'z-telm-intro.png'});await p.waitForTimeout(2800);
 await p.keyboard.down('ArrowUp');await p.waitForTimeout(1500);await p.screenshot({path:'z-telm-start.png'});
 // steering test
 const x0=await p.evaluate(()=>__G.P.x);await p.keyboard.down('ArrowRight');await p.waitForTimeout(700);await p.keyboard.up('ArrowRight');
 const x1=await p.evaluate(()=>__G.P.x);await p.screenshot({path:'z-telm-right.png'});
 await p.keyboard.down('ArrowLeft');await p.waitForTimeout(1100);await p.keyboard.up('ArrowLeft');const x2=await p.evaluate(()=>__G.P.x);
 // jump to a cala and a mount section
 const info=await p.evaluate(()=>({zone:__G.zone.Z.name,mirror:__G.zone.Z.mirror,y:__G.P.y|0,fin:__G.zone.finishY|0}));
 for(const [n,dy] of [['a',-3000],['b',-5200],['c',-7400],['d',-9800]]){await p.evaluate(dy=>{const G=__G;G.P.y=dy;G.P.x=270;G.P.h=0;G.P.va=0;},dy);await p.waitForTimeout(900);await p.screenshot({path:'z-telm-'+n+'.png'});}
 await p.evaluate(()=>{const G=__G;G.P.y=G.zone.finishY+500;G.P.x=250;});await p.waitForTimeout(900);await p.screenshot({path:'z-telm-meta.png'});
 await p.keyboard.up('ArrowUp');
 console.log(JSON.stringify({x0,x1,x2,info}),JSON.stringify(errs));await b.close();})();
