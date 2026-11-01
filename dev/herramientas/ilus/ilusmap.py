"""Piezas de la moto ilustrada: 1 casco abajo, 2 casco arriba, 3 tapa delantera, 4 detalles, 5 asiento, 6 negro fijo."""
import cv2, numpy as np, json, base64, io
from PIL import Image
rgba = cv2.cvtColor(cv2.imread('ilus_cut.png', cv2.IMREAD_UNCHANGED), cv2.COLOR_BGRA2RGBA)
H, W = rgba.shape[:2]; rgb = rgba[..., :3]; on = rgba[..., 3] > 100
hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV).astype(np.float32)
Hh, S, V = hsv[..., 0] * 2, hsv[..., 1] / 255, hsv[..., 2] / 255
L = (rgb[..., 0] * .299 + rgb[..., 1] * .587 + rgb[..., 2] * .114) / 255
red = on & (S > .4) & ((Hh < 30) | (Hh > 330))
dark = on & ~red
def poly(p):
    m = np.zeros((H, W), np.uint8); cv2.fillPoly(m, [np.array(p, np.int32)], 1); return m > 0
RAIL = [(0, 205), (70, 282), (230, 338), (400, 400), (540, 452), (760, 522), (980, 596), (1150, 612), (1272, 600)]
xs = np.arange(W); ry = np.interp(xs, [p[0] for p in RAIL], [p[1] for p in RAIL]); low = np.arange(H)[:, None] > ry[None, :]
SEAT = [(262, 40), (300, 4), (400, 8), (470, 40), (540, 80), (610, 120), (655, 165), (662, 235), (645, 268), (590, 280), (520, 268), (470, 240), (420, 200), (360, 160), (300, 115), (266, 78)]
HOOD = [(722, 205), (790, 175), (860, 150), (930, 140), (995, 150), (1040, 220), (1075, 290), (1105, 345), (1135, 395), (1142, 445), (1090, 440), (1020, 405), (950, 365), (880, 320), (820, 290), (760, 255), (725, 235)]
DET = [[(585, 62), (640, 56), (642, 78), (588, 82)], [(835, 8), (870, 6), (872, 28), (838, 30)],
       [(240, 168), (305, 172), (308, 205), (245, 205)], [(548, 282), (690, 292), (695, 330), (552, 322)]]
MK = json.load(open('marks3.json')); OX, OY = 24, 69
line = L < .1
def grow(hulls, dil, base):
    out = np.zeros((H, W), bool)
    for hpts in hulls:
        p = np.array([[x - OX, y - OY] for x, y in hpts], np.int32)
        hm = np.zeros((H, W), np.uint8); cv2.fillPoly(hm, [p], 1)
        lim = cv2.dilate(hm, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (dil, dil))) > 0
        cand = (base & ~line & lim).astype(np.uint8)
        n, l = cv2.connectedComponents(cand)
        ids = set(np.unique(l[(hm > 0) & (cand > 0)]).tolist()) - {0}
        for i in ids:
            comp = l == i
            if comp.sum() > 15: out |= comp
        out |= (hm > 0) & base
    out = cv2.morphologyEx(out.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8)) > 0
    return out & on
DETM = grow(MK['blue'], 31, dark)
SEATM = grow(MK['pink'], 61, dark)
HOODM = grow(MK['yel'], 71, dark)
lab = np.zeros((H, W), np.uint8)
lab[dark] = 6
lab[red & low] = 1
lab[red & ~low] = 2
lab[HOODM | (poly(HOOD) & dark)] = 3
lab[(poly(SEAT) & dark) | SEATM] = 5
lab[DETM] = 4
# contornos negros finos dentro de piezas: se quedan como líneas (factor bajo)
lab[~on] = 0
# luz relativa a la mediana de cada pieza
F = np.ones((H, W), np.float32); ref = {}
for v in range(1, 6):
    m = lab == v
    if not m.any(): continue
    md = float(np.median(L[m])); ref[v] = md
    F[m] = L[m] / max(md, .02)
F = np.clip(F * 90, 0, 255)
mp = np.dstack([(lab * 36).astype(np.uint8), F.astype(np.uint8), np.zeros((H, W), np.uint8), np.full((H, W), 255, np.uint8)])
out = {'w': W, 'h': H, 'ref': ref}
b = io.BytesIO(); Image.fromarray(mp, 'RGBA').save(b, 'PNG', optimize=True); out['map'] = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
b = io.BytesIO(); Image.fromarray(rgba, 'RGBA').save(b, 'WEBP', quality=88, method=6); out['img'] = 'data:image/webp;base64,' + base64.b64encode(b.getvalue()).decode()
json.dump(out, open('ilus_map.json', 'w')); print(ref, len(out['map']), len(out['img']))
vis = rgb.astype(np.float32).copy()
COL = {1: (255, 60, 60), 2: (60, 160, 255), 3: (255, 200, 0), 4: (60, 220, 90), 5: (220, 80, 255)}
for v, c in COL.items():
    m = lab == v; vis[m] = vis[m] * .3 + np.array(c) * .7
bg = np.full_like(vis, 235); a = rgba[..., 3:4] / 255.
Image.fromarray((vis * a + bg * (1 - a)).astype(np.uint8)).save('ilus_parts.png')
