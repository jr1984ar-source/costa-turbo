const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 const nz=await E(()=>__Z.length);const out=[];
 for(let zi=0;zi<nz;zi++){await E(zi=>{__T.newGame();__G.zi=zi;__goMap();},zi);await W(200);await E(()=>__T.startRace());await W(3700);
  const r=await E(()=>{const raf=window.requestAnimationFrame;window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30;let t=0,err=null;P.ai=P.ai||{re:0,tx:0};
   try{while(t<12&&G.mode==='play'){const a=__aiCtl(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__upd(dt);if(((t*30)|0)%10===0){__pop(P.x,P.y-40,'¡PRUEBA!','#ffc93c');__render();}t+=dt;}__render();}catch(e){err=e.message+' '+(e.stack||'').split('\n')[1];}
   window.requestAnimationFrame=raf;return{z:G.zone.Z.name,t:Math.round(t),mode:G.mode,err,pops:G.pops.length};});
  out.push(r);await E(()=>{window.requestAnimationFrame=f=>setTimeout(()=>f(performance.now()),16);});}
 for(const r of out)console.log(JSON.stringify(r));console.log('errs',JSON.stringify(errs.slice(0,5)));await b.close();})();
