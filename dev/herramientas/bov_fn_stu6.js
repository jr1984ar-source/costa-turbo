Snd.bov=function(k){if(!this.ok())return;const c=this.ctx,t0=c.currentTime+.02;k=k||1;this.bovT=t0+1;
 // silbido del turbo que se apaga
 this.tone({at:t0,w:'sine',f:4600,f2:1500,v:.06*k,a:.005,t:.7});
 // "stu" repetido: cada vez más flojo y un poco más grave
 let t=t0,d=.13,a=k,p=1;for(let i=0;i<6;i++){
  this.hiss({at:t,ft:'bandpass',f:2900*p,f2:1300*p,q:1.3,v:.62*a,a:.003,t:.11});
  const u=t+.08;
  this.hiss({at:u,ft:'bandpass',f:3200*p,q:1,v:.33*a,a:.001,t:.014});
  this.hiss({at:u,ft:'bandpass',f:1150*p,f2:450*p,q:2.4,v:1.1*a,a:.003,t:.075});
  this.tone({at:u,w:'triangle',f:260*p,f2:120*p,v:.3*a,a:.003,t:.07});
  t+=d;d*=1.06;a*=.7;p*=.9;}};
