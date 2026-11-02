import shutil, json
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v70.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:90]); return s.replace(a, b)
h = rep(h, "const APP_VER=69", "const APP_VER=70")
M = json.load(open('ilus2/ski_map2.json'))
R = json.load(open('ilus2/riva2.json'))
i0 = h.index("const SKI_MAP="); i1 = h.index("\n", i0)
h = h[:i0] + "const SKI_MAP=" + json.dumps(M, separators=(',', ':')) + ";\nconst RIVA_ST=" + json.dumps(R, separators=(',', ':')) + ";" + h[i1:]
h = rep(h, open('skiart2.js').read().strip(), open('skiart3.js').read().strip())
h = rep(h, open('skidecor.js').read(), open('skidecor2.js').read())
open(H, 'w').write(h); print('ok')
