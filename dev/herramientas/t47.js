const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__G.free=true;__G.zi=11;__goMap();});await W(400);await p.screenshot({path:'b-01-map.png'});
 await E(()=>__T.startRace());await W(3600);await E(()=>{const r=__G.zone.ring,P=__G.P;P.y=r.y+320;P.x=r.x;P.v=0;});await W(700);await p.screenshot({path:'b-02-top.png'});
 await p.keyboard.down('ArrowUp');for(let i=0;i<40;i++){await W(100);if(await E(()=>__G.mode==='bar'))break;}await p.keyboard.up('ArrowUp');
 const mode=await E(()=>__G.mode);if(mode!=='bar'){await E(()=>__T.openBar());}await W(500);await p.screenshot({path:'b-03-bar.png'});
 console.log(mode,JSON.stringify(errs));await b.close();})();
