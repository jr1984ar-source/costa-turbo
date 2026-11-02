import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v88.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=87", "const APP_VER=88")
h = rep(h, "riv:0,bar:'roxy',theme:'cove',tod:'night'", "riv:0,bar:null,theme:'cove',tod:'night'")
open(H, 'w').write(h); print('ok')
