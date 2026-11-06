const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:844}});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('http://localhost:8765/');await p.waitForTimeout(1500);
 const a=await p.evaluate(async()=>{const r=await navigator.serviceWorker.getRegistration();return {sw:!!r,ver:document.getElementById('verTag').textContent};});
 await p.reload();await p.waitForTimeout(1200);const ctl=await p.evaluate(()=>!!navigator.serviceWorker.controller);
 await ctx.setOffline(true);await p.reload();await p.waitForTimeout(1200);const off=await p.evaluate(()=>document.getElementById('verTag')?document.getElementById('verTag').textContent:'NO');
 console.log(JSON.stringify({a,ctl,off}),JSON.stringify(errs));await b.close();})();
