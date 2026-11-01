const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1000);
 const r=await p.evaluate(()=>{__G.free=true;__G.zi=6;__goMap();const Z=__G.zone;return {passes:Z.big.filter(o=>o.t==='pass').map(o=>({y:o.y,gx:o.gx,w:o.wedge})),ramps:Z.objs.filter(o=>o.t==='ramp').map(o=>({y:Math.round(o.y),x:Math.round(o.x),s:o.sand}))};});
 console.log(JSON.stringify(r),JSON.stringify(errs));await b.close();})();
