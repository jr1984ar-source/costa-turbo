"""Moto de agua en estilo dibujo (línea + colores planos por pieza) a partir de la foto blanca."""
import json, base64, io, sys, cv2, numpy as np
from PIL import Image
import os
from masks import build
if os.environ.get('FX'):
    from fxmask import build as bfx
    rgba, lab = bfx()
else:
    rgba, lab = build('blanca')
H, W = lab.shape
S = 2  # trabajar al doble para líneas finas
rgba2 = cv2.resize(rgba, (W * S, H * S), interpolation=cv2.INTER_CUBIC)
lab2 = cv2.resize(lab, (W * S, H * S), interpolation=cv2.INTER_NEAREST)
rgb = rgba2[..., :3]; al = rgba2[..., 3]
on = al > 100
g = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY).astype(np.float32) / 255
# luz suave en 3 bandas
gs = cv2.bilateralFilter((g * 255).astype(np.uint8), 15, 40, 9).astype(np.float32) / 255
gs = cv2.GaussianBlur(gs, (0, 0), 2.2)
# líneas: bordes fuertes de la foto, limpiados
sm = cv2.bilateralFilter(rgb, 9, 50, 9)
if os.environ.get('FX'): sm = cv2.bilateralFilter(cv2.bilateralFilter(sm, 11, 60, 11), 11, 60, 11)
e = cv2.Canny(cv2.cvtColor(sm, cv2.COLOR_RGB2GRAY), 40, 110)
e = cv2.morphologyEx(e, cv2.MORPH_CLOSE, np.ones((2, 2), np.uint8))
n, ll, st, _ = cv2.connectedComponentsWithStats((e > 0).astype(np.uint8))
keep = np.zeros_like(e)
for i in range(1, n):
    if st[i, cv2.CC_STAT_AREA] >= (90 if os.environ.get('FX') else 25): keep[ll == i] = 255
e = cv2.GaussianBlur(keep.astype(np.float32), (0, 0), .7)
e = np.clip(e / 120, 0, 1)
# zonas oscuras de la foto (alfombrillas, manillar, asas) se quedan oscuras
darkfix = ((lab2 == 6) & on) if os.environ.get('FX') else ((g < .35) & on)

def hx(c): c = c.lstrip('#'); return np.array([int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16)], np.float32)

def render(P, base='#f2f4f7'):
    col = np.zeros((H * S, W * S, 3), np.float32); col[:] = hx(base)
    for k, v in P.items():
        col[lab2 == int(k)] = hx(v)
    col[lab2 == 6] = hx('#202329')
    # rayas (4) sin color propio: gris claro
    # luz: 3 bandas sobre la luminancia suave
    # como los cascos: degradado suave de arriba-izquierda a abajo-derecha y muy poca sombra de la foto
    yy, xx = np.mgrid[0:H * S, 0:W * S].astype(np.float32)
    ys_, xs_ = np.where(on); x0, x1, y0, y1 = xs_.min(), xs_.max(), ys_.min(), ys_.max()
    t = ((xx - x0) / (x1 - x0)) * .4 + ((yy - y0) / (y1 - y0)) * .6
    f = 1.08 - .2 * t
    soft = cv2.GaussianBlur(gs, (0, 0), 6)
    q = (.9 + .14 * np.clip((soft - .55) / .38, 0, 1)) * f
    out = col * q[..., None]
    # bordes de cada panel un poco más oscuros (volumen leve)
    panel = cv2.GaussianBlur((1 - e).astype(np.float32), (0, 0), 3)
    out *= (.9 + .1 * panel)[..., None]
    # brillo muy ligero solo en la parte más alta
    spec = np.clip((soft - .94) / .04, 0, 1)
    out = out + (255 - out) * spec[..., None] * .18
    out[darkfix] = np.array([30, 33, 40], np.float32) * (0.7 + g[darkfix][:, None] * 1.4)
    # líneas
    lumc = (out[..., 0] * .3 + out[..., 1] * .59 + out[..., 2] * .11) / 255
    lc = np.where((lumc < .22)[..., None], np.array([110, 118, 130], np.float32), np.array([18, 20, 26], np.float32))
    out = out * (1 - e[..., None] * .85) + lc * e[..., None] * .85
    out = np.clip(out, 0, 255).astype(np.uint8)
    cs, _ = cv2.findContours(on.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(out, cs, -1, (16, 18, 24), 4, cv2.LINE_AA)
    a = cv2.GaussianBlur(cv2.dilate(on.astype(np.uint8) * 255, np.ones((3, 3), np.uint8)), (0, 0), .8)
    return np.dstack([out, a])

if __name__ == '__main__':
    V = json.load(open(sys.argv[1]))
    for name, P in V.items():
        im = render(P)
        Image.fromarray(im, 'RGBA').resize((W, H), Image.LANCZOS).save(os.environ.get('PRE','toon_') + name + '.png')
        print(name)
