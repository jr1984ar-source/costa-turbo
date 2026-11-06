const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);
 await p.click('#bFree');await W(800);await p.screenshot({path:'cov-free.png'});
 await E(()=>{const el=document.querySelector('#scrFree .screen-body, #scrFree');el&&el.scrollTo&&el.scrollTo(0,1400);document.querySelectorAll('#scrFree *').forEach(e=>{if(e.scrollHeight>e.clientHeight+50)e.scrollTop=1400;});});await W(400);await p.screenshot({path:'cov-free2.png'});
 await E(()=>{__T.newGame();__G.zi=19;__goMap();});await W(600);await p.screenshot({path:'cov-map.png'});
 console.log(JSON.stringify(errs));await b.close();})();
