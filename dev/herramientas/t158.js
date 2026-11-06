const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();
 const E=(f,a)=>p.evaluate(f,a);await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1000);
 await E(()=>{__T.newGame();__G.zi=3;__goMap();});await p.waitForTimeout(300);
 console.log(await E(()=>{const Zn=__G.zone,isl=Zn.objs.filter(o=>o.t==='island'&&o.cut===1).sort((a,b)=>a.y-b.y);const out=[];
  for(let y=isl[2].y+isl[2].ry;y>isl[0].y-isl[0].ry;y-=100){let edge=-1e9;for(const o of isl){const dy=(y-o.y)/(o.ry+10);if(Math.abs(dy)<1)edge=Math.max(edge,o.x+(o.rx+10)*Math.sqrt(1-dy*dy));}const w=Zn.rwall(y)-11;out.push(Math.round(y)+':'+Math.round(w-edge));}
  const ramps=Zn.objs.filter(o=>o.t==='ramp'&&o.y<isl[2].y+isl[2].ry&&o.y>isl[0].y-isl[0].ry).map(o=>Math.round(o.x)+','+Math.round(o.y));
  return 'ancho canal: '+out.join(' ')+' | rampas '+ramps.join(' ')+' | x '+Math.round(isl[0].x)+' rw '+Math.round(Zn.rwall(isl[1].y));}));
 await b.close();})();
