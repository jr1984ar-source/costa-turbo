const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);
 await p.click('#bPlay');await W(300);await p.click('#aGo');await W(700);
 const st=()=>E(()=>{const c=document.querySelector('#gPv canvas.mph');return {moto:__M[__G.moto].id,lk:document.querySelector('#gPv').classList.contains('lk'),filter:c&&getComputedStyle(c).filter.slice(0,60),btn:document.querySelector('#gGo').textContent};});
 for(let i=0;i<10;i++){console.log(JSON.stringify(await st()));await p.click('#gNext');await W(250);}
 for(let i=0;i<4;i++){await p.click('#gPrev');await W(250);console.log('back',JSON.stringify(await st()));}
 console.log(JSON.stringify(errs));await b.close();})();
