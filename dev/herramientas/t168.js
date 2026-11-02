const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1000);await p.evaluate(()=>__C.goCups());await p.waitForTimeout(400);
 console.log(await p.evaluate(()=>[...document.querySelectorAll('#cuList .cupc b')].map(b=>b.textContent).join(' | ')));
 await p.screenshot({path:'v86-copas.png',fullPage:true});await b.close();})();
