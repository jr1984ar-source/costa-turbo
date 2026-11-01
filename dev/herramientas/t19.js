const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.waitForTimeout(300);
 await p.click('#aGo');await p.waitForTimeout(300);await p.click('#gGo');await p.waitForTimeout(300);
 await p.evaluate(()=>{__G.zi=7;__goMap();});await p.waitForTimeout(300);await p.click('#mGo');await p.waitForTimeout(3600);
 const info=await p.evaluate(()=>{const all=[...__G.zone.objs,...(__G.zone.movers||[])];const ts={};all.forEach(o=>ts[o.t]=(ts[o.t]||0)+1);const o=all.find(o=>o.t==='patrol'&&o.y<-1500);__G.P.y=o.y+230;__G.P.x=Math.min(300,Math.max(120,o.x));return ts;});
 await p.waitForTimeout(250);await p.screenshot({path:'z-telm-pol.png'});
 console.log(JSON.stringify(info),JSON.stringify(errs));await b.close();})();
