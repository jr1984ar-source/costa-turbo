import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v75.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:90]); return s.replace(a, b)
h = rep(h, "const APP_VER=74", "const APP_VER=75")
h = rep(h, "{id:'charger',name:'SUPER CHARGER',", "{id:'charger',name:'SUPERCHARGER',")
open(H, 'w').write(h); print('ok')
h = open(H).read()
# nombre largo: el texto de colores/precio baja a la línea de abajo en vez de apretarse
h = rep(h, ".gname{display:flex;justify-content:space-between;align-items:baseline;gap:8px}", ".gname{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:baseline;gap:2px 8px}")
h = rep(h, ".gname small{font-size:13px;color:var(--dim);text-align:right}", ".gname small{flex:1 1 150px;font-size:13px;color:var(--dim);text-align:right}")
h = rep(h, "'En el taller: '+pts(mpr)+' PTA'", "'En el taller: '+pts(mpr)+'\\u00a0PTA'")
open(H, 'w').write(h); print('ok css')
