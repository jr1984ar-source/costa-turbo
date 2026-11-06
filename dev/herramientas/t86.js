const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 for(let run=0;run<4;run++){
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='BAHAMAS');__goMap();});await W(300);await E(()=>__T.startRace());await W(3800);
 const r=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30,C=G.zone.circ;P.ai=P.ai||{re:0,tx:0};let t=0;const last={},log=[];
  while(t<90&&G.mode==='play'){const a=__aiCirc(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__upd(dt);t+=dt;
   for(const c of G.rivals){const l=last[c.id]||(last[c.id]={cs:c.cs,t:t});if(c.cs!==l.cs){l.cs=c.cs;l.t=t;}else if(t-l.t>3&&!l.logged){l.logged=1;const m=C.mid.find(m=>Math.abs(m.i-c.cs)<40);const i=c.cs,nx=Math.cos(C.h[i]),ny=Math.sin(C.h[i]),lat=(c.x-C.x[i])*nx+(c.y-C.y[i])*ny;
     log.push({id:c.id,cs:c.cs,lat:Math.round(lat),lane:Math.round(c.lane),v:Math.round(c.v),h:+(c.h-C.h[i]).toFixed(2),mid:m?{i:m.i,lat:Math.round(m.lat),r:Math.round(m.r)}:null,flip:c._flipT});}}}
  return log;});
 console.log(JSON.stringify(r));
 await E(()=>{window.requestAnimationFrame=f=>setTimeout(()=>f(performance.now()),16);});await W(200);}
 console.log(JSON.stringify(errs));await b.close();})();
