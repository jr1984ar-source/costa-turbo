const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 const res={};
 for(const n of ['LAS RAMPAS','EL PUERTO','FORMENTERA','GRAN CARRERA','AUSTRALIA']){await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},n);await W(200);await E(()=>__T.startRace());await W(3600);
  res[n]=await E(()=>{const O=__G.zone.objs,D={s:330,m:470,l:690},OB=['rock','sail','motor','kayak','yacht','patrol','turtle','pig','surfer','croc','coral'];const rs=O.filter(o=>o.t==='ramp');let bad=0,cnt={};
   for(const r of rs){const d=r.mega?820:D[r.sz||'m'];cnt[r.mega?'mega':r.sz||'-']=(cnt[r.mega?'mega':r.sz||'-']||0)+1;for(const o of O){if(!OB.includes(o.t))continue;const du=-o.y+r.y;if(du>d*.5&&du<d*1.45&&Math.abs(o.x-r.x)<(r.w||100)/2+70)bad++;}}
   // ramp-to-ramp spacing (same lane) for kick ramps
   const ks=rs.filter(o=>o.kick&&!o.mega).sort((a,b)=>b.y-a.y);let close=0;for(let i=1;i<ks.length;i++){const a=ks[i-1],b2=ks[i],du=a.y-b2.y;if(du>0&&du<D[a.sz||'m']*1.3)close++;}
   return{ramps:rs.length,cnt,bad,close};});}
 // simulate jumps in Las Rampas with autopilot: count crashes on landing
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},'LAS RAMPAS');await W(200);await E(()=>__T.startRace());await W(3600);
 const run=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30;P.ai=P.ai||{re:0,tx:P.x,lane:0};let t=0,cr=0,why=[];
  while(t<200&&G.mode==='play'){const a=__aiCtl(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__upd(dt);t+=dt;if(P.crash>.74){cr++;}}
  return{t:Math.round(t),mode:G.mode,jumps:G.jumps,crashes:cr};});
 console.log(JSON.stringify(res),JSON.stringify(run),JSON.stringify(errs.slice(0,3)));await b.close();})();
