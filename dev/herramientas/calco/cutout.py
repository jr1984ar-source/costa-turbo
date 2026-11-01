"""Recorta un objeto de una foto con fondo claro y guarda PNG con transparencia.
Opcional: recolorea (amarillo/rojo -> otro tono) y aclara grises para versiones blancas.
uso: python3 cutout.py foto salida.png [--hue SRC:DST] [--white] [--flip]
"""
import sys, cv2, numpy as np

def mask_of(img):
    h, w = img.shape[:2]
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gm = np.full((h, w), cv2.GC_PR_FGD, np.uint8)
    light = (hsv[..., 2] > 232) & (hsv[..., 1] < 18)
    gm[light] = cv2.GC_PR_BGD
    gm[:3, :] = gm[-3:, :] = cv2.GC_BGD
    gm[:, :3] = gm[:, -3:] = cv2.GC_BGD
    b = np.zeros((1, 65), np.float64); f = np.zeros((1, 65), np.float64)
    cv2.grabCut(img, gm, None, b, f, 6, cv2.GC_INIT_WITH_MASK)
    fg = np.isin(gm, [cv2.GC_FGD, cv2.GC_PR_FGD]).astype(np.uint8) * 255
    fg = cv2.morphologyEx(fg, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    n, lab, st, _ = cv2.connectedComponentsWithStats(fg)
    big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
    fg = (lab == big).astype(np.uint8) * 255
    inv = 255 - fg; ff = inv.copy(); mm = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(ff, mm, (0, 0), 0)
    fg = fg | ff
    return fg

def main():
    src, out = sys.argv[1], sys.argv[2]
    args = sys.argv[3:]
    raw = cv2.imread(src, cv2.IMREAD_UNCHANGED)
    srcA = None
    if raw.ndim == 3 and raw.shape[2] == 4:
        srcA = raw[..., 3]
        al = srcA.astype(np.float32)[..., None] / 255
        img = (raw[..., :3].astype(np.float32) * al + 255 * (1 - al)).astype(np.uint8)
    else:
        img = raw if raw.ndim == 3 else cv2.cvtColor(raw, cv2.COLOR_GRAY2BGR)
    if '--flip' in args:
        img = cv2.flip(img, 1)
    # recorte opcional x0,y0,x1,y1
    if '--crop' in args:
        x0, y0, x1, y1 = map(int, args[args.index('--crop') + 1].split(','))
        img = img[y0:y1, x0:x1]
    h, w = img.shape[:2]
    S = 900 / max(w, h)
    if S > 1:
        img = cv2.resize(img, (int(w * S), int(h * S)), interpolation=cv2.INTER_LANCZOS4)
    if srcA is not None and (srcA < 128).mean() > .05:
        m = srcA
        if S > 1: m = cv2.resize(m, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_LINEAR)
        fg = (m > 127).astype(np.uint8) * 255
        n, lab, st, _ = cv2.connectedComponentsWithStats(fg)
        big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA]); fg = (lab == big).astype(np.uint8) * 255
    else:
        fg = mask_of(img)
    if '--cutshadow' in args:
        hsv0 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        solid = ((hsv0[..., 2] < 30) | ((hsv0[..., 1] > 80) & (hsv0[..., 2] > 80))) & (fg > 0)
        solid = cv2.morphologyEx(solid.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        hh, ww = fg.shape
        keel = np.full(ww, np.nan)
        for x in range(ww):
            ys_ = np.where(solid[:, x] > 0)[0]
            if len(ys_): keel[x] = ys_.max()
        ok = ~np.isnan(keel); xs_ = np.arange(ww)
        keel = np.interp(xs_, xs_[ok], keel[ok])
        r = 25; kp = np.pad(keel, r, mode='edge')
        keel = np.array([np.median(kp[i:i + 2 * r + 1]) for i in range(ww)])
        keel = np.maximum(keel, np.interp(xs_, xs_[ok], np.where(ok, keel, 0)[ok]))
        for x in range(ww):
            fg[int(keel[x]) + 4:, x] = 0
        n, lab, st, _ = cv2.connectedComponentsWithStats(fg)
        big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA]); fg = (lab == big).astype(np.uint8) * 255
    a = cv2.GaussianBlur(fg, (0, 0), 1.2)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
    if '--hue' in args:
        s0, d0 = args[args.index('--hue') + 1].split(':')
        s0, d0 = float(s0) / 2, float(d0) / 2  # OpenCV usa 0-180
        H = hsv[..., 0]
        diff = np.abs(((H - s0 + 90) % 180) - 90)
        sel = (diff < 16) & (hsv[..., 1] > 60)
        k = np.clip(1 - (diff - 10) / 6, 0, 1) * (hsv[..., 1] > 60)
        newH = (H + (d0 - s0)) % 180
        hsv[..., 0] = np.where(k > 0, newH, H)
        if '--vk' in args:
            vk = float(args[args.index('--vk') + 1])
            hsv[..., 2] = np.where(k > 0, np.clip(hsv[..., 2] * vk, 0, 255), hsv[..., 2])
    if '--goldy' in args:
        H, S_, V = hsv[..., 0], hsv[..., 1], hsv[..., 2]
        sel = (H > 8) & (H < 32) & (S_ > 18) & (V > 70)
        w = cv2.GaussianBlur(sel.astype(np.float32), (0, 0), 1.5)
        hsv[..., 0] = H * (1 - w) + 25 * w
        hsv[..., 1] = np.clip(S_ * (1 - w) + np.clip(S_ * 4.2 + 60, 0, 245) * w, 0, 255)
        hsv[..., 2] = np.clip(V * (1 - w) + np.clip(V * 1.08, 0, 255) * w, 0, 255)
    if '--greyy' in args:
        H, S_, V = hsv[..., 0], hsv[..., 1], hsv[..., 2]
        w = np.clip((45 - S_) / 20, 0, 1) * np.clip((V - 105) / 30, 0, 1)
        w = cv2.GaussianBlur(w.astype(np.float32), (0, 0), 1.5)
        hsv[..., 0] = H * (1 - w) + 26 * w
        hsv[..., 1] = S_ * (1 - w) + 215 * w
        hsv[..., 2] = np.clip(V * (1 - w) + (V * 1.12 + 10) * w, 0, 255)
    if '--white' in args:
        S_, V = hsv[..., 1], hsv[..., 2]
        wgt = np.clip((70 - S_) / 30, 0, 1)
        wgt = cv2.GaussianBlur(wgt, (0, 0), 2)
        nv = 112 + V * .58
        hsv[..., 2] = V * (1 - wgt) + nv * wgt
        hsv[..., 1] = S_ * (1 - wgt * .7)
    out_img = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    ys, xs = np.where(fg > 0)
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    rgba = np.dstack([out_img, a])[y0:y1, x0:x1]
    cv2.imwrite(out, rgba)
    print(out, rgba.shape[1], rgba.shape[0])

main()
