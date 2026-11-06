const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);
 await p.click('#bPlay');await W(300);await p.click('#aGo');await W(700);
 await p.click('#gNext');await W(300);await p.click('#gNext');await W(400);
 const st=(t)=>E((t)=>{const c=document.querySelector('#gPv canvas.mph');const g=c.getContext('2d');const d=g.getImageData(0,0,c.width,c.height).data;let sat=0,n=0;for(let i=0;i<d.length;i+=16){if(d[i+3]<200)continue;n++;const mx=Math.max(d[i],d[i+1],d[i+2]),mn=Math.min(d[i],d[i+1],d[i+2]);if(mx-mn>60)sat++;}
   return t+' '+JSON.stringify({moto:__M[__G.moto].id,lk:document.querySelector('#gPv').classList.contains('lk'),filter:getComputedStyle(c).filter.slice(0,40),hidden:c.hidden,cvHidden:document.querySelector('#gMoto').hidden,satPx:sat,n,w:c.width,paint:(()=>{try{return JSON.stringify(window.__gearT.sideOf(__M[__G.moto]).hull)}catch(e){return e.message}})()});},t);
 console.log(await st('inicio'));await p.screenshot({path:'t139-a.png'});
 await p.click('#gPaint');await W(600);console.log('taller abierto');
 await p.click('#sBack');await W(600);console.log(await st('vuelta1'));
 await p.click('#gPaint');await W(600);await p.click('#sBack');await W(600);console.log(await st('vuelta2'));
 await p.click('#gGo');await W(800);console.log('elegir ->',await E(()=>[...document.querySelectorAll('.scr:not([hidden])')].map(s=>s.id).join(',')));
 await p.screenshot({path:'t139-b.png'});
 console.log(JSON.stringify(errs));await b.close();})();
