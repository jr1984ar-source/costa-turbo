const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms);const E=(f,a)=>p.evaluate(f,a);const out={};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1200);
 // OLAS
 await E(()=>{__G.free=true;__G.zi=5;__goMap();__T.startRace();});await W(3600);
 out.waves=await E(()=>__G.zone.waves.map(o=>Math.round(o.y)));
 await E(()=>{const o=__G.zone.waves[0],P=__G.P;P.y=o.y+560;P.x=230;P.v=0;P.h=0;P.va=0;});await W(300);
 await E(()=>{const P=__G.P;P.y-=100;});await W(900);await p.screenshot({path:'w-01-wave.png'});
 // slow crossing
 await E(()=>{const o=__G.zone.waves[0],P=__G.P;P.y=o.y+30;P.v=70;P.h=0;P.va=0;});await p.keyboard.down('ArrowUp');await W(500);
 out.cap=await E(()=>({capT:+(__G.P.capT||0).toFixed(2),done:__G.zone.waves[0].done}));await W(500);await p.screenshot({path:'w-02-capsize.png'});await W(2200);out.after=await E(()=>({capT:__G.P.capT,v:Math.round(__G.P.v)}));
 // fast crossing on wave 2
 await E(()=>{const o=__G.zone.waves[1],P=__G.P;o.act=1;o.side=1;P.y=o.y+160;P.x=230;P.v=320;P.h=0;P.va=0;P.capT=0;});const j0=await E(()=>__G.jumps);await W(700);
 out.fast=await E(()=>({air:+__G.P.air.toFixed(2),cap:__G.P.capT||0,jumps:__G.jumps}));out.j0=j0;await p.screenshot({path:'w-03-bigjump.png'});await p.keyboard.up('ArrowUp');
 // final set
 await E(()=>{const o=__G.zone.waves[4],P=__G.P;P.y=o.y+420;P.x=230;P.v=0;});await W(400);await E(()=>{__G.zone.waves.slice(4).forEach(o=>{o.act=1;});});await W(200);await p.screenshot({path:'w-04-set.png'});
 // ES TRENC
 await E(()=>{__G.zi=6;__goMap();__T.startRace();});await W(3600);
 out.pass=await E(()=>__G.zone.big.filter(o=>o.t==='pass').map(o=>({y:Math.round(o.y),gx:Math.round(o.gx),wedge:o.wedge,ramp:(()=>{const r=__G.zone.objs.find(r=>r.t==='ramp'&&r.sand&&Math.abs(r.y-o.y)<200);return r?{x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.w)}:null})()})));
 for(let k=0;k<2;k++){await E(k=>{const o=__G.zone.big.filter(o=>o.t==='pass')[k],P=__G.P;P.y=o.y+330;P.x=o.gx;P.v=0;},k);await W(700);await p.screenshot({path:'w-1'+k+'-pass.png'});}
 // wedge slide test (pass 0)
 await E(()=>{const o=__G.zone.big.filter(o=>o.t==='pass')[0],P=__G.P;const gl=o.gx-38,gr=o.gx+38;P.x=o.wedge<0?gl-40:gr+40;P.y=o.y+90;P.v=200;P.h=0;P.va=0;window.__o=o;});await p.keyboard.down('ArrowUp');
 const w0=await E(()=>({x:Math.round(__G.P.x),y:Math.round(__G.P.y-__o.y)}));await W(600);await p.screenshot({path:'w-12-wedge.png'});await W(900);
 const w1=await E(()=>({x:Math.round(__G.P.x),y:Math.round(__G.P.y-__o.y)}));out.wedge={w0,w1,o:await E(()=>({gx:Math.round(__o.gx),side:__o.wedge}))};
 // flat jump fast
 await E(()=>{const o=__G.zone.big.filter(o=>o.t==='pass')[1],r=__G.zone.objs.find(r=>r.t==='ramp'&&r.sand&&Math.abs(r.y-o.y)<200),P=__G.P;P.x=r.x;P.y=r.y+60;P.v=320;P.h=0;P.va=0;P.stuckT=0;window.__o=o;});await W(450);await p.screenshot({path:'w-13-jumpflat.png'});await W(1300);
 out.flatFast=await E(()=>({dy:Math.round(__G.P.y-__o.y),stuck:__G.P.stuckT||0}));
 // flat jump slow
 await E(()=>{const o=__G.zone.big.filter(o=>o.t==='pass')[1],r=__G.zone.objs.find(r=>r.t==='ramp'&&r.sand&&Math.abs(r.y-o.y)<200),P=__G.P;P.x=r.x;P.y=r.y+40;P.v=150;P.h=0;P.va=0;window.__o=o;});await p.keyboard.up('ArrowUp');await W(900);
 out.flatSlow=await E(()=>({dy:Math.round(__G.P.y-__o.y),stuck:+(__G.P.stuckT||0).toFixed(2)}));await p.screenshot({path:'w-14-stuck.png'});await W(1300);out.flatSlow2=await E(()=>({dy:Math.round(__G.P.y-__o.y),stuck:__G.P.stuckT||0}));
 console.log(JSON.stringify(out,null,0),JSON.stringify(errs));await b.close();})();
