p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)

# ================= ESCAPES =================
i=s.index(" engineStart(){");j=s.index(" sirenStart(){")
s=s[:i]+""" engineStart(){if(!this.ctx||this.eng)return;const c=this.ctx;
  const o1=c.createOscillator();o1.type='sawtooth';const o2=c.createOscillator();o2.type='square';const o3=c.createOscillator();o3.type='triangle';
  const mx=c.createGain();mx.gain.value=.5;const ws=c.createWaveShaper();ws.curve=this.curve(2);
  const lp=c.createBiquadFilter();lp.type='lowpass';lp.Q.value=3;lp.frequency.value=500;const am=c.createGain();am.gain.value=1;const g=c.createGain();g.gain.value=0;
  o1.connect(mx);o2.connect(mx);o3.connect(mx);mx.connect(ws);ws.connect(lp);lp.connect(am);am.connect(g);g.connect(this.sfx);
  const lfo=c.createOscillator();lfo.type='square';const ld=c.createGain();ld.gain.value=0;lfo.connect(ld);ld.connect(am.gain);
  const sub=c.createOscillator();sub.type='sine';const slp=c.createBiquadFilter();slp.type='lowpass';slp.frequency.value=220;const sg=c.createGain();sg.gain.value=0;sub.connect(slp);slp.connect(sg);sg.connect(this.sfx);
  const rs=c.createOscillator();rs.type='sawtooth';const rbp=c.createBiquadFilter();rbp.type='bandpass';rbp.frequency.value=1500;rbp.Q.value=.9;const rg=c.createGain();rg.gain.value=0;rs.connect(rbp);rbp.connect(rg);rg.connect(this.sfx);
  const wn=c.createBufferSource();wn.buffer=this.noise;wn.loop=true;const wf=c.createBiquadFilter();wf.type='bandpass';wf.frequency.value=900;wf.Q.value=.6;const wg=c.createGain();wg.gain.value=0;wn.connect(wf);wf.connect(wg);wg.connect(this.sfx);
  const wh=c.createOscillator();wh.type='sine';wh.frequency.value=2000;const whg=c.createGain();whg.gain.value=0;wh.connect(whg);whg.connect(this.sfx);
  [o1,o2,o3,lfo,sub,rs,wn,wh].forEach(n=>n.start());this.eng={o1,o2,o3,ws,lp,g,lfo,ld,sub,sg,rs,rg,wn,wg,wf,wh,whg,ex:-1};},
 engineSet(rpm,spd,boost,thr,exh,tur,idle,drift){const e=this.eng;if(!e)return;const t=this.ctx.currentTime,f=30+rpm*92,x=clamp(exh|0,0,3),r1=Math.min(1,rpm);
  if(e.ex!==x){e.ws.curve=this.curve(2+x*3.4);e.ex=x;}
  e.o1.frequency.setTargetAtTime(f,t,.05);e.o2.frequency.setTargetAtTime(f*.5,t,.05);e.o3.frequency.setTargetAtTime(f*2.01,t,.05);
  e.lp.frequency.setTargetAtTime((240+rpm*2000)*(1+x*.16),t,.06);
  e.g.gain.setTargetAtTime(idle?0:(.03+thr*.042+rpm*.042)*[1,1.15,1.32,1.5][x],t,.08);
  e.sub.frequency.setTargetAtTime(f*.5,t,.05);e.sg.gain.setTargetAtTime(idle?0:[0,.03,.045,.06][x]*(.45+rpm*.55),t,.08);
  e.rs.frequency.setTargetAtTime(f*1.5,t,.05);e.rg.gain.setTargetAtTime(idle?0:[0,0,.009,.017][x]*r1*(thr?1:.5),t,.08);
  e.lfo.frequency.setTargetAtTime(f*.5,t,.05);e.ld.gain.setTargetAtTime(idle?0:[0,.12,.22,.32][x]*(1.2-r1*.6),t,.08);
  e.wg.gain.setTargetAtTime(idle?0:drift?.34:spd*.16,t,.06);e.wf.frequency.setTargetAtTime(drift?2600:500+spd*1400,t,.08);
  e.whg.gain.setTargetAtTime(idle?0:(tur?.004+rpm*.009:0)+boost*.02,t,.08);e.wh.frequency.setTargetAtTime(1400+rpm*2600+boost*1500,t,.08);},
 engineStop(){const e=this.eng;if(!e)return;this.eng=null;const t=this.ctx.currentTime;[e.g,e.sg,e.rg,e.wg,e.whg].forEach(g=>g.gain.setTargetAtTime(0,t,.05));[e.o1,e.o2,e.o3,e.lfo,e.sub,e.rs,e.wn,e.wh].forEach(n=>{try{n.stop(t+.4);}catch(_){}});},
 pops(st,level){if(!this.ok()||st<2)return;const n=st>=3?9+Math.floor(Math.random()*4):4+Math.floor(Math.random()*2);let t=this.ctx.currentTime+.05;for(let i=0;i<n;i++){const v=(st>=3?.95:.65)*(.6+Math.random()*.4)*(.6+clamp(level,0,1)*.4);
  this.hiss({at:t,ft:'bandpass',f:2800+Math.random()*900,q:.7,t:.014,v:v*1.1,a:.001});this.hiss({at:t,ft:'lowpass',f:1300+Math.random()*700,q:.7,t:.05,v:v*.95,a:.002});this.tone({at:t,w:'sine',f:115,f2:42,t:.08,v:v*1.05,a:.003});t+=.045+Math.random()*.12;}},
"""+s[j:]
rep("if(wasThr&&!ctlP.thr&&G.parts.bov&&P.v>P.st.maxV*.55&&racing)Snd.bov(G.parts.bov,(P.v-P.st.maxV*.55)/(P.st.maxV*.45));",
    "if(wasThr&&!ctlP.thr&&G.parts.bov&&P.v>P.st.maxV*.55&&racing)Snd.bov(G.parts.bov,(P.v-P.st.maxV*.55)/(P.st.maxV*.45));\n if(wasThr&&!ctlP.thr&&(G.parts.escape|0)>=2&&P.v>P.st.maxV*.55&&racing&&!G.demo)Snd.pops(Math.min(3,G.parts.escape|0),P.v/P.st.maxV);")

# ================= ZONAS NUEVAS =================
rep("{name:'CARRERA ES TRENC',","{name:'LAS RAMPAS',obj:'jumps',needJ:10,goal:'Haz 10 saltos de rampa y llega antes de que se acabe el tiempo. Mar abierto, sin costa.',len:15000,riv:0,bar:null,theme:'open',tod:'noon',pace:195,ramps:1},\n {name:'CARRERA ES TRENC',")
rep("{name:'LA FINAL',","{name:'CARRERA DE BOYAS',obj:'race3',goal:'Termina entre los 3 primeros. Pasa cada boya por el lado de la flecha: naranja por la izquierda, verde por la derecha. Si fallas, 2 segundos parado.',len:16000,riv:5,bar:null,theme:'open',tod:'afternoon',skill:.9,turns:1},\n {name:'LA FINAL',")
rep("let best=Math.max(0,Math.min(10,store.get('ct_best',0)|0));","let best=Math.max(0,Math.min(12,store.get('ct_best',0)|0));")
rep("if(Z.obj==='jumps'&&G.jumps<6){ok=false;why='Solo has hecho '+G.jumps+' saltos de 6.';}","if(Z.obj==='jumps'&&G.jumps<(Z.needJ||6)){ok=false;why='Solo has hecho '+G.jumps+' saltos de '+(Z.needJ||6)+'.';}")
rep("setTxt('hvL',Math.min(G.jumps,99)+'<i>/6</i>');","setTxt('hvL',Math.min(G.jumps,99)+'<i>/'+(Z.needJ||6)+'</i>');")
# mar abierto
rep("kindU=u=>{const cv=cove(u);return cv&&cv.d<cv.w*.86?'cala':'mount';};}",
    "kindU=u=>{const cv=cove(u);return cv&&cv.d<cv.w*.86?'cala':'mount';};}\n if(Z.theme==='open'){shoreU=u=>-(VW>WG?(VW-WG)/2:0);kindU=u=>'open';}")
rep("let lastYacht=-2000,u=560,gateSide=0;","""let lastYacht=-2000,u=560,gateSide=0;
 if(Z.ramps){u=len;let u2=650,pat=0;const ramp=(x,uu,w)=>add({t:'ramp',x,y:-uu,w:w||100,kick:1}),air=(x,uu)=>{for(let i=0;i<4;i++)add({t:'coin',x,y:-uu-64-i*28,air:1});};
  while(u2<len-800){const L=zone.shore(-u2)+40,R=WG-40,mid=(L+R)/2,k=pat++%6;
   if(k===0){const x=[L+64,mid,R-64][(r()*3)|0];ramp(x,u2);air(x,u2);u2+=430;}
   else if(k===1){for(let i=0;i<3;i++)ramp(i%2?R-72:L+72,u2+i*300,92);u2+=1000;}
   else if(k===2){const x=lerp(L+70,R-70,r());ramp(x,u2);ramp(x,u2+240);air(x,u2+240);u2+=660;}
   else if(k===3){const x=lerp(L+70,R-70,r());ramp(x,u2,112);add({t:r()<.5?'sail':'motor',x,y:-u2-125,rot:0});u2+=540;}
   else if(k===4){ramp(L+72,u2,90);ramp(R-72,u2,90);air(r()<.5?L+72:R-72,u2);u2+=470;}
   else{for(let i=0;i<3;i++)add({t:'rock',x:lerp(L+20,R-20,r()),y:-u2-(r()-.5)*60,rad:10+r()*7,v:(r()*3)|0});const x=lerp(L+60,R-60,r());for(let i=0;i<6;i++)add({t:'coin',x:clamp(x+Math.sin(i*.8)*30,L,R),y:-u2-90-i*28});u2+=400;}
   if(r()<.14)add({t:'fuel',x:lerp(L+20,R-20,r()),y:-u2+70});u2+=130+r()*90;}
  const mu=len-560;add({t:'ramp',x:WG/2,y:-mu,w:210,kick:1,mega:1});for(let i=0;i<7;i++)add({t:'coin',x:WG/2,y:-mu-90-i*34,air:1});}
 if(Z.turns){u=len;let tu=900,side=r()<.5?-1:1;while(tu<len-520){const L=zone.shore(-tu)+40,R=WG-40,mid=(L+R)/2;if(r()<.72)side=-side;const x=side<0?lerp(mid-10,R-40,r()):lerp(L+40,mid+10,r());add({t:'tbuoy',x,y:-tu,side});
   for(let i=0;i<4;i++)add({t:'coin',x:clamp(x+side*48,L,R),y:-tu+150-i*30});if(r()<.35)add({t:'rock',x:clamp(x-side*72,L+10,R-10),y:-tu-210,rad:10+r()*6,v:0});if(r()<.1)add({t:'fuel',x:lerp(L+30,R-30,r()),y:-tu+260});tu+=480+r()*170;}}""")
rep("for(let uu=-400;uu<len+600;uu+=18+dr()*26){const y=-uu,kd=zone.kind(y),sx=zone.shore(y);","for(let uu=-400;uu<len+600;uu+=18+dr()*26){if(Z.theme==='open')break;const y=-uu,kd=zone.kind(y),sx=zone.shore(y);")
# render: sin terreno en mar abierto, boyas de los lados
rep(" const[x0]=chunkRange();for(let i=Math.floor(camTop/CH);",
""" if(Zn.Z.theme==='open'){const xl=Zn.shore(camTop)+8,xr=(VW>WG?WG+(VW-WG)/2:WG)-8;
  for(let cy=Math.floor(camTop/90);cy<=Math.floor((camTop+VH)/90);cy++)for(let k=0;k<3;k++){const h=hash2(cy,k,Zn.seed),x=xl+14+h*(xr-xl-28),y=cy*90+hash2(k,cy,7)*90,a=.18+.18*Math.sin(G.t*2+h*9);ctx.strokeStyle=`rgba(255,255,255,${a.toFixed(3)})`;ctx.lineWidth=1.4;ctx.beginPath();ctx.moveTo(x-7,y);ctx.quadraticCurveTo(x,y-3,x+7,y);ctx.stroke();}
  ctx.strokeStyle='rgba(255,255,255,.28)';ctx.lineWidth=1;ctx.setLineDash([4,6]);for(const x of[xl,xr]){ctx.beginPath();ctx.moveTo(x,camTop-10);ctx.lineTo(x,camTop+VH+10);ctx.stroke();}ctx.setLineDash([]);
  for(let y=Math.floor(camTop/36)*36;y<camTop+VH+36;y+=36)for(const x of[xl,xr]){ctx.fillStyle='rgba(0,20,50,.25)';ctx.beginPath();ctx.ellipse(x+2,y+3,6,3.5,0,0,TAU);ctx.fill();ctx.fillStyle='#ffd21a';ctx.beginPath();ctx.arc(x,y,4.6,0,TAU);ctx.fill();ctx.fillStyle='rgba(255,255,255,.65)';ctx.beginPath();ctx.arc(x-1.4,y-1.6,1.6,0,TAU);ctx.fill();}}
 else{const[x0]=chunkRange();for(let i=Math.floor(camTop/CH);""")
rep("ctx.drawImage(c,x0,i*CH,c.width/K,c.height/K);}\n","ctx.drawImage(c,x0,i*CH,c.width/K,c.height/K);}}\n")
# rampas de verdad + boyas de giro (dibujo)
rep("case 'ramp':{const w=o.w;ctx.save();","""case 'ramp':{if(o.kick){const w=o.w,Lr=o.mega?92:52;ctx.save();ctx.translate(o.x,o.y);
  ctx.fillStyle='rgba(0,20,50,.28)';ctx.beginPath();ctx.moveTo(-w/2+8,4);ctx.lineTo(w/2+8,4);ctx.lineTo(w/2+12,Lr+6);ctx.lineTo(-w/2+4,Lr+6);ctx.closePath();ctx.fill();
  ctx.save();ctx.beginPath();ctx.moveTo(-w/2,0);ctx.lineTo(w/2,0);ctx.lineTo(w/2+6,Lr);ctx.lineTo(-w/2-6,Lr);ctx.closePath();ctx.clip();
  let gg=ctx.createLinearGradient(0,0,0,Lr);gg.addColorStop(0,'#ffffff');gg.addColorStop(1,'#d9dee6');ctx.fillStyle=gg;ctx.fillRect(-w/2-8,0,w+16,Lr);
  ctx.fillStyle='#ff7a1a';for(let k=-w-Lr;k<w;k+=24){ctx.beginPath();ctx.moveTo(k,0);ctx.lineTo(k+12,0);ctx.lineTo(k+12+Lr*.5,Lr);ctx.lineTo(k+Lr*.5,Lr);ctx.closePath();ctx.fill();}
  gg=ctx.createLinearGradient(0,0,0,Lr);gg.addColorStop(0,'rgba(255,255,255,.3)');gg.addColorStop(1,'rgba(0,0,0,.2)');ctx.fillStyle=gg;ctx.fillRect(-w/2-8,0,w+16,Lr);ctx.restore();
  ctx.strokeStyle='#2a2f3a';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(-w/2,0);ctx.lineTo(-w/2-6,Lr);ctx.moveTo(w/2,0);ctx.lineTo(w/2+6,Lr);ctx.stroke();ctx.strokeStyle='#ffffff';ctx.lineWidth=3.5;ctx.beginPath();ctx.moveTo(-w/2,0);ctx.lineTo(w/2,0);ctx.stroke();
  ctx.fillStyle='#9aa6b5';for(const sx of[-1,1]){ctx.beginPath();ctx.ellipse(sx*(w/2+8),Lr-8,4,10,0,0,TAU);ctx.fill();}
  for(let i=0;i<14;i++){const x=lerp(-w/2-6,w/2+6,i/13);ctx.globalAlpha=.75;ctx.drawImage(SP.dot.c,x-3,Lr-2+Math.sin(i*1.7+t*6)*1.5,6,6);}ctx.globalAlpha=1;
  if(o.mega){ctx.fillStyle='rgba(10,22,48,.85)';ctx.beginPath();ctx.roundRect(-46,Lr*.5-10,92,20,8);ctx.fill();ctx.fillStyle='#ffc93c';ctx.font='800 13px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('MEGA RAMPA',0,Lr*.5+1);}
  ctx.restore();return;}
  const w=o.w;ctx.save();""")
rep(" case 'gate':{",""" case 'tbuoy':{const s=o.side,col=s<0?'#ff7a1a':'#28c25a',dk=s<0?'#b8420a':'#13803a';ctx.save();ctx.translate(o.x,o.y);
  ctx.globalAlpha=.55;ctx.strokeStyle='#ffffff';ctx.lineWidth=3;ctx.lineCap='round';ctx.lineJoin='round';const ax=s*48;for(let k=0;k<3;k++){const yy=42-k*16;ctx.beginPath();ctx.moveTo(ax-8,yy+6);ctx.lineTo(ax,yy-2);ctx.lineTo(ax+8,yy+6);ctx.stroke();}ctx.globalAlpha=1;
  ctx.fillStyle='rgba(255,255,255,.45)';ctx.beginPath();ctx.ellipse(0,5,21,8,0,0,TAU);ctx.fill();ctx.fillStyle='rgba(0,20,50,.3)';ctx.beginPath();ctx.ellipse(5,8,15,10,0,0,TAU);ctx.fill();
  const gg=ctx.createRadialGradient(-5,-6,2,0,0,16);gg.addColorStop(0,'#ffffff');gg.addColorStop(.25,col);gg.addColorStop(1,dk);ctx.fillStyle=gg;ctx.beginPath();ctx.arc(0,0,14,0,TAU);ctx.fill();ctx.strokeStyle='#ffffff';ctx.lineWidth=2.5;ctx.beginPath();ctx.arc(0,0,9,0,TAU);ctx.stroke();
  ctx.fillStyle=col;ctx.beginPath();ctx.roundRect(-18,-48,36,22,7);ctx.fill();ctx.strokeStyle='#ffffff';ctx.lineWidth=2;ctx.stroke();
  ctx.fillStyle='#ffffff';ctx.beginPath();ctx.moveTo(s*13,-37);ctx.lineTo(s*3,-45);ctx.lineTo(s*3,-40);ctx.lineTo(-s*11,-40);ctx.lineTo(-s*11,-34);ctx.lineTo(s*3,-34);ctx.lineTo(s*3,-29);ctx.closePath();ctx.fill();
  if(o.ok){ctx.fillStyle='#7be35a';ctx.beginPath();ctx.arc(22,-37,7,0,TAU);ctx.fill();ctx.strokeStyle='#0b2a12';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(18.5,-37);ctx.lineTo(21.5,-34);ctx.lineTo(26,-40);ctx.stroke();}
  ctx.restore();}return;
 case 'gate':{""")
rep("case 'buoy':return Math.hypot(o.x-x,o.y-y)<7+rad;","case 'buoy':return Math.hypot(o.x-x,o.y-y)<7+rad;case 'tbuoy':return Math.hypot(o.x-x,o.y-y)<12+rad;")
# saltos: mega rampa
rep("if(o.t==='ramp'){if(c.prevY>o.y&&c.y<=o.y&&Math.abs(c.x-o.x)<o.w/2&&c.air<=0&&c.v>110&&c.crash<=0){startJump(c);if(c.isP&&!G.demo){const b=100+Math.round(c.v/4);G.score+=b;pop(c.x,c.y-40,'¡SALTO! +'+b,'#ffc93c');}}continue;}",
    "if(o.t==='ramp'){if(c.prevY>o.y&&c.y<=o.y&&Math.abs(c.x-o.x)<o.w/2&&c.air<=0&&c.v>110&&c.crash<=0){startJump(c);if(o.mega){c.airT*=1.8;c.air=c.airT;}if(c.isP&&!G.demo){const b=(o.mega?600:100)+Math.round(c.v/4);G.score+=b;pop(c.x,c.y-40,(o.mega?'¡MEGA SALTO! +':'¡SALTO! +')+b,o.mega?'#33d6ff':'#ffc93c');if(o.mega)msg('¡MEGA SALTO!','','var(--cyan)');}}continue;}")
# boyas de giro: lado bueno / penalización
rep("   if(o.t==='island'||o.t==='pass')continue;\n   if(o.t==='piri'",
"""   if(o.t==='tbuoy'&&!G.demo&&!c.fin&&c.prevY>o.y&&c.y<=o.y){const ok=o.side<0?c.x<o.x:c.x>o.x;
    if(c.isP){if(ok){o.ok=1;G.score+=60;Snd.gate();pop(c.x,c.y-36,'¡BIEN! +60','#7be35a');}else{c.stuckT=2;c.stuckY=c.y;c.v=0;c.boostT=0;Snd.miss();G.shake=4;msg('¡PENALIZACIÓN!','Boya por el lado malo · 2 s','var(--red)');}}
    else if(!ok){c.stuckT=2;c.stuckY=c.y;c.v=0;c.boostT=0;}}
   if(o.t==='island'||o.t==='pass')continue;
   if(o.t==='piri'""")
rep("if(!c.isP&&c.pit===2){","if(!c.isP&&c.stuckT>0&&Zn.Z.turns){ctx.font='800 10px \"Saira Condensed\",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';const w=ctx.measureText('PENALIZADO').width+12;ctx.fillStyle='rgba(8,22,48,.78)';ctx.beginPath();ctx.roundRect(c.x-w/2,c.y-50,w,15,7);ctx.fill();ctx.fillStyle='#ff4757';ctx.fillText('PENALIZADO',c.x,c.y-42.5);}\n  if(!c.isP&&c.pit===2){")
# IA: buscar el lado bueno de la siguiente boya
rep(" const O=Zn.objs,s=findStart(O,c.y-240);if(!bigDone)",
    " if(!bigDone&&Zn.Z.turns){let nb=null;const O2=Zn.objs;for(let i=findStart(O2,c.y-560);i<O2.length&&O2[i].y<c.y-4;i++)if(O2[i].t==='tbuoy')nb=O2[i];if(nb){c.ai.tx=clamp(nb.x+nb.side*48,L+8,R-8);c.ai.re=Math.max(c.ai.re,.25);bigDone=true;}}\n const O=Zn.objs,s=findStart(O,c.y-240);if(!bigDone)")
rep("if(o.t==='coin'||o.t==='check'||o.t==='finish'||o.t==='ramp'||o.t==='can'||o.t==='fuel'||o.t==='gate'||o.t==='island'||o.t==='pass')continue;const w=",
    "if(o.t==='coin'||o.t==='check'||o.t==='finish'||o.t==='ramp'||o.t==='can'||o.t==='fuel'||o.t==='gate'||o.t==='island'||o.t==='pass'||o.t==='tbuoy')continue;const w=")

# ================= PORTADAS =================
rep(" {tag:'CARRERA · TOP 2',sky:['#1ea6f5','#e8faff']"," {tag:'10 SALTOS DE RAMPA',sky:['#1f8ae6','#d2efff'],sea:['#56b8ea','#0a4f9e'],sun:[90,24,'#ffffff'],land:'ramps'},\n {tag:'CARRERA · TOP 2',sky:['#1ea6f5','#e8faff']")
rep(" {tag:'GANA A EL TIBURÓN',"," {tag:'CARRERA · TOP 3',sky:['#3d72c8','#ffd8a6'],sea:['#4f9fd2','#0a4486'],sun:[320,48,'#fff0c8'],land:'buoys'},\n {tag:'GANA A EL TIBURÓN',")
rep("function drawCover(c,zi){","""function cvRampSide(g,x,y,s){g.save();g.translate(x,y);g.scale(s,s);g.fillStyle='rgba(255,255,255,.75)';g.beginPath();g.ellipse(-4,1,40,4,0,0,TAU);g.fill();
 g.beginPath();g.moveTo(-36,0);g.lineTo(34,0);g.lineTo(34,-26);g.closePath();g.save();g.clip();g.fillStyle='#ffffff';g.fillRect(-40,-30,80,32);g.fillStyle='#ff7a1a';for(let k=-50;k<40;k+=14){g.beginPath();g.moveTo(k,0);g.lineTo(k+7,0);g.lineTo(k+19,-30);g.lineTo(k+12,-30);g.closePath();g.fill();}g.restore();
 g.strokeStyle='#2a2f3a';g.lineWidth=2;g.beginPath();g.moveTo(-36,0);g.lineTo(34,-26);g.lineTo(34,0);g.stroke();g.fillStyle='#9aa6b5';g.fillRect(-30,0,60,4);g.restore();}
function cvTBuoy(g,x,y,s,side){const col=side<0?'#ff7a1a':'#28c25a',dk=side<0?'#b8420a':'#13803a';g.save();g.translate(x,y);g.scale(s,s);g.fillStyle='rgba(255,255,255,.7)';g.beginPath();g.ellipse(0,2,26,5,0,0,TAU);g.fill();
 const gg=g.createLinearGradient(-16,0,16,0);gg.addColorStop(0,dk);gg.addColorStop(.35,col);gg.addColorStop(.6,'#ffffff');gg.addColorStop(1,dk);g.fillStyle=gg;g.beginPath();g.roundRect(-16,-46,32,48,10);g.fill();g.fillStyle='rgba(255,255,255,.85)';g.fillRect(-16,-30,32,7);
 g.fillStyle=col;g.beginPath();g.roundRect(-20,-76,40,24,7);g.fill();g.strokeStyle='#fff';g.lineWidth=2;g.stroke();g.fillStyle='#fff';g.beginPath();g.moveTo(side*15,-64);g.lineTo(side*4,-72);g.lineTo(side*4,-67);g.lineTo(-side*12,-67);g.lineTo(-side*12,-61);g.lineTo(side*4,-61);g.lineTo(side*4,-56);g.closePath();g.fill();g.restore();}
function drawCover(c,zi){""")
rep(" if(L==='storm'){cvRidge(g,q,-20,420,HZ,40,8,'#111a30');",""" if(L==='ramps'||L==='buoys'){for(let i=0;i<3;i++){const x=40+q()*320;g.fillStyle='rgba(255,255,255,.85)';g.fillRect(x,HZ-3,10+q()*8,2.5);g.fillStyle='rgba(40,60,90,.5)';g.fillRect(x+3,HZ-6,4,3);}}
 if(L==='storm'){cvRidge(g,q,-20,420,HZ,40,8,'#111a30');""")
rep(" else if(L==='final'){cvRival(g,q,SHARK,150,152,.36,-.08);hero(285,168,.42,-.15,0);}",""" else if(L==='final'){cvRival(g,q,SHARK,150,152,.36,-.08);hero(285,168,.42,-.15,0);}
 else if(L==='ramps'){cvRampSide(g,120,HZ+16,.45);cvRampSide(g,330,HZ+30,.6);cvRampSide(g,175,200,1.1);for(let i=0;i<6;i++){g.fillStyle='#ffd21a';g.beginPath();g.arc(232+i*20,96-Math.sin(i/5*Math.PI)*26,4.5,0,TAU);g.fill();g.strokeStyle='#b8860b';g.lineWidth=1;g.stroke();}hero(258,118,.38,-.34,56);}
 else if(L==='buoys'){cvTBuoy(g,90,HZ+22,.45,-1);cvTBuoy(g,330,HZ+34,.6,1);cvTBuoy(g,200,206,1,-1);cvRival(g,q,rv(0),110,150,.24,-.05);cvRival(g,q,rv(1),330,126,.2,-.03);hero(286,170,.42,-.16,0);}""")
open(p,'w').write(s);print('ok')
