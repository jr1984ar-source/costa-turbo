const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 for(const [tag,name] of [['palma','BAHÍA DE PALMA'],['alc','BAHÍA DE ALCÚDIA']]){
  await E(n=>{__G.free=true;__G.zi=__Z.findIndex(z=>z.name===n);__goMap();__T.startRace();},name);await W(3600);
  await E(tag=>{const C=__G.zone.circ,P=__G.P;let bi=0;for(let i=0;i<C.n;i++){if(tag==='palma'?C.y[i]<C.y[bi]:C.x[i]<C.x[bi])bi=i;}P.x=C.x[bi];P.y=C.y[bi];P.h=P.va=C.h[bi];P.cs=bi;P.v=0;__G.camA=P.h;},tag);await W(700);await p.screenshot({path:`c-${tag}-land.png`});}
 console.log(JSON.stringify(errs));await b.close();})();
