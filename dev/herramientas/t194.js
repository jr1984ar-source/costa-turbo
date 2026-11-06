const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:1})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(500);
 console.log(await p.evaluate(()=>JSON.stringify({x:__G.P.x,y:__G.P.y,lane:__G.zone.lane})));await b.close();})();
