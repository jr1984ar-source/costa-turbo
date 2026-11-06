const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext()).newPage();await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(800);
 const r=await p.evaluate(()=>__M.map(m=>({id:m.id,name:m.name,ui:m.ui,sk:m.sk,side:m.side?{deck:m.side.deck,hull:m.side.hull,stripe:m.side.stripe,seat:m.side.seat,hood:m.side.hood}:null})));
 console.log(JSON.stringify(r));await b.close();})();
