const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},'BAHAMAS');await W(300);await E(()=>__T.startRace());await W(3800);
 const r=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,C=G.zone.circ,dt=1/30;const out=[];
  for(const onBank of[false,true]){const g=C.gaps[1],i=g.i;let x=C.x[i],y=C.y[i];if(onBank){const B=C.banks[1];let sx=0,sy=0;for(const q of B.pts){sx+=q[0];sy+=q[1];}x=sx/B.pts.length;y=sy/B.pts.length;}else{x=C.x[i]+Math.cos(C.h[i])*g.lat;y=C.y[i]+Math.sin(C.h[i])*g.lat;}
   P.x=x;P.y=y;P.h=P.va=C.h[i];P.cs=null;P.v=P.st.maxV*.8;G.pops=[];__input.acc=true;__input.left=__input.right=false;let t=0;while(t<.8){__upd(dt);t+=dt;}out.push({onBank,v:Math.round(P.v),max:Math.round(P.st.maxV),pops:G.pops.map(q=>q.txt)});}
  return out;});
 console.log(JSON.stringify(r));await b.close();})();
