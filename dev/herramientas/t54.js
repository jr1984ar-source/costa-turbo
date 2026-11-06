const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),out={};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 for(const [tag,name] of [['palma','BAHÍA DE PALMA'],['alc','BAHÍA DE ALCÚDIA']]){
  await E(n=>{__G.free=true;__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},name);await W(400);await p.screenshot({path:`c-${tag}-map.png`});
  await E(()=>__T.startRace());await W(3600);out[tag+'L']=await E(()=>__G.zone.circ.L);
  await p.keyboard.down('ArrowUp');await W(1500);await p.screenshot({path:`c-${tag}-a.png`});
  const drive=async(ms)=>{const t0=Date.now();while(Date.now()-t0<ms){const d=await E(()=>{const C=__G.zone.circ,P=__G.P,N=C.n,i=((P.cs||0)+12)%N;let d=Math.atan2(C.x[i]-P.x,-(C.y[i]-P.y))-P.h;while(d>Math.PI)d-=2*Math.PI;while(d<-Math.PI)d+=2*Math.PI;return d;});if(d>.06){await p.keyboard.down('ArrowRight');await p.keyboard.up('ArrowLeft');}else if(d<-.06){await p.keyboard.down('ArrowLeft');await p.keyboard.up('ArrowRight');}else{await p.keyboard.up('ArrowLeft');await p.keyboard.up('ArrowRight');}await W(60);}await p.keyboard.up('ArrowLeft');await p.keyboard.up('ArrowRight');};
  await drive(6000);await p.screenshot({path:`c-${tag}-b.png`});
  out[tag]=await E(()=>({pProg:Math.round(__G.P.prog),lap:__G.P.lapN,off:Math.round(__G.P.off),riv:__G.rivals.map(c=>Math.round(c.prog)+'/'+Math.round(c.off)).join(' '),rank:__G.P.rank,hl:document.getElementById('hlL').textContent}));
  await drive(6000);await p.screenshot({path:`c-${tag}-c.png`});
  out[tag+'2']=await E(()=>({pProg:Math.round(__G.P.prog),lap:__G.P.lapN,riv:__G.rivals.map(c=>Math.round(c.prog)).join(' ')}));
  await p.keyboard.up('ArrowUp');}
 console.log(JSON.stringify(out,null,0),JSON.stringify(errs.slice(0,5)));await b.close();})();
