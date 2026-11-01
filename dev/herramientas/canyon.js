CIRCS.calobra={h0:0,open:1,canyon:1,W:260,segs:[['S',500],['R',60,250],['L',150,215],['R',150,230],['L',150,250],['S',120],['R',130,215],['S',180],['L',110,230],['R',150,205],['S',320],['L',110,250],['S',180],['R',60,230],['S',120],['L',75,230],['S',250],['R',110,230],['L',160,215],['R',160,230],['S',180],['L',160,205],['R',110,230],['S',320],['L',90,250],['S',180],['R',150,230],['S',320],['L',160,205],['S',120],['R',130,205],['S',120],['L',60,215],['R',90,250],['S',250],['L',60,215],['S',320],['R',90,250],['S',650]]};
function buildCanyon(Z,zi,lap,seed){const r=rng(seed),def=CIRCS[Z.circ],step=8,W=def.W,raw=[];let x=0,y=0,h=def.h0*Math.PI/180;raw.push([x,y]);
 for(const sg of def.segs){if(sg[0]==='S'){const n=Math.max(1,Math.round(sg[1]/4));for(let i=0;i<n;i++){x+=Math.sin(h)*sg[1]/n;y-=Math.cos(h)*sg[1]/n;raw.push([x,y]);}}
  else{const sgn=sg[0]==='R'?1:-1,a=sg[1]*Math.PI/180,Lr=a*sg[2],n=Math.max(1,Math.round(Lr/4));for(let i=0;i<n;i++){h+=sgn*a/n/2;x+=Math.sin(h)*Lr/n;y-=Math.cos(h)*Lr/n;h+=sgn*a/n/2;raw.push([x,y]);}}}
 const R=raw.length,cl=[0];for(let i=1;i<R;i++)cl.push(cl[i-1]+Math.hypot(raw[i][0]-raw[i-1][0],raw[i][1]-raw[i-1][1]));const LL=cl[R-1];
 const xs=[],ys=[];let j=0;for(let sd=0;sd<=LL;sd+=step){while(j<R-2&&cl[j+1]<sd)j++;const a=raw[j],b=raw[j+1],t=(sd-cl[j])/((cl[j+1]-cl[j])||1);xs.push(a[0]+(b[0]-a[0])*t);ys.push(a[1]+(b[1]-a[1])*t);}
 const N=xs.length,hs=[],cum=[];for(let i=0;i<N;i++){const a=Math.max(0,i-1),b=Math.min(N-1,i+1);hs.push(Math.atan2(xs[b]-xs[a],-(ys[b]-ys[a])));cum.push(i*step);}
 const Lp=(N-1)*step,C={x:xs,y:ys,h:hs,cum,n:N,L:Lp,step,W,laps:1,open:1,canyon:1,finS:Lp-230},O=[],add=o=>{O.push(o);return o;};
 const I=s=>Math.max(0,Math.min(N-1,Math.round(s/step))),P=(s,d)=>{const i=I(s);return[xs[i]+Math.cos(hs[i])*d,ys[i]+Math.sin(hs[i])*d];};
 const clr=(x,y)=>{let m=1e18;for(let i=0;i<N;i+=2){const d=(xs[i]-x)**2+(ys[i]-y)**2;if(d<m)m=d;}return Math.sqrt(m);};
 C.edgeL=[];C.edgeR=[];for(let i=0;i<N;i++){const nx=Math.cos(hs[i]),ny=Math.sin(hs[i]);C.edgeL.push([xs[i]-nx*W/2,ys[i]-ny*W/2]);C.edgeR.push([xs[i]+nx*W/2,ys[i]+ny*W/2]);}
 C.arches=[{s:40,txt:'SALIDA',col:'#ffc93c'},{s:Math.round(Lp/3),txt:'CONTROL',col:'#7be35a'},{s:Math.round(Lp*2/3),txt:'CONTROL',col:'#7be35a'},{s:C.finS,txt:'META',col:'#ffc93c'}].map(a=>{const i=I(a.s);return Object.assign(a,{x:xs[i],y:ys[i],h:hs[i]});});
 C.cps=[{s:Math.round(Lp/3)},{s:Math.round(Lp*2/3)}];C.beach=I(Lp-150);
 {const i=I(C.finS);add({t:'cline',x:xs[i],y:ys[i],h:hs[i],w:W});}
 for(let i=40;i<N-40;i+=34)add({t:'carrow',x:xs[i],y:ys[i],h:hs[i]});
 const coinS=[];for(let s=420;s<Lp-420;s+=380+r()*200){const lat=(r()-.5)*W*.45;coinS.push(s);for(let k=0;k<6;k++){const i=I(s+k*26);add({t:'coin',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat});}}
 for(let s=950;s<Lp-700;s+=850+r()*650){if(coinS.some(q=>Math.abs(q-s)<200))s+=220;const i=I(s),lat=(r()<.5?-1:1)*W*(.22+r()*.1);add({t:'rock',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat,rad:10+r()*6,v:(r()*3)|0});}
 {const i=I(Lp*.5);add({t:'fuel',x:xs[i],y:ys[i]});}
 if(!G.free){const rh=rng(seed+77),nh=rh()<.5?1:2;for(let k=0;k<nh;k++){const i=I(Lp*(nh===1?.42:k?.78:.42)),ln=(rh()-.5)*W*.3;add({t:'heart',x:xs[i]+Math.cos(hs[i])*ln,y:ys[i]+Math.sin(hs[i])*ln});}}
 for(let s=0;s<Lp+200;s+=24)for(const sd of[-1,1]){if(r()<.5)continue;const d=W/2+34+r()*280,[px,py]=P(s,sd*d);if(clr(px,py)<W/2+30)continue;add({t:'cdeco',x:px,y:py,d:{t:'pine',x:px,y:py,r:9+r()*10,s:(r()*1e6)|0}});}
 for(const[s,lat]of[[Lp-120,-W*.3],[Lp-90,W*.32]]){const i=I(s);add({t:'cboat',kind:'motor',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat,r:hs[i]+(lat<0?.4:-.4),...BOATK.motor,moored:1,s:(r()*1e6)|0});}
 const labels=[];{const i=I(Lp*.52);labels.push({x:xs[i],y:ys[i],txt:'TORRENT DE PAREIS'});}{const i=N-1;labels.push({x:xs[i],y:ys[i],txt:'SA CALOBRA'});}
 O.sort((a,b)=>a.y-b.y);
 return{Z,zi,lap,len:Lp,lenK:1,seed,shore:()=>-1e7,kind:()=>'open',barY:1e9,bar:null,objs:O,movers:[],decos:[],gatesTotal:0,finishY:-1e9,checks:[],big:[],ring:null,swimX:()=>null,cliffK:()=>0,rwall:null,waves:[],circ:C,lands:[],strips:[],cbig:[],cars:[],walk:[],labels};}
function rockTile(){return cspr('rock',256,256,g=>{const q=rng(99);g.fillStyle='#8f8a80';g.fillRect(-128,-128,256,256);
 for(let i=0;i<300;i++){const x=-128+q()*256,y=-128+q()*256,rr=4+q()*14,c=['#a39e93','#7d786e','#b8b3a8','#6b665d','#948f84','#9a8e7c'][(q()*6)|0],rot=q()*3;g.globalAlpha=.8;g.fillStyle=c;for(const dx of[-256,0,256])for(const dy of[-256,0,256]){if(Math.abs(x+dx)>150||Math.abs(y+dy)>150)continue;g.beginPath();g.ellipse(x+dx,y+dy,rr,rr*.65,rot,0,TAU);g.fill();}}g.globalAlpha=1;});}
function drawCanyon(Zn){const C=Zn.circ,V=G._vis,W=C.W;let i0=1e9,i1=-1;const m=W+320;
 for(let i=0;i<C.n;i+=3){const x=C.x[i],y=C.y[i];if(V?V(x,y,m):(x>camX-m&&x<camX+VW+m&&y>camTop-m&&y<camTop+VH+m)){if(i<i0)i0=i;if(i>i1)i1=i;}}
 if(i1<0){i0=0;i1=C.n-1;}const a=Math.max(0,i0-10),b=Math.min(C.n-1,i1+10);
 const edge=E=>{ctx.beginPath();for(let i=a;i<=b;i++)i===a?ctx.moveTo(E[i][0],E[i][1]):ctx.lineTo(E[i][0],E[i][1]);};
 ctx.save();ctx.lineJoin='round';ctx.strokeStyle='rgba(120,230,225,.32)';ctx.lineWidth=36;for(const E of[C.edgeL,C.edgeR]){edge(E);ctx.stroke();}
 if(b>=C.beach){ctx.lineCap='round';ctx.strokeStyle='#d6c9ae';ctx.lineWidth=W+10;ctx.beginPath();for(let i=C.beach;i<C.n;i++)i===C.beach?ctx.moveTo(C.x[i],C.y[i]):ctx.lineTo(C.x[i],C.y[i]);ctx.stroke();ctx.lineCap='butt';ctx.strokeStyle='rgba(255,255,255,.7)';ctx.lineWidth=3;ctx.setLineDash([4,4]);const i=C.beach,nx=Math.cos(C.h[i]),ny=Math.sin(C.h[i]);ctx.beginPath();ctx.moveTo(C.x[i]-nx*W/2,C.y[i]-ny*W/2);ctx.lineTo(C.x[i]+nx*W/2,C.y[i]+ny*W/2);ctx.stroke();ctx.setLineDash([]);
  ctx.fillStyle='rgba(110,100,85,.5)';for(let k=0;k<160;k++){const ii=C.beach+((k*7)%Math.max(1,C.n-C.beach)),lat=(((k*37)%100)/100-.5)*W*.9;ctx.fillRect(C.x[ii]+Math.cos(C.h[ii])*lat,C.y[ii]+Math.sin(C.h[ii])*lat,2.2,2.2);}}
 ctx.beginPath();ctx.rect(camX-60,camTop-60,VW+120,VH+120);ctx.moveTo(C.edgeL[a][0],C.edgeL[a][1]);for(let i=a+1;i<=b;i++)ctx.lineTo(C.edgeL[i][0],C.edgeL[i][1]);
 for(let i=b;i>=a;i--)ctx.lineTo(C.edgeR[i][0],C.edgeR[i][1]);ctx.closePath();ctx.clip('evenodd');
 const sp=rockTile(),ts=256;for(let y=Math.floor((camTop-60)/ts)*ts;y<camTop+VH+60;y+=ts)for(let x=Math.floor((camX-60)/ts)*ts;x<camX+VW+60;x+=ts){if(V&&!V(x+128,y+128,182))continue;ctx.drawImage(sp.c,x,y,ts,ts);}
 ctx.strokeStyle='rgba(25,20,15,.38)';ctx.lineWidth=44;for(const E of[C.edgeL,C.edgeR]){edge(E);ctx.stroke();}
 ctx.strokeStyle='rgba(255,250,235,.14)';ctx.lineWidth=12;for(const E of[C.edgeL,C.edgeR]){edge(E);ctx.stroke();}
 ctx.restore();
 ctx.save();ctx.strokeStyle='rgba(255,255,255,.75)';ctx.lineWidth=2.4;ctx.setLineDash([3,4]);for(const E of[C.edgeL,C.edgeR]){edge(E);ctx.stroke();}ctx.setLineDash([]);ctx.restore();
 for(const A of C.arches){if(Math.abs(A.x-G.P.x)>700||Math.abs(A.y-G.P.y)>700)continue;ctx.save();ctx.translate(A.x+14,A.y+20);ctx.rotate(A.h);ctx.fillStyle='rgba(0,20,50,.22)';ctx.beginPath();ctx.roundRect(-W/2-28,-10,W+56,20,10);ctx.fill();ctx.restore();}}
