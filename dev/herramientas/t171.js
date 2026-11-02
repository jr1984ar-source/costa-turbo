const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1000);
 await p.evaluate(()=>__T.startFree(13));await p.waitForTimeout(400);
 console.log('tormenta:',await p.evaluate(()=>__G.zone.Z.name+' bar:'+__G.zone.bar+' ring:'+!!__G.zone.ring+' | '+[...document.querySelectorAll('#mInfo span')].map(s=>s.textContent).join(' / ')));
 await p.evaluate(()=>__T.startRace());await p.waitForTimeout(5000);console.log('errs',JSON.stringify(errs));await b.close();})();
