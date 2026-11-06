const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},'BAHAMAS');await W(300);await E(()=>__T.startRace());await W(3800);
 const r=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30,L=G.zone.lands,C=G.zone.circ;let t=0,hits=[];
  while(t<150&&G.mode==='play'){const a=__aiCirc(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__upd(dt);
   for(const c of G.rivals){if(c.air<=0&&__landIn(L,c.x,c.y)&&hits.length<6){const i=c.cs,lat=(c.x-C.x[i])*Math.cos(C.h[i])+(c.y-C.y[i])*Math.sin(C.h[i]);hits.push({cs:i,lat:Math.round(lat),wl:Math.round(C.wl[i]),wr:Math.round(C.wr[i]),lane:Math.round(c.lane),id:c.id});}}t+=dt;}
  return{hits,mid:C.mid.map(m=>[m.i,Math.round(m.lat),Math.round(m.r)]),nar:C.nar,huge:C.huge};});
 console.log(JSON.stringify(r));await b.close();})();
