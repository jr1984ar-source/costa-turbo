import shutil
H='costa-turbo.html'
shutil.copy(H,'costa-turbo.pre-v60.html')
h=open(H).read()
def rep(s,a,b,n=1):
    c=s.count(a)
    assert c==n,(c,a[:90])
    return s.replace(a,b)

h=rep(h,"const APP_VER=59","const APP_VER=60")

# ---------- CSS sala de trofeos ----------
h=rep(h,".mgrid{width:min(100%,440px);display:grid;grid-template-columns:1fr 1fr;gap:8px}",
""".mgrid{width:min(100%,440px);display:grid;grid-template-columns:1fr 1fr;gap:8px}
.tgrid{width:min(100%,440px);display:grid;gap:10px}
.tr{display:grid;grid-template-columns:88px minmax(0,1fr);gap:12px;align-items:center;padding:8px 12px 8px 8px;border-radius:14px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);text-align:left}
.tr .ts{width:88px;height:100px;display:flex;align-items:flex-end;justify-content:center;border-radius:10px;background:radial-gradient(ellipse at 50% 35%,rgba(255,255,255,.12),transparent 70%),linear-gradient(180deg,rgba(10,22,48,.35),rgba(10,22,48,.6));box-shadow:inset 0 -9px 0 #6b4526,inset 0 -11px 0 #8a5a33}
.tr svg{width:74px;height:88px;margin-bottom:4px}
.tr b{display:block;font-family:var(--cond);font-weight:800;font-size:19px;line-height:1.05}
.tr small{display:block;font-size:12px;line-height:1.25;color:var(--dim);margin-top:3px}
.tr .dots{display:block;font-size:11px;letter-spacing:3px;color:var(--orange);margin-top:3px}
.tr em{display:block;font-style:normal;font-family:var(--cond);font-weight:700;font-size:13px;line-height:1.2;color:var(--gold);margin-top:4px}
.tr.off{opacity:.6}.tr.off em{color:var(--dim)}
.tr.cur{opacity:1;border-color:rgba(51,214,255,.55);background:rgba(51,214,255,.08)}.tr.cur em{color:var(--cyan)}
.tr.on{border-color:rgba(255,201,60,.5);background:rgba(255,201,60,.09)}.tr.on svg{filter:drop-shadow(0 4px 12px rgba(255,220,120,.5))}
.trophy svg{width:100%;height:100%}
.ctrof{margin:0;font-family:var(--cond);font-weight:800;font-size:19px;letter-spacing:.03em;color:var(--gold)}""")
h=rep(h,"@media (orientation:landscape){.mgrid{grid-template-columns:repeat(3,1fr);width:min(100%,720px)}}",
        "@media (orientation:landscape){.mgrid{grid-template-columns:repeat(3,1fr);width:min(100%,720px)}.tgrid{grid-template-columns:1fr 1fr;width:min(100%,720px)}}")

# ---------- menú inicio ----------
h=rep(h,'<div class="row" style="flex-wrap:nowrap"><button class="btn ghost" id="bRank">RANKING TOP 10</button><button class="btn ghost" id="bMed">MEDALLAS</button></div>',
        '<div class="row" style="flex-wrap:nowrap"><button class="btn ghost" id="bRank">RANKING</button><button class="btn ghost" id="bMed">MEDALLAS</button><button class="btn ghost" id="bTrof">TROFEOS</button></div>')

# ---------- pantalla sala de trofeos ----------
HOME='<button class="btn ghost sm hm" data-home style="flex:none"><svg class="hm-i" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8 8 2.5 14 8M4 7v6.5h3V10h2v3.5h3V7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>INICIO</button>'
h=rep(h,'    <section id="scrChamp" class="screen" hidden>',
'''    <section id="scrTrof" class="screen" hidden>
      <div class="head"><button class="btn ghost sm" id="trBk" style="flex:none">‹ ATRÁS</button><h2 class="h">SALA DE TROFEOS</h2>'''+HOME+'''</div>
      <p class="sub" id="trSub"></p>
      <div class="tgrid" id="trGrid"></div>
    </section>

    <section id="scrChamp" class="screen" hidden>''')

# ---------- pantalla de campeón: trofeo de la dificultad ----------
i0=h.index('<svg class="trophy" viewBox="0 0 64 64"');i1=h.index('</svg>',i0)+6
h=h[:i0]+'<div class="trophy" id="cTrof" style="width:96px;height:112px"></div>'+h[i1:]
h=rep(h,'<p class="crank" id="cRank"></p>\n      <div class="menu"><button class="btn p" id="cNext">VUELTA 2</button><button class="btn" id="cRk">VER RANKING</button>',
        '<p class="ctrof" id="cTrofTxt"></p>\n      <p class="crank" id="cRank"></p>\n      <div class="menu"><button class="btn p" id="cNext">VUELTA 2</button><button class="btn" id="cTr">SALA DE TROFEOS</button><button class="btn" id="cRk">VER RANKING</button>')

# ---------- lógica: dificultad 1-5 y trofeos ----------
TROF=r'''
const TROFEOS=[{lv:1,n:'Copa Costa',m:'Bronce'},{lv:2,n:'Copa Mediterráneo',m:'Plata'},{lv:3,n:'Copa Baleares',m:'Oro'},{lv:4,n:'Trofeo Tiburón',m:'Platino'},{lv:5,n:'Trofeo Leyenda',m:'Diamante'}];
let trofStore=store.get('ct_trof',null);if(!trofStore||typeof trofStore!=='object'){trofStore={};if(medStore.campeon&&store.get('ct_dif',null)==null){trofStore[1]={n:1,best:0,at:medStore.campeon};store.set('ct_dif',2);}store.set('ct_trof',trofStore);}
function difLv(){return Math.max(1,Math.min(5,store.get('ct_dif',1)|0));}
function trofCount(){let k=0;for(const t of TROFEOS)if(trofStore[t.lv]&&trofStore[t.lv].n>0)k++;return k;}
function trofSvg(lv,on,u){const id='tg'+u+lv,L=!on,G2=(a,b,c)=>L?'#5b6578':`url(#${id})`,gr=(a,b,c)=>L?'':`<defs><linearGradient id="${id}" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="${a}"/><stop offset=".5" stop-color="${b}"/><stop offset="1" stop-color="${c}"/></linearGradient></defs>`,dk=L?'#4a5366':null;
 const plinth=`<rect x="14" y="62" width="36" height="12" rx="2" fill="${L?'#2a2f3a':'#5a3a22'}"/><rect x="14" y="62" width="36" height="3" rx="1.5" fill="${L?'#353b48':'#7a5232'}"/><rect x="23" y="66" width="18" height="5" rx="1" fill="${L?'#353b48':'#e8cf9a'}"/>`;
 let s='';
 if(lv===1){s=gr('#ffe1c2','#d38b4f','#7f4220')+`<path d="M20 12h24v13c0 8-5 14-12 14s-12-6-12-14z" fill="${G2()}"/><path d="M20 16h-6c0 7 3 11 8 12M44 16h6c0 7-3 11-8 12" fill="none" stroke="${L?dk:'#b8703c'}" stroke-width="3.2" stroke-linecap="round"/><path d="M24 22q2-2 4 0t4 0 4 0 4 0" fill="none" stroke="${L?dk:'rgba(255,240,220,.7)'}" stroke-width="1.6"/><rect x="29" y="39" width="6" height="12" fill="${L?dk:'#a5602f'}"/><rect x="21" y="51" width="22" height="11" rx="2" fill="${G2()}"/>`;}
 else if(lv===2){s=gr('#ffffff','#c5d0da','#66727e')+`<ellipse cx="32" cy="9" rx="17" ry="3.2" fill="${L?dk:'#e9eef3'}"/><path d="M15 9h34c0 15-7 25-17 25S15 24 15 9z" fill="${G2()}"/><path d="M16 12c-10 0-11 13 3 16M48 12c10 0 11 13-3 16" fill="none" stroke="${L?dk:'#9aa7b3'}" stroke-width="3.6" stroke-linecap="round"/><path d="M20 17q3-3 6 0t6 0 6 0 6 0M22 23q2.5-2.5 5 0t5 0 5 0 5 0" fill="none" stroke="${L?dk:'rgba(255,255,255,.75)'}" stroke-width="1.5"/><path d="M29 34h6l2 13H27z" fill="${L?dk:'#8d99a5'}"/><rect x="20" y="47" width="24" height="5" rx="2" fill="${G2()}"/><rect x="17" y="52" width="30" height="10" rx="2" fill="${L?dk:'#7d8995'}"/>`;}
 else if(lv===3){s=gr('#fff3b0','#ffc93c','#c47a12')+`<path d="M18 8h28v15c0 9-6 16-14 16s-14-7-14-16z" fill="${G2()}"/><path d="M18 12H9c0 9 5 14 11 14M46 12h9c0 9-5 14-11 14" fill="none" stroke="${L?dk:'#ffc93c'}" stroke-width="4" stroke-linecap="round"/><path d="M32 13l3 6 6.5 1-4.7 4.5 1.1 6.4L32 28l-5.9 2.9 1.1-6.4-4.7-4.5 6.5-1z" fill="${L?dk:'#ffffff'}" opacity="${L?1:.9}"/><rect x="28" y="39" width="8" height="10" fill="${L?dk:'#e0a227'}"/><rect x="19" y="49" width="26" height="13" rx="2" fill="${G2()}"/>`+(L?'':`<g fill="#e0a227">${[[10,44,-40],[8,37,-20],[9,30,0],[54,44,40],[56,37,20],[55,30,0]].map(([x,y,a])=>`<ellipse cx="${x}" cy="${y}" rx="2.6" ry="5" transform="rotate(${a} ${x} ${y})"/>`).join('')}</g>`);}
 else if(lv===4){s=gr('#f4fbff','#a9c9e2','#45678a')+`<path d="M24 44C27 28 35 13 49 6c-5 9-7 22-3 38z" fill="${G2()}"/><path d="M30 40c3-12 9-23 17-30" fill="none" stroke="${L?dk:'rgba(255,255,255,.8)'}" stroke-width="2" stroke-linecap="round"/><path d="M10 50c5-6 9 1 14-3s9 1 14-3 9 1 16-3v9H10z" fill="${G2()}"/><path d="M12 49c4-4 8 1 12-2s8 1 12-2 8 1 13-2" fill="none" stroke="${L?dk:'#ffffff'}" stroke-width="1.6" opacity=".8"/><rect x="18" y="53" width="28" height="9" rx="2" fill="${L?dk:'#5f84a8'}"/>`;}
 else{s=gr('#ffffff','#8ff0ff','#7a5cff')+`<path d="M32 3l4.3 10.6 11.4.9-8.7 7.4 2.7 11.1L32 27l-9.7 6 2.7-11.1-8.7-7.4 11.4-.9z" fill="${G2()}" stroke="${L?dk:'#ffffff'}" stroke-width="1.2" stroke-linejoin="round"/><path d="M32 3v24M16.3 14.5 32 27l15.7-12.5M25 32.9 32 27l7 5.9" fill="none" stroke="${L?dk:'rgba(255,255,255,.75)'}" stroke-width="1"/><path d="M28 33h8l3 15H25z" fill="${L?dk:'#ffc93c'}"/><rect x="18" y="48" width="28" height="14" rx="3" fill="${L?dk:'#1b1f2e'}" stroke="${L?dk:'#ffc93c'}" stroke-width="1.6"/>`+(L?'':`<circle cx="25" cy="55" r="2.2" fill="#ff3b4f"/><circle cx="32" cy="55" r="2.6" fill="#33d6ff"/><circle cx="39" cy="55" r="2.2" fill="#7be35a"/>`);}
 return `<svg viewBox="0 0 64 76" aria-hidden="true">${s}${plinth}${L?'<g transform="translate(32 30)"><rect x="-7" y="-2" width="14" height="11" rx="2" fill="#c3cad6"/><path d="M-4.5-2v-3a4.5 4.5 0 0 1 9 0v3" fill="none" stroke="#c3cad6" stroke-width="2.4"/></g>':''}</svg>`;}
function renderTrof(){const g=$('#trGrid');g.textContent='';const dl=difLv(),k=trofCount();$('#trSub').textContent='Dificultad del campeonato: '+dl+'/5 · Trofeos: '+k+' de 5';
 for(const t of TROFEOS){const st=trofStore[t.lv],on=!!(st&&st.n>0),cur=!on&&t.lv===dl;const d=document.createElement('div');d.className='tr '+(on?'on':cur?'cur':'off');d.innerHTML='<div class="ts">'+trofSvg(t.lv,on,'r')+'</div><div><b></b><small></small><span class="dots"></span><em></em></div>';
  d.querySelector('b').textContent=t.n;d.querySelector('small').textContent=t.m+' · Dificultad '+t.lv;d.querySelector('.dots').textContent='●'.repeat(t.lv)+'○'.repeat(5-t.lv);
  d.querySelector('em').textContent=on?('Ganado'+(st.n>1?' ×'+st.n:'')+(st.best?' · Mejor: '+pts(st.best)+' puntos':'')+(st.moto?' · '+st.moto:'')):cur?'Gana el campeonato en dificultad '+t.lv+' para conseguirlo':'Bloqueado: primero gana la dificultad '+(t.lv-1);g.append(d);}}
function trofBack(){if(G._trFrom==='champ'){G._trFrom=null;show('scrChamp');}else toTitle();}
'''
a="function medalLines(lines){for(const m of G._newMed||[])lines.push(['🏅 '+m.n,'+'+pts(m.r)+' PTA']);G._newMed=[];}\n"
h=rep(h,a,a+TROF.lstrip('\n'))

# campeonato nuevo: empieza en la dificultad conseguida
h=rep(h,"function newGame(){G._champOn=true;G._champDone=false;G.runId=Date.now();G.free=false;G.demo=false;G.zi=0;G.lap=0;",
        "function newGame(){G._champOn=true;G._champDone=false;G.runId=Date.now();G.free=false;G.demo=false;G.zi=0;G.lap=difLv()-1;")
# fin del campeonato: trofeo + subir dificultad
h=rep(h,"function champEnd(){G._champDone=true;medal('campeon');G.mode='over';const m=MOTOS[G.moto],",
        "function champEnd(){G._champDone=true;medal('campeon');G.mode='over';const lv=Math.max(1,Math.min(5,G.lap+1)),T=trofStore[lv]||(trofStore[lv]={n:0,best:0});T.n=(T.n|0)+1;if(!T.at)T.at=Date.now();if((G.score|0)>(T.best|0)){T.best=G.score|0;T.moto=motoName(MOTOS[G.moto]);}store.set('ct_trof',trofStore);const nxt=Math.min(5,lv+1);if(nxt>difLv())store.set('ct_dif',nxt);const m=MOTOS[G.moto],")
h=rep(h,"$('#cInfo').textContent='Has ganado las '+ZONES.length+' carreras'+(G.lap?' de la vuelta '+(G.lap+1):'')+' con '+motoName(m)+'.';",
        "$('#cInfo').textContent='Has ganado las '+ZONES.length+' carreras en dificultad '+lv+' con '+motoName(m)+'.';const TT=TROFEOS[lv-1];$('#cTrof').innerHTML=trofSvg(lv,true,'c');$('#cTrofTxt').textContent=(T.n>1?'Trofeo '+TT.n+' ×'+T.n:'¡Nuevo trofeo: '+TT.n+'!')+(lv<5?' · Siguiente: dificultad '+(lv+1)+'/5':' · Dificultad máxima');")
h=rep(h,"$('#cNext').textContent='VUELTA '+(G.lap+2)+' · MÁS DIFÍCIL';show('scrChamp');",
        "$('#cNext').textContent=lv<5?'CAMPEONATO · DIFICULTAD '+(lv+1)+'/5':'OTRO CAMPEONATO · DIFICULTAD 5/5';show('scrChamp');")
h=rep(h,"on('#cNext',()=>{Snd.click();G._champDone=false;G.zi=0;G.lap++;goMap();});",
        "on('#cNext',()=>{Snd.click();G._champDone=false;G.zi=0;G.lap=difLv()-1;goMap();});on('#cTr',()=>{Snd.click();G._trFrom='champ';show('scrTrof');renderTrof();});")
h=rep(h,"on('#bMed',()=>{Snd.click();show('scrMedals');renderMedals();});",
        "on('#bMed',()=>{Snd.click();show('scrMedals');renderMedals();});on('#bTrof',()=>{Snd.click();G._trFrom=null;show('scrTrof');renderTrof();});on('#trBk',()=>{Snd.click();trofBack();});")
# textos: dificultad en vez de vuelta
h=rep(h,"'CAMPEONATO · ZONA '+(G.zi+1)+' DE '+ZONES.length+(G.lap?' · VUELTA '+(G.lap+1):'')",
        "'CAMPEONATO · ZONA '+(G.zi+1)+' DE '+ZONES.length+' · DIFICULTAD '+(G.lap+1)+'/5'")
h=rep(h,"'Llegaste a la zona '+(G.zi+1)+' ('+G.zone.Z.name+')'+(G.lap?' de la vuelta '+(G.lap+1):'')+' con '",
        "'Llegaste a la zona '+(G.zi+1)+' ('+G.zone.Z.name+') en dificultad '+(G.lap+1)+' con '")
h=rep(h,"(e.lap>0?' · vuelta '+((e.lap|0)+1):'')","(e.lap>0?' · dificultad '+((e.lap|0)+1):'')")
h=rep(h,"$('#uProg').textContent='Campeonato '+best+'/'+ZONES.length;}",
        "$('#uProg').textContent='Campeonato '+best+'/'+ZONES.length;{const k=trofCount();$('#uTrof').textContent='Dificultad '+difLv()+'/5 · 🏆 '+k+(k===1?' trofeo':' trofeos');}}")
h=rep(h,'PTA · <span id="uProg"></span></span>','PTA · <span id="uProg"></span></span><span id="uTrof"></span>')
open(H,'w').write(h)
print('ok')
