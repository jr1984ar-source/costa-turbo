const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='BAHAMAS');__goMap();});await W(300);await E(()=>__T.startRace());await W(3800);
 const r=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30,C=G.zone.circ;P.ai=P.ai||{re:0,tx:0};let t=0;const hist={};
  while(t<100&&G.mode==='play'){const a=__aiCirc(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__upd(dt);t+=dt;
   for(const c of __crafts()){const k=c.id;(hist[k]=hist[k]||[]).push([Math.round(t*10)/10,c.cs,Math.round(c.v),Math.round(c.lane||0)]);}}
  const out={};for(const k in hist){const h=hist[k];let stuck=null;for(let i=60;i<h.length;i+=30){if(h[i][1]===h[i-60][1]&&!stuck)stuck=h[i];}out[k]=stuck;}
  return{mid:C.mid,out};});
 console.log(JSON.stringify(r),JSON.stringify(errs));await b.close();})();
