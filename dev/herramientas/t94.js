const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='BAHAMAS');__goMap();});await W(300);await E(()=>__T.startRace());await W(3800);
 const info=await E(()=>{const C=__G.zone.circ;return{nar:C.nar,huge:C.huge,mid:C.mid.map(m=>m.i)};});
 const idx=[info.nar[0]-30,info.nar[1]-30,(info.huge||[0])[0]-20,info.mid[1]-40,Math.round(info.nar[0]/2),info.mid[2]+30];
 let k=0;for(const i of idx){await E(i=>{const C=__G.zone.circ,P=__G.P;i=Math.max(0,Math.min(C.n-1,i));P.x=C.x[i];P.y=C.y[i];P.h=P.va=C.h[i];P.cs=i;P.v=0;__G.camA=P.h;for(const c of __G.rivals)c.x=1e5;},i);await W(450);await p.screenshot({path:`bah2-${k++}.png`,clip:{x:0,y:0,width:390,height:690}});}
 console.log(JSON.stringify(info),JSON.stringify(errs));await b.close();})();
