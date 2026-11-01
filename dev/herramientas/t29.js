const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);
 await E(()=>{__G.free=true;__G.zi=5;__goMap();__T.startRace();});await W(3600);
 await E(()=>{const o=__G.zone.waves[1],P=__G.P;P.y=o.y+300;P.x=230;P.v=0;o.act=1;});await W(600);await p.screenshot({path:'w-05-wave.png'});
 await E(()=>{const P=__G.P;P.y=__G.zone.waves[4].y+330;P.v=0;__G.zone.waves.slice(4).forEach(o=>o.act=1);});await W(500);await p.screenshot({path:'w-06-set.png'});
 console.log(JSON.stringify(errs));await b.close();})();
