const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>__T.goFree());await p.waitForTimeout(600);
 const t=await p.evaluate(()=>{const sc=[...document.querySelectorAll('*')].filter(e=>e.offsetParent!==null&&e.scrollHeight>e.clientHeight+20&&getComputedStyle(e).overflowY!=='visible');sc.forEach(e=>e.scrollTop=e.scrollHeight);return sc.map(e=>e.id||e.className);});
 console.log(JSON.stringify(t));await p.waitForTimeout(400);await p.screenshot({path:'v103-menu2.png'});console.log('errs',JSON.stringify(errs));await b.close();})();
