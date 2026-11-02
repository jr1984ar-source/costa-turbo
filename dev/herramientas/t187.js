const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(400);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);await p.screenshot({path:'v96-salida.png'});
 console.log(await p.evaluate(()=>'len '+__G.zone.len+' P '+Math.round(__G.P.x)+','+Math.round(__G.P.y)+' objs '+__G.zone.objs.length));
 // piloto automático y capturas cada 6 s
 await p.evaluate(()=>{window.__auto=setInterval(()=>{const P=__G.P;if(!P)return;const r=__aiCtl(P,.05);__input.acc=true;__input.left=r.turn<0;__input.right=r.turn>0;if(!r.turn)P.h*=.88;},50);});
 for(let k=0;k<14;k++){await p.waitForTimeout(6000);const st=await p.evaluate(()=>({mode:__G.mode,P:Math.round(-__G.P.y),x:Math.round(__G.P.x),riv:__G.rivals.map(c=>Math.round(-c.y)).join(','),fin:__G.rivals.filter(c=>c.fin).length}));console.log(JSON.stringify(st));
  if(k<10)await p.screenshot({path:'v96-r'+k+'.png'});if(st.mode!=='play')break;}
 console.log('errs',JSON.stringify(errs));await b.close();})();
