const {chromium}=require('playwright');const fs=require('fs');
const CLIPS=[['escape-nuevo-stage2-petardos','new',2],['escape-nuevo-stage3-petardos','new',3]];
(async()=>{const b=await chromium.launch();const p=await b.newPage();await p.goto('about:blank');
 for(const [name,ver,st] of CLIPS){
  const b64=await p.evaluate(async([ver,st])=>{
   const SR=44100,DUR=4.8,ctx=new OfflineAudioContext(1,Math.ceil(SR*DUR),SR);
   const comp=ctx.createDynamicsCompressor();comp.threshold.value=-14;comp.ratio.value=4;comp.connect(ctx.destination);const out=ctx.createGain();out.gain.value=.8;out.connect(comp);
   const len=SR*2,noise=ctx.createBuffer(1,len,SR),nd=noise.getChannelData(0);for(let i=0;i<len;i++)nd[i]=Math.random()*2-1;
   const curve=k=>{const n=1024,a=new Float32Array(n);for(let i=0;i<n;i++){const x=i*2/n-1;a[i]=(1+k)*x/(1+k*Math.abs(x));}return a;};
   const c=ctx,nw=ver==='new',x=st;
   const o1=c.createOscillator();o1.type='sawtooth';const o2=c.createOscillator();o2.type='square';const o3=c.createOscillator();o3.type='triangle';
   const mx=c.createGain();mx.gain.value=.5;const ws=c.createWaveShaper();ws.curve=curve(nw?2+x*3.4:2+x*2.5);const lp=c.createBiquadFilter();lp.type='lowpass';lp.Q.value=3;lp.frequency.value=500;
   const am=c.createGain();am.gain.value=1;const g=c.createGain();g.gain.value=0;
   o1.connect(mx);o2.connect(mx);o3.connect(mx);mx.connect(ws);ws.connect(lp);lp.connect(am);am.connect(g);g.connect(out);
   const lfo=c.createOscillator();lfo.type='square';const ld=c.createGain();ld.gain.value=0;lfo.connect(ld);ld.connect(am.gain);
   const sub=c.createOscillator();sub.type='sine';const slp=c.createBiquadFilter();slp.type='lowpass';slp.frequency.value=220;const sg=c.createGain();sg.gain.value=0;sub.connect(slp);slp.connect(sg);sg.connect(out);
   const rs=c.createOscillator();rs.type='sawtooth';const rhp=c.createBiquadFilter();rhp.type='bandpass';rhp.frequency.value=1500;rhp.Q.value=.9;const rg=c.createGain();rg.gain.value=0;rs.connect(rhp);rhp.connect(rg);rg.connect(out);
   const wn=c.createBufferSource();wn.buffer=noise;wn.loop=true;const wf=c.createBiquadFilter();wf.type='bandpass';wf.frequency.value=900;wf.Q.value=.6;const wg=c.createGain();wg.gain.value=0;wn.connect(wf);wf.connect(wg);wg.connect(out);
   [o1,o2,o3,lfo,sub,rs,wn].forEach(n=>n.start(0));
   const set=(t,rpm,spd,th)=>{const f=30+rpm*92;
    o1.frequency.setTargetAtTime(f,t,.05);o2.frequency.setTargetAtTime(f*.5,t,.05);o3.frequency.setTargetAtTime(f*2.01,t,.05);
    lp.frequency.setTargetAtTime(nw?(240+rpm*2000)*(1+x*.16):(260+rpm*2100)*(1+x*.1),t,.06);
    const base=.03+th*.042+rpm*.042;g.gain.setTargetAtTime(base*(nw?[1,1.15,1.32,1.5][x]:1+x*.18),t,.08);
    sub.frequency.setTargetAtTime(f*.5,t,.05);sg.gain.setTargetAtTime(nw?[0,.03,.045,.06][x]*(.45+rpm*.55):0,t,.08);
    rs.frequency.setTargetAtTime(f*1.5,t,.05);rg.gain.setTargetAtTime(nw?[0,0,.009,.017][x]*rpm*(th?1:.5):0,t,.08);
    lfo.frequency.setTargetAtTime(f*.5,t,.05);ld.gain.setTargetAtTime(nw?[0,.12,.22,.32][x]*(1.2-Math.min(1,rpm)*.6):0,t,.08);
    wg.gain.setTargetAtTime(spd*.16,t,.06);wf.frequency.setTargetAtTime(500+spd*1400,t,.08);};
   const burst=(at,v)=>{const mk=(ft,fr,q,a,dur,vv)=>{const s=c.createBufferSource();s.buffer=noise;const f=c.createBiquadFilter();f.type=ft;f.frequency.value=fr;f.Q.value=q;const gg=c.createGain();gg.gain.setValueAtTime(.0001,at);gg.gain.exponentialRampToValueAtTime(vv,at+a);gg.gain.exponentialRampToValueAtTime(.0001,at+dur);s.connect(f);f.connect(gg);gg.connect(out);s.start(at,Math.random());s.stop(at+dur+.03);};
    mk('bandpass',2800+Math.random()*900,.7,.001,.014,v*1.1);mk('lowpass',1300+Math.random()*700,.7,.002,.05,v*.95);
    const o=c.createOscillator();o.type='sine';o.frequency.setValueAtTime(115,at);o.frequency.exponentialRampToValueAtTime(42,at+.07);const og=c.createGain();og.gain.setValueAtTime(.0001,at);og.gain.exponentialRampToValueAtTime(v*1.05,at+.003);og.gain.exponentialRampToValueAtTime(.0001,at+.08);o.connect(og);og.connect(out);o.start(at);o.stop(at+.1);};
   let r=0,thr=false;const T_ON=.6,T_OFF=2.9,dt=1/120;
   for(let t=0;t<DUR;t+=dt){const th=t>=T_ON&&t<T_OFF;if(thr&&!th&&nw&&x>=2&&r>=.55){const n=x===3?10:5;let tt=t+.05;for(let i=0;i<n;i++){burst(tt,(x===3?.95:.65)*(.7+((i*37)%10)/30)*(.6+r*.4));tt+=.045+((i*53)%13)/100;}}
    thr=th;if(thr)r+=(1-r)*dt*.9;else r-=r*dt*.75;r=Math.max(0,Math.min(1,r));const rpm=Math.min(1.3,.18+r*.72+(thr?.12:0));set(t,rpm,r,thr?1:0);}
   const buf=await ctx.startRendering(),d=buf.getChannelData(0);
   let pk=0;for(let i=0;i<d.length;i++)pk=Math.max(pk,Math.abs(d[i]));const gain=2.1;
   const n=d.length,ab=new ArrayBuffer(44+n*2),v=new DataView(ab);const ws2=(o,s)=>{for(let i=0;i<s.length;i++)v.setUint8(o+i,s.charCodeAt(i));};
   ws2(0,'RIFF');v.setUint32(4,36+n*2,true);ws2(8,'WAVE');ws2(12,'fmt ');v.setUint32(16,16,true);v.setUint16(20,1,true);v.setUint16(22,1,true);v.setUint32(24,SR,true);v.setUint32(28,SR*2,true);v.setUint16(32,2,true);v.setUint16(34,16,true);ws2(36,'data');v.setUint32(40,n*2,true);
   for(let i=0;i<n;i++){const s=Math.tanh(d[i]*gain)*.97;v.setInt16(44+i*2,s<0?s*0x8000:s*0x7fff,true);}
   let bin='';const u=new Uint8Array(ab);for(let i=0;i<u.length;i+=0x8000)bin+=String.fromCharCode.apply(null,u.subarray(i,i+0x8000));return [btoa(bin),pk];
  },[ver,st]);
  fs.writeFileSync('audios/'+name+'.wav',Buffer.from(b64[0],'base64'));console.log(name,'peak',b64[1].toFixed(3));}
 await b.close();})();
