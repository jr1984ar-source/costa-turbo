const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),out={};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__G.free=true;__G.zi=6;__goMap();__T.startRace();});await W(3600);await p.keyboard.down('ArrowUp');
 const toRamp=async(i)=>E(i=>{const rs=__G.zone.objs.filter(o=>o.t==='ramp'&&o.kick&&!o.mega).sort((a,b)=>b.y-a.y),o=rs[i],P=__G.P;P.x=o.x;P.y=o.y+60;P.v=330;P.h=0;P.va=0;P.crash=0;P.inv=0;},i);
 // mortal
 await toRamp(0);await W(350);out.air1=await E(()=>+__G.P.air.toFixed(2));await p.keyboard.down('c');await W(80);await p.keyboard.up('c');await W(200);await p.screenshot({path:'k-01-mortal.png'});const s0=await E(()=>__G.score);await W(1400);out.flip={score:await E(()=>__G.score)-s0,crash:await E(()=>__G.P.crash>0)};
 // superman
 await toRamp(3);await W(300);await p.keyboard.press('x');await W(220);await p.screenshot({path:'k-02-superman.png'});const s1=await E(()=>__G.score);await W(1400);out.sup={score:await E(()=>__G.score)-s1,crash:await E(()=>__G.P.crash>0)};
 // mortal tarde -> mal aterrizaje
 await toRamp(5);await W(150);await E(()=>{__G.P.air=.25;});await p.keyboard.down('c');await W(60);await p.keyboard.up('c');await W(700);out.late={crash:await E(()=>__G.P.crash>0||__G.P.inv>0)};
 await p.keyboard.up('ArrowUp');
 // animales vuelta 2
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__G.free=false;__G.zi=3;__G.lap=1;__goMap();__T.startRace();});await W(3600);
 out.anim=await E(()=>({dol:__G.zone.movers.filter(o=>o.t==='dolphin').length,jel:__G.zone.objs.filter(o=>o.t==='jelly').length,tur:__G.zone.objs.filter(o=>o.t==='turtle').length}));
 await E(()=>{const d=__G.zone.movers.find(o=>o.t==='dolphin'),P=__G.P;if(!d)return;P.y=d.y+120;P.x=d.x+30;P.v=0;window.__t0=__G.turbo;});await W(600);await p.screenshot({path:'k-03-delfines.png'});
 await E(()=>{const P=__G.P,d=__G.zone.movers.find(o=>o.t==='dolphin');if(!d)return;P.x=d.x+20;P.y=d.y+20;});await W(200);out.dolTurbo=await E(()=>__G.turbo-window.__t0);
 await E(()=>{const j=__G.zone.objs.find(o=>o.t==='jelly'),P=__G.P;if(!j)return;P.y=j.y+200;P.x=j.x;});await W(400);await p.screenshot({path:'k-04-medusas.png'});
 await E(()=>{const j=__G.zone.objs.find(o=>o.t==='turtle'),P=__G.P;if(!j)return;P.y=j.y+220;P.x=j.x+40;});await W(400);await p.screenshot({path:'k-05-tortuga.png'});
 console.log(JSON.stringify(out),JSON.stringify(errs));await b.close();})();
