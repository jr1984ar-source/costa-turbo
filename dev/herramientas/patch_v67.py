import shutil, json
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v67.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:90]); return s.replace(a, b)
h = rep(h, "const APP_VER=66", "const APP_VER=67")
M = json.load(open('ilus/ilus_map.json'))
i0 = h.index("const SKI_MAP="); i1 = h.index("\n", i0)
h = h[:i0] + "const SKI_MAP=" + json.dumps(M, separators=(',', ':')) + ";" + h[i1:]
h = rep(h, '"veneno": ["#1f9e52", "#62d41c", "#16181d", "#f4f5f7", "#16181d"]', '"veneno": ["#1f9e52", "#62d41c", "#62d41c", "#f4f5f7", "#16181d"]')
h = rep(h, '"dorada": ["#b8903c", "#d6c39a", "#1d1f24", "#e3202b", "#e3202b"]', '"dorada": ["#b8903c", "#d6c39a", "#d6c39a", "#1d1f24", "#e3202b"]')
open(H, 'w').write(h); print('ok')
