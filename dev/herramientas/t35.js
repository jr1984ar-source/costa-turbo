const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({args:['--autoplay-policy=no-user-gesture-required']});const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__G.free=true;__G.zi=3;__G.parts={escape:3};__goMap();__T.startRace();window.__pops=0;const o=__S.pops.bind(__S);__S.pops=(a,b)=>{window.__pops++;o(a,b);};});await W(3600);
 for(let i=0;i<3;i++){await p.keyboard.down('ArrowUp');await W(2500);await p.keyboard.up('ArrowUp');await W(400);}
 const pops=await E(()=>window.__pops);
 await E(()=>{__G.zi=10;__G.parts={};__goMap();__T.startRace();window.__pen=0;window.__seen=new Set();setInterval(()=>{__G.rivals.forEach((c,i)=>{const k=i+':'+Math.round(c.stuckY||0);if(c.stuckT>0&&!__seen.has(k)){__seen.add(k);__pen++;}});},50);});await W(3600);await p.keyboard.down('ArrowUp');await W(20000);
 const r=await E(()=>({pen:__pen,passed:__G.zone.objs.filter(o=>o.t==='tbuoy'&&o.y>Math.min(...__G.rivals.map(c=>c.y))).length*5}));
 console.log('pops',pops,'rival penalties',JSON.stringify(r),JSON.stringify(errs));await b.close();})();
