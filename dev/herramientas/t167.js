const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1200);
 for(const zi of [3,19]){await p.evaluate(zi=>__T.startFree(zi),zi);await p.waitForTimeout(300);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4500);
  const r=await p.evaluate(()=>{const st=document.querySelector('#stage').getBoundingClientRect();const Zn=__G.zone;if(Zn.circ)return {circuito:true};return {posMoto:Math.round((__G.P.y-window.__camTop)/1)};});
  await p.screenshot({path:'v84-'+zi+'.png'});console.log(zi,JSON.stringify(r));}
 console.log('errs',JSON.stringify(errs));await b.close();})();
