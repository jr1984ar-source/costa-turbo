import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v77.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=76", "const APP_VER=77")
HOME = '<button class="btn ghost sm hm" data-home style="flex:none"><svg class="hm-i" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8 8 2.5 14 8M4 7v6.5h3V10h2v3.5h3V7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>INICIO</button>'

# ---------- copas ----------
h = rep(h, "function difLv(){return Math.max(1,Math.min(5,store.get('ct_dif',1)|0));}",
"""function difLv(){return Math.max(1,Math.min(5,store.get('ct_dif',1)|0));}
// Campeonato en copas de 5 carreras; La Final se abre al ganar las 4 copas
const CUPS=[
 {id:'costa',n:'COPA COSTA',nm:'Copa Costa',ic:'🏁',d:'Carreras junto a la costa',z:[2,11,8,9,18],zs:'Al Mago · Cabrera · San Telm · Formentor · Es Vedrà',c:'#ff9a3c'},
 {id:'paraiso',n:'COPA PARAÍSO',nm:'Copa Paraíso',ic:'🌴',d:'Circuitos y aguas turquesa',z:[19,7,15,20,16],zs:'Bahía de Palma · Es Trenc · Formentera · Bahía de Alcúdia · Bahamas',c:'#3fe0d0'},
 {id:'crono',n:'COPA CONTRARRELOJ',nm:'Copa Contrarreloj',ic:'⏱️',d:'Contra el reloj',z:[0,1,12,13,10],zs:'El Puerto · La Cala · Portals · Tormenta · Sa Calobra',c:'#5cb8ff'},
 {id:'accion',n:'COPA ACCIÓN',nm:'Copa Acción',ic:'🌊',d:'Saltos, boyas y policía',z:[5,4,6,14,17],zs:'Olas Gigantes · Persecución · Las Rampas · Carrera de Boyas · Australia',c:'#ffd21a'},
 {id:'final',n:'LA FINAL',nm:'La Final',ic:'🦈',d:'Contra El Tiburón',z:[21],zs:'Gana a El Tiburón y serás el campeón de la costa',c:'#ff5a5f',fin:1}];
const METAL=['Bronce','Plata','Oro','Platino','Diamante'];
let cupStore=store.get('ct_cups',null);if(!cupStore||typeof cupStore!=='object')cupStore={};
function cupS(id){const s=cupStore[id]||(cupStore[id]={won:0,t:{}});if(!s.t||typeof s.t!=='object')s.t={};return s;}
function cupLv(i){return Math.min(5,(cupS(CUPS[i].id).won|0)+1);}
function finalOpen(){const need=cupLv(4);return CUPS.slice(0,4).every(C=>(cupS(C.id).won|0)>=need);}
function cupTrofN(C){const s=cupS(C.id);let k=0;for(let l=1;l<=5;l++)if(s.t[l]&&s.t[l].n>0)k++;return k;}
function inCup(){return !G.free&&!G.demo&&G.cup!=null&&CUPS[G.cup];}
// dificultad de la carrera dentro de la copa (la 1ª fácil, la 5ª como las últimas del campeonato largo)
function dzi(zi){const C=inCup();if(!C)return zi;return C.fin?21:Math.round((G.cpos|0)*20/Math.max(1,C.z.length-1));}
let zwon=store.get('ct_zwon',[]);if(!Array.isArray(zwon))zwon=[];""")
h = rep(h, "function trofCount(){let k=0;for(const t of TROFEOS)if(trofStore[t.lv]&&trofStore[t.lv].n>0)k++;return k;}",
 "function trofCount(){let k=0;for(const t of TROFEOS)if(trofStore[t.lv]&&trofStore[t.lv].n>0)k++;for(const C of CUPS)k+=cupTrofN(C);return k;}")

# rivales y portada: dificultad según la posición en la copa
h = rep(h, "*(1+G.lap*.04)*(1+zi*.005)*", "*(1+G.lap*.04)*(1+dzi(zi)*.005)*")
h = rep(h, "const lvl=Math.max(1,Math.min(5,Math.ceil((zi+1)*5/ZONES.length))),k=.86+lvl*.024;", "const lvl=Math.max(1,Math.min(5,Math.ceil((dzi(zi)+1)*5/ZONES.length))),k=.86+lvl*.024;")
h = rep(h, "{const n=ZONES.length,lv=Math.max(1,Math.min(5,Math.ceil((zi+1)*5/n))),", "{const n=ZONES.length,lv=Math.max(1,Math.min(5,Math.ceil(((zi===G.zi?dzi(zi):zi)+1)*5/n))),")

# nueva partida en una copa
h = rep(h, "function newGame(){G._champOn=true;G._champDone=false;G.runId=Date.now();G.free=false;G.demo=false;G.zi=0;G.lap=difLv()-1;",
 "function newGame(ci){ci=ci==null?(G.cup|0):ci;G.cup=ci;G.cpos=0;G._champOn=true;G._champDone=false;G.runId=Date.now();G.free=false;G.demo=false;G.zi=CUPS[ci].z[0];G.lap=cupLv(ci)-1;")
h = rep(h, "store.set('ct_moto',G.moto);if(G.free)goFree();else if(G._champOn){G.parts=partsOf(MOTOS[G.moto]);goMap();}else newGame();});",
 "store.set('ct_moto',G.moto);if(G.free)goFree();else if(G._champOn){G.parts=partsOf(MOTOS[G.moto]);goMap();}else goCups();});\n"
 "function goCups(){show('scrCups');renderCups();Music.play('menu');}\n"
 "function renderCups(){const L=$('#cuList');L.textContent='';CUPS.forEach((C,ci)=>{const S=cupS(C.id),lv=cupLv(ci),lock=!!C.fin&&!finalOpen(),b=document.createElement('button');b.className='cupc'+(lock?' lk':'');b.style.setProperty('--cc',C.c);\n"
 " b.innerHTML='<i class=\"ci\"></i><div class=\"cm\"><b></b><small></small><span class=\"cz\"></span></div><div class=\"cr\"><em></em><span class=\"ct\"></span></div>';\n"
 " b.querySelector('.ci').textContent=C.ic;b.querySelector('b').textContent=C.n;b.querySelector('small').textContent=C.d+(C.fin?'':' · 5 carreras');b.querySelector('.cz').textContent=lock?('Gana las 4 copas'+(lv>1?' en dificultad '+lv:'')+' para desbloquearla'):C.zs;\n"
 " b.querySelector('em').textContent=lock?'🔒 BLOQUEADA':'DIFICULTAD '+lv+'/5';const k=cupTrofN(C);b.querySelector('.ct').textContent=lock?'':k?'🏆 '+k+' de 5':'Sin trofeos';\n"
 " b.addEventListener('click',()=>{Snd.init();if(lock){Snd.miss();return;}Snd.click();newGame(ci);});L.append(b);});}")
h = rep(h, "on('#gBack',()=>{Snd.click();goPilot();});", "on('#gBack',()=>{Snd.click();goPilot();});on('#cuBk',()=>{Snd.click();goGarage();});")

# pantalla de copas
h = rep(h, '    <section id="scrPaint" class="screen" hidden>',
 '''    <section id="scrCups" class="screen" hidden>
      <div class="head"><button class="btn ghost sm" id="cuBk" style="flex:none">‹ ATRÁS</button><h2 class="h">CAMPEONATO</h2>''' + HOME + '''</div>
      <p class="sub">Elige una copa. Cada una tiene su dificultad y sus trofeos.</p>
      <div class="cups" id="cuList"></div>
    </section>

    <section id="scrPaint" class="screen" hidden>''')
h = rep(h, ".slist{", """.cups{width:min(100%,440px);display:grid;gap:10px}
.cupc{display:grid;grid-template-columns:40px minmax(0,1fr) auto;gap:10px;align-items:center;width:100%;padding:12px 12px 12px 10px;border-radius:16px;border:1px solid color-mix(in srgb,var(--cc) 55%,transparent);background:linear-gradient(135deg,color-mix(in srgb,var(--cc) 22%,transparent),rgba(255,255,255,.04));color:#fff;text-align:left;cursor:pointer;font:inherit}
.cupc:active{transform:scale(.98)}
.cupc .ci{font-style:normal;font-size:28px;text-align:center;line-height:1}
.cupc b{display:block;font-family:var(--cond);font-weight:800;font-size:21px;letter-spacing:.04em;color:var(--cc);line-height:1}
.cupc small{display:block;font-family:var(--cond);font-weight:600;font-size:14px;color:#fff;margin-top:3px}
.cupc .cz{display:block;font-size:11.5px;color:var(--dim);margin-top:4px;line-height:1.3}
.cupc .cr{text-align:right;align-self:start}
.cupc em{display:block;font-style:normal;font-family:var(--cond);font-weight:800;font-size:13px;letter-spacing:.04em;white-space:nowrap}
.cupc .ct{display:block;font-family:var(--cond);font-weight:700;font-size:12px;color:var(--gold);margin-top:4px;white-space:nowrap}
.cupc.lk{opacity:.6}
.tcup{width:100%;padding:10px 10px 8px;border-radius:14px;background:rgba(255,255,255,.06);border:1px solid color-mix(in srgb,var(--cc) 45%,transparent);text-align:left}
.tch{display:flex;justify-content:space-between;align-items:baseline;gap:8px;margin:0 2px 6px}
.tch b{font-family:var(--cond);font-weight:800;font-size:18px;letter-spacing:.04em;color:var(--cc)}
.tch small{font-family:var(--cond);font-weight:700;font-size:13px;color:var(--dim);white-space:nowrap}
.trow{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:4px}
.tsm{display:flex;flex-direction:column;align-items:center;gap:2px;min-width:0}
.tsm svg{width:100%;max-width:54px;height:60px}
.tsm span{font-family:var(--cond);font-weight:700;font-size:11px;color:var(--dim);white-space:nowrap}
.tsm.on span{color:var(--gold)}.tsm.cur span{color:var(--cyan)}.tsm.off{opacity:.45}
.tsm.on svg{filter:drop-shadow(0 3px 8px rgba(255,220,120,.45))}
.slist{""")

# mapa
h = rep(h, "$('#mZoneN').textContent=(retry?'OTRA VEZ · ':'')+(G.free?'CARRERA LIBRE · ZONA '+(G.zi+1):'CAMPEONATO · ZONA '+(G.zi+1)+' DE '+ZONES.length+' · DIFICULTAD '+(G.lap+1)+'/5');",
 "{const C=inCup();$('#mZoneN').textContent=(retry?'OTRA VEZ · ':'')+(!C?'CARRERA LIBRE · ZONA '+(G.zi+1):C.n+(C.fin?'':' · CARRERA '+((G.cpos|0)+1)+' DE '+C.z.length)+' · DIFICULTAD '+(G.lap+1)+'/5');}")
h = rep(h, "const P=$('#mProg');P.hidden=!!G.free;P.textContent='';if(!G.free)ZONES.forEach((_,i)=>{const sp=document.createElement('span');sp.textContent=i+1;if(i<G.zi)sp.className='ok';else if(i===G.zi)sp.className='on';P.append(sp);});",
 "const P=$('#mProg'),PC=inCup();P.hidden=!PC||!!PC.fin;P.textContent='';if(PC&&!PC.fin)PC.z.forEach((_,i)=>{const sp=document.createElement('span');sp.textContent=i+1;if(i<(G.cpos|0))sp.className='ok';else if(i===(G.cpos|0))sp.className='on';P.append(sp);});")
# etiqueta de la carrera
h = rep(h, "$('#zonePill').innerHTML='ZONA '+(G.zi+1)+' <span>·</span> '+G.zone.Z.name;",
 "{const C=inCup();$('#zonePill').innerHTML=(!C?'ZONA '+(G.zi+1):C.fin?'FINAL':'CARRERA '+((G.cpos|0)+1)+'/'+C.z.length)+' <span>·</span> '+G.zone.Z.name;}")

# fin de carrera
h = rep(h, " const last=G.zi===ZONES.length-1;\n", " const CU=inCup(),last=!!CU&&(G.cpos|0)>=CU.z.length-1;\n")
h = rep(h, "const nb=Math.max(best,G.lap>0?ZONES.length:G.zi+1);",
 "if(!zwon.includes(G.zi)){zwon.push(G.zi);store.set('ct_zwon',zwon);}const nb=Math.min(22,Math.max(best,zwon.length));")
h = rep(h, "showResult(last?'¡HAS GANADO LA FINAL!':'¡ZONA SUPERADA!',last?'Has ganado a El Tiburón y el campeonato.':'Zona '+(G.zi+1)+' · '+Z.name,lines,()=>{if(last)champEnd();else{G.zi++;goMap();}});}",
 "showResult(last?(CU.fin?'¡HAS GANADO LA FINAL!':'¡HAS GANADO LA '+CU.n+'!'):'¡CARRERA SUPERADA!',last?(CU.fin?'Has ganado a El Tiburón.':'Has ganado las '+CU.z.length+' carreras.'):'Carrera '+((G.cpos|0)+1)+' de '+CU.z.length+' · '+Z.name,lines,()=>{if(last)champEnd();else{G.cpos=(G.cpos|0)+1;G.zi=CU.z[G.cpos];goMap();}});}")

# fin de copa
i0 = h.index("function champEnd(){"); i1 = h.index("function medSvg(")
old = h[i0:i1]; assert "store.set('ct_dif',nxt)" in old
h = h[:i0] + """function champEnd(){G._champDone=true;medal('campeon');G.mode='over';const C=CUPS[G.cup|0],S=cupS(C.id),lv=Math.max(1,Math.min(5,G.lap+1)),T=S.t[lv]||(S.t[lv]={n:0,best:0});T.n=(T.n|0)+1;if(!T.at)T.at=Date.now();if((G.score|0)>(T.best|0)){T.best=G.score|0;T.moto=motoName(MOTOS[G.moto]);}
 const wasOpen=finalOpen();if(lv>(S.won|0))S.won=lv;store.set('ct_cups',cupStore);
 const m=MOTOS[G.moto],en={name:pilotName(),score:G.score|0,zone:C.z.length,lap:G.lap,cup:C.id,moto:m.id,mname:paintOf(m).name||'',at:G.runId||Date.now()};
 const q=qualifies(G.score);if(q){lastHl=en.at;saveScore(en);}
 $('#cH').textContent=C.fin?'¡CAMPEÓN DE LA COSTA!':'¡GANAS LA '+C.n+'!';
 $('#cScore').textContent=pts(G.score)+' PUNTOS';$('#cInfo').textContent=(C.fin?'Has ganado a El Tiburón':'Has ganado las '+C.z.length+' carreras de la '+C.nm)+' en dificultad '+lv+' con '+motoName(m)+'.';
 $('#cTrof').innerHTML=trofSvg(lv,true,'c');const tn=C.nm+' · '+METAL[lv-1];let tx=(T.n>1?'Trofeo '+tn+' ×'+T.n:'¡Nuevo trofeo: '+tn+'!')+(lv<5?' · Siguiente: dificultad '+(lv+1)+'/5':' · Dificultad máxima');
 if(!C.fin&&!wasOpen&&finalOpen())tx+=' · ¡LA FINAL DESBLOQUEADA!';$('#cTrofTxt').textContent=tx;
 const r=$('#cRank');r.className='crank'+(q?'':' no');r.textContent=q?'¡Entras en el TOP 10 como '+en.name+'!':'Esta vez no entras en el top 10.';
 $('#cNext').textContent='ELEGIR COPA';show('scrChamp');Snd.win();}
""" + h[i1:]
h = rep(h, '<h2 class="h">¡CAMPEÓN DE LA COSTA!</h2>', '<h2 class="h" id="cH">¡CAMPEÓN DE LA COSTA!</h2>')
h = rep(h, "on('#cNext',()=>{Snd.click();G._champDone=false;G.zi=0;G.lap=difLv()-1;goMap();});", "on('#cNext',()=>{Snd.click();G._champDone=false;G._champOn=false;goCups();});")
h = rep(h, "&&!G.free&&(G.zi>0||G.lap>0)&&G.mode!=='over';}", "&&!G.free&&(G.cpos|0)>0&&G.mode!=='over';}")

# derrota
h = rep(h, "[['Zona',(G.zi+1)+' · '+G.zone.Z.name],['Puntos',pts(G.score)]]", "[[G.free?'Zona':'Carrera',(G.free?G.zi+1:(G.cpos|0)+1)+' · '+G.zone.Z.name],['Puntos',pts(G.score)]]")
h = rep(h, "$('#oInfo').textContent='Llegaste a la zona '+(G.zi+1)+' ('+G.zone.Z.name+') en dificultad '+(G.lap+1)+' con '+MOTOS[G.moto].name+'.';",
 "{const C=CUPS[G.cup|0];$('#oInfo').textContent='Llegaste a la carrera '+((G.cpos|0)+1)+' de '+(C.fin?'La Final':'la '+C.nm)+' ('+G.zone.Z.name+') en dificultad '+(G.lap+1)+' con '+MOTOS[G.moto].name+'.';}")
h = rep(h, "const en={name,score:G.score|0,zone:G.zi+1,lap:G.lap,", "const en={name,score:G.score|0,zone:(G.cpos|0)+1,cup:(CUPS[G.cup|0]||{}).id,lap:G.lap,")

# inicio
h = rep(h, "$('#uProg').textContent='Campeonato '+best+'/'+ZONES.length;{const k=trofCount();$('#uTrof').textContent='Dificultad '+difLv()+'/5 · 🏆 '+k+(k===1?' trofeo':' trofeos');}",
 "{const w=CUPS.slice(0,4).filter(C=>cupS(C.id).won>0).length;$('#uProg').textContent='Copas '+w+'/4'+(cupS('final').won>0?' · Final ✓':'');}{const k=trofCount();$('#uTrof').textContent='🏆 '+k+(k===1?' trofeo':' trofeos');}")

# ranking
h = rep(h, "m.name+' · zona '+((e.zone|0)||1)+(e.lap>0?", "m.name+(e.cup?' · '+String((CUPS.find(C=>C.id===e.cup)||{nm:e.cup}).nm).slice(0,20):' · zona '+((e.zone|0)||1))+(e.lap>0?")

# sala de trofeos por copas
i0 = h.index("function renderTrof(){"); i1 = h.index("function trofBack(")
h = h[:i0] + """function renderTrof(){const g=$('#trGrid');g.textContent='';const k=trofCount();$('#trSub').textContent='Trofeos: '+k+' · uno por copa y dificultad';
 const sec=(nm,col,sub,cells)=>{const d=document.createElement('div');d.className='tcup';d.style.setProperty('--cc',col);d.innerHTML='<div class="tch"><b></b><small></small></div><div class="trow"></div>';d.querySelector('b').textContent=nm;d.querySelector('small').textContent=sub;const r=d.querySelector('.trow');cells.forEach(c=>r.append(c));g.append(d);};
 const cell=(l,on,cur,u,t)=>{const d=document.createElement('div');d.className='tsm '+(on?'on':cur?'cur':'off');d.innerHTML=trofSvg(l,on,u)+'<span></span>';d.querySelector('span').textContent=METAL[l-1]+(on&&t.n>1?' ×'+t.n:'');return d;};
 CUPS.forEach((C,ci)=>{const S=cupS(C.id),cur=cupLv(ci),lock=C.fin&&!finalOpen()&&!(S.won>0),cs=[];for(let l=1;l<=5;l++){const t=S.t[l];cs.push(cell(l,!!(t&&t.n>0),!lock&&l===cur,C.id,t));}sec(C.ic+' '+C.n,C.c,lock?'Gana las 4 copas':'Dificultad '+cur+'/5',cs);});
 if(TROFEOS.some(t=>trofStore[t.lv]&&trofStore[t.lv].n>0)){const cs=TROFEOS.map(t=>{const st=trofStore[t.lv];return cell(t.lv,!!(st&&st.n>0),false,'old',st);});sec('🏆 CAMPEONATO CLÁSICO','#c9ced6','22 pantallas',cs);}}
""" + h[i1:]
h = rep(h, "const zt='ZONA '+(zi+1),zw=g.measureText(zt).width+16", "const CZ=zi===G.zi&&inCup(),zt=CZ?(CZ.fin?'FINAL':'CARRERA '+((G.cpos|0)+1)):'ZONA '+(zi+1),zw=g.measureText(zt).width+16")
open(H, 'w').write(h); print('ok')
