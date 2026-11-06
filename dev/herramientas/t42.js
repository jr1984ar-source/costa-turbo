const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1000);await p.click('#bPlay');
 const r=await p.evaluate(()=>{__G.free=false;__G.zi=3;__G.lap=1;__goMap();const z=__G.zone;return {lap:z.lap,m:z.movers.map(o=>o.t).join(','),j:z.objs.filter(o=>o.t==='jelly'||o.t==='turtle').length};});
 console.log(JSON.stringify(r),JSON.stringify(errs));await b.close();})();
