BOATK.cat={bw:26,bl:46,pp:[[-7,6],[7,8],[0,14],[-6,16]]};
CIRCS.bahamas={h0:0,open:1,archi:1,W:390,segs:[['S',700],['R',35,720],['S',300],['L',35,480],['S',700],['R',35,560],['S',700],['L',65,560],['R',65,560],['L',35,640],['R',50,560],['S',700],['L',35,640],['S',500],['R',50,560],['S',300],['L',100,640],['S',700],['R',100,640],['L',100,560],['S',700],['R',80,720],['S',700],['L',65,480],['S',900],['R',65,720],['L',50,560],['S',500],['R',80,640],['S',900],['L',100,640],['S',500],['S',700]]};
function buildArchi(Z,zi,lap,seed){const r=rng(seed),def=CIRCS[Z.circ],step=8,W=def.W,raw=[];let x=0,y=0,h=def.h0*Math.PI/180;raw.push([x,y]);
 for(const sg of def.segs){if(sg[0]==='S'){const n=Math.max(1,Math.round(sg[1]/4));for(let i=0;i<n;i++){x+=Math.sin(h)*sg[1]/n;y-=Math.cos(h)*sg[1]/n;raw.push([x,y]);}}
  else{const sgn=sg[0]==='R'?1:-1,a=sg[1]*Math.PI/180,Lr=a*sg[2],n=Math.max(1,Math.round(Lr/4));for(let i=0;i<n;i++){h+=sgn*a/n/2;x+=Math.sin(h)*Lr/n;y-=Math.cos(h)*Lr/n;h+=sgn*a/n/2;raw.push([x,y]);}}}
 const R=raw.length,cl=[0];for(let i=1;i<R;i++)cl.push(cl[i-1]+Math.hypot(raw[i][0]-raw[i-1][0],raw[i][1]-raw[i-1][1]));const LL=cl[R-1];
 const xs=[],ys=[];let j=0;for(let sd=0;sd<=LL;sd+=step){while(j<R-2&&cl[j+1]<sd)j++;const a=raw[j],b=raw[j+1],t=(sd-cl[j])/((cl[j+1]-cl[j])||1);xs.push(a[0]+(b[0]-a[0])*t);ys.push(a[1]+(b[1]-a[1])*t);}
 const N=xs.length,hs=[],cum=[];for(let i=0;i<N;i++){const a=Math.max(0,i-1),b=Math.min(N-1,i+1);hs.push(Math.atan2(xs[b]-xs[a],-(ys[b]-ys[a])));cum.push(i*step);}
 const Lp=(N-1)*step,C={x:xs,y:ys,h:hs,cum,n:N,L:Lp,step,W,laps:1,open:1,archi:1,finS:Lp-320},O=[],add=o=>{O.push(o);return o;},lands=[],labels=[];
 const I=s=>Math.max(0,Math.min(N-1,Math.round(s/step))),P=(s,d)=>{const i=I(s);return[xs[i]+Math.cos(hs[i])*d,ys[i]+Math.sin(hs[i])*d];};
 const bbOf=pts=>{const b=[1e9,1e9,-1e9,-1e9];for(const[x,y]of pts){if(x<b[0])b[0]=x;if(y<b[1])b[1]=y;if(x>b[2])b[2]=x;if(y>b[3])b[3]=y;}return b;};
 const rr=rng(seed+5),nW=noise1(seed+41),nA=noise1(seed+43),nB=noise1(seed+47);
 // islotes en medio del canal (se pasa por un lado o por otro)
 const mids=[];for(let s=1500;s<Lp-1700;s+=1500+rr()*1100)mids.push({s,r:75+rr()*40,lat:(rr()-.5)*50});
 const bump=(d,w)=>{const t=Math.abs(d)/w;return t>=1?0:(1-t*t)*(1-t*t);};
 const calm=s=>Math.min(sm(60,300,s),sm(Lp-60,Lp-500,s),sm(40,200,Math.abs(s-C.finS)));
 const wl=[],wr=[];for(let i=0;i<N;i++){const s=i*step;let hb=W/2+40*nW(s/1100);for(const m of mids)hb=Math.max(hb,lerp(hb,m.r+230+Math.abs(m.lat),bump(s-m.s,650)));
  wl.push(lerp(W/2,hb+16*nA(s/170),calm(s)));wr.push(lerp(W/2,hb+16*nB(s/170),calm(s)));}
 C.wl=wl;C.wr=wr;C.edgeL=[];C.edgeR=[];for(let i=0;i<N;i++){const nx=Math.cos(hs[i]),ny=Math.sin(hs[i]);C.edgeL.push([xs[i]-nx*wl[i],ys[i]-ny*wl[i]]);C.edgeR.push([xs[i]+nx*wr[i],ys[i]+ny*wr[i]]);}
 C.mid=mids.map(m=>({i:I(m.s),lat:m.lat,r:m.r}));
 C.arches=[{s:40,txt:'SALIDA',col:'#ffc93c'},{s:C.finS,txt:'META',col:'#ffc93c'}].map(a=>{const i=I(a.s);return Object.assign(a,{x:xs[i],y:ys[i],h:hs[i]});});C.cps=[];
 // cayos alargados e irregulares, con lenguas de arena, roca gris y matorral
 const isl=[],far=(px,py,rad,mg)=>{for(let q=0;q<N;q+=3){if(Math.hypot(xs[q]-px,ys[q]-py)-rad<Math.max(wl[q],wr[q])+mg)return false;}return true;};
 const mkShape=(o)=>{const q=rng((o.x*13+o.y*7)|0);o.rot=q()*Math.PI;o.el=o.mid?.85:.3+q()*.38;o.ph=[q()*6,q()*6,q()*6];o.spit=!o.mid&&q()<.4?q()*TAU:null;o.R0=o.mid?o.rad:o.rad*1.3;o.maxR=o.R0*(1.32+(o.spit!=null?1:0));o.q=q;};
 for(let s=-300;s<Lp+600;s+=40+rr()*60)for(const sd of[-1,1]){if(rr()<.2)continue;const i=I(s),rad=30+rr()*rr()*155,o={rad,mid:0};const off=(sd<0?wl[i]:wr[i])+rad*1.6+22+(rr()<.6?rr()*140:rr()*520);o.x=xs[i]+Math.cos(hs[i])*sd*off+(s<0?Math.sin(hs[0])*s:0);o.y=ys[i]+Math.sin(hs[i])*sd*off-(s<0?Math.cos(hs[0])*s:0);mkShape(o);
  if(!far(o.x,o.y,o.maxR,26))continue;if(isl.some(p=>Math.hypot(p.x-o.x,p.y-o.y)<p.maxR*.8+o.maxR*.8+18))continue;isl.push(o);}
 for(const m of mids){const i=I(m.s),o={x:xs[i]+Math.cos(hs[i])*m.lat,y:ys[i]+Math.sin(hs[i])*m.lat,rad:m.r,mid:1};mkShape(o);isl.push(o);}
 const big=[];
 for(const o of isl){const q=o.q,cr=Math.cos(o.rot),sr=Math.sin(o.rot),T=(cx,cy)=>[o.x+cx*cr-cy*sr,o.y+cx*sr+cy*cr],pts=[],vg=[],rimK=(q()*40)|0;
  for(let k=0;k<44;k++){const a=k/44*TAU;let n=1+.17*Math.sin(2*a+o.ph[0])+.1*Math.sin(3*a+o.ph[1])+.05*Math.sin(7*a+o.ph[2]);const nv=n;let sp=0;if(o.spit!=null){let d=a-o.spit;while(d>Math.PI)d-=TAU;while(d<-Math.PI)d+=TAU;sp=Math.exp(-((d/.2)**2));n+=1.05*sp;}
   pts.push(T(Math.cos(a)*o.R0*n,Math.sin(a)*o.R0*o.el*n));vg.push(T(Math.cos(a)*o.R0*nv*.74,Math.sin(a)*o.R0*o.el*nv*.74));}
  lands.push({pts,bb:bbOf(pts),fill:'#f4eedb',foam:true,halo:true});
  const rel=a=>a.map(([x,y])=>[x-o.x,y-o.y]),vb=bbOf(vg),blobs=[];const area=(vb[2]-vb[0])*(vb[3]-vb[1]);const nb=Math.min(90,Math.round(area/160));
  for(let k=0;k<nb*2&&blobs.length<nb;k++){const x=vb[0]+q()*(vb[2]-vb[0]),y=vb[1]+q()*(vb[3]-vb[1]);if(!polyIn(vg,x,y))continue;blobs.push([x-o.x,y-o.y,4+q()*7,(q()*5)|0]);}
  const rim=[];for(let k=0;k<22;k++){const kk=(rimK+k)%44;rim.push([pts[kk][0]-o.x,pts[kk][1]-o.y]);}
  const B={t:'isle',x:o.x,y:o.y,R:o.maxR+40,vg:rel(vg),blobs,rim:o.spit!=null?rim.slice(0,12):rim};
  if(!o.mid&&o.rad>70&&q()<.45){let ci=0,cd=1e18;for(let q2=0;q2<N;q2+=6){const d=(xs[q2]-o.x)**2+(ys[q2]-o.y)**2;if(d<cd){cd=d;ci=q2;}}const ang=Math.atan2(ys[ci]-o.y,xs[ci]-o.x);let ek=0,eb=-1e9;for(let k=0;k<44;k++){const v=(pts[k][0]-o.x)*Math.cos(ang)+(pts[k][1]-o.y)*Math.sin(ang);if(v>eb){eb=v;ek=k;}}
   const ex=pts[ek][0]-o.x,ey=pts[ek][1]-o.y;B.house={x:ex*.62,y:ey*.62,a:ang,c:['#ffffff','#ffe2e8','#d6f0ff','#fff3c4'][(q()*4)|0]};B.dock={x0:ex*.9,y0:ey*.9,x1:ex+Math.cos(ang)*46,y1:ey+Math.sin(ang)*46};
   add({t:'cboat',kind:'motor',x:o.x+ex+Math.cos(ang)*58+Math.cos(ang+Math.PI/2)*14,y:o.y+ey+Math.sin(ang)*58+Math.sin(ang+Math.PI/2)*14,r:ang,...BOATK.motor,moored:1,s:(q()*1e6)|0});}
  big.push(B);
  const np=o.rad>90?3:o.rad>55?1:0;for(let k=0;k<np;k++){const b=blobs[(q()*blobs.length)|0];if(!b)break;const px=o.x+b[0],py=o.y+b[1];add({t:'cdeco',x:px,y:py,d:{t:'palm',x:px,y:py,r:13+q()*6,s:(q()*1e6)|0}});}}
 // remolinos de arena en los bajíos
 const bars=[];for(let s=0;s<Lp;s+=260+rr()*380){const sd=rr()<.5?-1:1,i=I(s),off=(sd<0?wl[i]:wr[i])+40+rr()*260;let x=xs[i]+Math.cos(hs[i])*sd*off,y=ys[i]+Math.sin(hs[i])*sd*off,a=hs[i]+sd*(.25+rr()*.9)+(rr()<.5?Math.PI:0),cv=(rr()-.5)*.012;const pts=[[x,y]],len=220+rr()*520;for(let d=0;d<len;d+=40){a+=cv*40;x+=Math.sin(a)*40;y-=Math.cos(a)*40;pts.push([x,y]);}bars.push({pts,w:26+rr()*70,bb:bbOf(pts)});}
 C.bars=bars;C.grass=[];for(let k=0;k<Lp/180;k++){const s=rr()*Lp,sd=rr()<.5?-1:1,i=I(s),off=(sd<0?wl[i]:wr[i])+20+rr()*300;C.grass.push([xs[i]+Math.cos(hs[i])*sd*off,ys[i]+Math.sin(hs[i])*sd*off,14+rr()*30]);}
 // veleros, yates y catamaranes fondeados en los bajíos
 const anch=[];for(let s=500;s<Lp-200;s+=330+rr()*520){const sd=rr()<.5?-1:1,i=I(s),off=(sd<0?wl[i]:wr[i])+38+rr()*100,x=xs[i]+Math.cos(hs[i])*sd*off,y=ys[i]+Math.sin(hs[i])*sd*off;if(landIn(lands,x,y)||landIn(lands,x+20,y)||landIn(lands,x-20,y))continue;if(anch.some(p=>Math.hypot(p[0]-x,p[1]-y)<90))continue;anch.push([x,y]);const kd=['sail','motor','cat','sail','cat'][(rr()*5)|0];add({t:'cboat',kind:kd,x,y,r:rr()*TAU,...BOATK[kd],s:(rr()*1e6)|0});}
 // playa de los cerdos: el cayo más cercano al canal hacia el 35 %
 {let best=null,bd=1e9;const tx=xs[I(Lp*.35)],ty=ys[I(Lp*.35)];for(const o of isl){if(o.mid)continue;const d=Math.hypot(o.x-tx,o.y-ty);if(d<bd){bd=d;best=o;}}
  if(best){const a0=Math.atan2(ty-best.y,tx-best.x);for(let k=0;k<5;k++){const a=a0+(k-2)*.28,d=best.rad+18+(k%2)*10;add({t:'pig',x:best.x+Math.cos(a)*d,y:best.y+Math.sin(a)*d,ph:k*1.3});}labels.push({x:best.x,y:best.y,txt:'PIG BEACH'});}}
 {const i=I(C.finS);add({t:'cline',x:xs[i],y:ys[i],h:hs[i],w:W});}
 for(let i=40;i<N-40;i+=40)add({t:'carrow',x:xs[i],y:ys[i],h:hs[i]});
 for(let s=450;s<Lp-450;s+=420+r()*220){const lat=(r()-.5)*W*.5;if(mids.some(m=>Math.abs(m.s-s)<500))continue;for(let k=0;k<6;k++){const i=I(s+k*26);add({t:'coin',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat});}}
 for(let s=1200;s<Lp-1200;s+=1500+r()*1300){if(mids.some(m=>Math.abs(m.s-s)<700))continue;const i=I(s),lat=(r()-.5)*W*.5;add({t:'cray',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat,vx:r()<.5?30:-30,ph:r()*6});}
 {const i=I(Lp*.5);add({t:'fuel',x:xs[i],y:ys[i]});}
 {let sp=Lp*.56;for(const m of mids)if(Math.abs(m.s-sp)<600)sp=m.s+700;const i=I(sp),sd=r()<.5?-1:1,lat=sd*((sd<0?wl[i]:wr[i])-120);add({t:'cplane',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat,r:hs[i]+.9*sd});const[lx,ly]=[xs[i]+Math.cos(hs[i])*lat*.55,ys[i]+Math.sin(hs[i])*lat*.55];labels.push({x:lx,y:ly,txt:'AVIONETA HUNDIDA'});}
 if(!G.free){const rh=rng(seed+77),nh=rh()<.5?1:2;for(let k=0;k<nh;k++){const i=I(Lp*(nh===1?.42:k?.78:.42)),ln=(rh()-.5)*W*.3;add({t:'heart',x:xs[i]+Math.cos(hs[i])*ln,y:ys[i]+Math.sin(hs[i])*ln});}}
 {const i=I(Lp*.6);labels.push({x:xs[i],y:ys[i],txt:'EXUMA CAYS'});}{const i=N-1;labels.push({x:xs[i],y:ys[i],txt:'EXUMAS'});}
 O.sort((a,b)=>a.y-b.y);
 return{Z,zi,lap,len:Lp,lenK:1,seed,shore:()=>-1e7,kind:()=>'open',barY:1e9,bar:null,objs:O,movers:[],decos:[],gatesTotal:0,finishY:-1e9,checks:[],big:[],ring:null,swimX:()=>null,cliffK:()=>0,rwall:null,waves:[],circ:C,lands,strips:[],cbig:big,cars:[],walk:[],labels};}
function planeSpr(){return cspr('plane2',240,220,g=>{const q=rng(808);
 const hg=g.createRadialGradient(0,0,20,0,0,118);hg.addColorStop(0,'rgba(245,240,215,.75)');hg.addColorStop(.7,'rgba(240,235,210,.45)');hg.addColorStop(1,'rgba(240,235,210,0)');g.fillStyle=hg;g.beginPath();g.ellipse(0,0,118,104,0,0,TAU);g.fill();
 for(let k=0;k<40;k++){g.fillStyle='rgba(150,140,110,.18)';g.beginPath();g.arc(-100+q()*200,-90+q()*180,2+q()*5,0,TAU);g.fill();}
 const wing=(sg,cut)=>{g.beginPath();g.moveTo(-18,sg*7);g.lineTo(-10,sg*(cut?72:98));g.quadraticCurveTo(-4,sg*(cut?78:106),6,sg*(cut?76:104));g.lineTo(22,sg*7);g.closePath();g.fillStyle='#dfe2dd';g.fill();g.strokeStyle='rgba(90,90,80,.35)';g.lineWidth=1.2;g.stroke();
  g.fillStyle='rgba(120,105,80,.22)';for(let k=0;k<6;k++){g.beginPath();g.ellipse(-6+q()*22,sg*(14+q()*(cut?54:82)),3+q()*5,2+q()*3,q()*3,0,TAU);g.fill();}
  g.fillStyle='#5e4030';g.beginPath();g.roundRect(-24,sg*34-5,22,10,4);g.fill();g.fillStyle='#3b2a20';g.beginPath();g.arc(-25,sg*34,4,0,TAU);g.fill();
  if(cut){g.fillStyle='rgba(225,222,212,.55)';g.beginPath();g.moveTo(-8,sg*80);g.lineTo(2,sg*92);g.lineTo(8,sg*84);g.closePath();g.fill();}};
 wing(-1,false);wing(1,true);
 g.fillStyle='#d9dcd6';g.beginPath();g.moveTo(66,-3);g.lineTo(72,-30);g.lineTo(80,-30);g.lineTo(80,-3);g.closePath();g.fill();g.beginPath();g.moveTo(66,3);g.lineTo(72,30);g.lineTo(80,30);g.lineTo(80,3);g.closePath();g.fill();
 g.fillStyle='#4a3326';g.beginPath();g.moveTo(-96,0);g.quadraticCurveTo(-94,-9,-80,-9);g.lineTo(78,-5);g.lineTo(86,0);g.lineTo(78,5);g.lineTo(-80,9);g.quadraticCurveTo(-94,9,-96,0);g.closePath();g.fill();
 g.fillStyle='#7a5438';for(let k=0;k<14;k++){g.beginPath();g.ellipse(-86+q()*160,(q()-.5)*10,3+q()*7,1.5+q()*2.5,0,0,TAU);g.fill();}
 g.fillStyle='rgba(40,28,20,.9)';for(let k=0;k<5;k++){g.fillRect(-70+k*30+q()*8,-7,3,14);}
 g.fillStyle='rgba(240,235,210,.85)';g.beginPath();g.moveTo(30,-8);g.lineTo(38,-3);g.lineTo(34,6);g.lineTo(26,8);g.lineTo(24,0);g.closePath();g.fill();g.beginPath();g.moveTo(-50,-9);g.lineTo(-44,-2);g.lineTo(-52,4);g.lineTo(-58,-4);g.closePath();g.fill();
 g.fillStyle='rgba(60,120,80,.45)';for(let k=0;k<10;k++){g.beginPath();g.arc(-80+q()*150,(q()-.5)*14,1.5+q()*2.5,0,TAU);g.fill();}});}
function drawShallows(Zn){const C=Zn.circ,V=G._vis;let i0=1e9,i1=-1;const m=C.W+360,x0=camX,x1=camX+VW,y0=camTop,y1=camTop+VH,vis=b=>!(b[2]<x0-80||b[0]>x1+80||b[3]<y0-80||b[1]>y1+80);
 for(let i=0;i<C.n;i+=3){const x=C.x[i],y=C.y[i];if(V?V(x,y,m):(x>camX-m&&x<camX+VW+m&&y>camTop-m&&y<camTop+VH+m)){if(i<i0)i0=i;if(i>i1)i1=i;}}
 if(i1<0){i0=0;i1=C.n-1;}const a=Math.max(0,i0-10),b=Math.min(C.n-1,i1+10);
 const edge=E=>{ctx.beginPath();for(let i=a;i<=b;i++)i===a?ctx.moveTo(E[i][0],E[i][1]):ctx.lineTo(E[i][0],E[i][1]);};
 ctx.save();ctx.beginPath();ctx.rect(camX-60,camTop-60,VW+120,VH+120);ctx.moveTo(C.edgeL[a][0],C.edgeL[a][1]);for(let i=a+1;i<=b;i++)ctx.lineTo(C.edgeL[i][0],C.edgeL[i][1]);for(let i=b;i>=a;i--)ctx.lineTo(C.edgeR[i][0],C.edgeR[i][1]);ctx.closePath();ctx.clip('evenodd');
 ctx.fillStyle='#62dbe6';ctx.fillRect(camX-60,camTop-60,VW+120,VH+120);
 const sp=sandTile(),ts=256;ctx.globalAlpha=.28;for(let y=Math.floor((camTop-60)/ts)*ts;y<camTop+VH+60;y+=ts)for(let x=Math.floor((camX-60)/ts)*ts;x<camX+VW+60;x+=ts){if(V&&!V(x+128,y+128,182))continue;ctx.drawImage(sp.c,x,y,ts,ts);}ctx.globalAlpha=1;
 ctx.fillStyle='rgba(20,120,140,.2)';for(const g of C.grass||[]){if(g[0]<x0-60||g[0]>x1+60||g[1]<y0-60||g[1]>y1+60)continue;ctx.beginPath();ctx.ellipse(g[0],g[1],g[2],g[2]*.6,g[0]%3,0,TAU);ctx.fill();}
 ctx.lineCap='round';ctx.lineJoin='round';for(const B of C.bars||[]){if(!vis(B.bb))continue;ctx.strokeStyle='rgba(240,252,248,.55)';ctx.lineWidth=B.w;ctx.beginPath();B.pts.forEach(([x,y],k)=>k?ctx.lineTo(x,y):ctx.moveTo(x,y));ctx.stroke();ctx.strokeStyle='rgba(255,255,255,.4)';ctx.lineWidth=B.w*.45;ctx.stroke();}
 ctx.strokeStyle='rgba(30,120,190,.55)';ctx.lineWidth=70;for(const E of[C.edgeL,C.edgeR]){edge(E);ctx.stroke();}ctx.strokeStyle='rgba(40,150,205,.45)';ctx.lineWidth=30;for(const E of[C.edgeL,C.edgeR]){edge(E);ctx.stroke();}
 ctx.restore();}
