const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch();
 for(const [w,h,tag] of [[390,844,'ip'],[820,1180,'ipad'],[1180,820,'ipadL']]){
 const p=await (await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:2,hasTouch:true,isMobile:true})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1500);await p.screenshot({path:`s-${tag}-title.png`});
 await p.click('#bPlay');await p.waitForTimeout(600);await p.screenshot({path:`s-${tag}-pilot.png`});
 await p.click('#aGo');await p.waitForTimeout(500);await p.screenshot({path:`s-${tag}-garage.png`});
 await p.click('#gGo');await p.waitForTimeout(500);await p.evaluate(()=>{__G.zi=7;__goMap();});await p.waitForTimeout(400);await p.screenshot({path:`s-${tag}-map.png`});
 await p.click('#mGo');await p.waitForTimeout(4000);await p.screenshot({path:`s-${tag}-race.png`});
 console.log(tag,JSON.stringify(errs));}
 await b.close();})();
