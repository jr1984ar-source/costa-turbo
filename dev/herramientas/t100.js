const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 const zn=process.argv[2]||'BAHAMAS',tag=process.argv[3]||'bplay',shots=JSON.parse(process.argv[4]||'[2,5,9,14,20,27]');
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},zn);await W(300);await E(()=>__T.startRace());await W(3800);
 await E(()=>{window.requestAnimationFrame=()=>0;window.__t=0;});
 let k=0;for(const st of shots){await E(st=>{const G=__G,P=G.P,dt=1/30;while(window.__t<st&&G.mode==='play'){const a=__aiCirc(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__upd(dt);window.__t+=dt;}__render();},st);
  await p.screenshot({path:`${tag}-${k++}.png`});}
 console.log(JSON.stringify(errs));await b.close();})();
