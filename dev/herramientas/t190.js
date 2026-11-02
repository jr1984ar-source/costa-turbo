const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(400);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 // conducir 40 s girando a ratos por el mapa
 await p.evaluate(()=>{let t=0;window.__drv=setInterval(()=>{t+=.1;__input.acc=true;__input.turbo=t%6<1;const s=Math.sin(t*.4);__input.left=s>.6;__input.right=s<-.6;},100);});
 let k=0;for(let s=0;s<8;s++){await p.waitForTimeout(5000);console.log(await p.evaluate(()=>JSON.stringify({mode:__G.mode,x:Math.round(__G.P.x),y:Math.round(__G.P.y),v:Math.round(__G.P.v),saltos:__G.jumps,vidas:__G.lives,choques:__G._crashes|0})));if(s%2)await p.screenshot({path:'v99-d'+(k++)+'.png'});}
 console.log('errs',JSON.stringify(errs));await b.close();})();
