const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);
 await E(()=>__T.goFree());await W(900);await p.screenshot({path:'cov41-a.png'});
 await E(()=>{document.querySelectorAll('#scrFree *').forEach(e=>{if(e.scrollHeight>e.clientHeight+50)e.scrollTop=1500;});const s=document.querySelector('#scrFree');s.scrollTop=1500;});await W(600);await p.screenshot({path:'cov41-b.png'});
 await E(()=>{document.querySelectorAll('#scrFree *').forEach(e=>{if(e.scrollHeight>e.clientHeight+50)e.scrollTop=9999;});const s=document.querySelector('#scrFree');s.scrollTop=9999;});await W(600);await p.screenshot({path:'cov41-c.png'});
 await E(()=>{__T.newGame();__G.zi=19;__goMap();});await W(700);await p.screenshot({path:'cov41-map.png'});
 console.log(JSON.stringify(errs));await b.close();})();
