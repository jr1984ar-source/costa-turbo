"""Moto más simple: menos líneas (solo contorno y bordes entre piezas), color casi plano, piezas suavizadas.
uso: python3 export_simple.py NIVEL salida.json   (NIVEL 1 = solo bordes de piezas, 2 = + pocas líneas largas)"""
import os, sys
os.environ['FX'] = '1'
import numpy as np, cv2, base64, io, json
from PIL import Image
import toonski as T
lvl = int(sys.argv[1]); outp = sys.argv[2]
H2, W2 = T.H * T.S, T.W * T.S
lab = T.lab2.copy(); on = T.on; gs = T.gs; g = T.g
unk = on & (lab == 0)
if unk.any():
    d, l = cv2.distanceTransformWithLabels((lab == 0).astype(np.uint8), cv2.DIST_L2, 3, labelType=cv2.DIST_LABEL_PIXEL)
    ys, xs = np.where(lab > 0); lut = np.zeros(l.max() + 1, np.uint8); lut[l[ys, xs]] = lab[ys, xs]; lab[unk] = lut[l[unk]]
# suavizar piezas (formas más limpias)
st = np.stack([cv2.GaussianBlur((lab == v).astype(np.float32), (0, 0), 3.5) for v in range(7)], 0)
lab = np.argmax(st, 0).astype(np.uint8); lab[~on] = 0
# quitar islas pequeñas de cada pieza
for v in range(1, 7):
    n, ll, s2, _ = cv2.connectedComponentsWithStats((lab == v).astype(np.uint8))
    for i in range(1, n):
        if s2[i, 4] < 260:
            m = ll == i; k = cv2.dilate(m.astype(np.uint8), np.ones((5, 5), np.uint8)) > 0
            ring = lab[k & ~m & on]; ring = ring[ring != v]
            if len(ring): lab[m] = np.bincount(ring).argmax()
# líneas: bordes entre piezas
b = np.zeros((H2, W2), np.uint8)
for dy, dx in [(0, 1), (1, 0)]:
    a1 = lab[:H2 - dy, :W2 - dx]; a2 = lab[dy:, dx:]
    m = (a1 != a2) & (a1 > 0) & (a2 > 0)
    b[:H2 - dy, :W2 - dx] |= m
e = cv2.dilate(b, np.ones((2, 2), np.uint8)).astype(np.float32)
if lvl >= 2:
    sm = cv2.bilateralFilter(T.rgb, 9, 60, 9); sm = cv2.bilateralFilter(sm, 11, 70, 11)
    c = cv2.Canny(cv2.cvtColor(sm, cv2.COLOR_RGB2GRAY), 70, 160)
    n, ll, s2, _ = cv2.connectedComponentsWithStats((c > 0).astype(np.uint8))
    keep = np.zeros_like(c)
    for i in range(1, n):
        x, y, w, h, a = s2[i]
        if max(w, h) > 90: keep[ll == i] = 1
    e = np.maximum(e, keep.astype(np.float32))
e = np.clip(cv2.GaussianBlur(e, (0, 0), .8) * 1.4, 0, 1)
# luz casi plana: degradado suave
yy, xx = np.mgrid[0:H2, 0:W2].astype(np.float32)
ys_, xs_ = np.where(on); x0, x1, y0, y1 = xs_.min(), xs_.max(), ys_.min(), ys_.max()
t = ((xx - x0) / (x1 - x0)) * .4 + ((yy - y0) / (y1 - y0)) * .6
q = 1.06 - .16 * t
soft = cv2.GaussianBlur(gs, (0, 0), 10)
q = q * (.95 + .06 * np.clip((soft - .5) / .4, 0, 1))
q[lab == 6] = 1.0
q = np.clip(q * 160, 0, 255)
cs, _ = cv2.findContours(on.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
ol = np.zeros((H2, W2), np.uint8); cv2.drawContours(ol, cs, -1, 1, 5, cv2.LINE_8)
lab[ol > 0] = 7
a = cv2.GaussianBlur(cv2.dilate(on.astype(np.uint8) * 255, np.ones((3, 3), np.uint8)), (0, 0), .8)
out = np.dstack([(lab * 36).astype(np.uint8), q.astype(np.uint8), (e * 255).astype(np.uint8), a])
ys2, xs2 = np.where(a > 0); m = 2
out = out[max(0, ys2.min() - m):ys2.max() + m, max(0, xs2.min() - m):xs2.max() + m]
im = Image.fromarray(out, 'RGBA'); bb = io.BytesIO(); im.save(bb, 'PNG', optimize=True)
print(lvl, im.size, len(bb.getvalue()))
json.dump({'w': im.size[0], 'h': im.size[1], 'src': 'data:image/png;base64,' + base64.b64encode(bb.getvalue()).decode()}, open(outp, 'w'))
