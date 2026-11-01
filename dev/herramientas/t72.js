const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='OLAS GIGANTES');__goMap();});await W(300);await E(()=>__T.startRace());await W(3800);
 const r1=await E(()=>{const P=__G.P;P.v=50;P.capT=0;P.air=0;P.z=0;const h0=__T.hpTot();__giant(P);return[h0,__T.hpTot(),__G.lives,__G.dmg,document.querySelector('#msg').textContent,P.capT];});
 await W(400);await p.screenshot({path:'v45-volcado.png'});
 // fast jump: no damage
 const r2=await E(()=>{const P=__G.P;P.capT=0;P.v=P.st.maxV;P.va=0;const h0=__T.hpTot();__giant(P);return[h0,__T.hpTot()];});
 // capsize with 2/3 left -> game over
 const r3=await E(()=>{const P=__G.P;P.air=0;P.z=0;P.capT=0;P.v=40;__T.setHp(2);__giant(P);return[__T.hpTot(),__G.mode];});await W(1500);
 const r4=await E(()=>[...document.querySelectorAll('.screen:not([hidden])')].map(e=>e.id).join());
 console.log(JSON.stringify({r1,r2,r3,r4}),JSON.stringify(errs));await b.close();})();
