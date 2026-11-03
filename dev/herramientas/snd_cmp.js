const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
 const res=await p.evaluate(async([A,B])=>{const out={};
  for(const [nm,src] of [['antes',A],['ahora',B]]){for(const kind of ['bov3','bov2','pops']){let E=0;for(let rep=0;rep<6;rep++){
   const store={get:(k,d)=>d,set(){}},clamp=(v,a,b)=>Math.max(a,Math.min(b,v)),Music={};const Snd=new Function('store','clamp','Music',src+';return Snd')(store,clamp,Music);
   const SR=44100,c=new OfflineAudioContext(1,SR*2,SR);Snd.ctx=c;Snd.out=c.createGain();Snd.out.gain.value=.8;Snd.out.connect(c.destination);Snd.sfx=c.createGain();Snd.sfx.connect(Snd.out);
   const nb=c.createBuffer(1,SR*2,SR),d=nb.getChannelData(0);for(let i=0;i<d.length;i++)d[i]=Math.random()*2-1;Snd.noise=nb;Snd.ok=()=>true;
   c.suspend(.1).then(()=>{if(kind==='bov3')Snd.bov(3,1);else if(kind==='bov2')Snd.bov(2,1);else Snd.pops(3,1);c.resume();});
   const x=(await c.startRendering()).getChannelData(0);for(let i=0;i<x.length;i++)E+=x[i]*x[i];}
   out[nm+'_'+kind]=10*Math.log10(E);}}
  return out;},[fs.readFileSync('snd_old.js','utf8'),fs.readFileSync('snd_new.js','utf8')]);
 for(const k of ['bov3','bov2','pops'])console.log(k,'cambio dB',(res['ahora_'+k]-res['antes_'+k]).toFixed(2));await b.close();})();
