const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='SA CALOBRA');__goMap();});await W(300);await E(()=>__T.startRace());await W(3800);
 const geo=await E(()=>{const Zn=__G.zone,ws=[],xs=[];for(let u=1000;u<Zn.len-800;u+=250){const L=Zn.shore(-u),R=Zn.rwall(-u);ws.push(Math.round(R-L));xs.push(Math.round((L+R)/2));}return{len:Zn.len,time:__G.time,minW:Math.min(...ws),maxW:Math.max(...ws),cx:xs.slice(0,16),rocks:Zn.objs.filter(o=>o.t==='rock').length};});
 for(const f of [.12,.2,.28,.36,.5,.62]){await E(f=>{const P=__G.P;P.y=-__G.zone.len*f;P.x=(__G.zone.shore(P.y)+__G.zone.rwall(P.y))/2;P.v=0;},f);await W(350);await p.screenshot({path:`v51-${Math.round(f*100)}.png`,clip:{x:0,y:0,width:390,height:690}});}
 // autopilot con la IA de demo
 await E(()=>{const P=__G.P;P.y=40;P.x=200;P.v=0;P.h=0;P.va=0;});
 const run=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30;P.ai=P.ai||{re:0,tx:P.x,lane:0};let t=0,crashes=0,min=1e9;const t0=G.time;
  while(t<200&&G.mode==='play'){const a=__aiCtl(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__upd(dt);t+=dt;if(P.crash>.74)crashes++;}
  return{t:Math.round(t),mode:G.mode,timeLeft:Math.round(G.time),t0,crashes,y:Math.round(P.y)};});
 console.log(JSON.stringify(geo),JSON.stringify(run),JSON.stringify(errs.slice(0,3)));await b.close();})();
