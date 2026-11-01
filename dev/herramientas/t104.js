const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 const runs=+process.argv[2]||1;
 for(let k=0;k<runs;k++){
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},process.argv[3]);await W(300);await E(()=>__T.startRace());await W(3800);
 const r=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30;P.ai=P.ai||{re:0,tx:0};let t=0,err=null,maxR=0,slow=[],stuck=null,lastCs=0,lastT=0;
  while(t<200&&G.mode==='play'){const a=__aiCirc(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;try{__upd(dt);}catch(e){err='upd:'+e.message+' @cs'+P.cs;break;}
   const t0=performance.now();try{__render();}catch(e){err='render:'+e.message+' @cs'+P.cs+' '+(e.stack||'').split('\n').slice(0,3).join('|');break;}const dtr=performance.now()-t0;if(dtr>maxR)maxR=dtr;if(dtr>120)slow.push([P.cs,Math.round(dtr)]);
   if(P.cs!==lastCs){lastCs=P.cs;lastT=t;}else if(t-lastT>4&&!stuck)stuck={cs:P.cs,x:Math.round(P.x),y:Math.round(P.y),v:Math.round(P.v)};t+=dt;}
  return{t:Math.round(t),mode:G.mode,err,maxR:Math.round(maxR),slow:slow.slice(0,8),stuck,prog:Math.round(P.prog),finS:G.zone.circ.finS,s0:G.zone.circ.s0,n:G.zone.circ.n,rank:P.rank,fin:!!P.fin};});
 console.log(JSON.stringify(r));
 await E(()=>{window.requestAnimationFrame=f=>setTimeout(()=>f(performance.now()),16);});await W(200);}
 console.log(JSON.stringify(errs.slice(0,5)));await b.close();})();
