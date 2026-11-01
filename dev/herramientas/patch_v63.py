import shutil, json, re
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v63.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, a[:90])
    return s.replace(a, b)

h = rep(h, "const APP_VER=62", "const APP_VER=63")

# ================= MOTOS =================
PH = json.load(open('trace/moto_photos.json'))
MODEL = {'brava': 'Yamaha FX Cruiser SVHO', 'inferno': 'Yamaha FX SVHO', 'avispa': 'Yamaha FX SVHO', 'oceano': 'Yamaha FX SVHO',
         'marea': 'Yamaha FX SVHO', 'sombra': 'Yamaha FX Limited SVHO', 'veneno': 'Kawasaki Ultra 310LX-S',
         'solar': 'Sea-Doo RXT-X 325', 'gris': 'Sea-Doo RXT-X 325', 'dorada': 'Sea-Doo RXT-X 325'}
h = rep(h, "colors:'Roja entera',", "colors:'Roja y negra',")
h = rep(h, "colors:'Azul entera',", "colors:'Azul y negra',")
h = rep(h, "colors:'Azul y blanca',", "colors:'Azul claro y negra',")
h = rep(h, "colors:'Gris · Kit Riva Racing',", "colors:'Gris y flúor · Kit Riva Racing',")
DORADA = """,
 {id:'dorada',name:'DORADA',riva:1,colors:'Dorada · Kit Riva Racing',pilot:'Leo Durán',bio:'La joya del taller. Rápida, fina y con estilo.',ui:'#d9c08a',st:{vel:5,ace:5,giro:4,turbo:4},
  sk:{hull:'#d6c39a',hullD:'#8f7c55',acc:'#e3202b',seat:'#e3202b',vest:'#1b1d22',helmet:'#d6c39a',hs:'#1b1d22',arm:'#1b1d22'},
  side:{deck:'#d6c39a',hood:'#1d1f24',hull:'#c9b48a',trim:'#15171b',seatA:'#e3202b',seatB:'#3a3d45',seatC:'#1d1f24',stripe:'#1d1f24'},face:{skin:'#e2b088',hair:'#3a2a1a',style:'short',vest:'#1b1d22'}}
];"""
a = "fin:1,face:{skin:'#e0b48e',hair:'#2a3240',style:'buzz',glasses:1,vest:'#1b2028'}}\n];"
h = rep(h, a, a[:-3] + DORADA)
h = rep(h, "sombra:[12000,0],gris:[15000,0]};", "sombra:[12000,0],gris:[15000,0],dorada:[20000,0]};")
h = rep(h, "gris:'Kit Riva Racing: la moto del Tiburón. La más bestia.'};", "gris:'Kit Riva Racing: la moto del Tiburón. La más bestia.',dorada:'Kit Riva Racing: la joya del taller. La más cara.'};")
PHJS = 'const MOTO_PH=' + json.dumps({k: {'w': v['w'], 'h': v['h'], 'src': v['src']} for k, v in PH.items()}, separators=(',', ':')) + ';\nconst MOTO_MODEL=' + json.dumps(MODEL, ensure_ascii=False) + ';\n'
PHJS += r"""function motoPhoto(cv,m){const box=cv.parentElement;let im=box.querySelector('img.mph');const ph=MOTO_PH[m.id],use=!!ph&&!paintOf(m).colors;if(!im){im=document.createElement('img');im.className='mph';im.alt='';im.decoding='async';box.insertBefore(im,cv);}im.hidden=!use;cv.hidden=use;if(use&&im.getAttribute('src')!==ph.src)im.setAttribute('src',ph.src);}
"""
a = "const MOTO_DESC={"
h = rep(h, a, PHJS + a)
# garage
h = rep(h, "const gc=$('#gMoto'),g=gc.getContext('2d');g.setTransform(2,0,0,2,0,0);g.clearRect(0,0,290,120);g.save();g.translate(2,4);g.scale(.836,.836);drawJetProfile(g,sideOf(m));g.restore();",
        "const gc=$('#gMoto'),g=gc.getContext('2d');g.setTransform(2,0,0,2,0,0);g.clearRect(0,0,290,120);g.save();g.translate(2,4);g.scale(.836,.836);drawJetProfile(g,sideOf(m));g.restore();motoPhoto(gc,m);")
h = rep(h, ":paintOf(m).colors?'Pintura personalizada':m.colors;", ":paintOf(m).colors?'Pintura personalizada':(MOTO_MODEL[m.id]?MOTO_MODEL[m.id]+' · ':'')+m.colors;")
# taller
h = rep(h, "const c=$('#sCv'),g=c.getContext('2d');g.setTransform(2,0,0,2,0,0);g.clearRect(0,0,290,120);g.save();g.translate(2,4);g.scale(.836,.836);drawJetProfile(g,sideOf(m));g.restore();",
        "const c=$('#sCv'),g=c.getContext('2d');g.setTransform(2,0,0,2,0,0);g.clearRect(0,0,290,120);g.save();g.translate(2,4);g.scale(.836,.836);drawJetProfile(g,sideOf(m));g.restore();motoPhoto(c,m);{const md=$('#sModel');if(md)md.textContent=(MOTO_MODEL[m.id]||'')+(paintOf(m).colors?' · pintura personalizada':'');}")
h = rep(h, '<div class="sname"><b id="sName"></b><span class="stag" id="sTag"></span></div>',
        '<div class="sname"><b id="sName"></b><span class="stag" id="sTag"></span></div>\n      <div class="smodel" id="sModel"></div>')
h = rep(h, ".slist{width:min(100%,440px);display:grid;gap:6px;text-align:left}",
        """.slist{width:min(100%,440px);display:grid;gap:6px;text-align:left}
.gmoto img.mph{width:auto;max-width:96%;height:118px;object-fit:contain;animation:bob 2.4s ease-in-out infinite;filter:drop-shadow(0 8px 8px rgba(0,20,60,.35))}
.gmoto.lk img.mph{filter:grayscale(1) brightness(.5)}
.smodel{width:min(100%,440px);margin-top:-6px;text-align:left;font-family:var(--cond);font-weight:700;font-size:14px;letter-spacing:.04em;color:var(--dim)}""")
h = rep(h, ".gmoto canvas,.fuel.low,.alert{animation:none}", ".gmoto canvas,.gmoto img.mph,.fuel.low,.alert{animation:none}")

# ================= EQUIPO =================
HA = json.load(open('lineart/helm_assets.json'))
pil = open('pilot_svg.js').read()
pil = pil[:pil.index("if (typeof module")]
pil = rep(pil, "  g += `<g transform=\"translate(118 182) rotate(-6)\">", "  if (!V.plain) g += `<g transform=\"translate(118 182) rotate(-6)\">")
pil = rep(pil, "  if (V.name) g += `<rect", "  if (V.name && !V.plain) g += `<rect")
glv = open('gloveIcon.js').read()
th = open('trace/tracedHelmet.js').read()
gs = th[th.index("  if (gog && J.port) {"):th.index("  return { defs, body: g, w: J.w, h: J.h };")]
gs = rep(gs, "const bt = gog.brand === 'oakley' ? 'OAKLEY' : gog.brand === '100' ? '100%' : 'alpinestars',", "const bt = ({ oakley: 'OAKLEY', '100': '100%', alpinestars: 'alpinestars' })[gog.brand] || '',")
GOGJS = """var LENSES = {
  clear: ['#eaf7ff', '#cfe9f7', '#9fcde6'], smoke: ['#7b8696', '#3d4552', '#1f242c'],
  red: ['#ffd166', '#ff5a3c', '#c2185b'], blue: ['#9ff3ff', '#2f8cff', '#3a2aa8'],
  gold: ['#fff3b0', '#ffc93c', '#b8741a'], silver: ['#ffffff', '#b9c3cf', '#6f7a88'],
  jade: ['#c8ffd8', '#2fbf71', '#0e6b4a'], prizm: ['#ffd166', '#ff7a3c', '#e2366e', '#5b3cff']
};
function gogSVG(J, gog, uid) {
  const id = (n) => n + uid;
  const mix = (a, b, t) => { const f = (x) => [parseInt(x.slice(1, 3), 16), parseInt(x.slice(3, 5), 16), parseInt(x.slice(5, 7), 16)]; const A = f(a), B = f(b); return '#' + A.map((v, i) => Math.round(v + (B[i] - v) * t).toString(16).padStart(2, '0')).join(''); };
  const lum = (h) => { h = h.replace('#', ''); return (parseInt(h.slice(0, 2), 16) * .3 + parseInt(h.slice(2, 4), 16) * .59 + parseInt(h.slice(4, 6), 16) * .11) / 255; };
  let defs = `<clipPath id="${id('sil')}"><path d="${J.sil}"/></clipPath>`, g = '';
""" + gs + """  return { defs, body: g };
}
"""
GEARX = r"""
const HELM_IMG=""" + json.dumps(HA['img'], separators=(',', ':')) + """;
const HELM_FR=""" + json.dumps(HA['frame'], separators=(',', ':')) + """;
""" + GOGJS + pil + glv + r"""
const STRAPS=['#1d2027','#ffffff','#e3202b','#1e5eff','#ffd21a','#b6f01e','#ff3f8e','#ff7a1a'];
const LENS_N={clear:'Transparente',smoke:'Ahumada',red:'Iridium rojo',blue:'Iridium azul',gold:'Oro',silver:'Espejo',jade:'Jade',prizm:'Prizm'};
function gogCol(it){const c=(gearStore.gc||{})[it.id]||{};return{strap:c.strap||it.strap,lens:c.lens||it.lens,own:!!c.strap};}
function gogOf(it){const k=gogCol(it);return{brand:it.brand,strap:k.strap,lens:k.lens,frame:it.frame,acc:k.own?k.strap:(it.acc||it.strap)};}
function gogIcon(it){const k=gogCol(it),L=LENSES[k.lens]||LENSES.smoke,st=k.strap,fr=it.frame||'#1b1d22',id='gi'+it.id,tc=['#ffffff','#ffd21a','#b6f01e'].includes(st)?'#15171c':'#fff',bt=({oakley:'OAKLEY','100':'100%',alpinestars:'alpinestars'})[it.brand]||'';
 return `<svg viewBox="0 0 100 50"><defs><linearGradient id="${id}" x1="0" x2="1" y1="0" y2="1">${L.map((c,i)=>`<stop offset="${i/(L.length-1)}" stop-color="${c}"/>`).join('')}</linearGradient></defs><rect x="0" y="16" width="100" height="16" rx="3" fill="${st}"/><text x="50" y="27.5" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="7" fill="${tc}">${bt}</text><path d="M14,10 C30,4 70,4 86,10 C92,16 92,34 86,40 C76,44 60,44 56,38 C53,34 47,34 44,38 C40,44 24,44 14,40 C8,34 8,16 14,10 Z" fill="${fr}" stroke="rgba(0,0,0,.5)"/><path d="M19,14 C34,9 66,9 81,14 C85,19 85,31 81,36 C73,39 62,39 59,34 C55,30 45,30 41,34 C38,39 27,39 19,36 C15,31 15,19 19,14 Z" fill="url(#${id})"/><path d="M26,14 L34,13 L26,36 L20,35 Z" fill="rgba(255,255,255,.45)"/></svg>`;}
function pilotFull(q,uid){const av=(AVATARS[G.avatar|0]||AVATARS[0]).face;
 const V=q.vest.c?{c:q.vest.c,c2:q.vest.c2,pat:q.vest.pat,name:q.vest.n}:{c:av.vest,c2:'#ffffff',pat:'band',plain:1};
 const S=q.suit.c?{c:q.suit.c,a:q.suit.a,pat:q.suit.pat}:{c:'#1d2027',a:'#3a3f4a'};
 const body=pilotSVG({vest:V,suit:S,glove:q.glove.c||'#1d2027',gloveA:q.glove.a||null,noHelm:true},uid+'b').replace(/^<svg[^>]*>/,'').replace(/<\/svg>$/,'');
 const J=HELM_FR,img=HELM_IMG[q.helm.paint||'serie']||HELM_IMG.serie,GG=gogSVG(J,gogOf(q.gog),uid+'g');
 const s=Math.min(206/J.w,196/J.h),tx=150-J.w*.55*s,ty=146-J.h*.9*s;
 return `<svg viewBox="0 -40 300 680" xmlns="http://www.w3.org/2000/svg"><defs>${GG.defs}</defs>${body}<g transform="translate(${tx.toFixed(1)} ${ty.toFixed(1)}) scale(${s.toFixed(4)})"><image href="${img}" width="${J.w}" height="${J.h}"/>${GG.body}</g></svg>`;}
"""
# lista de cascos nueva + gafas + guantes
i0 = h.index(" helm:[{id:'h0',n:'Sin casco',b:'De serie',p:0},")
i1 = h.index("}]};", i0) + 4
h = h[:i0] + """ helm:[{id:'h0',n:'Casco de serie',b:'De serie',p:0,paint:'serie'},
  {id:'h1',n:'S-M3 Morado',b:'Alpinestars',p:3000,c:'#a7afbd',c2:'#7b5cff',st:'mx',pat:'split',paint:'jettson'},
  {id:'h2',n:'S-M5 Rojo',b:'Alpinestars',p:4500,c:'#d0151f',c2:'#ff5a1f',st:'mx',pat:'twin',paint:'rojo'},
  {id:'h3',n:'S-M5 Azul',b:'Alpinestars',p:6000,c:'#f4f6f9',c2:'#1e4fd8',st:'mx',pat:'split',paint:'azul'},
  {id:'h4',n:'S-M7 Negro',b:'Alpinestars',p:9000,c:'#24262c',c2:'#f4f6f9',st:'mx',pat:'star',paint:'negro'},
  {id:'h5',n:'S-M8 Amarillo',b:'Alpinestars',p:12000,c:'#ffd21a',c2:'#1d2027',st:'mx',pat:'twin',paint:'amarillo'},
  {id:'h6',n:'Supertech Flúor',b:'Alpinestars',p:16000,c:'#ff6a1a',c2:'#ff3f8e',st:'mx',pat:'flame',paint:'fluor'}],
 gog:[{id:'g0',n:'Gafas básicas',b:'De serie',p:0,brand:'',strap:'#1d2027',lens:'smoke'},
  {id:'g1',n:'Strata 2',b:'100%',p:2000,brand:'100',strap:'#ffd21a',lens:'gold',acc:'#1d2027'},
  {id:'g2',n:'Racecraft 2',b:'100%',p:3500,brand:'100',strap:'#1e5eff',lens:'red'},
  {id:'g3',n:'Armega',b:'100%',p:5500,brand:'100',strap:'#ffffff',lens:'blue',frame:'#f4f6f9',acc:'#1e5eff'},
  {id:'g4',n:'Vision 8',b:'Alpinestars',p:2500,brand:'alpinestars',strap:'#ff3f8e',lens:'jade'},
  {id:'g5',n:'Supertech',b:'Alpinestars',p:5000,brand:'alpinestars',strap:'#1d2027',lens:'gold',acc:'#ffd21a'},
  {id:'g6',n:'Front Line MX',b:'Oakley',p:4500,brand:'oakley',strap:'#1d2027',lens:'silver',acc:'#e3202b'},
  {id:'g7',n:'Airbrake MX',b:'Oakley',p:6500,brand:'oakley',strap:'#e3202b',lens:'prizm',acc:'#ff7a1a'}],
 glove:[{id:'gl0',n:'Guantes negros',b:'De serie',p:0,c:'#1d2027',a:null,d:'Neopreno básico'},
  {id:'gl1',n:'Matrix Race',b:'Jet Pilot',p:2000,c:'#1d2027',a:'#e3202b',t:'JP',d:'Palma antideslizante'},
  {id:'gl2',n:'RX Race',b:'Jet Pilot',p:3500,c:'#1d2027',a:'#ffd21a',t:'JP',d:'Nudillos reforzados'},
  {id:'gl3',n:'Radar',b:'Alpinestars',p:1500,c:'#f4f6f9',a:'#1e5eff',t:'A★',d:'Ligeros y ventilados'},
  {id:'gl4',n:'Techstar',b:'Alpinestars',p:4000,c:'#16181d',a:'#f4f6f9',t:'A★',d:'Protección de carbono'},
  {id:'gl5',n:'Superlite',b:"O'Neill",p:1200,c:'#6f7680',a:'#33a3ff',t:'ON',d:'Finos de competición'},
  {id:'gl6',n:'Reactor',b:"O'Neill",p:2500,c:'#1d2027',a:'#ff7a1a',t:'ON',d:'Cierre de velcro ancho'}]};""" + h[i1:]
h = rep(h, "function saveGear(){store.set('ct_gear',gearStore);}",
        "if(!gearStore.eq.gog)gearStore.eq.gog='g0';if(!gearStore.eq.glove)gearStore.eq.glove='gl0';for(const k of['g0','gl0','h0'])if(!gearStore.own.includes(k))gearStore.own.push(k);\nfunction saveGear(){store.set('ct_gear',gearStore);}")
h = rep(h, "function gearEq(tr){const e=Object.assign({},gearStore.eq,tr||{});return{suit:gearItem('suit',e.suit),vest:gearItem('vest',e.vest),helm:gearItem('helm',e.helm)};}",
        "function gearEq(tr){const e=Object.assign({},gearStore.eq,tr||{});return{suit:gearItem('suit',e.suit),vest:gearItem('vest',e.vest),helm:gearItem('helm',e.helm),gog:gearItem('gog',e.gog),glove:gearItem('glove',e.glove)};}" + GEARX)

# pantalla
h = rep(h, '<div class="gmoto gearpv"><canvas id="eCv" width="580" height="300"></canvas><canvas id="eTop" width="96" height="164"></canvas></div>\n      <div class="etabs" id="eTabs"><button class="btn ghost sm" data-c="helm">CASCO</button><button class="btn ghost sm" data-c="vest">CHALECO</button><button class="btn ghost sm" data-c="suit">NEOPRENO</button></div>',
        '<div class="showroom" id="eShow"><div class="beam" style="left:30px;transform:rotate(14deg)"></div><div class="beam" style="right:30px;transform:rotate(-14deg)"></div><div class="pod"></div><div class="pil" id="ePil"></div><canvas id="eTop" width="96" height="164"></canvas><div class="tag" id="eTags"></div></div>\n      <div class="etabs" id="eTabs"><button class="btn ghost sm" data-c="helm">CASCO</button><button class="btn ghost sm" data-c="gog">GAFAS</button><button class="btn ghost sm" data-c="glove">GUANTES</button><button class="btn ghost sm" data-c="vest">CHALECO</button><button class="btn ghost sm" data-c="suit">NEOPRENO</button></div>\n      <div class="gswb" id="eSw" hidden></div>')
h = rep(h, """.gearpv{height:172px;position:relative;width:min(100%,440px);flex:none}
.gearpv #eCv{width:min(100%,300px);aspect-ratio:580/300;height:auto;animation:none}
.gearpv #eTop{position:absolute;right:8px;top:8px;width:48px;height:82px;aspect-ratio:auto;animation:none;background:rgba(8,40,80,.28);border-radius:10px}
.etabs{flex:none;width:min(100%,440px);display:grid;grid-template-columns:repeat(3,1fr);gap:6px}
.etabs .btn{width:100%}""", """.showroom{position:relative;flex:none;width:min(100%,440px);height:340px;border-radius:18px;overflow:hidden;background:radial-gradient(ellipse 70% 60% at 50% 0%,rgba(120,200,255,.55),rgba(30,90,160,.15) 60%,transparent 75%),linear-gradient(180deg,#123a6a 0%,#0c2548 60%,#0a1a36 100%);box-shadow:inset 0 0 0 1px rgba(255,255,255,.12)}
.showroom .beam{position:absolute;top:-20px;width:120px;height:420px;background:linear-gradient(180deg,rgba(160,220,255,.22),transparent 80%);filter:blur(6px);pointer-events:none}
.showroom .pod{position:absolute;left:50%;bottom:40px;width:240px;height:42px;transform:translateX(-50%);border-radius:50%;background:radial-gradient(ellipse at 50% 35%,#4a7fb8,#173a66 70%);box-shadow:0 0 0 3px rgba(51,214,255,.6),0 0 34px rgba(51,214,255,.45)}
.showroom .pil{position:absolute;left:50%;bottom:44px;height:292px;transform:translateX(-50%)}.showroom .pil svg{height:100%;width:auto;display:block}
.showroom #eTop{position:absolute;right:10px;top:10px;width:48px;height:82px;border-radius:12px;background:rgba(8,40,80,.45);border:1px solid rgba(255,255,255,.14)}
.showroom .tag{position:absolute;left:0;right:0;bottom:8px;display:flex;justify-content:center;gap:4px;flex-wrap:wrap;padding:0 6px}
.showroom .tag span{font-family:var(--cond);font-weight:800;font-size:10.5px;letter-spacing:.03em;padding:2px 6px;border-radius:8px;background:rgba(8,20,40,.72);color:var(--gold);border:1px solid rgba(255,255,255,.14)}
.etabs{flex:none;width:min(100%,440px);display:grid;grid-template-columns:repeat(5,1fr);gap:4px}
.etabs .btn{width:100%;padding:9px 2px;font-size:11.5px}
.gswb{flex:none;width:min(100%,440px);display:grid;gap:7px}.gswb[hidden]{display:none}
.gsw{display:grid;grid-template-columns:52px 1fr;gap:6px;align-items:center;text-align:left}.gsw .gk{font-family:var(--cond);font-weight:800;font-size:12px;letter-spacing:.12em;color:var(--dim)}
.gsw .gr2{display:flex;gap:6px;flex-wrap:wrap}.gsw .dot{flex:none;width:28px;height:28px;border-radius:50%;border:2px solid rgba(255,255,255,.28);box-sizing:border-box;cursor:pointer;padding:0}
.gsw .dot.on{border-color:#fff;box-shadow:0 0 0 2px var(--orange)}.gsw .dot.ln{border-radius:8px;width:30px}
.gnote{width:min(100%,440px);font-size:11px;color:var(--dim);text-align:left;margin:0}
.gico{width:40px;height:40px;border-radius:10px;background:radial-gradient(circle at 40% 30%,#24406e,#0c1c3a);display:grid;place-items:center;overflow:hidden}.gico img,.gico svg{width:38px;height:auto;display:block}""")
# lógica de la pantalla
h = rep(h, """function gearPreview(){const tr=gearTry?{[gearTry.cat]:gearTry.id}:null,q=gearEq(tr),m=MOTOS[G.moto|0],av=(AVATARS[G.avatar|0]||AVATARS[0]).face;
 const c=$('#eCv'),g=c.getContext('2d');g.setTransform(2,0,0,2,0,0);g.clearRect(0,0,290,150);g.save();g.translate(22,54);g.scale(.68,.68);drawJetProfile(g,sideOf(m));drawRiderProfile(g,av,q.vest.c||av.vest,q);g.restore();""",
        """function gearPreview(){const tr=gearTry?{[gearTry.cat]:gearTry.id}:null,q=gearEq(tr);
 $('#ePil').innerHTML=pilotFull(q,'ep');
 const tg=$('#eTags');tg.textContent='';const nm=(it)=>(it.b==='De serie'||it.b==='Neopreno'?'':it.b+' ')+it.n;for(const it of[q.helm,q.gog,q.glove,q.vest,q.suit]){if(it.p===0&&it.id!=='h0')continue;const s=document.createElement('span');s.textContent=nm(it).toUpperCase();tg.append(s);}""")
h = rep(h, "function gearDesc(cat,it){if(cat==='helm')return it.id==='h0'?'Sin casco':(it.st==='full'?'Casco integral':'Casco de cross con visera');",
        "function gearDesc(cat,it){if(cat==='helm')return it.id==='h0'?'Blanco liso':'Casco de cross';if(cat==='gog')return 'Lente '+(LENS_N[it.lens]||'')+(it.id==='g0'?' · goma negra':'');if(cat==='glove')return it.d||'';")
h = rep(h, """ const L=$('#eList');L.textContent='';const eq=gearStore.eq[gearCat];let lastB='';""",
        """ const SW=$('#eSw');SW.hidden=gearCat!=='gog';if(gearCat==='gog'){const gi=gearItem('gog',gearStore.eq.gog),gk=gogCol(gi),cs=gk.strap,cl=gk.lens;
  SW.innerHTML=`<div class="gsw"><span class="gk">GOMA</span><div class="gr2">${STRAPS.map(c=>`<button class="dot ${c===cs?'on':''}" data-st="${c}" style="background:${c}" aria-label="Goma"></button>`).join('')}</div></div><div class="gsw"><span class="gk">LENTE</span><div class="gr2">${Object.keys(LENSES).map(k=>`<button class="dot ln ${k===cl?'on':''}" data-ln="${k}" style="background:linear-gradient(135deg,${LENSES[k].join(',')})" aria-label="${LENS_N[k]}"></button>`).join('')}</div></div><p class="gnote">Goma y lente se cambian gratis en las gafas que lleves puestas.</p>`;}
 const L=$('#eList');L.textContent='';const eq=gearStore.eq[gearCat];let lastB='';""")
h = rep(h, "row.append(iconCanvas(g=>gearIcon(g,gearCat,it)));",
        "if(gearCat==='helm'||gearCat==='gog'||gearCat==='glove'){const ic=document.createElement('span');ic.className='gico';ic.innerHTML=gearCat==='helm'?`<img alt=\"\" src=\"${HELM_IMG[it.paint]||HELM_IMG.serie}\">`:gearCat==='gog'?gogIcon(it):gloveIcon({c:it.c,a:it.a||'#3a3f4a',t:it.t||''},'gl'+it.id);row.append(ic);}else row.append(iconCanvas(g=>gearIcon(g,gearCat,it)));")
h = rep(h, "inf.querySelector('.nm').textContent=(it.b==='De serie'||it.b==='Neopreno'?'':it.b+' ')+it.n;",
        "inf.querySelector('.nm').textContent=(it.b==='De serie'||it.b==='Neopreno'?'':it.b+' ')+it.n;")
h = rep(h, "$('#eTabs').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;gearCat=b.dataset.c;gearTry=null;Snd.click();renderGear();});",
        "$('#eTabs').addEventListener('click',e=>{const b=e.target.closest('button');if(!b)return;gearCat=b.dataset.c;gearTry=null;Snd.click();renderGear();});\n$('#eSw').addEventListener('click',e=>{const b=e.target.closest('.dot');if(!b)return;const gid=gearStore.eq.gog,gc=gearStore.gc||(gearStore.gc={}),cc=gc[gid]||(gc[gid]={});if(b.dataset.st)cc.strap=b.dataset.st;if(b.dataset.ln)cc.lens=b.dataset.ln;saveGear();Snd.click();renderGear();});")
open(H, 'w').write(h)
print('ok', len(h))
