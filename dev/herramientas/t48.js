const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),out={};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 out.z=await E(()=>__Z.map((z,i)=>i+':'+z.name).join(' | '));
 const idx=await E(()=>({f:__Z.findIndex(z=>z.name==='FORMENTOR'),c:__Z.findIndex(z=>z.name==='SA CALOBRA'),k:__Z.findIndex(z=>z.name==='CABRERA'),p:__Z.findIndex(z=>z.name==='PORTALS')}));
 for(const [tag,zi] of [['formentor',idx.f],['calobra',idx.c],['cabrera',idx.k],['portals',idx.p]]){
  await E(zi=>{__G.free=true;__G.zi=zi;__goMap();},zi);await W(400);await p.screenshot({path:`g-${tag}-map.png`});
  await E(()=>__T.startRace());await W(3600);await p.keyboard.down('ArrowUp');await W(2500);await p.screenshot({path:`g-${tag}-a.png`});
  out[tag]=await E(()=>{const z=__G.zone,c={};z.objs.forEach(o=>c[o.t]=(c[o.t]||0)+1);z.movers.forEach(o=>c['M'+o.t]=(c['M'+o.t]||0)+1);c.rw=!!z.rwall;return c;});
  await E(tag=>{const z=__G.zone,P=__G.P;let y=null;if(tag==='formentor'){const o=z.objs.find(o=>o.t==='island');y=o.y+o.ry+300;}if(tag==='calobra'){y=-4000;}if(tag==='cabrera'){const o=z.objs.find(o=>o.t==='nozone');y=o?o.y+o.ry+280:null;}if(tag==='portals'){const o=z.movers.find(o=>o.t==='super');o.x=200;y=o.y+320;}if(y!=null){P.y=y;P.x=tag==='calobra'?(z.shore(y)+z.rwall(y))/2:200;P.v=0;}},tag);await W(700);await p.screenshot({path:`g-${tag}-b.png`});
  if(tag==='formentor'){await E(()=>{const P=__G.P;P.y=__G.zone.finishY+380;P.x=230;P.v=0;});await W(900);await p.screenshot({path:`g-${tag}-c.png`});}
  if(tag==='calobra'){out.calW=await E(()=>{const z=__G.zone;const w=[];for(let u=1500;u<12000;u+=1500)w.push(Math.round(z.rwall(-u)-z.shore(-u)));return w.join(',');});
   await E(()=>{const P=__G.P,z=__G.zone;P.x=z.rwall(P.y)-30;P.h=.8;P.va=.8;P.v=250;});await W(500);out.calClamp=await E(()=>{const P=__G.P,z=__G.zone;return Math.round(z.rwall(P.y)-P.x);});}
  await p.keyboard.up('ArrowUp');}
 await E(zi=>{__G.zi=zi;__goMap();__T.startRace();},idx.k);await W(3600);out.m0=await E(()=>__G.money);await E(()=>{const o=__G.zone.objs.find(o=>o.t==='nozone'),P=__G.P;P.x=o.x;P.y=o.y+o.ry+30;P.v=200;P.h=0;P.va=0;});await p.keyboard.down('ArrowUp');await W(800);out.m1=await E(()=>__G.money);await p.keyboard.up('ArrowUp');
 await W(12000);out.cabRiv=await E(()=>__G.rivals.map(c=>Math.round(-c.y)).join(','));
 console.log(JSON.stringify(out,null,0),JSON.stringify(errs));await b.close();})();
