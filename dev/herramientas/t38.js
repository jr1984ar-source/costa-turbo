const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__G.free=true;__G.zi=10;__goMap();});await W(500);await p.screenshot({path:'z-boyas-map.png'});
 await E(()=>__T.startRace());await W(3600);await E(()=>{const bs=__G.zone.objs.filter(o=>o.t==='tbuoy').sort((a,c)=>c.y-a.y);__G.P.y=bs[1].y+380;__G.P.x=200;__G.P.v=0;});await W(500);await p.screenshot({path:'z-boyas3.png'});
 console.log(JSON.stringify(errs));await b.close();})();
