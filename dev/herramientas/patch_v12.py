p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
LOCK='<svg class="lk-i" viewBox="0 0 16 16" aria-hidden="true"><path d="M4.5 7V5a3.5 3.5 0 0 1 7 0v2" fill="none" stroke="currentColor" stroke-width="2"/><rect x="2.5" y="7" width="11" height="8" rx="2" fill="currentColor"/></svg>'

# ---------- CSS ----------
rep("#mapCv{width:min(100%,360px);height:auto;aspect-ratio:360/200;max-width:100%;border-radius:16px}",
"#mapCv{width:min(100%,440px);height:auto;aspect-ratio:16/9;max-width:100%;border-radius:16px;border:1px solid rgba(255,255,255,.18);box-shadow:0 10px 28px rgba(0,0,0,.45)}\n"
".prog{display:flex;gap:4px;justify-content:center;flex-wrap:wrap}\n"
".prog span{width:22px;height:22px;border-radius:50%;display:grid;place-items:center;font-family:var(--cond);font-weight:800;font-size:12px;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);color:var(--dim)}\n"
".prog span.ok{background:var(--lime);color:#0b2a12;border-color:transparent}.prog span.on{background:var(--orange);color:#fff;border-color:#fff}")
rep("@media (prefers-reduced-motion:reduce){.gmoto canvas",
"""/* iPhone: cada pantalla en su propia capa, siempre pintada encima del mar */
#cv{z-index:0}
.screen{-webkit-transform:translateZ(0);transform:translateZ(0)}
/* centrado que no corta cuando no cabe */
.screen:not(.bar){justify-content:flex-start}
.screen:not(.bar)>:first-child{margin-top:auto}
.screen:not(.bar)>:last-child{margin-bottom:auto}
@media (max-height:760px){.logo .l1{font-size:clamp(34px,10vw,56px)}.logo .l2{font-size:clamp(50px,16vw,90px)}.tagline{font-size:15px;margin-top:2px}}
@media (orientation:landscape) and (max-height:560px){.av{padding:4px}.av canvas{width:min(44px,100%)}.screen{gap:8px}}
/* usuario */
.ucard{width:min(100%,320px);display:flex;align-items:center;gap:10px;padding:8px 10px;text-align:left}
.ucard canvas{width:44px;height:44px;border-radius:50%;flex:none;border:2px solid var(--orange)}
.ucard .ui{flex:1;min-width:0;display:flex;flex-direction:column;gap:1px}
.ucard b{font-family:var(--cond);font-weight:800;font-size:18px;line-height:1.05;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ucard span{font-family:var(--cond);font-weight:700;font-size:13px;color:var(--dim);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ucard em{font-style:normal;color:var(--gold)}
.ucard .btn{width:auto;flex:none;padding:9px 14px;font-size:15px}
/* carrera libre */
.fgrid{width:min(100%,440px);display:grid;grid-template-columns:1fr 1fr;gap:8px}
.fz{padding:0;border:2px solid rgba(255,255,255,.16);border-radius:12px;overflow:hidden;background:#0b2a4a;box-shadow:0 6px 14px rgba(0,0,0,.3)}
.fz canvas{display:block;width:100%;height:auto;aspect-ratio:16/9}
.fz:active{transform:scale(.97)}
@media (orientation:landscape){.fgrid{grid-template-columns:repeat(3,1fr);width:min(100%,720px)}}
/* taller */
.lk-i{width:14px;height:14px;flex:none;vertical-align:-2px}
.spv{position:relative;flex:1;min-width:0}
.gmoto.lk canvas{filter:grayscale(1) brightness(.5)}
.lockov{position:absolute;inset:0;display:grid;place-items:center;pointer-events:none;color:#fff}
.lockov .lk-i{width:44px;height:44px;filter:drop-shadow(0 3px 6px rgba(0,0,0,.5))}
.sname{width:min(100%,440px);display:flex;justify-content:space-between;align-items:center;gap:8px}
.sname b{font-family:var(--cond);font-weight:800;font-size:28px;line-height:1;letter-spacing:.04em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.stag{flex:none;font-family:var(--cond);font-weight:800;font-size:14px;padding:4px 10px;border-radius:999px;display:inline-flex;align-items:center;gap:5px;white-space:nowrap}
.stag.own{background:rgba(123,227,90,.16);color:var(--lime);border:1px solid rgba(123,227,90,.5)}
.stag.buy{background:rgba(255,201,60,.14);color:var(--gold);border:1px solid rgba(255,201,60,.45)}
.stag.lock{background:rgba(255,255,255,.08);color:var(--dim);border:1px solid rgba(255,255,255,.22)}
.slist{width:min(100%,440px);display:grid;gap:6px;text-align:left}
.prt{display:grid;grid-template-columns:40px minmax(0,1fr) auto;gap:9px;align-items:center;padding:6px 8px;border-radius:12px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12)}
.prt canvas{width:40px;height:40px;border-radius:10px;background:radial-gradient(circle at 40% 30%,#24406e,#0c1c3a)}
.prt .nm{font-family:var(--cond);font-weight:700;font-size:15px;line-height:1}
.prt .ef{font-size:11px;color:var(--dim);margin-top:2px}
.prt .lv{display:flex;gap:3px;margin-top:4px;align-items:center;max-width:160px}.prt .lv i{flex:1;height:4px;border-radius:2px;background:rgba(255,255,255,.15)}.prt .lv i.on{background:var(--cyan)}
.prt .btn{width:auto;min-width:88px;padding:8px 10px;font-size:14px;display:inline-flex;align-items:center;justify-content:center;gap:4px;white-space:nowrap}
.prt .btn.max{background:rgba(123,227,90,.16);color:var(--lime);border-color:rgba(123,227,90,.5);opacity:1}
.snote{margin:0;font-size:13px;color:var(--dim);text-align:center}
.card .pr.lkt{color:var(--dim);display:flex;align-items:center;gap:4px;font-size:13px}
.sw{display:grid;place-items:center;color:#fff}.sw.lk{opacity:.5}.sw .lk-i{width:13px;height:13px;filter:drop-shadow(0 1px 1px rgba(0,0,0,.6))}
.rl b{text-align:right}
@media (prefers-reduced-motion:reduce){.gmoto canvas""")

# ---------- HTML ----------
rep("""      <p class="tagline">CARRERAS DE MOTOS DE AGUA</p>
      <div class="menu">
        <button class="btn p" id="bPlay">JUGAR</button>
        <button class="btn" id="bRank">RANKING TOP 10</button>""",
"""      <p class="tagline">CARRERAS DE MOTOS DE AGUA</p>
      <div class="ucard panel"><canvas id="uAv" width="96" height="96"></canvas><div class="ui"><b id="uName">PILOTO</b><span><i class="coin"></i><em id="uCash">0</em> PTA · <span id="uProg"></span></span></div><button class="btn p" id="bShop">TALLER</button></div>
      <div class="menu">
        <button class="btn p" id="bPlay">CAMPEONATO</button>
        <button class="btn" id="bFree">CARRERA LIBRE</button>
        <button class="btn ghost" id="bRank" style="width:100%">RANKING TOP 10</button>""")
rep('<div class="gmoto"><canvas id="gMoto" width="580" height="240"></canvas></div>','<div class="gmoto spv" id="gPv"><canvas id="gMoto" width="580" height="240"></canvas><div class="lockov" id="gLock" hidden>'+LOCK+'</div></div>')
rep('<button class="btn" id="gPaint" style="flex:1">PINTAR</button>','<button class="btn" id="gPaint" style="flex:1">TALLER</button>')
rep("""      <canvas id="mapCv" width="720" height="400"></canvas>
      <div class="mcard panel"><small id="mZoneN"></small><h2 id="mZoneName"></h2><p id="mGoal"></p><div class="minfo" id="mInfo"></div></div>
      <div class="menu"><button class="btn p" id="mGo">¡AL AGUA!</button></div>""",
"""      <canvas id="mapCv" width="880" height="495"></canvas>
      <div class="prog" id="mProg"></div>
      <div class="mcard panel"><small id="mZoneN"></small><h2 id="mZoneName"></h2><p id="mGoal"></p><div class="minfo" id="mInfo"></div></div>
      <div class="menu"><button class="btn p" id="mGo">¡AL AGUA!</button><button class="btn ghost" id="mBack" style="width:100%" hidden>‹ OTRA PANTALLA</button></div>""")
rep("""    <section id="scrMap" class="screen" hidden>""",
"""    <section id="scrFree" class="screen" hidden>
      <div class="head"><button class="btn ghost sm" id="fBack" style="flex:none">‹ VOLVER</button><h2 class="h">CARRERA LIBRE</h2><span style="width:70px"></span></div>
      <p class="sub">Elige pantalla. Lo que ganes va a tu monedero.</p>
      <div class="fgrid" id="fGrid"></div>
    </section>

    <section id="scrShop" class="screen" hidden>
      <div class="head"><button class="btn ghost sm" id="sBack" style="flex:none">‹ VOLVER</button><h2 class="h">TALLER</h2><div class="cash"><i class="coin"></i><span class="cashv">0</span></div></div>
      <div class="garage">
        <button class="nav" id="sPrev" aria-label="Moto anterior"><svg viewBox="0 0 16 16"><path d="M11 2 4 8l7 6" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
        <div class="gmoto spv" id="sPv"><canvas id="sCv" width="580" height="240"></canvas><div class="lockov" id="sLock" hidden>"""+LOCK+"""</div></div>
        <button class="nav" id="sNext" aria-label="Moto siguiente"><svg viewBox="0 0 16 16"><path d="M5 2l7 6-7 6" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button>
      </div>
      <div class="sname"><b id="sName"></b><span class="stag" id="sTag"></span></div>
      <div class="dots" id="sDots"></div>
      <div class="slist" id="sList"></div>
      <div class="row" style="width:min(100%,440px);flex-wrap:nowrap"><button class="btn" id="sPaint" style="flex:1">PINTAR</button><button class="btn p" id="sMain" style="flex:1.5"></button></div>
    </section>

    <section id="scrMap" class="screen" hidden>""")

# ---------- DATOS ----------
rep("const SWATCHES=[","""const LOCK_SVG='"""+LOCK+"""';
const SHOP={brava:[0,0],oceano:[0,0],solar:[0,0],avispa:[2500,0],marea:[3500,2],inferno:[5000,3],veneno:[6500,5],sombra:[9000,7]};
const PART_NEED=[0,2,5],PAINT_PRICE=200,SWATCH_PRO=['#e0b13a','#c9ced6','#ff2bd6','#00e0b0'],PRO_NEED=4;
let ownList=store.get('ct_own',null);if(!Array.isArray(ownList))ownList=Object.keys(SHOP).filter(k=>!SHOP[k][0]);
const owns=m=>ownList.includes(m.id);
let best=Math.max(0,Math.min(10,store.get('ct_best',0)|0));
let partsStore=store.get('ct_parts',{});if(!partsStore||typeof partsStore!=='object')partsStore={};
function partsOf(m){return partsStore[m.id]||(partsStore[m.id]={});}
function saveParts(){store.set('ct_parts',partsStore);}
function motoState(m){if(owns(m))return 'own';const n=(SHOP[m.id]||[0,0])[1];return best<n?'lock':'buy';}
function unlocksBetween(a,b){const u=[];for(const m of MOTOS){const[pr,n]=SHOP[m.id]||[0,0];if(pr&&n>a&&n<=b)u.push('moto '+m.name);}PART_NEED.forEach((n,i)=>{if(i&&n>a&&n<=b)u.push('piezas nivel '+(i+1));});if(PRO_NEED>a&&PRO_NEED<=b)u.push('colores especiales');return u;}
const SWATCHES=[""")
rep("const G={mode:'title',zi:0,lap:0,lives:3,money:0,","const G={mode:'title',zi:0,lap:0,lives:3,money:Math.max(0,Math.round(+store.get('ct_wallet',1500)||0)),")
rep("let input={left:false,right:false,acc:false,turbo:false};","""if(!owns(MOTOS[G.moto]))G.moto=Math.max(0,MOTOS.findIndex(owns));
function saveWallet(){G._wm=G.money;store.set('ct_wallet',Math.max(0,Math.round(G.money)));}
setInterval(()=>{if(G.money!==G._wm)saveWallet();},1500);
let input={left:false,right:false,acc:false,turbo:false};""")
rep("goal:'Llega a El Mago entre los 3 primeros. La isla la puedes rodear por los dos lados y antes de la meta hay muchos barcos fondeados.',len:16000,riv:5,bar:null,theme:'cove',tod:'noon',skill:.88,piri:1,island:1,anchored:1,finish:'EL MAGO'}",
    "goal:'Llega a El Mago entre los 3 primeros. La costa queda a la derecha, la isla la puedes rodear por los dos lados y antes de la meta hay muchos barcos fondeados.',len:16000,riv:5,bar:null,theme:'cove',tod:'noon',skill:.88,piri:1,island:1,anchored:1,finish:'EL MAGO',mirror:1}")

# ---------- FLUJO ----------
rep("function show(id){screens.forEach(s=>s.hidden=s.id!==id);$('#app').classList.toggle('nopads',id==='scrJJ'||id==='scrRoxy'||id==='scrPaint'||id==='scrPilot');}",
"""const NOPADS=['scrJJ','scrRoxy','scrPaint','scrPilot','scrShop','scrFree'];
function show(id){screens.forEach(s=>s.hidden=s.id!==id);$('#app').classList.toggle('nopads',NOPADS.includes(id));
 const el=id&&document.getElementById(id);if(el){el.scrollTop=0;requestAnimationFrame(()=>{el.style.opacity='.995';requestAnimationFrame(()=>{el.style.opacity='';});});}}""")
rep("function goTitle(){Snd.engineStop();Snd.sirenStop();$('#hud').hidden=true;$('#msg').hidden=true;demoStart();show('scrTitle');Music.play('menu');wake(false);}",
"""function goTitle(){Snd.engineStop();Snd.sirenStop();$('#hud').hidden=true;$('#msg').hidden=true;demoStart();show('scrTitle');renderUser();Music.play('menu');wake(false);}
function toTitle(){if(G.mode!=='demo'){goTitle();return;}show('scrTitle');renderUser();}
function renderUser(){drawPortrait($('#uAv'),AVATARS[G.avatar|0]||AVATARS[0]);$('#uName').textContent=pilotName();$('#uCash').textContent=pts(G.money);$('#uProg').textContent='Campeonato '+best+'/'+ZONES.length;}""")
rep("function newGame(){G.demo=false;G.zi=0;G.lap=0;G.lives=3;G.money=500;G.score=0;G.fuel=100;G.turbo=2;G.parts={};store.set('ct_moto',G.moto);goMap();}",
"""function newGame(){G.free=false;G.demo=false;G.zi=0;G.lap=0;G.lives=3;G.score=0;G.fuel=100;G.turbo=2;G.parts=partsOf(MOTOS[G.moto]);store.set('ct_moto',G.moto);goMap();}
function startFree(zi){G.free=true;G.demo=false;G.zi=zi;G.lap=0;G.lives=3;G.score=0;G.fuel=100;G.turbo=2;G.parts=partsOf(MOTOS[G.moto]);store.set('ct_moto',G.moto);goMap();}
function goFree(){G.free=true;if(G.mode!=='demo'){Snd.engineStop();Snd.sirenStop();$('#hud').hidden=true;$('#msg').hidden=true;demoStart();wake(false);}show('scrFree');renderFree();Music.play('menu');}
function renderFree(){const F=$('#fGrid');F.textContent='';ZONES.forEach((Z,i)=>{const b=document.createElement('button');b.className='fz';b.setAttribute('aria-label','Zona '+(i+1)+' '+Z.name);const c=document.createElement('canvas');c.width=400;c.height=225;b.append(c);drawCover(c,i);b.addEventListener('click',()=>{Snd.click();startFree(i);});F.append(b);});
 fontsOK.then(()=>{if(!$('#scrFree').hidden)F.querySelectorAll('canvas').forEach((c,i)=>drawCover(c,i));});}""")
# result / win / fail / over
rep(" const last=G.zi===ZONES.length-1;\n showResult(last?",
""" const last=G.zi===ZONES.length-1;saveWallet();
 if(G.free){showResult('¡PANTALLA SUPERADA!','Carrera libre · '+Z.name,lines,()=>goFree());return;}
 const nb=Math.max(best,G.lap>0?ZONES.length:G.zi+1);if(nb>best){const un=unlocksBetween(best,nb);best=nb;store.set('ct_best',best);if(un.length)lines.push(['¡Desbloqueado!',un.join(' · ')]);}
 showResult(last?""")
rep("function gameOver(){G.mode='over';Snd.engineStop();Snd.sirenStop();$('#hud').hidden=true;Music.play('menu');wake(false);",
"""function gameOver(){G.mode='over';Snd.engineStop();Snd.sirenStop();$('#hud').hidden=true;Music.play('menu');wake(false);saveWallet();
 if(G.free){showResult('¡SIN VIDAS!','Se acabó esta carrera libre. Las pesetas que has ganado se quedan en tu monedero.',[['Zona',(G.zi+1)+' · '+G.zone.Z.name],['Monedero',pts(G.money)+' PTA']],()=>goFree());return;}""")
# map
rep("function renderMap(retry){const Z=ZONES[G.zi];$('#mZoneN').textContent=(retry?'OTRA VEZ · ':'')+'ZONA '+(G.zi+1)+' DE '+ZONES.length+(G.lap?' · VUELTA '+(G.lap+1):'');",
    "function renderMap(retry){const Z=ZONES[G.zi];$('#mZoneN').textContent=(retry?'OTRA VEZ · ':'')+(G.free?'CARRERA LIBRE · ZONA '+(G.zi+1):'CAMPEONATO · ZONA '+(G.zi+1)+' DE '+ZONES.length+(G.lap?' · VUELTA '+(G.lap+1):''));")
i0=s.index(" const c=$('#mapCv'),g=c.getContext('2d');g.setTransform(2,0,0,2,0,0);const W=360,H=200;")
i1=s.index("g.fillText('LA COSTA',10,190);}",i0)+len("g.fillText('LA COSTA',10,190);}")
s=s[:i0]+""" const c=$('#mapCv');drawCover(c,G.zi);fontsOK.then(()=>{if(!$('#scrMap').hidden)drawCover(c,G.zi);});
 const P=$('#mProg');P.hidden=!!G.free;P.textContent='';if(!G.free)ZONES.forEach((_,i)=>{const sp=document.createElement('span');sp.textContent=i+1;if(i<G.zi)sp.className='ok';else if(i===G.zi)sp.className='on';P.append(sp);});
 $('#mBack').hidden=!G.free;}"""+s[i1:]
# roxy
rep("""PARTS.forEach((p,i)=>{const lv=Math.min(3,G.parts[p.id]|0),next=lv<3?p.price[lv]:0;const d=document.createElement('button');d.className='card'+(i===G._sel?' sel':'')+(lv<3&&G.money<next?' poor':'');""",
"""PARTS.forEach((p,i)=>{const lv=Math.min(3,G.parts[p.id]|0),next=lv<3?p.price[lv]:0,lk=lv<3&&best<PART_NEED[lv];const d=document.createElement('button');d.className='card'+(i===G._sel?' sel':'')+(lv<3&&!lk&&G.money<next?' poor':'');""")
rep("""(lv>=3?'<span class="ok">NIVEL MÁXIMO</span>':`<div class="pr">${pts(next)} PTA</div>`);""",
"""(lv>=3?'<span class="ok">NIVEL MÁXIMO</span>':lk?`<div class="pr lkt">${LOCK_SVG} ZONA ${PART_NEED[lv]}</div>`:`<div class="pr">${pts(next)} PTA</div>`);""")
rep("""b=$('#rxBuy');if(lv>=3){b.textContent='NIVEL MÁXIMO';b.disabled=true;}else{""",
"""b=$('#rxBuy');if(lv>=3){b.textContent='NIVEL MÁXIMO';b.disabled=true;}else if(best<PART_NEED[lv]){b.innerHTML=LOCK_SVG+' SUPERA LA ZONA '+PART_NEED[lv];b.disabled=true;}else{""")
rep("on('#rxBuy',()=>{const p=PARTS[G._sel],lv=Math.min(3,G.parts[p.id]|0);if(lv>=3)return;const pr=p.price[lv];if(G.money<pr)return;G.money-=pr;G.parts[p.id]=lv+1;",
    "on('#rxBuy',()=>{const p=PARTS[G._sel],lv=Math.min(3,G.parts[p.id]|0);if(lv>=3||best<PART_NEED[lv])return;const pr=p.price[lv];if(G.money<pr)return;G.money-=pr;G.parts[p.id]=lv+1;saveParts();saveWallet();")
# garage
rep("function renderGarage(){const m=MOTOS[G.moto];$('#gCard').style.setProperty('--sc',m.ui);",
    "function renderGarage(){const m=MOTOS[G.moto],ms=motoState(m),[mpr,mneed]=SHOP[m.id]||[0,0];$('#gCard').style.setProperty('--sc',m.ui);$('#gPv').classList.toggle('lk',ms!=='own');$('#gLock').hidden=ms==='own';$('#gGo').textContent=ms==='own'?(G.free?'ELEGIR Y VER PANTALLAS':'ELEGIR ESTA MOTO'):'CONSEGUIRLA EN EL TALLER';")
rep("$('#gColors').textContent=paintOf(m).colors?'Pintura personalizada':m.colors;",
    "$('#gColors').textContent=ms==='buy'?'En el taller: '+pts(mpr)+' PTA':ms==='lock'?'Se desbloquea en la zona '+mneed:paintOf(m).colors?'Pintura personalizada':m.colors;")
# pintura + taller (bloque entero)
i0=s.index("function paintPreview(){const m=MOTOS[G.moto]")
i1=s.index("on('#gGo',()=>{Snd.click();newGame();});",i0)+len("on('#gGo',()=>{Snd.click();newGame();});")
s=s[:i0]+"""const paintM=()=>MOTOS[shopI]||MOTOS[G.moto];
function paintChanged(){const a=G._draft,b=paintOf(paintM());return['colors','hull','deck','hood','stripe','seat'].some(k=>String(a[k])!==String(b[k]));}
function paintBtn(){const ch=paintChanged(),b=$('#pSave');b.textContent=ch?'GUARDAR · '+PAINT_PRICE+' PTA':'GUARDAR';b.disabled=ch&&G.money<PAINT_PRICE;}
function paintPreview(){const m=paintM(),c=$('#pCv'),g=c.getContext('2d');g.setTransform(2,0,0,2,0,0);g.clearRect(0,0,290,120);g.save();g.translate(2,4);g.scale(.836,.836);drawJetProfile(g,sideOf(m,G._draft));g.restore();paintBtn();}
function paintRows(){const d=G._draft,R=$('#pRows');R.textContent='';const proLock=best<PRO_NEED;for(const[k,l]of PAINT_PARTS){const row=document.createElement('div');row.className='prow';const sp=document.createElement('span');sp.textContent=l;const sw=document.createElement('div');sw.className='sws';
  for(const col of SWATCHES.concat(SWATCH_PRO)){const lk=proLock&&SWATCH_PRO.includes(col);const b=document.createElement('button');b.className='sw'+(String(d[k]).toLowerCase()===col?' on':'')+(lk?' lk':'');b.style.background=col;b.setAttribute('aria-label',l+' '+col+(lk?' bloqueado':''));if(lk){b.innerHTML=LOCK_SVG;b.disabled=true;}
   b.addEventListener('click',()=>{if(lk)return;d[k]=col;d.colors=true;Snd.click();sw.querySelectorAll('.sw').forEach(x=>x.classList.toggle('on',x===b));paintPreview();});sw.append(b);}
  row.append(sp,sw);R.append(row);}}
function goPaint(){const m=paintM();G._draft=Object.assign({},paintOf(m));show('scrPaint');$('#pName').value=G._draft.name||'';paintRows();paintPreview();}
$('#pName').addEventListener('input',e=>{G._draft.name=e.target.value.toUpperCase().replace(/[^A-Z0-9ÁÉÍÓÚÜÑ .\\-_]/g,'').trim().slice(0,12);paintPreview();});
on('#gPaint',()=>{Snd.click();goShop('garage');});
on('#pBack',()=>{Snd.click();backShop();});
on('#pReset',()=>{const m=paintM();G._draft=Object.assign(defaultPaint(m),{name:G._draft.name});Snd.click();paintRows();paintPreview();});
on('#pSave',()=>{const m=paintM(),ch=paintChanged();if(ch&&G.money<PAINT_PRICE)return;if(ch){G.money-=PAINT_PRICE;saveWallet();}paintStore[m.id]=Object.assign({},G._draft);store.set('ct_paint',paintStore);SP.jet[m.id]=sprite(32,68,g=>drawJet(g,skOf(m)));SP.jetP=sprite(32,68,g=>drawJet(g,playerSk()));Snd.cash();backShop();});on('#gPrev',()=>changeMoto(-1));on('#gNext',()=>changeMoto(1));
on('#gGo',()=>{Snd.click();const m=MOTOS[G.moto];if(!owns(m)){goShop('garage');return;}store.set('ct_moto',G.moto);if(G.free)goFree();else newGame();});
/* ---- taller ---- */
let shopI=0,shopFrom='title';
function goShop(from){shopFrom=from||'title';shopI=G.moto;show('scrShop');renderShop();Music.play('menu');}
function backShop(){show('scrShop');renderShop();}
function renderShop(){const m=MOTOS[shopI],st=motoState(m),[price,need]=SHOP[m.id]||[0,0];cashUI();
 const c=$('#sCv'),g=c.getContext('2d');g.setTransform(2,0,0,2,0,0);g.clearRect(0,0,290,120);g.save();g.translate(2,4);g.scale(.836,.836);drawJetProfile(g,sideOf(m));g.restore();
 $('#sPv').classList.toggle('lk',st==='lock');$('#sLock').hidden=st!=='lock';
 const nm=$('#sName');nm.textContent=motoName(m);nm.style.color=m.ui;
 const tg=$('#sTag');tg.className='stag '+st;tg.innerHTML=st==='own'?(shopI===G.moto?'EN USO':'ES TUYA'):st==='buy'?'<i class="coin"></i>'+pts(price)+' PTA':LOCK_SVG+' ZONA '+need;
 const D=$('#sDots');D.textContent='';MOTOS.forEach((_,i)=>{const sp=document.createElement('span');if(i===shopI)sp.className='on';D.append(sp);});
 const L=$('#sList');L.textContent='';
 if(st==='own'){const parts=partsOf(m);PARTS.forEach(p=>{const lv=Math.min(3,parts[p.id]|0),nd=PART_NEED[lv],lk=lv<3&&best<nd,pr=lv<3?p.price[lv]:0;const row=document.createElement('div');row.className='prt';row.append(iconCanvas(ICONS[p.id]));
   const inf=document.createElement('div');inf.innerHTML=`<div class="nm"></div><div class="ef"></div><div class="lv">${[0,1,2].map(k=>`<i class="${k<lv?'on':''}"></i>`).join('')}</div>`;inf.querySelector('.nm').textContent=p.name+' · nivel '+lv+'/3';inf.querySelector('.ef').textContent=p.ef;row.append(inf);
   const b=document.createElement('button');b.className='btn'+(lv>=3?' max':lk?'':' p');
   if(lv>=3){b.textContent='MÁXIMO';b.disabled=true;}else if(lk){b.innerHTML=LOCK_SVG+' ZONA '+nd;b.disabled=true;}else{b.textContent=pts(pr);b.disabled=G.money<pr;}
   b.addEventListener('click',()=>{if(lv>=3||lk||G.money<pr)return;G.money-=pr;parts[p.id]=lv+1;saveParts();saveWallet();Snd.cash();renderShop();});row.append(b);L.append(row);});}
 else{const S2=document.createElement('div');S2.className='stats';for(const[k,l]of[['vel','VELOCIDAD'],['ace','ACELERACIÓN'],['giro','GIRO'],['turbo','TURBO']]){const row=document.createElement('div');row.className='st';const a=document.createElement('span');a.textContent=l;const bb=document.createElement('i');for(let j=0;j<5;j++){const x=document.createElement('b');if(j<m.st[k])x.className='on';bb.append(x);}row.append(a,bb);S2.append(row);}L.append(S2);
  const n=document.createElement('p');n.className='snote';n.textContent=st==='lock'?'Bloqueada: supera la zona '+need+' del campeonato y luego cómprala aquí.':'Cómprala para poder correr con ella, pintarla y meterle piezas.';L.append(n);}
 const pb=$('#sPaint');pb.disabled=st!=='own';pb.textContent='PINTAR · '+PAINT_PRICE;
 const mb=$('#sMain');if(st==='own'){mb.textContent=shopI===G.moto?'EN USO':'USAR ESTA MOTO';mb.disabled=shopI===G.moto;}else if(st==='buy'){mb.textContent='COMPRAR · '+pts(price);mb.disabled=G.money<price;}else{mb.innerHTML=LOCK_SVG+' ZONA '+need;mb.disabled=true;}}
on('#sPrev',()=>{shopI=(shopI-1+MOTOS.length)%MOTOS.length;Snd.click();renderShop();});on('#sNext',()=>{shopI=(shopI+1)%MOTOS.length;Snd.click();renderShop();});
on('#sMain',()=>{const m=MOTOS[shopI],st=motoState(m);if(st==='own'){G.moto=shopI;store.set('ct_moto',G.moto);SP.jetP=sprite(32,68,g=>drawJet(g,playerSk()));Snd.click();renderShop();return;}if(st!=='buy')return;const pr=SHOP[m.id][0];if(G.money<pr)return;G.money-=pr;ownList.push(m.id);store.set('ct_own',ownList);saveWallet();G.moto=shopI;store.set('ct_moto',G.moto);Snd.cash();renderShop();});
on('#sPaint',()=>{if(!owns(MOTOS[shopI]))return;Snd.click();goPaint();});
on('#sBack',()=>{Snd.click();if(shopFrom==='garage')goGarage();else toTitle();});
on('#bShop',()=>{Snd.click();goShop('title');});
on('#bFree',()=>{Snd.click();G.free=true;goPilot();});
on('#fBack',()=>{Snd.click();goTitle();});
on('#mBack',()=>{Snd.click();goFree();});"""+s[i1:]
rep("on('#bPlay',()=>{Snd.click();goPilot();});","on('#bPlay',()=>{Snd.click();G.free=false;goPilot();});")
rep("on('#oAgain',()=>{Snd.click();goPilot();});","on('#oAgain',()=>{Snd.click();G.free=false;goPilot();});")
rep("on('#rxFuel',()=>{if(G.money<300||G.fuel>=99)return;G.money-=300;","on('#rxFuel',()=>{if(G.money<300||G.fuel>=99)return;G.money-=300;saveWallet();")
rep("resize();labels();demoStart();show('scrTitle');Music.play('menu');","resize();labels();demoStart();show('scrTitle');renderUser();fontsOK.then(()=>renderUser());Music.play('menu');")
# insert cover code before ranking
cov=open('cover.js').read()
rep("/* ---- ranking ---- */",cov+"\n/* ---- ranking ---- */")
open(p,'w').write(s);print('ok')
