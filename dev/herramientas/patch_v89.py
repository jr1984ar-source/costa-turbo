import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v89.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=88", "const APP_VER=89")
# en modo app (icono de inicio) el iPhone resta la franja de la hora a la altura: usar la altura real de la pantalla
h = rep(h, "function fitH(){const hh=window.innerHeight;if(hh>200)document.documentElement.style.height=hh+'px';}",
 "function fitH(){let hh=window.innerHeight;try{const st=navigator.standalone||matchMedia('(display-mode: standalone)').matches;if(st){const sh=matchMedia('(orientation: portrait)').matches?Math.max(screen.width,screen.height):Math.min(screen.width,screen.height);if(sh>hh&&sh-hh<160)hh=sh;}}catch(_){}if(hh>200)document.documentElement.style.height=hh+'px';}")
# botones más cerca del borde de abajo (sin tapar la barra del iPhone)
h = rep(h, ".pad{display:flex;align-items:center;gap:10px;padding-block:14px max(8px,env(safe-area-inset-bottom,0px));", ".pad{display:flex;align-items:center;gap:10px;padding-block:14px max(10px,calc(env(safe-area-inset-bottom,0px) - 14px));")
open(H, 'w').write(h); print('ok')
