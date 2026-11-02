import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v92.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=91", "const APP_VER=92")
# corazones en el agua: más cuanto más avanzada la carrera en la copa y más alta la dificultad
h = rep(h, "function placeHearts(O,add,seed,len,shore,rwall){const rh=rng(seed+77),nh=rh()<.5?1:2;\n for(let k=0;k<nh;k++){const base=Math.round(len*(nh===1?.5:k?.7:.36)+(rh()-.5)*300);",
 "function heartsN(rh){const r0=rh(),C=inCup();if(!C)return r0<.5?1:2;return Math.min(10,1+(C.fin?3:(G.cpos|0))+Math.max(0,G.lap|0));}\n"
 "function placeHearts(O,add,seed,len,shore,rwall){const rh=rng(seed+77),nh=heartsN(rh);\n for(let k=0;k<nh;k++){const base=Math.round(len*((k+1)/(nh+1))+(rh()-.5)*Math.min(300,len/(nh+1)*.5));")
h = rep(h, "nh=rh()<.5?1:2;for(let k=0;k<nh;k++){const i=I(Lp*(nh===1?.42:k?.78:.42)),", "nh=heartsN(rh);for(let k=0;k<nh;k++){const i=I(Lp*((k+1)/(nh+1))),")
h = rep(h, "nh=rh()<.5?1:2;for(let k=0;k<nh;k++){let s=Lp*(nh===1?.42:k?.78:.42);", "nh=heartsN(rh);for(let k=0;k<nh;k++){let s=Lp*((k+1)/(nh+1));")
h = rep(h, "nh=rh()<.5?1:2;for(let k=0;k<nh;k++){const ii=Math.floor(N*(nh===1?.3:k?.75:.3))%N,", "nh=heartsN(rh);for(let k=0;k<nh;k++){const ii=Math.floor(N*((k+1)/(nh+1)))%N,")
h = rep(h, "for(const o of O){if(o.y==null||Math.abs(o.y-hy)>420)continue;\n     if(o.t==='island'", "for(const o of O){if(o.y==null||Math.abs(o.y-hy)>420)continue;\n     if((o.t==='check'||o.t==='finish'||o.t==='heart')&&Math.abs(o.y-hy)<90){bad=true;continue;}\n     if(o.t==='island'")
open(H, 'w').write(h); print('ok')
