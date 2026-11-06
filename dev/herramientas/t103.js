const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},'BAHAMAS');await W(300);await E(()=>__T.startRace());await W(3800);
 const r=await E(()=>{window.requestAnimationFrame=()=>0;const G=__G,P=G.P,dt=1/30;let t=0;const cnt={};let on=false;
  const pr=CanvasRenderingContext2D.prototype;const hook=(name)=>{const o=pr[name];pr[name]=function(...a){if(on){const fs=String(name==='stroke'?this.strokeStyle:this.fillStyle);let m=/^#([0-9a-f]{6})$/i.exec(fs);if(m){const v=parseInt(m[1],16),R=v>>16,Gg=(v>>8)&255,B=v&255;const red=R>180&&Gg<90&&B<90,blue=B>170&&R<80&&Gg<140,yel=R>220&&Gg>180&&B<60;if(red||blue||yel){const st=(new Error().stack||'').split('\n').slice(2,4).map(s=>s.trim().replace(/^at /,'').replace(/\(.*html:/,'(')).join(' < ');const k=(red?'RED ':blue?'BLUE ':'YEL ')+st;cnt[k]=(cnt[k]||0)+1;}}}return o.apply(this,a);};};
  hook('fill');hook('stroke');hook('fillRect');hook('drawImage');
  let nx=0;while(t<110&&G.mode==='play'){const a=__aiCirc(P,dt);__input.acc=a.thr;__input.left=a.turn<0;__input.right=a.turn>0;__upd(dt);t+=dt;if(t>nx){nx+=1;on=true;__render();on=false;}}
  return Object.entries(cnt).sort((a,b)=>b[1]-a[1]).slice(0,30);});
 for(const x of r)console.log(x[1],x[0]);
 await b.close();})();
