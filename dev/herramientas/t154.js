const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await W(1200);
 const zs=(process.argv[2]||'0').split(',').map(Number);
 for(const zi of zs){await E(zi=>__T.startFree(zi),zi);await W(400);await E(()=>__T.startRace());await W(4200);
  await E(()=>{const P=__G.P,r=__G.zone.ring;P.y=r.y+330;P.x=r.x+200;P.v=0;P.h=0;P.inv=5;__G.rivals.forEach(c=>c.y=P.y+900);});await W(600);await p.screenshot({path:'bar-'+zi+'.png'});}
 console.log('errs',JSON.stringify(errs));await b.close();})();
