const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),out={};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);
 await p.click('#bFree');await p.click('#aGo');await p.click('#gGo');await W(300);
 await E(()=>document.querySelectorAll('.fz')[0].click());await W(300);await p.click('#mGo');await W(3700);await p.keyboard.down('ArrowUp');await W(3000);
 // jump -> medalla
 await E(()=>{const o=__G.zone.objs.filter(o=>o.t==='ramp').sort((a,b)=>b.y-a.y).find(o=>o.y<__G.P.y-200),P=__G.P;P.x=o.x;P.y=o.y+50;P.v=300;P.h=0;P.va=0;});await W(500);await p.screenshot({path:'m-01-medalla.png'});
 out.med=await E(()=>localStorage.getItem('ct_medals'));out.money=await E(()=>__G.money);
 // terminar rápido: ir cerca de la meta
 await E(()=>{const P=__G.P;P.y=__G.zone.finishY+600;P.x=220;P.v=330;P.h=0;P.va=0;});await W(4500);await p.screenshot({path:'m-02-result.png'});
 out.ghost=await E(()=>{const g=JSON.parse(localStorage.getItem('ct_ghost_0')||'null');return g?{t:g.t,n:g.p.length,m:g.m}:null;});
 await p.keyboard.up('ArrowUp');
 await p.click('#rGo');await W(300);await E(()=>document.querySelectorAll('.fz')[0].click());await W(400);await p.screenshot({path:'m-03-map-record.png'});
 await p.click('#mGo');await W(3700);await W(800);await p.screenshot({path:'m-04-fantasma.png'});out.gdraw=await E(()=>!!__G.ghost);
 await E(()=>{__T.goFree();});await W(200);await p.click('#fBack');await W(300);await p.click('#bMed');await W(400);await p.screenshot({path:'m-05-medallas.png'});
 console.log(JSON.stringify(out),JSON.stringify(errs));await b.close();})();
