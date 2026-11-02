const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(400);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 // vistas: colocar la moto junto a la costa en varios puntos
 const L=await p.evaluate(()=>__G.zone.len);let k=0;
 for(const f of [.04,.15,.3,.45,.6,.72,.85,.95]){await p.evaluate(f=>{const P=__G.P,y=-__G.zone.len*f;let sx=0;for(let x=0;x<3000;x+=3){if(window.__dummy)break;}P.y=y;P.v=0;P.inv=5;__G.rivals.forEach(c=>c.y=y+3000);},f);
  await p.evaluate(()=>{const P=__G.P;let best=null;for(let x=20;x<2400;x+=6){if(__probe(x,P.y)){best=x;break;}}if(best!=null)P.x=best+150;},);
  await p.waitForTimeout(900);await p.screenshot({path:'v97-p'+(k++)+'.png'});}
 console.log('errs',JSON.stringify(errs));await b.close();})();
