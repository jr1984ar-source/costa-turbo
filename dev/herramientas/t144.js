const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);
 await p.click('#bPlay');await W(300);await p.click('#aGo');await W(700);
 await p.click('#gPrev');await W(500);await p.screenshot({path:'v75-garage.png'});
 console.log(await E(()=>__M.length+' '+document.querySelector('#gName').textContent+' / '+document.querySelector('#gColors').textContent+' / lock:'+!document.querySelector('#gLock').hidden+' / dots:'+document.querySelectorAll('#gDots span').length));
 await p.click('#gGo');await W(700);await p.screenshot({path:'v75-taller.png'});
 console.log(await E(()=>document.querySelector('#sName').textContent+' | '+(document.querySelector('#sTag')||{}).textContent+' | '+[...document.querySelectorAll('#scrShop button')].map(b=>b.textContent).filter(t=>/PTA|COMPRAR|ZONA/.test(t)).join(' ; ')));
 // comprarla con dinero y correr
 await E(()=>{__G.money=60000;});await E(()=>__T.renderShop());await W(300);
 const buy=await E(()=>{const bt=[...document.querySelectorAll('#scrShop button')].find(b=>/25\.000/.test(b.textContent)&&!b.disabled);if(bt){bt.click();return bt.id||bt.textContent;}return 'no';});console.log('compra',buy);await W(600);
 console.log('owns',await E(()=>__T.owns(__M[10])), 'money',await E(()=>__G.money));
 await E(()=>{__G.moto=10;__T.newGame();__G.zi=0;});await W(300);await E(()=>__T.startRace());await W(4500);await p.screenshot({path:'v75-race.png'});
 console.log(JSON.stringify(errs));await b.close();})();
