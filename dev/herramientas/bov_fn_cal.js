Snd.bov=function(k,vr){if(!this.ok())return;const c=this.ctx,t0=c.currentTime+.02;k=k||1;this.bovT=t0+1;
 // corte de graves: nada por debajo de 400 Hz
 const h1=c.createBiquadFilter(),h2=c.createBiquadFilter();h1.type=h2.type='highpass';h1.frequency.value=h2.frequency.value=400;h1.Q.value=h2.Q.value=.707;h1.connect(h2);h2.connect(this.sfx);const bus=h1;
 // silbido del turbo que se apaga
 if(0)this.tone({at:t0,w:'sine',f:4600,f2:1500,v:.06*k,a:.005,t:.7,bus});
 // "stu" (el que gusta)
 this.hiss({at:t0,ft:'bandpass',f:2900,f2:1300,q:1.3,v:.62*k,a:.003,t:.11,bus});
 const u=t0+.08;
 this.hiss({at:u,ft:'bandpass',f:3200,q:1,v:.33*k,a:.001,t:.014,bus});
 this.hiss({at:u,ft:'bandpass',f:1150,f2:450,q:2.4,v:1.1*k,a:.003,t:.075,bus});
 this.tone({at:u,w:'triangle',f:260,f2:120,v:.3*k,a:.003,t:.07,bus});
 // repeticiones de aire, sin golpe grave; cada una 3 dB más baja
 const st=Math.pow(10,-3/20);let a=k*st,p=1;
 if(vr==='B'){let t=t0+.17,d=.055;for(let i=0;i<8;i++){
   this.hiss({at:t,ft:'bandpass',f:2700*p,f2:1800*p,q:3.5,v:.55*a,a:.002,t:.038,bus});
   t+=d;d*=1.04;a*=st;p*=.96;}}
 else{let t=t0+.13,d=.137;for(let i=0;i<5;i++){p*=.95;
   this.hiss({at:t,ft:'bandpass',f:2900*p,f2:1300*p,q:1.3,v:.62*a,a:.003,t:.11,bus});
   this.hiss({at:t+.08,ft:'bandpass',f:2100*p,f2:1400*p,q:3,v:.45*a,a:.002,t:.05,bus});
   t+=d;d*=1.06;a*=st;}}};
