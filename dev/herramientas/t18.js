const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.waitForTimeout(300);
 await p.click('#aGo');await p.waitForTimeout(300);await p.click('#gGo');await p.waitForTimeout(300);
 await p.evaluate(()=>{__G.zi=7;__goMap();});await p.waitForTimeout(300);await p.click('#mGo');await p.waitForTimeout(3600);
 const pat=await p.evaluate(()=>{const o=__G.zone.objs.concat(__G.zone.movers||[]).find(o=>/patrol|police/.test(o.t)&&o.y<-1500);if(!o)return null;__G.P.y=o.y+260;__G.P.x=o.x;return {t:o.t,x:o.x|0,y:o.y|0};});
 await p.waitForTimeout(500);await p.screenshot({path:'z-telm-pol.png'});
 const r=[];for(let i=0;i<4;i++){await p.waitForTimeout(5000);r.push(await p.evaluate(()=>__G.rivals.map(c=>Math.round(-c.y)+'/'+Math.round(c.v)).join(' ')));}
 console.log(JSON.stringify(pat));console.log(r.join('\n'));console.log(JSON.stringify(errs));await b.close();})();
