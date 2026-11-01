p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)

# ---- zona: olas gigantes ----
rep("{name:'OLAS GIGANTES',obj:'jumps',goal:'Haz 6 saltos en las olas y llega antes de que se acabe el tiempo.',",
    "{name:'OLAS GIGANTES',obj:'jumps',giant:1,goal:'Haz 6 saltos y llega a tiempo. Las olas gigantes, cógelas rápido y recto: si vas lento o torcido, vuelcas.',")
rep("const wPat=Z.obj==='slalom'?{coins:3,ramp:1,rocks:1.5,boat:1,yacht:.6,kayak:.6,patrol:.4}:Z.obj==='jumps'?{coins:3,ramp:4,",
    "const wPat=Z.obj==='slalom'?{coins:3,ramp:1,rocks:1.5,boat:1,yacht:.6,kayak:.6,patrol:.4}:Z.obj==='jumps'?{coins:3,ramp:8,")
# pasos con cuña + ola
rep("if(Z.passes){for(const f of[.45,.8]){const cu=Math.round(len*f),L=zone.shore(-cu);add({t:'pass',y:-cu,gx:lerp(L+70,RX-70,.2+r()*.6),gw:76,h:110});resv.push([cu-260,cu+220]);}}",
"""if(Z.passes){for(const f of[.45,.8]){const cu=Math.round(len*f),L=zone.shore(-cu),gx=lerp(L+70,RX-70,.2+r()*.6),h=110,lw=gx-38-(L+12),rw=(RX-24)-(gx+38),wedge=lw<rw?-1:1;add({t:'pass',y:-cu,gx,gw:76,h,wedge});
  const fx0=wedge<0?gx+38:L+12,fx1=wedge<0?RX-24:gx-38,rx=(fx0+fx1)/2,rw2=Math.max(50,Math.min(112,fx1-fx0-20));add({t:'ramp',x:rx,y:-cu+h/2+78,w:rw2,sand:1});for(let i=0;i<3;i++)add({t:'coin',x:rx,y:-cu+40-i*40,air:1});
  resv.push([cu-260,cu+220]);}}
 zone.waves=[];if(Z.giant){for(const f of[.2,.34,.48,.62,.85,.88,.91]){const cu=Math.round(len*f);zone.waves.push({y:-cu,act:0,side:1,done:0,sp:44+r()*16,ph:r()*6,fade:1});resv.push([cu-240,cu+260]);}}""")
rep("G.time=Z.obj==='time'||Z.obj==='slalom'||Z.obj==='jumps'?Math.round(Zn.len/3/(Z.pace||200))+9:0;",
    "G.time=Z.obj==='time'||Z.obj==='slalom'||Z.obj==='jumps'?Math.round(Zn.len/3/(Z.pace||200))+9+(Z.giant?6:0):0;")

# ---- física: volcar / encallar ----
rep("function updateCraft(c,dt,ctl){const Zn=G.zone,st=c.st;\n c.prevY=c.y;",
"""function updateCraft(c,dt,ctl){const Zn=G.zone,st=c.st;
 c.prevY=c.y;
 if(c.capT>0){c.capT-=dt;c.v=0;c.air=0;c.z=0;c.boostT=0;if(c.capT<=0){c.capT=0;c.inv=1.3;c.h=0;c.va=0;}for(const p of c.trail)p.t+=dt;return;}
 if(c.stuckT>0){c.stuckT-=dt;c.v=0;if(c.stuckT<=0){c.stuckT=0;c.y=c.stuckY;c.inv=.8;}for(const p of c.trail)p.t+=dt;return;}""")
rep("if(input.turbo){input.turbo=false;if(G.turbo>0&&P.boostT<=0&&P.crash<=0){",
    "if(input.turbo){input.turbo=false;if(G.turbo>0&&P.boostT<=0&&P.crash<=0&&!(P.capT>0)&&!(P.stuckT>0)){")
rep(" for(const c of G.rivals){if(G.mode==='count'){c.prevY=c.y;continue;}updateCraft(c,dt,c.fin?{turn:0,thr:true}:aiCtl(c,dt));}",
""" for(const c of G.rivals){if(G.mode==='count'){c.prevY=c.y;continue;}updateCraft(c,dt,c.fin?{turn:0,thr:true}:aiCtl(c,dt));}
 if(Zn.waves&&Zn.waves.length&&!G.demo){for(const o of Zn.waves){
  if(o.done){o.y+=o.sp*dt;o.fade=Math.max(0,o.fade-dt*.5);continue;}
  if(!o.act&&o.y>P.y-640){o.act=1;if(racing){Snd.thunder();msg('¡OLA GIGANTE!','Rápido y recto o vuelcas','var(--cyan)');}}
  if(o.act&&racing)o.y+=o.sp*dt;
  const side=P.y>o.y?1:-1;if(o.act&&o.side>0&&side<0){o.done=1;giantHit(P);}o.side=side;}}""")
rep("function startJump(c){",
"""function giantHit(c){if(c.air>0||c.z>.5)return;
 if(c.v>=c.st.maxV*.72&&Math.abs(c.va)<.42&&!(c.capT>0)&&!(c.stuckT>0)){c.airT=.95+c.v/420;c.air=c.airT;c.trick=0;Snd.jump();G.jumps++;const b=400+Math.round(c.v);G.score+=b;pop(c.x,c.y-46,'¡OLA GIGANTE! +'+b,'#33d6ff');splash(c.x,c.y,26,170);G.shake=6;}
 else{c.capT=2.8;c.v=0;c.boostT=0;c.driftT=0;c.driftDir=0;c.air=0;c.z=0;Snd.crash();G.shake=12;buzz(160);splash(c.x,c.y,34,180);msg('¡VOLCADO!','Pierdes unos segundos','var(--red)');}}
function startJump(c){""")
# pasos: cuña, pared plana, encallar
rep("""   if(o.t==='pass'){if(c.z<.5&&Math.abs(c.y-o.y)<o.h/2+6){const gl=o.gx-o.gw/2,gr=o.gx+o.gw/2;if(c.x<gl+9||c.x>gr-9){if(c.prevY>=o.y+o.h/2-1){c.y=o.y+o.h/2+6;c.v*=.4;}else c.x=clamp(c.x,gl+9,gr-9);if(c.isP&&!G.demo&&!(c._isl>0)){c._isl=.7;Snd.bump();G.shake=5;pop(c.x,c.y-30,'¡ARENA!','#ff4757');}}}}""",
"""   if(o.t==='pass'){if(c.z<.5&&!(c.stuckT>0)&&Math.abs(c.y-o.y)<o.h/2+6){const gl=o.gx-o.gw/2,gr=o.gx+o.gw/2;if(c.x<gl+9||c.x>gr-9){
     const onW=o.wedge<0?c.x<gl+9:c.x>gr-9,back=o.y-o.h/2;let fy=o.y+o.h/2;
     if(onW){const xs=o.wedge<0?Zn.shore(o.y)-12:WG+(VW>WG?(VW-WG)/2:0)+30,xe=o.wedge<0?gl+9:gr-9,t=clamp((c.x-xs)/(xe-xs),0,1);fy=o.y+o.h/2-t*(o.h-8);}
     if(c.y<fy+6){
      if(c.prevY>=fy-2){if(onW){c.y=fy+6;c.x+=(o.wedge<0?1:-1)*Math.max(70,c.v*.75)*dt;c.v*=1-.5*dt;if(c.isP&&!G.demo&&!(c._isl>0)&&c.v>60){c._isl=.5;Snd.bump();G.shake=2;}}
       else{c.y=fy+6;c.v*=.4;if(c.isP&&!G.demo&&!(c._isl>0)){c._isl=.7;Snd.bump();G.shake=5;pop(c.x,c.y-30,'¡ARENA!','#ff4757');}}}
      else if(c.prevY<=back+1){c.y=back-6;}
      else{c.stuckT=1.1;c.stuckY=back-10;c.v=0;splash(c.x,c.y,14,90);if(c.isP&&!G.demo){Snd.bump();G.shake=6;pop(c.x,c.y-30,'¡ENCALLADO!','#ff4757');}}}}}}""")

# ---- dibujo: cuña, ola gigante, volcado ----
rep("""  bar(x0,gl);bar(gr,x1);for(const x of[gl,gr])ctx.drawImage(SP.buoy.c,x-9,o.y+h/2-9,18,18);""",
"""  const wedge=(xo,xg)=>{const yf=o.y+h/2,yb=o.y-h/2,P=[[xo,yf],[xg,yb+8],[xg,yb],[xo,yb]];const path=(k)=>{const cx=(xo*2+xg)/3,cy=(yf+yb*2)/3;ctx.beginPath();P.forEach(([a,b],i)=>{const X=cx+(a-cx)*k,Y=cy+(b-cy)*k;i?ctx.lineTo(X,Y):ctx.moveTo(X,Y);});ctx.closePath();};
   ctx.lineJoin='round';path(1);ctx.strokeStyle='rgba(120,240,230,.45)';ctx.lineWidth=22;ctx.stroke();ctx.fillStyle='#e6c88a';ctx.fill();ctx.strokeStyle='#e6c88a';ctx.lineWidth=8;ctx.stroke();path(.8);ctx.fillStyle='#f3dcae';ctx.fill();
   for(let i=0;i<34;i++){const t=i/33,x=lerp(xo,xg,t),y=lerp(yf,yb+8,t);ctx.fillStyle='rgba(255,255,255,.8)';ctx.beginPath();ctx.arc(x+Math.sin(i+G.t*3)*1.5,y+5,1.6,0,TAU);ctx.fill();}
   ctx.fillStyle='rgba(255,255,255,.55)';ctx.font='800 11px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';};
  if(o.wedge<0){wedge(x0,gl);bar(gr,x1);}else if(o.wedge>0){bar(x0,gl);wedge(x1,gr);}else{bar(x0,gl);bar(gr,x1);}for(const x of[gl,gr])ctx.drawImage(SP.buoy.c,x-9,o.y+h/2-9,18,18);""")
rep(" // objects\n for(const o of Zn.big||[]){",
""" // olas gigantes
 for(const o of Zn.waves||[])if(o.fade>0&&o.y>camTop-110&&o.y<camTop+VH+70)drawGiant(o);
 // objects
 for(const o of Zn.big||[]){""")
rep("function label(x,y,t,s){",
"""function drawGiant(o){const x0=G.zone.shore(o.y)-6,x1=WG+(VW>WG?(VW-WG)/2:0)+30,y=o.y,t=G.t+o.ph;ctx.save();ctx.globalAlpha=o.fade;
 let g=ctx.createLinearGradient(0,y-100,0,y);g.addColorStop(0,'rgba(120,230,240,0)');g.addColorStop(1,'rgba(160,245,248,.6)');ctx.fillStyle=g;ctx.fillRect(x0,y-100,x1-x0,100);
 g=ctx.createLinearGradient(0,y,0,y+54);g.addColorStop(0,'rgba(3,28,66,.62)');g.addColorStop(1,'rgba(3,28,66,0)');ctx.fillStyle=g;ctx.fillRect(x0,y,x1-x0,54);
 ctx.strokeStyle='rgba(255,255,255,.2)';ctx.lineWidth=1.2;for(let x=x0;x<x1;x+=13){ctx.beginPath();ctx.moveTo(x,y+6);ctx.lineTo(x+5,y+30+Math.sin(x*.3+t*3)*5);ctx.stroke();}
 ctx.fillStyle='#ffffff';ctx.beginPath();ctx.moveTo(x0,y+7);for(let x=x0;x<=x1;x+=8)ctx.lineTo(x,y-3+Math.sin(x*.09+t*4)*3+Math.sin(x*.23-t*2)*2);for(let x=x1;x>=x0;x-=8)ctx.lineTo(x,y+8+Math.sin(x*.13+t*3)*3);ctx.closePath();ctx.fill();
 for(let i=0;i<9;i++){const x=x0+(i+.5)*(x1-x0)/9+Math.sin(t+i)*8;ctx.fillStyle='rgba(255,255,255,.9)';ctx.beginPath();ctx.ellipse(x,y+11,11+Math.sin(t*3+i)*3,5,0,0,TAU);ctx.fill();}
 for(let i=0;i<46;i++){const x=x0+((i*53.7+t*30)%(x1-x0)),yy=y-6-((i*17+t*40)%26);ctx.fillStyle='rgba(255,255,255,.75)';ctx.beginPath();ctx.arc(x,yy,1.2+(i%3)*.7,0,TAU);ctx.fill();}
 ctx.restore();}
function drawCapsized(c){const T=2.8-c.capT,fl=T<.35?Math.cos(T/.35*Math.PI):c.capT<.35?Math.cos(c.capT/.35*Math.PI):-1;
 if(!SP.jetBot||SP.jetBot.k!==K){const hc=playerSk().hull||'#ffffff';SP.jetBot=sprite(32,68,g=>{hullPath(g);g.fillStyle=mixc(hc,'#000000',.5);g.fill();g.strokeStyle='rgba(255,255,255,.28)';g.lineWidth=1.3;g.beginPath();g.moveTo(0,-26);g.lineTo(0,27);g.stroke();g.fillStyle='#2a2d33';g.fillRect(-4,23,8,7);});SP.jetBot.k=K;}
 ctx.save();ctx.translate(c.x,c.y);ctx.rotate(c.h);ctx.fillStyle='rgba(255,255,255,.35)';ctx.beginPath();ctx.ellipse(0,0,24+Math.sin(G.t*6)*2,42,0,0,TAU);ctx.fill();
 ctx.save();ctx.scale(Math.max(.06,Math.abs(fl)),1);ctx.drawImage((fl>=0?(c.isP&&SP.jetP?SP.jetP:SP.jet[c.id]):SP.jetBot).c,-16,-34,32,68);ctx.restore();
 if(fl<0){const f=(AVATARS[G.avatar|0]||AVATARS[0]).face,w=Math.sin(G.t*8)*4;ctx.fillStyle=f.vest;ctx.beginPath();ctx.arc(22,8,6.5,0,TAU);ctx.fill();ctx.fillStyle=f.skin;ctx.beginPath();ctx.arc(22,7,4,0,TAU);ctx.fill();ctx.fillStyle=f.hair;ctx.beginPath();ctx.arc(22,5.5,3.6,Math.PI,TAU);ctx.fill();ctx.strokeStyle=f.skin;ctx.lineWidth=2.2;ctx.lineCap='round';ctx.beginPath();ctx.moveTo(16,8);ctx.lineTo(11,2+w);ctx.moveTo(28,8);ctx.lineTo(33,2-w);ctx.stroke();}
 ctx.restore();}
function label(x,y,t,s){""")
rep(" for(const c of cs){if(c.y<camTop-60||c.y>camTop+VH+60)continue;const sc=1+c.z*.32;",
    " for(const c of cs){if(c.y<camTop-60||c.y>camTop+VH+60)continue;if(c.capT>0){drawCapsized(c);continue;}const sc=1+c.z*.32;")
open(p,'w').write(s);print('ok')
