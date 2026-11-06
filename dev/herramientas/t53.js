const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),out={};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 for(const [tag,name] of [['gc','GRAN CARRERA'],['tor','TORMENTA']]){
  await E(n=>{__G.free=true;__G.zi=__Z.findIndex(z=>z.name===n);__goMap();__T.startRace();},name);await W(3600);
  const len=await E(()=>__G.zone.len);
  for(const f of [.1,.21,.3,.5,.7]){await E(f=>{const P=__G.P,z=__G.zone,y=-z.len*f;P.y=y;P.x=200;P.v=0;},f);await W(500);await p.screenshot({path:`alt-${tag}-${Math.round(f*100)}.png`});}
  out[tag]=await E(()=>{const z=__G.zone,o=z.objs.filter(o=>o.x<0||o.x>380).map(o=>o.t);return {off:o.length,offT:[...new Set(o)].join(',')}});
  await p.keyboard.down('ArrowUp');await W(8000);await p.keyboard.up('ArrowUp');out[tag+'R']=await E(()=>__G.rivals.map(c=>Math.round(-c.y)).join(','));}
 console.log(JSON.stringify(out),JSON.stringify(errs));await b.close();})();
