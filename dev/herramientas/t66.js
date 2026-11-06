const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);
 await E(()=>__T.goFree());await W(800);await p.screenshot({path:'cov-free.png'});
 console.log(await E(()=>[...document.querySelectorAll('.screen:not([hidden])')].map(e=>e.id+':'+e.innerHTML.length).join(',')));
 console.log(JSON.stringify(errs));await b.close();})();
