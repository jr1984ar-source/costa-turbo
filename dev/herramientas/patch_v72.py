import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v72.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:90]); return s.replace(a, b)
h = rep(h, "const APP_VER=71", "const APP_VER=72")
# moto bloqueada: con sus colores (solo el candado encima)
h = rep(h, ".gmoto.lk canvas{filter:grayscale(1) brightness(.5)}\n", "")
h = rep(h, ".gmoto.lk canvas.mph{filter:grayscale(1) brightness(.5)}\n", "")
# la moto se dibuja a la mitad de tamaño (lo que necesita la pantalla) usando un lienzo de trabajo compartido
h = rep(h, "skiMapLoad(()=>{if(c2._tok!==tok)return;const d=skiPaint(p);if(c2.width!==d.width){c2.width=d.width;c2.height=d.height;}const cx2=c2.getContext('2d');cx2.putImageData(d,0,0);skiDecor(cx2,m,p);});}",
 "skiMapLoad(()=>{if(c2._tok!==tok)return;const d=skiPaint(p);if(!SKI_TMP){SKI_TMP=document.createElement('canvas');SKI_TMP.width=d.width;SKI_TMP.height=d.height;}const t=SKI_TMP.getContext('2d');t.putImageData(d,0,0);skiDecor(t,m,p);const w=Math.round(d.width/2),hh=Math.round(d.height/2);if(c2.width!==w){c2.width=w;c2.height=hh;}const cx2=c2.getContext('2d');cx2.clearRect(0,0,w,hh);cx2.imageSmoothingQuality='high';cx2.drawImage(SKI_TMP,0,0,w,hh);});}")
h = rep(h, "let SKI_D=null,SKI_O=null,SKI_P=null,RIVA_IM=null;", "let SKI_D=null,SKI_O=null,SKI_P=null,RIVA_IM=null,SKI_TMP=null;")
open(H, 'w').write(h); print('ok')
