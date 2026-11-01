import shutil
H='costa-turbo.html'
shutil.copy(H,'costa-turbo.pre-v59b.html')
h=open(H).read()
def rep(s,a,b,n=1):
    c=s.count(a)
    assert c==n,(c,a[:90])
    return s.replace(a,b)

PREPOST="const PRE=def.pre||[],POST=def.post||[],segL=sg=>sg[0]==='S'?sg[1]:sg[1]*Math.PI/180*sg[2];for(const sg of[...PRE,...def.segs,...POST]){"
LEN="const Lt=(N-1)*step,S0=Math.round(PRE.reduce((a,sg)=>a+segL(sg),0)/step)*step,PO=POST.reduce((a,sg)=>a+segL(sg),0),Lp=Math.round(Lt-S0-PO),"

# ---------------- archi (Bahamas / Es Trenc) ----------------
a0=open('archi2.js').read()
a=a0
a=rep(a,"CIRCS.bahamas={h0:0,open:1,archi:1,style:'bahamas',W:320,segs:","CIRCS.bahamas={h0:0,open:1,archi:1,style:'bahamas',W:320,pre:[['R',30,700],['S',300]],post:[['S',300],['L',40,700],['S',500],['R',35,700],['S',400]],segs:")
a=rep(a,"CIRCS.trenc={h0:0,open:1,archi:1,style:'trenc',W:350,segs:","CIRCS.trenc={h0:0,open:1,archi:1,style:'trenc',W:350,pre:[['L',20,1000],['S',300]],post:[['S',300],['R',25,1100],['S',600],['L',20,1100],['S',300]],segs:")
a=rep(a,"for(const sg of def.segs){",PREPOST)
a=rep(a,"const Lp=(N-1)*step,C={x:xs,y:ys,h:hs,cum,n:N,L:Lp,step,W,laps:1,open:1,archi:1,style:ST,finS:Lp-320}",LEN+"C={x:xs,y:ys,h:hs,cum,n:N,L:Lt,step,W,laps:1,open:1,archi:1,style:ST,finS:S0+Lp-320,s0:S0}")
a=rep(a,"const I=s=>Math.max(0,Math.min(N-1,Math.round(s/step)))","const I=s=>Math.max(0,Math.min(N-1,Math.round((s+S0)/step)))")
a=rep(a,"const finS=C.finS,calm=s=>Math.min(sm(60,300,s),sm(Lp-60,Lp-500,s),sm(40,200,Math.abs(s-finS)));","const finS=Lp-320,calm=s=>Math.min(sm(40,260,Math.abs(s-40)),sm(40,200,Math.abs(s-finS)));")
a=rep(a,"for(let s=2600;s<Lp-1500;s+=2400+rr()*1400){if(mids.some(m=>Math.abs(m.s-s)<900))s+=900;nar.push","for(let s=2600;s<Lp-1500;s+=2400+rr()*1400){if(mids.some(m=>Math.abs(m.s-s)<900))s+=900;if(mids.some(m=>Math.abs(m.s-s)<900))continue;nar.push")
a=rep(a,"const wl=[],wr=[];for(let i=0;i<N;i++){const s=i*step;","const wl=[],wr=[];for(let i=0;i<N;i++){const s=i*step-S0;")
# pasos de Es Trenc: hueco pegado a la playa, isla a la derecha
a=rep(a,"C.gaps=gaps.map(q=>({i:I(q.s),lat:q.g,w:q.w}));","for(const q of gaps){const i=I(q.s);q.w=112+rr()*24;q.e=-wl[i]+q.w;q.g=-wl[i]+q.w/2+4;}C.gaps=gaps.map(q=>({i:I(q.s),lat:q.g,w:q.w}));")
a=rep(a,"{s:C.finS,txt:'META',col:'#ffc93c'}","{s:finS,txt:'META',col:'#ffc93c'}")
a=rep(a," // cayos pequeños\n",""" // islas que cierran los pasos estrechos contra la playa (Es Trenc)
 for(const q of gaps){const i=I(q.s),nx=Math.cos(hs[i]),ny=Math.sin(hs[i]),aR=(wr[i]+470-q.e)/2,bR=150+rr()*60,o={rad:aR,mid:0,noSpit:1,big:1,pass:1,rot:hs[i]};o.x=xs[i]+nx*(q.e+aR);o.y=ys[i]+ny*(q.e+aR);mkShape(o);o.R0=aR;o.el=bR/aR;o.maxR=aR*1.35;
  let sp=shapePts(o),mn=1e9;for(const[px,py]of sp.pts){const lat=(px-xs[i])*nx+(py-ys[i])*ny;if(lat<mn)mn=lat;}const sh=q.e-mn;o.x+=nx*sh;o.y+=ny*sh;o.sp=shapePts(o);isl.push(o);}
 // cayos pequeños
""")
a=rep(a,"for(let s=-300;s<Lp+600;s+=(TR?70:40)+rr()*60)","for(let s=-S0-300;s<Lp+PO+300;s+=(TR?70:40)+rr()*60)")
a=rep(a,"o.x=xs[i]+Math.cos(hs[i])*sd*off+(s<0?Math.sin(hs[0])*s:0);o.y=ys[i]+Math.sin(hs[i])*sd*off-(s<0?Math.cos(hs[0])*s:0);","const ee=s<-S0?s+S0:(s>Lp+PO?s-Lp-PO:0),he=hs[s<-S0?0:N-1];o.x=xs[i]+Math.cos(hs[i])*sd*off+Math.sin(he)*ee;o.y=ys[i]+Math.sin(hs[i])*sd*off-Math.cos(he)*ee;")
a=rep(a,"const np=TR?(o.rad>40?2:1):","const np=o.pass?12:TR?(o.rad>40?2:1):")
# quitar cuña + banco + ola; monedas por el paso
i0=a.index(" // ----- Es Trenc: pasos estrechos");i1=a.index(" // ----- Es Trenc: playa")
a=a[:i0]+""" // ----- Es Trenc: monedas por el paso -----
 for(const q of gaps){const i=I(q.s);for(let k=0;k<4;k++){const[cx,cy]=loc(i,q.g,-90+k*60);add({t:'coin',x:cx,y:cy});}{const[lx,ly]=loc(i,q.g,-170);labels.push({x:lx,y:ly,txt:'PASO'});}}
"""+a[i1:]
a=rep(a,"if(TR){for(let s=-200;s<Lp+300;s+=22){const i=I(s);if(gaps.some(q=>Math.abs(q.s-s)<260))continue;","if(TR){for(let s=-S0;s<Lp+PO;s+=22){const i=I(s);")
a=rep(a,"{const i=N-1;labels.push({x:xs[i],y:ys[i],txt:'ES TRENC'});}","{const i=I(Lp);labels.push({x:xs[i],y:ys[i],txt:'ES TRENC'});}")
a=rep(a,"const bars=[];for(let s=0;s<Lp;s+=","const bars=[];for(let s=-S0;s<Lp+PO;s+=")
a=rep(a,"for(let k=0;k<Lp/160;k++){const s=rr()*Lp,","for(let k=0;k<Lt/160;k++){const s=-S0+rr()*Lt,")
a=rep(a,"const anch=[];for(let s=500;s<Lp-200;s+=","const anch=[];for(let s=-S0+200;s<Lp+PO-200;s+=")
a=rep(a,"{const i=I(C.finS);add({t:'cline'","{const i=I(finS);add({t:'cline'")
a=rep(a,"for(let i=40;i<N-40;i+=40)add({t:'carrow',x:xs[i],y:ys[i],h:hs[i]});","for(let i=I(0)+40;i<I(finS);i+=40){if(gaps.some(q=>Math.abs(q.s-(i*step-S0))<300))continue;add({t:'carrow',x:xs[i],y:ys[i],h:hs[i]});}")
a=rep(a,"const j2=N-1;","const j2=I(Lp);")
# colores: camino casi igual que los bajíos, bordes suaves
a=rep(a,"ctx.fillStyle=TR?'#7fe3e8':'#46cede';","ctx.fillStyle=TR?'#79e1e8':'#5ad4e3';")
a=rep(a,"ctx.strokeStyle=TR?'rgba(30,160,205,.45)':'rgba(25,115,190,.45)';ctx.lineWidth=TR?50:56;","ctx.strokeStyle=TR?'rgba(40,175,210,.2)':'rgba(30,150,200,.22)';ctx.lineWidth=TR?50:56;")
a=rep(a,"ctx.strokeStyle=TR?'rgba(50,185,215,.35)':'rgba(45,160,215,.4)';","ctx.strokeStyle=TR?'rgba(70,200,225,.18)':'rgba(60,185,220,.2)';")
open('archi3.js','w').write(a)
h=rep(h,a0.strip(),a.strip())

# ---------------- Sa Calobra ----------------
h=rep(h,"CIRCS.calobra={h0:0,open:1,canyon:1,W:430,segs:","CIRCS.calobra={h0:0,open:1,canyon:1,W:430,pre:[['L',35,600],['S',300]],post:[['S',300],['L',45,500],['S',400],['R',40,520],['S',500]],segs:")
c0=h.index("function buildCanyon(");c1=h.index("function rockTile(")
c=h[c0:c1]
c=rep(c,"for(const sg of def.segs){",PREPOST)
c=rep(c,"const Lp=(N-1)*step,C={x:xs,y:ys,h:hs,cum,n:N,L:Lp,step,W,laps:1,open:1,canyon:1,finS:Lp-260}",LEN+"C={x:xs,y:ys,h:hs,cum,n:N,L:Lt,step,W,laps:1,open:1,canyon:1,finS:S0+Lp-260,s0:S0}")
c=rep(c,"const I=s=>Math.max(0,Math.min(N-1,Math.round(s/step)))","const I=s=>Math.max(0,Math.min(N-1,Math.round((s+S0)/step)))")
c=rep(c,"const archS=[40,Math.round(Lp/3),Math.round(Lp*2/3),C.finS]","const archS=[40,Math.round(Lp/3),Math.round(Lp*2/3),Lp-260]")
c=rep(c,"for(let s=1100;s<Lp-1100;s+=1100+rr()*900)","for(let s=-S0+300;s<Lp+PO-300;s+=1100+rr()*900)")
c=rep(c,"for(let s=650;s<Lp-650;s+=300+rr()*420)","for(let s=-S0+200;s<Lp+PO-200;s+=300+rr()*420)")
c=rep(c,"const calm=s=>{let k=Math.min(sm(60,260,s),sm(Lp-60,Lp-420,s));for","const calm=s=>{let k=1;for")
c=rep(c,"for(let i=0;i<N;i++){const s=i*step,k=calm(s);","for(let i=0;i<N;i++){const s=i*step-S0,k=calm(s);")
c=rep(c,"{s:C.finS,txt:'META',col:'#ffc93c'}","{s:Lp-260,txt:'META',col:'#ffc93c'}")
c=rep(c,"C.cps=[{s:Math.round(Lp/3)},{s:Math.round(Lp*2/3)}];C.beach=I(Lp-170);","C.cps=[{s:S0+Math.round(Lp/3)},{s:S0+Math.round(Lp*2/3)}];")
c=rep(c,"{const i=I(C.finS);add({t:'cline'","{const i=I(Lp-260);add({t:'cline'")
c=rep(c,"for(let i=40;i<N-40;i+=34)add({t:'carrow'","for(let i=I(0)+40;i<I(Lp-260);i+=34)add({t:'carrow'")
c=rep(c,"for(const c of cov){if(c.d<85||c.s>Lp-900)continue;","for(const c of cov){if(c.d<85||Math.abs(c.s-40)<300||Math.abs(c.s-(Lp-260))<300)continue;")
c=rep(c,"for(let s=0;s<Lp+200;s+=26)","for(let s=-S0;s<Lp+PO;s+=26)")
c=rep(c," for(const[s,lat]of[[Lp-130,-W*.32],[Lp-100,W*.34]]){const i=I(s);add({t:'cboat',kind:'motor',x:xs[i]+Math.cos(hs[i])*lat,y:ys[i]+Math.sin(hs[i])*lat,r:hs[i]+(lat<0?.4:-.4),...BOATK.motor,moored:1,s:(r()*1e6)|0});}\n","")
c=rep(c,"{const i=N-1;labels.push({x:xs[i],y:ys[i],txt:'SA CALOBRA'});}","{const i=I(Lp);labels.push({x:xs[i],y:ys[i],txt:'SA CALOBRA'});}")
h=h[:c0]+c+h[c1:]

# ---------------- motor de circuitos ----------------
h=rep(h,"const row=Math.floor(j/2),col=j%2,sd=170-row*56,","const row=Math.floor(j/2),col=j%2,sd=(C.s0||0)+170-row*56,")
h=rep(h,"if(C.gaps)for(const q of C.gaps){if(q.i-c.cs<95&&q.i-c.cs>-6)","if(C.gaps)for(const q of C.gaps){if(q.i-c.cs<95&&q.i-c.cs>-26)")
h=rep(h,"if(Math.abs(lat)>lim&&c.air<=0){c.v*=1-1.5*dt;if(c.isP&&!G.demo&&!(c._offT>0)){c._offT=1.8;pop(c.x,c.y-40,'¡BAJÍO!','#ffb84d');}}if(Math.abs(lat)>lim+300){",
        "if(Math.abs(lat)>lim+230&&c.air<=0){c.v*=1-1.5*dt;if(c.isP&&!G.demo&&!(c._offT>0)){c._offT=1.8;pop(c.x,c.y-40,'¡FUERA DEL CAMINO!','#ff4757');}}if(Math.abs(lat)>lim+330){")
# no salir por los extremos del tramo
h=rep(h,"function circTick(dt){const C=G.zone.circ,LDS=G.zone.lands;\n for(const c of crafts()){circProg(c);",
        "function circTick(dt){const C=G.zone.circ,LDS=G.zone.lands;\n for(const c of crafts()){circProg(c);\n  if(C.open&&(c.cs<=2||c.cs>=C.n-3)){const e0=c.cs<=2?0:C.n-1,sg=e0?1:-1,fx=Math.sin(C.h[e0]),fy=-Math.cos(C.h[e0]),d=((c.x-C.x[e0])*fx+(c.y-C.y[e0])*fy)*sg;if(d>-30){c.x-=fx*sg*(d+30);c.y-=fy*sg*(d+30);c.v*=.5;}}")
# minimapa: solo de la salida a la meta
h=rep(h,"let a=1e9,b=1e9,c=-1e9,d=-1e9;for(let i=0;i<C.n;i++){a=Math.min(a,C.x[i]);",
        "const mA=C.open?Math.round((C.s0||0)/C.step):0,mB=C.open?Math.min(C.n-1,Math.round(C.finS/C.step)):C.n-1;let a=1e9,b=1e9,c=-1e9,d=-1e9;for(let i=mA;i<=mB;i++){a=Math.min(a,C.x[i]);")
h=rep(h,"g.lineJoin='round';g.beginPath();for(let i=0;i<=(C.open?C.n-1:C.n);i++){const k=i%C.n;i?g.lineTo(",
        "g.lineJoin='round';g.beginPath();for(let i=mA;i<=(C.open?mB:C.n);i++){const k=i%C.n;i>mA?g.lineTo(")
h=rep(h,"const h=C.h[0],sx=C.x[0]*sc+ox,sy=C.y[0]*sc+oy;","const h=C.h[mA],sx=C.x[mA]*sc+ox,sy=C.y[mA]*sc+oy;")
h=rep(h,"if(C.open){const ex=C.x[C.n-1]*sc+ox,ey=C.y[C.n-1]*sc+oy;","if(C.open){const ex=C.x[mB]*sc+ox,ey=C.y[mB]*sc+oy;")

# ---------------- textos que no se pisan ----------------
h=rep(h,"function pop(x,y,txt,col){const P=G.P;let f=null;if(P&&Math.hypot(x-P.x,y-P.y)<140){const n=G.pops.filter(q=>q.f&&q.life>.45).length;f={dx:0,dy:Math.min(-34,y-P.y)-n*22};}G.pops.push({x,y,txt,col:col||'#fff',life:2.2,max:2.2,f});}",
        "function pop(x,y,txt,col){const P=G.P;let f=null;if(P&&Math.hypot(x-P.x,y-P.y)<140){const ex=G.pops.find(q=>q.f&&q.txt===txt&&q.life>.4);if(ex){G.pops.splice(G.pops.indexOf(ex),1);ex.life=ex.max;G.pops.push(ex);return;}f={dx:0,dy:-44};const fs=G.pops.filter(q=>q.f&&q.life>.35);for(let k=0;k<fs.length-2;k++)fs[k].life=.35;}G.pops.push({x,y,txt,col:col||'#fff',life:2.2,max:2.2,f});}")
h=rep(h," G.pops=G.pops.filter(p=>(p.life-=dt)>0);\n",
        " G.pops=G.pops.filter(p=>(p.life-=dt)>0);{let k=0;for(let j=G.pops.length-1;j>=0;j--){const p=G.pops[j];if(!p.f)continue;const tg=p.f.dy-k*26;p.oy=p.oy==null?tg:p.oy+(tg-p.oy)*Math.min(1,dt*12);k++;}}\n")
h=rep(h,"const px=fo?P.x+p.f.dx:p.x,py=fo?P.y:p.y,oy=(fo?p.f.dy:0)-rise;","const px=fo?P.x+p.f.dx:p.x,py=fo?P.y:p.y,oy=fo?(p.oy!=null?p.oy:p.f.dy):-rise;")

# ---------------- Bahamas sin filas de boyas ----------------
h=rep(h,"if(Zn.Z.theme==='open'){const xl=Zn.shore(camTop)+8,","if(Zn.Z.theme==='open'&&!Zn.circ){const xl=Zn.shore(camTop)+8,")

# ---------------- agua y textos de las pantallas ----------------
h=rep(h,"{name:'BAHAMAS',water:['#1569b5','#0f509a'],","{name:'BAHAMAS',water:['#3cc4dd','#33bad8'],")
h=rep(h,"La pantalla gira contigo. Si te metes en los bajíos de arena frenas, y cuidado","La pantalla gira contigo. Si te alejas mucho del camino frenas, y cuidado")
h=rep(h,"{name:'CARRERA ES TRENC',water:['#23c6de','#1198d0'],","{name:'CARRERA ES TRENC',water:['#4dd2e3','#44cae0'],")
h=rep(h,"Hay 4 pasos estrechos: busca el hueco o salta el banco de arena con la ola.","Hay 4 pasos estrechos entre la playa y las islas: no te comas la isla.")
h=rep(h,"hasta la playa de Sa Calobra antes","hasta Sa Calobra antes")
h=rep(h,"o=lerp(W/2,clamp(o,140,360),k);(sd<0?wl:wr).push(o);","o=lerp(W/2,clamp(o,140,(s<0||s>Lp-200)?200:360),k);(sd<0?wl:wr).push(o);")
open(H,'w').write(h)
print('ok')
