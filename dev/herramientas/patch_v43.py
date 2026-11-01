p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
i=s.find('const ZONES=[');j=s.find('];',i);Z=s[i:j]
a=Z.find("{name:'CARRERA AL MAGO'");b=Z.find('\n',a);line=Z[a:b];assert line.count("bar:null,")==1
Z=Z[:a]+line.replace("bar:null,","bar:'jj',barAt:.27,")+Z[b:]
a=Z.find("{name:'PORTALS'");b=Z.find('\n',a);line=Z[a:b];assert line.count("bar:null,")==1
Z=Z[:a]+line.replace("bar:null,","bar:'roxy',")+Z[b:]
s=s[:i]+Z+s[j:]
rep("const barU=Z.bar?Math.round(len*.47):-99999;","const barU=Z.bar?Math.round(len*(Z.barAt||.47)):-99999;")
rep("if(Z.supers){for(let su=1200;su<len-700;su+=850+r()*450){","if(Z.supers){for(let su=1200;su<len-700;su+=850+r()*450){if(Math.abs(su-barU)<420)continue;")
rep("""for(const[a,b,col,t]of sign){g.fillStyle=col;g.fillRect(a,62,b-a-1,13);g.fillStyle='#fff';g.font=`800 ${t==="JJ's"?11.5:10.5}px "Saira Condensed",sans-serif`;g.fillText(t,(a+b-1)/2,68.8);}""",
    """const MJ=!!Zn.Z.mirror;for(let[a,b,col,t]of sign){if(MJ){const a2=101-b,b2=101-a;a=a2;b=b2;}g.fillStyle=col;g.fillRect(a,62,b-a-1,13);g.fillStyle='#fff';g.font=`800 ${t==="JJ's"?11.5:10.5}px "Saira Condensed",sans-serif`;if(MJ){g.save();g.translate((a+b-1)/2,68.8);g.scale(-1,1);g.fillText(t,0,0);g.restore();}else g.fillText(t,(a+b-1)/2,68.8);}""")
rep("const APP_VER=42;","const APP_VER=43;")
open(p,'w').write(s);print('ok')
