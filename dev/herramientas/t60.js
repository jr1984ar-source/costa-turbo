const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:900,height:1000},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 const which=process.argv[2]||'palma',name=which==='palma'?'BAHÍA DE PALMA':'BAHÍA DE ALCÚDIA',views=JSON.parse(process.argv[3]);
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},name);await W(300);await E(()=>__T.startRace());await W(1500);
 await E(()=>{window.requestAnimationFrame=()=>0;document.querySelector('#hud').hidden=true;document.querySelector('#count').style.display='none';});await W(200);
 let k=0;for(const v of views){await E(v=>__overview(v[0],v[1],v[2]),v);await p.screenshot({path:`ov-${which}-${k++}.png`});}
 console.log('ERRS',JSON.stringify(errs));await b.close();})();
