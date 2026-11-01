p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
rep(""" g.font='700 12px "Saira Condensed",sans-serif';const tw=g.measureText(C.tag).width+14;g.fillStyle='rgba(8,22,48,.75)';g.beginPath();g.roundRect(2,y+6,tw,17,8.5);g.fill();g.fillStyle='#33d6ff';g.fillText(C.tag,9,y+18.5);\n""","")
rep("const APP_VER=53;","const APP_VER=54;")
open(p,'w').write(s);print('ok')
