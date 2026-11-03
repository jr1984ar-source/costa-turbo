const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>{localStorage.clear();});await p.reload();await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 const W=t=>p.waitForTimeout(t);const put=async(f,name,w=1300)=>{await p.evaluate(f);await W(w);await p.screenshot({path:'v104-'+name+'.png'});};
 await put(()=>{const P=__G.P;P.x=700;P.y=-5550;P.h=P.va=0;P.v=0;},'puerto1');
 await put(()=>{const P=__G.P;P.x=700;P.y=-6150;P.h=P.va=0;P.v=0;},'puerto2');
 await put(()=>{const P=__G.P;P.x=700;P.y=-6800;P.h=P.va=0;P.v=0;},'puerto3');
 await put(()=>{const P=__G.P,g=__G.zone.big.filter(o=>o.t==='pggas')[1];P.x=g.x-300;P.y=g.y+150;P.h=P.va=0;P.v=0;},'puerto-dcha');
 const g0=await p.evaluate(()=>{const g=__G.zone.big.find(o=>o.t==='pggas');return [g.x,g.y,__probe(g.x,g.y)];});console.log('gas',JSON.stringify(g0));
 await put(()=>{const P=__G.P,g=__G.zone.big.find(o=>o.t==='pggas');P.x=g.x;P.y=g.y+260;P.h=P.va=0;P.v=0;},'gasolinera');
 // repostar
 const r=await p.evaluate(async()=>{__G.fuel=20;__G.money=1000;const P=__G.P,g=__G.zone.big.find(o=>o.t==='pggas');P.x=g.x;P.y=g.y;P.v=0;await new Promise(r=>setTimeout(r,500));return {fuel:__G.fuel,money:__G.money,msg:document.querySelector('#msg').textContent};});console.log('repostar',JSON.stringify(r));
 // consumo
 const c=await p.evaluate(async()=>{const P=__G.P;P.x=2910;P.y=-2000;P.h=0;P.va=0;__G.fuel=100;__input.acc=true;await new Promise(r=>setTimeout(r,4000));__input.acc=false;return __G.fuel;});console.log('gasolina tras 4 s a fondo',c);
 // bares
 for(const k of ['roxy','jj']){const bb=await p.evaluate(k=>{const o=__G.zone.big.find(o=>o.t==='pgbar'&&o.k===k);return [o.bx,o.by,__probe(o.bx,o.by),__probe(o.bx+40,o.by),__probe(o.bx-40,o.by),__probe(o.bx,o.by+40),__probe(o.bx,o.by-40)];},k);console.log(k,'aro agua',JSON.stringify(bb));
  await put(new Function(`const P=__G.P,o=__G.zone.big.find(o=>o.t==='pgbar'&&o.k==='${k}');P.x=o.bx;P.y=o.by+230;P.h=P.va=0;P.v=0;`),'bar-'+k);
  const st=await p.evaluate(async k=>{const P=__G.P,o=__G.zone.big.find(o=>o.t==='pgbar'&&o.k===k);P.x=o.bx;P.y=o.by;P.v=0;await new Promise(r=>setTimeout(r,500));const scr=[...document.querySelectorAll('.screen')].filter(e=>!e.hidden).map(e=>e.id);return {mode:__G.mode,scr};},k);console.log(k,'parada',JSON.stringify(st));
  await p.screenshot({path:'v104-tienda-'+k+'.png'});
  await p.evaluate(()=>{const b=document.querySelector('#scrJJ:not([hidden]) .btns .btn, #scrRoxy:not([hidden]) .btns .btn');});
  await p.evaluate(()=>{for(const id of ['#jjOut','#rxOut']){const e=document.querySelector(id);if(e&&e.offsetParent){e.click();return id;}}});await W(600);
  console.log('tras salir',await p.evaluate(()=>__G.mode));await W(1500);console.log('sigue fuera',await p.evaluate(()=>__G.mode));}
 // Piri fondeado
 await p.evaluate(()=>{const o=__G.zone.movers.find(o=>o.t==='piripg');o.sail=0.01;});await W(300);
 await put(()=>{const o=__G.zone.movers.find(o=>o.t==='piripg'),P=__G.P;P.x=o.rx;P.y=o.ry+220;P.h=P.va=0;P.v=0;},'piri');
 const pr=await p.evaluate(async()=>{const o=__G.zone.movers.find(o=>o.t==='piripg'),P=__G.P;const t0=__G.turbo;P.x=o.rx;P.y=o.ry;P.v=0;await new Promise(r=>setTimeout(r,400));return {anch:o.anch,gift:o.gift,turbo:[t0,__G.turbo]};});console.log('piri',JSON.stringify(pr));
 console.log('errs',JSON.stringify(errs));await b.close();})();
