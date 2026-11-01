BOATK.cat={bw:26,bl:46,pp:[[-7,6],[7,8],[0,14],[-6,16]]};
CIRCS.bahamas={h0:0,open:1,archi:1,style:'bahamas',W:320,pre:[['R',30,700],['S',300]],post:[['S',300],['L',40,700],['S',500],['R',35,700],['S',400]],segs:[['S',700],['R',35,720],['S',300],['L',35,480],['S',700],['R',35,560],['S',700],['L',65,560],['R',65,560],['L',35,640],['R',50,560],['S',700],['L',35,640],['S',500],['R',50,560],['S',300],['L',100,640],['S',700],['R',100,640],['L',100,560],['S',700],['R',80,720],['S',700],['L',65,480],['S',900],['R',65,720],['L',50,560],['S',500],['R',80,640],['S',900],['L',100,640],['S',500],['S',700]]};
CIRCS.trenc={h0:0,open:1,archi:1,style:'trenc',W:350,pre:[['L',20,1000],['S',300]],post:[['S',300],['R',25,1100],['S',600],['L',20,1100],['S',300]],segs:[['S',700],['R',20,1000],['S',800],['L',55,1200],['R',20,1200],['S',800],['L',55,700],['S',800],['R',30,700],['L',20,700],['S',1100],['R',20,1200],['S',800],['L',20,850],['R',55,850],['S',1100],['L',30,1200],['R',20,1200],['L',20,850],['S',1100],['R',40,700],['L',55,850],['S',1100],['R',55,1200],['S',500],['L',55,850],['R',55,1200],['S',800],['S',700]]};
function buildArchi(Z,zi,lap,seed){const r=rng(seed),def=CIRCS[Z.circ],ST=def.style,TR=ST==='trenc',step=8,W=def.W,raw=[];let x=0,y=0,h=def.h0*Math.PI/180;raw.push([x,y]);
 const PRE=def.pre||[],POST=def.post||[],segL=sg=>sg[0]==='S'?sg[1]:sg[1]*Math.PI/180*sg[2];for(const sg of[...PRE,...def.segs,...POST]){if(sg[0]==='S'){const n=Math.max(1,Math.round(sg[1]/4));for(let i=0;i<n;i++){x+=Math.sin(h)*sg[1]/n;y-=Math.cos(h)*sg[1]/n;raw.push([x,y]);}}
  else{const sgn=sg[0]==='R'?1:-1,a=sg[1]*Math.PI/180,Lr=a*sg[2],n=Math.max(1,Math.round(Lr/4));for(let i=0;i<n;i++){h+=sgn*a/n/2;x+=Math.sin(h)*Lr/n;y-=Math.cos(h)*Lr/n;h+=sgn*a/n/2;raw.push([x,y]);}}}
 const R=raw.length,cl=[0];for(let i=1;i<R;i++)cl.push(cl[i-1]+Math.hypot(raw[i][0]-raw[i-1][0],raw[i][1]-raw[i-1][1]));const LL=cl[R-1];
 const xs=[],ys=[];let j=0;for(let sd=0;sd<=LL;sd+=step){while(j<R-2&&cl[j+1]<sd)j++;const a=raw[j],b=raw[j+1],t=(sd-cl[j])/((cl[j+1]-cl[j])||1);xs.push(a[0]+(b[0]-a[0])*t);ys.push(a[1]+(b[1]-a[1])*t);}
 const N=xs.length,hs=[],cum=[];for(let i=0;i<N;i++){const a=Math.max(0,i-1),b=Math.min(N-1,i+1);hs.push(Math.atan2(xs[b]-xs[a],-(ys[b]-ys[a])));cum.push(i*step);}
 const Lt=(N-1)*step,S0=Math.round(PRE.reduce((a,sg)=>a+segL(sg),0)/step)*step,PO=POST.reduce((a,sg)=>a+segL(sg),0),Lp=Math.round(Lt-S0-PO),C={x:xs,y:ys,h:hs,cum,n:N,L:Lt,step,W,laps:1,open:1,archi:1,style:ST,finS:S0+Lp-320,s0:S0},O=[],add=o=>{O.push(o);return o;},lands=[],labels=[];
 const I=s=>Math.max(0,Math.min(N-1,Math.round((s+S0)/step))),P=(s,d)=>{const i=I(s);return[xs[i]+Math.cos(hs[i])*d,ys[i]+Math.sin(hs[i])*d];};
 const bbOf=pts=>{const b=[1e9,1e9,-1e9,-1e9];for(const[x,y]of pts){if(x<b[0])b[0]=x;if(y<b[1])b[1]=y;if(x>b[2])b[2]=x;if(y>b[3])b[3]=y;}return b;};
 const rr=rng(seed+5),nW=noise1(seed+41),nA=noise1(seed+43),nB=noise1(seed+47);
 const bump=(d,w)=>{const t=Math.abs(d)/w;return t>=1?0:(1-t*t)*(1-t*t);};
 // islotes en medio (Bahamas), estrechamientos entre islas grandes (Bahamas) y pasos con barrera (Es Trenc)
 const mids=[],nar=[],gaps=[];
 if(!TR){for(let s=1500;s<Lp-1700;s+=1900+rr()*1300)mids.push({s,r:75+rr()*40,lat:(rr()-.5)*50});
  for(let s=2600;s<Lp-1500;s+=2400+rr()*1400){if(mids.some(m=>Math.abs(m.s-s)<900))s+=900;if(mids.some(m=>Math.abs(m.s-s)<900))continue;nar.push({s,h:118+rr()*20});}}
 else{const n=4;for(let k=0;k<n;k++){const s=Math.round(Lp*(.17+k*.21)+(rr()-.5)*400);gaps.push({s,g:(rr()-.5)*120,w:118});}}
 const finS=Lp-320,calm=s=>Math.min(sm(40,260,Math.abs(s-40)),sm(40,200,Math.abs(s-finS)));
 const wl=[],wr=[];for(let i=0;i<N;i++){const s=i*step-S0;let hb=W/2+(TR?24:40)*nW(s/1100);for(const m of mids)hb=Math.max(hb,lerp(hb,m.r+205+Math.abs(m.lat),bump(s-m.s,650)));for(const q of nar)hb=lerp(hb,q.h,bump(s-q.s,420));
  wl.push(lerp(W/2,hb-(TR?32:0)+(TR?10:16)*nA(s/170),calm(s)));wr.push(lerp(W/2,hb+(TR?18:0)+16*nB(s/170),calm(s)));}
 C.wl=wl;C.wr=wr;C.edgeL=[];C.edgeR=[];for(let i=0;i<N;i++){const nx=Math.cos(hs[i]),ny=Math.sin(hs[i]);C.edgeL.push([xs[i]-nx*wl[i],ys[i]-ny*wl[i]]);C.edgeR.push([xs[i]+nx*wr[i],ys[i]+ny*wr[i]]);}
 C.mid=mids.map(m=>({i:I(m.s),lat:m.lat,r:m.r}));C.nar=nar.map(q=>I(q.s));
 if(TR){C.bo1=[];C.bo2=[];for(let i=0;i<N;i++){const nx=Math.cos(hs[i]),ny=Math.sin(hs[i]);C.bo1.push([xs[i]-nx*(wl[i]+230),ys[i]-ny*(wl[i]+230)]);C.bo2.push([xs[i]-nx*(wl[i]+520),ys[i]-ny*(wl[i]+520)]);}}for(const q of gaps){const i=I(q.s);q.w=112+rr()*24;q.e=-wl[i]+q.w;q.g=-wl[i]+q.w/2+4;}C.gaps=gaps.map(q=>({i:I(q.s),lat:q.g,w:q.w}));C.beachL=TR?1:0;
 C.arches=[{s:40,txt:'SALIDA',col:'#ffc93c'},{s:finS,txt:'META',col:'#ffc93c'}].map(a=>{const i=I(a.s);return Object.assign(a,{x:xs[i],y:ys[i],h:hs[i]});});C.cps=[];
 const loc=(i,lat,al)=>{const nx=Math.cos(hs[i]),ny=Math.sin(hs[i]),tx=Math.sin(hs[i]),ty=-Math.cos(hs[i]);return[xs[i]+nx*lat+tx*al,ys[i]+ny*lat+ty*al];};
 // ----- islas -----
 const isl=[],far=(px,py,rad,mg)=>{for(let q=0;q<N;q+=3){const dx=px-xs[q],dy=py-ys[q],d=Math.hypot(dx,dy);if(d>1700)continue;const lat=dx*Math.cos(hs[q])+dy*Math.sin(hs[q]),need=lat>=0?wr[q]:(TR?wl[q]+500:wl[q]);if(d-rad<need+mg)return false;}return true;};
 const shapePts=o=>{const cr=Math.cos(o.rot),sr=Math.sin(o.rot),T=(cx,cy)=>[o.x+cx*cr-cy*sr,o.y+cx*sr+cy*cr],pts=[],vg=[];
  for(let k=0;k<48;k++){const a=k/48*TAU;let n=1+.17*Math.sin(2*a+o.ph[0])+.1*Math.sin(3*a+o.ph[1])+.05*Math.sin(7*a+o.ph[2]);const nv=n;if(o.spit!=null){let d=a-o.spit;while(d>Math.PI)d-=TAU;while(d<-Math.PI)d+=TAU;n+=1.05*Math.exp(-((d/.2)**2));}
   pts.push(T(Math.cos(a)*o.R0*n,Math.sin(a)*o.R0*o.el*n));vg.push(T(Math.cos(a)*o.R0*nv*.76,Math.sin(a)*o.R0*o.el*nv*.76));}return{pts,vg};};
 const ptsFree=(pts,mg)=>{for(const[px,py]of pts){for(let q=0;q<N;q+=4){const lat=(px-xs[q])*Math.cos(hs[q])+(py-ys[q])*Math.sin(hs[q]),al=(px-xs[q])*Math.sin(hs[q])-(py-ys[q])*Math.cos(hs[q]);if(Math.abs(al)>10)continue;if(lat>-wl[q]-mg-(TR?460:0)&&lat<wr[q]+mg)return false;}}return true;};
 const mkShape=o=>{const q=rng((o.x*13+o.y*7)|0);o.rot=o.rot!=null?o.rot:q()*Math.PI;o.el=o.el||(o.mid?.85:.3+q()*.38);o.ph=[q()*6,q()*6,q()*6];o.spit=o.noSpit||o.mid?null:(q()<.4?q()*TAU:null);o.R0=o.mid?o.rad:o.rad*1.3;o.maxR=o.R0*(1.32+(o.spit!=null?1:0));o.q=q;};
 const sides=TR?[1]:[-1,1];
 // islas grandes que forman un paso (Bahamas)
 for(const q of nar){for(const sd of[-1,1]){const i=I(q.s),rad=150+rr()*60,o={rad,mid:0,noSpit:1,big:1,el:.42+rr()*.12,rot:hs[i]-Math.PI/2};const off=(sd<0?wl[i]:wr[i])+rad*1.3*o.el*1.12+14;[o.x,o.y]=[xs[i]+Math.cos(hs[i])*sd*off,ys[i]+Math.sin(hs[i])*sd*off];mkShape(o);
   for(let tr=0;tr<4;tr++){const sp=shapePts(o);if(ptsFree(sp.pts,14)){o.sp=sp;break;}o.rad*=.82;o.R0=o.rad*1.3;}if(o.sp)isl.push(o);}}
 // isla enorme tipo costa (Bahamas)
 if(!TR)for(let s=1800;s<Lp-1800;s+=4200+rr()*1800){const sd=rr()<.5?-1:1,i=I(s),o={rad:520,mid:0,noSpit:1,big:1,huge:1,el:.24,rot:hs[i]-Math.PI/2};const off=(sd<0?wl[i]:wr[i])+520*1.3*.24*1.12+26;[o.x,o.y]=[xs[i]+Math.cos(hs[i])*sd*off,ys[i]+Math.sin(hs[i])*sd*off];mkShape(o);
  for(let tr=0;tr<5;tr++){const sp=shapePts(o);if(ptsFree(sp.pts,20)&&!isl.some(p=>Math.hypot(p.x-o.x,p.y-o.y)<p.maxR+o.maxR*.6)){o.sp=sp;break;}o.rad*=.85;o.R0=o.rad*1.3;}if(o.sp){isl.push(o);(C.huge=C.huge||[]).push(I(s));labels.push({x:o.x,y:o.y,txt:['GREAT EXUMA','STANIEL CAY','NORMAN’S CAY','COMPASS CAY'][isl.filter(p=>p.huge).length%4]});}}
 // islas que cierran los pasos estrechos contra la playa (Es Trenc)
 for(const q of gaps){const i=I(q.s),nx=Math.cos(hs[i]),ny=Math.sin(hs[i]),aR=(wr[i]+470-q.e)/2,bR=150+rr()*60,o={rad:aR,mid:0,noSpit:1,big:1,pass:1,rot:hs[i]};o.x=xs[i]+nx*(q.e+aR);o.y=ys[i]+ny*(q.e+aR);mkShape(o);o.R0=aR;o.el=bR/aR;o.maxR=aR*1.35;
  let sp=shapePts(o),mn=1e9;for(const[px,py]of sp.pts){const lat=(px-xs[i])*nx+(py-ys[i])*ny;if(lat<mn)mn=lat;}const sh=q.e-mn;o.x+=nx*sh;o.y+=ny*sh;o.sp=shapePts(o);isl.push(o);}
 // cayos pequeños
 for(let s=-S0-300;s<Lp+PO+300;s+=(TR?70:40)+rr()*60)for(const sd of sides){if(rr()<(TR?.55:.2))continue;const i=I(s),rad=(TR?22:30)+rr()*rr()*(TR?70:155),o={rad,mid:0};const off=(sd<0?wl[i]:wr[i])+rad*1.6+22+(rr()<.6?rr()*140:rr()*520);const ee=s<-S0?s+S0:(s>Lp+PO?s-Lp-PO:0),he=hs[s<-S0?0:N-1];o.x=xs[i]+Math.cos(hs[i])*sd*off+Math.sin(he)*ee;o.y=ys[i]+Math.sin(hs[i])*sd*off-Math.cos(he)*ee;mkShape(o);
  if(!far(o.x,o.y,o.maxR,26))continue;if(isl.some(p=>Math.hypot(p.x-o.x,p.y-o.y)<p.maxR*.8+o.maxR*.8+18))continue;isl.push(o);}
 for(const m of mids){const i=I(m.s),o={x:xs[i]+Math.cos(hs[i])*m.lat,y:ys[i]+Math.sin(hs[i])*m.lat,rad:m.r,mid:1};mkShape(o);isl.push(o);}
 const big=[];
 for(const o of isl){const q=o.q,sp=o.sp||shapePts(o),pts=sp.pts,vg=sp.vg,rimK=(q()*40)|0;
  lands.push({pts,bb:bbOf(pts),fill:'#f6f1e1',foam:true,halo:true});
  const vb=bbOf(vg),blobs=[];const area=(vb[2]-vb[0])*(vb[3]-vb[1]);const nb=Math.min(o.huge?260:110,Math.round(area/150));
  for(let k=0;k<nb*2&&blobs.length<nb;k++){const x=vb[0]+q()*(vb[2]-vb[0]),y=vb[1]+q()*(vb[3]-vb[1]);if(!polyIn(vg,x,y))continue;blobs.push([x-o.x,y-o.y,4+q()*(o.big?9:7),(q()*5)|0]);}
  const rim=[];for(let k=0;k<24;k++){const kk=(rimK+k)%48;rim.push([pts[kk][0]-o.x,pts[kk][1]-o.y]);}
  const B={t:'isle',x:o.x,y:o.y,R:(o.big?o.R0*1.4:o.maxR)+40,vg:vg.map(([x,y])=>[x-o.x,y-o.y]),blobs,rim:o.spit!=null?rim.slice(0,12):rim,tr:TR};
  if(!TR&&!o.mid&&o.rad>70&&q()<(o.huge?.9:.45)){let ci=0,cd=1e18;for(let q2=0;q2<N;q2+=6){const d=(xs[q2]-o.x)**2+(ys[q2]-o.y)**2;if(d<cd){cd=d;ci=q2;}}const ang=Math.atan2(ys[ci]-o.y,xs[ci]-o.x);let ek=0,eb=-1e9;for(let k=0;k<48;k++){const v=(pts[k][0]-o.x)*Math.cos(ang)+(pts[k][1]-o.y)*Math.sin(ang);if(v>eb){eb=v;ek=k;}}
   const ex=pts[ek][0]-o.x,ey=pts[ek][1]-o.y;B.house={x:ex*.66,y:ey*.66,a:ang,c:['#ffffff','#ffe2e8','#d6f0ff','#fff3c4'][(q()*4)|0]};B.dock={x0:ex*.92,y0:ey*.92,x1:ex+Math.cos(ang)*46,y1:ey+Math.sin(ang)*46};
   {const bx=o.x+ex+Math.cos(ang)*58+Math.cos(ang+Math.PI/2)*14,by=o.y+ey+Math.sin(ang)*58+Math.sin(ang+Math.PI/2)*14;if(far(bx,by,36,40))add({t:'cboat',kind:'motor',x:bx,y:by,r:ang,...BOATK.motor,moored:1,s:(q()*1e6)|0});else{B.dock.x1=ex+Math.cos(ang)*14;B.dock.y1=ey+Math.sin(ang)*14;}}}
  big.push(B);
  const np=o.pass?12:TR?(o.rad>40?2:1):(o.huge?8:o.rad>90?3:o.rad>55?1:0);for(let k=0;k<np;k++){const b=blobs[(q()*blobs.length)|0];if(!b)break;const px=o.x+b[0],py=o.y+b[1];add({t:'cdeco',x:px,y:py,d:{t:TR?'pine':'palm',x:px,y:py,r:13+q()*6,s:(q()*1e6)|0}});}}
 // ----- Es Trenc: monedas por el paso -----
 for(const q of gaps){const i=I(q.s);for(let k=0;k<4;k++){const[cx,cy]=loc(i,q.g,-90+k*60);add({t:'coin',x:cx,y:cy});}{const[lx,ly]=loc(i,q.g,-170);labels.push({x:lx,y:ly,txt:'PASO'});}}
 // ----- Es Trenc: playa, dunas, pinos, sombrillas, chiringuito -----
 if(TR){for(let s=-S0;s<Lp+PO;s+=22){const i=I(s);
   if(r()<.35){const[x,y]=P(s,-(wl[i]+26+r()*60));const c=r()<.5?'#ffffff':['#ff4f6b','#33a3ff','#ffd21a','#1f9e52'][(r()*4)|0];if(r()<.55)add({t:'cdeco',x,y,d:{t:'umb',x,y,s:15,c}});else add({t:'cdeco',x,y,d:{t:'towel',x,y,s:(r()*1e6)|0,c}});}
   for(let k=0;k<2;k++){if(r()<.5)continue;const[x,y]=P(s+r()*20,-(wl[i]+110+r()*90));add({t:'cdeco',x,y,d:{t:'grass',x,y,s:(r()*1e6)|0}});}
   if(r()<.7){const[x,y]=P(s+r()*20,-(wl[i]+215+r()*230));add({t:'cdeco',x,y,d:{t:'pine',x,y,r:11+r()*10,s:(r()*1e6)|0}});}}
  for(const f of[.3,.62,.9]){const s=Lp*f,[x,y]=P(s,-(wl[I(s)]+150));big.push({t:'chiri',x,y,h:hs[I(s)]+Math.PI/2,R:40});labels.push({x,y:y-34,txt:'CHIRINGUITO'});}
  for(let s=900;s<Lp-900;s+=1300+r()*900){if(gaps.some(q=>Math.abs(q.s-s)<500))continue;const i=I(s),lat=-wl[i]+15+r()*8;add({t:'float',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat,kind:r()<.5?0:1,hair:['#f2cf63','#5a3218','#111111','#b5402a'][(r()*4)|0],bik:['#ff3f8e','#22c4ff','#ffd21a','#7be35a','#ff7a1a'][(r()*5)|0],rot:(r()-.5)*1.2,dist:0,wave:0,txt:''});}
  {const i=I(Lp*.5);labels.push({...(()=>{const[x,y]=P(Lp*.5,-(wl[i]+70));return{x,y};})(),txt:'ES TRENC'});}{const i=I(Lp);labels.push({x:xs[i],y:ys[i],txt:'ES TRENC'});}}
 // ----- remolinos de arena y hierba en los bajíos -----
 const bars=[];for(let s=-S0;s<Lp+PO;s+=(TR?320:200)+rr()*300){const sd=TR?1:(rr()<.5?-1:1),i=I(s),off=(sd<0?wl[i]:wr[i])+30+rr()*240;let x=xs[i]+Math.cos(hs[i])*sd*off,y=ys[i]+Math.sin(hs[i])*sd*off,a=hs[i]+sd*(.2+rr()*.9)+(rr()<.5?Math.PI:0),cv=(rr()-.5)*.014;const pts=[[x,y]],len=260+rr()*620;for(let d=0;d<len;d+=40){a+=cv*40;x+=Math.sin(a)*40;y-=Math.cos(a)*40;pts.push([x,y]);}bars.push({pts,w:40+rr()*110,bb:bbOf(pts)});}
 C.bars=bars;C.grass=[];for(let k=0;k<Lt/160;k++){const s=-S0+rr()*Lt,sd=TR?1:(rr()<.5?-1:1),i=I(s),off=(sd<0?wl[i]:wr[i])+20+rr()*300;C.grass.push([xs[i]+Math.cos(hs[i])*sd*off,ys[i]+Math.sin(hs[i])*sd*off,14+rr()*30]);}
 // ----- barcos fondeados -----
 const anch=[];for(let s=-S0+200;s<Lp+PO-200;s+=(TR?520:330)+rr()*520){const sd=TR?1:(rr()<.5?-1:1),i=I(s),off=(sd<0?wl[i]:wr[i])+62+rr()*100,x=xs[i]+Math.cos(hs[i])*sd*off,y=ys[i]+Math.sin(hs[i])*sd*off;if(landIn(lands,x,y)||landIn(lands,x+20,y)||landIn(lands,x-20,y))continue;if(anch.some(p=>Math.hypot(p[0]-x,p[1]-y)<90))continue;anch.push([x,y]);const kd=TR?['llaut','sail','motor','llaut'][(rr()*4)|0]:['sail','motor','cat','sail','cat'][(rr()*5)|0];add({t:'cboat',kind:kd,x,y,r:rr()*TAU,...BOATK[kd],s:(rr()*1e6)|0});}
 if(!TR){let best=null,bd=1e9;const tx=xs[I(Lp*.35)],ty=ys[I(Lp*.35)];for(const o of isl){if(o.mid||o.big)continue;const d=Math.hypot(o.x-tx,o.y-ty);if(d<bd){bd=d;best=o;}}
  if(best){const a0=Math.atan2(ty-best.y,tx-best.x);for(let k=0;k<5;k++){const a=a0+(k-2)*.28,d=best.rad+18+(k%2)*10;add({t:'pig',x:best.x+Math.cos(a)*d,y:best.y+Math.sin(a)*d,ph:k*1.3});}labels.push({x:best.x,y:best.y,txt:'PIG BEACH'});}}
 {const i=I(finS);add({t:'cline',x:xs[i],y:ys[i],h:hs[i],w:W});}
 for(let i=I(0)+40;i<I(finS);i+=40){if(gaps.some(q=>Math.abs(q.s-(i*step-S0))<300))continue;add({t:'carrow',x:xs[i],y:ys[i],h:hs[i]});}
 const busy=s=>mids.some(m=>Math.abs(m.s-s)<500)||gaps.some(q=>Math.abs(q.s-s)<420);
 for(let s=450;s<Lp-450;s+=420+r()*220){if(busy(s))continue;const lat=(r()-.5)*W*.5;for(let k=0;k<6;k++){const i=I(s+k*26);add({t:'coin',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat});}}
 if(!TR)for(let s=1200;s<Lp-1200;s+=1500+r()*1300){if(busy(s))continue;const i=I(s),lat=(r()-.5)*W*.5;add({t:'cray',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat,vx:r()<.5?30:-30,ph:r()*6});}
 {let s=Lp*.5;while(busy(s))s+=300;const i=I(s);add({t:'fuel',x:xs[i],y:ys[i]});}
 if(!TR){let sp=Lp*.56;for(const m of mids)if(Math.abs(m.s-sp)<600)sp=m.s+700;const i=I(sp),sd=r()<.5?-1:1,lat=sd*((sd<0?wl[i]:wr[i])-120);add({t:'cplane',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat,r:hs[i]+.9*sd});const[lx,ly]=[xs[i]+Math.cos(hs[i])*lat*.55,ys[i]+Math.sin(hs[i])*lat*.55];labels.push({x:lx,y:ly,txt:'AVIONETA HUNDIDA'});}
 if(!G.free){const rh=rng(seed+77),nh=rh()<.5?1:2;for(let k=0;k<nh;k++){let s=Lp*(nh===1?.42:k?.78:.42);while(busy(s))s+=300;const i=I(s),ln=(rh()-.5)*W*.3;add({t:'heart',x:xs[i]+Math.cos(hs[i])*ln,y:ys[i]+Math.sin(hs[i])*ln});}}
 if(!TR){const i=I(Lp*.6);labels.push({x:xs[i],y:ys[i],txt:'EXUMA CAYS'});const j2=I(Lp);labels.push({x:xs[j2],y:ys[j2],txt:'EXUMAS'});}
 O.sort((a,b)=>a.y-b.y);
 return{Z,zi,lap,len:Lp,lenK:Math.max(1,Lp/16000),seed,shore:()=>-1e7,kind:()=>'open',barY:1e9,bar:null,objs:O,movers:[],decos:[],gatesTotal:0,finishY:-1e9,checks:[],big:[],ring:null,swimX:()=>null,cliffK:()=>0,rwall:null,waves:[],circ:C,lands,strips:[],cbig:big,cars:[],walk:[],labels};}

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
function drawShallows(Zn){const C=Zn.circ,V=G._vis,TR=C.style==='trenc';let i0=1e9,i1=-1;const m=C.W+380,x0=camX,x1=camX+VW,y0=camTop,y1=camTop+VH,vis=b=>!(b[2]<x0-80||b[0]>x1+80||b[3]<y0-80||b[1]>y1+80);
 for(let i=0;i<C.n;i+=3){const x=C.x[i],y=C.y[i];if(V?V(x,y,m):(x>camX-m&&x<camX+VW+m&&y>camTop-m&&y<camTop+VH+m)){if(i<i0)i0=i;if(i>i1)i1=i;}}
 if(i1<0){i0=0;i1=C.n-1;}const a=Math.max(0,i0-10),b=Math.min(C.n-1,i1+10);
 const line=E=>{ctx.beginPath();for(let i=a;i<=b;i++)i===a?ctx.moveTo(E[i][0],E[i][1]):ctx.lineTo(E[i][0],E[i][1]);};
 ctx.save();ctx.beginPath();ctx.rect(camX-60,camTop-60,VW+120,VH+120);ctx.moveTo(C.edgeL[a][0],C.edgeL[a][1]);for(let i=a+1;i<=b;i++)ctx.lineTo(C.edgeL[i][0],C.edgeL[i][1]);for(let i=b;i>=a;i--)ctx.lineTo(C.edgeR[i][0],C.edgeR[i][1]);ctx.closePath();ctx.clip('evenodd');
 ctx.fillStyle=TR?'#79e1e8':'#5ad4e3';ctx.fillRect(camX-60,camTop-60,VW+120,VH+120);
 const sp=sandTile(),ts=256;ctx.globalAlpha=TR?.38:.26;for(let y=Math.floor((camTop-60)/ts)*ts;y<camTop+VH+60;y+=ts)for(let x=Math.floor((camX-60)/ts)*ts;x<camX+VW+60;x+=ts){if(V&&!V(x+128,y+128,182))continue;ctx.drawImage(sp.c,x,y,ts,ts);}ctx.globalAlpha=1;
 ctx.fillStyle=TR?'rgba(30,130,120,.16)':'rgba(15,110,130,.22)';for(const g of C.grass||[]){if(g[0]<x0-60||g[0]>x1+60||g[1]<y0-60||g[1]>y1+60)continue;ctx.beginPath();ctx.ellipse(g[0],g[1],g[2],g[2]*.6,g[0]%3,0,TAU);ctx.fill();}
 ctx.lineCap='round';ctx.lineJoin='round';for(const B of C.bars||[]){if(!vis(B.bb))continue;ctx.strokeStyle='rgba(236,251,246,.62)';ctx.lineWidth=B.w;ctx.beginPath();B.pts.forEach(([x,y],k)=>k?ctx.lineTo(x,y):ctx.moveTo(x,y));ctx.stroke();ctx.strokeStyle='rgba(255,255,255,.5)';ctx.lineWidth=B.w*.45;ctx.stroke();}
 ctx.strokeStyle=TR?'rgba(40,175,210,.2)':'rgba(30,150,200,.22)';ctx.lineWidth=TR?50:56;for(const E of[C.edgeL,C.edgeR]){line(E);ctx.stroke();}ctx.strokeStyle=TR?'rgba(70,200,225,.18)':'rgba(60,185,220,.2)';ctx.lineWidth=TR?22:24;for(const E of[C.edgeL,C.edgeR]){line(E);ctx.stroke();}
 if(TR&&C.bo1){const poly=(A,B2,col)=>{ctx.beginPath();ctx.moveTo(A[a][0],A[a][1]);for(let i=a+1;i<=b;i++)ctx.lineTo(A[i][0],A[i][1]);for(let i=b;i>=a;i--)ctx.lineTo(B2[i][0],B2[i][1]);ctx.closePath();ctx.fillStyle=col;ctx.fill();};
  poly(C.edgeL,C.bo2,'#f6efdc');poly(C.bo1,C.bo2,'#6f9b4c');ctx.strokeStyle='rgba(220,205,160,.6)';ctx.lineWidth=46;line(C.bo1);ctx.stroke();ctx.strokeStyle='#5d8a40';ctx.lineWidth=6;line(C.bo1);ctx.stroke();
  ctx.strokeStyle='#e6d6b0';ctx.lineWidth=16;line(C.edgeL);ctx.stroke();ctx.strokeStyle='rgba(255,255,255,.85)';ctx.lineWidth=2.6;ctx.setLineDash([4,4]);line(C.edgeL);ctx.stroke();ctx.setLineDash([]);}
 ctx.restore();}
