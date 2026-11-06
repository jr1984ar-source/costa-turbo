const Snd={ctx:null,out:null,sfx:null,mus:null,on:store.get('ct_snd',true),musOn:store.get('ct_mus',true),noise:null,eng:null,sir:null,
 init(){const AC=window.AudioContext||window.webkitAudioContext;if(!AC)return;
  if(!this.ctx){try{if(navigator.audioSession)navigator.audioSession.type='playback';}catch(e){}
   try{this.ctx=new AC();}catch(e){return;}const c=this.ctx;
   const comp=c.createDynamicsCompressor();comp.threshold.value=-14;comp.ratio.value=4;comp.connect(c.destination);
   this.out=c.createGain();this.out.gain.value=this.on?.8:0;this.out.connect(comp);
   this.sfx=c.createGain();this.sfx.gain.value=1;this.sfx.connect(this.out);
   this.mus=c.createGain();this.mus.gain.value=this.musOn?.6:0;this.mus.connect(this.out);
   const b=c.createBuffer(1,c.sampleRate*2,c.sampleRate),d=b.getChannelData(0);for(let i=0;i<d.length;i++)d[i]=Math.random()*2-1;this.noise=b;
   try{const s=c.createBufferSource();s.buffer=c.createBuffer(1,1,22050);s.connect(c.destination);s.start(0);}catch(e){}
   if(Music.want){const w=Music.want;Music.want=null;Music.play(w);}}
  if(this.ctx.state!=='running'){try{if(navigator.audioSession)navigator.audioSession.type='playback';}catch(e){}this.ctx.resume().catch(()=>{});}},
 ok(){return this.ctx&&this.on&&this.ctx.state==='running';},
 bg(h){if(!this.ctx)return;this._bg=h;try{if(h){try{if(navigator.audioSession)navigator.audioSession.type='auto';}catch(e){}try{if(navigator.mediaSession){navigator.mediaSession.playbackState='none';navigator.mediaSession.metadata=null;}}catch(e){}this.ctx.suspend().catch(()=>{});}
  else{try{if(navigator.audioSession)navigator.audioSession.type='playback';}catch(e){}if(this.ctx.state!=='running')this.ctx.resume().catch(()=>{});}}catch(e){}},
 setOn(v){this.on=v;store.set('ct_snd',v);if(this.out)this.out.gain.setTargetAtTime(v?.8:0,this.ctx.currentTime,.03);labels();},
 setMus(v){this.musOn=v;store.set('ct_mus',v);if(this.mus)this.mus.gain.setTargetAtTime(v?.6:0,this.ctx.currentTime,.05);labels();},
 tone(o){if(!this.ok())return;const c=this.ctx,t0=o.at!=null?o.at:c.currentTime+(o.d||0),os=c.createOscillator(),g=c.createGain();
  os.type=o.w||'square';os.frequency.setValueAtTime(o.f,t0);if(o.f2)os.frequency.exponentialRampToValueAtTime(o.f2,t0+o.t);
  g.gain.setValueAtTime(.0001,t0);g.gain.exponentialRampToValueAtTime(o.v||.1,t0+(o.a||.006));g.gain.exponentialRampToValueAtTime(.0001,t0+o.t);
  os.connect(g);g.connect(o.bus||this.sfx);os.start(t0);os.stop(t0+o.t+.03);},
 hiss(o){if(!this.ok())return;const c=this.ctx,t0=o.at!=null?o.at:c.currentTime+(o.d||0),s=c.createBufferSource();s.buffer=this.noise;
  const f=c.createBiquadFilter();f.type=o.ft||'lowpass';f.frequency.setValueAtTime(o.f||3000,t0);if(o.f2)f.frequency.exponentialRampToValueAtTime(o.f2,t0+o.t);f.Q.value=o.q||.7;let nd=f;if(o.hp){const h=c.createBiquadFilter();h.type='highpass';h.frequency.value=o.hp;f.connect(h);nd=h;}
  const g=c.createGain();g.gain.setValueAtTime(.0001,t0);g.gain.exponentialRampToValueAtTime(o.v||.2,t0+(o.a||.01));if(o.hold)g.gain.setValueAtTime(o.v||.2,t0+(o.a||.01)+o.hold);g.gain.exponentialRampToValueAtTime(.0001,t0+o.t);
  s.connect(f);nd.connect(g);g.connect(o.bus||this.sfx);s.start(t0,Math.random());s.stop(t0+o.t+.03);},
 curve(k){const n=1024,a=new Float32Array(n);for(let i=0;i<n;i++){const x=i*2/n-1;a[i]=(1+k)*x/(1+k*Math.abs(x));}return a;},
 engineStart(){if(!this.ctx||this.eng)return;const c=this.ctx;
  const o1=c.createOscillator();o1.type='sawtooth';const o2=c.createOscillator();o2.type='square';const o3=c.createOscillator();o3.type='triangle';
  const mx=c.createGain();mx.gain.value=.5;const ws=c.createWaveShaper();ws.curve=this.curve(2);
  const lp=c.createBiquadFilter();lp.type='lowpass';lp.Q.value=3;lp.frequency.value=500;const am=c.createGain();am.gain.value=1;const g=c.createGain();g.gain.value=0;
  o1.connect(mx);o2.connect(mx);o3.connect(mx);mx.connect(ws);ws.connect(lp);lp.connect(am);am.connect(g);g.connect(this.sfx);
  const lfo=c.createOscillator();lfo.type='square';const ld=c.createGain();ld.gain.value=0;lfo.connect(ld);ld.connect(am.gain);
  const sub=c.createOscillator();sub.type='sine';const slp=c.createBiquadFilter();slp.type='lowpass';slp.frequency.value=220;const sg=c.createGain();sg.gain.value=0;sub.connect(slp);slp.connect(sg);sg.connect(this.sfx);
  const rs=c.createOscillator();rs.type='sawtooth';const rbp=c.createBiquadFilter();rbp.type='bandpass';rbp.frequency.value=1500;rbp.Q.value=.9;const rg=c.createGain();rg.gain.value=0;rs.connect(rbp);rbp.connect(rg);rg.connect(this.sfx);
  const wn=c.createBufferSource();wn.buffer=this.noise;wn.loop=true;const wf=c.createBiquadFilter();wf.type='bandpass';wf.frequency.value=900;wf.Q.value=.6;const wg=c.createGain();wg.gain.value=0;wn.connect(wf);wf.connect(wg);wg.connect(this.sfx);
  const wh=c.createOscillator();wh.type='sine';wh.frequency.value=2000;const whg=c.createGain();whg.gain.value=0;wh.connect(whg);whg.connect(this.sfx);
  [o1,o2,o3,lfo,sub,rs,wn,wh].forEach(n=>n.start());this.eng={o1,o2,o3,ws,lp,g,lfo,ld,sub,sg,rs,rg,wn,wg,wf,wh,whg,ex:-1};},
 engineSet(rpm,spd,boost,thr,exh,tur,idle,drift){const e=this.eng;if(!e)return;if(this.bovT&&this.bovT>this.ctx.currentTime)spd*=.3;const t=this.ctx.currentTime,f=30+rpm*92,x=clamp(exh|0,0,3),r1=Math.min(1,rpm);
  if(e.ex!==x){e.ws.curve=this.curve(2+x*3.4);e.ex=x;}
  e.o1.frequency.setTargetAtTime(f,t,.05);e.o2.frequency.setTargetAtTime(f*.5,t,.05);e.o3.frequency.setTargetAtTime(f*2.01,t,.05);
  e.lp.frequency.setTargetAtTime((240+rpm*2000)*(1+x*.16),t,.06);
  e.g.gain.setTargetAtTime(idle?0:(.03+thr*.042+rpm*.042)*[1,1.15,1.32,1.5][x],t,.08);
  e.sub.frequency.setTargetAtTime(f*.5,t,.05);e.sg.gain.setTargetAtTime(idle?0:[0,.03,.045,.06][x]*(.45+rpm*.55),t,.08);
  e.rs.frequency.setTargetAtTime(f*1.5,t,.05);e.rg.gain.setTargetAtTime(idle?0:[0,0,.009,.017][x]*r1*(thr?1:.5),t,.08);
  e.lfo.frequency.setTargetAtTime(f*.5,t,.05);e.ld.gain.setTargetAtTime(idle?0:[0,.12,.22,.32][x]*(1.2-r1*.6),t,.08);
  e.wg.gain.setTargetAtTime(idle?0:drift?.34:spd*.16,t,.06);e.wf.frequency.setTargetAtTime(drift?2600:500+spd*1400,t,.08);
  e.whg.gain.setTargetAtTime(idle?0:(tur?.004+rpm*.009:0)+boost*.02,t,.08);e.wh.frequency.setTargetAtTime(1400+rpm*2600+boost*1500,t,.08);},
 engineStop(){const e=this.eng;if(!e)return;this.eng=null;const t=this.ctx.currentTime;[e.g,e.sg,e.rg,e.wg,e.whg].forEach(g=>g.gain.setTargetAtTime(0,t,.05));[e.o1,e.o2,e.o3,e.lfo,e.sub,e.rs,e.wn,e.wh].forEach(n=>{try{n.stop(t+.4);}catch(_){}});},
 pops(st,level){if(!this.ok()||st<2)return;const n=st>=3?9+Math.floor(Math.random()*4):4+Math.floor(Math.random()*2);let t=this.ctx.currentTime+.05;for(let i=0;i<n;i++){const v=(st>=3?.95:.65)*(.6+Math.random()*.4)*(.6+clamp(level,0,1)*.4);
  this.hiss({at:t,ft:'bandpass',f:2800+Math.random()*900,q:.7,t:.014,v:v*1.1,a:.001});this.hiss({at:t,ft:'lowpass',f:1300+Math.random()*700,q:.7,t:.05,v:v*.95,a:.002});this.tone({at:t,w:'sine',f:115,f2:42,t:.08,v:v*1.05,a:.003});t+=.045+Math.random()*.12;}},
 sirenStart(){if(!this.ok()||this.sir)return;const c=this.ctx,o=c.createOscillator();o.type='square';const lp=c.createBiquadFilter();lp.type='lowpass';lp.frequency.value=2200;const g=c.createGain();g.gain.value=0;o.connect(lp);lp.connect(g);g.connect(this.sfx);o.start();this.sir={o,g,ph:0};},
 sirenTick(dt,vol){const s=this.sir;if(!s)return;s.ph+=dt;const t=this.ctx.currentTime;s.o.frequency.setTargetAtTime((s.ph%.9)<.45?740:990,t,.01);s.g.gain.setTargetAtTime(.035*vol,t,.05);},
 sirenStop(){const s=this.sir;if(!s)return;this.sir=null;try{const t=this.ctx.currentTime;s.g.gain.setTargetAtTime(0,t,.05);s.o.stop(t+.3);}catch(_){}},
 coin(){this.tone({w:'square',f:1320,t:.05,v:.05});this.tone({w:'square',f:1980,t:.12,v:.05,d:.05});},
 jump(){this.hiss({ft:'bandpass',f:600,f2:2400,t:.35,v:.18,q:1.2});},
 land(){this.hiss({f:1800,f2:200,t:.5,v:.35});this.tone({w:'sine',f:120,f2:50,t:.25,v:.25});},
 crash(){this.hiss({f:2600,f2:120,t:.6,v:.45});this.tone({w:'sine',f:90,f2:40,t:.35,v:.5});this.tone({w:'square',f:160,f2:60,t:.2,v:.08});},
 bump(){this.tone({w:'sine',f:140,f2:70,t:.15,v:.25});},
 boost(){this.hiss({ft:'bandpass',f:400,f2:3000,t:.5,v:.22,q:1.5});this.tone({w:'sawtooth',f:220,f2:660,t:.4,v:.06});},
 bovA(k){const c=this.ctx,t0=c.currentTime+.01;this.bovT=t0+1;
  const h1=c.createBiquadFilter(),h2=c.createBiquadFilter();h1.type=h2.type='highpass';h1.frequency.value=h2.frequency.value=400;h1.Q.value=h2.Q.value=.707;h1.connect(h2);h2.connect(this.sfx);const bus=h1;
  this.tone({at:t0,w:'sine',f:4600,f2:1500,v:.06*k,a:.005,t:.7,bus});
  this.hiss({at:t0,ft:'bandpass',f:2900,f2:1300,q:1.3,v:.62*k,a:.003,t:.11,bus});
  const u=t0+.08;this.hiss({at:u,ft:'bandpass',f:3200,q:1,v:.33*k,a:.001,t:.014,bus});this.hiss({at:u,ft:'bandpass',f:1150,f2:450,q:2.4,v:1.1*k,a:.003,t:.075,bus});this.tone({at:u,w:'triangle',f:260,f2:120,v:.3*k,a:.003,t:.07,bus});
  const st=Math.pow(10,-3/20);let a=k*st,p=1,t=t0+.13,d=.137;
  for(let i=0;i<5;i++){p*=.95;this.hiss({at:t,ft:'bandpass',f:2900*p,f2:1300*p,q:1.3,v:.62*a,a:.003,t:.11,bus});this.hiss({at:t+.08,ft:'bandpass',f:2100*p,f2:1400*p,q:3,v:.45*a,a:.002,t:.05,bus});t+=d;d*=1.06;a*=st;}},
 bov(st,sp){if(!this.ok())return;st=clamp(st|0,1,3);sp=clamp(sp||0,0,1);if(st===3){this.bovA(.6+.4*sp);return;}const t0=this.ctx.currentTime+.01,k=[0,.85,1,1.1][st]*(.55+.45*sp),dur=[0,.42,.72,.9][st];
  this.hiss({at:t0,ft:'bandpass',f:2300,q:.9,t:.06,v:.55*k,a:.002});
  this.hiss({at:t0,ft:'bandpass',f:6800,f2:1700,q:.75,hp:850,t:dur,v:.34*k,a:.006,hold:dur*.14});
  this.hiss({at:t0+.01,ft:'lowpass',f:1500,f2:480,t:dur*.8,v:.13*k,a:.012});
  if(st>=2)this.tone({at:t0,w:'sine',f:3200,f2:1300,t:.09,v:.05*k,a:.004});
  this.tone({at:t0,w:'sine',f:7400,f2:2500,t:dur*1.35,v:(st>1?.045:.03)*k,a:.012});
  if(st===3){let t=t0+.06;for(let i=0;i<9;i++){const fall=1-i/11;this.hiss({at:t,ft:'lowpass',f:1150,f2:620,q:1,t:.036,v:.24*k*fall,a:.003});this.tone({at:t,w:'sine',f:98,f2:70,t:.045,v:.13*k*fall,a:.003});t+=.04+i*.006;}}},
 check(){[784,988,1318].forEach((f,i)=>this.tone({w:'square',f,t:.1,v:.06,d:i*.07}));},
 gate(){this.tone({w:'triangle',f:880,f2:1320,t:.12,v:.1});},
 miss(){this.tone({w:'square',f:300,f2:150,t:.25,v:.07});},
 pickup(){[660,880,1320].forEach((f,i)=>this.tone({w:'square',f,t:.08,v:.06,d:i*.05}));},
 cash(){this.tone({w:'square',f:2093,t:.08,v:.05});this.tone({w:'square',f:2637,t:.25,v:.06,d:.08});this.hiss({ft:'highpass',f:6000,t:.15,v:.08});},
 girls(){this.tone({w:'sine',f:900,f2:1500,t:.18,v:.07});this.tone({w:'sine',f:1500,f2:1100,t:.25,v:.07,d:.2});},
 gull(){this.tone({w:'sawtooth',f:1500,f2:900,t:.22,v:.025});this.tone({w:'sawtooth',f:1400,f2:800,t:.2,v:.02,d:.28});},
 beep(hi){this.tone({w:'square',f:hi?1320:660,t:hi?.5:.18,v:.09});},
 fine(){this.tone({w:'square',f:520,t:.15,v:.07});this.tone({w:'square',f:390,t:.3,v:.07,d:.16});},
 thunder(){this.hiss({f:400,f2:40,t:2.4,v:.55,a:.05});},
 win(){[523,659,784,1047,784,1047,1319].forEach((f,i)=>this.tone({w:'square',f,t:.14,v:.06,d:i*.11}));},
 fail(){[523,466,415,349].forEach((f,i)=>this.tone({w:'triangle',f,t:.3,v:.14,d:i*.22}));},
 click(){this.tone({w:'square',f:660,f2:990,t:.04,v:.035});},
 warn(){this.tone({w:'square',f:880,t:.08,v:.05});this.tone({w:'square',f:880,t:.08,v:.05,d:.14});}
};