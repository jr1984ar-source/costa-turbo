const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(400);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(3600);
 const r=await p.evaluate(()=>{const out=[];for(let y=-5900;y>=-6250;y-=25){let row='';for(let x=0;x<390;x+=10){const v=window.__rmV?0:0;}out.push(y);}return out.length;});
 await p.evaluate(()=>{const P=__G.P;P.y=-5950;P.x=250;P.v=0;P.inv=5;__G.rivals.forEach(c=>c.y=-5000);});await p.waitForTimeout(800);await p.screenshot({path:'v95-atasco.png'});
 await b.close();})();
