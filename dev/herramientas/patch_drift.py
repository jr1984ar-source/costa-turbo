p='costa-turbo.html';s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,a[:100]
    s=s.replace(a,b)
# CSS: replace round turbo with pills
rep(""".tur{--s:clamp(64px,20vw,80px);width:var(--s);height:var(--s);align-self:flex-start;font-size:13px;background:radial-gradient(circle at 50% 30%,#7fe8ff,#18b6e6 60%,#0a7fb0);box-shadow:0 8px 18px rgba(51,214,255,.4),inset 0 2px 0 rgba(255,255,255,.35)}
.tur .ring{position:absolute;inset:-6px;border-radius:50%;background:conic-gradient(#fff calc(var(--p,0)*1%),rgba(255,255,255,.16) 0);-webkit-mask:radial-gradient(circle,transparent 61%,#000 62%);mask:radial-gradient(circle,transparent 61%,#000 62%)}
.tur.empty{filter:saturate(.2) brightness(.75)}""",
""".smalls{flex:1;min-width:0;max-width:96px;display:flex;flex-direction:column;gap:6px}
.pill{position:relative;height:38px;width:100%;border:0;padding:0 6px;border-radius:13px;font-family:var(--cond);font-weight:800;font-size:13px;letter-spacing:.06em;color:#fff;touch-action:none;display:flex;align-items:center;justify-content:center;gap:4px;transition:transform .05s;box-shadow:inset 0 1px 0 rgba(255,255,255,.35),0 5px 12px rgba(0,0,0,.3)}
.pill svg{width:15px;height:15px;flex:none}
.pill.on{transform:scale(.94);filter:brightness(1.15)}
.pill.tur{background:linear-gradient(#6fe7ff,#0f9fd4)}
.pill.tur.empty{filter:saturate(.2) brightness(.75)}
.pill.drf{background:linear-gradient(#ff7ab5,#d81b74)}
.pill.rev{background:linear-gradient(#66718a,#2c3446)}
.pill .badge{top:-8px;right:-7px;width:22px;height:22px;font-size:12px}
.pbar{position:absolute;left:8px;bottom:4px;height:3px;border-radius:2px;width:calc((100% - 16px)*var(--p,0)/100);background:#fff}""")
rep(""" .tur{--s:clamp(60px,22vh,80px)}""","""""")
rep("""#padR{grid-area:R;padding-right:max(14px,env(safe-area-inset-right,0px));padding-left:6px;justify-content:flex-end}""",
"""#padR{grid-area:R;padding-right:max(14px,env(safe-area-inset-right,0px));padding-left:6px;justify-content:flex-end;gap:10px}""")
# HTML pad
rep("""    <button class="ab tur" id="bTurbo" aria-label="Turbo"><span class="ring" id="turRing"></span>TURBO<span class="badge" id="turN">2</span></button>""",
"""    <div class="smalls">
      <button class="pill tur" id="bTurbo" aria-label="Turbo">TURBO<span class="badge" id="turN">2</span><span class="pbar" id="turRing"></span></button>
      <button class="pill drf" id="bDrift" aria-label="Derrape"><svg viewBox="0 0 16 16"><path d="M3 13c0-5 4-8 9-8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/><path d="M10 2l3.5 3L10 8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>DERRAPE</button>
      <button class="pill rev" id="bRev" aria-label="Freno y marcha atrás"><svg viewBox="0 0 16 16"><path d="M8 13V3M4 7l4-4 4 4" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" transform="rotate(180 8 8)"/></svg>ATRÁS</button>
    </div>""")
rep("""<p class="hint">Izquierda: girar · Derecha: acelerar y turbo</p>""","""<p class="hint">Izquierda: girar · Derecha: acelerar, turbo, derrape y atrás</p>""")
# craft fields
rep("""inv:0,trail:[],trailAcc:0,fin:0,""","""inv:0,va:0,driftT:0,driftDir:0,trail:[],trailAcc:0,fin:0,""")
# physics
rep("""  if(c.air<=0){c.h+=ctl.turn*st.turn*dt*(.5+.5*clamp(c.v/st.maxV,0,1));if(!ctl.turn)c.h*=1-2.4*dt;c.h=clamp(c.h,-1.05,1.05);}
  else if(ctl.turn){c.trick+=dt;c.spin+=ctl.turn*dt*TAU/c.airT*.95;}
  if(ctl.thr){const a=st.acc*(c.boostT>0?1.9:1)*(1.15-Math.min(1,c.v/maxV)*.75);c.v=Math.min(Math.max(c.v,0)+a*dt,Math.max(maxV,c.v-120*dt));if(c.v>maxV)c.v=Math.max(maxV,c.v-160*dt);}
  else c.v=Math.max(0,c.v-(55+c.v*.9)*dt);}
 c.x+=Math.sin(c.h)*c.v*dt;c.y-=Math.cos(c.h)*c.v*dt;""",
"""  const drifting=ctl.drift&&c.air<=0&&c.v>90;
  if(c.air<=0){
   if(drifting){if(ctl.turn)c.driftDir=ctl.turn;c.driftT+=dt;if(c.driftDir){c.h+=c.driftDir*st.turn*1.9*dt;c.v*=1-.1*dt;}else c.v*=1-1.3*dt;}
   else{c.h+=ctl.turn*st.turn*dt*(.5+.5*clamp(Math.abs(c.v)/st.maxV,0,1));if(!ctl.turn)c.h*=1-2.4*dt;}
   const lim=drifting?1.45:1.05;if(Math.abs(c.h)>lim)c.h=Math.sign(c.h)*Math.max(lim,Math.abs(c.h)-2.2*dt);}
  else if(ctl.turn){c.trick+=dt;c.spin+=ctl.turn*dt*TAU/c.airT*.95;}
  const thr=ctl.thr||(drifting&&c.driftDir);
  if(ctl.rev){if(c.v>0)c.v=Math.max(0,c.v-(260+c.v*1.3)*dt);else c.v=Math.max(-95,c.v-130*dt);}
  else if(thr){if(c.v<0)c.v=Math.min(0,c.v+320*dt);else{const a=st.acc*(c.boostT>0?1.9:1)*(1.15-Math.min(1,c.v/maxV)*.75);c.v=Math.min(c.v+a*dt,Math.max(maxV,c.v-120*dt));if(c.v>maxV)c.v=Math.max(maxV,c.v-160*dt);}}
  else c.v=c.v>0?Math.max(0,c.v-(55+c.v*.9)*dt):Math.min(0,c.v+90*dt);}
 if(c.driftT>0&&!(ctl.drift&&c.air<=0&&c.v>90&&c.crash<=0)){if(c.isP&&!G.demo&&c.driftT>.6&&c.driftDir){const b=Math.round(80+Math.min(c.driftT,3)*140);G.score+=b;pop(c.x,c.y-42,'¡DERRAPE! +'+b,'#ff3f8e');c.boostT=Math.max(c.boostT,.45+Math.min(c.driftT,2.2)*.3);Snd.boost();}c.driftT=0;c.driftDir=0;}
 {let d=c.h-c.va;while(d>Math.PI)d-=TAU;while(d<-Math.PI)d+=TAU;c.va+=d*Math.min(1,(c.driftT>0&&c.driftDir?1.6:9)*dt);}
 c.x+=Math.sin(c.va)*c.v*dt;c.y-=Math.cos(c.va)*c.v*dt;""")
rep("""const sx=Zn.shore(c.y)+11;if(c.x<sx){c.x=sx;if(c.h<0)c.h=Math.abs(c.h)*.4;""","""const sx=Zn.shore(c.y)+11;if(c.x<sx){c.x=sx;if(c.h<0)c.h=Math.abs(c.h)*.4;c.va=c.h;""")
rep("""if(c.x>ex){c.x=ex;if(c.h>0)c.h=-Math.abs(c.h)*.4;c.v*=.9;}""","""if(c.x>ex){c.x=ex;if(c.h>0)c.h=-Math.abs(c.h)*.4;c.va=c.h;c.v*=.9;}""")
# control input
rep(""" const ctlP=G.demo?aiCtl(P,dt):{turn:(input.right?1:0)-(input.left?1:0),thr:racing&&input.acc&&P.fin===0};""",
""" const ctlP=G.demo?aiCtl(P,dt):{turn:(input.right?1:0)-(input.left?1:0),thr:racing&&input.acc&&P.fin===0,rev:racing&&input.rev,drift:racing&&input.drift&&P.fin===0};""")
rep(""" if(G.mode==='count'){ctlP.thr=false;}""",""" if(G.mode==='count'){ctlP.thr=false;ctlP.drift=false;ctlP.rev=false;}""")
# drift spray particles
rep(""" for(const c of crafts())if(c.v>60&&c.air<=0""",""" if(P.driftT>0&&P.air<=0){const nx=Math.cos(P.h),ny=Math.sin(P.h),bx=P.x-Math.sin(P.h)*22,by=P.y+Math.cos(P.h)*22;for(let k=0;k<6;k++){const side=P.driftDir?-P.driftDir:(Math.random()<.5?-1:1),sp=110+Math.random()*200;G.parts_fx.push({x:bx+side*nx*9,y:by+side*ny*9,vx:side*nx*sp+(Math.random()-.5)*50,vy:side*ny*sp+Math.cos(P.h)*70,life:.45+Math.random()*.45,max:.9,s:3+Math.random()*5});}if(G.parts_fx.length>650)G.parts_fx.splice(0,G.parts_fx.length-650);G.shake=Math.max(G.shake,P.driftDir?1.6:.8);}
 for(const c of crafts())if(c.v>60&&c.air<=0""")
# fuel use with reverse
rep("""G.fuel=Math.max(0,G.fuel-(ctlP.thr?1.25:.12)""","""G.fuel=Math.max(0,G.fuel-(ctlP.thr||ctlP.drift?1.25:ctlP.rev?.5:.12)""")
# audio
rep(""" engineSet(rpm,spd,boost,thr,exh,tur,idle){const e=this.eng;if(!e)return;""",""" engineSet(rpm,spd,boost,thr,exh,tur,idle,drift){const e=this.eng;if(!e)return;""")
rep("""e.wg.gain.setTargetAtTime(idle?0:spd*.16,t,.1);e.wf.frequency.setTargetAtTime(500+spd*1400,t,.1);""","""e.wg.gain.setTargetAtTime(idle?0:drift?.34:spd*.16,t,.06);e.wf.frequency.setTargetAtTime(drift?2600:500+spd*1400,t,.08);""")
rep("""const r=clamp(P.v/P.st.maxV,0,1.4);const rpm=clamp(.18+r*.72+(P._thr?.1:0),0,1.3);Snd.engineSet(rpm,clamp(r,0,1)*(P.air>0?.2:1),P.boostT>0?1:0,P._thr?1:0,G.parts.escape?1:0,G.parts.turbo?1:0,0);}""",
"""const r=clamp(Math.abs(P.v)/P.st.maxV,0,1.4);const rpm=clamp(.18+r*.72+(P._thr||P.driftT>0?.12:0),0,1.3);Snd.engineSet(rpm,clamp(r,0,1)*(P.air>0?.2:1),P.boostT>0?1:0,P._thr?1:0,G.parts.escape?1:0,G.parts.turbo?1:0,0,P.driftT>0&&P.air<=0);}""")
# HUD speed
rep("""const kmh=Math.round(P.v*.31);setTxt('spd',String(kmh));""","""const kmh=Math.round(Math.abs(P.v)*.31);setTxt('spd',(P.v<-3?'R ':'')+kmh);""")
# bar open / close reset va
rep("""const P=G.P;P.v=0;P.h=0;""","""const P=G.P;P.v=0;P.h=0;P.va=0;P.driftT=0;""")
rep("""Frena en el círculo para entrar""","""Frena con ATRÁS dentro del círculo""")
# controls
rep("""let padDir=0,padAcc=false;""","""let padDir=0,padAcc=false,padRev=false,padDrift=false;""")
rep("""input.acc=!!keys.a||padAcc;""","""input.acc=!!keys.a||padAcc;input.rev=!!keys.b||padRev;input.drift=!!keys.dr||padDrift;""")
rep("""hold($('#bTurbo'),v=>{if(v&&G.mode==='play')input.turbo=true;});""","""hold($('#bTurbo'),v=>{if(v&&G.mode==='play')input.turbo=true;});
hold($('#bDrift'),v=>{padDrift=v;sync();});
hold($('#bRev'),v=>{padRev=v;sync();});""")
rep(""" else if(k==='ArrowUp'||k==='w'||k==='W'||k===' '){keys.a=1;menuOk();}else if(k==='Shift'||k==='x'||k==='X'||k==='ArrowDown'){if(G.mode==='play')input.turbo=true;}""",
""" else if(k==='ArrowUp'||k==='w'||k==='W'){keys.a=1;menuOk();}else if(k==='ArrowDown'||k==='s'||k==='S'){keys.b=1;}else if(k===' '||k==='c'||k==='C'){keys.dr=1;}else if(k==='Shift'||k==='x'||k==='X'){if(G.mode==='play')input.turbo=true;}""")
rep("""else if(k==='ArrowUp'||k==='w'||k==='W'||k===' ')keys.a=0;sync();});""","""else if(k==='ArrowUp'||k==='w'||k==='W')keys.a=0;else if(k==='ArrowDown'||k==='s'||k==='S')keys.b=0;else if(k===' '||k==='c'||k==='C')keys.dr=0;sync();});""")
rep("""addEventListener('blur',()=>{keys.l=keys.r=keys.a=0;padAcc=false;""","""addEventListener('blur',()=>{keys.l=keys.r=keys.a=keys.b=keys.dr=0;padAcc=false;padRev=false;padDrift=false;""")
# tip at first race
rep("""msg(G.zone.Z.name,G.zone.Z.goal.split('.')[0],'var(--cyan)');}};""","""msg(G.zone.Z.name,G.zone.Z.goal.split('.')[0],'var(--cyan)');if(G.zi===0&&G.lap===0&&!G._tip){G._tip=1;setTimeout(()=>{if(G.mode==='play')msg('TRUCO','DERRAPE + un lado = derrape y miniturbo','var(--pink)');},2600);}}};""")
open(p,'w',encoding='utf-8').write(s)
print('ok')
