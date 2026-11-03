const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>{localStorage.clear();});await p.reload();await p.waitForTimeout(1500);
 const W=t=>p.waitForTimeout(t);
 await p.evaluate(()=>{__G.money=5000;__T.goShop('title');});await W(500);await p.click('#sPaint');await W(900);
 await p.screenshot({path:'v107-pintura.png'});
 // elegir dorsal, vinilo llamas amarillo y logo JJ
 await p.evaluate(()=>{const chips=[...document.querySelectorAll('#pRows .chip')];const f=t=>chips.find(c=>c.textContent===t);for(let i=0;i<7;i++)f('+').click();f('LLAMAS').click();f("JJ'S SPORTS").click();const sw=[...document.querySelectorAll('#pRows .prow')].find(r=>r.querySelector('span').textContent==='COLOR DEL VINILO').querySelectorAll('.sw')[6];sw.click();});
 await W(900);await p.screenshot({path:'v107-pintura2.png'});
 await p.evaluate(()=>{const r=[...document.querySelectorAll('#pRows .prow')].find(r=>r.querySelector('span').textContent==='DORSAL');r.scrollIntoView({block:'center'});});await W(300);await p.screenshot({path:'v107-pintura3.png'});
 const saved=await p.evaluate(()=>{const b=document.querySelector('#pSave');const t=b.textContent;b.click();return {btn:t,money:__G.money,paint:JSON.parse(localStorage.getItem('ct_paint')||'{}')};});console.log('guardar',JSON.stringify(saved));
 // vista desde arriba en carrera
 await p.evaluate(()=>{__T.startFree(22);});await W(500);await p.evaluate(()=>__T.startRace());await W(4500);
 const P=await p.evaluate(()=>{const c=document.createElement('canvas');c.width=128;c.height=272;const g=c.getContext('2d');g.scale(4,4);g.translate(16,34);__gearT.drawJet(g,__gearT.playerSk());return c.toDataURL();});require('fs').writeFileSync('v107-arriba.png',Buffer.from(P.split(',')[1],'base64'));
 await p.screenshot({path:'v107-carrera.png'});
 console.log('errs',JSON.stringify(errs));await b.close();})();
