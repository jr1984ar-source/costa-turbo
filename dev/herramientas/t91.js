const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='BAHAMAS');__goMap();});await W(300);await E(()=>__T.startRace());await W(3800);
 // avioneta
 await E(()=>{const o=__G.zone.objs.find(o=>o.t==='cplane'),C=__G.zone.circ,P=__G.P;let bi=0,bd=1e18;for(let i=0;i<C.n;i++){const d=(C.x[i]-o.x)**2+(C.y[i]-o.y)**2;if(d<bd){bd=d;bi=i;}}const i=Math.max(0,bi-22);P.x=C.x[i];P.y=C.y[i];P.h=P.va=C.h[i];P.cs=i;P.v=0;__G.camA=P.h;for(const c of __G.rivals)c.x=1e5;});await W(500);await p.screenshot({path:'v57c-plane.png',clip:{x:0,y:0,width:390,height:690}});
 // isla grande con palmeras
 await E(()=>{const Zn=__G.zone,C=Zn.circ,P=__G.P;let best=null;for(const L of Zn.lands){const w=L.bb[2]-L.bb[0];if(L.fill==='#4f9a45'&&(!best||w>best.w))best={L,w};}const cx=(best.L.bb[0]+best.L.bb[2])/2,cy=(best.L.bb[1]+best.L.bb[3])/2;let bi=0,bd=1e18;for(let i=0;i<C.n;i++){const d=(C.x[i]-cx)**2+(C.y[i]-cy)**2;if(d<bd){bd=d;bi=i;}}const i=Math.max(0,bi-15);P.x=C.x[i];P.y=C.y[i];P.h=P.va=C.h[i];P.cs=i;__G.camA=P.h;});await W(500);await p.screenshot({path:'v57c-isla.png',clip:{x:0,y:0,width:390,height:690}});
 console.log(JSON.stringify(errs));await b.close();})();
