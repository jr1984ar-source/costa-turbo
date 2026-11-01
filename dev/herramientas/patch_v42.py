import re
p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
i=s.find('const ZONES=[');j=s.find('];',i);Z=s[i:j]
for nm in ['EL PUERTO','GRAN CARRERA','OLAS GIGANTES','CARRERA ES TRENC','CARRERA SAN TELM']:
    a=Z.find("{name:'"+nm+"'");b=Z.find('\n',a);line=Z[a:b];assert line.count(',piri:1')==1,nm
    Z=Z[:a]+line.replace(',piri:1','')+Z[b:]
a=Z.find("{name:'PORTALS'");b=Z.find('\n',a);line=Z[a:b];assert 'supers:1,' in line
Z=Z[:a]+line.replace('supers:1,','supers:1,piri:1,').replace("esquivando los superyates que entran y salen.","esquivando los superyates que entran y salen. A mitad de camino está el Piri-Piri: pasa a su lado y te da vida y turbos.")+Z[b:]
s=s[:i]+Z+s[j:]
rep("L==='portals'){cvSuper(g,170,HZ+34,.8);","L==='portals'){cvPiri(g,352,HZ+16,.62);cvSuper(g,170,HZ+34,.8);")
rep("const APP_VER=41;","const APP_VER=42;")
open(p,'w').write(s);print('ok')
