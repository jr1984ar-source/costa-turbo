const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:1280,height:800},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.addInitScript(()=>{const mk=()=>({pressed:false,value:0});window.__gp={connected:true,id:'Xbox fake',buttons:Array.from({length:17},mk),axes:[0,0,0,0],vibrationActuator:{playEffect:(...a)=>{window.__rumble=(window.__rumble||0)+1;return Promise.resolve();}}};Object.defineProperty(navigator,'getGamepads',{value:()=>[window.__gp],configurable:true});
  window.__press=async(i,ms=120)=>{__gp.buttons[i]={pressed:true,value:1};await new Promise(r=>setTimeout(r,ms));__gp.buttons[i]={pressed:false,value:0};await new Promise(r=>setTimeout(r,80));};});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>localStorage.clear());await p.reload();await p.waitForTimeout(1500);
 const vis=()=>p.evaluate(()=>[...document.querySelectorAll('.screen')].filter(e=>!e.hidden).map(e=>e.id).join(','));
 console.log('inicio',await vis());
 await p.evaluate(()=>__press(13));const f1=await p.evaluate(()=>{const e=document.querySelector('.gpf');return e&&(e.id||e.textContent.trim().slice(0,20));});console.log('foco',f1);
 await p.evaluate(()=>__press(13));const f2=await p.evaluate(()=>{const e=document.querySelector('.gpf');return e&&(e.id||e.textContent.trim().slice(0,20));});console.log('foco abajo',f2);
 await p.screenshot({path:'v112-menu.png'});
 // ir a ajustes con el ratón y activar ocultar controles con el mando
 await p.evaluate(()=>document.querySelector('#bSet').click());await p.waitForTimeout(300);console.log('pantalla',await vis());
 for(let i=0;i<4;i++)await p.evaluate(()=>__press(13));const f3=await p.evaluate(()=>{const e=document.querySelector('.gpf');return e&&e.id;});console.log('foco ajustes',f3);
 await p.evaluate(()=>{if(document.querySelector('.gpf')?.id!=='sCtl'){}});
 await p.evaluate(()=>document.querySelector('#sCtl').click());console.log('ocultar',await p.evaluate(()=>[document.querySelector('#sCtl').classList.contains('on'),localStorage.getItem('ct_hidectl')]));
 await p.screenshot({path:'v112-ajustes.png'});
 await p.evaluate(()=>__press(1));await p.waitForTimeout(300);console.log('B vuelve a',await vis());
 // jugar: modo libre
 await p.evaluate(()=>{__T.startFree(22);});await p.waitForTimeout(500);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4300);
 console.log('sin controles',await p.evaluate(()=>[document.querySelector('#app').classList.contains('nopads'),Math.round(document.querySelector('#stage').getBoundingClientRect().height)]));
 await p.evaluate(()=>{__gp.buttons[1]={pressed:true,value:1};});await p.waitForTimeout(1500);console.log('B acelera, velocidad',await p.evaluate(()=>Math.round(__G.P.v)));
 await p.evaluate(()=>{__gp.axes[0]=-1;});await p.waitForTimeout(400);console.log('gira',await p.evaluate(()=>+__G.P.h.toFixed(2)));await p.evaluate(()=>{__gp.axes[0]=0;});
 const t0=await p.evaluate(()=>__G.turbo);await p.evaluate(()=>__press(2));console.log('X turbo',t0,'->',await p.evaluate(()=>[__G.turbo,__G.P.boostT>0]));
 await p.evaluate(()=>{__gp.buttons[0]={pressed:true,value:1};});await p.waitForTimeout(300);console.log('A derrape',await p.evaluate(()=>__input.drift));await p.evaluate(()=>{__gp.buttons[0]={pressed:false,value:0};__gp.buttons[1]={pressed:false,value:0};});
 await p.screenshot({path:'v112-juego.png'});
 await p.evaluate(()=>__press(9));console.log('START',await p.evaluate(()=>__G.mode));await p.evaluate(()=>__press(9));console.log('START otra vez',await p.evaluate(()=>__G.mode));
 console.log('errs',JSON.stringify(errs));await b.close();})();
