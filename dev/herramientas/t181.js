const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:1})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(400);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(3600);
 await p.evaluate(()=>{window.__auto=setInterval(()=>{const P=__G.P;if(!P)return;const r=__aiCtl(P,.05);__input.acc=true;__input.left=r.turn<0;__input.right=r.turn>0;},50);});
 for(let s=0;s<10;s++){await p.waitForTimeout(2000);console.log(await p.evaluate(()=>{const c=__G.rivals[1];return JSON.stringify({x:Math.round(c.x),y:Math.round(c.y),v:Math.round(c.v),h:+c.h.toFixed(2),crash:+(c.crash||0).toFixed(2),cap:+(c.capT||0).toFixed(2),stuck:+(c.stuckT||0).toFixed(2),tx:Math.round(c.ai.tx),air:+(c.air||0).toFixed(2),re:+c.ai.re.toFixed(2),sk:c.skill});}));}
 await b.close();})();
