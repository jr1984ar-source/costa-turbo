const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),sh=n=>p.screenshot({path:`tr-${n}.png`});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);await sh('title');
 await p.click('#bTrof');await W(300);await sh('room0');await p.click('#trBk');await W(200);
 const out=[];
 for(let lv=1;lv<=5;lv++){await E(()=>{__T.newGame();},null);await W(300);out.push(await E(()=>({lap:__G.lap,dif:__difLv(),map:document.querySelector('#mZoneN').textContent})));
  await E(s=>{__G.score=s;__champEnd();},10000+lv*1234);await W(300);if(lv===1||lv===5)await sh('champ'+lv);}
 await p.click('#cTr');await W(300);await sh('room5');await p.click('#trBk');await W(200);out.push(await E(()=>({vis:[...document.querySelectorAll('.screen')].filter(s=>!s.hidden).map(s=>s.id),next:document.querySelector('#cNext').textContent,store:localStorage.getItem('ct_trof'),dif:localStorage.getItem('ct_dif')})));
 await p.click('#cNext');await W(300);out.push(await E(()=>document.querySelector('#mZoneN').textContent));
 // migración: campeón antiguo sin trofeos
 await E(()=>{localStorage.removeItem('ct_trof');localStorage.removeItem('ct_dif');localStorage.setItem('ct_medals',JSON.stringify({campeon:1700000000000}));});await p.reload();await W(1200);
 out.push(await E(()=>({trof:localStorage.getItem('ct_trof'),dif:localStorage.getItem('ct_dif'),prog:document.querySelector('#uProg').textContent})));
 for(const o of out)console.log(JSON.stringify(o));console.log(JSON.stringify(errs));await b.close();})();
