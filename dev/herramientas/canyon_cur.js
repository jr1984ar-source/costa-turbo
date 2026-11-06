function buildCanyon(Z,zi,lap,seed){const r=rng(seed),def=CIRCS[Z.circ],step=8,W=def.W,raw=[];let x=0,y=0,h=def.h0*Math.PI/180;raw.push([x,y]);
 for(const sg of def.segs){if(sg[0]==='S'){const n=Math.max(1,Math.round(sg[1]/4));for(let i=0;i<n;i++){x+=Math.sin(h)*sg[1]/n;y-=Math.cos(h)*sg[1]/n;raw.push([x,y]);}}
  else{const sgn=sg[0]==='R'?1:-1,a=sg[1]*Math.PI/180,Lr=a*sg[2],n=Math.max(1,Math.round(Lr/4));for(let i=0;i<n;i++){h+=sgn*a/n/2;x+=Math.sin(h)*Lr/n;y-=Math.cos(h)*Lr/n;h+=sgn*a/n/2;raw.push([x,y]);}}}
 const R=raw.length,cl=[0];for(let i=1;i<R;i++)cl.push(cl[i-1]+Math.hypot(raw[i][0]-raw[i-1][0],raw[i][1]-raw[i-1][1]));const LL=cl[R-1];
 const xs=[],ys=[];let j=0;for(let sd=0;sd<=LL;sd+=step){while(j<R-2&&cl[j+1]<sd)j++;const a=raw[j],b=raw[j+1],t=(sd-cl[j])/((cl[j+1]-cl[j])||1);xs.push(a[0]+(b[0]-a[0])*t);ys.push(a[1]+(b[1]-a[1])*t);}
 const N=xs.length,hs=[],cum=[];for(let i=0;i<N;i++){const a=Math.max(0,i-1),b=Math.min(N-1,i+1);hs.push(Math.atan2(xs[b]-xs[a],-(ys[b]-ys[a])));cum.push(i*step);}
 const Lp=(N-1)*step,C={x:xs,y:ys,h:hs,cum,n:N,L:Lp,step,W,laps:1,open:1,canyon:1,finS:Lp-260},O=[],add=o=>{O.push(o);return o;};
 const I=s=>Math.max(0,Math.min(N-1,Math.round(s/step))),P=(s,d)=>{const i=I(s);return[xs[i]+Math.cos(hs[i])*d,ys[i]+Math.sin(hs[i])*d];};
 // ---- anchura variable, costa escarpada y calas ----
 const rr=rng(seed+5),nW=noise1(seed+41),nA=noise1(seed+43),nB=noise1(seed+47),nC=noise1(seed+53),nD=noise1(seed+59),nE=noise1(seed+61),nF=noise1(seed+67);
 const archS=[40,Math.round(Lp/3),Math.round(Lp*2/3),C.finS],ev=[],cov=[];
 for(let s=1100;s<Lp-1100;s+=1100+rr()*900)ev.push({s,w:260+rr()*220,a:rr()<.5?-70:100});
 for(let s=650;s<Lp-650;s+=300+rr()*420)cov.push({s,side:rr()<.5?-1:1,w:55+rr()*75,d:55+rr()*85});
 const bump=(d,w)=>{const t=Math.abs(d)/w;return t>=1?0:(1-t*t)*(1-t*t);};
 const calm=s=>{let k=Math.min(sm(60,260,s),sm(Lp-60,Lp-420,s));for(const a of archS)k=Math.min(k,sm(40,170,Math.abs(s-a)));return k;};
 const wl=[],wr=[];
 for(let i=0;i<N;i++){const s=i*step,k=calm(s);let hb=W/2+44*nW(s/950);for(const e of ev)hb+=e.a*bump(s-e.s,e.w);
  for(const sd of[-1,1]){const n=sd<0?[nA,nB,nC]:[nD,nE,nF];let o=hb+22*n[0](s/120)+11*n[1](s/42)+6*n[2](s/14);for(const c of cov)if(c.side===sd)o+=c.d*bump(s-c.s,c.w);o=lerp(W/2,clamp(o,140,360),k);(sd<0?wl:wr).push(o);}}
 // que no se coma la roca entre tramos cercanos del cañón
 for(let i=0;i<N;i++)for(const sd of[-1,1]){const A=sd<0?wl:wr;let o=A[i];const nx=Math.cos(hs[i])*sd,ny=Math.sin(hs[i])*sd;
  for(let it=0;it<8;it++){const ex=xs[i]+nx*o,ey=ys[i]+ny*o;let bad=false;for(let q=0;q<N;q+=3){if(Math.abs(q-i)*step<1300)continue;const dd=Math.hypot(xs[q]-ex,ys[q]-ey);if(dd<Math.max(wl[q],wr[q])+80){bad=true;break;}}if(!bad)break;o=Math.max(140,o-24);}A[i]=o;}
 C.wl=wl;C.wr=wr;C.edgeL=[];C.edgeR=[];for(let i=0;i<N;i++){const nx=Math.cos(hs[i]),ny=Math.sin(hs[i]);C.edgeL.push([xs[i]-nx*wl[i],ys[i]-ny*wl[i]]);C.edgeR.push([xs[i]+nx*wr[i],ys[i]+ny*wr[i]]);}
 C.arches=[{s:40,txt:'SALIDA',col:'#ffc93c'},{s:Math.round(Lp/3),txt:'CONTROL',col:'#7be35a'},{s:Math.round(Lp*2/3),txt:'CONTROL',col:'#7be35a'},{s:C.finS,txt:'META',col:'#ffc93c'}].map(a=>{const i=I(a.s);return Object.assign(a,{x:xs[i],y:ys[i],h:hs[i]});});
 C.cps=[{s:Math.round(Lp/3)},{s:Math.round(Lp*2/3)}];C.beach=I(Lp-170);
 {const i=I(C.finS);add({t:'cline',x:xs[i],y:ys[i],h:hs[i],w:W});}
 for(let i=40;i<N-40;i+=34)add({t:'carrow',x:xs[i],y:ys[i],h:hs[i]});
 const coinS=[];for(let s=420;s<Lp-420;s+=360+r()*200){const lat=(r()-.5)*W*.5;coinS.push(s);for(let k=0;k<6;k++){const i=I(s+k*26);add({t:'coin',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat});}}
 for(let s=900;s<Lp-700;s+=620+r()*520){if(coinS.some(q=>Math.abs(q-s)<200))s+=220;const i=I(s),sd=r()<.5?-1:1,lat=sd*((sd<0?wl[i]:wr[i])-45-r()*60);add({t:'rock',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat,rad:10+r()*8,v:(r()*3)|0});}
 for(const c of cov){if(c.d<85||c.s>Lp-900)continue;const i=I(c.s),A=c.side<0?wl:wr,lat=c.side*(A[i]-30);const kd=r()<.7?'llaut':'rib';add({t:'cboat',kind:kd,x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat,r:hs[i]+(r()<.5?0:Math.PI),...BOATK[kd],moored:1,s:(r()*1e6)|0});}
 {const i=I(Lp*.5);add({t:'fuel',x:xs[i],y:ys[i]});}
 if(!G.free){const rh=rng(seed+77),nh=rh()<.5?1:2;for(let k=0;k<nh;k++){const i=I(Lp*(nh===1?.42:k?.78:.42)),ln=(rh()-.5)*W*.3;add({t:'heart',x:xs[i]+Math.cos(hs[i])*ln,y:ys[i]+Math.sin(hs[i])*ln});}}
 const inWater=(px,py)=>{for(let q=0;q<N;q+=3){const dd=Math.hypot(xs[q]-px,ys[q]-py);if(dd<Math.max(wl[q],wr[q])+18)return true;}return false;};
 for(let s=0;s<Lp+200;s+=26)for(const sd of[-1,1]){if(r()<.45)continue;const i=I(s),d=(sd<0?wl[i]:wr[i])+26+r()*260,px=xs[i]+Math.cos(hs[i])*sd*d,py=ys[i]+Math.sin(hs[i])*sd*d;if(inWater(px,py))continue;add({t:'cdeco',x:px,y:py,d:{t:'pine',x:px,y:py,r:9+r()*10,s:(r()*1e6)|0}});}
 for(const[s,lat]of[[Lp-130,-W*.32],[Lp-100,W*.34]]){const i=I(s);add({t:'cboat',kind:'motor',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat,r:hs[i]+(lat<0?.4:-.4),...BOATK.motor,moored:1,s:(r()*1e6)|0});}
 const labels=[];{const i=I(Lp*.52);labels.push({x:xs[i],y:ys[i],txt:'TORRENT DE PAREIS'});}{const i=N-1;labels.push({x:xs[i],y:ys[i],txt:'SA CALOBRA'});}
 O.sort((a,b)=>a.y-b.y);
 return{Z,zi,lap,len:Lp,lenK:Math.max(1,Lp/16000),seed,shore:()=>-1e7,kind:()=>'open',barY:1e9,bar:null,objs:O,movers:[],decos:[],gatesTotal:0,finishY:-1e9,checks:[],big:[],ring:null,swimX:()=>null,cliffK:()=>0,rwall:null,waves:[],circ:C,lands:[],strips:[],cbig:[],cars:[],walk:[],labels};}
function rockTile(){return cspr('rock',256,256,g=>{const q=rng(99);g.fillStyle='#8f8a80';g.fillRect(-128,-128,256,256);
 for(let i=0;i<300;i++){const x=-128+q()*256,y=-128+q()*256,rr=4+q()*14,c=['#a39e93','#7d786e','#b8b3a8','#6b665d','#948f84','#9a8e7c'][(q()*6)|0],rot=q()*3;g.globalAlpha=.8;g.fillStyle=c;for(const dx of[-256,0,256])for(const dy of[-256,0,256]){if(Math.abs(x+dx)>150||Math.abs(y+dy)>150)continue;g.beginPath();g.ellipse(x+dx,y+dy,rr,rr*.65,rot,0,TAU);g.fill();}}g.globalAlpha=1;});}
