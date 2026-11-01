"""Versión 'ilustración' de una foto de casco: mismo encuadre que vtrace.py (para que las gafas encajen).
uso: python3 cartoon.py foto x0 y0 x1 y1 modo salida.png
modos: styl | toon | ink
"""
import sys, cv2, numpy as np

def prep(f, x0, y0, x1, y1):
    img = cv2.imread(f)[y0:y1, x0:x1]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    ys, xs = np.where(hsv[..., 2] > 200)
    if len(xs):
        img = img[ys.min() + 6:ys.max() - 6, xs.min() + 6:xs.max() - 6]
    h, w = img.shape[:2]
    S = 700 / max(w, h)
    img = cv2.resize(img, (int(w * S), int(h * S)), interpolation=cv2.INTER_CUBIC)
    h, w = img.shape[:2]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gm = np.full((h, w), cv2.GC_PR_FGD, np.uint8)
    light = (hsv[..., 2] > 228) & (hsv[..., 1] < 22)
    gm[light] = cv2.GC_PR_BGD
    gm[:4, :] = gm[-4:, :] = cv2.GC_BGD
    gm[:, :4] = gm[:, -4:] = cv2.GC_BGD
    b = np.zeros((1, 65), np.float64); fgm = np.zeros((1, 65), np.float64)
    cv2.grabCut(img, gm, None, b, fgm, 6, cv2.GC_INIT_WITH_MASK)
    fg = np.isin(gm, [cv2.GC_FGD, cv2.GC_PR_FGD]).astype(np.uint8) * 255
    fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(fg)
    big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
    fg = (lab == big).astype(np.uint8) * 255
    inv = 255 - fg; ff = inv.copy(); mm = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(ff, mm, (0, 0), 0)
    fg = fg | ff
    fg = cv2.morphologyEx(fg, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
    sat = hsv[..., 1][fg > 0].mean()
    if sat > 70:
        sh = ((hsv[..., 1] < 40) & (hsv[..., 2] > 110) & (fg > 0)).astype(np.uint8)
        ns, ls, ss, _ = cv2.connectedComponentsWithStats(sh)
        yb = np.where(fg > 0)[0].max()
        for i in range(1, ns):
            x, y, ww, hh, ar = ss[i]
            if y + hh > yb - 6 and ar > 200:
                fg[ls == i] = 0
        fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        n, lab, st, _ = cv2.connectedComponentsWithStats(fg)
        big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
        fg = (lab == big).astype(np.uint8) * 255
    return img, fg

def toon(img, fg, levels=3, ink=True, K=10):
    # 1) suavizado fuerte que conserva bordes
    sm = img.copy()
    for _ in range(6):
        sm = cv2.bilateralFilter(sm, 9, 28, 7)
    sm = cv2.pyrMeanShiftFiltering(sm, 9, 22)
    lab = cv2.cvtColor(sm, cv2.COLOR_BGR2LAB).astype(np.float32)
    L, A, B = lab[..., 0], lab[..., 1], lab[..., 2]
    # 2) color de diseño: agrupar por croma (a,b) + luminosidad suave
    pts = np.stack([A[fg > 0], B[fg > 0], L[fg > 0] * .45], 1)
    crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, .5)
    _, lbl, cen = cv2.kmeans(pts, K, None, crit, 4, cv2.KMEANS_PP_CENTERS)
    lab_img = np.zeros(fg.shape, np.uint8); lab_img[fg > 0] = lbl.ravel() + 1
    lab_img = cv2.medianBlur(lab_img, 5)
    # 3) luz en bandas dentro de cada región
    Lb = cv2.GaussianBlur(L, (0, 0), 3)
    out = np.zeros_like(lab)
    for k in range(K):
        m = (lab_img == k + 1)
        if not m.any():
            continue
        Lk = Lb[m]
        mu = np.median(Lk)
        # bandas: sombra / medio / brillo
        q = np.where(Lk < mu - 14, -1, np.where(Lk > mu + 16, 1, 0))
        base = np.array([np.median(L[m]), np.median(A[m]), np.median(B[m])])
        Lout = base[0] + q * np.where(q > 0, 22, 18)
        out[..., 0][m] = np.clip(Lout, 0, 255)
        out[..., 1][m] = base[1]
        out[..., 2][m] = base[2]
    res = cv2.cvtColor(np.clip(out, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)
    # suavizar bordes de bandas
    res = cv2.medianBlur(res, 5)
    if ink:
        g = cv2.cvtColor(sm, cv2.COLOR_BGR2GRAY)
        e = cv2.Canny(cv2.GaussianBlur(g, (0, 0), 1.6), 40, 90)
        e = cv2.dilate(e, np.ones((2, 2), np.uint8))
        res[e > 0] = (res[e > 0] * .35).astype(np.uint8)
    return res

def main():
    f = sys.argv[1]; x0, y0, x1, y1 = map(int, sys.argv[2:6]); mode = sys.argv[6]; out = sys.argv[7]
    img, fg = prep(f, x0, y0, x1, y1)
    if mode == 'styl':
        res = cv2.stylization(img, sigma_s=40, sigma_r=.35)
        g = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
        e = cv2.Canny(cv2.GaussianBlur(g, (0, 0), 1.4), 50, 110)
        res[e > 0] = (res[e > 0] * .45).astype(np.uint8)
    elif mode == 'toon':
        res = toon(img, fg, ink=False)
    else:
        res = toon(img, fg, ink=True)
    # contorno exterior
    cs, _ = cv2.findContours(fg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(res, cs, -1, (28, 20, 17), 6, cv2.LINE_AA)
    a = cv2.dilate(fg, np.ones((5, 5), np.uint8))
    a = cv2.GaussianBlur(a, (0, 0), 1)
    cv2.imwrite(out, np.dstack([res, a]))
    print(out, res.shape[1], res.shape[0])

main()
