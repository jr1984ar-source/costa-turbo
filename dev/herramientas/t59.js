const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),out={};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 const which=process.argv[2]||'palma',name=which==='palma'?'BAHÍA DE PALMA':'BAHÍA DE ALCÚDIA',spots=JSON.parse(process.argv[3]||'[0]');
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},name);await W(300);await E(()=>__T.startRace());await W(500);await p.screenshot({path:`cv-${which}-grid.png`});await W(3200);
 out.info=await E(()=>{const Zn=__G.zone,C=Zn.circ;const cnt={};for(const o of Zn.objs)cnt[o.t]=(cnt[o.t]||0)+1;return{L:C.L,N:C.n,lands:Zn.lands.length,cbig:Zn.cbig.map(b=>b.t),cnt};});
 for(const s of spots){await E(s=>{const C=__G.zone.circ,P=__G.P,i=Math.round(s/8)%C.n;P.x=C.x[i];P.y=C.y[i];P.h=P.va=C.h[i];P.cs=i;P.v=0;__G.camA=P.h;for(const c of __G.rivals){c.x=C.x[(i+40)%C.n]+Math.random()*60-30;c.y=C.y[(i+40)%C.n];c.h=c.va=C.h[(i+40)%C.n];c.cs=(i+40)%C.n;}},s);await W(400);await p.screenshot({path:`cv-${which}-${s}.png`});}
 // run a bit with throttle
 console.log(JSON.stringify(out));console.log('ERRS',JSON.stringify(errs));await b.close();})();
