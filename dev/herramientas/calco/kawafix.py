"""Kawasaki: voltear, poner los letreros del derecho y quitar la sombra del suelo."""
import cv2, numpy as np
img = cv2.flip(cv2.imread('kawa.jpg'), 1)
H, W = img.shape[:2]
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
BOX = [(355, 448, 448, 536, 'white', 0.55), (212, 498, 338, 552, 'white', None), (462, 672, 608, 742, 'white', None),
       (968, 598, 1138, 668, 'grey', None), (732, 448, 798, 512, 'white', None)]
out = img.copy()
layers = []
for x0, y0, x1, y1, kind, fth in BOX:
    p = hsv[y0:y1, x0:x1]
    S, V = p[..., 1], p[..., 2]
    if kind == 'white':
        soft = np.clip((V - 150) / 60, 0, 1) * (S < 70)
    else:
        soft = np.clip((90 - S) / 30, 0, 1) * np.clip((235 - V) / 25, 0, 1) * (V > 80)
    hard = (soft > .35).astype(np.uint8)
    ys, xs = np.where(hard > 0)
    pts = np.stack([xs, ys], 1).astype(np.float32)
    mu = pts.mean(0)
    cov = np.cov((pts - mu).T)
    ev, evec = np.linalg.eigh(cov)
    d = evec[:, np.argmax(ev)]
    th = np.arctan2(d[1], d[0])
    if abs(th) > np.pi / 2: th -= np.sign(th) * np.pi
    if fth is not None: th = fth
    c2, s2 = np.cos(2 * th), np.sin(2 * th)
    R = np.array([[-c2, -s2], [-s2, c2]], np.float32)
    cx, cy = mu
    M = np.hstack([R, (np.array([cx, cy]) - R @ np.array([cx, cy]))[:, None]]).astype(np.float32)
    patch = img[y0:y1, x0:x1]
    wp = cv2.warpAffine(patch, M, (x1 - x0, y1 - y0), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    wa = cv2.warpAffine(soft.astype(np.float32), M, (x1 - x0, y1 - y0), flags=cv2.INTER_LINEAR)
    # borrar el letrero espejado
    m = np.zeros((H, W), np.uint8)
    m[y0:y1, x0:x1] = cv2.dilate(hard, np.ones((5, 5), np.uint8)) * 255
    out = cv2.inpaint(out, m, 6, cv2.INPAINT_TELEA)
    layers.append((x0, y0, x1, y1, wp, wa))
for x0, y0, x1, y1, wp, wa in layers:
    reg = out[y0:y1, x0:x1].astype(np.float32)
    a = wa[..., None]
    out[y0:y1, x0:x1] = (wp.astype(np.float32) * a + reg * (1 - a)).astype(np.uint8)
# sombra: todo lo que queda por debajo de la quilla, a blanco
K = [(0, 600), (100, 618), (200, 642), (290, 690), (400, 740), (500, 772), (600, 798), (700, 822), (800, 842), (900, 862),
     (1000, 880), (1100, 886), (1180, 870), (1230, 840), (1270, 812), (1300, 790), (1400, 745), (1500, 700)]
poly = np.array(K + [(W, H), (0, H)], np.int32)
cv2.fillPoly(out, [poly], (255, 255, 255))
cv2.imwrite('kawa_fixed.png', out)
print('ok')
