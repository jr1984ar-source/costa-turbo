const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='LAS RAMPAS');__goMap();});await W(300);await E(()=>__T.startRace());await W(3800);
 const info=await E(()=>{const O=__G.zone.objs;const c={};for(const o of O)if(o.t==='ramp'||o.t==='cramp'){const k=o.t+':'+(o.mega?'mega':o.sz||'-');c[k]=(c[k]||0)+1;}return c;});
 // vista de rampas de colores
 await E(()=>{const O=__G.zone.objs,r=O.filter(o=>o.t==='ramp'&&o.sz==='l')[1],P=__G.P;P.x=200;P.y=r.y+330;P.v=0;P.h=0;P.va=0;});await W(500);await p.screenshot({path:'v50-a.png'});
 // salto de lado
 const side=await E(()=>{const o=__G.zone.objs.find(o=>o.t==='cramp'),P=__G.P;P.x=o.x;P.y=o.y+170;P.v=P.st.maxV;P.h=0;P.va=0;P.air=0;P.crash=0;P.inv=0;window.__o=o;return{h:o.h,x:o.x,y:o.y};});
 await p.keyboard.down('ArrowUp');await W(650);
 const air=await E(()=>{const P=__G.P;return{air:+P.air.toFixed(2),h:+P.h.toFixed(2),va:+P.va.toFixed(2),x:Math.round(P.x),pops:__G.pops.map(q=>q.txt+'/'+(q.f?'follow':'fixed'))};});
 await p.screenshot({path:'v50-b.png'});await W(900);await p.screenshot({path:'v50-c.png'});
 const after=await E(()=>{const P=__G.P;return{air:+P.air.toFixed(2),x:Math.round(P.x),pops:__G.pops.map(q=>q.txt+'/'+q.life.toFixed(1))};});
 await p.keyboard.up('ArrowUp');
 console.log(JSON.stringify({info,side,air,after}),JSON.stringify(errs));await b.close();})();
