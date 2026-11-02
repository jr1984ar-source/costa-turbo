const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await W(1200);
 // ---- TORMENTA ----
 await E(()=>__T.startFree(13));await W(400);await E(()=>__T.startRace());await W(4200);
 const info=await E(()=>{const O=__G.zone.objs;return {swell:O.filter(o=>o.t==='swell').length,lb:O.filter(o=>o.t==='lbuoy').length,sw0:(O.find(o=>o.t==='swell')||{}).y};});console.log('tormenta',JSON.stringify(info));
 // ver oleaje + boyas
 await E(y=>{const P=__G.P;P.y=y+260;P.x=200;P.v=0;P.h=0;P.inv=5;__G.boltT=99;__G.bolts=[];},info.sw0);await W(600);await p.screenshot({path:'v79-tormenta-oleaje.png'});
 // empuje del oleaje
 const push=await E(async y=>{const P=__G.P;P.y=y+30;P.x=200;P.v=150;P.h=0;const x0=P.x;__input.acc=true;await new Promise(r=>setTimeout(r,900));__input.acc=false;return Math.round(P.x-x0);},info.sw0);console.log('empuje oleaje x:',push);
 // aviso de rayo y golpe
 await E(()=>{const P=__G.P;P.y-=900;P.v=0;P.h=0;P.inv=0;__G.bolts=[{x:P.x,y:P.y-60,t:1.25,s:0,life:0}];__G.boltT=99;});await W(500);await p.screenshot({path:'v79-tormenta-aviso.png'});
 await E(()=>{__G.P.v=200;__G.bolts[0].y=__G.P.y;__G.bolts[0].x=__G.P.x;});await W(900);await p.screenshot({path:'v79-tormenta-rayo.png'});
 console.log('rayo: velocidad tras golpe',await E(()=>Math.round(__G.P.v)),'pops',await E(()=>__G.pops.map(p=>p.txt).join('|')));
 // ---- SAN TELM ----
 await E(()=>__T.startFree(8));await W(400);await E(()=>__T.startRace());await W(4200);
 const st=await E(()=>{const O=__G.zone.objs;return {caves:(__G.zone.caves||[]).map(c=>Math.round(c.y)),isl:O.filter(o=>o.t==='island'&&o.cave).map(o=>({x:Math.round(o.x),y:Math.round(o.y),rx:o.rx,ry:o.ry,sh:Math.round(__G.zone.shore(o.y))})),boats:O.filter(o=>o.t==='fboat').map(o=>({x:Math.round(o.x),y:Math.round(o.y),nx1:Math.round(o.nx1)}))};});
 console.log('san telm',JSON.stringify(st));
 const o=st.isl[0];
 await E(o=>{const P=__G.P,Zn=__G.zone,y0=o.y+o.ry+130;P.x=(Zn.shore(y0)+o.x-o.rx-10)/2;P.y=y0;P.v=0;P.h=0;P.va=0;P.inv=3;__G.rivals.forEach(c=>c.y=P.y+900);},o);await W(500);await p.screenshot({path:'v79-santelm-cueva.png'});
 const r=await E(async o=>{const P=__G.P;let bumps=0;__input.acc=true;const t0=performance.now();await new Promise(res=>{const iv=setInterval(()=>{if(P._isl>0.6)bumps++;if(P.y<o.y-o.ry*.2&&!window.__shot){window.__shot=1;}if(P.y<o.y-o.ry-60||performance.now()-t0>7000){clearInterval(iv);res();}},50);});__input.acc=false;return {pasa:P.y<o.y-o.ry-60,bumps,turbo:__G.turbo};},o);
 console.log('cueva recta:',JSON.stringify(r));
 // dentro de la cueva (captura)
 await E(o=>{const P=__G.P,Zn=__G.zone;P.x=(Zn.shore(o.y)+o.x-o.rx-10)/2;P.y=o.y+40;P.v=0;P.h=0;},o);await W(400);await p.screenshot({path:'v79-santelm-dentro.png'});
 // barca y red
 const fb=st.boats[0];
 await E(fb=>{const P=__G.P;P.y=fb.y+240;P.x=(fb.x+fb.nx1)/2+(fb.nx1>fb.x?10:-10);P.v=0;P.h=0;P.inv=0;},fb);await W(500);await p.screenshot({path:'v79-santelm-barca.png'});
 const net=await E(async fb=>{const P=__G.P;P.v=220;__input.acc=true;let vmin=999;await new Promise(res=>{const iv=setInterval(()=>{if(Math.abs(P.y-fb.y)<40)vmin=Math.min(vmin,P.v);if(P.y<fb.y-120){clearInterval(iv);res();}},30);});__input.acc=false;return {vmin:Math.round(vmin),pops:__G.pops.map(p=>p.txt).join('|')};},fb);console.log('red:',JSON.stringify(net));
 console.log('errs',JSON.stringify(errs));await b.close();})();
