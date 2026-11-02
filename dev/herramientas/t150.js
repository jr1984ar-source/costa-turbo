const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await W(1200);
 await E(()=>{__T.newGame();__G.zi=3;__goMap();});await W(300);await E(()=>__T.startRace());await W(4200);
 const isl=await E(()=>__G.zone.objs.filter(o=>o.t==='island'&&o.cut).map(o=>({x:o.x,y:o.y,rx:o.rx,ry:o.ry,cut:o.cut})));
 for(const o of isl){
  const res=await E(async o=>{const P=__G.P;P.y=o.y+o.ry+500;P.x=195;P.v=200;P.h=0;P.inv=20;__G.rivals.forEach((c,i)=>{c.y=o.y+o.ry+380+i*40;c.x=150+i*30;c.v=200;c.h=0;c.fin=0;});__input.acc=true;
   const t0=performance.now();const side={};let stuck=0;
   await new Promise(res=>{const iv=setInterval(()=>{for(const [i,c] of __G.rivals.entries()){if(Math.abs(c.y-o.y)<o.ry*.6){const inCh=o.cut<0?c.x<o.x:c.x>o.x;side[i]=inCh?'canal':'fuera';}}
     if(__G.rivals.every(c=>c.y<o.y-o.ry-80)||performance.now()-t0>12000){clearInterval(iv);res();}},60);});
   __input.acc=false;return {todos_pasan:__G.rivals.every(c=>c.y<o.y-o.ry-80),secs:Math.round((performance.now()-t0)/100)/10,side,ys:__G.rivals.map(c=>Math.round(c.y-o.y))};},o);
  console.log(o.cut<0?'izquierda':'derecha',JSON.stringify(res));}
 console.log('errs',JSON.stringify(errs));await b.close();})();
