import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v87.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=86", "const APP_VER=87")
# Al Mago pasa a llamarse El Mago y sale desde el Bar JJ'S (solo decorado, sin parada)
h = rep(h, "{name:'CARRERA AL MAGO',piriAt:.5,", "{name:'EL MAGO',jjStart:1,piriAt:.5,")
h = rep(h, "zs:'Al Mago · San Telm · Formentor · S", "zs:'El Mago · San Telm · Formentor · S")
# costa: paseo un poco más ancho junto a la salida para que quepa el bar
h = rep(h, "const RING_R=72;", "const RING_R=72,JJS_PU=-130;")
# paseo de baldosa junto a la salida
h = rep(h, "if(Z.bar==='jj'){zone.kind=y=>{const d=-y-barU;return d>JJP+190&&d<JJP+1000?'beach':d>JJP-950&&d<=JJP+190?'prom':kindU(-y);};}",
 "if(Z.bar==='jj'){zone.kind=y=>{const d=-y-barU;return d>JJP+190&&d<JJP+1000?'beach':d>JJP-950&&d<=JJP+190?'prom':kindU(-y);};}\n if(Z.jjStart){const bk=zone.kind;zone.kind=y=>{const u=-y;return u>-1100&&u<170?'prom':bk(y);};}")
# espigón con barcas detrás de la línea de salida (sin zona de parada)
h = rep(h, " zone.pier=null;", """ zone.jjDeco=null;if(Z.jjStart){const pu=JJS_PU,sx=zone.shore(-pu),x0=sx-6,x1=sx+112,ph=40;zone.jjDeco={barY:-(pu-JJP)};add({t:'pier',x:(x0+x1)/2,cx:(x0+x1)/2,hw:(x1-x0)/2+8,x0,x1,y:-pu,h:ph});
  const bc=()=>['#f4f5f7','#1e5eff','#1f9e52','#e3202b','#f4f5f7','#ffd21a'][(r()*6)|0];for(let bx=sx+18;bx<x1-8;bx+=22)add({t:'barca',x:bx,y:-pu-ph/2-14,rot:(r()-.5)*.1,c:bc()});for(let bx=sx+30;bx<x1-20;bx+=40)add({t:'barca',x:bx,y:-pu+ph/2+14,rot:Math.PI+(r()-.5)*.1,c:bc()});}
 zone.pier=null;""")
# dibujar el Bar JJ'S de la salida
h = rep(h, "if(Zn.bar&&Zn.barY>y0-(Zn.bar==='jj'?1100:240)&&Zn.barY<y1+(Zn.bar==='jj'?1100:240)){",
 "if(Zn.jjDeco&&Zn.jjDeco.barY>y0-1100&&Zn.jjDeco.barY<y1+1100)drawJJTop(g,{barY:Zn.jjDeco.barY,shore:Zn.shore,Z:Zn.Z});\n if(Zn.bar&&Zn.barY>y0-(Zn.bar==='jj'?1100:240)&&Zn.barY<y1+(Zn.bar==='jj'?1100:240)){")
open(H, 'w').write(h); print('ok')
