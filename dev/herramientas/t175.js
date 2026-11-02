const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1000);
 await p.evaluate(()=>{__T.newGame(0);__G.cpos=4;__G.zi=__C.CUPS[0].z[4];__goMap();});await p.waitForTimeout(300);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 const r=await p.evaluate(async()=>{const P=__G.P,out=[];const hs=__G.zone.objs.filter(o=>o.t==='heart');__T.setHp(4);out.push('antes '+__T.hpTot()/3);
  for(const h of hs){P.x=h.x;P.y=h.y+4;P.v=0;await new Promise(r=>setTimeout(r,120));out.push(Math.round(__T.hpTot()/3*100)/100);}
  return out.join(' → ')+' | corazones en el agua: '+hs.length+' | vidas en pantalla: '+__G.lives;});
 console.log(r);console.log('errs',JSON.stringify(errs));await b.close();})();
