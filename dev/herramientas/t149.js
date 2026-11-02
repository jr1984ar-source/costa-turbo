const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await W(1200);
 await E(()=>__T.startFree(3));await W(400);await E(()=>__T.startRace());await W(4200);
 const isl=await E(()=>__G.zone.objs.filter(o=>o.t==='island'&&o.cut).map(o=>({x:o.x,y:o.y,rx:o.rx,ry:o.ry,cut:o.cut})));
 for(const [k,o] of isl.entries()){
  // vista: jugador quieto debajo de la isla
  await E(o=>{const P=__G.P,Zn=__G.zone,y0=o.y+o.ry+120;const wall=o.cut<0?Zn.shore(y0):Zn.rwall(y0),edge=o.cut<0?o.x-o.rx-10:o.x+o.rx+10;P.x=(wall+edge)/2;P.y=o.y+o.ry+120;P.v=0;P.h=0;P.va=0;P.inv=3;for(const c of __G.rivals){c.y=P.y+900;}},o);
  await W(500);await p.screenshot({path:'v78-atajo'+k+'.png'});
  // cruzar el canal recto acelerando
  const r=await E(async o=>{const P=__G.P;P._isl=0;let bumps=0,minV=999;__input.acc=true;const y0=P.y;const t0=performance.now();
    await new Promise(res=>{const iv=setInterval(()=>{if(P._isl>0.6)bumps++;if(P.y<o.y)minV=Math.min(minV,P.v);if(P.y<o.y-o.ry-60||performance.now()-t0>7000){clearInterval(iv);res();}},50);});
    __input.acc=false;return {pasado:P.y<o.y-o.ry-60,bumps,x:Math.round(P.x),dy:Math.round(y0-P.y),turbo:__G.turbo};},o);
  console.log('atajo',k,o.cut<0?'izquierda':'derecha',JSON.stringify(r));
 }
 console.log('errs',JSON.stringify(errs));await b.close();})();
