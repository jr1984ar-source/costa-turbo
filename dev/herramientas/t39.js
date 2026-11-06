const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1000);await p.click('#bPlay');await p.waitForTimeout(200);
 await p.evaluate(()=>{__G.free=true;__G.zi=0;__G.lives=2;__goMap();__T.startRace();});await p.waitForTimeout(1500);
 const bb=await p.locator('#lives').boundingBox();await p.screenshot({path:'z-hearts.png',clip:{x:bb.x-60,y:bb.y-10,width:bb.width+120,height:bb.height+20}});
 console.log(JSON.stringify(errs));await b.close();})();
