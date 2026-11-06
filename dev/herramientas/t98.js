const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 for(const name of process.argv.slice(2)){
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},name);await W(300);await E(()=>__T.startRace());await W(3800);
 const r=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30;P.ai=P.ai||{re:0,tx:0};let t=0,n=0,sum=0,slow=0,ts=[];
  while(t<25&&G.mode==='play'){const a=G.zone.circ?__aiCirc(P,dt):{thr:true,turn:0};__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__upd(dt);const t0=performance.now();__render();const d=performance.now()-t0;ts.push(d);sum+=d;n++;if(d>120)slow++;t+=dt;}
  ts.sort((a,b)=>a-b);return{avg:+(sum/n).toFixed(1),med:+ts[n>>1].toFixed(1),p90:+ts[Math.floor(n*.9)].toFixed(1),slow,n};});
 console.log(name,JSON.stringify(r));
 await E(()=>{window.requestAnimationFrame=f=>setTimeout(()=>f(performance.now()),16);});await W(200);}
 console.log(JSON.stringify(errs.slice(0,3)));await b.close();})();
