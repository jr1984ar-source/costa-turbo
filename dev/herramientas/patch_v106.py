p='costa-turbo.html';s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
# destinos, motos que retan y marca de meta
rep("trail:[]});}}\nconst PG_GEAR=","""trail:[]});}
 // destinos para retos y paseos
 const wn=(x,y)=>{for(let rr=0;rr<520;rr+=20)for(let a=0;a<24;a++){const px=x+Math.cos(a/24*TAU)*rr,py=y+Math.sin(a/24*TAU)*rr;if(free(px,py,45))return[px,py];}return[x,y];};
 const D=[],S2=RSPOTS||{};
 if(S2.faro){const[a,b]=wn(S2.faro[0]+34,S2.faro[1]+60);D.push({n:'EL FARO',x:a,y:b});}
 for(const o of O){if(o.t==='pgbar')D.push({n:o.k==='jj'?"BAR JJ'S":'BAR ROXY',x:o.bx,y:o.by});if(o.t==='pggas')D.push({n:o.x<RMW/2?'PUERTO PORTALS':'PUERTO DEL ESTE',x:o.x,y:o.y});}
 if(S2.pigb){const[a,b]=wn(S2.pigb[0],S2.pigb[1]+S2.pigb[2]+70);D.push({n:'PIG BEACH',x:a,y:b});}
 if(S2.girls&&S2.girls.length){const g=S2.girls[0];const[a,b]=wn(g[0],g[1]+100);D.push({n:'LA ISLITA',x:a,y:b});}
 if(zone.lane)D.push({n:'LA RECTA',x:zone.lane.x,y:zone.lane.y0+80});
 zone.pgDest=D;G.pgRace=null;G.pgMis=null;
 {let k=0;for(const o of M)if(o.t==='npcjet'&&k<4){o.ch=1;k++;}}
 O.push({t:'pgtarget',x:0,y:0,ry:1e9});}
// ---- retos en el lago: camino por el agua (A* sobre una rejilla) ----
function pgGrid(){if(G.zone._pgG)return G.zone._pgG;const C=60,w=Math.ceil(RMW/C),h=Math.ceil((RM_BOT-RM_TOP)/C),ok=new Uint8Array(w*h);
 for(let j=0;j<h;j++)for(let i=0;i<w;i++){const x=i*C+C/2,y=RM_TOP+j*C+C/2;let f=rmLand(x,y)?0:1;for(let a=0;a<8&&f;a++)if(rmLand(x+Math.cos(a*.785)*42,y+Math.sin(a*.785)*42))f=0;ok[j*w+i]=f;}
 return G.zone._pgG={C,w,h,ok};}
function pgPath(x0,y0,x1,y1){const{C,w,h,ok}=pgGrid(),id=(x,y)=>clamp(Math.floor((y-RM_TOP)/C),0,h-1)*w+clamp(Math.floor(x/C),0,w-1);
 const near=k=>{if(ok[k])return k;const i0=k%w,j0=(k/w)|0;for(let r=1;r<8;r++)for(let dj=-r;dj<=r;dj++)for(let di=-r;di<=r;di++){const i=i0+di,j=j0+dj;if(i>=0&&j>=0&&i<w&&j<h&&ok[j*w+i])return j*w+i;}return k;};
 const s0=near(id(x0,y0)),t=near(id(x1,y1)),N=w*h,gS=new Float32Array(N).fill(1e9),came=new Int32Array(N).fill(-1),cl=new Uint8Array(N),hp=[];
 const push=(k,f)=>{hp.push([f,k]);let i=hp.length-1;while(i>0){const q=(i-1)>>1;if(hp[q][0]<=hp[i][0])break;[hp[q],hp[i]]=[hp[i],hp[q]];i=q;}};
 const pop=()=>{const top=hp[0],last=hp.pop();if(hp.length){hp[0]=last;let i=0;for(;;){const l=2*i+1,r=l+1;let m=i;if(l<hp.length&&hp[l][0]<hp[m][0])m=l;if(r<hp.length&&hp[r][0]<hp[m][0])m=r;if(m===i)break;[hp[m],hp[i]]=[hp[i],hp[m]];i=m;}}return top;};
 const ti=t%w,tj=(t/w)|0,hh=k=>Math.hypot(k%w-ti,((k/w)|0)-tj);gS[s0]=0;push(s0,hh(s0));
 while(hp.length){const k=pop()[1];if(cl[k])continue;cl[k]=1;if(k===t)break;const i=k%w,j=(k/w)|0;
  for(let dj=-1;dj<=1;dj++)for(let di=-1;di<=1;di++){if(!di&&!dj)continue;const ni=i+di,nj=j+dj;if(ni<0||nj<0||ni>=w||nj>=h)continue;const nk=nj*w+ni;if(!ok[nk]||cl[nk])continue;if(di&&dj&&(!ok[j*w+ni]||!ok[nj*w+i]))continue;const ng=gS[k]+(di&&dj?1.414:1);if(ng<gS[nk]){gS[nk]=ng;came[nk]=k;push(nk,ng+hh(nk));}}}
 if(t!==s0&&came[t]<0)return null;const pts=[];for(let k=t;k>=0;k=came[k]){pts.push([(k%w)*C+C/2,RM_TOP+((k/w)|0)*C+C/2]);if(k===s0)break;}pts.reverse();
 const los=(a,b)=>{const n=Math.ceil(Math.hypot(b[0]-a[0],b[1]-a[1])/20);for(let q=1;q<n;q++){const x=a[0]+(b[0]-a[0])*q/n,y=a[1]+(b[1]-a[1])*q/n;if(rmLand(x,y)||rmLand(x+32,y)||rmLand(x-32,y)||rmLand(x,y+32)||rmLand(x,y-32))return false;}return true;};
 const out=[pts[0]];let a=0;while(a<pts.length-1){let b=pts.length-1;while(b>a+1&&!los(pts[a],pts[b]))b--;out.push(pts[b]);a=b;}out.push([x1,y1]);return out;}
function pgRivalMove(o,dt){const R=G.pgRace;if(!R||R.rv!==o||R.st!=='run'){o.v=0;return;}const wp=R.path[Math.min(R.i,R.path.length-1)],dx=wp[0]-o.x,dy=wp[1]-o.y,d=Math.hypot(dx,dy);if(d<80&&R.i<R.path.length-1)R.i++;
 let dh=Math.atan2(dx,-dy)-o.h;while(dh>Math.PI)dh-=TAU;while(dh<-Math.PI)dh+=TAU;o.h+=clamp(dh,-2.4*dt,2.4*dt);const tv=R.sp*(Math.abs(dh)>.9?.5:1);o.v+=(tv-o.v)*Math.min(1,1.1*dt);
 const nx=o.x+Math.sin(o.h)*o.v*dt,ny=o.y-Math.cos(o.h)*o.v*dt;if(!rmLand(nx,ny)){o.x=nx;o.y=ny;}else o.v*=.5;
 o.tacc=(o.tacc||0)+o.v*dt;if(o.tacc>10){o.tacc=0;o.trail.unshift({x:o.x-Math.sin(o.h)*24,y:o.y+Math.cos(o.h)*24,h:o.h});if(o.trail.length>16)o.trail.pop();}}
function pgRaceEnd(win,cancel){const R=G.pgRace;if(!R)return;const o=R.rv;o.race=0;o.cd=cancel?25:40;o.v=o.v0||150;G.pgRace=null;G.pgMis=null;if(cancel)return;
 if(win){G.money+=R.prize;G.score+=R.prize;saveWallet();Snd.cash();buzz(80);msg('¡GANAS EL RETO!','+'+pts(R.prize)+' PESETAS','var(--lime)');}else{Snd.fail();msg('¡TE HA GANADO!','Búscale otra vez y repite','var(--red)');}}
const PG_GEAR=""")
# lógica del reto (oferta, cuenta atrás, carrera y meta)
rep("""msg(o.t==='pggas'?'GASOLINERA':o.k==='jj'?"BAR JJ'S":'BAR ROXY','Frena con ATRÁS dentro del círculo','var(--gold)');}}""",
"""msg(o.t==='pggas'?'GASOLINERA':o.k==='jj'?"BAR JJ'S":'BAR ROXY','Frena con ATRÁS dentro del círculo','var(--gold)');}}
 {const R=G.pgRace;
  if(!R&&!G.pgMis&&!G.demo){for(const o of Zn.movers){if(o.t!=='npcjet'||!o.ch||o.cd>0)continue;if(Math.hypot(P.x-o.x,P.y-o.y)<180){const opts=(Zn.pgDest||[]).filter(q=>{const dd=Math.hypot(q.x-o.x,q.y-o.y);return dd>2500&&dd<9000;});if(!opts.length){o.cd=30;continue;}const q=opts[(Math.random()*opts.length)|0];G.pgRace={rv:o,d:q,st:'offer',t:10};o.v0=o.v0||o.v;o.race=1;o.v=0;msg('¡RETO!','Carrera hasta '+q.n+' · frena a su lado','var(--gold)');Snd.warn();break;}}}
  else if(R&&R.st==='offer'){R.t-=dt;const o=R.rv,d=Math.hypot(P.x-o.x,P.y-o.y);
   if(d<95&&P.v<P.st.maxV*.4){const path=pgPath(o.x,o.y,R.d.x,R.d.y);if(!path)pgRaceEnd(false,true);else{R.path=path;R.i=0;let L2=0;for(let k=1;k<path.length;k++)L2+=Math.hypot(path[k][0]-path[k-1][0],path[k][1]-path[k-1][1]);R.prize=300+Math.round(L2/2000)*100;R.st='count';R.t=3.2;R.last=4;G.pgMis={x:R.d.x,y:R.d.y,n:R.d.n,kind:'race'};}}
   else if(R.t<=0||d>450)pgRaceEnd(false,true);}
  else if(R&&R.st==='count'){R.t-=dt;P.v=0;const n=Math.ceil(R.t);if(n!==R.last&&n>0){R.last=n;msg(String(n),'Carrera hasta '+R.d.n+' · premio '+pts(R.prize)+' pesetas','var(--gold)');Snd.click();}if(R.t<=0){R.st='run';R.sp=P.st.maxV*.84;msg('¡YA!','Gana el primero que llegue a '+R.d.n,'var(--lime)');Snd.boost();}}
  else if(R&&R.st==='run'){const o=R.rv;if(Math.hypot(P.x-R.d.x,P.y-R.d.y)<130)pgRaceEnd(true);else if(R.i>=R.path.length-1&&Math.hypot(o.x-R.d.x,o.y-R.d.y)<100)pgRaceEnd(false);}}""")
rep("else if(o.t==='npcjet'){o.tt-=dt;","else if(o.t==='npcjet'){if(o.cd>0)o.cd-=dt;if(o.race){pgRivalMove(o,dt);continue;}o.tt-=dt;")
# dibujo: bandera de reto, meta y flecha
rep("else{const sp=SP.jet[o.id]||SP.jet[MOTOS[0].id];ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);ctx.drawImage(sp.c,-16,-34,32,68);ctx.restore();}}return;",
"""else{const sp=SP.jet[o.id]||SP.jet[MOTOS[0].id];ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);ctx.drawImage(sp.c,-16,-34,32,68);ctx.restore();
   if(o.ch&&!(o.cd>0)){ctx.save();ctx.translate(o.x,o.y);ctx.rotate(G.camA||0);ctx.strokeStyle='#2a2a2a';ctx.lineWidth=1.8;ctx.beginPath();ctx.moveTo(12,-4);ctx.lineTo(12,-36);ctx.stroke();for(let a=0;a<3;a++)for(let b=0;b<4;b++){ctx.fillStyle=(a+b)%2?'#111':'#fff';ctx.fillRect(12+b*4,-36+a*4+Math.sin(G.t*6+b)*1.2,4,4);}
    const R=G.pgRace,P=G.P;if((!R||R.rv!==o)&&P&&Math.hypot(P.x-o.x,P.y-o.y)<650)label(0,-56,'¡RETO!','CARRERA');ctx.restore();}}}return;
 case 'pgtarget':{const M2=G.pgMis;if(!M2)return;const p=1+Math.sin(G.t*4)*.06,col=M2.kind==='race'?'#ffffff':'#ff8fc4';ctx.save();ctx.translate(M2.x,M2.y);ctx.fillStyle=M2.kind==='race'?'rgba(255,255,255,.12)':'rgba(255,143,196,.14)';ctx.beginPath();ctx.arc(0,0,112*p,0,TAU);ctx.fill();ctx.setLineDash([12,9]);ctx.lineDashOffset=-G.t*30;ctx.strokeStyle=col;ctx.lineWidth=4;ctx.beginPath();ctx.arc(0,0,110*p,0,TAU);ctx.stroke();ctx.setLineDash([]);
  for(let k=0;k<8;k++){const a=k/8*TAU,x=Math.cos(a)*110*p,y=Math.sin(a)*110*p;for(let q=0;q<4;q++){ctx.fillStyle=q%3?'#111':'#fff';ctx.fillRect(x-4+(q%2)*4,y-4+((q/2)|0)*4,4,4);}}
  ctx.rotate(G.camA||0);label(0,-138,M2.kind==='race'?'META':'DESTINO',M2.n);ctx.restore();
  const P=G.P,dx=M2.x-P.x,dy=M2.y-P.y,d=Math.hypot(dx,dy);if(d>260){const a=Math.atan2(dy,dx);ctx.save();ctx.translate(P.x+Math.cos(a)*80,P.y+Math.sin(a)*80);ctx.rotate(a);ctx.fillStyle=M2.kind==='race'?'#ffe14d':'#ff8fc4';ctx.strokeStyle='rgba(0,0,0,.5)';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(20,0);ctx.lineTo(-9,-13);ctx.lineTo(-3,0);ctx.lineTo(-9,13);ctx.closePath();ctx.stroke();ctx.fill();ctx.restore();}}return;""")
rep("zone.big=zone.objs.filter(o=>o.t==='island'||o.t==='pass'||o.t==='nozone'||o.t==='pgbar'||o.t==='pggas');","zone.big=zone.objs.filter(o=>o.t==='island'||o.t==='pass'||o.t==='nozone'||o.t==='pgbar'||o.t==='pggas'||o.t==='pgtarget');")
rep("if(o.t!=='island'&&o.t!=='pass'&&o.t!=='nozone'&&o.t!=='pgbar'&&o.t!=='pggas')drawObj(o);","if(o.t!=='island'&&o.t!=='pass'&&o.t!=='nozone'&&o.t!=='pgbar'&&o.t!=='pggas'&&o.t!=='pgtarget')drawObj(o);")
rep("if(o.t==='bgirl'||o.t==='bpalm'||o.t==='faro'||o.t==='pgbar'||o.t==='pggas'||o.t==='pglabel'||o.t==='turtle'||o.t==='pig')continue;","if(o.t==='bgirl'||o.t==='bpalm'||o.t==='faro'||o.t==='pgbar'||o.t==='pggas'||o.t==='pglabel'||o.t==='turtle'||o.t==='pig'||o.t==='pgtarget')continue;")
# minimapa: meta o destino (en el borde si está lejos)
rep("g.translate(MW/2,MH*.62);g.rotate(P.h);","if(G.pgMis){let x=tx(G.pgMis.x),y=ty(G.pgMis.y);const out=x<5||x>MW-5||y<5||y>MH-5;x=clamp(x,6,MW-6);y=clamp(y,6,MH-6);g.fillStyle=G.pgMis.kind==='race'?'#ffe14d':'#ff8fc4';g.beginPath();g.arc(x,y,out?4:5.5,0,TAU);g.fill();g.strokeStyle='#0a1630';g.lineWidth=1.4;g.stroke();}\n g.translate(MW/2,MH*.62);g.rotate(P.h);")
rep(" if(!G.demo)for(const o of Zn.big){if(o.t!=='pgbar'&&o.t!=='pggas')continue;"," if(G._stopCool>0)G._stopCool-=dt;\n if(!G.demo&&!G.pgRace&&!(G._stopCool>0))for(const o of Zn.big){if(o.t!=='pgbar'&&o.t!=='pggas')continue;")
rep("function pgRaceEnd(win,cancel){const R=G.pgRace;if(!R)return;","function pgRaceEnd(win,cancel){const R=G.pgRace;if(!R)return;G._stopCool=2.5;")
rep("const APP_VER=105;","const APP_VER=106;")
open(p,'w').write(s);print('ok',len(s))
