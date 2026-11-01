const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);await E(()=>{__G.money=50000;});
 await p.click('#bShop');await W(400);await p.click('#sGear');await W(500);await p.click('#eTabs [data-c="suit"]');await W(300);await p.screenshot({path:'v64-a.png'});
 await E(()=>{const r=[...document.querySelectorAll('#eList .prt')];r[3].click();});await W(300);await p.screenshot({path:'v64-b.png'});
 for(const av of [2,5]){await E(a=>{__G.avatar=a;},av);await E(()=>{const r=[...document.querySelectorAll('#eList .prt')];r[0].click();});await W(300);await p.screenshot({path:'v64-c'+av+'.png'});}
 console.log(JSON.stringify(errs));await b.close();})();
