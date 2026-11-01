const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 const name=process.argv[2],tag=process.argv[3],times=JSON.parse(process.argv[4]);
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},name);await W(300);await E(()=>__T.startRace());await W(1200);await p.screenshot({path:`rt-${tag}-grid.png`});await W(2600);
 await E(()=>{const P=__G.P;P.ai=P.ai||{re:0,tx:0};window.__ap=setInterval(()=>{if(__G.mode!=='play')return;const a=__aiCirc(P,1/60);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;},16);});
 let last=0;for(const t of times){await W((t-last)*1000);last=t;await p.screenshot({path:`rt-${tag}-${t}.png`});}
 console.log('ERRS',JSON.stringify(errs.slice(0,5)));await b.close();})();
