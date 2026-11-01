p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
rep("splash(c.x,c.y,34,180);msg('¡VOLCADO!','Pierdes unos segundos','var(--red)');}}",
    "splash(c.x,c.y,34,180);if(c.isP&&!G.demo&&G.mode==='play'){setHp(hpTot()-2);const L=$('#lives');L.classList.remove('hit');void L.offsetWidth;L.classList.add('hit');if(G.lives<=0){G.mode='over';endRace();Snd.fail();setTimeout(gameOver,900);msg('¡SIN CORAZONES!','La ola te ha volcado','var(--red)');}else msg('¡VOLCADO!','Pierdes tiempo y ⅔ de corazón','var(--red)');}else msg('¡VOLCADO!','Pierdes unos segundos','var(--red)');}}")
rep("si vas lento o torcido, vuelcas.","si vas lento o torcido, vuelcas y pierdes ⅔ de corazón.")
rep("msg('¡OLA GIGANTE!','Rápido y recto o vuelcas','var(--cyan)')","msg('¡OLA GIGANTE!','Rápido y recto o vuelcas (−⅔ ♥)','var(--cyan)')")
rep("const APP_VER=44;","const APP_VER=45;")
open(p,'w').write(s);print('ok')
