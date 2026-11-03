const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>{localStorage.clear();});await p.reload();await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 const W=t=>p.waitForTimeout(t);
 console.log(await p.evaluate(()=>{const c={};for(const o of __G.zone.objs)if(['pgboat','sail','barca','yacht','pgbar'].includes(o.t))c[o.t+(o.k!=null?o.k:'')]=(c[o.t+(o.k!=null?o.k:'')]||0)+1;const pol=__G.zone.movers.filter(o=>o.t==='pgpol').length;const jj=__G.zone.objs.find(o=>o.t==='pgbar'&&o.k==='jj');return JSON.stringify({c,pol,jj:[Math.round(jj.x),Math.round(jj.y),Math.round(jj.bx),Math.round(jj.by),__probe(jj.bx,jj.by)],start:[__G.P.x,__G.P.y]});}));
 const shot=async(f,n,w=1300)=>{await p.evaluate(f);await W(w);await p.screenshot({path:'v108-'+n+'.png'});};
 await shot(()=>{const P=__G.P,o=__G.zone.objs.find(o=>o.t==='pgbar'&&o.k==='jj');P.x=o.bx+40;P.y=o.by+250;P.h=P.va=0;P.v=0;},'jj',3200);
 const bts=await p.evaluate(()=>__G.zone.objs.filter(o=>o.t==='pgboat').map(o=>[o.x,o.y,o.k]));
 for(const k of [2,3,0]){const o=bts.find(q=>q[2]===k);await shot(new Function(`const P=__G.P;P.x=${o[0]};P.y=${o[1]}+200;P.h=P.va=0;P.v=0;`),'barco'+k,900);}
 await shot(()=>{const P=__G.P,o=__G.zone.movers.find(o=>o.t==='pgpol');P.x=o.x;P.y=o.y+230;P.h=P.va=0;P.v=0;},'policia',600);
 const pol=await p.evaluate(async()=>{const P=__G.P,o=__G.zone.movers.find(o=>o.t==='pgpol');const a=[o.x,o.y];await new Promise(r=>setTimeout(r,2000));return [Math.round(Math.hypot(o.x-a[0],o.y-a[1]))];});console.log('policía se mueve',pol);
 console.log('errs',JSON.stringify(errs));await b.close();})();
