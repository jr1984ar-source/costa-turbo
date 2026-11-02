import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v94.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=93", "const APP_VER=94")
# cada corazón del agua da una vida entera (máximo 6: setHp ya limita a 18 tercios)
h = rep(h, "setHp(hpTot()+1);msg('¡CORAZÓN!','+⅓ de corazón','#ff4f6b');", "setHp(hpTot()+3);msg('¡CORAZÓN!',hpTot()>=18?'Vidas al máximo':'+1 corazón','#ff4f6b');")
open(H, 'w').write(h); print('ok')
