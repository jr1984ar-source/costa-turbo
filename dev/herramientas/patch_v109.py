p='costa-turbo.html';s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
# motor entero 4 dB más bajo (motor, graves, escape y silbido del turbo; el ruido del agua igual)
rep("engineStart(){if(!this.ctx||this.eng)return;const c=this.ctx;","engineStart(){if(!this.ctx||this.eng)return;const c=this.ctx;const eb=c.createGain();eb.gain.value=Math.pow(10,-4/20);eb.connect(this.sfx);")
rep("am.connect(g);g.connect(this.sfx);","am.connect(g);g.connect(eb);")
rep("sg.gain.value=0;sub.connect(slp);slp.connect(sg);sg.connect(this.sfx);","sg.gain.value=0;sub.connect(slp);slp.connect(sg);sg.connect(eb);")
rep("rs.connect(rbp);rbp.connect(rg);rg.connect(this.sfx);","rs.connect(rbp);rbp.connect(rg);rg.connect(eb);")
rep("whg.connect(this.sfx)","whg.connect(eb)")
# carrera de recta: 3 motos esperando en la salida de la recta
rep(" zone.pgDest=D;G.pgRace=null;G.pgMis=null;",""" zone.pgDest=D;G.pgRace=null;G.pgMis=null;G.pgDrag=0;
 if(zone.lane){const L=zone.lane,ids=MOTOS.map(m=>m.id).filter(id=>id!==MOTOS[G.moto|0].id);zone.drag={st:'wait',t:0};
  for(let k=0;k<3;k++){const id=ids[(k*2+((r()*ids.length)|0))%ids.length],x=L.x+[-63,21,63][k];M.push({t:'pgdrag',k,id,x,y:L.y0+70,sx:x,sy:L.y0+70,h:0,v:0,vx:0,vy:0,flash:0,trail:[],boostT:0,fin:0,bt:[],fac:[.9,.96,1][k]});}}""")
rep("const L=Zn.lane;if(L&&P.prevY>L.mid&&P.y<=L.mid&&Math.abs(P.x-L.x)<L.w/2+20){","""{const L=Zn.lane,DR=Zn.drag;if(L&&DR){const rv=Zn.movers.filter(o=>o.t==='pgdrag'),sx=L.x-21,sy=L.y0+70;
  const mv=o=>{if(o.boostT>0)o.boostT-=dt;else if(o.bt.length&&DR.el>=o.bt[0]){o.bt.shift();o.boostT=o.btl;pop(o.x,o.y-50,'¡TURBO!','#33d6ff');}const tg=o.fin?0:o.vmax*(o.boostT>0?o.bm:1);if(o.v<tg)o.v=Math.min(tg,o.v+o.acc*dt);else o.v=Math.max(tg,o.v-(o.fin?220:120)*dt);o.y-=o.v*dt;
   o.tacc=(o.tacc||0)+o.v*dt;if(o.tacc>10){o.tacc=0;o.trail.unshift({x:o.x,y:o.y+26,h:0});if(o.trail.length>18)o.trail.pop();}};
  if(DR.st==='wait'){if(!G.pgRace&&!G.pgMis&&!G.demo){const d=Math.hypot(P.x-sx,P.y-sy);if(d<300&&!DR.hint){DR.hint=1;msg('CARRERA DE RECTA','Frena en tu sitio, entre las motos','var(--gold)');}else if(d>700)DR.hint=0;
    if(d<70&&P.v<P.st.maxV*.35){DR.st='count';DR.t=3.2;DR.last=4;G.pgDrag=1;DR.order=[];DR.pfin=0;
     for(const o of rv){o.x=o.sx;o.y=o.sy;o.v=0;o.fin=0;o.boostT=0;o.trail.length=0;o.bt=[1.5+Math.random()*4,6.5+Math.random()*9];o.vmax=P.st.maxV*o.fac;o.acc=P.st.acc*(.92+o.fac*.08);o.bm=P.st.bm;o.btl=P.st.bt;}}}}
  else if(DR.st==='count'){DR.t-=dt;P.v=0;P.h=0;P.va=0;P.x=sx;P.y=sy;const n=Math.ceil(DR.t);if(n!==DR.last&&n>0){DR.last=n;msg(String(n),'Carrera de recta · 2,5 km · usa el turbo','var(--gold)');Snd.click();}if(DR.t<=0){DR.st='run';DR.el=0;msg('¡YA!','¡A fondo!','var(--lime)');Snd.boost();}}
  else if(DR.st==='run'){DR.el+=dt;for(const o of rv){mv(o);if(!o.fin&&o.y<=L.y1){o.fin=1;DR.order.push(o);}}
   if(P.y<=L.y1){const pos=DR.order.length+1,prize=[600,250,100,0][pos-1],tt=DR.el.toFixed(2).replace('.',',');DR.st='done';DR.t=6;G.pgDrag=0;if(prize){G.money+=prize;G.score+=prize;saveWallet();}
    const best=store.get('ct_pg_drag',0);if(pos===1&&(!best||DR.el<best))store.set('ct_pg_drag',DR.el);if(pos===1)Snd.cash();else Snd.fail();buzz(60);
    msg(pos===1?'¡GANAS LA CARRERA DE RECTA!':'LLEGAS '+pos+'º',tt+' s'+(prize?' · +'+pts(prize)+' PESETAS':''),pos===1?'var(--lime)':'var(--gold)');}
   else if(Math.abs(P.x-L.x)>700||P.y>L.y0+500){DR.st='done';DR.t=4;G.pgDrag=0;msg('CARRERA ABANDONADA','','var(--red)');}}
  else if(DR.st==='done'){DR.t-=dt;for(const o of rv){if(!o.fin&&o.y<=L.y1)o.fin=1;mv(o);}if(DR.t<=0&&Math.hypot(P.x-sx,P.y-sy)>800&&rv.every(o=>Math.hypot(P.x-o.x,P.y-o.y)>700)){for(const o of rv){o.x=o.sx;o.y=o.sy;o.v=0;o.fin=0;o.boostT=0;o.trail.length=0;}DR.st='wait';}}}}
 const L=Zn.lane;if(L&&P.prevY>L.mid&&P.y<=L.mid&&Math.abs(P.x-L.x)<L.w/2+20){""")
# durante la carrera de recta no hay retos, paseos ni paradas
rep("  if(!R&&!G.pgMis&&!G.demo){for(const o of Zn.movers){if(o.t!=='npcjet'||!o.ch||o.cd>0)continue;","  if(!R&&!G.pgMis&&!G.pgDrag&&!G.demo){for(const o of Zn.movers){if(o.t!=='npcjet'||!o.ch||o.cd>0)continue;")
rep("  if(!M2&&!G.pgRace&&!G.demo&&!(G._stopCool>0)){for(const f of Zn._fares){","  if(!M2&&!G.pgRace&&!G.pgDrag&&!G.demo&&!(G._stopCool>0)){for(const f of Zn._fares){")
rep(" if(!G.demo&&!G.pgRace&&!G.pgMis&&!(G._stopCool>0))for(const o of Zn.big){"," if(!G.demo&&!G.pgRace&&!G.pgMis&&!G.pgDrag&&!(G._stopCool>0))for(const o of Zn.big){")
# dibujo: motos de la recta (estela, turbo) y sitio de salida
rep("case 'pgpol':{const pr=o._d||(o._d={t:'patrol'});","""case 'pgdrag':{const pr=o._d||(o._d={t:'npcjet'});pr.x=o.x;pr.y=o.y;pr.h=0;pr.id=o.id;pr.trail=o.trail;drawObj(pr);
  if(o.boostT>0){ctx.save();ctx.globalCompositeOperation='lighter';for(let k=0;k<3;k++){ctx.globalAlpha=.55;ctx.drawImage(SP.dot.c,o.x-6,o.y+34+k*7-6,12,12);}ctx.restore();}
  const DR=G.zone.drag,L=G.zone.lane,P=G.P;if(o.k===0&&DR&&DR.st==='wait'&&L&&P&&Math.hypot(P.x-L.x,P.y-o.y)<900){const x=L.x-21,y=L.y0+70,p=1+Math.sin(G.t*5)*.08;ctx.save();ctx.translate(x,y);ctx.fillStyle='rgba(255,225,77,.14)';ctx.beginPath();ctx.arc(0,0,44*p,0,TAU);ctx.fill();ctx.setLineDash([7,6]);ctx.lineDashOffset=-G.t*24;ctx.strokeStyle='#ffe14d';ctx.lineWidth=3;ctx.beginPath();ctx.arc(0,0,38*p,0,TAU);ctx.stroke();ctx.setLineDash([]);
   ctx.rotate(G.camA||0);label(0,64,'CARRERA DE RECTA','FRENA AQUÍ PARA EMPEZAR');ctx.restore();}}return;
 case 'pgpol':{const pr=o._d||(o._d={t:'patrol'});""")
rep("const APP_VER=108;","const APP_VER=109;")
open(p,'w').write(s);print('ok',len(s))
