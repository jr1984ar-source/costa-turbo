p='costa-turbo.html';s=open(p,encoding='utf-8').read()
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:110])
    s=s.replace(a,b)
# --- PARTS with levels + paint helpers
a=s.index('const PARTS=[');b=s.index('];',a)+2
s=s[:a]+'''const PARTS=[
 {id:'turbo',name:'Turbo',ef:'Más aceleración',price:[3000,5000,8000]},
 {id:'bov',name:'Válvula de descarga',ef:'«Pssshh» y recarga turbos',price:[1500,2500,4000]},
 {id:'escape',name:'Escape deportivo',ef:'Más punta y más ruido',price:[2000,3500,5500]},
 {id:'turbina',name:'Turbina',ef:'Más velocidad máxima',price:[2500,4500,7000]},
 {id:'intercooler',name:'Intercooler',ef:'El turbo dura más',price:[1800,3000,4800]},
 {id:'aletas',name:'Aletas',ef:'Gira mejor',price:[1200,2200,3500]}
];
const SWATCHES=['#f4f5f7','#b8c0cc','#3a3e46','#16181d','#e3202b','#ff7a1a','#ffd21a','#7be35a','#1f9e52','#19c3c9','#1e5eff','#13285e','#7b3fe4','#ff3f8e'];
const PAINT_PARTS=[['hull','CASCO'],['deck','LATERALES'],['hood','CAPÓ'],['stripe','RAYAS'],['seat','ASIENTO']];
let paintStore=store.get('ct_paint',{});if(!paintStore||typeof paintStore!=='object')paintStore={};
function defaultPaint(m){const s=m.side;return{colors:false,hull:s.hull,deck:s.deck,hood:s.hood,stripe:s.stripe,seat:s.seatA,name:''};}
function paintOf(m){if(!m.side)return{colors:false,name:''};const p=paintStore[m.id];return p?Object.assign(defaultPaint(m),p):defaultPaint(m);}
function sideOf(m,p){p=p||paintOf(m);const b=Object.assign({},m.side);if(p.colors)Object.assign(b,{hull:p.hull,deck:p.deck,hood:p.hood,stripe:p.stripe,seatA:p.seat,seatB:p.hood});b.name=p.name||'';return b;}
function skOf(m,p){if(!m.side)return m.sk;p=p||paintOf(m);if(!p.colors)return m.sk;return Object.assign({},m.sk,{hull:p.deck,hullD:mixc(p.deck,'#000000',.35),acc:p.hood!==p.deck?p.hood:p.stripe,seat:p.seat});}
function motoName(m){return paintOf(m).name||m.name;}'''+s[b:]
# --- stats with levels
rep(" if(parts.turbo){acc*=1.25;bm+=.08;}if(parts.escape)maxV*=1.05;if(parts.turbina)maxV*=1.09;if(parts.intercooler)bt*=1.5;if(parts.aletas)turn*=1.3;return{maxV,acc,turn,bt,bm};}",
    " const L=k=>Math.min(3,parts[k]|0);acc*=1+.22*L('turbo');bm+=.07*L('turbo');maxV*=1+.045*L('escape');maxV*=1+[0,.08,.14,.19][L('turbina')];bt*=[1,1.5,1.9,2.3][L('intercooler')];turn*=[1,1.3,1.5,1.7][L('aletas')];return{maxV,acc,turn,bt,bm};}")
rep("  if(G.parts.bov){G.regenT+=dt;if(G.regenT>=25){G.regenT=0;",
    "  const iv=[0,25,18,12][Math.min(3,G.parts.bov|0)];if(iv){G.regenT+=dt;if(G.regenT>=iv){G.regenT=0;")
# --- engine sound by exhaust level
rep("if(e.ex!==exh){e.ws.curve=this.curve(exh?7:2);e.ex=exh;}","if(e.ex!==exh){e.ws.curve=this.curve(2+exh*2.5);e.ex=exh;}")
rep("(260+rpm*2100)*(exh?1.25:1)","(260+rpm*2100)*(1+exh*.1)")
rep("(.03+thr*.042+rpm*.042)*(exh?1.45:1)","(.03+thr*.042+rpm*.042)*(1+exh*.18)")
rep("G.parts.escape?1:0","Math.min(3,G.parts.escape|0)")
# --- sprites & colors use paint
rep("for(const m of[...MOTOS,SHARK])SP.jet[m.id]=sprite(32,68,g=>drawJet(g,m.sk));","for(const m of[...MOTOS,SHARK])SP.jet[m.id]=sprite(32,68,g=>drawJet(g,skOf(m)));")
rep("d.style.background=c.m.sk.hull;c._dot=d;","d.style.background=skOf(c.m).hull;c._dot=d;")
rep("drawJetProfile(g,MOTOS[G.moto].side);","drawJetProfile(g,sideOf(MOTOS[G.moto]));")
rep("$('#gName').textContent=m.name;$('#gColors').textContent=m.colors;","$('#gName').textContent=motoName(m);$('#gColors').textContent=paintOf(m).colors?'Pintura personalizada':m.colors;")
rep("g.save();g.translate(2,4);g.scale(.836,.836);drawJetProfile(g,m.side);g.restore();","g.save();g.translate(2,4);g.scale(.836,.836);drawJetProfile(g,sideOf(m));g.restore();")
# name decal on profile (after the hull block restore: insert before sponson)
rep(" g.fillStyle=s.trim;g.beginPath();g.moveTo(58,103);g.lineTo(150,99);g.lineTo(157,102);g.lineTo(64,107);g.closePath();g.fill();",
    " if(s.name){const hx=s.hull.replace('#',''),lum=(parseInt(hx.slice(0,2),16)*.3+parseInt(hx.slice(2,4),16)*.59+parseInt(hx.slice(4,6),16)*.11)/255;g.save();g.translate(104,92);g.rotate(-.035);g.font='800 17px \"Saira Condensed\",sans-serif';g.textAlign='center';g.textBaseline='middle';g.transform(1,0,-.22,1,0,0);g.lineWidth=3;g.strokeStyle=lum>.62?'rgba(255,255,255,.6)':'rgba(0,0,0,.45)';g.strokeText(s.name,0,0);g.fillStyle=lum>.62?'#16181d':'#ffffff';g.fillText(s.name,0,0);g.restore();}\n g.fillStyle=s.trim;g.beginPath();g.moveTo(58,103);g.lineTo(150,99);g.lineTo(157,102);g.lineTo(64,107);g.closePath();g.fill();")
# --- Roxy levels
a=s.index('function renderRoxy(){');b=s.index('/* ---- dibujos de los bares')
s=s[:a]+'''function renderRoxy(){cashUI();const Gd=$('#rxGrid');Gd.textContent='';
 PARTS.forEach((p,i)=>{const lv=Math.min(3,G.parts[p.id]|0),next=lv<3?p.price[lv]:0;const d=document.createElement('button');d.className='card'+(i===G._sel?' sel':'')+(lv<3&&G.money<next?' poor':'');d.append(iconCanvas(ICONS[p.id]));const info=document.createElement('div');
  info.innerHTML=`<div class="nm"></div><div class="ef"></div><div class="lv lv3">${[0,1,2].map(k=>`<i class="${k<lv?'on':''}"></i>`).join('')}<em>NIVEL ${lv}/3</em></div>`+(lv>=3?'<span class="ok">NIVEL MÁXIMO</span>':`<div class="pr">${pts(next)} PTA</div>`);
  info.querySelector('.nm').textContent=p.name;info.querySelector('.ef').textContent=p.ef;d.append(info);d.addEventListener('click',()=>{G._sel=i;Snd.click();renderRoxy();});Gd.append(d);});
 const p=PARTS[G._sel],lv=Math.min(3,G.parts[p.id]|0),b=$('#rxBuy');if(lv>=3){b.textContent='NIVEL MÁXIMO';b.disabled=true;}else{const pr=p.price[lv];b.textContent=(lv?'NIVEL '+(lv+1)+' · ':'COMPRAR · ')+pts(pr);b.disabled=G.money<pr;}
 const f=$('#rxFuel');f.textContent=G.fuel>=99?'DEPÓSITO LLENO':'GASOLINA · 300';f.disabled=G.fuel>=99||G.money<300;}

'''+s[b:]
rep("on('#rxBuy',()=>{const p=PARTS[G._sel];if(G.parts[p.id]||G.money<p.price)return;G.money-=p.price;G.parts[p.id]=1;G.P.st=stats(MOTOS[G.moto],G.parts);Snd.cash();msg('¡'+p.name.toUpperCase()+'!','Instalado','var(--lime)');renderRoxy();});",
    "on('#rxBuy',()=>{const p=PARTS[G._sel],lv=Math.min(3,G.parts[p.id]|0);if(lv>=3)return;const pr=p.price[lv];if(G.money<pr)return;G.money-=pr;G.parts[p.id]=lv+1;G.P.st=stats(MOTOS[G.moto],G.parts);Snd.cash();msg('¡'+p.name.toUpperCase()+'!','Nivel '+(lv+1),'var(--lime)');renderRoxy();});")
rep("G._sel=PARTS.findIndex(p=>!G.parts[p.id]);","G._sel=PARTS.findIndex(p=>(G.parts[p.id]|0)<3);")
rep(".card .lv{display:flex;gap:3px;margin-top:5px}",".card .lv{display:flex;gap:3px;margin-top:5px;align-items:center}.card .lv em{flex:none;margin-left:4px;font-style:normal;font-family:var(--cond);font-weight:700;font-size:10px;letter-spacing:.06em;color:var(--dim)}")
# --- ranking with custom name
rep("const en={name,score:G.score|0,zone:G.zi+1,lap:G.lap,moto:MOTOS[G.moto].id,at:Date.now()};","const en={name,score:G.score|0,zone:G.zi+1,lap:G.lap,moto:MOTOS[G.moto].id,mname:paintOf(MOTOS[G.moto]).name||'',at:Date.now()};")
rep("mt.textContent=m.name+' · zona '","mt.textContent=(e.mname?String(e.mname).slice(0,12)+' · ':'')+m.name+' · zona '")
# --- garage button + paint screen
rep('<div class="menu"><button class="btn p" id="gGo">ELEGIR ESTA MOTO</button></div>',
    '<div class="menu"><div class="row" style="flex-wrap:nowrap"><button class="btn" id="gPaint" style="flex:1">PINTAR</button><button class="btn p" id="gGo" style="flex:2">ELEGIR ESTA MOTO</button></div></div>')
rep('    <section id="scrMap" class="screen" hidden>','''    <section id="scrPaint" class="screen" hidden>
      <div class="head"><button class="btn ghost sm" id="pBack" style="flex:none">‹ VOLVER</button><h2 class="h">TALLER</h2><span style="width:70px"></span></div>
      <div class="gmoto pprev"><canvas id="pCv" width="580" height="240"></canvas></div>
      <div class="pname"><label for="pName">NOMBRE DE LA MOTO</label><input id="pName" maxlength="12" autocomplete="off" autocapitalize="characters" spellcheck="false" enterkeyhint="done" placeholder="Escribe un nombre"></div>
      <div class="prows" id="pRows"></div>
      <div class="row" style="width:min(100%,440px);flex-wrap:nowrap"><button class="btn ghost" id="pReset" style="flex:1">COLORES ORIGINALES</button><button class="btn p" id="pSave" style="flex:1">GUARDAR</button></div>
    </section>

    <section id="scrMap" class="screen" hidden>''')
rep("/* resultado / fin / ranking */","""/* taller */
.pprev{width:min(100%,440px);flex:none}
.pname{width:min(100%,440px);display:flex;flex-direction:column;gap:4px;text-align:left}
.pname label,.prow span{font-family:var(--cond);font-weight:700;font-size:12px;letter-spacing:.14em;color:var(--dim)}
#pName{font-family:var(--cond);font-weight:800;font-size:20px;text-transform:uppercase;padding:8px 12px;border-radius:12px;border:1px solid rgba(255,255,255,.3);background:rgba(0,0,0,.3);color:#fff;outline:none;user-select:text;-webkit-user-select:text}
#pName:focus{border-color:var(--orange)}
.prows{width:min(100%,440px);display:grid;gap:6px;text-align:left}
.prow{display:grid;gap:3px;min-width:0}
.sws{display:flex;gap:6px;overflow-x:auto;padding:3px 2px;scrollbar-width:none;touch-action:pan-x}
.sws::-webkit-scrollbar{display:none}
.sw{flex:none;width:30px;height:30px;border-radius:50%;border:2px solid rgba(255,255,255,.28);padding:0}
.sw.on{border-color:#fff;box-shadow:0 0 0 3px var(--orange)}

/* resultado / fin / ranking */""")
rep("$('#app').classList.toggle('nopads',id==='scrJJ'||id==='scrRoxy');","$('#app').classList.toggle('nopads',id==='scrJJ'||id==='scrRoxy'||id==='scrPaint');")
rep("on('#gBack',()=>{Snd.click();goTitle();});","""on('#gBack',()=>{Snd.click();goTitle();});
function paintPreview(){const m=MOTOS[G.moto],c=$('#pCv'),g=c.getContext('2d');g.setTransform(2,0,0,2,0,0);g.clearRect(0,0,290,120);g.save();g.translate(2,4);g.scale(.836,.836);drawJetProfile(g,sideOf(m,G._draft));g.restore();}
function paintRows(){const d=G._draft,R=$('#pRows');R.textContent='';for(const[k,l]of PAINT_PARTS){const row=document.createElement('div');row.className='prow';const sp=document.createElement('span');sp.textContent=l;const sw=document.createElement('div');sw.className='sws';
  for(const col of SWATCHES){const b=document.createElement('button');b.className='sw'+(String(d[k]).toLowerCase()===col?' on':'');b.style.background=col;b.setAttribute('aria-label',l+' '+col);
   b.addEventListener('click',()=>{d[k]=col;d.colors=true;Snd.click();sw.querySelectorAll('.sw').forEach(x=>x.classList.toggle('on',x===b));paintPreview();});sw.append(b);}
  row.append(sp,sw);R.append(row);}}
function goPaint(){const m=MOTOS[G.moto];G._draft=Object.assign({},paintOf(m));show('scrPaint');$('#pName').value=G._draft.name||'';paintRows();paintPreview();}
$('#pName').addEventListener('input',e=>{G._draft.name=e.target.value.toUpperCase().replace(/[^A-Z0-9ÁÉÍÓÚÜÑ .\\-_]/g,'').trim().slice(0,12);paintPreview();});
on('#gPaint',()=>{Snd.click();goPaint();});
on('#pBack',()=>{Snd.click();goGarage();});
on('#pReset',()=>{const m=MOTOS[G.moto];G._draft=Object.assign(defaultPaint(m),{name:G._draft.name});Snd.click();paintRows();paintPreview();});
on('#pSave',()=>{const m=MOTOS[G.moto];paintStore[m.id]=Object.assign({},G._draft);store.set('ct_paint',paintStore);SP.jet[m.id]=sprite(32,68,g=>drawJet(g,skOf(m)));Snd.cash();goGarage();});""")
open(p,'w',encoding='utf-8').write(s)
print('ok')
