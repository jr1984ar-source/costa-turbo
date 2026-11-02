const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1000);
 const out=await p.evaluate(()=>{const res=[];for(const ci of [0,1,2,3,4]){const C=__C.CUPS[ci];for(const lap of [0,2,4]){const row=[];for(let pos=0;pos<C.z.length;pos++){__G.cup=ci;__G.cpos=pos;__G.lap=lap;__G.free=false;__G.demo=false;__G.zi=C.z[pos];__goMap();row.push(__G.zone.objs.filter(o=>o.t==='heart').length);}res.push(C.n+' dif '+(lap+1)+': '+row.join(' '));}}
  __G.free=true;__T.startFree(3);res.push('carrera libre: '+__G.zone.objs.filter(o=>o.t==='heart').length);return res.join('\n');});
 console.log(out);console.log('errs',JSON.stringify(errs));await b.close();})();
