"""Calca un casco de una foto (fondo claro) a SVG por capas de color.
uso: python3 vtrace.py foto.jpg x0 y0 x1 y1 K salida.json [flip]
"""
import sys, json, cv2, numpy as np

def smooth_path(pts):
    # curva suave por puntos medios (cuadráticas)
    n = len(pts)
    if n < 3:
        return ''
    mids = [((pts[i][0] + pts[(i + 1) % n][0]) / 2, (pts[i][1] + pts[(i + 1) % n][1]) / 2) for i in range(n)]
    d = 'M%.1f,%.1f' % mids[-1]
    for i in range(n):
        d += 'Q%.1f,%.1f %.1f,%.1f' % (pts[i][0], pts[i][1], mids[i][0], mids[i][1])
    return d + 'Z'

def main():
    f, x0, y0, x1, y1, K, out = sys.argv[1], *map(int, sys.argv[2:7]), sys.argv[7]
    flip = len(sys.argv) > 8 and sys.argv[8] == 'flip'
    img = cv2.imread(f)[y0:y1, x0:x1]
    if flip:
        img = cv2.flip(img, 1)
    # recortar a la tarjeta blanca (caja de todos los píxeles claros)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ys, xs = np.where(hsv[..., 2] > 200)
    if len(xs):
        img = img[ys.min() + 6:ys.max() - 6, xs.min() + 6:xs.max() - 6]
    h, w = img.shape[:2]
    S = 700 / max(w, h)
    img = cv2.resize(img, (int(w * S), int(h * S)), interpolation=cv2.INTER_CUBIC)
    h, w = img.shape[:2]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # GrabCut: claro y gris = probable fondo, borde = fondo seguro
    gm = np.full((h, w), cv2.GC_PR_FGD, np.uint8)
    light = (hsv[..., 2] > 228) & (hsv[..., 1] < 22)
    gm[light] = cv2.GC_PR_BGD
    gm[:4, :] = gm[-4:, :] = cv2.GC_BGD
    gm[:, :4] = gm[:, -4:] = cv2.GC_BGD
    bgm = np.zeros((1, 65), np.float64); fgm = np.zeros((1, 65), np.float64)
    cv2.grabCut(img, gm, None, bgm, fgm, 6, cv2.GC_INIT_WITH_MASK)
    fg = np.isin(gm, [cv2.GC_FGD, cv2.GC_PR_FGD]).astype(np.uint8) * 255
    fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(fg)
    big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
    fg = (lab == big).astype(np.uint8) * 255
    # rellenar agujeros
    inv = 255 - fg
    ff = inv.copy(); mm = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(ff, mm, (0, 0), 0)
    fg = fg | ff
    fg = cv2.morphologyEx(fg, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
    # quitar sombra gris pegada abajo en cascos de color
    sat = hsv[..., 1][fg > 0].mean()
    if sat > 70:
        sh = ((hsv[..., 1] < 40) & (hsv[..., 2] > 110) & (fg > 0)).astype(np.uint8)
        ns, ls, ss, cs_ = cv2.connectedComponentsWithStats(sh)
        yb = np.where(fg > 0)[0].max()
        for i in range(1, ns):
            x, y, ww, hh, ar = ss[i]
            if y + hh > yb - 6 and ar > 200:
                fg[ls == i] = 0
        fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        n, lab, st, _ = cv2.connectedComponentsWithStats(fg)
        big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
        fg = (lab == big).astype(np.uint8) * 255
    # suavizado conservando bordes
    sm = cv2.pyrMeanShiftFiltering(img, 7, 18)
    sm = cv2.bilateralFilter(sm, 9, 30, 9)
    labi = cv2.cvtColor(sm, cv2.COLOR_BGR2LAB).astype(np.float32)
    pts = labi[fg > 0]
    crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, .5)
    _, lbl, cen = cv2.kmeans(pts, K, None, crit, 4, cv2.KMEANS_PP_CENTERS)
    L = np.full((h, w), -1, np.int32)
    L[fg > 0] = lbl.ravel()
    # limpiar etiquetas: filtro de moda
    Lm = L.copy().astype(np.float32)
    lab_img = np.zeros((h, w), np.uint8)
    lab_img[fg > 0] = (lbl.ravel() + 1).astype(np.uint8)
    lab_img = cv2.medianBlur(lab_img, 5)
    lab_img[fg == 0] = 0
    cols = cv2.cvtColor(cen.reshape(1, -1, 3).astype(np.uint8), cv2.COLOR_LAB2BGR).reshape(-1, 3)
    layers = []
    # silueta
    cs, _ = cv2.findContours(fg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    sil = max(cs, key=cv2.contourArea)
    sil = cv2.approxPolyDP(sil, 1.2, True).reshape(-1, 2).tolist()
    # orden por luminancia (oscuro primero) para que las zonas claras queden encima
    order = np.argsort(cen[:, 0])
    for k in order:
        m = (lab_img == k + 1).astype(np.uint8) * 255
        m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        cs, hier = cv2.findContours(m, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
        if hier is None:
            continue
        d = ''
        for i, c in enumerate(cs):
            if cv2.contourArea(c) < 18:
                continue
            a = cv2.approxPolyDP(c, 1.0, True).reshape(-1, 2).tolist()
            d += smooth_path(a)
        if d:
            b, g_, r = [int(v) for v in cols[k]]
            layers.append({'col': '#%02x%02x%02x' % (r, g_, b), 'L': float(cen[k][0]), 'a': float(cen[k][1]), 'b': float(cen[k][2]), 'd': d, 'area': int((lab_img == k + 1).sum())})
    # hueco del ojo: componente oscura grande en la parte delantera
    TH = int(sys.argv[9]) if len(sys.argv) > 9 else 40
    dark = ((cv2.cvtColor(sm, cv2.COLOR_BGR2GRAY) < TH) & (fg > 0)).astype(np.uint8)
    yy, xx = np.where(fg > 0); fx0, fx1, fy0, fy1 = xx.min(), xx.max(), yy.min(), yy.max()
    win = np.zeros_like(dark); win[int(fy0 + (fy1 - fy0) * .18):int(fy0 + (fy1 - fy0) * .85), int(fx0 + (fx1 - fx0) * .08):int(fx0 + (fx1 - fx0) * .72)] = 1
    dark = dark & win
    dark = cv2.morphologyEx(dark, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    nd, ld, sd, cd = cv2.connectedComponentsWithStats(dark)
    port = None
    best = 0
    for i in range(1, nd):
        x, y, ww, hh, ar = sd[i]
        cx, cy = cd[i]
        if ar > best:
            best = ar; port = [int(x), int(y), int(ww), int(hh)]
    json.dump({'w': w, 'h': h, 'sil': smooth_path(sil), 'layers': layers, 'port': port}, open(out, 'w'))
    print(out, w, h, len(layers))

main()
