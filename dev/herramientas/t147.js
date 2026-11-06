const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:900,height:2200},deviceScaleFactor:1})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);
 await p.evaluate(()=>__T.goFree());await p.waitForTimeout(2500);
 const el=await p.$('#fGrid');await el.screenshot({path:'portadas-22.png'});await b.close();})();
