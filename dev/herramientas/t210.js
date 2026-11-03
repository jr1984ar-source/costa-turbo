const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>{localStorage.clear();});await p.reload();await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 const W=t=>p.waitForTimeout(t);
 await p.evaluate(()=>{const L=__G.zone.lane,P=__G.P;P.x=L.x-21;P.y=L.y0+330;P.h=P.va=0;P.v=0;});await W(1200);await p.screenshot({path:'v109-salida.png'});
 await p.evaluate(()=>{const L=__G.zone.lane,P=__G.P;P.x=L.x-21;P.y=L.y0+70;P.v=0;});await W(600);
 console.log('estado',await p.evaluate(()=>__G.zone.drag.st));
 await W(3200);console.log('estado',await p.evaluate(()=>__G.zone.drag.st));
 // el jugador acelera a fondo con el input
 await p.evaluate(()=>{__input.acc=true;});await W(2500);await p.screenshot({path:'v109-carrera.png'});
 const r=await p.evaluate(async()=>{const rv=__G.zone.movers.filter(o=>o.t==='pgdrag');const out=[];for(let i=0;i<6;i++){await new Promise(r=>setTimeout(r,1000));out.push(rv.map(o=>[Math.round(o.y),Math.round(o.v),o.boostT>0?1:0]).concat([[Math.round(__G.P.y),Math.round(__G.P.v)]]));}return out;});
 console.log('avance',JSON.stringify(r));
 await p.evaluate(()=>{const P=__G.P,L=__G.zone.lane;P.y=L.y1+5;});await W(400);
 console.log('meta',await p.evaluate(()=>JSON.stringify({st:__G.zone.drag.st,msg:document.querySelector('#msg').textContent,money:__G.money})));
 await p.evaluate(()=>{__input.acc=false;});
 console.log('errs',JSON.stringify(errs));await b.close();})();
