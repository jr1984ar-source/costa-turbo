const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await W(800);
 // datos antiguos: copas contrarreloj y acción ganadas
 await E(()=>{const k=Object.keys(localStorage).find(k=>k.includes('ct_cups'))||'ct_cups';const pre=k.replace('ct_cups','');localStorage.setItem(pre+'ct_cups',JSON.stringify({costa:{won:1,t:{1:{n:1,best:5000}}},crono:{won:2,t:{1:{n:1,best:3000},2:{n:1,best:4000}}},accion:{won:1,t:{1:{n:2,best:6000}}}}));});
 const keys=await E(()=>Object.keys(localStorage).filter(k=>k.includes('ct_')).join(','));console.log('keys',keys);
 await p.reload();await W(1200);
 console.log('migrado',await E(()=>JSON.stringify(__C.cupStore.retos)),'| inicio',await E(()=>document.querySelector('#uProg').textContent+' / '+document.querySelector('#uTrof').textContent));
 await E(()=>__C.goCups());await W(400);await p.screenshot({path:'v80-copas.png',fullPage:true});
 await E(()=>document.querySelectorAll('#cuList .cupc')[2].click());await W(700);console.log('circuitos:',await E(()=>document.querySelector('#mZoneN').textContent+' | '+document.querySelector('#mZoneName').textContent+' | prog '+document.querySelectorAll('#mProg span').length));
 console.log('errs',JSON.stringify(errs));await b.close();})();
