const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=1;__goMap();});await W(300);await E(()=>__T.startRace());await W(3800);
 const info=await E(()=>{const Zn=__G.zone,r=Zn.ring;const P=__G.P;P.x=r.x+30;P.y=r.y+250;P.v=0;return{bar:Zn.bar,ring:r,len:Zn.len};});
 await W(500);await p.screenshot({path:'lacala-bar.png'});
 console.log(JSON.stringify(info),JSON.stringify(errs));await b.close();})();
