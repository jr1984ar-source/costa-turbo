const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext()).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message+' '+(e.stack||'').slice(0,300)));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1500);console.log(JSON.stringify(errs));await b.close();})();
