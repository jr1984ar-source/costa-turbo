import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v83.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=82", "const APP_VER=83")
# el panel de mandos: menos relleno arriba; abajo solo el margen de la barra del iPhone
h = rep(h, ".pad{display:flex;align-items:center;gap:10px;padding-block:16px 18px;", ".pad{display:flex;align-items:center;gap:10px;padding-block:14px max(8px,env(safe-area-inset-bottom,0px));")
# menús: margen seguro abajo (antes lo ponía la página entera)
h = rep(h, "  padding-block:16px;padding-left:max(16px,env(safe-area-inset-left,0px));", "  padding-block:16px max(16px,env(safe-area-inset-bottom,0px));padding-left:max(16px,env(safe-area-inset-left,0px));")
# la página ocupa toda la altura de la pantalla
h = rep(h, "html{box-sizing:border-box;height:100%;", "html{box-sizing:border-box;height:100%;height:100dvh;")
h = rep(h, "\n/* ================= BUCLE ================= */\nfunction resize(){",
 "\nfunction fitH(){const hh=window.innerHeight;if(hh>200)document.documentElement.style.height=hh+'px';}\nfitH();addEventListener('resize',fitH);addEventListener('orientationchange',()=>setTimeout(fitH,350));\n/* ================= BUCLE ================= */\nfunction resize(){")
open(H, 'w').write(h); print('ok')
# web: quitar el margen inferior de toda la página (ahora va bajo los botones)
r = open('rebuild.js').read()
a = ":root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
assert r.count(a) == 1
r = r.replace(a, ":root{padding-top:env(safe-area-inset-top,0px)}")
open('rebuild.js', 'w').write(r); print('ok rebuild')
