const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 const name=process.argv[2],tag=process.argv[3],fs=JSON.parse(process.argv[4]);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},name);await W(300);await E(()=>__T.startRace());await W(3800);
 let k=0;for(const f of fs){await E(f=>{const C=__G.zone.circ,P=__G.P;let i;if(typeof f==='string'){const g=C.gaps[+f.slice(1)];i=Math.max(0,g.i-28);}else i=Math.round(C.n*f);const nx=Math.cos(C.h[i]),ny=Math.sin(C.h[i]);let lat=0;for(const m of (C.mid||[]))if(Math.abs(m.i-i)<40)lat=m.lat+(m.r+110);P.x=C.x[i]+nx*lat;P.y=C.y[i]+ny*lat;P.h=P.va=C.h[i];P.cs=i;P.v=0;__G.camA=P.h;for(const c of __G.rivals){c.x=1e5;}},f);await W(450);await p.screenshot({path:`${tag}-${k++}.png`,clip:{x:0,y:0,width:390,height:690}});}
 console.log(JSON.stringify(errs));await b.close();})();
