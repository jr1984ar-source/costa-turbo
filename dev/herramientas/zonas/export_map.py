"""Exporta el mapa de la moto dibujada para pintarla en el juego.
PNG RGBA a 2x: R = pieza*36 (0 nada,1-5 pintables,6 negro fijo,7 contorno), G = luz*160, B = línea*255, A = silueta."""
import os
os.environ['FX'] = '1'
import numpy as np, cv2, base64, io, json
from PIL import Image
import toonski as T
H2, W2 = T.H * T.S, T.W * T.S
lab = T.lab2.copy(); on = T.on; gs = T.gs; g = T.g; e = T.e
yy, xx = np.mgrid[0:H2, 0:W2].astype(np.float32)
ys_, xs_ = np.where(on); x0, x1, y0, y1 = xs_.min(), xs_.max(), ys_.min(), ys_.max()
t = ((xx - x0) / (x1 - x0)) * .4 + ((yy - y0) / (y1 - y0)) * .6
f = 1.08 - .2 * t
soft = cv2.GaussianBlur(gs, (0, 0), 6)
q = (.9 + .14 * np.clip((soft - .55) / .38, 0, 1)) * f
panel = cv2.GaussianBlur((1 - e).astype(np.float32), (0, 0), 3)
q = q * (.9 + .1 * panel)
dk = lab == 6
q[dk] = (0.7 + g[dk] * 1.4)
q = np.clip(q * 160, 0, 255)
unk = on & (lab == 0)
if unk.any():
    d, l = cv2.distanceTransformWithLabels((lab == 0).astype(np.uint8), cv2.DIST_L2, 3, labelType=cv2.DIST_LABEL_PIXEL)
    ys, xs = np.where(lab > 0); lut = np.zeros(l.max() + 1, np.uint8); lut[l[ys, xs]] = lab[ys, xs]; lab[unk] = lut[l[unk]]
cs, _ = cv2.findContours(on.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
ol = np.zeros((H2, W2), np.uint8); cv2.drawContours(ol, cs, -1, 1, 4, cv2.LINE_8)
lab[(ol > 0)] = 7
lab[~on & (ol == 0)] = 0
a = cv2.GaussianBlur(cv2.dilate(on.astype(np.uint8) * 255, np.ones((3, 3), np.uint8)), (0, 0), .8)
out = np.dstack([(lab * 36).astype(np.uint8), q.astype(np.uint8), np.clip(e * 255, 0, 255).astype(np.uint8), a])
ys2, xs2 = np.where(a > 0); m = 2
out = out[max(0, ys2.min() - m):ys2.max() + m, max(0, xs2.min() - m):xs2.max() + m]
im = Image.fromarray(out, 'RGBA'); b = io.BytesIO(); im.save(b, 'PNG', optimize=True)
print(im.size, len(b.getvalue()))
json.dump({'w': im.size[0], 'h': im.size[1], 'src': 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()}, open('ski_map.json', 'w'))
