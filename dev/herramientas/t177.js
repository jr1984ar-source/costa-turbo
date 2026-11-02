const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(400);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(3600);
 // el jugador va en piloto automático como un rival
 await p.evaluate(()=>{window.__auto=setInterval(()=>{const P=__G.P;if(!P)return;P.isP=false;const r=__aiCtl(P,.05);P.isP=true;__input.acc=true;__input.left=r.turn<0;__input.right=r.turn>0;},50);});
 const t0=Date.now();let last=null;
 for(let s=0;s<14;s++){await p.waitForTimeout(5000);const st=await p.evaluate(()=>({P:Math.round(-__G.P.y),mode:__G.mode,riv:__G.rivals.map(c=>Math.round(-c.y)),fin:__G.rivals.map(c=>c.fin|0),len:__G.zone.len,crash:__G._crashes|0}));
  console.log(Math.round((Date.now()-t0)/1000)+'s',JSON.stringify(st));if(st.mode!=='play'&&st.mode!=='count')break;}
 console.log('errs',JSON.stringify(errs));await b.close();})();
