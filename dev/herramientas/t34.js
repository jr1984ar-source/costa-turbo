const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({args:['--autoplay-policy=no-user-gesture-required']});const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),out={};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 out.zones=await E(()=>__Z.map(z=>z.name).join(' | '));
 // RAMPAS
 await E(()=>{__G.free=true;__G.zi=6;__G.parts={escape:3};__goMap();});await W(400);await p.screenshot({path:'n-01-map-rampas.png'});
 await E(()=>__T.startRace());await W(3600);await p.keyboard.down('ArrowUp');await W(2000);await p.screenshot({path:'n-02-rampas.png'});
 out.ramps=await E(()=>__G.zone.objs.filter(o=>o.t==='ramp').length);
 // jump test: put P in front of first kick ramp
 await E(()=>{const o=__G.zone.objs.filter(o=>o.t==='ramp'&&o.kick).sort((a,b)=>b.y-a.y)[0],P=__G.P;P.x=o.x;P.y=o.y+120;P.v=300;P.h=0;P.va=0;window.__o=o;});await W(420);await p.screenshot({path:'n-03-salto.png'});await W(900);out.j1=await E(()=>__G.jumps);
 // boat jump pattern
 await E(()=>{const os=__G.zone.objs,i=os.findIndex(o=>o.t==='ramp'&&o.kick&&os.some(b=>(b.t==='sail'||b.t==='motor')&&Math.abs(b.x-o.x)<1&&Math.abs(b.y-(o.y-125))<2));const o=os[i],P=__G.P;P.x=o.x;P.y=o.y+110;P.v=290;P.h=0;P.va=0;P.crash=0;P.inv=0;});await W(300);await p.screenshot({path:'n-04-barca.png'});await W(1200);out.boat=await E(()=>({crash:__G.P.crash>0,jumps:__G.jumps}));
 // mega
 await E(()=>{const o=__G.zone.objs.find(o=>o.mega),P=__G.P;P.x=o.x;P.y=o.y+160;P.v=320;P.h=0;P.va=0;P.crash=0;});await W(700);await p.screenshot({path:'n-05-mega.png'});out.mega=await E(()=>+__G.P.airT.toFixed(2));
 // pops spy
 await E(()=>{window.__pops=0;const o=__S.pops.bind(__S);__S.pops=(a,b)=>{window.__pops++;o(a,b);};});await W(1500);await p.keyboard.up('ArrowUp');await W(300);out.pops=await E(()=>window.__pops);
 // BOYAS
 await E(()=>{__G.zi=10;__G.parts={};__goMap();});await W(400);await p.screenshot({path:'n-06-map-boyas.png'});
 await E(()=>__T.startRace());await W(3600);await p.keyboard.down('ArrowUp');await W(2500);await p.screenshot({path:'n-07-boyas.png'});
 // wrong side test
 await E(()=>{const b=__G.zone.objs.filter(o=>o.t==='tbuoy').sort((a,c)=>c.y-a.y)[1],P=__G.P;P.x=b.x-b.side*40;P.y=b.y+60;P.v=200;P.h=0;P.va=0;window.__b=b;});await W(500);out.wrong=await E(()=>+(__G.P.stuckT||0).toFixed(2));await p.screenshot({path:'n-08-penal.png'});await W(2200);
 await E(()=>{const b=__G.zone.objs.filter(o=>o.t==='tbuoy').sort((a,c)=>c.y-a.y)[2],P=__G.P;P.x=b.x+b.side*44;P.y=b.y+60;P.v=200;P.h=0;P.va=0;window.__b=b;});await W(500);out.right=await E(()=>({ok:__b.ok||0,stuck:__G.P.stuckT||0}));
 // rivals behaviour 20s
 await E(()=>{__G.zi=10;__goMap();__T.startRace();});await W(3600);await p.keyboard.down('ArrowUp');
 const samp=[];for(let i=0;i<4;i++){await W(5000);samp.push(await E(()=>__G.rivals.map(c=>Math.round(-c.y)+(c.stuckT>0?'P':'')).join(',')));}out.riv=samp;
 out.pen=await E(()=>{let n=0,ok=0;for(const o of __G.zone.objs)if(o.t==='tbuoy'&&o.y>__G.rivals[0].y){}return 1;});
 console.log(JSON.stringify(out,null,1),JSON.stringify(errs));await b.close();})();
