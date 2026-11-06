const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
 const src=fs.readFileSync('snd_src.js','utf8'),fn=fs.readFileSync('bov_fn.js','utf8');
 const b64=await p.evaluate(async([src,fn])=>{
  const store={get:(k,d)=>d,set(){}},clamp=(v,a,b)=>Math.max(a,Math.min(b,v)),Music={};
  const Snd=new Function('store','clamp','Music',src+fn+';return Snd')(store,clamp,Music);
  const SR=44100,DUR=10.6,c=new OfflineAudioContext(1,Math.ceil(SR*DUR),SR);
  const comp=c.createDynamicsCompressor();comp.threshold.value=-14;comp.ratio.value=4;comp.connect(c.destination);
  Snd.ctx=c;Snd.out=c.createGain();Snd.out.gain.value=.8;Snd.out.connect(comp);Snd.sfx=c.createGain();Snd.sfx.connect(Snd.out);
  const nb=c.createBuffer(1,SR*2,SR),d=nb.getChannelData(0);for(let i=0;i<d.length;i++)d[i]=Math.random()*2-1;Snd.noise=nb;Snd.ok=()=>true;
  const at=(t,f)=>c.suspend(t).then(()=>{f();c.resume();});
  at(.2,()=>Snd.bov(1));at(1.4,()=>Snd.bov(1));
  let r=0,thr=0,on=0;const thrOn=[[3.3,5.6],[6.6,8.4]];
  at(2.8,()=>{Snd.engineStart();on=1;});
  const dt=1/40;for(let t=2.8+dt;t<10.2;t+=dt){const tt=t;at(tt,()=>{const want=thrOn.some(([a,b])=>tt>=a&&tt<b)?1:0;
    if(thr&&!want&&r>.5)Snd.bov(Math.min(1,Math.max(.45,(r-.4)/.5)));thr=want;
    r+=thr?.55*dt*(1-r)*1.6:-.15*dt*r;const rpm=clamp(.18+r*.72+(thr?.12:0),0,1.3);Snd.engineSet(rpm,Snd.bovT>c.currentTime?r*.3:r,0,thr,0,0,0,0);});}
  at(10.2,()=>Snd.engineStop());
  const buf=await c.startRendering(),x=buf.getChannelData(0);
  const n=x.length,ab=new ArrayBuffer(44+n*2),v=new DataView(ab);const w=(o,s)=>{for(let i=0;i<s.length;i++)v.setUint8(o+i,s.charCodeAt(i));};
  w(0,'RIFF');v.setUint32(4,36+n*2,true);w(8,'WAVE');w(12,'fmt ');v.setUint32(16,16,true);v.setUint16(20,1,true);v.setUint16(22,1,true);v.setUint32(24,SR,true);v.setUint32(28,SR*2,true);v.setUint16(32,2,true);v.setUint16(34,16,true);w(36,'data');v.setUint32(40,n*2,true);
  let pk=0;for(let i=0;i<n;i++){const s=Math.max(-1,Math.min(1,x[i]));pk=Math.max(pk,Math.abs(s));v.setInt16(44+i*2,s*32767,true);}
  let bin='';const u=new Uint8Array(ab);for(let i=0;i<u.length;i+=8192)bin+=String.fromCharCode.apply(null,u.subarray(i,i+8192));return [btoa(bin),pk];},[src,fn]);
 fs.writeFileSync('bov.wav',Buffer.from(b64[0],'base64'));console.log('peak',b64[1]);await b.close();})();
