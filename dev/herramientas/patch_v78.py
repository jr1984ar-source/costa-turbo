import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v78.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=77", "const APP_VER=78")
h = rep(h, "{name:'GRAN CARRERA',water:['#2ccbe0','#1396c9'],alt:1,obj:'race3',goal:'Termina entre los 3 primeros.',",
 "{name:'GRAN CARRERA',water:['#2ccbe0','#1396c9'],alt:1,cuts:1,obj:'race3',goal:'Termina entre los 3 primeros. Hay dos atajos: canales estrechos detrás de las islas de arena, uno pegado a cada costa.',")
# atajos: isla de arena alargada junto a la costa; canal estrecho por dentro, paso ancho por fuera
h = rep(h, " if(Z.island)island(Math.round(len*.45),58,220);\n",
 """ if(Z.island)island(Math.round(len*.45),58,220);
 if(Z.cuts&&Z.alt){const sl=len/5;for(const[f,side]of[[1.5,1],[4.3,-1]]){let cu=Math.round(f*sl);if(Math.abs(cu-barU)<900)cu=barU+(cu<barU?-900:900);
   const rx=36,ry=215,gap=86,wallAt=y=>side<0?zone.shore(y):zone.rwall(y);let lim=side<0?-1e9:1e9;for(let du=-ry-40;du<=ry+40;du+=15){const w=wallAt(-(cu+du));lim=side<0?Math.max(lim,w):Math.min(lim,w);}
   const x=side<0?lim+gap+rx:lim-gap-rx;add({t:'island',x,y:-cu,rx,ry,seed:(r()*1e6)|0,theme:'cay',cut:side});resv.push([cu-ry-190,cu+ry+190]);
   for(let du=-ry+20;du<=ry-20;du+=36){if(Math.abs(du)<30)continue;const y=-(cu+du),e=Math.sqrt(Math.max(0,1-(du/ry)*(du/ry))),edge=side<0?x-(rx+10)*e:x+(rx+10)*e,cx=(edge+wallAt(y)+(side<0?11:-11))/2;add({t:'coin',x:cx,y});}
   {const edge=side<0?x-rx-10:x+rx+10;add({t:'can',x:(edge+wallAt(-cu)+(side<0?11:-11))/2,y:-cu});}
   const far=side<0?(zone.rwall?Math.min(WG-24,zone.rwall(-cu)):WG-24):Math.max(24,zone.shore(-cu)+11),near=side<0?x+rx+10:x-rx-10;
   for(const[fu,t]of[[-.55,.3],[.05,.72],[.6,.4]]){const uu=cu+fu*ry,xx=lerp(near+26,far-26,t);add({t:'rock',x:xx,y:-uu,rad:12+r()*5,v:(r()*3)|0});if(r()<.6)add({t:'rock',x:xx+(r()-.5)*36,y:-uu-28,rad:9+r()*4,v:(r()*3)|0});}}}
""")
open(H, 'w').write(h); print('ok')
