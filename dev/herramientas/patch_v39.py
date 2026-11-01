p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
build=open('circ_build.js').read();draw=open('circ_draw.js').read()
# 1. sustituir CIRCS + buildCircuit
i=s.find('const CIRCS={');j=s.find('function circProg(')
assert 0<i<j
s=s[:i]+build+'\n'+s[j:]
# 2. sustituir drawCircuit
i=s.find('function drawCircuit(Zn){');j=s.find('\nfunction buildZone(',i)
assert 0<i<j
s=s[:i]+draw.rstrip('\n')+s[j:]
# 3. parrilla más ancha
rep("const row=Math.floor(j/2),col=j%2,sd=150-row*48,i=((Math.round(sd/C.step))%C.n+C.n)%C.n,lane=(col?1:-1)*44;",
    "const row=Math.floor(j/2),col=j%2,sd=170-row*56,i=((Math.round(sd/C.step))%C.n+C.n)%C.n,lane=(col?1:-1)*64;")
# 4. tierra sólida en circuitos
rep("function circTick(dt){const C=G.zone.circ;\n for(const c of crafts()){circProg(c);",
    "function circTick(dt){const C=G.zone.circ,LDS=G.zone.lands;\n for(const c of crafts()){circProg(c);\n  if(LDS&&landIn(LDS,c.x,c.y)){if(c._lx!=null){c.x=c._lx;c.y=c._ly;}c.v*=.3;c.boostT=0;if(c.isP&&!G.demo&&!(c._bumpT>0)){c._bumpT=.7;Snd.bump();G.shake=5;pop(c.x,c.y-36,'¡TIERRA!','#ff4757');}}else{c._lx=c.x;c._ly=c.y;}if(c._bumpT>0)c._bumpT-=dt;")
# 5. colisiones: rampas giradas, decorado fuera
rep("  for(let i=s;i<Zn.objs.length;i++){const o=Zn.objs[i];if(o.y>c.y+170)break;\n   if(o.t==='heart')",
    "  for(let i=s;i<Zn.objs.length;i++){const o=Zn.objs[i];if(o.y>c.y+170)break;\n   if(o.t==='cdeco'||o.t==='cbld'||o.t==='cbuoy'||o.t==='carrow'||o.t==='cline'||o.t==='cban')continue;\n   if(o.t==='cramp'){const sa=Math.sin(o.h),ca=Math.cos(o.h),dx=c.x-o.x,dy=c.y-o.y,al=dx*sa-dy*ca,lt=dx*ca+dy*sa,pk='_r'+c.id,pa=o[pk];o[pk]=al;if(pa!=null&&pa<0&&al>=0&&Math.abs(lt)<o.w/2&&c.air<=0&&c.v>110&&c.crash<=0){startJump(c);if(c.isP&&!G.demo){const b=100+Math.round(c.v/4);G.score+=b;pop(c.x,c.y-40,'¡SALTO! +'+b,'#ffc93c');}}continue;}\n   if(o.t==='heart')")
rep("case 'turtle':return Math.hypot(o.x-x,o.y-y)<11+rad;}return false;}",
    "case 'turtle':return Math.hypot(o.x-x,o.y-y)<11+rad;case 'cturn':return Math.hypot(o.x-x,o.y-y)<15+rad;case 'cboat':{const dx=x-o.x,dy=y-o.y,ca=Math.cos(o.r),sa=Math.sin(o.r),lx=dx*ca+dy*sa,ly=-dx*sa+dy*ca;return Math.abs(lx)<o.bw/2+rad*.6&&Math.abs(ly)<o.bl/2+rad*.6;}}return false;}")
rep("crash(c,{rock:'¡ROCA!',pig:'¡OINK!',surfer:'¡SURFISTA!',turtle:'¡TORTUGA!'}[o.t]||'¡PUM!')",
    "crash(c,{rock:'¡ROCA!',pig:'¡OINK!',surfer:'¡SURFISTA!',turtle:'¡TORTUGA!',cturn:'¡BOYA!',cboat:'¡BARCO!'}[o.t]||'¡PUM!')")
# 6. dibujo de objetos nuevos
i=s.find(" case 'cbuoy':");j=s.find(" case 'carrow':",i);assert 0<i<j
s=s[:i]+""" case 'cbuoy':{const b=Math.sin(t*3+o.ph)*.7,sp=cBuoySpr(o.c);ctx.fillStyle='rgba(0,20,50,.25)';ctx.beginPath();ctx.ellipse(o.x+3,o.y+4,8.5,5.5,0,0,TAU);ctx.fill();ctx.strokeStyle='rgba(255,255,255,.3)';ctx.lineWidth=1;ctx.beginPath();ctx.arc(o.x,o.y,11+Math.sin(t*3+o.ph)*1.5,0,TAU);ctx.stroke();ctx.drawImage(sp.c,o.x-12,o.y-12+b,24,24);}return;
 case 'cturn':{const b=Math.sin(t*2.4+o.ph)*.9,sp=cTurnSpr();ctx.strokeStyle='rgba(255,255,255,.4)';ctx.lineWidth=1.4;ctx.beginPath();ctx.arc(o.x,o.y,21+Math.sin(t*3+o.ph)*2,0,TAU);ctx.stroke();ctx.fillStyle='rgba(0,20,50,.3)';ctx.beginPath();ctx.ellipse(o.x+5,o.y+7,17,12,0,0,TAU);ctx.fill();ctx.drawImage(sp.c,o.x-22,o.y-22+b,44,44);
  ctx.save();ctx.translate(o.x,o.y+b);ctx.rotate(G.camA||0);ctx.fillStyle='#ffffff';ctx.font='800 13px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(String(o.n),0,1);
  ctx.strokeStyle='#e9edf2';ctx.lineWidth=1.6;ctx.beginPath();ctx.moveTo(6,-8);ctx.lineTo(10,-30);ctx.stroke();const w=Math.sin(t*7+o.ph)*2.2;ctx.fillStyle='#ffffff';ctx.beginPath();ctx.moveTo(10,-30);ctx.quadraticCurveTo(17,-29+w,24,-27+w*1.3);ctx.lineTo(22,-20+w);ctx.quadraticCurveTo(16,-21+w*.6,9.5,-21);ctx.closePath();ctx.fill();ctx.fillStyle='#e3202b';ctx.beginPath();ctx.moveTo(10,-30);ctx.quadraticCurveTo(17,-29+w,24,-27+w*1.3);ctx.lineTo(23,-23.5+w*1.1);ctx.quadraticCurveTo(16,-25+w*.8,9.8,-25.5);ctx.closePath();ctx.fill();ctx.restore();}return;
 case 'cramp':{ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);drawObj({t:'ramp',x:0,y:0,w:o.w,kick:1});ctx.restore();}return;
 case 'cboat':{const sp=cBoatSpr(o.kind),bob=Math.sin(t*1.6+(o.s%7))*.04;ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.r+bob);ctx.fillStyle='rgba(0,20,50,.28)';ctx.beginPath();ctx.ellipse(4,5,o.bw*.55,o.bl*.52,0,0,TAU);ctx.fill();
  if(!o.moored){ctx.strokeStyle='rgba(255,255,255,.3)';ctx.lineWidth=1.2;ctx.beginPath();ctx.ellipse(0,0,o.bw*.7+Math.sin(t*2+o.s)*1.2,o.bl*.58,0,0,TAU);ctx.stroke();}
  ctx.drawImage(sp.c,-sp.w/2,-sp.h/2,sp.w,sp.h);const q=hash2(o.s,3,1);
  for(let k=0;k<o.pp.length;k++){if(o.moored&&k>1)break;const[px,py]=o.pp[k],cc=o.kind==='resc'?'#e3202b':['#ff3b4f','#ffd21a','#33a3ff','#ffffff','#7be35a','#ff7a1a','#ff3f8e'][((q*97+k*3)|0)%7],sk=['#f1c9a5','#e0b08a','#c98c62','#8d5a3b'][((q*31+k)|0)%4];ctx.fillStyle=cc;ctx.beginPath();ctx.arc(px,py,2.5,0,TAU);ctx.fill();ctx.fillStyle=sk;ctx.beginPath();ctx.arc(px,py-.6,1.7,0,TAU);ctx.fill();
   if(!o.moored&&o.kind!=='resc'&&Math.sin(t*7+k*2+q*9)>.3){ctx.strokeStyle=sk;ctx.lineWidth=1.1;ctx.beginPath();ctx.moveTo(px+1.5,py);ctx.lineTo(px+4,py-3-Math.sin(t*12+k)*1.5);ctx.stroke();}}
  if(o.kind==='resc'){const on=Math.sin(t*10)>0;ctx.fillStyle=on?'#4aa3ff':'#1b3a8a';ctx.beginPath();ctx.arc(0,-6,2.2,0,TAU);ctx.fill();if(on){ctx.fillStyle='rgba(74,163,255,.25)';ctx.beginPath();ctx.arc(0,-6,8,0,TAU);ctx.fill();}}
  ctx.restore();}return;
 case 'cban':{ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);const L=o.len,cols=[['#e3202b','#ffffff'],['#ffd21a','#13285e'],['#1e5eff','#ffffff'],['#ff3f8e','#ffffff']][o.k%4];ctx.fillStyle='rgba(0,20,50,.25)';ctx.beginPath();ctx.roundRect(-2,-L/2+4,10,L,5);ctx.fill();ctx.fillStyle=cols[0];ctx.beginPath();ctx.roundRect(-5,-L/2,10,L,5);ctx.fill();ctx.fillStyle='rgba(255,255,255,.3)';ctx.fillRect(-4,-L/2+4,2,L-8);ctx.rotate(-Math.PI/2);ctx.fillStyle=cols[1];ctx.font='800 7.5px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(o.txt,0,.5);ctx.restore();}return;
 case 'cline':{ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);const w=o.w,n=Math.floor(w/10);for(let i=0;i<n;i++)for(let k=0;k<2;k++){ctx.fillStyle=(i+k)%2?'#ffffff':'#111111';ctx.fillRect(-n*5+i*10,-10+k*10,10,10);}ctx.restore();}return;
"""+s[j:]
i=s.find(" case 'cbld':");j=s.find(" case 'cdeco':",i);assert 0<i<j
s=s[:i]+""" case 'cbld':{ctx.save();ctx.translate(o.x,o.y);if(o.rot!=null)ctx.rotate(o.rot);ctx.fillStyle='rgba(0,0,0,.2)';ctx.fillRect(-o.w/2+5,-o.h/2+5,o.w,o.h);ctx.fillStyle=o.c;ctx.fillRect(-o.w/2,-o.h/2,o.w,o.h);
  if(o.roof){ctx.fillStyle='#c4683c';ctx.fillRect(-o.w/2,-o.h/2,o.w,o.h/2);ctx.fillStyle='#a9552f';ctx.fillRect(-o.w/2,0,o.w,o.h/2);}else{ctx.fillStyle='rgba(0,0,0,.07)';ctx.fillRect(-o.w/2+3,-o.h/2+3,o.w-6,o.h-6);ctx.fillStyle='#c9ced6';ctx.fillRect(o.w/2-9,-o.h/2+4,5,4);}
  if(o.pool){ctx.fillStyle='#4fd1e8';ctx.fillRect(-o.w/2+4,-o.h/2+4,o.w*.4,o.h*.3);}ctx.strokeStyle='rgba(0,0,0,.12)';ctx.lineWidth=1;ctx.strokeRect(-o.w/2,-o.h/2,o.w,o.h);ctx.restore();}return;
"""+s[j:]
# 7. cámara con zoom y recorte lateral, capa de arriba
rep("if(CIRC){const RR=Math.hypot(VW*.5,VH*.72)+80;","if(CIRC){const RR=Math.hypot(VW*.5/CZ,VH*.72/CZ)+80;")
rep("ctx.translate(sv[0]/2+sx,sv[1]*.7+sy);ctx.rotate(-(G.camA||0));","ctx.translate(sv[0]/2+sx,sv[1]*.7+sy);ctx.scale(CZ,CZ);ctx.rotate(-(G.camA||0));")
rep("if(o.y>camTop+VH+170)break;if(o.t!=='island'&&o.t!=='pass'&&o.t!=='nozone')drawObj(o);}",
    "if(o.y>camTop+VH+170)break;if(VIS&&!VIS(o.x,o.y,90))continue;if(o.t!=='island'&&o.t!=='pass'&&o.t!=='nozone')drawObj(o);}")
rep(" // particles\n"," if(CIRC)drawCircTop(Zn);\n // particles\n")
# 8. mini-mapa
rep('<div class="track" id="track"></div>','<div class="track" id="track"></div><canvas class="cmap" id="cmap" hidden></canvas>')
rep(".track{position:absolute;",".cmap{position:absolute;right:max(8px,env(safe-area-inset-right,0px));top:110px;width:112px;height:112px;border-radius:14px;background:rgba(8,22,48,.5);border:1px solid rgba(255,255,255,.2);box-shadow:0 4px 12px rgba(0,10,30,.25)}\n.track{position:absolute;")
rep("function buildTrack(){const tr=$('#track');","function buildTrack(){{const isC=!!G.zone.circ;$('#track').hidden=isC;$('#cmap').hidden=!isC;G._mm=null;if(isC)buildMiniMap();}const tr=$('#track');")
rep("function hudTick(){const Zn=G.zone,Z=Zn.Z,P=G.P;","function hudTick(){const Zn=G.zone,Z=Zn.Z,P=G.P;if(Zn.circ)drawMiniMap();")
rep(" // deep water\n"," const VIS=CIRC?(()=>{const a=G.camA||0,ca=Math.cos(a),sa=Math.sin(a),hw=sv[0]/2/CZ,ht=sv[1]*.7/CZ,hb=sv[1]*.3/CZ,px=G.P.x,py=G.P.y;return(x,y,m)=>{const dx=x-px,dy=y-py,lx=dx*ca+dy*sa,ly=-dx*sa+dy*ca;return lx>-hw-m&&lx<hw+m&&ly>-ht-m&&ly<hb+m;};})():null;G._vis=VIS;\n // deep water\n")
rep("x<camX+VW+ts;x+=ts)ctx.drawImage(SP.tile.c,x,y,ts,ts);","x<camX+VW+ts;x+=ts)if(!VIS||VIS(x+128,y+128,182))ctx.drawImage(SP.tile.c,x,y,ts,ts);",2)
rep("updateCraft(c,dt,c.fin?{turn:0,thr:true}:aiCtl(c,dt));","updateCraft(c,dt,c.fin?(Zn.circ?Object.assign(aiCirc(c,dt),{thr:c.v<c.st.maxV*.45}):{turn:0,thr:true}):aiCtl(c,dt));")
rep("const APP_VER=38;","const APP_VER=39;")
open(p,'w').write(s);print('ok')
