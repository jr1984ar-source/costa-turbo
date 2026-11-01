const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 const out={};
 for(const n of ['CARRERA AL MAGO','PORTALS']){await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},n);await W(300);await E(()=>__T.startRace());await W(3800);
  out[n]=await E(()=>{const Zn=__G.zone,o=Zn.objs.find(o=>o.t==='piri');return{len:Zn.len,piri:[Math.round(o.x),Math.round(-o.y),+(-o.y/Zn.len).toFixed(2)],bar:[Math.round(-Zn.ring.y),+(-Zn.ring.y/Zn.len).toFixed(2)],isl:Zn.big.filter(b=>b.t==='island').map(b=>[Math.round(b.x),Math.round(-b.y),b.rx,b.ry])};});
  if(n==='CARRERA AL MAGO'){await E(()=>{const o=__G.zone.objs.find(o=>o.t==='piri'),P=__G.P;P.x=o.x;P.y=o.y+280;P.v=0;P.h=0;});await W(600);await p.screenshot({path:'v49-mago.png'});}}
 console.log(JSON.stringify(out),JSON.stringify(errs));await b.close();})();
