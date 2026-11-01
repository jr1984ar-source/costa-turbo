const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();
const errs=[];p.on('pageerror',e=>errs.push(e.message));
for(const [h,f] of [['?mar','motos-1-mar.png'],['?bar','motos-2-bar-roxy.png']]){await p.goto('file://'+process.cwd()+'/motos-mock.html'+h);await p.waitForTimeout(1500);await p.screenshot({path:f});}
console.log(JSON.stringify(errs));await b.close();})();
