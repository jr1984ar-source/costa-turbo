const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>{localStorage.clear();});await p.reload();await p.waitForTimeout(1500);
 const W=t=>p.waitForTimeout(t);
 await p.evaluate(()=>__T.goShop('title'));await W(500);await p.click('#sGear');await W(600);
 await p.evaluate(()=>{const rows=[...document.querySelectorAll('#eList .prt')];rows[rows.length-1].scrollIntoView({block:'end'});});await W(300);await p.screenshot({path:'v101-equipo-oculto.png'});
 // ya conseguido
 await p.evaluate(()=>{const g=JSON.parse(localStorage.getItem('ct_gear')||'{}');});
 await p.evaluate(()=>{__T.startFree(22);});await W(400);await p.evaluate(()=>__T.startRace());await W(4200);
 await p.evaluate(async()=>{const o=__G.zone.objs.find(o=>o.t==='gearbox'&&o.gold);const P=__G.P;P.x=o.x;P.y=o.y+12;P.v=0;await new Promise(r=>setTimeout(r,400));});
 await p.evaluate(()=>{const P=__G.P,o=__G.zone.objs.find(o=>o.t==='pgbar'&&o.k==='jj');P.x=o.x+40;P.y=o.y+300;P.h=P.va=0;P.v=0;});await W(3500);await p.screenshot({path:'v101-jj2.png'});
 await p.evaluate(()=>{const P=__G.P,o=__G.zone.objs.find(o=>o.t==='pgbar'&&o.k==='roxy');P.x=o.x;P.y=o.y+330;P.h=P.va=0;P.v=0;});await W(1200);await p.screenshot({path:'v101-roxy2.png'});
 await p.evaluate(()=>{const P=__G.P,o=__G.zone.movers.find(o=>o.t==='piripg');P.x=o.x-Math.sin(o.h)*-200;P.y=o.y+Math.cos(o.h)*200;P.h=o.h;P.va=o.h;P.v=0;});await W(700);await p.screenshot({path:'v101-piri2.png'});
 await p.evaluate(()=>__T.goShop('title'));await W(500);await p.click('#sGear');await W(600);
 await p.evaluate(()=>{const rows=[...document.querySelectorAll('#eList .prt')];rows[rows.length-1].querySelector('.btn').click();});await W(500);
 await p.evaluate(()=>{const rows=[...document.querySelectorAll('#eList .prt')];rows[rows.length-1].scrollIntoView({block:'end'});});await W(300);await p.screenshot({path:'v101-equipo-dorado.png'});
 console.log('errs',JSON.stringify(errs));await b.close();})();
