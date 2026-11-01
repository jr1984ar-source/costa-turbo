p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
HOME='<button class="btn ghost sm hm" data-home style="flex:none"><svg class="hm-i" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8 8 2.5 14 8M4 7v6.5h3V10h2v3.5h3V7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>INICIO</button>'
# 1. mandos solo en carrera
rep("$('#app').classList.toggle('nopads',NOPADS.includes(id));","$('#app').classList.toggle('nopads',!!id);")
# 2. pantalla de campeón
rep('    <section id="scrRank" class="screen" hidden>','''    <section id="scrChamp" class="screen" hidden>
      <div class="head"><button class="btn ghost sm" id="cBk" style="flex:none">‹ ATRÁS</button><span class="sp"></span>'''+HOME+'''</div>
      <svg class="trophy" viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="tg" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#fff3b0"/><stop offset=".5" stop-color="#ffc93c"/><stop offset="1" stop-color="#c47a12"/></linearGradient></defs><path d="M18 8h28v14c0 9-6 16-14 16s-14-7-14-16z" fill="url(#tg)"/><path d="M18 12H9c0 9 5 14 11 14M46 12h9c0 9-5 14-11 14" fill="none" stroke="#ffc93c" stroke-width="4" stroke-linecap="round"/><rect x="28" y="37" width="8" height="10" fill="#e0a227"/><rect x="20" y="47" width="24" height="8" rx="2" fill="url(#tg)"/><path d="M26 16l3 6 6 1-4 4 1 6-5-3-5 3 1-6-4-4 6-1z" fill="#fff" opacity=".85"/></svg>
      <h2 class="h">¡CAMPEÓN DE LA COSTA!</h2>
      <div class="big" id="cScore">0</div>
      <p class="sub" id="cInfo"></p>
      <p class="crank" id="cRank"></p>
      <div class="menu"><button class="btn p" id="cNext">VUELTA 2</button><button class="btn" id="cRk">VER RANKING</button><button class="btn ghost" id="cMenu" style="width:100%">MENÚ</button></div>
    </section>

    <section id="scrRank" class="screen" hidden>''')
rep("/* usuario */",""".trophy{width:84px;height:84px;filter:drop-shadow(0 6px 18px rgba(255,201,60,.55))}
.crank{margin:0;font-family:var(--cond);font-weight:800;font-size:20px;letter-spacing:.04em;color:var(--lime)}.crank.no{color:var(--dim);font-size:16px}
/* usuario */""")
rep("showResult(last?'¡CAMPEÓN DE LA COSTA!':'¡ZONA SUPERADA!',last?'Has ganado a El Tiburón. Empieza la vuelta '+(G.lap+2)+', más difícil.':'Zona '+(G.zi+1)+' · '+Z.name,lines,()=>{if(last){G.zi=0;G.lap++;}else G.zi++;goMap();});}",
    "showResult(last?'¡HAS GANADO LA FINAL!':'¡ZONA SUPERADA!',last?'Has ganado a El Tiburón y el campeonato.':'Zona '+(G.zi+1)+' · '+Z.name,lines,()=>{if(last)champEnd();else{G.zi++;goMap();}});}")
rep("function failZone(why,fromFinish){","""function champEnd(){G._champDone=true;G.mode='over';const m=MOTOS[G.moto],en={name:pilotName(),score:G.score|0,zone:ZONES.length,lap:G.lap,moto:m.id,mname:paintOf(m).name||'',at:G.runId||Date.now()};
 const q=qualifies(G.score);if(q){lastHl=en.at;saveScore(en);}
 $('#cScore').textContent=pts(G.score)+' PUNTOS';$('#cInfo').textContent='Has ganado las '+ZONES.length+' carreras'+(G.lap?' de la vuelta '+(G.lap+1):'')+' con '+motoName(m)+'.';
 const r=$('#cRank');r.className='crank'+(q?'':' no');r.textContent=q?'¡Entras en el TOP 10 como '+en.name+'!':'Esta vez no entras en el top 10.';
 $('#cNext').textContent='VUELTA '+(G.lap+2)+' · MÁS DIFÍCIL';show('scrChamp');Snd.win();}
function rankBack(){if(G._champDone&&G.mode==='over'&&!G.demo)show('scrChamp');else goTitle();}
function failZone(why,fromFinish){""")
rep("on('#psBk',()=>resume());on('#oBk',()=>{Snd.click();goTitle();});on('#rkBk',()=>{Snd.click();goTitle();});",
    """on('#psBk',()=>resume());on('#oBk',()=>{Snd.click();goTitle();});on('#rkBk',()=>{Snd.click();rankBack();});
on('#cNext',()=>{Snd.click();G._champDone=false;G.zi=0;G.lap++;goMap();});on('#cRk',()=>{Snd.click();show('scrRank');renderRank();});on('#cMenu',()=>{Snd.click();goTitle();});on('#cBk',()=>{Snd.click();goTitle();});""")
rep("function midChamp(){return !!G._champOn&&!G.free&&","function midChamp(){return !!G._champOn&&!G._champDone&&!G.free&&")
rep("function goTitle(){G._champOn=false;","function goTitle(){G._champOn=false;G._champDone=false;")
rep("function newGame(){G._champOn=true;","function newGame(){G._champOn=true;G._champDone=false;G.runId=Date.now();")
# ranking: misma partida = una sola entrada (la mejor)
rep("function rankList(){return(globalScores&&dbWritable)?globalScores:localRank();}",
    "function dedupe(l){const m=new Map();for(const e of l){const k=String(e.at);const o=m.get(k);if(!o||e.score>o.score)m.set(k,e);}return[...m.values()].sort((a,b)=>b.score-a.score);}\nfunction rankList(){return dedupe((globalScores&&dbWritable)?globalScores:localRank());}")
rep("async function saveScore(e){const loc=localRank();loc.push(e);","async function saveScore(e){const loc=localRank().filter(x=>x.at!==e.at);loc.push(e);")
rep("const en={name,score:G.score|0,zone:G.zi+1,lap:G.lap,moto:MOTOS[G.moto].id,mname:paintOf(MOTOS[G.moto]).name||'',at:Date.now()};",
    "const en={name,score:G.score|0,zone:G.zi+1,lap:G.lap,moto:MOTOS[G.moto].id,mname:paintOf(MOTOS[G.moto]).name||'',at:G.runId||Date.now()};")
open(p,'w').write(s);print('ok')
