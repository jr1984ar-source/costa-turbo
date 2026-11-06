const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3})).newPage();
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 for(const [name,spots] of [['EL PUERTO',[0]],['FORMENTERA',[0]],['BAHÍA DE PALMA',[60,1400]],['BAHÍA DE ALCÚDIA',[60,700]]]){
  await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},name);await W(300);await E(()=>__T.startRace());await W(3800);
  for(const s of spots){const ms=await E(s=>{window.requestAnimationFrame=()=>0;const G=__G,C=G.zone.circ,P=G.P;if(C){const i=Math.round(s/8*C.n/(C.L/8))%C.n;P.x=C.x[i];P.y=C.y[i];P.h=P.va=C.h[i];G.camA=P.h;}else{P.y=-3000;}
   for(let k=0;k<5;k++)__render();const t0=performance.now();for(let k=0;k<60;k++){G.t+=1/60;__render();}return((performance.now()-t0)/60).toFixed(2);},s);console.log(name,s,ms+' ms/frame');}
  await E(()=>{window.requestAnimationFrame=f=>setTimeout(()=>f(performance.now()),16);});}
 await b.close();})();
