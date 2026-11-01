const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),out={};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);
 // garaje con piezas a tope
 await E(()=>{const m=__M[0];const pp=__T.partsOf(m);for(const k of['turbo','bov','escape','turbina','intercooler','aletas'])pp[k]=3;});
 await p.click('#bPlay');await W(200);await p.click('#aGo');await W(400);await p.screenshot({path:'v38-garaje.png'});
 out.gstats=await E(()=>[...document.querySelectorAll('#gStats .st')].map(r=>r.querySelector('span').textContent+':'+r.querySelectorAll('b.on').length+'+'+r.querySelectorAll('b.up').length));
 // taller
 await E(()=>__T.goShop());await W(400);await p.screenshot({path:'v38-taller.png'});
 // campeonato Sa Calobra
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='SA CALOBRA');__goMap();});await W(300);await E(()=>__T.startRace());await W(3600);
 out.calobra=await E(()=>{const Zn=__G.zone;const ws=[];for(let u=1500;u<Zn.len-1500;u+=500)ws.push(Math.round(Zn.rwall(-u)-Zn.shore(-u)));return{len:Zn.len,minW:Math.min(...ws),avgW:Math.round(ws.reduce((a,b)=>a+b)/ws.length),rocks:Zn.objs.filter(o=>o.t==='rock').length,hearts:Zn.objs.filter(o=>o.t==='heart').map(o=>[Math.round(o.x),Math.round(o.y)])};});
 await p.keyboard.down('ArrowUp');await W(2500);await p.screenshot({path:'v38-calobra.png'});await p.keyboard.up('ArrowUp');
 // golpe contra roca a velocidad
 const hit=async()=>E(()=>{const P=__G.P,Zn=__G.zone;P.inv=0;P.crash=0;P.v=P.st.maxV*.8;P.h=0;P.va=0;const o={t:'rock',x:P.x,y:P.y-12,rad:10,v:0};const i=Zn.objs.findIndex(q=>q.y>o.y);Zn.objs.splice(i<0?Zn.objs.length:i,0,o);});
 out.hp0=await E(()=>__T.hpTot());await hit();await W(300);out.hp1=await E(()=>[__T.hpTot(),__G.lives,__G.dmg]);await p.screenshot({path:'v38-golpe1.png'});
 await hit();await W(300);await hit();await W(300);out.hp3=await E(()=>[__T.hpTot(),__G.lives,__G.dmg,document.querySelector('#msg').textContent]);await p.screenshot({path:'v38-golpe3.png'});
 // golpe lento: no quita
 await E(()=>{const P=__G.P,Zn=__G.zone;P.inv=0;P.crash=0;P.v=P.st.maxV*.1;const o={t:'rock',x:P.x,y:P.y-12,rad:10,v:0};const i=Zn.objs.findIndex(q=>q.y>o.y);Zn.objs.splice(i,0,o);});await W(300);out.slow=await E(()=>__T.hpTot());
 // recoger corazón
 await E(()=>{const P=__G.P,h=__G.zone.objs.find(o=>o.t==='heart');P.inv=0;P.x=h.x;P.y=h.y+30;P.v=120;P.h=0;P.va=0;});await W(500);out.pick=await E(()=>[__T.hpTot(),document.querySelector('#msg').textContent]);await p.screenshot({path:'v38-corazon.png'});
 // ver corazón flotando
 await E(()=>{const P=__G.P,h=__G.zone.objs.filter(o=>o.t==='heart'&&!o.got)[0];if(h){P.x=h.x+40;P.y=h.y+260;P.v=0;}});await W(400);await p.screenshot({path:'v38-corazon-agua.png'});
 // bar
 await E(()=>{__G.mode='play';__T.setHp(7);});await E(()=>{try{__T.openBar('jj')}catch(e){window.__e=String(e)}});await W(500);await p.screenshot({path:'v38-bar.png'});out.bar=await E(()=>[...document.querySelectorAll('#scrJJ .item')].map(d=>d.textContent));
 const btn=await p.$$('#scrJJ .item button');if(btn[2]){await btn[2].click();await W(200);}out.afterDrink=await E(()=>[__T.hpTot(),__G.turbo]);
 // sin corazones -> fin
await E(()=>{__G.mode='play';});
 // carrera libre: corazones llenos, sin corazones flotando
 await E(()=>{__T.startFree(3);});await W(300);await E(()=>__T.startRace());await W(3600);out.free=await E(()=>[__G.lives,__G.dmg,__G.zone.objs.filter(o=>o.t==='heart').length]);
 // circuito campeonato: corazones
 await E(()=>{__G.free=false;__G.zi=__Z.findIndex(z=>z.name==='BAHÍA DE PALMA');__goMap();});await W(200);await E(()=>__T.startRace());await W(3600);out.circ=await E(()=>__G.zone.objs.filter(o=>o.t==='heart').length);
 // vaciar corazones con golpes
 await E(()=>__T.setHp(1));await W(100);
 await E(()=>{const P=__G.P,Zn=__G.zone;P.inv=0;P.crash=0;P.v=P.st.maxV*.8;const o={t:'rock',x:P.x+Math.sin(P.h)*12,y:P.y-Math.cos(P.h)*12,rad:10,v:0};const i=Zn.objs.findIndex(q=>q.y>o.y);Zn.objs.splice(i<0?Zn.objs.length:i,0,o);});await W(1500);
 out.dead=await E(()=>[__G.mode,__G.lives,document.querySelector('.screen:not([hidden])')?.id]);await p.screenshot({path:'v38-fin.png'});
 console.log(JSON.stringify(out,null,1));console.log('ERRS',JSON.stringify(errs));await b.close();})();
