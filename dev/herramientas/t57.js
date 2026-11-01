const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),out={};
 const which=process.argv[2]||'ct-wrapped.html';
 await p.goto('file://'+process.cwd()+'/'+which);await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='SA CALOBRA');__goMap();});await W(300);await E(()=>__T.startRace());await W(3600);
 out.calobra=await E(()=>{const Zn=__G.zone;const ws=[];for(let u=1500;u<Zn.len-1500;u+=500)ws.push(Math.round(Zn.rwall(-u)-Zn.shore(-u)));return{len:Zn.len,minW:Math.min(...ws),avgW:Math.round(ws.reduce((a,b)=>a+b)/ws.length),rocks:Zn.objs.filter(o=>o.t==='rock').length};});
 if(which==='ct-wrapped.html'){
 await E(()=>{__T.newGame();__G.zi=0;__goMap();});await W(300);await E(()=>__T.startRace());await W(3600);
 await E(()=>{__T.setHp(7);__T.openBar();});await W(600);await p.screenshot({path:'v38-bar.png'});
 out.bar=await E(()=>[...document.querySelectorAll('#jjList .item')].map(d=>d.textContent));
 let btn=await p.$$("#jjList .item button");await btn[2].click();await W(200);out.afterDrink=await E(()=>[__T.hpTot(),__G.turbo]);btn=await p.$$("#jjList .item button");await btn[2].click();
 await W(200);out.bar2=await E(()=>[...document.querySelectorAll('#jjList .item')].map(d=>d.textContent));await p.screenshot({path:'v38-bar2.png'});}
 console.log(JSON.stringify(out));console.log('ERRS',JSON.stringify(errs));await b.close();})();
