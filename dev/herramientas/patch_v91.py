import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v91.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=90", "const APP_VER=91")
# mensajes de carrera legibles sobre agua clara: sombra oscura en el título y fondo oscuro en el texto de abajo
h = rep(h, "#msg .mt{font-family:var(--cond);font-weight:800;font-size:clamp(28px,9vw,46px);line-height:1;color:#fff;text-shadow:0 3px 0 rgba(0,0,0,.35),0 0 18px var(--mc,var(--orange))}",
 "#msg .mt{font-family:var(--cond);font-weight:800;font-size:clamp(28px,9vw,46px);line-height:1;color:#fff;text-shadow:0 3px 0 rgba(0,0,0,.55),0 0 4px rgba(4,14,34,.9),0 0 10px rgba(4,14,34,.7),0 0 22px var(--mc,var(--orange))}")
h = rep(h, "#msg .ms{font-family:var(--cond);font-weight:700;font-size:18px;letter-spacing:.06em;color:var(--mc,var(--gold));text-shadow:0 2px 0 rgba(0,0,0,.4)}",
 "#msg .ms{font-family:var(--cond);font-weight:700;font-size:18px;letter-spacing:.06em;color:var(--mc,var(--gold));text-shadow:0 2px 0 rgba(0,0,0,.4);background:rgba(6,18,42,.78);padding:4px 12px;border-radius:12px;margin-top:4px;max-width:100%}")
open(H, 'w').write(h); print('ok')
