const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1000);
 console.log(await p.evaluate(()=>{const r=[];for(const C of __C.CUPS)r.push(C.n+': '+C.z.map(z=>__Z[z].name).join(', '));return r.join('\n');}));
 console.log('libre:',await p.evaluate(()=>{__T.goFree?0:0;return document.querySelectorAll('#fGrid .fz').length;}));
 await p.evaluate(()=>__T.goFree());await p.waitForTimeout(500);console.log('portadas libre:',await p.evaluate(()=>[...document.querySelectorAll('#fGrid .fz')].map(b=>b.getAttribute('aria-label')).join(' | ')));
 console.log('errs',JSON.stringify(errs));await b.close();})();
