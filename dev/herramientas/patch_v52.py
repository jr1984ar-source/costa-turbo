p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
rep("   else if(k===3){const left=r()<.5;side(left?L+72:R-72,u2,left?1:-1,'m');u2+=560;}",
    "   else if(k===3){const x=lerp(L+70,R-70,r());ramp(x,u2,'m');ramp(x,u2+270,'s');air(x,u2+270,4,28);u2+=650;}")
rep("   else if(k===6){side(L+72,u2,1,'s');side(R-72,u2+430,-1,'m');u2+=920;}",
    "   else if(k===6){ramp(L+70,u2,'m');ramp(R-70,u2+300,'m');ramp(mid,u2+600,'l');air(mid,u2+600,6,34);u2+=1000;}")
rep(" Rampas amarillas (pequeñas), naranjas y rojas (saltos enormes), y algunas de lado que te lanzan en diagonal.'"," Rampas amarillas (pequeñas), naranjas y rojas (saltos enormes).'")
rep("const APP_VER=51;","const APP_VER=52;")
open(p,'w').write(s);print('ok')
