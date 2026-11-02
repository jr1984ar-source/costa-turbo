import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v93.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=92", "const APP_VER=93")
# sin cartel oscuro: el texto lleva un borde oscuro fino para leerse sobre cualquier agua
h = rep(h, "text-shadow:0 2px 0 rgba(0,0,0,.4);background:rgba(6,18,42,.78);padding:4px 12px;border-radius:12px;margin-top:4px;max-width:100%}",
 "font-weight:800;text-shadow:1px 1px 0 #061430,-1px -1px 0 #061430,1px -1px 0 #061430,-1px 1px 0 #061430,0 1.5px 0 #061430,0 -1.5px 0 #061430,1.5px 0 0 #061430,-1.5px 0 0 #061430,0 3px 4px rgba(0,0,0,.45);margin-top:3px;max-width:100%}")
# el objetivo de la carrera en amarillo en vez de azul claro
h = rep(h, "msg(G.zone.Z.name,G.zone.Z.goal.split('.')[0],'var(--cyan)');", "msg(G.zone.Z.name,G.zone.Z.goal.split('.')[0],'#ffe14d');")
open(H, 'w').write(h); print('ok')
