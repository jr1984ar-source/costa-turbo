import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v90.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=89", "const APP_VER=90")
# botones un poco más arriba (unos 20 px más en el iPhone)
h = rep(h, "padding-block:14px max(10px,calc(env(safe-area-inset-bottom,0px) - 14px));", "padding-block:14px max(16px,calc(env(safe-area-inset-bottom,0px) + 6px));")
open(H, 'w').write(h); print('ok')
