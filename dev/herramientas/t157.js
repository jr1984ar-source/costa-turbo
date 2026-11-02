const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await W(1200);
 await E(()=>{__T.newGame();__G.zi=3;__goMap();});await W(300);await E(()=>__T.startRace());await W(4200);
 const groups=await E(()=>{const g={};for(const o of __G.zone.objs.filter(o=>o.t==='island'&&o.grp)){(g[o.grp]=g[o.grp]||[]).push({x:o.x,y:o.y,rx:o.rx,ry:o.ry,cut:o.cut});}return Object.values(g).map(a=>{a.sort((p,q)=>p.y-q.y);return{side:a[0].cut,x:a[0].x,rx:a[0].rx,top:a[0].y-a[0].ry,bot:a[a.length-1].y+a[a.length-1].ry,n:a.length};});});
 console.log(JSON.stringify(groups.map(g=>({side:g.side,len:Math.round(g.bot-g.top),n:g.n}))));
 let k=0;for(const g of groups){
  // capturas: entrada y mitad
  for(const [lbl,yy] of [['entrada',g.bot+200],['mitad',(g.top+g.bot)/2+300]]){await E(([g,yy])=>{const P=__G.P,Zn=__G.zone,wall=g.side<0?Zn.shore(yy):Zn.rwall(yy);P.x=(wall+(g.side<0?g.x-g.rx-10:g.x+g.rx+10))/2;P.y=yy;P.v=0;P.h=0;P.va=0;P.inv=3;__G.rivals.forEach(c=>c.y=P.y+1500);},[g,yy]);await W(500);await p.screenshot({path:`v80-gc-${k}-${lbl}.png`});}
  // conducir por el camino estrecho
  const r=await E(async g=>{const P=__G.P,Zn=__G.zone,y0=g.bot+150;const wall=g.side<0?Zn.shore(y0):Zn.rwall(y0);P.x=(wall+(g.side<0?g.x-g.rx-10:g.x+g.rx+10))/2;P.y=y0;P.h=0;P.v=150;P.inv=0;P.crash=0;let bumps=0,crash=0,jumps=__G.jumps;__input.acc=true;const t0=performance.now();
    await new Promise(res=>{const iv=setInterval(()=>{if(P._isl>0.6)bumps++;if(P.crash>0)crash++;
      // piloto automático: mantener el centro del canal
      const w=g.side<0?Zn.shore(P.y-60):Zn.rwall(P.y-60),edge=g.side<0?g.x-g.rx-10:g.x+g.rx+10,tx=(w+edge)/2;__input.left=P.x>tx+6;__input.right=P.x<tx-6;
      if(P.y<g.top-80||performance.now()-t0>16000){clearInterval(iv);res();}},40);});
    __input.acc=false;__input.left=__input.right=false;return {pasa:P.y<g.top-80,bumps,crash,saltos:__G.jumps-jumps,secs:Math.round((performance.now()-t0)/100)/10};},g);
  console.log('camino estrecho',g.side<0?'izq':'der',JSON.stringify(r));k++;}
 console.log('errs',JSON.stringify(errs));await b.close();})();
