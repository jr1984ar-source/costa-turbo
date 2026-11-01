const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),sh=(n,full)=>p.screenshot({path:`gear-${n}.png`,fullPage:!!full});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);
 await E(()=>{__G.money=200000;});
 await p.click('#bShop');await W(400);await p.click('#sGear');await W(400);await sh('helm',true);
 // probar y comprar
 await p.click('#eList .prt.gr:nth-of-type(9)');await W(300);await sh('try');
 await E(()=>{const rows=[...document.querySelectorAll('#eList .prt')];rows[rows.length-1].querySelector('.btn').click();});await W(300);
 await p.click('#eTabs [data-c="vest"]');await W(300);await sh('vest',true);
 await E(()=>{const rows=[...document.querySelectorAll('#eList .prt')];rows[2].querySelector('.btn').click();});await W(300);
 await p.click('#eTabs [data-c="suit"]');await W(300);await sh('suit',true);
 await E(()=>{const rows=[...document.querySelectorAll('#eList .prt')];rows[3].querySelector('.btn').click();});await W(300);await sh('done');
 await p.click('#eBack');await W(300);await p.click('#sBack');await W(400);await sh('title');
 console.log(JSON.stringify(await E(()=>localStorage.getItem('ct_gear'))));
 console.log(JSON.stringify(errs));await b.close();})();
