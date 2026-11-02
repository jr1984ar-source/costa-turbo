const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);
 await p.click('#bPlay');await W(300);await p.click('#aGo');await W(700);
 const shots=[];
 for(const k of [0,2,7,10]){await E(k=>{__G.moto=k;},k);await E(()=>__T.renderGarage());await W(400);const r=await E(()=>{const a=document.querySelector('#gName').getBoundingClientRect(),c=document.querySelector('#gColors').getBoundingClientRect();return {n:document.querySelector('#gName').textContent,nameTop:a.top|0,colTop:c.top|0,colH:c.height|0,colW:c.width|0};});console.log(JSON.stringify(r));
   const el=await p.$('.gname');await el.screenshot({path:'v75-gname-'+k+'.png'});}
 console.log(JSON.stringify(errs));await b.close();})();
