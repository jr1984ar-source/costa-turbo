import shutil,re
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v86.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=85", "const APP_VER=86")
i_c = h.index(" {id:'circuitos',"); e_c = h.index("\n", i_c) + 1
i_r = h.index(" {id:'retos',"); e_r = h.index("\n", i_r) + 1
assert e_c == i_r, 'circuitos debe ir justo antes de retos'
circ = h[i_c:e_c]; ret = h[i_r:e_r]
h = h[:i_c] + ret + circ + h[e_r:]
open(H, 'w').write(h); print('ok')
