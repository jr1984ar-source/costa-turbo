const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(500);
 await E(()=>localStorage.setItem('ct_gear',JSON.stringify({own:['s0','v0','h0','h3','v3','s4'],eq:{suit:'s4',vest:'v3',helm:'h3'}})));await p.reload();await W(1000);await p.click('#bPlay');await W(200);
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},'BAHAMAS');await W(300);await E(()=>__T.startRace());await W(3800);
 await p.screenshot({path:'race-gear.png',clip:{x:145,y:400,width:100,height:120}});console.log(JSON.stringify(errs));await b.close();})();
