const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:900,height:1000},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='BAHAMAS');__goMap();});await W(300);await E(()=>__T.startRace());await W(1500);
 await E(()=>{window.requestAnimationFrame=()=>0;document.querySelector('#hud').hidden=true;document.querySelector('#count').style.display='none';});await W(200);
 const c=await E(()=>{const C=__G.zone.circ,i=Math.round(C.n*.3);return[C.x[i],C.y[i]];});
 await E(c=>__overview(c[0],c[1],1400),c);await p.screenshot({path:'v57-ov.png',clip:{x:0,y:0,width:900,height:830}});
 console.log(JSON.stringify(errs));await b.close();})();
