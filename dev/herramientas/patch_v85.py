import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v85.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=84", "const APP_VER=85")
# El Puerto fuera del juego (se queda solo como fondo de la pantalla de inicio)
h = rep(h, "{name:'EL PUERTO',water:", "{name:'EL PUERTO',off:1,water:")
h = rep(h, "z:[0,4,5,6,13],zs:'El Puerto · Persecución · Olas Gigantes · Las Rampas · Tormenta'", "z:[4,5,6,13],zs:'Persecución · Olas Gigantes · Las Rampas · Tormenta'")
open(H, 'w').write(h); print('ok')
