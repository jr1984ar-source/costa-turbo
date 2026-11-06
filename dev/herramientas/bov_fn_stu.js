Snd.bov=function(k){if(!this.ok())return;const c=this.ctx,t0=c.currentTime+.02;k=k||1;this.bovT=t0+.5;
 // silbido del turbo que se apaga
 this.tone({at:t0,w:'sine',f:4600,f2:1500,v:.06*k,a:.005,t:.6});
 // "s": soplido inicial
 this.hiss({at:t0,ft:'bandpass',f:2900,f2:1300,q:1.3,v:.62*k,a:.003,t:.11});
 // "tu": un solo golpe, sin repetir
 const t=t0+.08;
 this.hiss({at:t,ft:'bandpass',f:3200,q:1,v:.33*k,a:.001,t:.014});
 this.hiss({at:t,ft:'bandpass',f:1150,f2:450,q:2.4,v:1.1*k,a:.003,t:.075});
 this.tone({at:t,w:'triangle',f:260,f2:120,v:.3*k,a:.003,t:.07});};
