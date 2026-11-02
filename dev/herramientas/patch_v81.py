import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v81.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=80", "const APP_VER=81")

# ===== textos sin inglés =====
h = rep(h, "<small>JJ'S SPORTS LOUNGE</small>EL BAR DEL PUERTO", "<small>BAR JJ</small>EL BAR DEL PUERTO", 2)
h = rep(h, "Zn.bar==='jj'?\"BAR JJ'S\":", "Zn.bar==='jj'?'BAR JJ':")
h = rep(h, "tag(Z.bar==='jj'?\"Bar JJ's a mitad de zona\":", "tag(Z.bar==='jj'?'Bar JJ a mitad de zona':")
h = rep(h, "'JJ’S SPORTS'", "'BAR JJ'")
h = rep(h, "const sign=[[3,28,'#8e1f2c',\"JJ's\"],[28,66,'#1f3fb0','SPORTS'],[66,97,'#1c1c1f','LOUNGE']];", "const sign=[[3,46,'#1f3fb0','BAR'],[46,97,'#8e1f2c','JJ']];")
h = rep(h, "${t===\"JJ's\"?11.5:10.5}px", "${t==='JJ'?11.5:10.5}px")
h = rep(h, "const sign=[[10,108,'#8e1f2c',\"JJ's\"],[110,250,'#1f3fb0','SPORTS'],[252,W-10,'#1c1c1f','LOUNGE']];", "const sign=[[10,Math.round(W*.45),'#1f3fb0','BAR'],[Math.round(W*.45)+2,W-10,'#8e1f2c','JJ']];")
h = rep(h, "n:'Slalom perfecto'", "n:'Boyas perfectas'")
h = rep(h, "Termina entre los 3 primeros. Slalom de verdad: rodea cada boya", "Termina entre los 3 primeros. Rodea cada boya")
h = rep(h, "Z.obj==='slalom'?['SLALOM',", "Z.obj==='slalom'?['BOYAS',")
h = rep(h, "{tag:'SLALOM DE BOYAS',", "{tag:'PASO DE BOYAS',")
h = rep(h, "¡ENTRAS EN EL TOP 10! TU NOMBRE:", "¡ESTÁS ENTRE LOS 10 MEJORES! TU NOMBRE:")
h = rep(h, '<h2 class="h">TOP 10</h2>', '<h2 class="h">LOS 10 MEJORES</h2>')
h = rep(h, "'¡Entras en el TOP 10 como '", "'¡Entras entre los 10 mejores como '")
h = rep(h, "'Esta vez no entras en el top 10.'", "'Esta vez no entras entre los 10 mejores.'")
h = rep(h, "u.push('piezas Stage '+(i+1))", "u.push('piezas nivel '+(i+1))")
h = rep(h, "p.name+' · Stage '+lv+'/3'", "p.name+' · Nivel '+lv+'/3'")
h = rep(h, "montadas en Stage 2.", "montadas en nivel 2.")
h = rep(h, "'Stage '+(lv+1),'var(--lime)'", "'Nivel '+(lv+1),'var(--lime)'")
h = rep(h, "<em>STAGE ${lv}/3</em>", "<em>NIVEL ${lv}/3</em>")
h = rep(h, "STAGE 3 · MÁX", "NIVEL 3 · MÁX", 2)
h = rep(h, "(lv?'STAGE '+(lv+1)+' · ':", "(lv?'NIVEL '+(lv+1)+' · ':")

# ===== copas =====
h = rep(h, "z:[2,8,9,10,11,13],zs:'Al Mago · San Telm · Formentor · Sa Calobra · Cabrera · Tormenta'", "z:[2,8,9,10,11,12],zs:'Al Mago · San Telm · Formentor · Sa Calobra · Cabrera · Portals'")
h = rep(h, "d:'Contrarreloj, slalom, saltos y policía',z:[0,1,4,5,6,12],zs:'El Puerto · La Cala · Persecución · Olas Gigantes · Las Rampas · Portals'",
 "d:'Contrarreloj, saltos, tormenta y policía',z:[0,4,5,6,13],zs:'El Puerto · Persecución · Olas Gigantes · Las Rampas · Tormenta'")

# ===== La Cala fuera del juego (sin mover el resto de pantallas) =====
h = rep(h, "{name:'LA CALA',water:", "{name:'LA CALA',off:1,water:")
h = rep(h, "const CUTS_AT=", "function zNum(i){let n=0;for(let k=0;k<=i&&k<ZONES.length;k++)if(!ZONES[k].off)n++;return n;}\nconst CUTS_AT=")
h = rep(h, "ZONES.forEach((Z,i)=>{const b=document.createElement('button');b.className='fz';b.setAttribute('aria-label','Zona '+(i+1)+' '+Z.name);const c=document.createElement('canvas');c.width=400;c.height=225;",
 "ZONES.forEach((Z,i)=>{if(Z.off)return;const b=document.createElement('button');b.className='fz';b.setAttribute('aria-label','Zona '+zNum(i)+' '+Z.name);const c=document.createElement('canvas');c.width=400;c.height=225;c.dataset.z=i;")
h = rep(h, "F.querySelectorAll('canvas').forEach((c,i)=>drawCover(c,i))", "F.querySelectorAll('canvas').forEach(c=>drawCover(c,+c.dataset.z))")
h = rep(h, ":'ZONA '+(zi+1),zw=g.measureText(zt).width+16", ":'ZONA '+zNum(zi),zw=g.measureText(zt).width+16")
h = rep(h, "'CARRERA LIBRE · ZONA '+(G.zi+1)", "'CARRERA LIBRE · ZONA '+zNum(G.zi)")
h = rep(h, "(!C?'ZONA '+(G.zi+1):C.fin?'FINAL'", "(!C?'ZONA '+zNum(G.zi):C.fin?'FINAL'")
h = rep(h, "(G.free?G.zi+1:(G.cpos|0)+1)", "(G.free?zNum(G.zi):(G.cpos|0)+1)")
h = rep(h, "[['Zona',(G.zi+1)+' · '+G.zone.Z.name],['Monedero'", "[['Zona',zNum(G.zi)+' · '+G.zone.Z.name],['Monedero'")

# ===== el JJ siempre en la costa de la izquierda: Al Mago (costa a la derecha) sin JJ =====
h = rep(h, "riv:5,bar:'jj',barAt:.27,theme:'cove'", "riv:5,bar:null,theme:'cove'")

# ===== JJ como el real (Son Matías): espigón ancho, barcas, playa al norte, paseo con palmeras =====
h = rep(h, "CUT_HALF=1000,JJC=110,JJP=-40;", "CUT_HALF=1000,JJC=85,JJP=-40;")
h = rep(h, "if(Z.bar==='jj'){const d=Math.abs(u-(barU+JJC));x+=46*sm(500,250,d)-84*sm(175,70,d);}", "if(Z.bar==='jj'){x+=82*sm(440,230,Math.abs(u-(barU+JJP+540)))+40*sm(400,240,Math.abs(u-(barU+JJP+40)));}")
h = rep(h, "return d>JJP+30&&d<JJC+190?'beach':Math.abs(d)<260?'prom':kindU(-y);", "return d>JJP+190&&d<JJP+1000?'beach':d>JJP-950&&d<=JJP+190?'prom':kindU(-y);")
h = rep(h, "if(d>JJP-80&&d<JJC+280)return null;", "if(d>JJP-950&&d<JJP+380)return null;")
h = rep(h, "{x:zone.shore(-(barU+JJC))+58,y:-(barU+JJC)}", "{x:zone.shore(-(barU+JJC))+52,y:-(barU+JJC)}")
i0 = h.index(" zone.pier=null;if(Z.bar==='jj'){"); i1 = h.index("\n", i0)
h = h[:i0] + """ zone.pier=null;if(Z.bar==='jj'){const pu=barU+JJP,sx=zone.shore(-pu),x0=sx-6,x1=sx+112,ph=40;zone.pier={x0,x1,y:-pu,h:ph};add({t:'pier',x:(x0+x1)/2,cx:(x0+x1)/2,hw:(x1-x0)/2+8,x0,x1,y:-pu,h:ph});
  const bc=()=>['#f4f5f7','#1e5eff','#1f9e52','#e3202b','#f4f5f7','#ffd21a'][(r()*6)|0];
  for(let bx=sx+18;bx<x1-8;bx+=22)add({t:'barca',x:bx,y:-pu-ph/2-14,rot:(r()-.5)*.1,c:bc()});
  for(let bx=sx+30;bx<x1-20;bx+=40)add({t:'barca',x:bx,y:-pu+ph/2+14,rot:Math.PI+(r()-.5)*.1,c:bc()});
  let nb=0;for(let au=pu-450;au>pu-820&&nb<7;au-=46+r()*26){add({t:'barca',x:sx+24+r()*72,y:-au,rot:(r()-.5)*1.2,c:bc(),moor:1});nb++;}}""" + h[i1:]
h = rep(h, "(Z.bar==='jj'?(u<barU+JJP-650||u>barU+JJC+330):", "(Z.bar==='jj'?(u<barU+JJP-900||u>barU+JJP+460):")
h = rep(h, "if(Z.bar&&cu>barU-500&&cu<barU+720)cu=barU+720;", "if(Z.bar&&cu>barU-950&&cu<barU+600)cu=barU+720;")
h = rep(h, "case 'pier':return x>o.x0-rad&&x<o.x1+rad&&Math.abs(y-o.y)<o.h/2+rad*.5;", "case 'pier':return x>o.x0-rad&&x<o.x1+rad&&Math.abs(y-o.y)<o.h/2+rad*.5;case 'barca':{const dx=x-o.x,dy=y-o.y,ca=Math.cos(o.rot),sa=Math.sin(o.rot),lx=dx*ca+dy*sa,ly=-dx*sa+dy*ca;return Math.abs(lx)<6+rad*.7&&Math.abs(ly)<15+rad*.6;}")
h = rep(h, "fboat:'¡BARCA!',pier:'¡PANTALÁN!'}[o.t]", "fboat:'¡BARCA!',barca:'¡BARCA!',pier:'¡ESPIGÓN!'}[o.t]")
i0 = h.index(" case 'pier':{"); i1 = h.index(" case 'lbuoy':{", i0)
h = h[:i0] + """ case 'pier':{const x0=o.x0,x1=o.x1,y0=o.y-o.h/2,hh=o.h;ctx.fillStyle='rgba(0,20,50,.3)';ctx.fillRect(x0+5,y0+6,x1-x0,hh);ctx.fillStyle='#c9c4ba';ctx.fillRect(x0,y0,x1-x0,hh);ctx.fillStyle='#b3ada2';for(let x=x0+18;x<x1;x+=18)ctx.fillRect(x,y0+3,1.2,hh-6);
  ctx.fillStyle='#9b958b';ctx.fillRect(x0,y0,x1-x0,3);ctx.fillRect(x0,y0+hh-3,x1-x0,3);ctx.fillRect(x1-3,y0,3,hh);ctx.fillStyle='#3d3a36';for(let x=x0+16;x<x1-6;x+=22){ctx.beginPath();ctx.arc(x,y0+5,1.8,0,TAU);ctx.arc(x,y0+hh-5,1.8,0,TAU);ctx.fill();}}return;
 case 'barca':{ctx.save();ctx.translate(o.x,o.y);if(o.moor){ctx.fillStyle='#ff8c1a';ctx.beginPath();ctx.arc(0,-23,2.6,0,TAU);ctx.fill();}ctx.rotate(o.rot);ctx.fillStyle='rgba(0,20,50,.25)';ctx.beginPath();ctx.ellipse(2,3,7,16,0,0,TAU);ctx.fill();ctx.fillStyle=o.c;ctx.beginPath();ctx.moveTo(0,-16);ctx.quadraticCurveTo(7,-6,6.5,9);ctx.quadraticCurveTo(0,15,-6.5,9);ctx.quadraticCurveTo(-7,-6,0,-16);ctx.fill();
  ctx.fillStyle='#caa070';ctx.beginPath();ctx.moveTo(0,-12);ctx.quadraticCurveTo(4.6,-5,4.3,7);ctx.quadraticCurveTo(0,11,-4.3,7);ctx.quadraticCurveTo(-4.6,-5,0,-12);ctx.fill();ctx.fillStyle='#8a6a48';ctx.fillRect(-4,-1,8,2);ctx.fillRect(-4,5,8,2);ctx.restore();}return;
""" + h[i1:]
i0 = h.index("function drawJJTop(g,Zn){"); i1 = h.index(" g.fillStyle='rgba(0,0,0,.2)';g.fillRect(4,8,102,80);", i0)
h = h[:i0] + """function drawJJTop(g,Zn){const by=Zn.barY,py=by-JJP,spx=Zn.shore(py);
 // muro con camino junto al agua, al sur del espigón
 g.save();for(let y=py+22;y<py+950;y+=6){const x=Zn.shore(y);g.fillStyle='#ddd7ca';g.fillRect(x-18,y,12,6.5);g.fillStyle='#9a948a';g.fillRect(x-6,y,6,6.5);}g.restore();
 // fila de palmeras en el borde del paseo
 {const q=rng(4321);for(let y=py-330;y<py+620;y+=46){if(y>py-205&&y<py-15)continue;const x=Zn.shore(y)-26;g.save();g.globalAlpha=.2;for(let k=0;k<8;k++)leaf(g,x+6,y+5,k/8*TAU+.2,14,'#203018');g.restore();for(let k=0;k<8;k++)leaf(g,x,y,k/8*TAU+q()*.3,12+q()*4,k%2?'#2f8f3f':'#46aa4a');}}
 const sx=spx,L=sx-114;
 g.save();g.translate(L,py-178);
""" + h[i1:]
h = rep(h, "if(Zn.bar&&Zn.barY>y0-240&&Zn.barY<y1+240)", "if(Zn.bar&&Zn.barY>y0-(Zn.bar==='jj'?1100:240)&&Zn.barY<y1+(Zn.bar==='jj'?1100:240))")
open(H, 'w').write(h); print('ok')
