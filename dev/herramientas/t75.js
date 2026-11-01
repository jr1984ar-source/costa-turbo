const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 const names=['EL PUERTO','LA CALA','CARRERA AL MAGO','GRAN CARRERA','PERSECUCIÓN','OLAS GIGANTES','CARRERA ES TRENC','CARRERA SAN TELM','FORMENTOR','SA CALOBRA','CABRERA','PORTALS','FORMENTERA','BAHAMAS','AUSTRALIA','ES VEDRÀ'];
 let k=0;for(const n of names){await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},n);await W(200);await E(()=>__T.startRace());await W(3600);
  await E(()=>{const P=__G.P;P.y=-__G.zone.len*.22;P.v=0;});await W(400);await p.screenshot({path:`w48-${k++}.png`,clip:{x:0,y:0,width:390,height:690}});}
 console.log(JSON.stringify(errs));await b.close();})();
