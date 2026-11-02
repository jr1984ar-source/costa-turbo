const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(400);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 // buscar tierra delante (un islote) y chocar de frente
 const r=await p.evaluate(async()=>{const P=__G.P;let found=null;for(let y=-2000;y>-15000&&!found;y-=40){for(let x=200;x<2300;x+=10){if(!__probe(x,y)&&__probe(x,y+120)&&__probe(x-60,y+120)&&__probe(x+60,y+120)){found=[x,y];break;}}}
  if(!found)return 'no';P.x=found[0];P.y=found[1]+110;P.h=P.va=0;P.v=0;__G.rivals.forEach(c=>c.y=P.y+3000);
  __input.acc=true;await new Promise(r=>setTimeout(r,1500));const y1=P.y;
  __input.left=true;await new Promise(r=>setTimeout(r,700));__input.left=false;await new Promise(r=>setTimeout(r,1800));__input.acc=false;
  return {isla:found,choque_y:Math.round(y1),fin:[Math.round(P.x),Math.round(P.y)],avanza:Math.round(y1-P.y),v:Math.round(P.v)};});
 console.log(JSON.stringify(r),'errs',JSON.stringify(errs));await b.close();})();
