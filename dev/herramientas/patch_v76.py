import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v76.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:90]); return s.replace(a, b)
h = rep(h, "const APP_VER=75", "const APP_VER=76")
HOME = '<button class="btn ghost sm hm" data-home style="flex:none"><svg class="hm-i" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8 8 2.5 14 8M4 7v6.5h3V10h2v3.5h3V7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>INICIO</button>'
assert h.count(HOME) > 3
# inicio: un solo botón AJUSTES en lugar de SONIDO / MÚSICA
h = rep(h, '<div class="row"><button class="btn ghost" id="bSnd">SONIDO: SÍ</button><button class="btn ghost" id="bMus">MÚSICA: SÍ</button></div>',
           '<div class="row"><button class="btn ghost" id="bSet">AJUSTES</button></div>')
# pantalla de ajustes
h = rep(h, '    <section id="scrMedals" class="screen" hidden>',
 '''    <section id="scrSet" class="screen" hidden>
      <div class="head"><button class="btn ghost sm" id="setBk" style="flex:none">‹ ATRÁS</button><h2 class="h">AJUSTES</h2>''' + HOME + '''</div>
      <div class="setl">
        <button class="setr" id="sSnd"><span>SONIDO<small>Efectos del juego</small></span><i class="tg"></i></button>
        <button class="setr" id="sMus"><span>MÚSICA<small>Música de fondo</small></span><i class="tg"></i></button>
        <button class="setr" id="sVib"><span>VIBRACIÓN<small>Cuando te das un golpe</small></span><i class="tg"></i></button>
      </div>
      <p class="hint" id="vibNote"></p>
    </section>

    <section id="scrMedals" class="screen" hidden>''')
# estilos de los interruptores
h = rep(h, ".slist{", """.setl{width:min(100%,380px);display:grid;gap:10px}
.setr{display:flex;justify-content:space-between;align-items:center;gap:12px;width:100%;padding:14px 16px;border-radius:14px;border:1px solid rgba(255,255,255,.16);background:rgba(255,255,255,.06);color:#fff;font-family:var(--cond);font-weight:800;font-size:22px;letter-spacing:.05em;text-align:left;cursor:pointer}
.setr small{display:block;font-family:var(--cond);font-weight:600;font-size:14px;letter-spacing:.02em;color:var(--dim);margin-top:2px}
.setr .tg{position:relative;flex:none;width:54px;height:32px;border-radius:999px;background:rgba(255,255,255,.2);transition:background .2s}
.setr .tg::after{content:'';position:absolute;top:3px;left:3px;width:26px;height:26px;border-radius:50%;background:#fff;box-shadow:0 2px 4px rgba(0,0,0,.3);transition:transform .2s}
.setr.on .tg{background:var(--lime)}
.setr.on .tg::after{transform:translateX(22px)}
#vibNote{max-width:380px}
.slist{""")
# vibración: ajuste guardado; Android vibra, iPhone hace un toque (truco del interruptor)
h = rep(h, "function buzz(ms){try{navigator.vibrate&&navigator.vibrate(ms);}catch(_){}}",
 "let VIB_ON=store.get('ct_vib',true)!==false,_hapT=0;const HAS_VIB=typeof navigator.vibrate==='function';\n"
 "function hapTick(){try{const l=document.createElement('label');l.setAttribute('aria-hidden','true');l.style.display='none';const i=document.createElement('input');i.type='checkbox';i.setAttribute('switch','');l.appendChild(i);document.head.appendChild(l);l.click();document.head.removeChild(l);}catch(_){}}\n"
 "function vibNow(ms){if(!VIB_ON)return;try{if(HAS_VIB){navigator.vibrate(ms);return;}}catch(_){}const t=performance.now();if(t-_hapT<120)return;_hapT=t;hapTick();if(ms>=100)setTimeout(hapTick,110);}\n"
 "function buzz(ms){if(G.demo)return;vibNow(ms);}")
# golpes que vibran
h = rep(h, "Snd.bump();G.shake=", "Snd.bump();buzz(40);G.shake=", 9)
h = rep(h, "Snd.miss();G.shake=3;", "Snd.miss();buzz(60);G.shake=3;")
h = rep(h, "Snd.miss();G.shake=4;", "Snd.miss();buzz(80);G.shake=4;")
h = rep(h, "G.catches++;Snd.fine();", "G.catches++;Snd.fine();buzz(120);")
h = rep(h, "G.money-=500;Snd.fine();", "G.money-=500;Snd.fine();buzz(100);")
h = rep(h, "loseLifeInZone('¡MULTA SIN PAGAR!');}P.v*=.4;", "loseLifeInZone('¡MULTA SIN PAGAR!');buzz(100);}P.v*=.4;")
# textos y estado de los interruptores
h = rep(h, "function labels(){const a='SONIDO: '+(Snd.on?'SÍ':'NO'),b='MÚSICA: '+(Snd.musOn?'SÍ':'NO');['#bSnd','#pSnd'].forEach(s=>$(s).textContent=a);['#bMus','#pMus'].forEach(s=>$(s).textContent=b);}",
 "function labels(){const a='SONIDO: '+(Snd.on?'SÍ':'NO'),b='MÚSICA: '+(Snd.musOn?'SÍ':'NO');$('#pSnd').textContent=a;$('#pMus').textContent=b;\n"
 " $('#sSnd').classList.toggle('on',!!Snd.on);$('#sMus').classList.toggle('on',!!Snd.musOn);$('#sVib').classList.toggle('on',!!VIB_ON);\n"
 " $('#vibNote').textContent=HAS_VIB?'':'En iPhone no puede vibrar de verdad: hace un toque suave (iOS 17.4 o más nuevo, con la vibración del sistema activada en Ajustes del iPhone > Sonidos y vibraciones).';}")
h = rep(h, "on('#bSnd',()=>Snd.setOn(!Snd.on));on('#bMus',()=>{Snd.setMus(!Snd.musOn);if(Snd.musOn)Music.play('menu');});",
 "on('#bSet',()=>{Snd.click();show('scrSet');labels();});on('#setBk',()=>{Snd.click();goTitle();});\n"
 "on('#sSnd',()=>{Snd.setOn(!Snd.on);Snd.click();});on('#sMus',()=>{Snd.setMus(!Snd.musOn);if(Snd.musOn)Music.play('menu');});\n"
 "on('#sVib',()=>{VIB_ON=!VIB_ON;store.set('ct_vib',VIB_ON);labels();if(VIB_ON)vibNow(80);});")
open(H, 'w').write(h); print('ok')
