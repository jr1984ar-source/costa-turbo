const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
 const src=fs.readFileSync('snd_src102.js','utf8'),demo=fs.readFileSync('bov_fn.js','utf8');
 const out=await p.evaluate(async([src,demo])=>{
  const store={get:(k,d)=>d,set(){}},clamp=(v,a,b)=>Math.max(a,Math.min(b,v)),Music={};
  const res={};
  for(const mode of ['juego3','demoA','juego1','juego2']){
   const Snd=new Function('store','clamp','Music',src+(mode==='demoA'?demo:'')+';return Snd')(store,clamp,Music);
   const SR=44100,c=new OfflineAudioContext(1,SR*2,SR);const comp=c.createDynamicsCompressor();comp.threshold.value=-14;comp.ratio.value=4;comp.connect(c.destination);
   Snd.ctx=c;Snd.out=c.createGain();Snd.out.gain.value=.8;Snd.out.connect(comp);Snd.sfx=c.createGain();Snd.sfx.connect(Snd.out);
   const nb=c.createBuffer(1,SR*2,SR),d=nb.getChannelData(0);for(let i=0;i<d.length;i++)d[i]=Math.random()*2-1;Snd.noise=nb;Snd.ok=()=>true;
   c.suspend(.1).then(()=>{if(mode==='demoA')Snd.bov(1,'A');else Snd.bov(+mode.slice(-1),1);c.resume();});
   const x=(await c.startRendering()).getChannelData(0);const env=[];for(let k=0;k<14;k++){let e=0;const a=Math.floor((.1+k*.07)*SR),bb=Math.floor((.1+(k+1)*.07)*SR);for(let i=a;i<bb;i++)e+=x[i]*x[i];env.push(+(10*Math.log10(e/(bb-a)+1e-12)).toFixed(1));}
   res[mode]=env;}
  return res;},[src,demo]);
 for(const k in out)console.log(k.padEnd(7),out[k].join(' '));await b.close();})();
