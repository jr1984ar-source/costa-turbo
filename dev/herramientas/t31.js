const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1000);
 await p.evaluate(()=>{__G.free=true;__G.zi=3;__goMap();__T.startRace();});await p.waitForTimeout(3600);await p.keyboard.down('ArrowUp');await p.waitForTimeout(2500);
 const r=await p.evaluate(()=>{const st=document.getElementById('stage').getBoundingClientRect();const sy=(__G.P.y-camTop)/VH;return {frac:+((__G.P.y-(window.camTop||0))).toFixed(1)};}).catch(e=>null);
 await p.screenshot({path:'v17-race.png'});console.log(JSON.stringify(errs));await b.close();})();
