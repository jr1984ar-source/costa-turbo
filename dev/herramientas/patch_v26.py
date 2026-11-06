p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)

# ================= TRUCOS =================
rep("function startJump(c){c.airT=.45+c.v/620;c.air=c.airT;c.trick=0;",
    "function startJump(c){c.airT=.45+c.v/620;c.air=c.airT;c.trick=0;c._tr=[];c.flipT=0;c.supT=0;")
rep("c.airT=.95+c.v/420;c.air=c.airT;c.trick=0;Snd.jump();G.jumps++;",
    "c.airT=.95+c.v/420;c.air=c.airT;c.trick=0;c._tr=[];c.flipT=0;c.supT=0;Snd.jump();G.jumps++;")
# turbo en el aire = superman; derrape en el aire = mortal
rep("if(input.turbo){input.turbo=false;if(G.turbo>0&&P.boostT<=0&&P.crash<=0&&!(P.capT>0)&&!(P.stuckT>0)){",
    """if(input.turbo&&P.air>0&&P.z>.15){input.turbo=false;if(!(P.supT>0)&&!(P._tr||[]).includes('sup')){P.supT=.62;P.supDur=.62;(P._tr=P._tr||[]).push('sup');Snd.hiss({ft:'bandpass',f:700,f2:2600,t:.35,v:.16,a:.02});}}
  const drNow=!!input.drift;if(drNow&&!P._drPrev&&P.air>0&&P.z>.12&&!(P.flipT>0)&&!(P._tr||[]).includes('flip')){P.flipDur=Math.min(.85,Math.max(.5,P.air*.9));P.flipT=P.flipDur;(P._tr=P._tr||[]).push('flip');Snd.hiss({ft:'bandpass',f:500,f2:1800,t:.4,v:.16,a:.02});}P._drPrev=drNow;
  if(!G._trTip&&P.air>0&&!store.get('ct_tip_tr',false)){G._trTip=1;store.set('ct_tip_tr',true);msg('EN EL AIRE','DERRAPE = mortal · TURBO = superman','var(--pink)');}
  if(input.turbo){input.turbo=false;if(G.turbo>0&&P.boostT<=0&&P.crash<=0&&!(P.capT>0)&&!(P.stuckT>0)){""")
rep(" if(c.air>0){c.air-=dt;c.z=Math.sin(Math.PI*(1-c.air/c.airT));if(c.air<=0){c.z=0;c.air=0;splash(c.x,c.y+10,22,140);if(c.isP){Snd.land();G.shake=5;if(c.trick>c.airT*.55){G.score+=300;pop(c.x,c.y-40,'¡GIRO 360! +300','#33d6ff');}c.spin=0;}}}",
""" if(c.flipT>0)c.flipT=Math.max(0,c.flipT-dt);if(c.supT>0)c.supT=Math.max(0,c.supT-dt);
 if(c.air>0){c.air-=dt;c.z=Math.sin(Math.PI*(1-c.air/c.airT));if(c.air<=0){c.z=0;c.air=0;splash(c.x,c.y+10,22,140);
  if(c.isP){Snd.land();G.shake=5;const tr=c._tr||[];
   if(c.flipT>0||c.supT>0){c.flipT=0;c.supT=0;c._tr=[];c.inv=0;crash(c,'¡MAL ATERRIZAJE!');}
   else if(!G.demo){let pts0=0,names=[];if(c.trick>c.airT*.55){pts0+=300;names.push('360');}if(tr.includes('flip')){pts0+=500;names.push('MORTAL');}if(tr.includes('sup')){pts0+=400;names.push('SUPERMAN');}
    if(pts0){const combo=names.length>1;if(combo)pts0=Math.round(pts0*1.5);G.score+=pts0;G.tricks=(G.tricks||0)+names.length;pop(c.x,c.y-40,(combo?'¡COMBO! ':'¡')+names.join(' + ')+(combo?'':'!')+' +'+pts0,combo?'#ff3f8e':'#33d6ff');}}
   c._tr=[];c.spin=0;}}}""")
# dibujo: mortal (se ve la panza) y superman (piloto estirado)
rep("ctx.translate(c.x,c.y-c.z*8);ctx.rotate(c.h+c.spin);ctx.scale(sc,sc);if(c.inv>0&&!c.crash&&((G.t*12)|0)%2)ctx.globalAlpha=.45;ctx.drawImage((c.isP&&!G.demo&&SP.jetP?SP.jetP:SP.jet[c.id]).c,-16,-34,32,68);ctx.restore();",
"""ctx.translate(c.x,c.y-c.z*8);ctx.rotate(c.h+c.spin);ctx.scale(sc,sc);if(c.inv>0&&!c.crash&&((G.t*12)|0)%2)ctx.globalAlpha=.45;
  if(c.supT>0){const k=Math.sin((1-c.supT/(c.supDur||.62))*Math.PI),f=(AVATARS[G.avatar|0]||AVATARS[0]).face;ctx.save();ctx.translate(0,24+k*16);ctx.fillStyle='#1b2a4a';ctx.fillRect(-5,6,4,14*k+4);ctx.fillRect(1,6,4,14*k+4);ctx.fillStyle=f.vest;ctx.beginPath();ctx.ellipse(0,0,7,11,0,0,TAU);ctx.fill();ctx.fillStyle=f.skin;ctx.beginPath();ctx.arc(0,-12,4.5,0,TAU);ctx.fill();ctx.restore();}
  if(c.flipT>0){const ph=1-c.flipT/(c.flipDur||.8),sy=Math.cos(ph*TAU);ctx.scale(1,Math.abs(sy)<.08?.08*Math.sign(sy||1):sy);ctx.drawImage((sy<0?jetBot():(c.isP&&!G.demo&&SP.jetP?SP.jetP:SP.jet[c.id])).c,-16,-34,32,68);}
  else ctx.drawImage((c.isP&&!G.demo&&SP.jetP?SP.jetP:SP.jet[c.id]).c,-16,-34,32,68);ctx.restore();""")
rep(" if(!SP.jetBot||SP.jetBot.k!==K){const hc=playerSk().hull||'#ffffff';SP.jetBot=sprite(32,68,g=>{hullPath(g);g.fillStyle=mixc(hc,'#000000',.5);g.fill();g.strokeStyle='rgba(255,255,255,.28)';g.lineWidth=1.3;g.beginPath();g.moveTo(0,-26);g.lineTo(0,27);g.stroke();g.fillStyle='#2a2d33';g.fillRect(-4,23,8,7);});SP.jetBot.k=K;}",
    " jetBot();")
rep("function drawCapsized(c){","function jetBot(){if(!SP.jetBot||SP.jetBot.k!==K){const hc=playerSk().hull||'#ffffff';SP.jetBot=sprite(32,68,g=>{hullPath(g);g.fillStyle=mixc(hc,'#000000',.5);g.fill();g.strokeStyle='rgba(255,255,255,.28)';g.lineWidth=1.3;g.beginPath();g.moveTo(0,-26);g.lineTo(0,27);g.stroke();g.fillStyle='#2a2d33';g.fillRect(-4,23,8,7);});SP.jetBot.k=K;}return SP.jetBot;}\nfunction drawCapsized(c){")
rep(" SP.jetP=sprite(32,68,g=>drawJet(g,playerSk()));\n buildTrack();"," SP.jetP=sprite(32,68,g=>drawJet(g,playerSk()));SP.jetBot=null;\n buildTrack();")

# ================= ANIMALES (vuelta 2+) =================
rep(" if(Z.obj==='time'||Z.obj==='slalom'||Z.obj==='jumps'){zone.checks=",
""" if(lap>0){let au=900;while(au<len-500){const L=zone.shore(-au)+40,R=WG-30,k=r();
   if(k<.36){const n=2+((r()*2)|0),x=lerp(L+30,R-30,r());for(let i=0;i<n;i++)M.push({t:'dolphin',x:clamp(x+(i-n/2)*26,L,R),y:-au-i*40,vx:0,vy:-(95+r()*30),flash:r()*2,got:0});}
   else if(k<.7){const n=3+((r()*3)|0),x=lerp(L+30,R-30,r());for(let i=0;i<n;i++)add({t:'jelly',x:clamp(x+(r()-.5)*90,L,R),y:-au-(r()-.5)*120,ph:r()*6,hit:0});}
   else{const n=1+((r()*2)|0);for(let i=0;i<n;i++)add({t:'turtle',x:lerp(L+20,R-20,r()),y:-au-i*70,rot:(r()-.5)*1.4,ph:r()*6});}
   au+=650+r()*500;}}
 if(Z.obj==='time'||Z.obj==='slalom'||Z.obj==='jumps'){zone.checks=""")
rep("case 'float':return Math.hypot(o.x-x,o.y-y)<14+rad;}return false;}","case 'float':return Math.hypot(o.x-x,o.y-y)<14+rad;case 'turtle':return Math.hypot(o.x-x,o.y-y)<11+rad;}return false;}")
# delfines: turbo si pasas cerca ; medusas: frenan
rep(" // movers\n for(const o of Zn.movers){",
""" for(const o of Zn.movers){if(o.t!=='dolphin'||o.got||G.demo)continue;if(Math.hypot(o.x-P.x,o.y-P.y)<56&&P.air<=0){o.got=1;if(G.turbo<5){G.turbo++;turboUI();}Snd.pickup();msg('¡DELFINES!','+1 TURBO','var(--cyan)');pop(P.x,P.y-40,'+1 TURBO','#33d6ff');}}
 // movers
 for(const o of Zn.movers){""")
rep("   if(o.t==='tbuoy'&&!G.demo&&!c.fin&&c.prevY>o.y&&c.y<=o.y){",
"""   if(o.t==='jelly'){if(c.isP&&!G.demo&&!o.hit&&c.z<.3&&Math.hypot(o.x-c.x,o.y-c.y)<20){o.hit=1;c.v*=.45;c.boostT=0;Snd.miss();G.shake=3;pop(c.x,c.y-36,'¡MEDUSA!','#ff3f8e');}continue;}
   if(o.t==='tbuoy'&&!G.demo&&!c.fin&&c.prevY>o.y&&c.y<=o.y){""")
rep("if(o.t==='coin'||o.t==='check'||o.t==='finish'||o.t==='ramp'||o.t==='can'||o.t==='fuel'||o.t==='gate'||o.t==='island'||o.t==='pass'||o.t==='tbuoy')continue;const w=",
    "if(o.t==='coin'||o.t==='check'||o.t==='finish'||o.t==='ramp'||o.t==='can'||o.t==='fuel'||o.t==='gate'||o.t==='island'||o.t==='pass'||o.t==='tbuoy'||o.t==='jelly')continue;const w=")
# dibujo animales
rep(" case 'tbuoy':{"," case 'dolphin':{const cyc=(o.flash%2.4),up=cyc<1,k=up?Math.sin(cyc*Math.PI):0;ctx.save();ctx.translate(o.x,o.y);\n  if(!up){ctx.globalAlpha=.28;ctx.fillStyle='#0a2c55';ctx.beginPath();ctx.ellipse(0,0,6,17,0,0,TAU);ctx.fill();ctx.restore();return;}\n  ctx.fillStyle='rgba(0,20,50,.25)';ctx.beginPath();ctx.ellipse(4+k*10,6+k*12,6,16,0,0,TAU);ctx.fill();ctx.translate(0,-k*10);ctx.scale(1+k*.25,1+k*.25);\n  ctx.fillStyle='#5f7f9c';ctx.beginPath();ctx.ellipse(0,0,6.5,18,0,0,TAU);ctx.fill();ctx.fillStyle='#93acc2';ctx.beginPath();ctx.ellipse(-1.5,-2,3,13,0,0,TAU);ctx.fill();\n  ctx.fillStyle='#4a6782';ctx.beginPath();ctx.moveTo(-9,4);ctx.lineTo(0,1);ctx.lineTo(9,4);ctx.lineTo(0,7);ctx.closePath();ctx.fill();ctx.beginPath();ctx.moveTo(-7,20);ctx.lineTo(0,15);ctx.lineTo(7,20);ctx.lineTo(0,17);ctx.closePath();ctx.fill();ctx.beginPath();ctx.ellipse(0,-20,2.2,4,0,0,TAU);ctx.fill();\n  if(k>.15&&k<.5)for(let i=0;i<6;i++){ctx.globalAlpha=.7;ctx.drawImage(SP.dot.c,(i-3)*4-3,18+Math.random()*4,6,6);}ctx.globalAlpha=1;ctx.restore();}return;\n case 'jelly':{const p=1+Math.sin(t*3+o.ph)*.12;ctx.save();ctx.translate(o.x,o.y);ctx.strokeStyle='rgba(255,140,200,.55)';ctx.lineWidth=1.2;for(let i=0;i<6;i++){const a=i/6*TAU;ctx.beginPath();ctx.moveTo(Math.cos(a)*6,Math.sin(a)*6);ctx.quadraticCurveTo(Math.cos(a+.6)*14,Math.sin(a+.6)*14,Math.cos(a)*(16+Math.sin(t*4+i)*2),Math.sin(a)*(16+Math.sin(t*4+i)*2));ctx.stroke();}\n  const gg=ctx.createRadialGradient(-2,-2,1,0,0,10*p);gg.addColorStop(0,'rgba(255,230,245,.95)');gg.addColorStop(.6,'rgba(255,120,190,.75)');gg.addColorStop(1,'rgba(255,90,170,.25)');ctx.fillStyle=gg;ctx.beginPath();ctx.arc(0,0,10*p,0,TAU);ctx.fill();ctx.strokeStyle='rgba(255,255,255,.6)';ctx.beginPath();ctx.arc(0,0,5*p,0,TAU);ctx.stroke();ctx.restore();}return;\n case 'turtle':{ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.rot+Math.sin(t*.8+o.ph)*.1);const sw=Math.sin(t*3+o.ph)*.35;ctx.fillStyle='rgba(0,20,50,.25)';ctx.beginPath();ctx.ellipse(3,4,11,14,0,0,TAU);ctx.fill();\n  ctx.fillStyle='#7aa35a';for(const[sx,sy,a]of[[-1,-1,-.6-sw],[1,-1,.6+sw],[-1,1,-2.4+sw*.6],[1,1,2.4-sw*.6]]){ctx.save();ctx.translate(sx*7,sy*6);ctx.rotate(a);ctx.beginPath();ctx.ellipse(0,-5,3,7,0,0,TAU);ctx.fill();ctx.restore();}\n  ctx.beginPath();ctx.ellipse(0,-14,4,5,0,0,TAU);ctx.fill();ctx.fillStyle='#4f7a3a';ctx.beginPath();ctx.ellipse(0,0,10,12,0,0,TAU);ctx.fill();ctx.strokeStyle='#c9d98a';ctx.lineWidth=1;for(const[a,b]of[[-4,-5],[4,-5],[-5,3],[5,3],[0,-1]]){ctx.beginPath();ctx.arc(a,b,3,0,TAU);ctx.stroke();}ctx.restore();}return;\n case 'tbuoy':{")
open(p,'w').write(s);print('ok')
