const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:1})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(400);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(3600);
 await p.evaluate(()=>{const P=__G.P;P.y=-8400;P.x=300;P.inv=99;__G.rivals.forEach((c,i)=>{c.y=-8550-i*30;c.x=100+i*60;c.v=200;c.h=0;});window.__auto=setInterval(()=>{__input.acc=false;},100);});
 for(let s=0;s<8;s++){await p.waitForTimeout(1000);console.log(await p.evaluate(()=>__G.rivals.map(c=>Math.round(c.x)+','+Math.round(c.y)+' v'+Math.round(c.v)+' tx'+Math.round(c.ai.tx)).join(' | ')));}
 await b.close();})();
