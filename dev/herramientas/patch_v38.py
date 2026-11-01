p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)

# ---------- 1. Sa Calobra: cañón más ancho y menos rocas ----------
rep("w=125+28*nw(u/380)+10*nw(u/90);","w=188+30*nw(u/380)+10*nw(u/90);")
rep("Z.canyon?{coins:3.4,rocks:2.4,ramp:.8,kayak:.8,boat:.4}","Z.canyon?{coins:3.4,rocks:.6,ramp:.8,kayak:.8,boat:.4}")
rep("Paredes de roca a los dos lados y muy poco sitio.","Paredes de roca a los dos lados: no te despistes.")

# ---------- 2-4. Corazones a tercios ----------
rep("lives:3,money","lives:3,dmg:0,money")
rep(".lives i.off{background:rgba(255,255,255,.25)}",".lives i.off{background:rgba(255,255,255,.25)}\n.lives.hit{animation:lvHit .5s ease-out}\n@keyframes lvHit{0%{transform:scale(1.35)}100%{transform:scale(1)}}")
rep("function livesUI(){const L=$('#lives');L.textContent='';for(let i=0;i<Math.max(3,G.lives);i++){const d=document.createElement('i');if(i>=G.lives)d.className='off';L.append(d);}}",
    """function livesUI(){const L=$('#lives');L.textContent='';const d0=G.dmg|0;for(let i=0;i<Math.max(3,G.lives);i++){const d=document.createElement('i');if(i>=G.lives)d.className='off';else if(i===G.lives-1&&d0>0){const p=Math.round((3-d0)/3*100);d.style.background='linear-gradient(to top,#ff3b4f '+p+'%,rgba(255,255,255,.25) '+p+'%)';}L.append(d);}}
function hpTot(){return G.lives*3-(G.dmg|0);}
function setHp(t){t=Math.max(0,Math.min(18,t));G.lives=Math.ceil(t/3);G.dmg=G.lives*3-t;livesUI();}
function hpTxt(){const t=Math.max(0,hpTot()),w=Math.floor(t/3),f=t%3,fr=['','⅓','⅔'][f];if(!w)return f?fr+' de corazón':'0 corazones';if(w===1&&!f)return '1 corazón';return w+(f?' '+fr:'')+' corazones';}
function hurt(c,v0){if(G.demo||G.mode!=='play'||!(v0>c.st.maxV*.25))return;setHp(hpTot()-1);const L=$('#lives');L.classList.remove('hit');void L.offsetWidth;L.classList.add('hit');
 if(G.lives<=0){G.mode='over';endRace();Snd.fail();setTimeout(gameOver,900);msg('¡SIN CORAZONES!','Demasiados golpes','var(--red)');return;}
 if(!G.dmg)msg('¡CORAZÓN PERDIDO!','Te queda'+(hpTot()>3?'n ':' ')+hpTxt(),'var(--red)');else pop(c.x,c.y-54,'−⅓ ♥','#ff4757');}""")
# golpes contra objetos (a cierta velocidad) y contra barcos que se mueven
rep("{crash(c,{rock:'¡ROCA!',pig:'¡OINK!',surfer:'¡SURFISTA!',turtle:'¡TORTUGA!'}[o.t]||'¡PUM!');if(!c.isP){c.ai.re=0;}}",
    "{const v0=Math.abs(c.v);crash(c,{rock:'¡ROCA!',pig:'¡OINK!',surfer:'¡SURFISTA!',turtle:'¡TORTUGA!'}[o.t]||'¡PUM!');if(c.isP)hurt(c,v0);else c.ai.re=0;}")
rep("crash(c,{cata:'¡CATAMARÁN!',super:'¡SUPERYATE!',patrol:'¡CHOQUE!',ray:'¡MANTARRAYA!',nurse:'¡TIBURÓN!',croc:'¡COCODRILO!'}[o.t]||'¡PUM!');",
    "crash(c,{cata:'¡CATAMARÁN!',super:'¡SUPERYATE!',patrol:'¡CHOQUE!',ray:'¡MANTARRAYA!',nurse:'¡TIBURÓN!',croc:'¡COCODRILO!'}[o.t]||'¡PUM!');if(c.isP)hurt(c,1e9);")
# nueva partida / carrera libre: corazones llenos
rep("G.free=false;G.demo=false;G.zi=0;G.lap=0;G.lives=3;","G.free=false;G.demo=false;G.zi=0;G.lap=0;G.lives=3;G.dmg=0;")
rep("function startFree(zi){G.free=true;G.demo=false;G.zi=zi;G.lap=0;G.lives=3;","function startFree(zi){G.free=true;G.demo=false;G.zi=zi;G.lap=0;G.lives=3;G.dmg=0;")
rep("function startZone(){\n const zi=G.zi;","function startZone(){\n if(G.free&&!G.demo){G.lives=3;G.dmg=0;}\n const zi=G.zi;")
# fallar en carrera libre no quita vida (se renueva)
rep("function failZone(why,fromFinish){if(G.mode==='over')return;G.mode='result';endRace();G.lives--;livesUI();",
    "function failZone(why,fromFinish){if(G.mode==='over')return;G.mode='result';endRace();if(!G.free)G.lives--;livesUI();")
rep("showResult('¡NO LO HAS CONSEGUIDO!',(why||'')+' Te queda'+(G.lives>1?'n ':' ')+G.lives+' vida'+(G.lives>1?'s':'')+'.',",
    "showResult('¡NO LO HAS CONSEGUIDO!',(why||'')+(G.free?' Vuelve a intentarlo: en carrera libre empiezas con los corazones llenos.':' Te queda'+(hpTot()>3?'n ':' ')+hpTxt()+'.'),")
# bar: bebida +1/3, vida +1 corazón
rep("{id:'life',name:'Vida extra',ef:'Una oportunidad más',price:1500},","{id:'life',name:'Vida extra',ef:'+1 corazón',price:1500},")
rep("{id:'turbo',name:'Refresco turbo',ef:'+1 turbo (máximo 5)',price:500}","{id:'turbo',name:'Refresco turbo',ef:'+1 turbo y +⅓ de corazón',price:500}")
rep("const full=it.id==='fuel'?G.fuel>=99:it.id==='turbo'?G.turbo>=5:G.lives>=6;","const full=it.id==='fuel'?G.fuel>=99:it.id==='turbo'?G.turbo>=5&&hpTot()>=18:G.lives>=6;")
rep("it.id==='turbo'?'Tienes '+G.turbo+' (máx. 5)':'Tienes '+G.lives+' vidas';","it.id==='turbo'?'Tienes '+G.turbo+' turbos · '+hpTxt():'Tienes '+hpTxt();")
rep("else if(it.id==='turbo')G.turbo++;else G.lives++;renderJJ();","else if(it.id==='turbo'){if(G.turbo<5)G.turbo++;setHp(hpTot()+1);}else G.lives++;renderJJ();")
rep("msg('¡PIRI-PIRI!','+1 VIDA · +2 TURBOS'","msg('¡PIRI-PIRI!','+1 CORAZÓN · +2 TURBOS'")
# corazones flotando (solo campeonato)
rep("function hitObj(o,x,y,rad){","""function heartPath(g,s){g.beginPath();g.moveTo(0,s*.78);g.bezierCurveTo(-s*1.35,-s*.12,-s*.62,-s*1.08,0,-s*.42);g.bezierCurveTo(s*.62,-s*1.08,s*1.35,-s*.12,0,s*.78);g.closePath();}
function placeHearts(O,add,seed,len,shore,rwall){const rh=rng(seed+77),nh=rh()<.5?1:2;
 for(let k=0;k<nh;k++){const base=Math.round(len*(nh===1?.5:k?.7:.36)+(rh()-.5)*300);let best=null,bd=-1;
  for(const dy of[0,-160,160,-320,320]){const hy=-(base+dy),L=Math.max(30,shore(hy)+50),R=Math.min(WG-30,rwall?rwall(hy)-50:WG-30);if(R<L+20)continue;
   for(let j=0;j<7;j++){const x=lerp(L,R,j/6);let d=1e9,bad=false;
    for(const o of O){if(o.y==null||Math.abs(o.y-hy)>420)continue;
     if(o.t==='island'||o.t==='nozone'){const ex=(x-o.x)/(o.rx+40),ey=(hy-o.y)/(o.ry+40);if(ex*ex+ey*ey<1)bad=true;continue;}
     if(o.t==='pass'){if(Math.abs(hy-o.y)<(o.h||100)/2+90)bad=true;continue;}
     if(o.t==='coin'||o.t==='check'||o.t==='finish'||Math.abs(o.y-hy)>110)continue;d=Math.min(d,Math.hypot((o.x||0)-x,(o.y-hy)*.8));}
    if(!bad&&d>bd){bd=d;best=[x,hy];}}}
  if(best)add({t:'heart',x:best[0],y:best[1]});}}
function hitObj(o,x,y,rad){""")
rep(" add({t:'finish',y:-len});\n"," add({t:'finish',y:-len});\n if(!G.free)placeHearts(O,add,seed,len,zone.shore,zone.rwall);\n")
rep("add({t:'fuel',x:xs[Math.floor(N/2)],y:ys[Math.floor(N/2)]});","add({t:'fuel',x:xs[Math.floor(N/2)],y:ys[Math.floor(N/2)]});\n if(!G.free){const rh=rng(seed+77),nh=rh()<.5?1:2;for(let k=0;k<nh;k++){const ii=Math.floor(N*(nh===1?.3:k?.75:.3))%N,ln=(rh()-.5)*W*.3;add({t:'heart',x:xs[ii]+Math.cos(hs[ii])*ln,y:ys[ii]+Math.sin(hs[ii])*ln});}}")
rep("   if(o.t==='coin'){if(!o.got&&c.isP&&!G.demo&&Math.hypot(o.x-c.x,o.y-c.y)<17){",
    "   if(o.t==='heart'){if(!o.got&&c.isP&&!G.demo&&Math.hypot(o.x-c.x,o.y-c.y)<20){o.got=1;Snd.pickup();setHp(hpTot()+1);msg('¡CORAZÓN!','+⅓ de corazón','#ff4f6b');}continue;}\n   if(o.t==='coin'){if(!o.got&&c.isP&&!G.demo&&Math.hypot(o.x-c.x,o.y-c.y)<17){")
rep("if(o.t==='coin'||o.t==='check'||o.t==='finish'||o.t==='ramp'||o.t==='can'||o.t==='fuel'||","if(o.t==='coin'||o.t==='heart'||o.t==='check'||o.t==='finish'||o.t==='ramp'||o.t==='can'||o.t==='fuel'||")
rep(" case 'can':case 'fuel':if(o.got)return;",""" case 'heart':if(o.got||G.demo)return;{const b=Math.sin(t*4+o.x)*1.5,pz=1+Math.sin(t*6)*.08;ctx.strokeStyle='rgba(255,255,255,.55)';ctx.lineWidth=1.2;ctx.beginPath();ctx.arc(o.x,o.y,14+Math.sin(t*5)*2,0,TAU);ctx.stroke();
  ctx.fillStyle='rgba(0,30,70,.25)';ctx.beginPath();ctx.ellipse(o.x+2,o.y+10,8,3,0,0,TAU);ctx.fill();ctx.save();ctx.translate(o.x,o.y+b);ctx.scale(pz,pz);heartPath(ctx,10);ctx.fillStyle='#ff3b4f';ctx.fill();ctx.strokeStyle='#ffffff';ctx.lineWidth=1.8;ctx.stroke();ctx.fillStyle='rgba(255,255,255,.65)';ctx.beginPath();ctx.ellipse(-4,-4,2.2,1.4,-.6,0,TAU);ctx.fill();ctx.restore();}return;
 case 'can':case 'fuel':if(o.got)return;""")

# ---------- 5. Barras de la moto con las piezas ----------
rep(".st i{display:grid;grid-template-columns:repeat(5,1fr);gap:3px}",".st i{display:grid;grid-template-columns:repeat(8,1fr);gap:3px}")
rep(".st i b.on{background:var(--cyan)}",".st i b.on{background:var(--cyan)}\n.st i b.up{background:#ffc93c;box-shadow:0 0 5px rgba(255,201,60,.6)}\n.stup{font-family:var(--cond);font-weight:700;font-size:11px;letter-spacing:.06em;color:#ffc93c;margin-top:2px}")
rep("function craft(m,x,y,isP){","""function partsShown(m){return owns(m)?partsOf(m):m.riva?RIVA_KIT:{};}
function statRows(S2,m){const parts=partsShown(m),L=k=>Math.min(3,parts[k]|0);
 const f={vel:((1+.045*L('escape'))*(1+[0,.08,.14,.19][L('turbina')])-1)/(1.135*1.19-1),ace:L('turbo')/3,giro:[0,.3,.5,.7][L('aletas')]/.7,turbo:[0,.5,.9,1.3][L('intercooler')]/1.3};
 S2.textContent='';let any=false;for(const[k,l]of[['vel','VELOCIDAD'],['ace','ACELERACIÓN'],['giro','GIRO'],['turbo','TURBO']]){const row=document.createElement('div');row.className='st';const a=document.createElement('span');a.textContent=l;const b=document.createElement('i');const base=m.st[k],up=Math.round((8-base)*f[k]);if(up>0)any=true;
  for(let j=0;j<8;j++){const x=document.createElement('b');if(j<base)x.className='on';else if(j<base+up)x.className='up';b.append(x);}row.append(a,b);S2.append(row);}
 if(any){const n=document.createElement('div');n.className='stup';n.textContent='EN DORADO: LO QUE SUMAN LAS PIEZAS';S2.append(n);}}
function craft(m,x,y,isP){""")
rep("const S2=$('#gStats');S2.textContent='';for(const[k,l]of[['vel','VELOCIDAD'],['ace','ACELERACIÓN'],['giro','GIRO'],['turbo','TURBO']]){const row=document.createElement('div');row.className='st';const a=document.createElement('span');a.textContent=l;const b=document.createElement('i');for(let j=0;j<5;j++){const x=document.createElement('b');if(j<m.st[k])x.className='on';b.append(x);}row.append(a,b);S2.append(row);}",
    "statRows($('#gStats'),m);")
rep("else{const S2=document.createElement('div');S2.className='stats';for(const[k,l]of[['vel','VELOCIDAD'],['ace','ACELERACIÓN'],['giro','GIRO'],['turbo','TURBO']]){const row=document.createElement('div');row.className='st';const a=document.createElement('span');a.textContent=l;const bb=document.createElement('i');for(let j=0;j<5;j++){const x=document.createElement('b');if(j<m.st[k])x.className='on';bb.append(x);}row.append(a,bb);S2.append(row);}L.append(S2);",
    "else{const S2=document.createElement('div');S2.className='stats';statRows(S2,m);L.append(S2);")
rep("if(st==='own'){const parts=partsOf(m);PARTS.forEach(","if(st==='own'){const parts=partsOf(m);{const S2=document.createElement('div');S2.className='stats';statRows(S2,m);L.append(S2);}PARTS.forEach(")

rep("const APP_VER=37;","const APP_VER=38;")
open(p,'w').write(s);print('ok')
