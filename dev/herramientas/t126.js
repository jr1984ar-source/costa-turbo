const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),sh=n=>p.screenshot({path:`v65-${n}.png`});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);await E(()=>{__G.money=50000;});
 await p.click('#bShop');await W(700);await sh('taller');
 for(let i=0;i<2;i++){await p.click('#sNext');await W(200);} await W(400);await sh('taller-avispa');
 await p.click('#sPrev');await p.click('#sPrev');await W(300);
 await p.click('#sPaint');await W(700);await sh('pintar');
 // pintar: casco arriba azul, tapa amarilla
 await E(()=>{const rows=[...document.querySelectorAll('#pRows .prow')];const pick=(r,i)=>{const s=rows[r].querySelectorAll('.sw');s[i].click();};pick(1,10);pick(2,6);pick(4,3);});await W(500);await sh('pintar2');
 await p.click('#pSave');await W(500);await sh('taller-pintada');
 await p.click('#sBack');await W(300);await p.click('#bPlay');await W(300);await p.click('#aGo');await W(700);await sh('garage');
 await E(()=>{__T.newGame();__G.zi=0;});await W(300);await E(()=>__T.startRace());await W(4500);await p.screenshot({path:'v65-race.png',clip:{x:120,y:450,width:150,height:200}});
 console.log(JSON.stringify(errs));await b.close();})();
