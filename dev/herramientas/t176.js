const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);await p.screenshot({path:'v95-mapa.png'});
 console.log('zona',await p.evaluate(()=>__G.zone.Z.name+' len '+__G.zone.len+' objs '+__G.zone.objs.length+' realMap '+__G.zone.realMap));
 await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);await p.screenshot({path:'v95-salida.png'});
 const L=await p.evaluate(()=>__G.zone.len);
 // vistas en varios puntos
 const pts=[.08,.2,.33,.47,.6,.74,.88];let k=0;
 for(const f of pts){await p.evaluate(f=>{const P=__G.P,y=-__G.zone.len*f;let x=330;for(let xx=380;xx>40;xx-=4){if(window.__rmok?0:1){}}P.y=y;P.x=__G.rivals[0]?P.x:P.x;P.v=0;P.inv=3;__G.rivals.forEach(c=>{c.y=y+600;});},f);
  await p.evaluate(()=>{const P=__G.P;for(let xx=360;xx>30;xx-=6){const ok=[0,-40,40].every(d=>!window.__rl||true);}});await p.waitForTimeout(700);await p.screenshot({path:'v95-p'+(k++)+'.png'});}
 console.log('errs',JSON.stringify(errs));await b.close();})();
