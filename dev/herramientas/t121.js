const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);
 await p.click('#bPlay');await W(400);await p.click('#aGo');await W(500);await p.screenshot({path:'v63-garage.png'});
 for(let i=0;i<5;i++){await p.click('#gNext');await W(150);} await W(300);await p.screenshot({path:'v63-garage2.png'});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.screenshot({path:'v63-inicio.png'});
 console.log(JSON.stringify(errs));await b.close();})();
