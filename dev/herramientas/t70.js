const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 for(const [nm,tag] of [['CARRERA AL MAGO','mago'],['PORTALS','portals']]){
  await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},nm);await W(600);await p.screenshot({path:`v43-${tag}-map.png`});
  await E(()=>__T.startRace());await W(3800);
  const info=await E(()=>{const Zn=__G.zone,r=Zn.ring,P=__G.P;P.x=Math.min(300,Math.max(60,r.x));P.y=r.y+300;P.v=0;P.h=0;return{ring:r,len:Zn.len,piri:Zn.objs.filter(o=>o.t==='piri').map(o=>Math.round(o.y)),isl:Zn.big.filter(o=>o.t==='island').map(o=>[Math.round(o.x),Math.round(o.y)])};});
  await W(600);await p.screenshot({path:`v43-${tag}-bar.png`});
  await E(()=>{const r=__G.zone.ring,P=__G.P;P.x=r.x;P.y=r.y+30;P.v=40;P.h=0;});await W(900);
  const md=await E(()=>[__G.mode,[...document.querySelectorAll('.screen:not([hidden])')].map(e=>e.id).join()]);await p.screenshot({path:`v43-${tag}-in.png`});
  console.log(tag,JSON.stringify(info),JSON.stringify(md));
  await E(()=>{try{document.querySelector('#scrJJ:not([hidden]) .btn, #scrRoxy:not([hidden]) .btn');}catch(e){}});
 }
 console.log(JSON.stringify(errs));await b.close();})();
