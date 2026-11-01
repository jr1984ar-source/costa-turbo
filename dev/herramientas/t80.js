const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='LAS RAMPAS');__goMap();});await W(300);await E(()=>__T.startRace());await W(3800);
 const info=await E(()=>{const c={};for(const o of __G.zone.objs)if(o.t==='ramp'||o.t==='cramp'){const k=o.t+':'+(o.mega?'mega':o.sz||'-');c[k]=(c[k]||0)+1;}return c;});
 console.log(JSON.stringify(info),JSON.stringify(errs));await b.close();})();
