"""Pinta el dibujo de líneas del casco por zonas con un diseño.
uso: python3 paint.py disenos.json salida_dir
"""
import cv2, numpy as np, json, sys, os

img = cv2.imread('helm_line.jpg'); g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY); H0, W0 = g.shape
line = (g < 150).astype(np.uint8)
lineC = cv2.dilate(line, np.ones((3, 3), np.uint8))
free = (1 - lineC).astype(np.uint8)
n, lab, st, cen = cv2.connectedComponentsWithStats(free, connectivity=4)
bgids = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]])).tolist())
bg = np.isin(lab, list(bgids))
helm = (~bg).astype(np.uint8)
nn, ll, ss, _ = cv2.connectedComponentsWithStats(helm)
big = 1 + np.argmax(ss[1:, cv2.CC_STAT_AREA]); helm = (ll == big).astype(np.uint8)
helm = cv2.morphologyEx(helm, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
inv = 1 - helm; ff = inv.copy(); mm = np.zeros((H0 + 2, W0 + 2), np.uint8); cv2.floodFill(ff, mm, (0, 0), 0); helm = helm | ff

PARTS = {
 'shell': [16, 12, 25, 7, 2, 17, 18, 52, 50, 93, 106, 26, 61, 162, 167],
 'band': [330], 'lower': [796], 'rim': [773],
 'peak': [9, 10, 19, 15, 35, 42, 58], 'peakAcc': [20],
 'chinFront': [849, 975, 887, 1001], 'chinVent': [888, 1007],
 'vent': [47, 59, 51, 60, 56, 65, 49, 94, 900, 21],
 'eyeMesh': [98], 'eyePad': [477, 187], 'eyeRim': [116, 818],
 'logo': [82], 'screw': [672],
}
MESH = ['eyeMesh', 'vent', 'chinVent']

def hx(c):
    c = c.lstrip('#'); return np.array([int(c[4:6], 16), int(c[2:4], 16), int(c[0:2], 16)], np.float32)  # BGR

def paint(D):
    col = np.zeros((H0, W0, 3), np.float32)
    known = np.zeros((H0, W0), np.uint8)
    partmap = {}
    base = {'eyeMesh': '#25282e', 'vent': '#23262c', 'chinVent': '#23262c', 'eyePad': '#3a3f48', 'eyeRim': '#1d2027', 'screw': '#2a2d33', 'logo': '#ffffff',
            'peak': D.get('shell'), 'peakAcc': D.get('peak', D.get('shell')), 'band': D.get('shell'), 'lower': D.get('shell'), 'rim': D.get('shell'), 'chinFront': D.get('lower', D.get('shell'))}
    base.update({k: v for k, v in D.items() if k in PARTS})
    if 'peak' in D: base['peakAcc'] = D.get('peakAcc', D['peak'])
    def filled(m):
        cs, _ = cv2.findContours(m.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        f = np.zeros((H0, W0), np.uint8); cv2.drawContours(f, cs, -1, 1, -1); return f.astype(bool)
    for p, ids in PARTS.items():
        m = np.isin(lab, ids)
        if p in MESH: m = filled(m) & (lineC == 0)
        col[m] = hx(base.get(p) or D['shell'])
        known[m] = 1
        partmap[p] = m
    # resto de zonas pequeñas sin clasificar: color carcasa
    rest = (helm > 0) & (known == 0) & (lineC == 0)
    col[rest] = hx(D['shell']); known[rest] = 1
    # rellenar píxeles de línea con el color de la zona más cercana
    dist, lbl = cv2.distanceTransformWithLabels((1 - known).astype(np.uint8), cv2.DIST_L2, 3, labelType=cv2.DIST_LABEL_PIXEL)
    ys, xs = np.where(known > 0)
    lut = np.zeros((lbl.max() + 1, 3), np.float32)
    idx = lbl[ys, xs]; lut[idx] = col[ys, xs]
    col = lut[lbl]
    # zonas de malla: oscuras con la retícula en gris
    meshm = np.zeros((H0, W0), bool)
    for p in MESH: meshm |= filled(partmap[p])
    meshm = cv2.dilate(meshm.astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool) & (helm > 0)
    # luz: degradado general desde arriba-izquierda
    yy, xx = np.mgrid[0:H0, 0:W0].astype(np.float32)
    ys2, xs2 = np.where(helm > 0); x0, x1, y0, y1 = xs2.min(), xs2.max(), ys2.min(), ys2.max()
    t = ((xx - x0) / (x1 - x0)) * .45 + ((yy - y0) / (y1 - y0)) * .75
    f = 1.22 - .55 * t
    # brillo especular en la parte alta de la carcasa
    spec = np.exp(-(((xx - (x0 + (x1 - x0) * .55)) / ((x1 - x0) * .22)) ** 2 + ((yy - (y0 + (y1 - y0) * .2)) / ((y1 - y0) * .07)) ** 2))
    shade = col * f[..., None] + 255 * .35 * spec[..., None] * (~meshm)[..., None]
    # sombra suave por zona (bordes de cada panel un poco más oscuros) para volumen
    panel = cv2.GaussianBlur((lineC == 0).astype(np.float32), (0, 0), 3)
    shade *= (0.86 + 0.14 * panel)[..., None]
    out = np.clip(shade, 0, 255)
    # líneas encima con antialias
    a = np.clip((200 - g.astype(np.float32)) / 110, 0, 1)
    lc = np.where(meshm[..., None], np.array([95, 92, 88], np.float32), np.array([28, 22, 18], np.float32))
    out = out * (1 - a[..., None]) + lc * a[..., None]
    # contorno exterior más grueso
    cs, _ = cv2.findContours(helm, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    out = out.astype(np.uint8)
    cv2.drawContours(out, cs, -1, (20, 16, 14), 5, cv2.LINE_AA)
    alpha = cv2.GaussianBlur(cv2.dilate(helm * 255, np.ones((3, 3), np.uint8)), (0, 0), .8)
    return out, alpha, cs

def main():
    designs = json.load(open(sys.argv[1])); od = sys.argv[2]; os.makedirs(od, exist_ok=True)
    ys, xs = np.where(helm > 0); m = 12
    X0, X1, Y0, Y1 = max(0, xs.min() - m), min(W0, xs.max() + m), max(0, ys.min() - m), min(H0, ys.max() + m)
    S = 700 / max(X1 - X0, Y1 - Y0)
    # hueco del ojo para las gafas
    ep = np.isin(lab, PARTS['eyeMesh'] + PARTS['eyePad'] + PARTS['eyeRim'])
    ey, ex = np.where(ep)
    port = [float((ex.min() - X0) * S), float((ey.min() - Y0) * S), float((ex.max() - ex.min()) * S), float((ey.max() - ey.min()) * S)]
    meta = {}
    for name, D in designs.items():
        out, alpha, cs = paint(D)
        rgba = np.dstack([out, alpha])[Y0:Y1, X0:X1]
        rgba = cv2.resize(rgba, (int((X1 - X0) * S), int((Y1 - Y0) * S)), interpolation=cv2.INTER_AREA)
        cv2.imwrite(os.path.join(od, name + '.png'), rgba)
    c = max(cs, key=cv2.contourArea).reshape(-1, 2).astype(np.float32)
    c = cv2.approxPolyDP(c.reshape(-1, 1, 2), 1.5, True).reshape(-1, 2)
    sil = 'M' + 'L'.join('%.1f,%.1f' % ((x - X0) * S, (y - Y0) * S) for x, y in c) + 'Z'
    json.dump({'w': int((X1 - X0) * S), 'h': int((Y1 - Y0) * S), 'port': port, 'sil': sil, 'layers': [{'col': '#000000', 'd': '', 'area': 1}]}, open(os.path.join(od, 'frame.json'), 'w'))
    print('ok', len(designs), port)

main()
