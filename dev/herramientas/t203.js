const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>{localStorage.clear();});await p.reload();await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 console.log(await p.evaluate(()=>{const c={};for(const o of __G.zone.objs)c[o.t]=(c[o.t]||0)+1;const m={};for(const o of __G.zone.movers)m[o.t]=(m[o.t]||0)+1;return JSON.stringify({objs:c,movers:m});}));
 const W=t=>p.waitForTimeout(t);const put=async(f,name,w=1400)=>{await p.evaluate(f);await W(w);await p.screenshot({path:'v105-'+name+'.png'});};
 const near=(X,Y,d)=>`const P=__G.P;let best=null;for(let a=0;a<64;a++)for(const dd of[${d}]){const x=${X}+Math.sin(a/64*6.283)*dd,y=${Y}+Math.cos(a/64*6.283)*dd;if(__probe(x,y)&&__probe(x,y-60)&&(!best||y>best[1]))best=[x,y];}if(best){P.x=best[0];P.y=best[1];}P.h=P.va=0;P.v=0;`;
 await put(new Function(near('RSPOTS_pigb[0]','RSPOTS_pigb[1]','200,240,300').replace(/RSPOTS_pigb/g,'(__G.zone.objs.find(o=>o.t==="pglabel"))').replace(/\[0\]/,'.x').replace(/\[1\]/,'.y+40')),'pigbeach');
 await put(()=>{const P=__G.P;P.x=5850;P.y=-1853;P.h=P.va=0;P.v=0;let k=0;while(!__probe(P.x,P.y)&&k++<50)P.x+=40;},'tropical');
 await put(()=>{const P=__G.P,o=__G.zone.movers.find(o=>o.t==='pgray');P.x=o.x;P.y=o.y+150;P.h=P.va=0;P.v=0;},'raya',900);
 await put(()=>{const P=__G.P;P.x=3750;P.y=-12203;P.h=P.va=0;P.v=0;let k=0;while(!__probe(P.x,P.y)&&k++<50)P.x+=40;},'profunda');
 await put(()=>{const P=__G.P;P.x=1800;P.y=-15450;P.h=P.va=0;P.v=0;let k=0;while(!__probe(P.x,P.y)&&k++<80)P.y+=30;P.y+=120;},'pueblo');
 await put(()=>{const P=__G.P,o=__G.zone.movers.find(o=>o.t==='pgpod');P.x=o.x-Math.sin(o.h)*-0;P.y=o.y+150;P.h=P.va=0;P.v=0;},'delfines',700);
 await put(()=>{const P=__G.P,o=__G.zone.objs.find(o=>o.t==='jelly');P.x=o.x;P.y=o.y+170;P.h=P.va=0;P.v=0;},'medusas');
 await put(()=>{const P=__G.P,o=__G.zone.objs.find(o=>o.t==='turtle');P.x=o.x;P.y=o.y+170;P.h=P.va=0;P.v=0;},'tortuga');
 // seguir a los delfines
 const f=await p.evaluate(async()=>{const o=__G.zone.movers.find(o=>o.t==='pgpod'),P=__G.P;const m0=__G.money;for(let i=0;i<75;i++){P.x=o.x+40;P.y=o.y+60;P.v=120;P.h=o.h;await new Promise(r=>setTimeout(r,100));}return {m:[m0,__G.money],msg:document.querySelector('#msg').textContent};});console.log('delfines',JSON.stringify(f));
 // banco de arena
 console.log('errs',JSON.stringify(errs));await b.close();})();
