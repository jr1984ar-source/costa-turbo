const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1000);await p.click('#bPlay');
 const r=await p.evaluate(()=>{const out=[];for(let zi=0;zi<12;zi++){__G.free=false;__G.zi=zi;__G.lap=1;__goMap();const z=__G.zone;out.push(zi+':'+z.movers.filter(o=>o.t==='dolphin').length+'/'+z.objs.filter(o=>o.t==='jelly').length+'/'+z.objs.filter(o=>o.t==='turtle').length);}return out.join(' ');});
 console.log(r);await b.close();})();
