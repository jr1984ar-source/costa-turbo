Snd.bov=function(k){if(!this.ok())return;const c=this.ctx,t0=c.currentTime+.02;k=k||1;this.bovT=t0+1;
 // corte de graves: nada por debajo de 400 Hz (dos filtros seguidos = corte fuerte)
 const h1=c.createBiquadFilter(),h2=c.createBiquadFilter();h1.type=h2.type='highpass';h1.frequency.value=h2.frequency.value=400;h1.Q.value=h2.Q.value=.707;h1.connect(h2);h2.connect(this.sfx);const bus=h1;
 // silbido del turbo que se apaga
 this.tone({at:t0,w:'sine',f:4600,f2:1500,v:.06*k,a:.005,t:.7,bus});
 // "stu" repetido: cada vez más flojo y un poco más grave
 const g=[1,.722,.508,.382,.263,.193];// cada "stu" 3 dB más bajo que el anterior (medido)
 let t=t0,d=.13,a=k,p=1;for(let i=0;i<6;i++){a=k*g[i];
  this.hiss({at:t,ft:'bandpass',f:2900*p,f2:1300*p,q:1.3,v:.62*a,a:.003,t:.11,bus});
  const u=t+.08;
  this.hiss({at:u,ft:'bandpass',f:3200*p,q:1,v:.33*a,a:.001,t:.014,bus});
  this.hiss({at:u,ft:'bandpass',f:1150*p,f2:450*p,q:2.4,v:1.1*a,a:.003,t:.075,bus});
  this.tone({at:u,w:'triangle',f:260*p,f2:120*p,v:.3*a,a:.003,t:.07,bus});
  t+=d;d*=1.06;p*=.9;}};
