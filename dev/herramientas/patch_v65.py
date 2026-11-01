import shutil, json, re
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v65.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, a[:90])
    return s.replace(a, b)
h = rep(h, "const APP_VER=64", "const APP_VER=65")
MAP = json.load(open('zonas/ski_map.json'))
ART = open('skiart.js').read()
DEF = {
 'brava': ['#e3202b', '#f4f5f7', '#e3202b', '#f4f5f7', '#16181d'],
 'inferno': ['#d81e28', '#e3202b', '#e3202b', '#16181d', '#16181d'],
 'avispa': ['#ffd21a', '#2c2f36', '#2c2f36', '#ffd21a', '#ffd21a'],
 'oceano': ['#1e5eff', '#2c2f36', '#2c2f36', '#1e5eff', '#1e5eff'],
 'marea': ['#1e5eff', '#f4f5f7', '#1e5eff', '#1e5eff', '#f4f5f7'],
 'solar': ['#ffd21a', '#ffd21a', '#ffd21a', '#2c2f36', '#2c2f36'],
 'veneno': ['#1f9e52', '#62d41c', '#16181d', '#f4f5f7', '#16181d'],
 'sombra': ['#25282e', '#33363d', '#33363d', '#8d9199', '#3a3e46'],
 'gris': ['#4a5d72', '#a9bccf', '#8094aa', '#e9eef4', '#1b2028'],
 'dorada': ['#b8903c', '#d6c39a', '#1d1f24', '#e3202b', '#e3202b'],
}
# quitar fotos y modelos, poner la moto dibujada
i0 = h.index("const MOTO_PH=")
i1 = h.index("function motoPhoto(")
i2 = h.index("\n", i1)
NEW = ("const SKI_MAP=" + json.dumps(MAP, separators=(',', ':')) + ";\nconst SKI_DEF=" + json.dumps(DEF) + ";\n" + ART +
       "function motoArt(cv,m,p){const box=cv.parentElement;let c2=box.querySelector('canvas.mph');if(!c2){c2=document.createElement('canvas');c2.className='mph';box.insertBefore(c2,cv);}cv.hidden=true;c2.hidden=false;p=p||paintOf(m);const tok=(c2._tok=(c2._tok|0)+1);skiMapLoad(()=>{if(c2._tok!==tok)return;const d=skiPaint(p);if(c2.width!==d.width){c2.width=d.width;c2.height=d.height;}c2.getContext('2d').putImageData(d,0,0);});}\n")
h = h[:i0] + NEW + h[i2 + 1:]
h = rep(h, "motoPhoto(gc,m)", "motoArt(gc,m)")
h = rep(h, "motoPhoto(c,m)", "motoArt(c,m)")
h = rep(h, "{const md=$('#sModel');if(md)md.textContent=(MOTO_MODEL[m.id]||'')+(paintOf(m).colors?' · pintura personalizada':'');}",
        "{const md=$('#sModel');if(md)md.textContent=paintOf(m).colors?'Pintura personalizada':m.colors;}")
h = rep(h, ":paintOf(m).colors?'Pintura personalizada':(MOTO_MODEL[m.id]?MOTO_MODEL[m.id]+' · ':'')+m.colors;", ":paintOf(m).colors?'Pintura personalizada':m.colors;")
# colores de serie y piezas nuevas
h = rep(h, "function defaultPaint(m){const s=m.side;return{colors:false,hull:s.hull,deck:s.deck,hood:s.hood,stripe:s.stripe,seat:s.seatA,name:''}",
        "function defaultPaint(m){const s=m.side,d=SKI_DEF[m.id];if(d)return{colors:false,hull:d[0],deck:d[1],hood:d[2],stripe:d[3],seat:d[4],name:''};return{colors:false,hull:s.hull,deck:s.deck,hood:s.hood,stripe:s.stripe,seat:s.seatA,name:''}")
h = rep(h, "const PAINT_PARTS=[['hull','CASCO'],['deck','LATERALES'],['hood','CAPÓ'],['stripe','RAYAS'],['seat','ASIENTO']];",
        "const PAINT_PARTS=[['hull','CASCO ABAJO'],['deck','CASCO ARRIBA'],['hood','TAPA DELANTERA'],['stripe','DETALLES'],['seat','ASIENTO']];")
h = rep(h, "drawJetProfile(g,sideOf(m,G._draft));g.restore();paintBtn();}", "drawJetProfile(g,sideOf(m,G._draft));g.restore();motoArt(c,m,G._draft);paintBtn();}")
h = rep(h, "colors:'Azul claro y negra',", "colors:'Azul y blanca',")
h = rep(h, "colors:'Gris y flúor · Kit Riva Racing',", "colors:'Gris · Kit Riva Racing',")
# estilos
h = rep(h, ".gmoto img.mph{width:auto;max-width:96%;height:118px;object-fit:contain;animation:bob 2.4s ease-in-out infinite;filter:drop-shadow(0 8px 8px rgba(0,20,60,.35))}",
        ".gmoto canvas.mph{width:auto;max-width:96%;height:118px;aspect-ratio:auto;animation:bob 2.4s ease-in-out infinite;filter:drop-shadow(0 8px 8px rgba(0,20,60,.35))}")
h = rep(h, ".gmoto.lk img.mph{filter:grayscale(1) brightness(.5)}", ".gmoto.lk canvas.mph{filter:grayscale(1) brightness(.5)}")
h = rep(h, ".gmoto canvas,.gmoto img.mph", ".gmoto canvas,.gmoto canvas.mph")
assert 'MOTO_PH' not in h and 'MOTO_MODEL' not in h
open(H, 'w').write(h)
print('ok', len(h))
