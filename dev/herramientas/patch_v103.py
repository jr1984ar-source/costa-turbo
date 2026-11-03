p='costa-turbo.html';s=open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
rep("{name:'SON MATÍAS · MODO LIBRE',","{name:'MODO LIBRE',")
rep("'Escondido en el lago de Son Matías'","'Escondido en el lago del Modo libre'")
rep("const APP_VER=102;","const APP_VER=103;")
open(p,'w',encoding='utf-8').write(s);print('ok')
