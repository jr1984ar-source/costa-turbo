const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 for(const name of[process.argv[2]]){
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},name);await W(300);await E(()=>__T.startRace());await W(3800);
 const r=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30,st={crash:{},maxOff:{},bumps:0,steps:0,hp0:__T.hpTot()};P.ai=P.ai||{re:0,tx:0};
  const oc=crafts=>{};for(const c of __crafts()){c._cc=0;}
  let t=0;while(t<220&&G.mode==='play'){const a=__aiCirc(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__upd(dt);t+=dt;st.steps++;
   for(const c of __crafts()){if(c.crash>.74){st.crash[c.id]=(st.crash[c.id]||0)+1;let bo=null,bd=1e9;for(const o of G.zone.objs){const d=Math.hypot(o.x-c.x,o.y-c.y);if(d<bd&&o.t!=='coin'&&o.t!=='cdeco'){bd=d;bo=o.t;}}(st.cw=st.cw||[]).push(c.id+':'+bo+'@'+c.cs+'/'+Math.round(t));}if((c.off||0)>240&&!(c['_o'+Math.floor(t/3)])){c['_o'+Math.floor(t/3)]=1;(st.offs=st.offs||[]).push(c.id+'@'+c.cs+'/'+Math.round(t)+'/'+Math.round(c.off));}st.maxOff[c.id]=Math.max(st.maxOff[c.id]||0,Math.round(c.off||0));if(c._bumpT>.69)st.bumps++;}}
  st.t=Math.round(t);st.mode=G.mode;st.order=G.finishOrder.map(c=>c.id+'@'+Math.round(c.finT));st.laps=__crafts().map(c=>c.id+':'+(c.lapN|0)+'/'+Math.round(c.prog));st.hp1=__T.hpTot();st.fuel=Math.round(G.fuel);return st;});
 console.log(name,JSON.stringify(r));
 await E(()=>{window.requestAnimationFrame=f=>setTimeout(()=>f(performance.now()),16);});await W(300);}
 console.log('ERRS',JSON.stringify(errs.slice(0,5)));await b.close();})();
