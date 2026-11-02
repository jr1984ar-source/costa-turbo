const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await W(1200);
 await E(()=>{__T.newGame();__G.zi=3;__goMap();});await W(300);await E(()=>__T.startRace());await W(4200);
 const groups=await E(()=>{const g={};for(const o of __G.zone.objs.filter(o=>o.t==='island'&&o.grp)){(g[o.grp]=g[o.grp]||[]).push(o);}return Object.values(g).map(a=>{a.sort((p,q)=>p.y-q.y);return{side:a[0].cut,x:a[0].x,top:a[0].y-a[0].ry,bot:a[a.length-1].y+a[a.length-1].ry};});});
 for(const g of groups){
  const res=await E(async g=>{const P=__G.P;P.y=g.bot+500;P.x=195;P.v=200;P.h=0;P.inv=40;__G.rivals.forEach((c,i)=>{c.y=g.bot+380+i*40;c.x=120+i*35;c.v=200;c.h=0;c.fin=0;c.crash=0;});__input.acc=true;
   const t0=performance.now(),side={},cr=new Set();
   await new Promise(res=>{const iv=setInterval(()=>{const mid=(g.top+g.bot)/2;for(const [i,c] of __G.rivals.entries()){if(c.crash>0)cr.add(i);if(Math.abs(c.y-mid)<300){side[i]=(g.side<0?c.x<g.x:c.x>g.x)?'estrecho':'ancho';}}
     if(__G.rivals.every(c=>c.y<g.top-80)||performance.now()-t0>25000){clearInterval(iv);res();}},60);});
   __input.acc=false;return {todos_pasan:__G.rivals.every(c=>c.y<g.top-80),secs:Math.round((performance.now()-t0)/100)/10,side,choques:[...cr]};},g);
  console.log(g.side<0?'izquierda':'derecha',JSON.stringify(res));}
 console.log('errs',JSON.stringify(errs));await b.close();})();
