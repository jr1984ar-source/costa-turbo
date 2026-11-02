const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);
 console.log(await p.evaluate(()=>{const Z=__G.zone,c={};for(const o of Z.objs)c[o.t]=(c[o.t]||0)+1;const m={};for(const o of Z.movers)m[o.t]=(m[o.t]||0)+1;return JSON.stringify({len:Z.len,lane:Z.lane,objs:c,movers:m,riv:__G.rivals.length});}));
 await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4300);await p.screenshot({path:'v99-salida.png'});
 // ir a una ola, una lancha y la recta
 const shots=[['ola',()=>{const o=__G.zone.objs.find(o=>o.t==='fwave');const P=__G.P;P.x=o.x+Math.sin(o.a)*120;P.y=o.y-Math.cos(o.a)*-120;P.h=P.va=o.a+Math.PI;}],
  ['lancha',()=>{const o=__G.zone.movers.find(o=>o.t==='skiboat');const P=__G.P;P.x=o.x+120;P.y=o.y+260;P.h=P.va=0;}],
  ['motos',()=>{const o=__G.zone.movers.find(o=>o.t==='npcjet');const P=__G.P;P.x=o.x+80;P.y=o.y+220;P.h=P.va=0;}],
  ['recta',()=>{const L=__G.zone.lane;const P=__G.P;P.x=L.x;P.y=L.y0-600;P.h=P.va=0;}]];
 for(const [n,f] of shots){await p.evaluate(f);await p.evaluate(()=>{__G.P.v=0;__G.P.inv=2;});await p.waitForTimeout(1200);await p.screenshot({path:'v99-'+n+'.png'});}
 // saltar una ola en marcha
 const j=await p.evaluate(async()=>{const P=__G.P,o=__G.zone.objs.find(o=>o.t==='fwave'&&Math.abs(Math.cos(o.a))>.8);P.x=o.x;P.y=o.y+160;P.h=P.va=0;P.v=250;P.inv=0;const j0=__G.jumps;__input.acc=true;await new Promise(r=>setTimeout(r,1400));__input.acc=false;return {saltos:__G.jumps-j0};});
 console.log('salto ola',JSON.stringify(j));
 const r2=await p.evaluate(async()=>{const P=__G.P,L=__G.zone.lane;P.x=L.x;P.y=L.mid+500;P.h=P.va=0;P.v=300;__input.acc=true;await new Promise(r=>setTimeout(r,2500));__input.acc=false;return document.querySelector('#msg').textContent;});console.log('radar:',r2);
 console.log('errs',JSON.stringify(errs));await b.close();})();
