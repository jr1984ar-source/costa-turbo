import shutil, json
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v69.html')
h = open(H).read()
assert h.count("const APP_VER=68") == 1
h = h.replace("const APP_VER=68", "const APP_VER=69")
M = json.load(open('ilus/ilus_map.json'))
i0 = h.index("const SKI_MAP="); i1 = h.index("\n", i0)
h = h[:i0] + "const SKI_MAP=" + json.dumps(M, separators=(',', ':')) + ";" + h[i1:]
open(H, 'w').write(h); print('ok')
