Snd.bov=function(k){if(!this.ok())return;const c=this.ctx,t0=c.currentTime+.02;k=k||1;this.bovT=t0+1;
 // silbido del turbo que se apaga
 this.tone({at:t0,w:'sine',f:4600,f2:1500,v:.06*k,a:.005,t:.75});
 // soplido inicial "sss-t"
 this.hiss({at:t0,ft:'bandpass',f:2900,f2:1300,q:1.3,v:.62*k,a:.003,t:.11});
 // flutter "tu-tu-tu-tu" (más golpes y más fuerte)
 let t=t0+.08,d=.05;for(let i=0;i<12;i++){const a=k*Math.pow(.86,i)*(.85+Math.random()*.3);
  this.hiss({at:t,ft:'bandpass',f:3200,q:1,v:.33*a,a:.001,t:.014});
  this.hiss({at:t,ft:'bandpass',f:1150,f2:450,q:2.4,v:1.1*a,a:.003,t:d*.78});
  this.tone({at:t,w:'triangle',f:260,f2:120,v:.3*a,a:.003,t:d*.72});
  t+=d;d*=1.06;}};
