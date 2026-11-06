p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)

# ================= ZONAS =================
rep("{name:'LA FINAL',","""{name:'FORMENTERA',obj:'race3',goal:'Termina entre los 3 primeros hasta la punta de Ses Illetes. Agua transparente, muchos barcos fondeados y praderas de posidonia que te frenan.',len:16000,riv:5,bar:null,theme:'form',tod:'tropical',skill:.9,form:1,shallowW:260,finish:'SES ILLETES'},
 {name:'BAHAMAS',obj:'race3',goal:'Termina entre los 3 primeros entre los cayos. Esquiva los cerdos nadando, las mantarrayas y los tiburones nodriza.',len:16000,riv:5,bar:null,theme:'open',tod:'tropical',skill:.9,bah:1,cays:1,finish:'EXUMAS'},
 {name:'AUSTRALIA',obj:'jumps',needJ:8,goal:'Haz 8 saltos en las olas de surf y llega a tiempo. No choques con los surfistas y cuidado con el coral y los cocodrilos.',len:15000,riv:0,bar:null,theme:'beach',tod:'morning',pace:200,aus:1,giant:[.3,.6,.88]},
 {name:'LA FINAL',""")
rep("let best=Math.max(0,Math.min(12,","let best=Math.max(0,Math.min(15,")
rep("const kindOf=k=>{k=Math.max(0,k);if(Z.theme==='trenc')return 'beach';","const kindOf=k=>{k=Math.max(0,k);if(Z.theme==='trenc'||Z.theme==='form')return 'beach';")
rep("kind==='beach'?(Z.theme==='trenc'?64+5*n1(u/700):","kind==='beach'?(Z.theme==='trenc'||Z.theme==='form'?64+5*n1(u/700):")
rep("Z.theme==='trenc'?2000:","Z.theme==='trenc'||Z.theme==='form'?2000:")
rep("if(Z.giant){for(const f of[.2,.34,.48,.62,.85,.88,.91])","if(Z.giant){for(const f of(Array.isArray(Z.giant)?Z.giant:[.2,.34,.48,.62,.85,.88,.91]))")
rep(" if(Z.island)island(Math.round(len*.45),58,220);",""" if(Z.cays){for(let cu=1300;cu<len-900;cu+=1250+r()*500){const L=zone.shore(-cu),rx=34+r()*16,ry=70+r()*50,x=lerp(L+rx+80,RX-rx-80,r());add({t:'island',x,y:-cu,rx,ry,seed:(r()*1e6)|0,theme:'cay'});resv.push([cu-ry-150,cu+ry+150]);}}
 if(Z.island)island(Math.round(len*.45),58,220);""")
rep("const wPat=Z.obj==='slalom'?","const wPat=Z.form?{coins:3,boat:2.6,yacht:1.2,rocks:.3,ramp:.8,kayak:.5,posi:2}:Z.bah?{coins:3,pig:2.2,ray:1,nurse:.8,ramp:.9,rocks:.3,yacht:.4}:Z.aus?{coins:3,ramp:6,surfer:2,coral:1.4,croc:.8,rocks:.4}:Z.obj==='slalom'?")
rep("  else if(k==='patrol'){","""  else if(k==='posi'){add({t:'posi',x:lerp(L+30,R-30,r()),y:-u,rx:30+r()*26,ry:50+r()*40,s:(r()*1e6)|0});u+=180;}
  else if(k==='coral'){add({t:'coral',x:lerp(L+30,R-30,r()),y:-u,rx:26+r()*20,ry:34+r()*26,s:(r()*1e6)|0});u+=170;}
  else if(k==='pig'){const n=1+((r()*3)|0),x=lerp(L+30,R-30,r());for(let i=0;i<n;i++)add({t:'pig',x:clamp(x+(i-n/2)*30,L+10,R-10),y:-u-(r()-.5)*40,ph:r()*6});u+=170;}
  else if(k==='surfer'){add({t:'surfer',x:lerp(L+30,R-30,r()),y:-u,rot:(r()-.5)*.6,ph:r()*6,c:['#ffd21a','#ff3f8e','#33d6ff','#7be35a'][(r()*4)|0]});u+=150;}
  else if(k==='ray'){M.push({t:'ray',x:r()<.5?L+10:R-10,y:-u,vx:(r()<.5?1:-1)*(30+r()*20),vy:0,flash:0});u+=150;}
  else if(k==='nurse'){M.push({t:'nurse',x:lerp(L+30,R-30,r()),y:-u,vx:(r()<.5?1:-1)*(18+r()*14),vy:0,flash:0});u+=150;}
  else if(k==='croc'){M.push({t:'croc',x:lerp(L+30,R-30,r()),y:-u,vx:(r()<.5?1:-1)*(16+r()*12),vy:0,flash:0});u+=150;}
  else if(k==='patrol'){""")
rep("for(const o of Zn.movers){if(o.t==='kayak'){","for(const o of Zn.movers){if(o.t==='kayak'||o.t==='ray'||o.t==='nurse'||o.t==='croc'){o.flash=(o.flash||0)+dt;")
rep("case 'float':return Math.hypot(o.x-x,o.y-y)<14+rad;","case 'float':return Math.hypot(o.x-x,o.y-y)<14+rad;case 'pig':return Math.hypot(o.x-x,o.y-y)<11+rad;case 'surfer':return Math.abs(o.x-x)<8+rad&&Math.abs(o.y-y)<18+rad*.5;case 'ray':return Math.abs(o.x-x)<18+rad*.5&&Math.abs(o.y-y)<11+rad*.5;case 'nurse':return Math.abs(o.x-x)<24+rad*.5&&Math.abs(o.y-y)<7+rad;case 'croc':return Math.abs(o.x-x)<26+rad*.5&&Math.abs(o.y-y)<8+rad;")
rep("crash(c,o.t==='rock'?'¡ROCA!':'¡PUM!')","crash(c,{rock:'¡ROCA!',pig:'¡OINK!',surfer:'¡SURFISTA!',turtle:'¡TORTUGA!'}[o.t]||'¡PUM!')")
rep("crash(c,o.t==='patrol'?'¡CHOQUE!':'¡PUM!')","crash(c,{patrol:'¡CHOQUE!',ray:'¡MANTARRAYA!',nurse:'¡TIBURÓN!',croc:'¡COCODRILO!'}[o.t]||'¡PUM!')")
rep("   if(o.t==='jelly'){","   if(o.t==='posi'||o.t==='coral'){const dx=(c.x-o.x)/o.rx,dy=(c.y-o.y)/o.ry;if(c.z<.3&&dx*dx+dy*dy<1){c.v*=1-(o.t==='coral'?2.4:1.4)*dt;if(c.isP&&!G.demo&&!o.hit){o.hit=1;pop(c.x,c.y-36,o.t==='coral'?'¡CORAL!':'¡POSIDONIA!',o.t==='coral'?'#ff7a1a':'#7be35a');}}continue;}\n   if(o.t==='jelly'){")
# canguros en la playa (Australia)
rep("else if(kd==='beach'){const v=dr();","else if(kd==='beach'&&Z.aus&&dr()<.1){D.push({t:'roo',x:sx-26-dr()*50,y,s:(dr()*1e6)|0});}\n  else if(kd==='beach'){const v=dr();")
rep("function drawDeco(g,d){const q=rng(d.s||((d.x*31+d.y*17)|0));","""function drawDeco(g,d){const q=rng(d.s||((d.x*31+d.y*17)|0));
 if(d.t==='roo'){g.save();g.translate(d.x,d.y);g.rotate((q()-.5)*1.2);g.fillStyle='rgba(60,40,20,.2)';g.beginPath();g.ellipse(3,3,6,10,0,0,TAU);g.fill();g.fillStyle='#a8663a';g.beginPath();g.ellipse(0,0,5.5,9,0,0,TAU);g.fill();g.beginPath();g.ellipse(0,-9,3.2,4.2,0,0,TAU);g.fill();g.strokeStyle='#8f532c';g.lineWidth=2.6;g.lineCap='round';g.beginPath();g.moveTo(0,8);g.quadraticCurveTo(2,15,0,20);g.stroke();g.fillStyle='#8f532c';g.beginPath();g.ellipse(-2,-13,1.2,3,-.3,0,TAU);g.ellipse(2,-13,1.2,3,.3,0,TAU);g.fill();g.restore();return;}""")
# dibujo de objetos nuevos
rep(" case 'dolphin':{",""" case 'posi':{const q=rng(o.s);ctx.save();ctx.translate(o.x,o.y);ctx.fillStyle='rgba(20,90,60,.35)';ctx.beginPath();for(let i=0;i<=18;i++){const a=i/18*TAU,k=.8+q()*.3;i?ctx.lineTo(Math.cos(a)*o.rx*k,Math.sin(a)*o.ry*k):ctx.moveTo(Math.cos(a)*o.rx*k,Math.sin(a)*o.ry*k);}ctx.closePath();ctx.fill();
  ctx.strokeStyle='rgba(40,130,80,.55)';ctx.lineWidth=1.3;ctx.lineCap='round';for(let i=0;i<26;i++){const a=q()*TAU,d=Math.sqrt(q())*.8,x=Math.cos(a)*o.rx*d,y=Math.sin(a)*o.ry*d,sw=Math.sin(t*1.5+i)*2;ctx.beginPath();ctx.moveTo(x,y+4);ctx.quadraticCurveTo(x+sw,y,x+sw*1.5,y-5);ctx.stroke();}ctx.restore();}return;
 case 'coral':{const q=rng(o.s);ctx.save();ctx.translate(o.x,o.y);ctx.fillStyle='rgba(140,240,232,.35)';ctx.beginPath();ctx.ellipse(0,0,o.rx+8,o.ry+8,0,0,TAU);ctx.fill();const cols=['rgba(255,110,150,.75)','rgba(255,160,60,.75)','rgba(170,110,255,.7)','rgba(255,230,120,.75)','rgba(90,200,160,.7)'];
  for(let i=0;i<16;i++){const a=q()*TAU,d=Math.sqrt(q())*.85,x=Math.cos(a)*o.rx*d,y=Math.sin(a)*o.ry*d,r=4+q()*6;ctx.fillStyle=cols[(q()*5)|0];ctx.beginPath();for(let k=0;k<7;k++){const b=k/7*TAU,rr=r*(.6+q()*.5);k?ctx.lineTo(x+Math.cos(b)*rr,y+Math.sin(b)*rr):ctx.moveTo(x+Math.cos(b)*rr,y+Math.sin(b)*rr);}ctx.closePath();ctx.fill();}ctx.restore();}return;
 case 'pig':{const b=Math.sin(t*3+o.ph);ctx.save();ctx.translate(o.x,o.y);ctx.strokeStyle='rgba(255,255,255,.55)';ctx.lineWidth=1.5;ctx.beginPath();ctx.ellipse(0,2,14+b,16+b,0,0,TAU);ctx.stroke();ctx.fillStyle='#f4a6b8';ctx.beginPath();ctx.ellipse(0,3,8.5,10,0,0,TAU);ctx.fill();ctx.beginPath();ctx.arc(0,-8,6,0,TAU);ctx.fill();
  ctx.fillStyle='#e88aa0';ctx.beginPath();ctx.ellipse(-4.5,-12,2.2,3.4,-.5,0,TAU);ctx.ellipse(4.5,-12,2.2,3.4,.5,0,TAU);ctx.fill();ctx.fillStyle='#e07890';ctx.beginPath();ctx.ellipse(0,-12.5,3,2.2,0,0,TAU);ctx.fill();ctx.fillStyle='#5a2a34';ctx.beginPath();ctx.arc(-1,-12.5,.7,0,TAU);ctx.arc(1,-12.5,.7,0,TAU);ctx.arc(-2.6,-8,.9,0,TAU);ctx.arc(2.6,-8,.9,0,TAU);ctx.fill();ctx.restore();}return;
 case 'surfer':{const b=Math.sin(t*2+o.ph)*.08;ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.rot+b);ctx.fillStyle='rgba(255,255,255,.6)';ctx.beginPath();ctx.ellipse(0,6,9,24,0,0,TAU);ctx.fill();ctx.fillStyle=o.c||'#ffd21a';ctx.beginPath();ctx.ellipse(0,0,5.5,20,0,0,TAU);ctx.fill();ctx.strokeStyle='rgba(0,0,0,.25)';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(0,-18);ctx.lineTo(0,18);ctx.stroke();
  ctx.fillStyle='#1b2a4a';ctx.beginPath();ctx.ellipse(-3,2,2,3.5,0,0,TAU);ctx.ellipse(3,5,2,3.5,0,0,TAU);ctx.fill();ctx.fillStyle='#e8b48c';ctx.beginPath();ctx.ellipse(0,0,5,3.4,0,0,TAU);ctx.fill();ctx.strokeStyle='#e8b48c';ctx.lineWidth=2;ctx.lineCap='round';ctx.beginPath();ctx.moveTo(-4,0);ctx.lineTo(-10,-3);ctx.moveTo(4,0);ctx.lineTo(10,3);ctx.stroke();ctx.fillStyle='#5a3218';ctx.beginPath();ctx.arc(0,-2,2.6,0,TAU);ctx.fill();ctx.restore();}return;
 case 'ray':{const f=Math.sin(o.flash*4)*.25,d=o.vx>0?1:-1;ctx.save();ctx.translate(o.x,o.y);ctx.scale(d,1);ctx.globalAlpha=.75;ctx.fillStyle='#2f3e52';ctx.beginPath();ctx.moveTo(14,0);ctx.quadraticCurveTo(0,-14-f*8,-10,-2);ctx.lineTo(-10,2);ctx.quadraticCurveTo(0,14+f*8,14,0);ctx.closePath();ctx.fill();ctx.strokeStyle='#2f3e52';ctx.lineWidth=1.4;ctx.beginPath();ctx.moveTo(-10,0);ctx.lineTo(-26,Math.sin(o.flash*3)*3);ctx.stroke();ctx.fillStyle='rgba(255,255,255,.3)';ctx.beginPath();ctx.arc(8,-2,1.2,0,TAU);ctx.arc(8,2,1.2,0,TAU);ctx.fill();ctx.restore();}return;
 case 'nurse':{const w=Math.sin(o.flash*3)*.15,d=o.vx>0?1:-1;ctx.save();ctx.translate(o.x,o.y);ctx.scale(d,1);ctx.rotate(w*.3);ctx.globalAlpha=.85;ctx.fillStyle='#8a7a5c';ctx.beginPath();ctx.ellipse(0,0,22,5.5,0,0,TAU);ctx.fill();ctx.beginPath();ctx.moveTo(-18,0);ctx.lineTo(-30,-6+w*20);ctx.lineTo(-28,5);ctx.closePath();ctx.fill();ctx.beginPath();ctx.moveTo(4,0);ctx.lineTo(-2,-11);ctx.lineTo(-6,0);ctx.moveTo(4,0);ctx.lineTo(-2,11);ctx.lineTo(-6,0);ctx.fill();ctx.fillStyle='#6d5f46';ctx.beginPath();ctx.moveTo(-4,-2);ctx.lineTo(-9,-8);ctx.lineTo(-12,-2);ctx.fill();ctx.restore();}return;
 case 'croc':{const w=Math.sin(o.flash*2.5)*.12,d=o.vx>0?1:-1;ctx.save();ctx.translate(o.x,o.y);ctx.scale(d,1);ctx.fillStyle='rgba(0,20,30,.25)';ctx.beginPath();ctx.ellipse(2,3,28,7,0,0,TAU);ctx.fill();ctx.fillStyle='#4a5a2c';ctx.beginPath();ctx.moveTo(26,0);ctx.lineTo(16,-4);ctx.lineTo(-10,-6);ctx.quadraticCurveTo(-24,-3,-34,w*20);ctx.quadraticCurveTo(-24,3,-10,6);ctx.lineTo(16,4);ctx.closePath();ctx.fill();
  ctx.fillStyle='#5f7236';for(let i=0;i<6;i++){ctx.beginPath();ctx.arc(-8+i*4,0,1.4,0,TAU);ctx.fill();}ctx.fillStyle='#c9d36a';ctx.beginPath();ctx.arc(14,-3.5,1.6,0,TAU);ctx.arc(14,3.5,1.6,0,TAU);ctx.fill();ctx.restore();}return;
 case 'dolphin':{""")
# isla tipo cayo: sin casas
rep("for(let i=0;i<3;i++){const x=(q()-.5)*o.rx*.9,y=(q()-.5)*o.ry*1.2;g.fillStyle='#fbfaf6';","for(let i=0;i<(o.theme==='cay'?0:3);i++){const x=(q()-.5)*o.rx*.9,y=(q()-.5)*o.ry*1.2;g.fillStyle='#fbfaf6';")

# ================= PORTADAS =================
rep(" {tag:'GANA A EL TIBURÓN',",""" {tag:'CARRERA · TOP 3',sky:['#1ea6f5','#e6f8ff'],sea:['#a6f5ee','#0aa0d8'],sun:[90,22,'#ffffff'],land:'form'},
 {tag:'CARRERA · TOP 3',sky:['#1b9cf0','#dff6ff'],sea:['#9cf2ea','#0896d6'],sun:[300,24,'#ffffff'],land:'bah'},
 {tag:'8 SALTOS EN LAS OLAS',sky:['#3a9ef0','#d6efff'],sea:['#6fd0ea','#0b5aa8'],sun:[70,30,'#fffbe8'],land:'aus'},
 {tag:'GANA A EL TIBURÓN',""")
rep(" if(L==='storm'){cvRidge(g,q,-20,420,HZ,40,8,'#111a30');",""" if(L==='form'){g.fillStyle='#fbf6e8';g.beginPath();g.moveTo(-10,HZ+2);for(let x=-10;x<=230;x+=8)g.lineTo(x,HZ-6-Math.sin(x*.04)*4-q()*2);g.lineTo(230,HZ+2);g.closePath();g.fill();g.fillStyle='#9cc58a';for(let i=0;i<10;i++){g.beginPath();g.arc(20+q()*190,HZ-6-q()*4,2.5,0,TAU);g.fill();}for(const[x,y,sc]of[[250,HZ+4,.5],[300,HZ+6,.6],[350,HZ+3,.45],[200,HZ+9,.7],[380,HZ+10,.75]])cvSail(g,x,y,sc);}
 if(L==='bah'){for(const[x,w,h]of[[60,70,10],[250,90,12],[360,50,8]]){g.fillStyle='#fbf3df';g.beginPath();g.ellipse(x,HZ,w/2,h/2,0,Math.PI,TAU);g.fill();cvPalm(g,x-8,HZ-3,.55);cvPalm(g,x+10,HZ-2,.5);}}
 if(L==='aus'){for(let i=0;i<9;i++){const h=18+q()*34,x=6+i*16;g.fillStyle=q()<.5?'#dfe7ee':'#c7d3de';g.fillRect(x,HZ-h,12,h);g.fillStyle='rgba(60,90,130,.35)';for(let y=HZ-h+3;y<HZ-2;y+=4)g.fillRect(x+2,y,8,1.3);}g.fillStyle='#f1d9a6';g.fillRect(0,HZ-3,170,4);}
 if(L==='storm'){cvRidge(g,q,-20,420,HZ,40,8,'#111a30');""")
rep(" else if(L==='buoys'){",""" else if(L==='form'){cvRival(g,q,rv(0),120,138,.24,-.05);cvRival(g,q,rv(1),200,152,.28,-.06);hero(290,170,.42,-.15,0);}
 else if(L==='bah'){for(const[x,y,r]of[[80,140,7],[110,150,6],[350,128,5]]){g.fillStyle='#f4a6b8';g.beginPath();g.arc(x,y,r,0,TAU);g.fill();g.beginPath();g.arc(x+r*.9,y-r*.4,r*.6,0,TAU);g.fill();g.strokeStyle='rgba(255,255,255,.7)';g.lineWidth=1.2;g.beginPath();g.ellipse(x,y+2,r*1.8,r*.6,0,0,TAU);g.stroke();}cvRival(g,q,rv(0),190,140,.24,-.05);hero(285,170,.42,-.15,0);}
 else if(L==='aus'){g.save();for(let k=0;k<3;k++){const y0=HZ+30+k*44;gg=g.createLinearGradient(0,y0-20,0,y0+12);gg.addColorStop(0,'#7fe0ec');gg.addColorStop(1,'#1f7fb6');g.fillStyle=gg;g.beginPath();g.moveTo(0,y0+12);g.quadraticCurveTo(200,y0-26-k*6,400,y0+12);g.closePath();g.fill();g.strokeStyle='rgba(255,255,255,.85)';g.lineWidth=3;g.beginPath();g.moveTo(20,y0+6);g.quadraticCurveTo(200,y0-24-k*6,380,y0+6);g.stroke();}g.restore();
  for(const[x,y]of[[90,HZ+40],[340,HZ+60]]){g.fillStyle='#ffd21a';g.beginPath();g.ellipse(x,y,12,3,-.1,0,TAU);g.fill();g.fillStyle='#e8b48c';g.fillRect(x-1.5,y-12,3,10);g.beginPath();g.arc(x,y-14,2.6,0,TAU);g.fill();}hero(230,120,.38,-.34,52);}
 else if(L==='buoys'){""")
open(p,'w').write(s);print('ok')
