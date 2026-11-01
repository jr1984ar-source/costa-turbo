const CIRC_W=340,CZ=.8;
const CIRCS={
 palma:{h0:90,land:'palma',segs:[['S',1300],['R',90,300],['S',600],['R',90,300],['S',300],['L',180,280],['S',300],['R',180,300],['S',1300],['R',90,300],['L',45,250],['R',90,250],['L',45,250],['S',1052.9],['R',90,300]]},
 alcudia:{h0:0,land:'alcudia',segs:[['S',1500],['R',180,300],['S',600],['L',30,260],['R',60,260],['L',30,260],['S',300],['L',90,280],['S',300],['R',180,300],['S',860],['R',90,320],['S',480]]}};
function mkSpr(w,h,fn){const k=3,c=document.createElement('canvas');c.width=Math.ceil(w*k);c.height=Math.ceil(h*k);const g=c.getContext('2d');g.scale(k,k);g.translate(w/2,h/2);fn(g);return{c,w,h};}
const CSPR={};function cspr(key,w,h,fn){return CSPR[key]||(CSPR[key]=mkSpr(w,h,fn));}
function polyIn(pts,x,y){let ins=false;for(let i=0,j=pts.length-1;i<pts.length;j=i++){const xi=pts[i][0],yi=pts[i][1],xj=pts[j][0],yj=pts[j][1];if(((yi>y)!==(yj>y))&&(x<(xj-xi)*(y-yi)/(yj-yi)+xi))ins=!ins;}return ins;}
function landIn(lands,x,y){for(const Ld of lands||[]){if(Ld.solid===false)continue;const b=Ld.bb;if(x<b[0]||x>b[2]||y<b[1]||y>b[3])continue;if(polyIn(Ld.pts,x,y))return true;}return false;}
function circTrace(def){const raw=[],segInfo=[];let x=0,y=0,h=def.h0*Math.PI/180,s=0;raw.push([x,y]);
 for(const sg of def.segs){const s0=s;if(sg[0]==='S'){const n=Math.max(1,Math.round(sg[1]/4));for(let i=0;i<n;i++){x+=Math.sin(h)*sg[1]/n;y-=Math.cos(h)*sg[1]/n;raw.push([x,y]);}s+=sg[1];}
  else{const sgn=sg[0]==='R'?1:-1,a=sg[1]*Math.PI/180,Lr=a*sg[2],n=Math.max(1,Math.round(Lr/4));for(let i=0;i<n;i++){h+=sgn*a/n/2;x+=Math.sin(h)*Lr/n;y-=Math.cos(h)*Lr/n;h+=sgn*a/n/2;raw.push([x,y]);}s+=Lr;}
  segInfo.push({k:sg[0],s0,s1:s,deg:sg[0]==='S'?0:sg[1]});}
 const ex=x,ey=y,n=raw.length-1;for(let i=0;i<=n;i++){raw[i][0]-=ex*i/n;raw[i][1]-=ey*i/n;}raw.pop();return{raw,segInfo,total:s};}
const BOATK={motor:{bw:22,bl:64,pp:[[-4,-4],[4,-2],[-3,14],[4,16],[0,22],[-5,24]]},llaut:{bw:14,bl:42,pp:[[0,-6],[-3,8],[3,12]]},sail:{bw:16,bl:50,pp:[[-3,12],[3,16],[0,20]]},rib:{bw:13,bl:32,pp:[[0,2],[0,10]]},resc:{bw:13,bl:34,pp:[[0,0],[0,9]]}};
function buildCircuit(Z,zi,lap,seed){const r=rng(seed),def=CIRCS[Z.circ],step=8,W=CIRC_W,T0=circTrace(def),raw=T0.raw;
 const R=raw.length,cl=[0];for(let i=1;i<=R;i++){const a=raw[i-1],b=raw[i%R];cl.push(cl[i-1]+Math.hypot(b[0]-a[0],b[1]-a[1]));}const LL=cl[R];
 const xs=[],ys=[];let j=0;for(let sd=0;sd<LL-step*.5;sd+=step){while(cl[j+1]<sd)j++;const a=raw[j],b=raw[(j+1)%R],t=(sd-cl[j])/((cl[j+1]-cl[j])||1);xs.push(a[0]+(b[0]-a[0])*t);ys.push(a[1]+(b[1]-a[1])*t);}
 const N=xs.length,hs=[],cum=[];for(let i=0;i<N;i++){const a=(i-1+N)%N,b=(i+1)%N;hs.push(Math.atan2(xs[b]-xs[a],-(ys[b]-ys[a])));cum.push(i*step);}
 const C={x:xs,y:ys,h:hs,cum,n:N,L:N*step,step,W,laps:Z.laps||3},O=[],add=o=>{O.push(o);return o;},lands=[],strips=[],big=[],TT=N*step;
 const I=s=>((Math.round(s/step)%N)+N)%N,P=(s,d)=>{const i=I(s);return[xs[i]+Math.cos(hs[i])*d,ys[i]+Math.sin(hs[i])*d];};
 const clr=(x,y)=>{let m=1e18;for(let i=0;i<N;i+=2){const d=(xs[i]-x)**2+(ys[i]-y)**2;if(d<m)m=d;}return Math.sqrt(m);};
 const bbOf=pts=>{const b=[1e9,1e9,-1e9,-1e9];for(const[x,y]of pts){if(x<b[0])b[0]=x;if(y<b[1])b[1]=y;if(x>b[2])b[2]=x;if(y>b[3])b[3]=y;}return b;};
 const land=(pts,o)=>{const L=Object.assign({pts,bb:bbOf(pts)},o||{});lands.push(L);return L;};
 const chunk=pts=>{const out=[];for(let i=0;i<pts.length-1;i+=20){const c=pts.slice(i,i+21);out.push({pts:c,bb:bbOf(c)});}return out;};
 const strip=(pts,o)=>{for(const ch of chunk(pts))strips.push(Object.assign({pts:ch.pts,bb:ch.bb},o||{}));};
 const spots=[],free=(x,y,rr,cl)=>{if(clr(x,y)<(cl||W/2+rr+22))return false;for(const p of spots)if(Math.hypot(p[0]-x,p[1]-y)<p[2]+rr+14)return false;for(const k of[[0,0],[rr,0],[-rr,0],[0,rr],[0,-rr]])if(landIn(lands,x+k[0],y+k[1]))return false;return true;};
 const outerPts=(sA,sB,Df,st)=>{const pts=[];for(let s=sA;s<=sB+.1;s+=st){const i=I(s),d=Df(s);pts.push([xs[i]-Math.cos(hs[i])*d,ys[i]-Math.sin(hs[i])*d]);}return pts;};
 // ----- pista -----
 const turns=[];let tn=0;for(const sg of T0.segInfo){if(sg.k==='S')continue;const sd=sg.k==='R'?1:-1,[x,y]=P((sg.s0+sg.s1)/2,sd*(W/2+26));tn++;turns.push([x,y,sg]);add({t:'cturn',x,y,n:tn,ph:tn*1.3});spots.push([x,y,30]);}
 for(let i=0;i<N;i+=8)for(const sd of[-1,1]){const x=xs[i]+Math.cos(hs[i])*sd*W/2,y=ys[i]+Math.sin(hs[i])*sd*W/2;if(turns.some(p=>Math.hypot(p[0]-x,p[1]-y)<62))continue;add({t:'cbuoy',x,y,c:sd<0?0:1,ph:i*.37});}
 add({t:'cline',x:xs[0],y:ys[0],h:hs[0],w:W});C.arch={x:xs[0],y:ys[0],h:hs[0]};
 for(let i=24;i<N;i+=40)add({t:'carrow',x:xs[i],y:ys[i],h:hs[i]});
 const ramps=[];let rk=0;T0.segInfo.forEach(sg=>{if(sg.k!=='S')return;const len=sg.s1-sg.s0;if(len<580||(sg.s0<10&&len<1200))return;const s=sg.s0+len*(sg.s0<10?.62:.55),lat=[0,-W*.22,W*.22][rk++%3],i=I(s),x=xs[i]+Math.cos(hs[i])*lat,y=ys[i]+Math.sin(hs[i])*lat;
  add({t:'cramp',x,y,h:hs[i],w:112,kick:1});ramps.push(s);for(let k2=0;k2<3;k2++){const d=74+k2*34;add({t:'coin',x:x+Math.sin(hs[i])*d,y:y-Math.cos(hs[i])*d,air:1});}});
 for(let s=320;s<TT-240;s+=470+r()*170){if(ramps.some(q=>Math.abs(q-s)<280))continue;const lat=(r()-.5)*W*.55;for(let k2=0;k2<6;k2++){const i=I(s+k2*26);add({t:'coin',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat});}}
 {const[x,y]=P(TT*.5,0);add({t:'fuel',x,y});}
 if(!G.free){const rh=rng(seed+77),nh=rh()<.5?1:2;for(let k=0;k<nh;k++){const ii=Math.floor(N*(nh===1?.3:k?.75:.3))%N,ln=(rh()-.5)*W*.3;add({t:'heart',x:xs[ii]+Math.cos(hs[ii])*ln,y:ys[ii]+Math.sin(hs[ii])*ln});}}
 // ----- tribuna en el pontón de salida (lado de dentro) -----
 {const s=230,i=I(s),x0=W/2+26,dep=68,len=380,h=hs[i],ca=Math.cos(h),sa=Math.sin(h),loc=(lx,ly)=>[xs[i]+lx*ca-ly*sa,ys[i]+lx*sa+ly*ca];
  const pts=[loc(x0,-len/2),loc(x0+dep,-len/2),loc(x0+dep,len/2),loc(x0,len/2)];land(pts,{draw:false});big.push({t:'stand',x:xs[i],y:ys[i],h,x0,dep,len,R:len/2+dep+x0});
  for(let k=-2;k<=2;k++)spots.push([...loc(x0+dep/2,k*len/5),60]);}
 const cars=[],walk=[],labels=[];
 // ----- PALMA -----
 if(def.land==='palma'){const B0=W/2+24,sA=7880,sB=TT+2050;
  const Df=s=>{const e=Math.min(s-sA,sB-s),k=1-sm(0,460,e);return B0+900*k*k;};
  const coast=outerPts(sA,sB,Df,16),far=outerPts(sA,sB,s=>Df(s)+2600,48).reverse();
  land(coast.concat(far),{fill:'#d8ceb7',edge:'#a2957b',edgeW:9,foam:true,cch:chunk(coast)});
  const belS=9108,seuS=TT+1535,gaps=[[belS-205,belS+205],[seuS-190,seuS+190]],inGap=s=>gaps.some(g=>s>g[0]&&s<g[1]),segs=[];{let a=sA;for(const g of gaps){segs.push([a,g[0]]);a=g[1];}segs.push([a,sB]);}
  for(const[a,b]of segs){strip(outerPts(a,b,s=>Df(s)+15,16),{w:30,col:'#f1e8d6',tile:1});const road=outerPts(a,b,s=>Df(s)+52,16);strip(road,{w:40,col:'#50555c',dash:1});strip(outerPts(a,b,s=>Df(s)+80,16),{w:14,col:'#78a24f'});
   const nc=Math.round((b-a)/260);for(let k=0;k<nc;k++)cars.push({p:road,lane:k%2?-9:9,u:r(),v:(k%2?1:-1)*(55+r()*35),c:['#e3202b','#ffffff','#1e5eff','#ffd21a','#222831','#7be35a','#c9ced6'][(r()*7)|0]});
   const nw=Math.round((b-a)/90);for(let k=0;k<nw;k++)walk.push({p:outerPts(a,b,s=>Df(s)+4+(k%4)*7,32),u:r(),v:(r()<.5?1:-1)*(4+r()*6),c:['#ff4f6b','#33a3ff','#ffd21a','#ffffff','#7be35a','#ff9f43'][(r()*6)|0],sk:['#f1c9a5','#d9a47c','#8d5a3b'][(r()*3)|0]});}
  const seuI=I(seuS),[sx,sy]=P(seuS,-(Df(seuS)+100));big.push({t:'seu',x:sx,y:sy,h:hs[seuI],R:190});{const[lx,ly]=P(seuS,-(Df(seuS)+46));labels.push({x:lx,y:ly,txt:'LA SEU'});}
  const[bx,by]=P(belS,-(Df(belS)+175));big.push({t:'bellver',x:bx,y:by,R:170});{const[lx,ly]=P(belS,-(Df(belS)+40));labels.push({x:lx,y:ly,txt:'CASTELL DE BELLVER'});}
  const avoid=(x,y)=>Math.hypot(x-sx,y-sy)<190||Math.hypot(x-bx,y-by)<175;
  for(let s=sA+20;s<sB-20;s+=44){const d=Df(s);if(d>B0+500||inGap(s))continue;{const[x,y]=P(s,-(d+15));add({t:'cdeco',x,y,d:{t:'palm',x,y,r:12+r()*4,s:(r()*1e6)|0}});}
   if(r()<.5){const[x,y]=P(s+22,-(d+3));add({t:'cdeco',x,y,d:{t:'lamp',x,y,s:(r()*1e6)|0}});}
   if(r()<.7){const[x,y]=P(s+10,-(d+80));if(!avoid(x,y))add({t:'cdeco',x,y,d:{t:'palm',x,y,r:10+r()*4,s:(r()*1e6)|0}});}
   for(let row=0;row<3;row++){if(r()<.18)continue;const[x,y]=P(s+(r()-.5)*10,-(d+112+row*60+r()*14));if(avoid(x,y))continue;add({t:'cbld',x,y,w:28+r()*22,h:28+r()*26,c:['#f4efe6','#ead9b9','#f2c9a0','#dfe7ee','#e7c08e','#f6dcc0'][(r()*6)|0],roof:r()<.45,pool:r()<.18,rot:hs[I(s)]});}}
  // dique del puerto con yates
  const mo=(s,d)=>P(s,-d),m0=W/2+46,m1=W/2+76;land([mo(1880,m0),mo(2330,m0),mo(2330,m1),mo(1912,m1),mo(1912,1000),mo(1880,1000)],{fill:'#bdb3a2',edge:'#8c8273',edgeW:4,foam:true,mole:1});
  big.push({t:'faro',x:mo(2336,m0+15)[0],y:mo(2336,m0+15)[1],R:30,c:'#2bb04a'});labels.push({x:mo(2100,m1+70)[0],y:mo(2100,m1+70)[1],txt:'PORT DE PALMA'});
  for(let s=1930;s<2310;s+=26){const[x,y]=mo(s,m1+34);add({t:'cboat',kind:r()<.7?'motor':'sail',x,y,r:hs[I(s)]+Math.PI/2,...BOATK.motor,moored:1,s:(r()*1e6)|0});}}
 // ----- ALCÚDIA -----
 if(def.land==='alcudia'){const B0=W/2+24,sA=5950,sB=TT+2700;
  const Df=s=>{const u=s-TT,e0=s-sA,k0=1-sm(0,420,e0);let d=B0+(430-B0)*sm(1250,1700,u)+900*sm(2250,2700,u)**2+900*k0*k0;return d;};
  const coast=outerPts(sA,sB,Df,16),far=outerPts(sA,sB,s=>Df(s)+2600,48).reverse();
  const LD=land(coast.concat(far),{fill:'#4b7b36',foam:true,cch:chunk(coast)});
  LD.sand='#f1d9a6';LD.sandW=124;LD.sandCh=chunk(outerPts(sA,TT+1460,s=>Df(s),16));LD.rock='#8a8070';LD.rockCh=chunk(outerPts(TT+1500,sB,s=>Df(s),16));
  strip(outerPts(sA,TT+1400,s=>Df(s)+118,16),{w:8,col:'#d8bf8f'});
  for(let s=sA+20;s<TT+1380;s+=24){const d=Df(s);if(d>B0+400)continue;
   if(r()<.62){const[x,y]=P(s,-(d+22+r()*56));const w2=r();add({t:'cdeco',x,y,d:{t:'umb',x,y,s:16,c:w2<.5?'#ffffff':['#ff4f6b','#33a3ff','#ffd21a','#1f9e52'][(r()*4)|0]}});const[bx2,by2]=P(s+9,-(d+30+r()*44));add({t:'cdeco',x:bx2,y:by2,d:{t:r()<.5?'bed':'towel',x:bx2,y:by2,s:(r()*1e6)|0,c:['#ff4f6b','#33a3ff','#ffd21a','#ffffff'][(r()*4)|0]}});}
   for(let k=0;k<3;k++){const[x,y]=P(s+r()*24,-(d+128+r()*260));add({t:'cdeco',x,y,d:{t:'pine',x,y,r:11+r()*10,s:(r()*1e6)|0}});}}
  for(let s=TT+1460;s<sB-10;s+=20){const d=Df(s);if(d>1000)continue;for(let k=0;k<3;k++){const[x,y]=P(s+r()*20,-(d+30+r()*420));add({t:'cdeco',x,y,d:{t:'pine',x,y,r:11+r()*11,s:(r()*1e6)|0}});}}
  {const s=TT-640,[x,y]=P(s,-(Df(s)+104));big.push({t:'chiri',x,y,h:hs[I(s)],R:40});labels.push({x,y:y-30,txt:'CHIRINGUITO'});}
  {const s=TT+380,[x,y]=P(s,-(Df(s)+40));big.push({t:'lifeg',x,y,h:hs[I(s)],R:20});}
  for(let k=0;k<26;k++)walk.push({p:outerPts(sA,TT+1380,s=>Df(s)+6+(k%4)*7,32),u:r(),v:(r()<.5?1:-1)*(3+r()*5),c:['#ff4f6b','#33a3ff','#ffd21a','#ffffff','#7be35a','#ff9f43'][(r()*6)|0],sk:['#f1c9a5','#d9a47c','#8d5a3b'][(r()*3)|0]});
  // pantalán frente a la horquilla
  {const s=TT+1971,i=I(s),d0=W/2+34,d1=Df(s)+30,nx=-Math.cos(hs[i]),ny=-Math.sin(hs[i]),tx=Math.sin(hs[i]),ty=-Math.cos(hs[i]),pw=13;
   const p=(d,o)=>[xs[i]+nx*d+tx*o,ys[i]+ny*d+ty*o];land([p(d0,-pw),p(d1,-pw),p(d1,pw),p(d0,pw)],{draw:false});big.push({t:'pier',x:xs[i]+nx*(d0+d1)/2,y:ys[i]+ny*(d0+d1)/2,h:Math.atan2(nx,-ny),len:d1-d0,R:(d1-d0)/2+20});labels.push({x:p(d0+40,0)[0],y:p(d0+40,0)[1],txt:'PANTALÁN'});
   for(let d=d0+30;d<d1-30;d+=30)for(const o of[-1,1]){if(r()<.25)continue;const k2=r()<.6?'llaut':'rib',[x,y]=p(d,o*(pw+BOATK[k2].bl/2+2));add({t:'cboat',kind:k2,x,y,r:Math.atan2(nx,-ny)+(o>0?Math.PI/2:-Math.PI/2),...BOATK[k2],moored:1,s:(r()*1e6)|0});spots.push([x,y,26]);}
   spots.push([...p((d0+d1)/2,0),(d1-d0)/2]);}
  // islote con faro (Alcanada)
  {const s=TT+2520,[x,y]=P(s,-(W/2+186)),pts=[];for(let k=0;k<28;k++){const a=k/28*TAU,rr=66+10*Math.sin(k*1.7)+6*Math.sin(k*3.3);pts.push([x+Math.cos(a)*rr,y+Math.sin(a)*rr*.86]);}land(pts,{fill:'#8f8577',edge:'#6f665b',edgeW:4,foam:true});big.push({t:'islet',x,y,R:80});big.push({t:'faro',x:x+8,y:y-4,R:30,c:'#ff3b4f',beam:1});labels.push({x,y:y+52,txt:'ILLA D’ALCANADA'});spots.push([x,y,90]);}
  labels.push({...(()=>{const[x,y]=P(TT+1700,-(Df(TT+1700)+70));return{x,y};})(),txt:'CAP DES PINAR'});}
 // ----- barcos de espectadores y lanchas de rescate -----
 let nres=0;for(const tp of turns){if(nres>=3||tp[2].deg<90)continue;const sg=tp[2],sd=sg.k==='R'?1:-1,[x,y]=P((sg.s0+sg.s1)/2,-sd*(W/2+50));if(!free(x,y,22))continue;add({t:'cboat',kind:'resc',x,y,r:hs[I((sg.s0+sg.s1)/2)],...BOATK.resc,s:(r()*1e6)|0});spots.push([x,y,22]);nres++;}
 let bk=0;for(const tp of turns){const sg=tp[2];if(sg.deg<60)continue;const sd=sg.k==='R'?1:-1,mid=(sg.s0+sg.s1)/2,n=Math.max(1,Math.floor((sg.s1-sg.s0)*.55/64));for(let k=0;k<n;k++){const s=mid+(k-(n-1)/2)*64,[x,y]=P(s,-sd*(W/2+16)),[x2,y2]=P(s,-sd*(W/2+34));if(landIn(lands,x2,y2))continue;add({t:'cban',x,y,h:hs[I(s)],len:56,k:bk,txt:['COSTA TURBO','RIVA RACING','JJ’S SPORTS','BESO BEACH'][bk%4]});bk++;spots.push([x,y,30]);}}
 for(let s=200;s<TT;s+=95+r()*110){for(const sd of[-1,1]){if(r()<.35)continue;const d=W/2+40+r()*55,[x,y]=P(s,sd*d);if(!free(x,y,30,W/2+34))continue;const kind=['motor','llaut','sail','motor','rib'][(r()*5)|0];add({t:'cboat',kind,x,y,r:hs[I(s)]+(r()<.5?0:Math.PI)+(r()-.5)*1.1,...BOATK[kind],s:(r()*1e6)|0});spots.push([x,y,36]);}}
 O.sort((a,b)=>a.y-b.y);
 return{Z,zi,lap,len:C.L*C.laps,lenK:Math.max(1,C.L*C.laps/16000),seed,shore:()=>-1e7,kind:()=>'open',barY:1e9,bar:null,objs:O,movers:[],decos:[],gatesTotal:0,finishY:-1e9,checks:[],big:[],ring:null,swimX:()=>null,cliffK:()=>0,rwall:null,waves:[],circ:C,lands,strips,cbig:big,cars,walk,labels};}
