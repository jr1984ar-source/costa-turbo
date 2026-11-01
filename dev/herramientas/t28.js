const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);
 await E(()=>{__G.free=true;__G.zi=6;__goMap();__T.startRace();});await W(3600);
 await E(()=>{const o=__G.zone.big.filter(o=>o.t==='pass')[1],r=__G.zone.objs.find(r=>r.t==='ramp'&&r.sand&&Math.abs(r.y-o.y)<200),P=__G.P;P.x=r.x;P.y=r.y+50;P.v=190;P.h=0;P.va=0;window.__o=o;});await p.keyboard.down('ArrowUp');
 const res=[];for(let i=0;i<10;i++){await W(200);res.push(await E(()=>Math.round(__G.P.y-__o.y)+'/'+(+(__G.P.stuckT||0)).toFixed(1)+'/z'+(+__G.P.z).toFixed(1)));if(i===4)await p.screenshot({path:'w-14-stuck.png'});}
 console.log(res.join(' '),JSON.stringify(errs));await b.close();})();
