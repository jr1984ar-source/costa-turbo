const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 const snap=async()=>{await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);return p.evaluate(()=>({jets:__G.zone.movers.filter(o=>o.t==='npcjet').slice(0,4).map(o=>[Math.round(o.x),Math.round(o.y)]),chicas:__G.zone.objs.filter(o=>o.t==='pgfare').slice(0,4).map(o=>[o.name,Math.round(o.x),Math.round(o.y)]),retos:__G.zone.movers.filter(o=>o.ch).length,nchicas:__G.zone.objs.filter(o=>o.t==='pgfare').length}));};
 const a=await snap(),c=await snap();console.log('partida 1',JSON.stringify(a));console.log('partida 2',JSON.stringify(c));
 await p.evaluate(()=>__T.goFree());await p.waitForTimeout(600);await p.evaluate(()=>{const sc=[...document.querySelectorAll('*')].filter(e=>e.offsetParent!==null&&e.scrollHeight>e.clientHeight+20&&getComputedStyle(e).overflowY!=='visible');sc.forEach(e=>e.scrollTop=e.scrollHeight);});await p.waitForTimeout(400);await p.screenshot({path:'v111-tarjeta.png'});
 console.log('errs',JSON.stringify(errs));await b.close();})();
