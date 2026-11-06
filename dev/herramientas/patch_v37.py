p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)

# ================= ZONAS =================
rep("{name:'LA FINAL',","""{name:'BAHÍA DE PALMA',obj:'race3',goal:'Circuito de 3 vueltas en la bahía de Palma, con la catedral al fondo. La pantalla gira con tu moto. Termina entre los 3 primeros; si te sales de las boyas, frenas.',len:13000,riv:5,bar:null,theme:'circ',tod:'afternoon',skill:.92,circ:'palma',laps:3},
 {name:'BAHÍA DE ALCÚDIA',obj:'race2',goal:'Circuito de 3 vueltas en la bahía de Alcúdia, con la playa de pinos y el Cap des Pinar. La pantalla gira con tu moto. Termina entre los 2 primeros.',len:13000,riv:5,bar:null,theme:'circ',tod:'morning',skill:.94,circ:'alcudia',laps:3},
 {name:'LA FINAL',""")
rep("let best=Math.max(0,Math.min(20,","let best=Math.max(0,Math.min(22,")
rep("const APP_VER=36;","const APP_VER=37;")

# ================= CONSTRUCCIÓN =================
rep("function buildZone(zi,lap){\n const Z=ZONES[zi],seed=1000+zi*977+lap*131,r=rng(seed),n1=noise1(seed),n2=noise1(seed+7);",
"""const CIRCS={
 palma:{pts:[[0,0],[420,-120],[820,-60],[1080,-380],[980,-820],[640,-940],[480,-1250],[60,-1320],[-300,-1050],[-260,-640],[-420,-300]],land:'palma'},
 alcudia:{pts:[[0,0],[0,-700],[160,-1250],[560,-1380],[900,-1150],[880,-700],[560,-560],[620,-180],[320,150]],land:'alcudia'}};
function buildCircuit(Z,zi,lap,seed){const r=rng(seed),def=CIRCS[Z.circ],P0=def.pts,n0=P0.length,step=8,W=190,raw=[];
 for(let i=0;i<n0;i++){const p0=P0[(i-1+n0)%n0],p1=P0[i],p2=P0[(i+1)%n0],p3=P0[(i+2)%n0];for(let t=0;t<1;t+=.02){const t2=t*t,t3=t2*t,f=k=>.5*((2*p1[k])+(-p0[k]+p2[k])*t+(2*p0[k]-5*p1[k]+4*p2[k]-p3[k])*t2+(-p0[k]+3*p1[k]-3*p2[k]+p3[k])*t3);raw.push([f(0),f(1)]);}}
 const R=raw.length,cl=[0];for(let i=1;i<=R;i++){const a=raw[i-1],b=raw[i%R];cl.push(cl[i-1]+Math.hypot(b[0]-a[0],b[1]-a[1]));}const LL=cl[R];
 const xs=[],ys=[];let j=0;for(let sd=0;sd<LL-step*.5;sd+=step){while(cl[j+1]<sd)j++;const a=raw[j],b=raw[(j+1)%R],t=(sd-cl[j])/((cl[j+1]-cl[j])||1);xs.push(a[0]+(b[0]-a[0])*t);ys.push(a[1]+(b[1]-a[1])*t);}
 const N=xs.length,hs=[],cum=[];for(let i=0;i<N;i++){const a=(i-1+N)%N,b=(i+1)%N;hs.push(Math.atan2(xs[b]-xs[a],-(ys[b]-ys[a])));cum.push(i*step);}
 const C={x:xs,y:ys,h:hs,cum,n:N,L:N*step,step,W,laps:Z.laps||3},O=[],add=o=>{O.push(o);return o;},lands=[];
 for(let i=0;i<N;i+=5){const h=hs[i],nx=Math.cos(h),ny=Math.sin(h);for(const sd of[-1,1])add({t:'cbuoy',x:xs[i]+nx*sd*W/2,y:ys[i]+ny*sd*W/2,c:sd<0?'#ffd21a':'#ff7a1a',ph:i*.37});}
 add({t:'cline',x:xs[0],y:ys[0],h:hs[0],w:W});
 for(let i=20;i<N;i+=34)add({t:'carrow',x:xs[i],y:ys[i],h:hs[i]});
 for(let i=40;i<N-20;i+=45+((r()*20)|0)){const lane=(r()-.5)*W*.5;for(let k=0;k<5;k++){const ii=(i+k*3)%N;add({t:'coin',x:xs[ii]+Math.cos(hs[ii])*lane,y:ys[ii]+Math.sin(hs[ii])*lane});}}
 for(let i=0;i<4;i++){const ii=(60+i*Math.floor(N/4))%N,lane=(r()<.5?-1:1)*W*.28;add({t:'rock',x:xs[ii]+Math.cos(hs[ii])*lane,y:ys[ii]+Math.sin(hs[ii])*lane,rad:9+r()*5,v:0});}
 add({t:'fuel',x:xs[Math.floor(N/2)],y:ys[Math.floor(N/2)]});
 let mnx=1e9,mxx=-1e9,mny=1e9,mxy=-1e9;for(let i=0;i<N;i++){mnx=Math.min(mnx,xs[i]);mxx=Math.max(mxx,xs[i]);mny=Math.min(mny,ys[i]);mxy=Math.max(mxy,ys[i]);}
 const poly=(pts,fill,o)=>{let b=[1e9,1e9,-1e9,-1e9];for(const[x,y]of pts)b=[Math.min(b[0],x),Math.min(b[1],y),Math.max(b[2],x),Math.max(b[3],y)];lands.push(Object.assign({pts,fill,bb:b},o||{}));};
 if(def.land==='palma'){const cy0=mny-280,coast=x=>cy0+38*Math.sin(x/260)+18*Math.sin(x/90),pts=[];for(let x=mnx-1400;x<=mxx+1400;x+=40)pts.push([x,coast(x)]);pts.push([mxx+1400,cy0-2400],[mnx-1400,cy0-2400]);poly(pts,'#e7dcc6',{sand:'#efe0bf',sandW:30});
  const cx=(mnx+mxx)/2-150;add({t:'seu',x:cx,y:coast(cx)-130});
  for(let x=mnx-1300;x<mxx+1300;x+=36+r()*30){const cy=coast(x);add({t:'cdeco',x,y:cy-30,d:{t:'palm',x,y:cy-30,r:13+r()*4,s:(r()*1e6)|0}});if(Math.abs(x-cx)<180)continue;for(let row=0;row<3;row++){if(r()<.25)continue;const w=26+r()*24,h=26+r()*30;add({t:'cbld',x,y:cy-80-row*70-r()*20,w,h,c:['#f4efe6','#ead9b9','#f2c9a0','#dfe7ee','#e7c08e'][(r()*5)|0],roof:r()<.4});}}}
 if(def.land==='alcudia'){const cx0=mnx-300,coast=y=>cx0+34*Math.sin(y/240)+14*Math.sin(y/80),pts=[];for(let y=mxy+1400;y>=mny-1400;y-=40)pts.push([coast(y),y]);pts.push([cx0-2400,mny-1400],[cx0-2400,mxy+1400]);poly(pts,'#4f7f3a',{sand:'#f1d9a6',sandW:60});
  for(let y=mny-1300;y<mxy+1300;y+=30+r()*30){const x=coast(y);if(r()<.5){const ux=x-26-r()*20;add({t:'cdeco',x:ux,y,d:{t:'umb',x:ux,y,s:16,c:r()<.6?'#ffffff':['#ff4f6b','#33a3ff','#ffd21a'][(r()*3)|0]}});}const px=x-90-r()*220;add({t:'cdeco',x:px,y,d:{t:'pine',x:px,y,r:12+r()*10,s:(r()*1e6)|0}});}
  const my=mny-420,mx0=(mnx+mxx)/2-200,mp=[];for(let x=mx0;x<=mxx+1600;x+=40)mp.push([x,my+40*Math.sin(x/200)]);mp.push([mxx+1600,my-2400],[mx0,my-2400]);poly(mp,'#6f6a4a',{});
  for(let i=0;i<70;i++){const x=mx0+50+r()*(mxx+1500-mx0),y=my-40-r()*600;add({t:'cdeco',x,y,d:{t:'pine',x,y,r:10+r()*10,s:(r()*1e6)|0}});}}
 O.sort((a,b)=>a.y-b.y);
 return{Z,zi,lap,len:C.L*C.laps,lenK:1,seed,shore:()=>-1e7,kind:()=>'open',barY:1e9,bar:null,objs:O,movers:[],decos:[],gatesTotal:0,finishY:-1e9,checks:[],big:[],ring:null,swimX:()=>null,cliffK:()=>0,rwall:null,waves:[],circ:C,lands};}
function circProg(c){const C=G.zone.circ,N=C.n;if(c.cs==null){let b=0,bd=1e18;for(let i=0;i<N;i++){const d=(C.x[i]-c.x)**2+(C.y[i]-c.y)**2;if(d<bd){bd=d;b=i;}}c.cs=b;}
 let best=c.cs,bd=1e18;for(let k=-25;k<=25;k++){const i=(c.cs+k+N)%N,d=(C.x[i]-c.x)**2+(C.y[i]-c.y)**2;if(d<bd){bd=d;best=i;}}
 const di=best-c.cs;if(di<-N/2)c.lapN=(c.lapN|0)+1;else if(di>N/2)c.lapN=(c.lapN|0)-1;c.cs=best;c.prog=(c.lapN|0)*C.L+C.cum[best];c.off=Math.sqrt(bd);c.tang=C.h[best];}
function circGrid(){const C=G.zone.circ,list=[...G.rivals,G.P];list.forEach((c,j)=>{const row=Math.floor(j/2),col=j%2,sd=150-row*48,i=((Math.round(sd/C.step))%C.n+C.n)%C.n,lane=(col?1:-1)*44;c.x=C.x[i]+Math.cos(C.h[i])*lane;c.y=C.y[i]+Math.sin(C.h[i])*lane;c.h=c.va=C.h[i];c.cs=i;c.lapN=0;c.prog=sd;c.prevY=c.y;c.trail=[];});G._lapShown=null;G._wrongT=0;}
function circTick(dt){const C=G.zone.circ;
 for(const c of crafts()){circProg(c);
  if(c.off>C.W/2+8&&c.air<=0){c.v*=1-1.8*dt;if(c.off>C.W/2+110){const i=c.cs;c.x+=(C.x[i]-c.x)*Math.min(1,dt*2);c.y+=(C.y[i]-c.y)*Math.min(1,dt*2);}if(c.isP&&!G.demo&&!(c._offT>0)){c._offT=1.6;pop(c.x,c.y-40,'¡FUERA DEL CIRCUITO!','#ff4757');}}
  if(c._offT>0)c._offT-=dt;
  if(!c.fin&&c.prog>=C.laps*C.L){c.fin=1;c.finT=G.elapsed;G.finishOrder.push(c);if(c.isP&&!G.demo)finishZone();}
  if(c.isP&&!G.demo&&G.mode==='play'&&!c.fin){const lp=Math.max(0,c.lapN|0);if(lp!==G._lapShown){if(G._lapShown!=null&&lp>G._lapShown){msg(lp===C.laps-1?'¡ÚLTIMA VUELTA!':'VUELTA '+(lp+1)+' / '+C.laps,'','var(--cyan)');Snd.check();}G._lapShown=lp;}
   const fx=Math.sin(c.va),fy=-Math.cos(c.va),tx=Math.sin(c.tang),ty=-Math.cos(c.tang);if(c.v>80&&fx*tx+fy*ty<-.3){G._wrongT=(G._wrongT||0)+dt;if(G._wrongT>1.2){G._wrongT=-2;msg('¡SENTIDO CONTRARIO!','Da la vuelta','var(--red)');}}else if(G._wrongT>0)G._wrongT=0;}}}
function aiCirc(c,dt){const C=G.zone.circ,N=C.n;if(c.cs==null)circProg(c);if(c.lane==null)c.lane=(Math.random()-.5)*C.W*.5;c.ai.re-=dt;if(c.ai.re<=0){c.ai.re=2+Math.random()*3;c.lane=clamp(c.lane+(Math.random()-.5)*50,-C.W*.32,C.W*.32);}
 const look=Math.round((60+Math.abs(c.v)*.45)/C.step),i=(c.cs+look)%N,h=C.h[i],tx=C.x[i]+Math.cos(h)*c.lane,ty=C.y[i]+Math.sin(h)*c.lane;
 let d=Math.atan2(tx-c.x,-(ty-c.y))-c.h;while(d>Math.PI)d-=TAU;while(d<-Math.PI)d+=TAU;const turn=d>.04?1:d<-.04?-1:0;
 let tv=c.st.maxV*(c.skill||.9);const P=G.P;if(P){const gap=(P.prog||0)-(c.prog||0);if(gap>420)tv*=1.12;else if(gap<-650)tv*=.9;}
 const ah=(c.cs+Math.round(160/C.step))%N;let cv=C.h[ah]-C.h[c.cs];while(cv>Math.PI)cv-=TAU;while(cv<-Math.PI)cv+=TAU;tv*=1-Math.min(.35,Math.abs(cv)*.35);
 if(c.boostT<=0&&Math.random()<dt*.03)c.boostT=c.st.bt;return{turn,thr:c.v<tv,rev:false,drift:false};}
function drawCircuit(Zn){const C=Zn.circ,x0=camX,x1=camX+VW,y0=camTop,y1=camTop+VH;
 for(const Ld of Zn.lands){const b=Ld.bb;if(b[2]<x0-80||b[0]>x1+80||b[3]<y0-80||b[1]>y1+80)continue;const path=()=>{ctx.beginPath();Ld.pts.forEach(([x,y],i)=>i?ctx.lineTo(x,y):ctx.moveTo(x,y));ctx.closePath();};
  ctx.save();ctx.lineJoin='round';path();ctx.strokeStyle='rgba(120,230,225,.45)';ctx.lineWidth=80;ctx.stroke();ctx.fillStyle=Ld.fill;ctx.fill();
  if(Ld.sand){ctx.save();path();ctx.clip();ctx.strokeStyle=Ld.sand;ctx.lineWidth=(Ld.sandW||40)*2;path();ctx.stroke();ctx.restore();}
  ctx.strokeStyle='rgba(255,255,255,.75)';ctx.lineWidth=2.4;ctx.setLineDash([3,4]);path();ctx.stroke();ctx.setLineDash([]);ctx.restore();}
 ctx.save();ctx.lineJoin='round';ctx.lineCap='round';ctx.strokeStyle='rgba(255,255,255,.07)';ctx.lineWidth=C.W;ctx.beginPath();let st=false;for(let i=0;i<=C.n;i++){const k=i%C.n,x=C.x[k],y=C.y[k],vis=x>x0-C.W&&x<x1+C.W&&y>y0-C.W&&y<y1+C.W;if(vis){st?ctx.lineTo(x,y):ctx.moveTo(x,y);st=true;}else st=false;}ctx.stroke();ctx.restore();}
function buildZone(zi,lap){
 const Z=ZONES[zi],seed=1000+zi*977+lap*131,r=rng(seed),n1=noise1(seed),n2=noise1(seed+7);
 if(Z.circ)return buildCircuit(Z,zi,lap,seed);""")

# ================= FÍSICA =================
rep("else{c.h+=ctl.turn*st.turn*dt*(.5+.5*clamp(Math.abs(c.v)/st.maxV,0,1));if(!ctl.turn)c.h*=1-2.4*dt;}",
    "else{c.h+=ctl.turn*st.turn*dt*(.5+.5*clamp(Math.abs(c.v)/st.maxV,0,1));if(!ctl.turn&&!Zn.circ)c.h*=1-2.4*dt;}")
rep("if(drifting)c.h=clamp(c.h,-1.25,1.25);else if(Math.abs(c.h)>1.05)c.h=Math.sign(c.h)*Math.max(1.05,Math.abs(c.h)-2.2*dt);}",
    "if(!Zn.circ){if(drifting)c.h=clamp(c.h,-1.25,1.25);else if(Math.abs(c.h)>1.05)c.h=Math.sign(c.h)*Math.max(1.05,Math.abs(c.h)-2.2*dt);}}")
rep(" const sx=Zn.shore(c.y)+11;if(c.x<sx){"," if(!Zn.circ){const sx=Zn.shore(c.y)+11;if(c.x<sx){")
rep("const ex=(VW>WG?WG+(VW-WG)/2:WG)-11;if(c.x>ex){c.x=ex;if(c.h>0)c.h=-Math.abs(c.h)*.4;c.va=c.h;c.v*=1-3*dt;}",
    "const ex=(VW>WG?WG+(VW-WG)/2:WG)-11;if(c.x>ex){c.x=ex;if(c.h>0)c.h=-Math.abs(c.h)*.4;c.va=c.h;c.v*=1-3*dt;}}")
rep("function aiCtl(c,dt){const Zn=G.zone,","function aiCtl(c,dt){if(G.zone.circ)return aiCirc(c,dt);const Zn=G.zone,")
rep(" for(const c of G.rivals){if(G.mode==='count'){c.prevY=c.y;continue;}updateCraft(c,dt,c.fin?{turn:0,thr:true}:aiCtl(c,dt));}",
    " for(const c of G.rivals){if(G.mode==='count'){c.prevY=c.y;continue;}updateCraft(c,dt,c.fin?{turn:0,thr:true}:aiCtl(c,dt));}\n if(Zn.circ&&!G.demo)circTick(dt);")
rep(" camTop=G.P.y-VH*.73;camX=-(VW-WG)/2;if(camX>0)camX=0;"," camTop=G.P.y-VH*.73;camX=-(VW-WG)/2;if(camX>0)camX=0;if(Zn.circ)circGrid();G.camA=G.P.va||0;")
rep(" // camera\n const target=P.y-VH*.73;camTop+=(target-camTop)*Math.min(1,dt*8);\n if(Math.abs(target-camTop)>VH)camTop=target;\n camX=VW>WG?-(VW-WG)/2:0;",
    " // camera\n if(Zn.circ){let d=(P.va||0)-(G.camA||0);while(d>Math.PI)d-=TAU;while(d<-Math.PI)d+=TAU;G.camA=(G.camA||0)+d*Math.min(1,dt*3.2);}else{\n const target=P.y-VH*.73;camTop+=(target-camTop)*Math.min(1,dt*8);\n if(Math.abs(target-camTop)>VH)camTop=target;\n camX=VW>WG?-(VW-WG)/2:0;}")
# HUD
rep("if(Z.riv){const order=crafts().slice().sort((a,b)=>(b.fin?1e9-b.finT:0)-(a.fin?1e9-a.finT:0)||a.y-b.y);P.rank=order.indexOf(P)+1;setTxt('hlL','POSICIÓN');",
    "if(Z.riv){const order=crafts().slice().sort((a,b)=>(b.fin?1e9-b.finT:0)-(a.fin?1e9-a.finT:0)||(Zn.circ?(b.prog||0)-(a.prog||0):a.y-b.y));P.rank=order.indexOf(P)+1;setTxt('hlL',Zn.circ?'VUELTA '+Math.min(Zn.circ.laps,Math.max(0,P.lapN|0)+1)+'/'+Zn.circ.laps:'POSICIÓN');")
rep("for(const c of crafts()){if(!c._dot)continue;const p=clamp((c.y-Zn.finishY)/(0-Zn.finishY),0,1);",
    "for(const c of crafts()){if(!c._dot)continue;const p=Zn.circ?clamp(1-(c.prog||0)/(Zn.circ.laps*Zn.circ.L),0,1):clamp((c.y-Zn.finishY)/(0-Zn.finishY),0,1);")
# ================= CÁMARA / DIBUJO =================
rep("const MIR=!!(Zn.Z.mirror&&!G.demo);if(MIR)ctx.setTransform(",
    "const CIRC=!!(Zn.circ&&G.P);let sv=null;if(CIRC){const RR=Math.hypot(VW*.5,VH*.72)+80;sv=[VW,VH,camX,camTop];camX=G.P.x-RR;camTop=G.P.y-RR;VW=VH=2*RR;}\n const MIR=!CIRC&&!!(Zn.Z.mirror&&!G.demo);if(CIRC){ctx.setTransform(K,0,0,K,0,0);ctx.translate(sv[0]/2+sx,sv[1]*.7+sy);ctx.rotate(-(G.camA||0));ctx.translate(-G.P.x,-G.P.y);}else if(MIR)ctx.setTransform(")
rep(" else{const[x0]=chunkRange();for(let i=Math.floor(camTop/CH);"," else if(!Zn.circ){const[x0]=chunkRange();for(let i=Math.floor(camTop/CH);")
rep(" // bar ring"," if(Zn.circ)drawCircuit(Zn);\n // bar ring")
rep("for(const p of G.pops){const a=clamp(p.life*1.6,0,1);ctx.globalAlpha=a;const y=p.y-(1.1-p.life)*26;ctx.strokeText(p.txt,p.x,y);ctx.fillStyle=p.col;ctx.fillText(p.txt,p.x,y);}",
    "for(const p of G.pops){const a=clamp(p.life*1.6,0,1);ctx.globalAlpha=a;const y=p.y-(1.1-p.life)*26;if(CIRC){ctx.save();ctx.translate(p.x,p.y);ctx.rotate(G.camA||0);ctx.translate(0,-(1.1-p.life)*26);ctx.strokeText(p.txt,0,0);ctx.fillStyle=p.col;ctx.fillText(p.txt,0,0);ctx.restore();}else{ctx.strokeText(p.txt,p.x,y);ctx.fillStyle=p.col;ctx.fillText(p.txt,p.x,y);}}")
rep(" // time of day\n mirText(false);"," if(sv){VW=sv[0];VH=sv[1];camX=sv[2];camTop=sv[3];}\n // time of day\n mirText(false);")
rep(" case 'cata':{",""" case 'cbuoy':{const b=Math.sin(t*3+o.ph)*.6;ctx.fillStyle='rgba(0,20,50,.25)';ctx.beginPath();ctx.ellipse(o.x+2,o.y+3,5,3,0,0,TAU);ctx.fill();ctx.fillStyle=o.c;ctx.beginPath();ctx.arc(o.x,o.y+b,4.6,0,TAU);ctx.fill();ctx.fillStyle='rgba(255,255,255,.65)';ctx.beginPath();ctx.arc(o.x-1.4,o.y-1.6+b,1.6,0,TAU);ctx.fill();}return;
 case 'cline':{ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);const w=o.w,n=Math.floor(w/10);for(let i=0;i<n;i++)for(let k=0;k<2;k++){ctx.fillStyle=(i+k)%2?'#ffffff':'#111111';ctx.fillRect(-n*5+i*10,-10+k*10,10,10);}ctx.fillStyle='rgba(8,22,48,.75)';ctx.beginPath();ctx.roundRect(-40,-32,80,16,7);ctx.fill();ctx.fillStyle='#ffc93c';ctx.font='800 11px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('SALIDA · META',0,-23.5);ctx.restore();}return;
 case 'carrow':{ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);ctx.globalAlpha=.35;ctx.strokeStyle='#ffffff';ctx.lineWidth=4;ctx.lineCap='round';ctx.lineJoin='round';for(let k=0;k<2;k++){ctx.beginPath();ctx.moveTo(-14,8-k*14);ctx.lineTo(0,-6-k*14);ctx.lineTo(14,8-k*14);ctx.stroke();}ctx.restore();}return;
 case 'cbld':{ctx.fillStyle='rgba(0,0,0,.18)';ctx.fillRect(o.x-o.w/2+5,o.y-o.h/2+5,o.w,o.h);ctx.fillStyle=o.c;ctx.fillRect(o.x-o.w/2,o.y-o.h/2,o.w,o.h);if(o.roof){ctx.fillStyle='#c4683c';ctx.fillRect(o.x-o.w/2,o.y-o.h/2,o.w,o.h*.4);}ctx.strokeStyle='rgba(0,0,0,.1)';ctx.lineWidth=1;ctx.strokeRect(o.x-o.w/2,o.y-o.h/2,o.w,o.h);}return;
 case 'cdeco':drawDeco(ctx,o.d);return;
 case 'seu':{ctx.save();ctx.translate(o.x,o.y);ctx.fillStyle='rgba(0,0,0,.2)';ctx.fillRect(-122,-36,250,84);ctx.fillStyle='#d9b98a';ctx.fillRect(-130,-44,250,84);ctx.fillStyle='#c7a676';for(let i=0;i<11;i++)ctx.fillRect(-128+i*24,-52,8,100);ctx.fillStyle='#b8946a';ctx.fillRect(-130,-10,250,6);ctx.fillStyle='#e6c99a';ctx.beginPath();ctx.arc(-110,0,22,0,TAU);ctx.fill();ctx.strokeStyle='#b8946a';ctx.lineWidth=2;for(let k=0;k<8;k++){ctx.beginPath();ctx.moveTo(-110,0);ctx.lineTo(-110+Math.cos(k*.785)*20,Math.sin(k*.785)*20);ctx.stroke();}ctx.fillStyle='#a4825a';ctx.fillRect(100,-58,26,26);
  ctx.fillStyle='rgba(8,22,48,.72)';ctx.beginPath();ctx.roundRect(-30,58,60,16,7);ctx.fill();ctx.fillStyle='#ffc93c';ctx.font='800 11px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('LA SEU',0,66.5);ctx.restore();}return;
 case 'cata':{""")

# ================= PORTADAS =================
rep(" {tag:'GANA A EL TIBURÓN',",""" {tag:'CIRCUITO · 3 VUELTAS',sky:['#3f7fd6','#ffd9a8'],sea:['#5ab0dc','#0a4a8e'],sun:[330,44,'#fff0c8'],land:'palma'},
 {tag:'CIRCUITO · 3 VUELTAS',sky:['#2f8de6','#d4f0ff'],sea:['#6fd0ea','#0b5aa8'],sun:[70,26,'#fffbe8'],land:'alcudia'},
 {tag:'GANA A EL TIBURÓN',""")
rep("\n if(L==='vedra'){","""\n if(L==='palma'){cvRidge(g,q,-20,420,HZ-6,34,6,'#8a9a7a');g.fillStyle=rgbaH(C.sky[1],.3);g.fillRect(0,30,W,HZ-30);cvCity(g,q,0,400,HZ,18);g.fillStyle='#d6b07a';g.fillRect(70,HZ-34,120,32);for(let i=0;i<9;i++){g.fillStyle='#c79c62';g.fillRect(72+i*14,HZ-46,5,44);g.beginPath();g.moveTo(72+i*14,HZ-46);g.lineTo(74.5+i*14,HZ-54);g.lineTo(77+i*14,HZ-46);g.fill();}g.fillStyle='#e7c99a';g.beginPath();g.arc(92,HZ-20,7,0,TAU);g.fill();g.fillStyle='#b88a52';g.fillRect(168,HZ-58,14,56);cvPalm(g,220,HZ+2,.6);cvPalm(g,240,HZ+3,.55);}
 if(L==='alcudia'){g.fillStyle='#f1d9a6';g.beginPath();g.moveTo(-10,HZ+2);g.lineTo(240,HZ+2);g.lineTo(240,HZ-3);g.lineTo(-10,HZ-6);g.closePath();g.fill();for(let i=0;i<22;i++){g.fillStyle=i%2?'#2f5a26':'#3b6b2c';g.beginPath();g.arc(q()*230,HZ-8-q()*6,3+q()*3,0,TAU);g.fill();}cvMount(g,q,250,400,HZ+2,26,'#5f6b4a','rgba(30,36,24,.4)');}
 if(L==='vedra'){""")
rep(" else if(L==='vedra'){",""" else if(L==='palma'||L==='alcudia'){for(let i=0;i<15;i++){const t=i/14,x=30+t*340,y=HZ+12+Math.sin(t*Math.PI)*52+t*24;cvBuoy(g,x,y,1.6+(y-HZ)*.055);}cvRival(g,q,rv(0),150,150,.25,-.2);cvRival(g,q,rv(1),220,138,.21,-.25);hero(285,175,.42,-.3,0);}
 else if(L==='vedra'){""")
open(p,'w').write(s);print('ok')
