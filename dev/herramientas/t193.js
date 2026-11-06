const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>{localStorage.clear();});await p.reload();await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);
 await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 const r=await p.evaluate(async()=>{const o=__G.zone.objs.find(o=>o.t==='gearbox');const P=__G.P;P.x=o.x;P.y=o.y+60;P.h=P.va=0;P.v=150;__input.acc=true;const tr=[];for(let i=0;i<8;i++){await new Promise(r=>setTimeout(r,100));tr.push([Math.round(P.x),Math.round(P.y),Math.round(P.v),+P.h.toFixed(2),!!o.got]);}__input.acc=false;return {box:[o.x,o.y],tr};});
 console.log(JSON.stringify(r));await b.close();})();
