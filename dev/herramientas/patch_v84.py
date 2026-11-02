import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v84.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=83", "const APP_VER=84")
# la moto un 3 % más abajo en la pantalla (antes al 73 %, ahora al 76 %)
h = rep(h, ".y-VH*.73", ".y-VH*.76", 4)
# circuitos (pantalla que gira): del 70 % al 73 %
h = rep(h, "ctx.translate(sv[0]/2+sx,sv[1]*.7+sy)", "ctx.translate(sv[0]/2+sx,sv[1]*.73+sy)")
h = rep(h, "ht=sv[1]*.7/CZ,hb=sv[1]*.3/CZ", "ht=sv[1]*.73/CZ,hb=sv[1]*.27/CZ")
h = rep(h, "const RR=Math.hypot(VW*.5/CZ,VH*.72/CZ)+80", "const RR=Math.hypot(VW*.5/CZ,VH*.75/CZ)+80")
open(H, 'w').write(h); print('ok')
