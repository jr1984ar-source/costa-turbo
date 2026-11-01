p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
i=s.find('const ZONES=[');j=s.find('];',i);Z=s[i:j]
a="{name:'CARRERA AL MAGO',";assert Z.count(a)==1
Z=Z.replace(a,a+"piriAt:.5,");s=s[:i]+Z+s[j:]
rep("if(Z.piri){let pu=Math.round(len*.3);while(isRes(pu)||Math.abs(pu-barU)<400)pu+=300;",
    "if(Z.piri){let pu=Math.round(len*(Z.piriAt||.3));while(isRes(pu)||Math.abs(pu-barU)<400)pu+=150;")
rep("const APP_VER=48;","const APP_VER=49;")
open(p,'w').write(s);print('ok')
