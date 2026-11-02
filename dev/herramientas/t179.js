const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:1})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(400);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(3600);
 console.log(await p.evaluate(()=>JSON.stringify(__G.zone.objs.filter(o=>o.y<-5900&&o.y>-6150).map(o=>o.t+'@'+Math.round(o.x)+','+Math.round(o.y)))));
 await p.evaluate(()=>{const c=__G.rivals[0];c.y=-5900;c.x=150;c.v=150;c.h=0;c.crash=0;c.inv=0;__G.P.y=-5700;__G.P.inv=99;__G.rivals.slice(1).forEach(r=>r.y=-3000);});
 for(let k=0;k<12;k++){await p.waitForTimeout(400);console.log(await p.evaluate(()=>{const c=__G.rivals[0];return JSON.stringify({x:Math.round(c.x),y:Math.round(c.y),v:Math.round(c.v),h:+c.h.toFixed(2),air:+(c.air||0).toFixed(2),crash:+(c.crash||0).toFixed(2),stuck:+(c.stuckT||0).toFixed(2),cap:+(c.capT||0).toFixed(2),pit:c.pit|0,tx:Math.round(c.ai.tx),fin:c.fin|0});}));}
 await b.close();})();
