const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await W(1200);
 for(const zi of [0,3]){
  await E(zi=>{__T.newGame();__G.zi=zi;__goMap();},zi);await W(300);await E(()=>__T.startRace());await W(4200);
  const r=await E(async()=>{const P=__G.P,Zn=__G.zone,ring=Zn.ring,pr=Zn.pier;P.y=ring.y+1300;P.x=pr.x1+60;P.v=150;P.inv=40;__G.pitSlots=0;
    __G.rivals.forEach((c,i)=>{c.y=ring.y+1100+i*45;c.x=pr.x1+40-i*10;c.v=170;c.h=0;c.pit=0;c.fin=0;c.crash=0;});let crashes=0;const seen=new Set();__input.acc=true;const t0=performance.now();
    await new Promise(res=>{const iv=setInterval(()=>{__G.rivals.forEach((c,i)=>{if(c.crash>0)seen.add(i);});if(__G.rivals.every(c=>c.pit===3||c.y<ring.y-300)||performance.now()-t0>20000){clearInterval(iv);res();}},50);});
    __input.acc=false;return {pit:__G.rivals.map(c=>c.pit|0),choques:[...seen],secs:Math.round((performance.now()-t0)/100)/10};});
  console.log('zona',zi,JSON.stringify(r));
  // jugador entra en la cala y para
  const bar=await E(async()=>{const P=__G.P,ring=__G.zone.ring;__G.barUsed=false;P.x=ring.x+4;P.y=ring.y+20;P.v=40;P.h=0;await new Promise(r=>setTimeout(r,400));return __G.mode;});console.log('  bar abre:',bar);
  await E(()=>{const b=document.querySelector('#jjOut')||document.querySelector('#rxOut');b&&b.click();});await W(300);
 }
 console.log('errs',JSON.stringify(errs));await b.close();})();
