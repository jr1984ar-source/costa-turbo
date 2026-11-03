const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852}})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1500);await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(800);
 console.log(await p.evaluate(()=>{const out=[];for(const y of [-6915,-6910,-6905,-6900,-6895,-6890,-6885,-6880,-6870,-6860,-6850,-6840]){let s='';for(let x=700;x<1300;x+=15)s+=__rmV(x,y).toString(16);out.push(y+' '+s);}return out.join('\n');}));
 await b.close();})();
