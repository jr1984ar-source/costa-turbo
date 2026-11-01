p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
rep("  shoreU=u=>lerp(-90,base(u),altPres(u,0));}\n const zone={Z,zi,lap,len,",
    """  shoreU=u=>lerp(-90,base(u),altPres(u,0));}
 let canF=null;if(Z.canyon){const nA=noise1(seed+31),nW=noise1(seed+37),Pc=1150;
  const cx=u=>WG/2+108*Math.sin(u/Pc*TAU+1.3)+22*nA(u/520),wd=u=>{let w=345+28*nW(u/700);const pn=Math.sin(u/(Pc*2.3)*TAU+.4);if(pn>.8)w-=(pn-.8)/.2*115;return w;},kk=u=>sm(420,950,u)*sm(len-200,len-700,u);
  canF={cx,wd,kk};shoreU=u=>lerp(-140,cx(u)-wd(u)/2,kk(u));kindU=u=>'mount';coveF=null;}
 const zone={Z,zi,lap,len,""")
rep(" if(Z.canyon){const nw=noise1(seed+21);zone.rwall=y=>{const u=-y,k=sm(500,1000,u)*sm(len-300,len-800,u),w=188+30*nw(u/380)+10*nw(u/90);return zone.shore(y)+lerp(560,w,k);};}",
    " if(Z.canyon){zone.rwall=y=>{const u=-y;return lerp((VW>WG?WG+(VW-WG)/2:WG)+320,canF.cx(u)+canF.wd(u)/2,canF.kk(u));};}")
rep("goal:'Cruza el cañón del Torrent de Pareis antes de que se acabe el tiempo. Paredes de roca a los dos lados: no te despistes.',len:13000,riv:0,bar:null,theme:'tram',tod:'noon',pace:185,",
    "goal:'Cruza el cañón del Torrent de Pareis antes de que se acabe el tiempo. Hace curvas todo el rato: las paredes de roca van saliendo por un lado y por el otro.',len:13000,riv:0,bar:null,theme:'tram',tod:'noon',pace:168,")
rep("const APP_VER=50;","const APP_VER=51;")
open(p,'w').write(s);print('ok')
