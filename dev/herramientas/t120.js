const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),sh=(n,full)=>p.screenshot({path:`v63-${n}.png`,fullPage:!!full});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);await E(()=>{__G.money=200000;});
 await p.click('#bShop');await W(500);await sh('taller');
 for(let i=0;i<9;i++){await p.click('#sNext');await W(120);} await W(300);await sh('taller-dorada');
 const info=await E(()=>({name:document.querySelector('#sName').textContent,model:document.querySelector('#sModel').textContent,img:!document.querySelector('#sPv img.mph').hidden,main:document.querySelector('#sMain').textContent}));console.log(JSON.stringify(info));
 await p.click('#sMain');await W(300);
 await p.click('#sGear');await W(600);await sh('equipo-casco');
 for(const c of ['gog','glove','vest','suit']){await p.click(`#eTabs [data-c="${c}"]`);await W(300);await sh('equipo-'+c);}
 await p.click('#eTabs [data-c="gog"]');await W(200);
 await E(()=>{const rows=[...document.querySelectorAll('#eList .prt')];rows[rows.length-1].querySelector('.btn').click();});await W(200);
 await E(()=>{document.querySelector('#eSw [data-st="#1e5eff"]').click();});await W(200);await E(()=>{document.querySelector('#eSw [data-ln="gold"]').click();});await W(300);await sh('equipo-gog2');
 await p.click('#eTabs [data-c="helm"]');await W(200);await E(()=>{const rows=[...document.querySelectorAll('#eList .prt')];rows[2].querySelector('.btn').click();});await W(200);
 await p.click('#eTabs [data-c="glove"]');await W(200);await E(()=>{const rows=[...document.querySelectorAll('#eList .prt')];rows[1].querySelector('.btn').click();});await W(300);await sh('equipo-final');
 console.log(JSON.stringify(await E(()=>localStorage.getItem('ct_gear'))));
 await p.click('#eBack');await W(300);await p.click('#sBack');await W(400);await sh('inicio');
 await E(()=>{__T.newGame();});await W(300);await p.click('#bPlay').catch(()=>{});
 console.log(JSON.stringify(errs));await b.close();})();
