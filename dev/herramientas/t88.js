const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='BAHAMAS');__goMap();});await W(300);
 await E(()=>{window.__popLog=[];const G=__G;const orig=G.pops.push;});
 await E(()=>__T.startRace());await W(1200);
 const r=await E(()=>{const P=__G.P,C=__G.zone.circ;return{pops:__G.pops.map(q=>q.txt),mode:__G.mode,P:[Math.round(P.x),Math.round(P.y),P.cs,Math.round(P.off||0)],lx:P._lx,offT:P._offT,bumpT:P._bumpT};});
 console.log(JSON.stringify(r));await b.close();})();
