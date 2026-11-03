const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>{localStorage.clear();});await p.reload();await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 const W=t=>p.waitForTimeout(t);
 console.log('destinos',await p.evaluate(()=>JSON.stringify(__G.zone.pgDest.map(d=>[d.n,Math.round(d.x),Math.round(d.y),__probe(d.x,d.y)]))));
 // acercarse a una moto con bandera
 await p.evaluate(()=>{const o=__G.zone.movers.find(o=>o.t==='npcjet'&&o.ch),P=__G.P;P.x=o.x;P.y=o.y+300;P.h=P.va=0;P.v=0;o.v=0;});await W(600);
 await p.screenshot({path:'v106-bandera.png'});
 await p.evaluate(()=>{const o=__G.zone.movers.find(o=>o.t==='npcjet'&&o.ch),P=__G.P;P.x=o.x+20;P.y=o.y+150;P.v=0;});await W(400);
 console.log('oferta',await p.evaluate(()=>JSON.stringify(__G.pgRace&&{st:__G.pgRace.st,d:__G.pgRace.d.n})),await p.evaluate(()=>document.querySelector('#msg').textContent));
 await p.evaluate(()=>{const R=__G.pgRace,P=__G.P;P.x=R.rv.x+30;P.y=R.rv.y+40;P.v=0;});const t0=Date.now();await W(500);
 console.log('cuenta',await p.evaluate(()=>JSON.stringify(__G.pgRace&&{st:__G.pgRace.st,path:__G.pgRace.path&&__G.pgRace.path.length,prize:__G.pgRace.prize})));
 await W(3200);console.log('estado',await p.evaluate(()=>__G.pgRace&&__G.pgRace.st));
 await W(1500);await p.screenshot({path:'v106-carrera.png'});
 // ver que el rival avanza por el camino sin quedarse atascado
 const prog=await p.evaluate(async()=>{const R=__G.pgRace,o=R.rv;const out=[];for(let i=0;i<8;i++){await new Promise(r=>setTimeout(r,1000));out.push([Math.round(o.x),Math.round(o.y),Math.round(o.v),R.i,R.path.length]);}return out;});console.log('rival',JSON.stringify(prog));
 // ganar: llevar al jugador a la meta
 const w=await p.evaluate(async()=>{const R=__G.pgRace,P=__G.P;const m0=__G.money;P.x=R.d.x;P.y=R.d.y;await new Promise(r=>setTimeout(r,300));return {m:[m0,__G.money],race:!!__G.pgRace,msg:document.querySelector('#msg').textContent};});console.log('gana',JSON.stringify(w));
 // segundo reto: dejar que gane el rival
 await p.evaluate(()=>{for(const o of __G.zone.movers)if(o.t==='npcjet'&&o.ch)o.cd=0;const o=__G.zone.movers.filter(o=>o.t==='npcjet'&&o.ch)[1],P=__G.P;P.x=o.x+20;P.y=o.y+150;P.v=0;});await W(400);
 await p.evaluate(()=>{const R=__G.pgRace,P=__G.P;P.x=R.rv.x+30;P.y=R.rv.y+40;P.v=0;});await W(4000);
 const l=await p.evaluate(async()=>{const R=__G.pgRace;if(!R)return 'sin reto';const o=R.rv;R.i=R.path.length-1;o.x=R.d.x;o.y=R.d.y+50;await new Promise(r=>setTimeout(r,300));return {race:!!__G.pgRace,msg:document.querySelector('#msg').textContent};});console.log('pierde',JSON.stringify(l));
 console.log('errs',JSON.stringify(errs));await b.close();})();
