const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='BAHAMAS');__goMap();});await W(300);await E(()=>__T.startRace());await W(3800);
 const r=await E(()=>{const Zn=__G.zone,C=Zn.circ,i=Math.round(C.n*.22),x=C.x[i],y=C.y[i];const cnt={};for(const o of Zn.objs){if(Math.hypot(o.x-x,o.y-y)<450){cnt[o.t]=(cnt[o.t]||0)+1;}}return{cnt,ghost:!!__G.ghost,mov:Zn.movers.length};});
 console.log(JSON.stringify(r));await b.close();})();
