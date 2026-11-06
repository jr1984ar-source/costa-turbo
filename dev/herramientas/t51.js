const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1000);await p.click('#bPlay');await p.waitForTimeout(200);
 await p.evaluate(()=>{__G.free=true;__G.zi=0;__goMap();});await p.waitForTimeout(400);await p.screenshot({path:'d-1.png'});
 await p.evaluate(()=>{__G.zi=19;__goMap();});await p.waitForTimeout(400);await p.screenshot({path:'d-2.png'});
 await p.evaluate(()=>__T.goFree());await p.waitForTimeout(600);await p.screenshot({path:'d-3.png'});
 console.log(JSON.stringify(errs));await b.close();})();
