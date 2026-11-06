const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),out={};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__G.free=false;__G.zi=3;__G.lap=1;__goMap();__T.startRace();});await W(3600);
 out.a=await E(()=>({mode:__G.mode,zi:__G.zi,lap:__G.zone.lap,dol:__G.zone.movers.filter(o=>o.t==='dolphin').length}));
 await E(()=>{const d=__G.zone.movers.find(o=>o.t==='dolphin'),P=__G.P;P.y=d.y+120;P.x=d.x+30;P.v=0;window.__t0=__G.turbo;});await W(600);
 out.b=await E(()=>({mode:__G.mode,zi:__G.zi,lap:__G.zone.lap,dol:__G.zone.movers.filter(o=>o.t==='dolphin').length,msg:document.getElementById('msg').textContent}));
 console.log(JSON.stringify(out),JSON.stringify(errs));await b.close();})();
