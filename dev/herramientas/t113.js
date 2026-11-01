const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 for(const zn of [process.argv[2]]){await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},zn);await W(300);await E(()=>__T.startRace());await W(3800);
 const r=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30,L=G.zone.lands;let t=0,inL={},bumps=0,fin=0;
  while(t<150&&G.mode==='play'){const a=__aiCirc(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;const bt=P._bumpT;__upd(dt);if(P._bumpT>0&&!(bt>0))bumps++;
   for(const c of G.rivals){if(c.air<=0&&__landIn(L,c.x,c.y)){inL[c.cs]=(inL[c.cs]||0)+1;}if(c._sandT>0||(G.zone.circ.banks||[]).some(B=>c.x>B.bb[0]&&c.x<B.bb[2]&&c.y>B.bb[1]&&c.y<B.bb[3]&&__polyIn(B.pts,c.x,c.y)))window.__bk=(window.__bk||0)+1;}t+=dt;}
  return{bankFrames:window.__bk||0,t:Math.round(t),mode:G.mode,bumps,rank:P.rank,rivFin:G.rivals.filter(c=>c.fin).length,inLand:Object.entries(inL).slice(0,12),gaps:(G.zone.circ.gaps||[]).map(g=>g.i)};});
 console.log(zn,JSON.stringify(r));}
 console.log(JSON.stringify(errs));await b.close();})();
