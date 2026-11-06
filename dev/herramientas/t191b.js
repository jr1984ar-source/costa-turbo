const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>{localStorage.clear();});await p.reload();await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(500);
 console.log(await p.evaluate(()=>{const c={};for(const o of __G.zone.objs)c[o.t]=(c[o.t]||0)+1;return JSON.stringify(c);}));
 await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 const go=async(name,f)=>{await p.evaluate(f);await p.evaluate(()=>{__G.P.v=0;__G.P.inv=2;});await p.waitForTimeout(1300);await p.screenshot({path:'v100b-'+name+'.png'});};
 await go('islita',()=>{const g=__G.zone.objs.find(o=>o.t==='bgirl');const P=__G.P;P.x=g.x-40;P.y=g.y+190;P.h=P.va=0;});
 await go('faro',()=>{const o=__G.zone.objs.find(o=>o.t==='faro');const P=__G.P;let best=null;for(let a=0;a<64;a++)for(const d of[180,230,280]){const x=o.x+Math.sin(a/64*6.283)*d,y=o.y+Math.cos(a/64*6.283)*d;if(__probe(x,y)&&__probe(x,y-60)&&(!best||y>best[1]))best=[x,y];}P.x=best[0];P.y=best[1];P.h=P.va=0;});
 await go('premio',()=>{const o=__G.zone.objs.find(o=>o.t==='gearbox');const P=__G.P;P.x=o.x;P.y=o.y+170;P.h=P.va=0;});
 await go('cala',()=>{const o=__G.zone.objs.filter(o=>o.t==='gearbox')[1];const P=__G.P;P.x=o.x;P.y=o.y+170;P.h=P.va=0;});
 await go('bosque',()=>{const P=__G.P;P.x=4600;P.y=-6500;P.h=P.va=0;let k=0;while(!__probe(P.x,P.y)&&k++<200)P.x+=20;});
 // coger un premio
 const r=await p.evaluate(async()=>{const o=__G.zone.objs.find(o=>o.t==='gearbox');const P=__G.P;P.x=o.x;P.y=o.y+60;P.h=P.va=0;P.v=150;__input.acc=true;await new Promise(r=>setTimeout(r,800));__input.acc=false;return {got:!!o.got,own:JSON.parse(localStorage.getItem(Object.keys(localStorage).find(k=>k.includes('ct_gear'))||'null')||'{}').own,msg:document.querySelector('#msg').textContent};});
 console.log('premio',JSON.stringify(r));
 console.log('errs',JSON.stringify(errs));await b.close();})();
