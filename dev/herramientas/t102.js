const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},'BAHAMAS');await W(300);await E(()=>__T.startRace());await W(3800);
 const r=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30;let t=0;while(t<18&&G.mode==='play'){const a=__aiCirc(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__upd(dt);t+=dt;}
  const pr=CanvasRenderingContext2D.prototype,cnt={};const hook=(name)=>{const o=pr[name];pr[name]=function(...a){const fs=String(name==='stroke'?this.strokeStyle:this.fillStyle);if(/^#(f[0-9a-f]{1}[c-f][0-9a-f]{1}[0-4][0-9a-f])|^#ff[cd]/i.test(fs)||/rgba?\(2[45]\d, ?2[0-2]\d, ?[0-9]{1,2},/.test(fs)){const st=(new Error().stack||'').split('\n').slice(2,5).map(s=>s.trim().replace(/\(.*\//,'(')).join(' < ');const k=fs+' | '+st;cnt[k]=(cnt[k]||0)+1;}return o.apply(this,a);};};
  hook('fill');hook('stroke');hook('fillRect');__render();return Object.entries(cnt).sort((a,b)=>b[1]-a[1]).slice(0,25);});
 for(const x of r)console.log(x[1],x[0]);
 await b.close();})();
