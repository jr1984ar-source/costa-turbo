const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 const out={};
 for(const nm of ['OLAS GIGANTES','AUSTRALIA']){
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},nm);await W(300);await E(()=>__T.startRace());await W(3800);
 out[nm]=await E(()=>__G.zone.waves.map(o=>Math.round(o.gx)));
 await E(()=>{const o=__G.zone.waves[0],P=__G.P;P.x=o.gx;P.y=o.y+260;P.v=0;P.h=0;o.act=1;});await W(700);await p.screenshot({path:`v46-${nm==='AUSTRALIA'?'aus':'olas'}.png`});
 }
 // pass through gap
 const r=await E(()=>{const o=__G.zone.waves[1],P=__G.P;const h0=__T.hpTot(),s0=__G.score;P.x=o.gx+10;P.v=80;P.capT=0;P.air=0;P.z=0;__giant(P,o);const a=[h0,__T.hpTot(),P.capT,P.air>0,__G.score-s0];P.x=o.gx+18;P.capT=0;P.v=80;__giant(P,o);a.push(__T.hpTot(),P.capT);return a;});
 console.log(JSON.stringify(out),JSON.stringify(r),JSON.stringify(errs));await b.close();})();
