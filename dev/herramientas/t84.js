const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='BAHAMAS');__goMap();});await W(600);await p.screenshot({path:'v57-map.png'});
 await E(()=>__T.startRace());await W(1200);await p.screenshot({path:'v57-start.png'});await W(2600);
 const info=await E(()=>{const C=__G.zone.circ;return{L:C.L,N:C.n,time:__G.time,bonus:C.bonus,finS:C.finS};});
 for(const f of [.08,.2,.33,.5,.7,.97]){await E(f=>{const C=__G.zone.circ,P=__G.P,i=Math.round(C.n*f)%C.n;P.x=C.x[i];P.y=C.y[i];P.h=P.va=C.h[i];P.cs=i;P.v=0;__G.camA=P.h;},f);await W(400);await p.screenshot({path:`v57-${Math.round(f*100)}.png`});}
 // wall test: drive into the wall
 const wall=await E(()=>{const C=__G.zone.circ,P=__G.P,i=Math.round(C.n*.3);P.x=C.x[i];P.y=C.y[i];P.cs=i;P.h=P.va=C.h[i]+Math.PI/2;P.v=300;window.requestAnimationFrame=()=>0;for(let k=0;k<60;k++){__input.acc=true;__upd(1/30);}__input.acc=false;return{off:Math.round(P.off),v:Math.round(P.v)};});
 await E(()=>{window.requestAnimationFrame=f=>setTimeout(()=>f(performance.now()),16);});
 // full run with autopilot from start
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='BAHAMAS');__goMap();});await W(300);await E(()=>__T.startRace());await W(3800);
 const run=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30;P.ai=P.ai||{re:0,tx:0};let t=0,maxOff=0,bumps=0;
  while(t<200&&G.mode==='play'){const a=__aiCirc(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__upd(dt);t+=dt;maxOff=Math.max(maxOff,P.off||0);if(P._bumpT>.49)bumps++;}
  return{t:Math.round(t),mode:G.mode,timeLeft:Math.round(G.time),prog:Math.round(P.prog),maxOff:Math.round(maxOff),bumps,fin:P.fin};});
 console.log(JSON.stringify({info,wall,run}),JSON.stringify(errs.slice(0,4)));await b.close();})();
