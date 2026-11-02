const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),txt=s=>E(s=>{const e=document.querySelector(s);return e?e.textContent:null},s);
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await W(1200);
 console.log('inicio:',await txt('#uProg'),'|',await txt('#uTrof'));
 await p.click('#bPlay');await W(300);await p.click('#aGo');await W(600);await p.click('#gGo');await W(600);
 console.log('pantalla:',await E(()=>[...document.querySelectorAll('.screen')].find(s=>!s.hidden).id));
 await p.screenshot({path:'v77-copas.png',fullPage:true});
 await E(()=>document.querySelectorAll('#cuList .cupc')[4].click());await W(300);console.log('final bloqueada sigue en copas:',await E(()=>!document.querySelector('#scrCups').hidden));
 await E(()=>document.querySelectorAll('#cuList .cupc')[0].click());await W(800);
 console.log('mapa:',await txt('#mZoneN'),'|',await txt('#mZoneName'),'| prog',await E(()=>document.querySelectorAll('#mProg span').length));
 await p.screenshot({path:'v77-mapa.png'});
 for(let i=0;i<8;i++){if(await E(()=>!document.querySelector('#scrChamp').hidden))break;await E(()=>__C.zoneWin());await W(300);console.log(' res',i+1,await txt('#rTitle'),'|',await txt('#rSub'));await E(()=>document.querySelector('#rGo').click());await W(700);
   const scr=await E(()=>[...document.querySelectorAll('.screen')].find(s=>!s.hidden).id);if(scr==='scrMap')console.log('   siguiente:',await txt('#mZoneN'),'|',await txt('#mZoneName'));else console.log('   pantalla',scr);}
 console.log('copa:',await txt('#cH'),'|',await txt('#cInfo'),'|',await txt('#cTrofTxt'));await p.screenshot({path:'v77-ganada.png'});
 console.log('store',JSON.stringify(await E(()=>__C.cupStore)));
 await p.click('#cNext');await W(500);
 await E(()=>{for(const id of ['paraiso','circuitos','retos'])__C.cupS(id).won=1;__C.renderCups();});await W(300);
 console.log('final abierta:',await E(()=>__C.finalOpen()));await p.screenshot({path:'v77-copas2.png',fullPage:true});
 // jugar la final y una carrera real en Paraíso
 await E(()=>document.querySelectorAll('#cuList .cupc')[4].click());await W(700);console.log('final mapa:',await txt('#mZoneN'),'|',await txt('#mZoneName'));
 await E(()=>__T.startRace());await W(4500);console.log('pill final:',await E(()=>document.querySelector('#zonePill').textContent));
 await E(()=>{__C.goCups();});await W(300);await E(()=>document.querySelectorAll('#cuList .cupc')[1].click());await W(700);await E(()=>__T.startRace());await W(4500);
 console.log('pill paraiso:',await E(()=>document.querySelector('#zonePill').textContent),'rivales',await E(()=>__G.rivals.length));
 await E(()=>{__C.renderTrof();});await E(()=>{document.querySelectorAll('.screen').forEach(s=>s.hidden=s.id!=='scrTrof');document.querySelector('#hud').hidden=true;});await W(400);await p.screenshot({path:'v77-trofeos.png',fullPage:true});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await W(1000);console.log('inicio tras recargar:',await txt('#uProg'),'|',await txt('#uTrof'));
 console.log('errs',JSON.stringify(errs));await b.close();})();
