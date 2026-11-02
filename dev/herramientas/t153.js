const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await W(1200);
 await E(()=>{__T.newGame();__G.zi=8;__goMap();});await W(300);await E(()=>__T.startRace());await W(4200);
 // los rivales recorren un tramo con barcas: ¿se atascan?
 const res=await E(async()=>{const P=__G.P,O=__G.zone.objs,fb=O.filter(o=>o.t==='fboat');const f=fb[Math.floor(fb.length/2)];P.y=f.y+700;P.x=195;P.v=200;P.inv=30;__G.rivals.forEach((c,i)=>{c.y=f.y+500+i*40;c.x=120+i*35;c.v=200;c.h=0;});__input.acc=true;const t0=performance.now();
  await new Promise(r=>{const iv=setInterval(()=>{if(__G.rivals.every(c=>c.y<f.y-200)||performance.now()-t0>9000){clearInterval(iv);r();}},60);});__input.acc=false;return {pasan:__G.rivals.every(c=>c.y<f.y-200),secs:Math.round((performance.now()-t0)/100)/10,ys:__G.rivals.map(c=>Math.round(c.y-f.y))};});
 console.log('barcas:',JSON.stringify(res),'errs',JSON.stringify(errs));await b.close();})();
