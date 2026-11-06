const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>errs.push(m.type()+':'+m.text()));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(400);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(3600);
 await p.evaluate(()=>{window.__auto=setInterval(()=>{const P=__G.P;if(!P)return;const r=__aiCtl(P,.05);__input.acc=true;__input.left=r.turn<0;__input.right=r.turn>0;},50);});
 for(let s=0;s<6;s++){await p.waitForTimeout(4000);console.log(await p.evaluate(()=>JSON.stringify({t:+__G.t.toFixed(1),mode:__G.mode,P:Math.round(-__G.P.y),x:Math.round(__G.P.x),v:Math.round(__G.P.v),riv:__G.rivals.map(c=>Math.round(-c.y)+'/'+Math.round(c.x)+'/'+Math.round(c.v)).join(' ')})));}
 console.log('errs',errs.slice(0,8).join('\n'));await b.close();})();
