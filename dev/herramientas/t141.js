const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);
 await p.click('#bPlay');await W(300);await p.click('#aGo');await W(700);
 const st=(t)=>E((t)=>{const c=document.querySelector('#gPv canvas.mph');const g=c.getContext('2d');const d=g.getImageData(0,0,c.width,c.height).data;let sat=0,n=0;for(let i=0;i<d.length;i+=16){if(d[i+3]<200)continue;n++;const mx=Math.max(d[i],d[i+1],d[i+2]),mn=Math.min(d[i],d[i+1],d[i+2]);if(mx-mn>60)sat++;}
   return t+' '+JSON.stringify({moto:__M[__G.moto].id,lock:!document.querySelector('#gLock').hidden,filter:getComputedStyle(c).filter.slice(0,30),satPx:sat,n,w:c.width,h:c.height,cssH:c.getBoundingClientRect().height|0});},t);
 for(let i=0;i<10;i++){console.log(await st(''+i));if(i===2)await p.screenshot({path:'v72-avispa.png'});if(i===7)await p.screenshot({path:'v72-sombra-bloq.png'});await p.click('#gNext');await W(250);}
 await p.click('#gPaint');await W(600);await p.screenshot({path:'v72-taller-dorada.png'});await p.click('#sBack');await W(500);console.log(await st('vuelta'));
 console.log(JSON.stringify(errs));await b.close();})();
