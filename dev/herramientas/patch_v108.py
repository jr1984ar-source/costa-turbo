import json
p='costa-turbo.html';s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
# mapa: el BAR JJ'S pasa a la costa izquierda a mitad del lago (lejos de la salida)
RM=json.load(open('/tmp/claude-0/-home-user/e02bf71e-076d-586d-89ee-84e1312586e6/scratchpad/costa_real/realmap5.json'))
i0=s.index("const RMAP={");i1=s.index("let RMD=null;",i0)
s=s[:i0]+"const RMAP={w:%d,h:%d,c:3,src:'%s'};const RCOR=%s;const RSPOTS=%s;const RZONE=%s;"%(RM['w'],RM['h'],RM['src'],json.dumps(RM['cor'],separators=(',',':')),json.dumps(RM['spots'],separators=(',',':')),json.dumps(RM['zones'],separators=(',',':')))+s[i1:]
# barcos de todo tipo: velero, lancha, yate, llaüt y neumática
DM="""function drawMoored(g,L,W,k,h,h2){const sh=f=>{g.save();g.translate(2,3);g.fillStyle='rgba(0,30,60,.25)';f();g.fill();g.restore();};
 const hull=(w,o)=>{w=w||W;o=o||0;g.beginPath();g.moveTo(o,-w/2);g.lineTo(L*.6,-w/2);g.quadraticCurveTo(L-o,-w*.3,L-o,0);g.quadraticCurveTo(L-o,w*.3,L*.6,w/2);g.lineTo(o,w/2);g.closePath();};
 if(k===0){sh(()=>hull());g.fillStyle=['#f7f8fa','#1d3557','#f7f8fa','#e9e4d6'][(h*4)|0];hull();g.fill();g.strokeStyle='#9aa6b2';g.lineWidth=.9;g.stroke();g.fillStyle='#d8c29a';hull(W*.74,3);g.fill();
  g.fillStyle='#f4f5f7';g.beginPath();g.roundRect(L*.25,-W*.22,L*.22,W*.44,3);g.fill();g.strokeStyle='#8f969e';g.lineWidth=1.3;g.beginPath();g.moveTo(L*.12,0);g.lineTo(L*.58,0);g.stroke();
  g.fillStyle=['#1f4fa8','#c03a2b','#2f8f6f','#24262c'][(h2*4)|0];g.fillRect(L*.16,-1.8,L*.38,3.6);g.fillStyle='#3b4250';g.beginPath();g.arc(L*.58,0,2,0,TAU);g.fill();}
 else if(k===1){sh(()=>hull());g.fillStyle=['#c8202b','#1d3557','#f7f8fa','#2a9d8f','#ffd21a'][(h*5)|0];hull();g.fill();g.strokeStyle='rgba(0,0,0,.25)';g.lineWidth=.9;g.stroke();g.fillStyle='#f4f1ea';g.beginPath();g.roundRect(L*.08,-W*.32,L*.42,W*.64,3);g.fill();
  g.fillStyle='rgba(30,50,70,.8)';g.beginPath();g.moveTo(L*.52,-W*.36);g.quadraticCurveTo(L*.6,0,L*.52,W*.36);g.lineTo(L*.48,W*.3);g.quadraticCurveTo(L*.55,0,L*.48,-W*.3);g.closePath();g.fill();g.fillStyle='#d7dde3';g.fillRect(L*.15,-W*.2,L*.1,W*.4);g.fillRect(L*.3,-W*.2,L*.1,W*.4);}
 else if(k===2){sh(()=>hull());g.fillStyle='#f7f8fa';hull();g.fill();g.strokeStyle='#bcc6d1';g.lineWidth=.9;g.stroke();g.fillStyle='#e2e6ea';g.fillRect(-3,-W*.42,4,W*.84);
  g.fillStyle='#ffffff';g.beginPath();g.roundRect(L*.14,-W*.36,L*.5,W*.72,4);g.fill();g.strokeStyle='#c9d1da';g.stroke();g.fillStyle='#1e2a38';g.fillRect(L*.5,-W*.32,L*.06,W*.64);g.fillRect(L*.18,-W*.4,L*.3,1.6);g.fillRect(L*.18,W*.4-1.6,L*.3,1.6);
  g.fillStyle='#eef1f4';g.beginPath();g.roundRect(L*.22,-W*.22,L*.24,W*.44,3);g.fill();g.fillStyle='#2b3440';g.fillRect(L*.36,-W*.16,L*.05,W*.32);}
 else if(k===3){const band=['#2f8f4f','#1f4fa8','#c03a2b','#e0b13a'][(h*4)|0],lh=()=>{g.beginPath();g.moveTo(0,0);g.quadraticCurveTo(L*.08,-W/2,L*.4,-W/2);g.quadraticCurveTo(L*.9,-W/2,L,0);g.quadraticCurveTo(L*.9,W/2,L*.4,W/2);g.quadraticCurveTo(L*.08,W/2,0,0);g.closePath();};
  sh(lh);g.fillStyle='#f4f1ea';lh();g.fill();g.strokeStyle=band;g.lineWidth=2.2;g.stroke();g.fillStyle='#b48a5a';g.save();g.scale(1,.72);lh();g.fill();g.restore();g.strokeStyle='rgba(90,60,30,.4)';g.lineWidth=.6;for(let q=L*.15;q<L*.9;q+=4){g.beginPath();g.moveTo(q,-W*.3);g.lineTo(q,W*.3);g.stroke();}
  g.fillStyle='#ffffff';g.fillRect(L*.3,-W*.22,L*.18,W*.44);g.fillStyle=band;g.fillRect(L*.3,-W*.22,L*.18,2);}
 else{const rb=()=>{g.beginPath();g.roundRect(0,-W/2,L*.92,W,W/2);};sh(rb);g.fillStyle='#5b636e';rb();g.fill();g.fillStyle='#2a2e35';g.beginPath();g.roundRect(W*.3,-W*.28,L*.92-W*.6,W*.56,W*.25);g.fill();
  g.fillStyle='#d9dde2';g.fillRect(L*.4,-W*.16,L*.12,W*.32);g.fillStyle='#e3202b';g.fillRect(L*.75,-W*.5,3,W);}}
"""
rep("function drawGirl(g,x,y,hair,bik,wave,ph){",DM+"function drawGirl(g,x,y,hair,bik,wave,ph){")
i=s.index("const h=hash2(Math.round(x),Math.round(y),71),h2=hash2(Math.round(y),Math.round(x),13),L=36+h*14,Wd=11+h2*4,sail=h2>.78;")
j=s.index(" for(let y=Math.ceil(y0/34)*34;y<y1;y+=34){const xb=rmCor(y);",i)
s=s[:i]+"""const h=hash2(Math.round(x),Math.round(y),71),h2=hash2(Math.round(y),Math.round(x),13),k=h2<.25?0:h2<.5?1:h2<.7?2:h2<.85?3:4,L=k===2?44+h*7:k===4?30+h*6:36+h*12,Wd=k===4?11+h*2:11+h2*4;
   g.save();g.translate(x+b.ca*(b.d-1),y+b.sa*(b.d-1));g.rotate(Math.atan2(-b.sa,-b.ca));drawMoored(g,L,Wd,k,h,hash2(Math.round(x),7,Math.round(y)));g.restore();}}
"""+s[j:]
# barcos fondeados por el lago y lancha de policía patrullando
rep(" // olas en todas direcciones",""" // barcos fondeados de todo tipo cerca de la costa
 {const busy=(x,y)=>O.some(o=>(o.t==='pgbar'||o.t==='pggas')&&Math.hypot((o.bx||o.x)-x,(o.by||o.y)-y)<320);
  const coastNear=(x,y,d)=>{for(let a=0;a<8;a++)if(rmLand(x+Math.cos(a*.785)*d,y+Math.sin(a*.785)*d))return true;return false;};
  const KB=[['pgboat',0,7,55],['pgboat',1,6,45],['pgboat',2,5,70],['pgboat',3,6,45],['pgboat',4,4,40],['sail',-1,4,45],['barca',-1,5,30],['yacht',-1,3,90]];
  for(const[t,k,n,m]of KB){for(let c=0,tr=0;c<n&&tr<8000;tr++){const x=rx(),y=ry();if(!free(x,y,m)||inLane(x,y,m+60)||!coastNear(x,y,m+240)||coastNear(x,y,m+15)||busy(x,y))continue;
    const o={t,x,y,rot:r()*TAU,ph:r()*6};if(t==='pgboat'){o.k=k;o.L=k===2?90+r()*30:k===4?40+r()*12:55+r()*25;o.W=o.L*(k===4?.36:k===2?.3:.28);o.h1=r();o.h2=r();}if(t==='barca'){o.moor=1;o.c=['#2f8f4f','#1f4fa8','#c03a2b','#e0b13a'][c%4];o.rot=0;}O.push(o);c++;}}}
 for(let n=0,t=0;n<1&&t<3000;t++){const x=rx(),y=ry();if(!free(x,y,200)||inLane(x,y,120))continue;M.push({t:'pgpol',x,y,h:r()*TAU,vx:0,vy:0,flash:0});n++;}
 // olas en todas direcciones""")
rep("  else if(o.t==='npcjet'){","""  else if(o.t==='pgpol'){o.tt=(o.tt||0)-dt;if(o.tt<=0){o.tt=3+Math.random()*4;o.th=o.h+(Math.random()-.5)*1.6;}const ax=o.x+Math.sin(o.h)*240,ay=o.y-Math.cos(o.h)*240;if(rmLand(ax,ay)||ax<150||ax>RMW-150||ay<RM_TOP+600||ay>RM_BOT-300)o.th=o.h+2.2;
   let d=(o.th==null?o.h:o.th)-o.h;while(d>Math.PI)d-=TAU;while(d<-Math.PI)d+=TAU;o.h+=clamp(d,-1*dt,1*dt);const nx=o.x+Math.sin(o.h)*125*dt,ny=o.y-Math.cos(o.h)*125*dt;if(!rmLand(nx,ny)){o.x=nx;o.y=ny;}else o.th=o.h+Math.PI;o.fl=(o.fl||0)+dt;
   if(!G.demo){o.cd=(o.cd||0)-dt;if(o.cd<=0&&Math.hypot(P.x-o.x,P.y-o.y)<180&&P.v>P.st.maxV*.85){o.cd=15;pop(o.x,o.y-70,'¡MÁS DESPACIO!','#5b8cff');Snd.warn();}}}
  else if(o.t==='npcjet'){""")
rep("case 'pgpod':{","""case 'pgboat':{ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.rot);ctx.fillStyle='#ff8c1a';ctx.beginPath();ctx.arc(o.L/2+10,0,2.6,0,TAU);ctx.fill();ctx.translate(-o.L/2,0);drawMoored(ctx,o.L,o.W,o.k,o.h1,o.h2);ctx.restore();}return;
 case 'pgpol':{const pr=o._d||(o._d={t:'patrol'});pr.x=o.x;pr.y=o.y;pr.rot=o.h;pr.flash=o.fl||0;drawObj(pr);}return;
 case 'pgpod':{""")
rep("case 'cboat':{const dx=x-o.x,dy=y-o.y,ca=Math.cos(o.r),sa=Math.sin(o.r),lx=dx*ca+dy*sa,ly=-dx*sa+dy*ca;return Math.abs(lx)<o.bw/2+rad*.6&&Math.abs(ly)<o.bl/2+rad*.6;}}return false;}",
    "case 'cboat':{const dx=x-o.x,dy=y-o.y,ca=Math.cos(o.r),sa=Math.sin(o.r),lx=dx*ca+dy*sa,ly=-dx*sa+dy*ca;return Math.abs(lx)<o.bw/2+rad*.6&&Math.abs(ly)<o.bl/2+rad*.6;}\n case 'pgboat':{const dx=x-o.x,dy=y-o.y,ca=Math.cos(o.rot),sa=Math.sin(o.rot),lx=dx*ca+dy*sa,ly=-dx*sa+dy*ca;return Math.abs(lx)<o.L/2+rad*.6&&Math.abs(ly)<o.W/2+rad*.6;}\n case 'pgpol':{const dx=x-o.x,dy=y-o.y,ca=Math.cos(o.h),sa=Math.sin(o.h),lx=dx*ca+dy*sa,ly=-dx*sa+dy*ca;return Math.abs(lx)<16+rad*.6&&Math.abs(ly)<50+rad*.6;}}return false;}")
rep("crash(c,{skiboat:'¡LANCHA!',","crash(c,{skiboat:'¡LANCHA!',pgpol:'¡POLICÍA!',")
rep("barca:'¡BARCA!',pier:'¡ESPIGÓN!'}","barca:'¡BARCA!',pgboat:'¡BARCO!',pier:'¡ESPIGÓN!'}")
rep("g.fillStyle=o.t==='piripg'?'#ffd21a':o.t==='skiboat'?'#ffffff':'#ff4f8b';","g.fillStyle=o.t==='piripg'?'#ffd21a':o.t==='pgpol'?'#5b8cff':o.t==='skiboat'?'#ffffff':'#ff4f8b';")
# sonido: válvulas de descarga +3 dB (todas las STAGE) y escape -5 dB (petardeo y ruido del escape deportivo)
rep("if(st===3){this.bovA(.6+.4*sp);return;}","if(st===3){this.bovA((.6+.4*sp)*1.413);return;}")
rep("const t0=this.ctx.currentTime+.01,k=[0,.85,1,1.1][st]*(.55+.45*sp)","const t0=this.ctx.currentTime+.01,k=[0,.85,1,1.1][st]*(.55+.45*sp)*1.413")
rep("const v=(st>=3?.95:.65)*(.6+Math.random()*.4)*(.6+clamp(level,0,1)*.4);","const v=(st>=3?.95:.65)*(.6+Math.random()*.4)*(.6+clamp(level,0,1)*.4)*.562;")
rep("e.sg.gain.setTargetAtTime(idle?0:[0,.03,.045,.06][x]*(.45+rpm*.55),t,.08);","e.sg.gain.setTargetAtTime(idle?0:[0,.03,.045,.06][x]*(.45+rpm*.55)*.562,t,.08);")
rep("e.rg.gain.setTargetAtTime(idle?0:[0,0,.009,.017][x]*r1*(thr?1:.5),t,.08);","e.rg.gain.setTargetAtTime(idle?0:[0,0,.009,.017][x]*r1*(thr?1:.5)*.562,t,.08);")
rep("const APP_VER=107;","const APP_VER=108;")
open(p,'w').write(s);print('ok',len(s))
