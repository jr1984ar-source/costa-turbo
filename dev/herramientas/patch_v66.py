import shutil, json
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v66.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:90]); return s.replace(a, b)
h = rep(h, "const APP_VER=65", "const APP_VER=66")
M = json.load(open('ilus/ilus_map.json'))
i0 = h.index("const SKI_MAP="); i1 = h.index("\n", i0)
h = h[:i0] + "const SKI_MAP=" + json.dumps(M, separators=(',', ':')) + ";" + h[i1:]
j0 = h.index("// Moto dibujada pintada por piezas"); j1 = h.index("function motoArt(")
h = h[:j0] + open('skiart2.js').read() + h[j1:]
open(H, 'w').write(h); print('ok', len(h))
