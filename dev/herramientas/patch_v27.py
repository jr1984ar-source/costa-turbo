p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
HOME='<button class="btn ghost sm hm" data-home style="flex:none"><svg class="hm-i" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8 8 2.5 14 8M4 7v6.5h3V10h2v3.5h3V7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>INICIO</button>'

# ================= FANTASMA =================
rep(" G.police=[];G.parts_fx=[];G.pops=[];G.pitSlots=0;G.jumps=0;",
    " G.ghostRec=[];G._gAcc=0;G.ghost=G.free?store.get('ct_ghost_'+zi,null):null;if(G.ghost&&!Array.isArray(G.ghost.p))G.ghost=null;G._pens=0;G._crashes=0;G._newMed=[];\n G.police=[];G.parts_fx=[];G.pops=[];G.pitSlots=0;G.jumps=0;")
rep(" if(racing&&!G.demo){G.elapsed+=dt;"," if(racing&&!G.demo){G.elapsed+=dt;if(G.free&&P.fin===0){G._gAcc+=dt;if(G._gAcc>=.1){G._gAcc-=.1;G.ghostRec.push([Math.round(P.x),Math.round(P.y),+P.h.toFixed(2)]);}}")
rep("if(G.free){showResult('¡PANTALLA SUPERADA!','Carrera libre · '+Z.name,lines,()=>goFree());return;}",
    "if(G.free){const ft=P.finT||G.elapsed,old=store.get('ct_ghost_'+G.zi,null);if(!old||!(old.t<=ft)){store.set('ct_ghost_'+G.zi,{t:+ft.toFixed(2),m:MOTOS[G.moto].id,p:G.ghostRec});lines.push([old?'¡Nuevo récord!':'Récord guardado',fmtT(ft)]);}else lines.push(['Tu récord',fmtT(old.t)]);medalLines(lines);showResult('¡PANTALLA SUPERADA!','Carrera libre · '+Z.name,lines,()=>goFree());return;}")
# dibujar fantasma (antes de las estelas)
rep(" // wakes\n for(const c of crafts())drawWake(c);",
""" // fantasma
 if(G.ghost&&G.free&&!G.demo&&G.ghost.p.length>1){const gp=G.ghost.p,f=G.elapsed/.1,i=Math.min(gp.length-2,Math.floor(f)),a=gp[i],b=gp[i+1],k=Math.min(1,f-i),gx=lerp(a[0],b[0],k),gy=lerp(a[1],b[1],k),gh=lerp(a[2],b[2],k);
  if(gy>camTop-60&&gy<camTop+VH+60&&f<gp.length+20){const gm=SP.jet[G.ghost.m]||SP.jet[MOTOS[0].id];ctx.save();ctx.globalAlpha=.4;ctx.translate(gx,gy);ctx.rotate(gh);ctx.drawImage(gm.c,-16,-34,32,68);ctx.restore();
   ctx.font='800 10px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';const tx='RÉCORD '+fmtT(G.ghost.t),w=ctx.measureText(tx).width+12;ctx.fillStyle='rgba(255,255,255,.75)';ctx.beginPath();ctx.roundRect(gx-w/2,gy-52,w,15,7);ctx.fill();ctx.fillStyle='#0a1630';ctx.fillText(tx,gx,gy-44.5);}}
 // wakes
 for(const c of crafts())drawWake(c);""")
rep(" tag(Z.bar==='jj'?"," if(G.free){const gh=store.get('ct_ghost_'+G.zi,null);if(gh&&gh.t)tag('Tu récord: '+fmtT(gh.t)+' · corre contra tu fantasma','gold');}\n tag(Z.bar==='jj'?")

# ================= MEDALLAS =================
rep("const SWATCHES=[","""const MEDALS=[
 {id:'salto',n:'Primer salto',d:'Salta por primera vez.',r:200},
 {id:'mega',n:'Mega saltador',d:'Salta la MEGA RAMPA.',r:500},
 {id:'saltos50',n:'Saltamontes',d:'Haz 50 saltos en total.',r:800},
 {id:'mortal',n:'Mortal perfecto',d:'Aterriza un mortal hacia atrás.',r:400},
 {id:'combo',n:'Combo',d:'Mortal y superman en el mismo salto.',r:800},
 {id:'ola',n:'Surfero',d:'Coge bien una ola gigante.',r:500},
 {id:'delfines',n:'Amigo de los delfines',d:'Coge turbo de 5 delfines.',r:600},
 {id:'monedas',n:'Hucha llena',d:'Coge 60 monedas en una sola pantalla.',r:800},
 {id:'limpio',n:'Sin un rasguño',d:'Termina una carrera sin chocar.',r:800},
 {id:'podio',n:'Ganador',d:'Gana una carrera llegando el primero.',r:500},
 {id:'boyas',n:'Slalom perfecto',d:'Termina la Carrera de Boyas sin penalizaciones.',r:1000},
 {id:'tiburon',n:'Cazatiburones',d:'Gana La Final a El Tiburón.',r:2000},
 {id:'campeon',n:'Campeón de la costa',d:'Gana el campeonato completo.',r:3000}];
let medStore=store.get('ct_medals',{});if(!medStore||typeof medStore!=='object')medStore={};
let statStore=store.get('ct_stats',{});if(!statStore||typeof statStore!=='object')statStore={};
function bumpStat(k,n){statStore[k]=(statStore[k]|0)+(n||1);store.set('ct_stats',statStore);return statStore[k];}
function medal(id){if(medStore[id]||G.demo)return;const m=MEDALS.find(x=>x.id===id);if(!m)return;medStore[id]=Date.now();store.set('ct_medals',medStore);G.money+=m.r;saveWallet();(G._newMed=G._newMed||[]).push(m);
 if(G.mode==='play'){msg('¡MEDALLA!',m.n+' · +'+pts(m.r)+' PTA','var(--gold)');}try{Snd.check();}catch(_){}}
function medalLines(lines){for(const m of G._newMed||[])lines.push(['🏅 '+m.n,'+'+pts(m.r)+' PTA']);G._newMed=[];}
const SWATCHES=[""")
# disparadores
rep("function startJump(c){c.airT=.45+c.v/620;c.air=c.airT;c.trick=0;c._tr=[];c.flipT=0;c.supT=0;if(c.isP){Snd.jump();G.jumps++;}}",
    "function startJump(c){c.airT=.45+c.v/620;c.air=c.airT;c.trick=0;c._tr=[];c.flipT=0;c.supT=0;if(c.isP){Snd.jump();G.jumps++;if(!G.demo){medal('salto');if(bumpStat('jumps')>=50)medal('saltos50');}}}")
rep("if(o.mega)msg('¡MEGA SALTO!','','var(--cyan)');","if(o.mega){msg('¡MEGA SALTO!','','var(--cyan)');medal('mega');}")
rep("G.tricks=(G.tricks||0)+names.length;","G.tricks=(G.tricks||0)+names.length;if(tr.includes('flip'))medal('mortal');if(tr.includes('flip')&&tr.includes('sup'))medal('combo');")
rep("pop(c.x,c.y-46,'¡OLA GIGANTE! +'+b,'#33d6ff');","pop(c.x,c.y-46,'¡OLA GIGANTE! +'+b,'#33d6ff');medal('ola');")
rep("if(Math.hypot(o.x-P.x,o.y-P.y)<56&&P.air<=0){o.got=1;","if(Math.hypot(o.x-P.x,o.y-P.y)<56&&P.air<=0){o.got=1;if(bumpStat('dolphins')>=5)medal('delfines');")
rep("else{c.stuckT=2;c.stuckY=c.y;c.v=0;c.boostT=0;Snd.miss();G.shake=4;msg('¡PENALIZACIÓN!'","else{G._pens=(G._pens|0)+1;c.stuckT=2;c.stuckY=c.y;c.v=0;c.boostT=0;Snd.miss();G.shake=4;msg('¡PENALIZACIÓN!'")
rep("function crash(c,why){if(c.crash>0||c.inv>0)return;c.crash=.75;c.v*=.22;c.inv=1.6;c.boostT=0;splash(c.x,c.y,18,120);if(c.isP){",
    "function crash(c,why){if(c.crash>0||c.inv>0)return;c.crash=.75;c.v*=.22;c.inv=1.6;c.boostT=0;splash(c.x,c.y,18,120);if(c.isP){G._crashes=(G._crashes|0)+1;")
rep(" const last=G.zi===ZONES.length-1;saveWallet();",
    " const last=G.zi===ZONES.length-1;\n if(G.zoneCoins>=60)medal('monedas');if(Z.riv&&P.rank===1)medal('podio');if(Z.riv&&!(G._crashes>0))medal('limpio');if(Z.turns&&!(G._pens>0))medal('boyas');if(Z.boss&&P.rank===1)medal('tiburon');\n saveWallet();")
rep("showResult(last?'¡HAS GANADO LA FINAL!'","medalLines(lines);showResult(last?'¡HAS GANADO LA FINAL!'")
rep("function champEnd(){G._champDone=true;","function champEnd(){G._champDone=true;medal('campeon');")

# pantalla de medallas
rep('<button class="btn ghost" id="bRank" style="width:100%">RANKING TOP 10</button>',
    '<div class="row" style="flex-wrap:nowrap"><button class="btn ghost" id="bRank">RANKING TOP 10</button><button class="btn ghost" id="bMed">MEDALLAS</button></div>')
rep('    <section id="scrChamp" class="screen" hidden>','''    <section id="scrMedals" class="screen" hidden>
      <div class="head"><button class="btn ghost sm" id="mdBk" style="flex:none">‹ ATRÁS</button><h2 class="h">MEDALLAS</h2>'''+HOME+'''</div>
      <p class="sub" id="mdSub"></p>
      <div class="mgrid" id="mdGrid"></div>
    </section>

    <section id="scrChamp" class="screen" hidden>''')
rep("/* usuario */",""".mgrid{width:min(100%,440px);display:grid;grid-template-columns:1fr 1fr;gap:8px}
.md{display:grid;grid-template-columns:38px minmax(0,1fr);gap:8px;align-items:center;padding:8px;border-radius:12px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);text-align:left}
.md svg{width:38px;height:38px}
.md b{display:block;font-family:var(--cond);font-weight:800;font-size:15px;line-height:1.05}
.md small{display:block;font-size:11px;line-height:1.2;color:var(--dim);margin-top:2px}
.md em{display:block;font-style:normal;font-family:var(--cond);font-weight:700;font-size:12px;color:var(--gold);margin-top:3px}
.md.off{opacity:.55}.md.off em{color:var(--dim)}
.md.on{border-color:rgba(255,201,60,.5);background:rgba(255,201,60,.1)}
@media (orientation:landscape){.mgrid{grid-template-columns:repeat(3,1fr);width:min(100%,720px)}}
/* usuario */""")
rep("function rankBack(){","""function medSvg(on){const a=on?'#ffe08a':'#6b7486',b=on?'#e0a227':'#454c5a',r=on?'#e3202b':'#3a404c';return `<svg viewBox="0 0 38 38" aria-hidden="true"><path d="M12 2h6l3 11h-6zM26 2h-6l-3 11h6z" fill="${r}"/><circle cx="19" cy="24" r="11" fill="${b}"/><circle cx="19" cy="24" r="8" fill="${a}"/><path d="M19 18.5l1.7 3.4 3.8.5-2.8 2.6.7 3.7-3.4-1.8-3.4 1.8.7-3.7-2.8-2.6 3.8-.5z" fill="${b}"/></svg>`;}
function renderMedals(){const g=$('#mdGrid');g.textContent='';let n=0;for(const m of MEDALS){const on=!!medStore[m.id];if(on)n++;const d=document.createElement('div');d.className='md '+(on?'on':'off');d.innerHTML=medSvg(on)+'<div><b></b><small></small><em></em></div>';d.querySelector('b').textContent=m.n;d.querySelector('small').textContent=m.d;d.querySelector('em').textContent=(on?'Conseguida · ':'Premio: ')+pts(m.r)+' PTA';g.append(d);}
 $('#mdSub').textContent=n+' de '+MEDALS.length+' medallas conseguidas';}
function rankBack(){""")
rep("on('#cNext',","on('#bMed',()=>{Snd.click();show('scrMedals');renderMedals();});on('#mdBk',()=>{Snd.click();toTitle();});\non('#cNext',")
open(p,'w').write(s);print('ok')
