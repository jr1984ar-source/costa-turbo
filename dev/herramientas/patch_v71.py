import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v71.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:90]); return s.replace(a, b)
h = rep(h, "const APP_VER=70", "const APP_VER=71")
h = rep(h, "g.strokeStyle=col;g.lineWidth=3;g.strokeRect(1.5,1.5,240,44);\n  ", "")
open(H, 'w').write(h); print('ok')
