const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},'BAHAMAS');await W(300);await E(()=>__T.startRace());await W(3800);
 const info=await E(()=>{const Z=__G.zone,pigs=Z.objs.filter(o=>o.t==='pig');return{n:pigs.length,onLand:pigs.filter(o=>__landIn(Z.lands,o.x,o.y)).length,plane:Z.labels.filter(l=>/AVIONETA/.test(l.txt)).length,pts:pigs.map(o=>[o.x,o.y])};});
 console.log(JSON.stringify({n:info.n,onLand:info.onLand,plane:info.plane}));
 const groups=[info.pts[0],info.pts[6],info.pts[9],info.pts[12]];let k=0;
 for(const g of groups){await E(g=>{const P=__G.P,C=__G.zone.circ;let b=0,bd=1e18;for(let i=0;i<C.n;i++){const d=(C.x[i]-g[0])**2+(C.y[i]-g[1])**2;if(d<bd){bd=d;b=i;}}const i=Math.max(0,b-22);P.x=C.x[i];P.y=C.y[i];P.h=P.va=C.h[i];P.cs=i;P.v=0;__G.camA=P.h;for(const c of __G.rivals){c.x=1e5;c.trail=[];}},g);await W(450);await p.screenshot({path:`pig2-${k++}.png`,clip:{x:0,y:0,width:390,height:690}});}
 console.log(JSON.stringify(errs));await b.close();})();
