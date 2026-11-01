const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='SA CALOBRA');__goMap();});await W(300);await E(()=>__T.startRace());await W(3700);
 await E(()=>{const P=__G.P;P.ai=P.ai||{re:0,tx:0};window.__ap=setInterval(()=>{if(__G.mode!=='play')return;const a=__aiCirc(P,1/60);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__input.turbo=false;},16);});
 await W(1500);
 for(let k=0;k<70;k++){await p.screenshot({path:`gif/f${String(k).padStart(3,'0')}.png`,clip:{x:0,y:0,width:390,height:690}});await W(60);}
 await b.close();})();
