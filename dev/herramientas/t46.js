const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),out={};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 out.z=await E(()=>__Z.map((z,i)=>i+':'+z.name).join(' | '));
 for(const [zi,tag] of [[11,'form'],[12,'bah'],[13,'aus']]){
  await E(zi=>{__G.free=true;__G.zi=zi;__goMap();},zi);await W(400);await p.screenshot({path:`f-${tag}-map.png`});
  await E(()=>__T.startRace());await W(3600);await p.keyboard.down('ArrowUp');await W(2500);await p.screenshot({path:`f-${tag}-a.png`});
  const info=await E(()=>{const z=__G.zone,c={};z.objs.forEach(o=>c[o.t]=(c[o.t]||0)+1);z.movers.forEach(o=>c['M'+o.t]=(c['M'+o.t]||0)+1);return c;});out[tag]=info;
  // salto a zona con objetos interesantes
  await E(tag=>{const z=__G.zone,P=__G.P;const pick=tag==='form'?z.objs.find(o=>o.t==='posi'&&o.y<P.y-1500):tag==='bah'?(z.objs.find(o=>o.t==='island')):z.objs.find(o=>o.t==='coral'&&o.y<P.y-1500);if(pick){P.y=pick.y+330;P.x=200;P.v=0;}},tag);await W(700);await p.screenshot({path:`f-${tag}-b.png`});
  if(tag==='bah'){await E(()=>{const z=__G.zone,P=__G.P,o=z.objs.find(o=>o.t==='pig'&&o.y<P.y-800);if(o){P.y=o.y+300;P.x=200;P.v=0;}});await W(600);await p.screenshot({path:`f-${tag}-c.png`});}
  if(tag==='aus'){await E(()=>{const z=__G.zone,P=__G.P,o=z.objs.find(o=>o.t==='surfer'&&o.y<P.y-800);if(o){P.y=o.y+300;P.x=200;P.v=0;}});await W(600);await p.screenshot({path:`f-${tag}-c.png`});}
  await p.keyboard.up('ArrowUp');}
 // rivales bahamas progresan
 await E(()=>{__G.zi=12;__goMap();__T.startRace();});await W(3600);await p.keyboard.down('ArrowUp');await W(15000);out.bahRiv=await E(()=>__G.rivals.map(c=>Math.round(-c.y)).join(','));
 console.log(JSON.stringify(out,null,0),JSON.stringify(errs));await b.close();})();
