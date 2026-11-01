const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();
const errs=[];p.on('pageerror',e=>errs.push(e.message));
for(const [q,f] of [['?mar','motos-v2-mar.png'],['?roxy','motos-v2-roxy.png']]){await p.goto('file://'+process.cwd()+'/motos-mock2.html'+q);await p.waitForTimeout(2500);await p.screenshot({path:f});}
console.log(JSON.stringify(errs));await b.close();})();
