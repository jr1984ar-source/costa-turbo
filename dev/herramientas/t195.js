const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>{localStorage.clear();});await p.reload();await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);
 console.log(await p.evaluate(()=>{const c={};for(const o of __G.zone.objs)c[o.t]=(c[o.t]||0)+1;return JSON.stringify(c)+' movers '+JSON.stringify(__G.zone.movers.map(m=>m.t).reduce((a,t)=>(a[t]=(a[t]||0)+1,a),{}))+' lane '+JSON.stringify(__G.zone.lane);}));
 await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 const go=async(name,f,w=1300)=>{await p.evaluate(f);await p.evaluate(()=>{__G.P.v=0;__G.P.inv=0;});await p.waitForTimeout(w);await p.screenshot({path:'v101-'+name+'.png'});};
 const near=(o,d)=>`const P=__G.P;let best=null;for(let a=0;a<64;a++)for(const dd of[${d}]){const x=${o}.x+Math.sin(a/64*6.283)*dd,y=${o}.y+Math.cos(a/64*6.283)*dd;if(__probe(x,y)&&__probe(x,y-60)&&(!best||y>best[1]))best=[x,y];}P.x=best[0];P.y=best[1];P.h=P.va=0;`;
 await go('roxy',new Function(`const o=__G.zone.objs.find(o=>o.t==='pgbar'&&o.k==='roxy');${near('o','200,260,320')}`));
 await go('jj',new Function(`const o=__G.zone.objs.find(o=>o.t==='pgbar'&&o.k==='jj');const P=__G.P;P.x=o.x+180;P.y=o.y+140;P.h=P.va=0;`));
 await go('piri',new Function(`const o=__G.zone.movers.find(o=>o.t==='piripg');const P=__G.P;P.x=o.x+60;P.y=o.y+230;P.h=P.va=0;`),600);
 await go('oro',new Function(`const o=__G.zone.objs.find(o=>o.t==='gearbox'&&o.gold);${near('o','150,200,260')}`));
 await go('islita',new Function(`const o=__G.zone.objs.find(o=>o.t==='bgirl');${near('o','170,220,280')}`));
 await go('recta',new Function(`const L=__G.zone.lane;const P=__G.P;P.x=L.x;P.y=L.y0+150;P.h=P.va=0;`));
 for(let k=0;k<4;k++){await go('cala'+k,new Function(`const o=__G.zone.objs.filter(o=>o.t==='gearbox'&&!o.gold).sort((a,b)=>b.x-a.x)[${k}];${near('o','150,200,260')}`));}
 await go('derecha',new Function(`const P=__G.P;P.x=7400;P.y=-9000;P.h=P.va=0;let k=0;while(__probe(P.x,P.y)&&k++<400)P.x+=20;P.x-=260;P.h=Math.PI/2;`));
 // coger el casco dorado
 const r=await p.evaluate(async()=>{const o=__G.zone.objs.find(o=>o.t==='gearbox'&&o.gold);const P=__G.P;P.x=o.x;P.y=o.y+12;P.h=P.va=0;P.v=0;await new Promise(r=>setTimeout(r,400));return {got:!!o.got,msg:document.querySelector('#msg').textContent,own:JSON.parse(localStorage.getItem('ct_gear')||'{}').own};});
 console.log('oro',JSON.stringify(r));
 const r2=await p.evaluate(async()=>{const o=__G.zone.movers.find(o=>o.t==='piripg');const P=__G.P;const t0=__G.turbo;P.x=o.rx;P.y=o.ry;P.v=0;await new Promise(r=>setTimeout(r,300));return {gift:o.gift,turbo:[t0,__G.turbo],msg:document.querySelector('#msg').textContent};});
 console.log('piri',JSON.stringify(r2));
 console.log('errs',JSON.stringify(errs));await b.close();})();
