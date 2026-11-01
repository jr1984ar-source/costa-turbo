const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2});await ctx.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){localStorage.setItem('ct_own',JSON.stringify(['brava','oceano','solar','avispa']));sessionStorage.setItem('x',1);}}catch(e){}});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);
 await p.click('#bFree');await p.click('#aGo');const r=[];for(let i=0;i<8;i++){r.push(await p.evaluate(()=>document.getElementById('gName').textContent+':'+document.getElementById('gGo').textContent));await p.click('#gNext');}
 console.log(r.join(' | '),JSON.stringify(errs));await b.close();})();
