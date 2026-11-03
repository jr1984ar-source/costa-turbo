const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>{localStorage.clear();});await p.reload();await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 const W=t=>p.waitForTimeout(t);
 console.log('chicas',await p.evaluate(()=>JSON.stringify(__G.zone.objs.filter(o=>o.t==='pgfare').map(f=>[f.name,Math.round(f.x),Math.round(f.y),__probe(f.bx,f.by)]))));
 // ir a la primera chica (que no esté en la islita)
 await p.evaluate(()=>{const f=__G.zone.objs.filter(o=>o.t==='pgfare')[2],P=__G.P;const dx=f.bx-f.x,dy=f.by-f.y,d=Math.hypot(dx,dy);P.x=f.bx+dx/d*220;P.y=f.by+dy/d*220;P.h=Math.atan2(-dx,dy);P.va=P.h;P.v=0;});await W(1500);await p.screenshot({path:'v106-chica.png'});
 const r=await p.evaluate(async()=>{const f=__G.zone.objs.filter(o=>o.t==='pgfare')[2],P=__G.P;P.x=f.bx;P.y=f.by;P.v=0;await new Promise(r=>setTimeout(r,400));return {mis:__G.pgMis&&{n:__G.pgMis.n,pay:__G.pgMis.pay,lim:Math.round(__G.pgMis.lim)},msg:document.querySelector('#msg').textContent};});console.log('sube',JSON.stringify(r));
 await p.evaluate(()=>{const P=__G.P;P.v=0;});await W(1200);await p.screenshot({path:'v106-paseo.png'});
 const d=await p.evaluate(async()=>{const M=__G.pgMis,P=__G.P;const m0=__G.money;P.x=M.x;P.y=M.y;P.v=0;await new Promise(r=>setTimeout(r,400));return {m:[m0,__G.money],mis:!!__G.pgMis,msg:document.querySelector('#msg').textContent};});console.log('llega',JSON.stringify(d));
 console.log('errs',JSON.stringify(errs));await b.close();})();
