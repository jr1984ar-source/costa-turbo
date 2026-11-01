"""Piezas siempre negras marcadas por el usuario (trazos amarillos en anot.jpg), en coordenadas del recorte 'brava'."""
import cv2, numpy as np
from masks import load
def user_black():
    a = cv2.imread('anot.jpg'); o = cv2.imread('../trace/yam2.jpg')
    hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)
    ym = ((hsv[..., 0] > 18) & (hsv[..., 0] < 42) & (hsv[..., 1] > 80) & (hsv[..., 2] > 110)).astype(np.uint8)
    rgba = load('brava'); al = rgba[..., 3] > 100; H, W = al.shape
    sx, sy = 559 / (301 - 16), 299 / (156 - 3)
    M = np.float32([[sx, 0, -16 * sx], [0, sy, -3 * sy]])
    ymw = (cv2.warpAffine(ym * 255, M, (W, H)) > 60).astype(np.uint8)
    band = cv2.dilate(ymw, np.ones((5, 5), np.uint8))
    inv = (1 - band).astype(np.uint8); ff = inv.copy(); mm = np.zeros((H + 2, W + 2), np.uint8); cv2.floodFill(ff, mm, (0, 0), 0)
    rgb = rgba[..., :3]; hv = cv2.cvtColor(rgb.astype(np.uint8), cv2.COLOR_RGB2HSV).astype(np.float32)
    dark = al & (hv[..., 2] / 255 < .42) & (hv[..., 1] / 255 < .6)
    out = np.zeros((H, W), bool)
    n, l, st, cen = cv2.connectedComponentsWithStats(ff)
    for i in range(1, n):
        cx = cen[i][0]; m = l == i
        if cx > 400: out |= m & dark          # proa: solo el parachoques oscuro
        else: out |= m & al                   # popa, zona tras el asiento, manillar, hueco de pies: entero
    wide = cv2.dilate(ymw, np.ones((17, 17), np.uint8)) > 0
    out |= wide & dark                        # tiras negras que siguen los trazos
    out = cv2.morphologyEx(out.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8)) > 0
    return out & al
