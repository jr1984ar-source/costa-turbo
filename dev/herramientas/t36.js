const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1000);await p.click('#bFree');await p.click('#aGo');await p.click('#gGo');await p.waitForTimeout(800);
 await p.evaluate(()=>document.getElementById('scrFree').scrollTop=600);await p.waitForTimeout(300);await p.screenshot({path:'n-09-free.png'});
 await p.evaluate(()=>document.querySelectorAll('.fz')[10].click());await p.waitForTimeout(600);await p.screenshot({path:'n-10-map-boyas.png'});
 console.log(JSON.stringify(errs));await b.close();})();
