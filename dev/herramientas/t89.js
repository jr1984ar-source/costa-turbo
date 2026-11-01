const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='BAHAMAS');__goMap();});await W(300);await E(()=>__T.startRace());await W(3800);
 const fs=[.06,.15,.25,.35,.45,.6];let k=0;
 for(const f of fs){await E(f=>{const C=__G.zone.circ,P=__G.P,i=Math.round(C.n*f);const nx=Math.cos(C.h[i]),ny=Math.sin(C.h[i]);let lat=0;for(const m of C.mid)if(Math.abs(m.i-i)<40)lat=m.lat+(m.r+110);P.x=C.x[i]+nx*lat;P.y=C.y[i]+ny*lat;P.h=P.va=C.h[i];P.cs=i;P.v=0;__G.camA=P.h;for(const c of __G.rivals){const j=Math.min(C.n-1,i+30);c.x=C.x[j]+(Math.random()-.5)*120;c.y=C.y[j];c.h=c.va=C.h[j];c.cs=j;}},f);await W(450);await p.screenshot({path:`v57b-${k++}.png`,clip:{x:0,y:0,width:390,height:690}});}
 console.log(JSON.stringify(errs));await b.close();})();
