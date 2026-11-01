const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 let body=fs.readFileSync('costa-turbo.html','utf8');body=body.replace("requestAnimationFrame(frame);\n})();","window.__G=G;window.__goMap=goMap;requestAnimationFrame(frame);\n})();");
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.waitForTimeout(300);
 const avs=await p.$$('.av');await avs[5].click();await p.fill('#aName','jose');await p.screenshot({path:'z-pilot.png'});
 await p.click('#aGo');await p.waitForTimeout(300);await p.screenshot({path:'z-garage.png'});
 await p.click('#gGo');await p.waitForTimeout(300);
 const shot=async(name,fn,wait)=>{await p.evaluate(fn);await p.waitForTimeout(wait||1200);await p.screenshot({path:name});};
 // MAGO
 await p.evaluate(()=>{__G.zi=2;__goMap();});await p.waitForTimeout(300);await p.screenshot({path:'z-map-mago.png'});
 await p.click('#mGo');await p.waitForTimeout(3600);await p.keyboard.down('ArrowUp');
 const isl=await p.evaluate(()=>{const o=__G.zone.big[0];return {x:o.x|0,y:o.y|0,rx:o.rx,ry:o.ry,big:__G.zone.big.length};});
 await shot('z-mago-island.png',()=>{const o=__G.zone.big[0];__G.P.y=o.y+o.ry+340;__G.P.x=o.x;__G.rivals.forEach((c,i)=>{c.y=o.y+o.ry+300+i*30;c.x=150+i*40;c.v=250;});},1500);
 await p.waitForTimeout(2500);const afterIsl=await p.evaluate(()=>{const o=__G.zone.big[0];return __G.rivals.map(c=>Math.round(c.y-o.y)).join(' ')+' | P '+Math.round(__G.P.y-o.y);});
 await shot('z-mago-boats.png',()=>{const G=__G;G.P.y=G.zone.finishY+1500;G.P.x=200;},1200);
 const piri=await p.evaluate(()=>{const o=__G.zone.objs.find(o=>o.t==='piri');__G.P.y=o.y+200;__G.P.x=o.rx;__G.P.h=0;return {lives:__G.lives,turbo:__G.turbo};});
 await p.waitForTimeout(400);await p.screenshot({path:'z-piri.png'});await p.waitForTimeout(1500);
 const piri2=await p.evaluate(()=>({lives:__G.lives,turbo:__G.turbo,gift:__G.zone.objs.find(o=>o.t==='piri').gift}));
 await p.keyboard.up('ArrowUp');
 // ES TRENC
 await p.evaluate(()=>{__G.zi=6;__goMap();});await p.waitForTimeout(300);await p.click('#mGo');await p.waitForTimeout(3600);await p.keyboard.down('ArrowUp');
 await p.waitForTimeout(1500);await p.screenshot({path:'z-trenc-start.png'});
 await shot('z-trenc-pass.png',()=>{const o=__G.zone.big.find(o=>o.t==='pass');__G.P.y=o.y+330;__G.P.x=o.gx;},900);
 await shot('z-trenc-island.png',()=>{const o=__G.zone.big.find(o=>o.t==='island');__G.P.y=o.y+o.ry+200;__G.P.x=o.x-o.rx-40;},900);
 await shot('z-trenc-float.png',()=>{const o=__G.zone.objs.find(o=>o.t==='float'&&o.y<-3000);__G.P.y=o.y+200;__G.P.x=o.x+60;},900);
 console.log(JSON.stringify(isl),afterIsl,JSON.stringify(piri),JSON.stringify(piri2),JSON.stringify(errs));await b.close();})();
