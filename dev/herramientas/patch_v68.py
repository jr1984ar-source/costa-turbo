import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v68.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:90]); return s.replace(a, b)
h = rep(h, "const APP_VER=67", "const APP_VER=68")
h = rep(h, "function motoArt(cv,m,p){", open('skidecor.js').read() + "function motoArt(cv,m,p){")
h = rep(h, "c2.getContext('2d').putImageData(d,0,0);});}", "const cx2=c2.getContext('2d');cx2.putImageData(d,0,0);skiDecor(cx2,m,p);});}")
open(H, 'w').write(h); print('ok')
