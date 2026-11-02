const {chromium}=require('playwright');
async function run(ios){const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2});
 await ctx.addInitScript((ios)=>{window.__vib=[];window.__hap=0;if(ios){try{delete Navigator.prototype.vibrate;}catch(e){}Object.defineProperty(navigator,'vibrate',{value:undefined,configurable:true});}else{navigator.vibrate=ms=>{window.__vib.push(ms);return true;};}
   const oc=HTMLLabelElement.prototype.click;HTMLLabelElement.prototype.click=function(){const i=this.querySelector('input[switch]');if(i)window.__hap++;return oc.call(this);};},ios);
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);
 if(!ios)await p.screenshot({path:'v76-inicio.png'});
 await p.click('#bSet');await W(400);if(!ios)await p.screenshot({path:'v76-ajustes.png'});
 const st=()=>E(()=>['#sSnd','#sMus','#sVib'].map(s=>document.querySelector(s).classList.contains('on')?1:0).join('')+' note:'+(document.querySelector('#vibNote').textContent.slice(0,30))+' vib:'+JSON.stringify(window.__vib)+' hap:'+window.__hap);
 console.log(ios?'IOS':'ANDROID','inicial',await st());
 await p.click('#sVib');await W(200);console.log('vib off',await st());
 await p.click('#sVib');await W(200);console.log('vib on (prueba)',await st());
 await p.click('#sSnd');await p.click('#sMus');await W(200);console.log('snd/mus off',await st());
 await p.reload();await W(1200);await p.click('#bSet');await W(300);console.log('tras recargar',await st());
 await p.click('#sSnd');await p.click('#sMus');await W(200);
 await p.click('#setBk');await W(500);console.log('vuelta inicio visible',await E(()=>!document.querySelector('#scrTitle').hidden));
 // carrera: chocar con la orilla
 await E(()=>{window.__vib.length=0;window.__hap=0;__T.newGame();__G.zi=0;});await W(300);await E(()=>__T.startRace());await W(4200);
 await E(()=>{const P=__G.P;P.x=-100;P.v=300;P.air=0;});await W(300);
 console.log('golpe orilla',await E(()=>'vib:'+JSON.stringify(window.__vib)+' hap:'+window.__hap));
 // pausa sigue funcionando
 await E(()=>document.querySelector('#btnPause').click());await W(300);console.log('pausa',await E(()=>document.querySelector('#pSnd').textContent+' / '+document.querySelector('#pMus').textContent));
 console.log('errs',JSON.stringify(errs));await b.close();}
(async()=>{await run(false);await run(true);})();
