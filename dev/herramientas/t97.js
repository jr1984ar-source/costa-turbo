const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3})).newPage();
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 const name=process.argv[2]||'BAHAMAS';
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},name);await W(300);await E(()=>__T.startRace());await W(3800);
 const r=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,Zn=G.zone,C=Zn.circ,P=G.P;const out={};
  for(const f of[.02,.3]){const i=Math.round(C.n*f);P.x=C.x[i];P.y=C.y[i];P.h=P.va=C.h[i];P.cs=i;G.camA=P.h;
   const meas=()=>{for(let k=0;k<2;k++)__render();const t0=performance.now();for(let k=0;k<10;k++){G.t+=1/60;__render();}return+((performance.now()-t0)/10).toFixed(1);};
   const sv={lands:Zn.lands,cbig:Zn.cbig,objs:Zn.objs,bars:C.bars,grass:C.grass};const res={base:meas()};
   Zn.lands=[];res.noLands=meas();Zn.lands=sv.lands;
   Zn.cbig=[];res.noBig=meas();Zn.cbig=sv.cbig;
   C.bars=[];C.grass=[];res.noBars=meas();C.bars=sv.bars;C.grass=sv.grass;
   Zn.objs=[];res.noObjs=meas();Zn.objs=sv.objs;
   res.nl=Zn.lands.length;res.nb=Zn.cbig.length;res.no=Zn.objs.length;res.nbars=C.bars.length;
   out[f]=res;}
  return out;});
 console.log(name,JSON.stringify(r));await b.close();})();
