const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>{localStorage.clear();});await p.reload();await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);
 await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);for(const tt of ['coin','heart','gearbox']){await p.evaluate(t=>{window.TT=t},tt);
 const r=await p.evaluate(async()=>{const o=__G.zone.objs.find(o=>o.t===(window.TT||"gearbox"));const P=__G.P;const out={box:[o.x,o.y,o.id,__probe(o.x,o.y)],demo:__G.demo,isP:P.isP};P.x=o.x;P.y=o.y+10;P.h=P.va=0;P.v=0;await new Promise(r=>setTimeout(r,300));out.after=[P.x,P.y,!!o.got];out.msg=document.querySelector('#msg').textContent;out.own=JSON.parse(localStorage.getItem('ct_gear')||'{}').own;return out;});
 console.log(JSON.stringify(r));}console.log('errs',JSON.stringify(errs));await b.close();})();
