import shutil
H='costa-turbo.html'
shutil.copy(H,'costa-turbo.pre-v62.html')
h=open(H).read()
def rep(s,a,b,n=1):
    c=s.count(a)
    assert c==n,(c,a[:90])
    return s.replace(a,b)
h=rep(h,"const APP_VER=61","const APP_VER=62")

# ================= ES TRENC =================
# 3 pasos (3 islas grandes)
h=rep(h,"else{const n=4;for(let k=0;k<n;k++){const s=Math.round(Lp*(.17+k*.21)+(rr()-.5)*400);gaps.push({s,g:(rr()-.5)*120,w:118});}}",
        "else{const n=3;for(let k=0;k<n;k++){const s=Math.round(Lp*(.22+k*.28)+(rr()-.5)*300);gaps.push({s,g:(rr()-.5)*120,w:118});}}")
h=rep(h,"for(const q of gaps){const i=I(q.s);q.w=112+rr()*24;q.e=-wl[i]+q.w;q.g=-wl[i]+q.w/2+4;}C.gaps=gaps.map(q=>({i:I(q.s),lat:q.g,w:q.w}));",
        "for(const q of gaps){const i=I(q.s);q.w=118+rr()*22;q.e=-wl[i]+q.w;q.g=-wl[i]+q.w/2+4;q.bR=330+rr()*110;}C.gaps=gaps.map(q=>({i:I(q.s),lat:q.g,w:q.w,a:Math.ceil(q.bR*1.2/step),b:Math.ceil((q.bR*1.2+450)/step)}));")
# islas grandes de los pasos: nunca más cerca de la playa que el ancho del paso, aunque el camino curve
h=rep(h,"for(const q of gaps){const i=I(q.s),nx=Math.cos(hs[i]),ny=Math.sin(hs[i]),aR=(wr[i]+470-q.e)/2,bR=150+rr()*60,o={rad:aR,mid:0,noSpit:1,big:1,pass:1,rot:hs[i]};o.x=xs[i]+nx*(q.e+aR);o.y=ys[i]+ny*(q.e+aR);mkShape(o);o.R0=aR;o.el=bR/aR;o.maxR=aR*1.35;\n  let sp=shapePts(o),mn=1e9;for(const[px,py]of sp.pts){const lat=(px-xs[i])*nx+(py-ys[i])*ny;if(lat<mn)mn=lat;}const sh=q.e-mn;o.x+=nx*sh;o.y+=ny*sh;o.sp=shapePts(o);isl.push(o);}",
        "for(const q of gaps){const i=I(q.s),nx=Math.cos(hs[i]),ny=Math.sin(hs[i]),aR=(wr[i]+640-q.e)/2,bR=q.bR,o={rad:aR,mid:0,noSpit:1,big:1,pass:1,rot:hs[i]};o.x=xs[i]+nx*(q.e+aR);o.y=ys[i]+ny*(q.e+aR);mkShape(o);o.R0=aR;o.el=bR/aR;o.maxR=Math.max(aR,bR)*1.35;\n  for(let it=0;it<4;it++){const sp=shapePts(o);let need=-1e9;for(const[px,py]of sp.pts){let j=i,bd=1e18;for(let k=Math.max(0,i-90);k<=Math.min(N-1,i+90);k+=2){const d=(xs[k]-px)**2+(ys[k]-py)**2;if(d<bd){bd=d;j=k;}}const lat=(px-xs[j])*Math.cos(hs[j])+(py-ys[j])*Math.sin(hs[j]);need=Math.max(need,(-wl[j]+q.w)-lat);}if(Math.abs(need)<2)break;o.x+=nx*need;o.y+=ny*need;}o.sp=shapePts(o);isl.push(o);}")
# sin micro islas en Es Trenc
h=rep(h,"for(let s=-S0-300;s<Lp+PO+300;s+=(TR?70:40)+rr()*60)for(const sd of sides){","if(!TR)for(let s=-S0-300;s<Lp+PO+300;s+=(TR?70:40)+rr()*60)for(const sd of sides){")
h=rep(h,"const np=o.pass?12:","const np=o.pass?24:")
h=rep(h,"const nb=Math.min(o.huge?260:110,Math.round(area/150));","const nb=Math.min(o.huge||o.pass?260:110,Math.round(area/150));")
# puntas que salen desde tierra (Es Trenc) + bancos de arena que frenan (Bahamas)
NEW=r"""for(const m of mids){const i=I(m.s),o={x:xs[i]+Math.cos(hs[i])*m.lat,y:ys[i]+Math.sin(hs[i])*m.lat,rad:m.r,mid:1};mkShape(o);isl.push(o);}
 const heads=[],banks=[];
 if(TR){for(const f of[.08,.37,.64,.92]){let s=Lp*f,tr=0;while(tr++<10&&gaps.some(q=>Math.abs(q.s-s)<q.bR+450))s+=160;if(s>Lp-150)continue;const d=95+rr()*55,hl=140+rr()*70,sk=(rr()-.5)*.5,inn=[],out=[];
   for(let k=0;k<=14;k++){const t=-1+k/7,si=s+t*hl,i=I(si),tt=Math.max(0,1-Math.abs(t-sk*(1-Math.abs(t)))),pr=Math.pow(tt,.75)*(1+.08*Math.sin(k*2.1+s));inn.push(P(si,-wl[i]+d*pr-6));out.push(P(si,-wl[i]-90));}
   const pts=inn.concat(out.reverse());lands.push({pts,bb:bbOf(pts),fill:'#d9c79c',foam:true,halo:true});
   const i0=I(s);heads.push({s,d});C.gaps.push({i:i0,lat:(-wl[i0]+d+wr[i0])/2,w:wr[i0]+wl[i0]-d,a:Math.ceil(hl*1.1/step),b:Math.ceil((hl+420)/step)});
   for(let k=0;k<7;k++){const t=(rr()-.5)*1.2,si=s+t*hl,i=I(si),[x,y]=P(si,-wl[i]-40+rr()*d*.5*(1-Math.abs(t)));add({t:'cdeco',x,y,d:{t:rr()<.6?'pine':'grass',x,y,r:9+rr()*7,s:(rr()*1e6)|0}});}}}
 else{for(const f of[.14,.31,.47,.63,.8,.93]){let s=Lp*f,tr=0;while(tr++<10&&(mids.some(m=>Math.abs(m.s-s)<750)||nar.some(q=>Math.abs(q.s-s)<650)||(C.huge||[]).some(hi=>Math.abs(hi*step-S0-s)<650)))s+=180;if(s>Lp-500)continue;
   const sd=rr()<.5?-1:1,hl=150+rr()*90,cov=.4+rr()*.14,inn=[],out=[];
   for(let k=0;k<=12;k++){const t=-1+k/6,si=s+t*hl,i=I(si),e=sd<0?wl[i]:wr[i],eo=sd<0?wr[i]:wl[i],sh=Math.pow(Math.max(0,1-t*t),.6);inn.push(P(si,sd*(e-cov*(e+eo)*sh+7*Math.sin(k*1.9+s))));out.push(P(si,sd*(e+80)));}
   const pts=inn.concat(out.reverse());const i0=I(s),e0=sd<0?wl[i0]:wr[i0],eo0=sd<0?wr[i0]:wl[i0],tip=sd*(e0-cov*(e0+eo0));banks.push({pts,bb:bbOf(pts),s});C.gaps.push({i:i0,lat:(tip-sd*eo0)/2,w:(1-cov)*(e0+eo0),a:Math.ceil(hl*1.1/step),b:Math.ceil((hl+420)/step)});}}
 C.banks=banks;"""
h=rep(h,"for(const m of mids){const i=I(m.s),o={x:xs[i]+Math.cos(hs[i])*m.lat,y:ys[i]+Math.sin(hs[i])*m.lat,rad:m.r,mid:1};mkShape(o);isl.push(o);}",NEW)
h=rep(h,"const busy=s=>mids.some(m=>Math.abs(m.s-s)<500)||gaps.some(q=>Math.abs(q.s-s)<420);",
        "const busy=s=>mids.some(m=>Math.abs(m.s-s)<500)||gaps.some(q=>Math.abs(q.s-s)<420)||heads.some(q=>Math.abs(q.s-s)<380)||banks.some(q=>Math.abs(q.s-s)<380);")
h=rep(h,"if(gaps.some(q=>Math.abs(q.s-s)<500))continue;const i=I(s),lat=-wl[i]+15","if(gaps.some(q=>Math.abs(q.s-s)<500)||heads.some(q=>Math.abs(q.s-s)<450))continue;const i=I(s),lat=-wl[i]+15")
# agua profunda de Es Trenc casi igual que el tramo, sin bancos blancos
h=rep(h,"const bars=[];for(let s=-S0;s<Lp+PO;s+=","const bars=[];if(!TR)for(let s=-S0;s<Lp+PO;s+=")
h=rep(h,"ctx.fillStyle=TR?'#79e1e8':'#5ad4e3';","ctx.fillStyle=TR?'#52d3e3':'#5ad4e3';")
h=rep(h,"ctx.globalAlpha=TR?.38:.26;","ctx.globalAlpha=TR?.1:.26;")
h=rep(h,"ctx.strokeStyle=TR?'rgba(40,175,210,.2)':'rgba(30,150,200,.22)';","ctx.strokeStyle=TR?'rgba(40,175,210,.08)':'rgba(30,150,200,.22)';")
h=rep(h,"ctx.strokeStyle=TR?'rgba(70,200,225,.18)':'rgba(60,185,220,.2)';","ctx.strokeStyle=TR?'rgba(70,200,225,.06)':'rgba(60,185,220,.2)';")
# dibujar bancos de arena (Bahamas)
a=" ctx.restore();}\n"
i0=h.index("function drawShallows(");i1=h.index(a,i0)
h=h[:i1]+""" ctx.restore();
 if(C.banks)for(const B of C.banks){if(!vis(B.bb))continue;ctx.save();ctx.lineJoin='round';ctx.beginPath();B.pts.forEach(([x,y],k)=>k?ctx.lineTo(x,y):ctx.moveTo(x,y));ctx.closePath();
  ctx.strokeStyle='rgba(150,232,228,.45)';ctx.lineWidth=40;ctx.stroke();ctx.strokeStyle='rgba(200,243,234,.7)';ctx.lineWidth=16;ctx.stroke();ctx.fillStyle='#d6f3ea';ctx.fill();ctx.clip();
  ctx.strokeStyle='rgba(185,170,130,.28)';ctx.lineWidth=3;for(let k=0;k<B.pts.length/2-1;k+=2){const[ax,ay]=B.pts[k],[bx,by]=B.pts[B.pts.length-1-k];ctx.beginPath();ctx.moveTo(ax,ay);ctx.quadraticCurveTo((ax+bx)/2+9,(ay+by)/2-9,bx,by);ctx.stroke();}ctx.restore();}}
"""+h[i1+len(a):]
# el banco de arena frena
h=rep(h,"  if(c._offT>0)c._offT-=dt;\n","  if(C.banks&&C.banks.length&&c.air<=0){let on=false;for(const B of C.banks){if(c.x<B.bb[0]||c.x>B.bb[2]||c.y<B.bb[1]||c.y>B.bb[3])continue;if(polyIn(B.pts,c.x,c.y)){on=true;break;}}if(on){c.v*=1-1.15*dt;if(c.isP&&!G.demo&&!(c._sandT>0)){c._sandT=1.6;pop(c.x,c.y-40,'¡BANCO DE ARENA!','#ffb84d');}}}if(c._sandT>0)c._sandT-=dt;\n  if(c._offT>0)c._offT-=dt;\n")
# la IA respeta la longitud de cada paso / banco / punta
h=rep(h,"if(C.gaps)for(const q of C.gaps){if(q.i-c.cs<95&&q.i-c.cs>-26)","if(C.gaps)for(const q of C.gaps){if(q.i-c.cs<(q.b||95)&&q.i-c.cs>-(q.a||26))")
# textos
h=rep(h,"Si te alejas mucho del camino frenas, y cuidado con los cerdos nadando en Pig Beach.","Los bancos de arena te frenan, y cuidado con los cerdos nadando.")
h=rep(h,"Hay 4 pasos estrechos entre la playa y las islas: no te comas la isla.","Hay 3 pasos estrechos entre la playa y las islas grandes, y puntas de roca que salen de la costa.")
h=rep(h,"if(gaps.some(q=>Math.abs(q.s-(i*step-S0))<300))continue;","if(gaps.some(q=>Math.abs(q.s-(i*step-S0))<(q.bR||200)+120)||heads.some(q=>Math.abs(q.s-(i*step-S0))<260))continue;")
h=rep(h,"||gaps.some(q=>Math.abs(q.s-s)<420)||heads.some(","||gaps.some(q=>Math.abs(q.s-s)<(q.bR?q.bR+160:420))||heads.some(")
h=rep(h,"if(gaps.some(q=>Math.abs(q.s-s)<500)||heads.some(q=>Math.abs(q.s-s)<450))continue;","if(gaps.some(q=>Math.abs(q.s-s)<q.bR+200)||heads.some(q=>Math.abs(q.s-s)<450))continue;")
h=rep(h,"vg.push(T(Math.cos(a)*o.R0*nv*.76,Math.sin(a)*o.R0*o.el*nv*.76));","vg.push(T(Math.cos(a)*o.R0*nv*(o.vk||.76),Math.sin(a)*o.R0*o.el*nv*(o.vk||.76)));")
h=rep(h,"o={rad:aR,mid:0,noSpit:1,big:1,pass:1,rot:hs[i]};","o={rad:aR,mid:0,noSpit:1,big:1,pass:1,vk:.88,rot:hs[i]};")
open(H,'w').write(h)
print('ok')
