"""Mapas de piezas de cada moto con foto: 0 nada, 1 casco, 2 laterales, 3 capó, 4 rayas, 5 asiento."""
import json, base64, io, cv2, numpy as np
from PIL import Image
PH = json.load(open('../trace/moto_photos.json'))
GEO = {
 'yam1': dict(rail=[(0,98),(30,108),(100,140),(200,178),(300,214),(400,246),(480,268),(520,278),(560,283)],
   seat=[(118,40),(122,12),(140,2),(175,4),(210,30),(250,48),(282,62),(292,85),(292,118),(272,126),(240,122),(205,108),(180,95),(150,80),(125,65)],
   hood=[(365,62),(400,58),(430,70),(470,100),(505,140),(540,190),(556,230),(540,250),(500,245),(460,220),(420,190),(380,160),(345,130),(335,100)]),
 'yam2': dict(rail=[(5,105),(100,145),(200,190),(260,212),(330,232),(420,252),(480,262),(540,268),(560,280)],
   seat=[(115,25),(125,5),(150,2),(170,20),(200,40),(240,55),(262,75),(265,90),(240,95),(200,90),(165,80),(135,65),(118,50)],
   hood=[(320,95),(370,80),(410,75),(440,80),(470,110),(500,150),(530,190),(545,230),(520,245),(470,235),(420,215),(370,180),(330,140),(310,115)]),
 'yam3': dict(rail=[(0,100),(60,125),(100,145),(200,182),(300,215),(400,245),(480,270),(540,282),(560,292)],
   seat=[(115,30),(125,8),(160,5),(200,30),(240,45),(270,65),(285,100),(285,125),(255,130),(220,120),(180,100),(140,80),(118,60)],
   hood=[(365,70),(400,65),(440,75),(470,110),(500,150),(530,200),(545,240),(520,255),(480,240),(440,215),(400,185),(360,155),(330,120),(330,95)]),
 'kawa': dict(rail=[(0,105),(100,128),(200,152),(300,176),(400,192),(480,205),(560,220)],
   seat=[(120,40),(130,15),(150,5),(190,15),(230,40),(265,60),(270,90),(260,110),(220,115),(180,105),(150,85),(125,65)],
   hood=[(300,60),(330,40),(380,40),(420,55),(460,80),(500,110),(530,140),(545,180),(520,200),(470,195),(420,180),(380,170),(330,160),(300,140),(290,100)]),
 'vx': dict(rail=[(0,100),(60,125),(150,160),(250,205),(320,235),(400,252),(480,268),(560,280)],
   seat=[(105,20),(115,4),(140,0),(175,6),(215,18),(255,36),(280,58),(286,95),(272,118),(240,124),(195,112),(160,95),(130,70),(110,45)],
   hood=[(300,90),(330,70),(370,60),(410,55),(440,75),(480,110),(510,150),(530,190),(535,220),(500,235),(450,220),(400,190),(350,150),(310,120)],
   bar=[(228,12),(260,8),(300,4),(356,14),(362,30),(352,42),(352,80),(318,84),(296,82),(282,80),(270,36),(232,32)]),
 'sd': dict(rail=[(10,95),(60,130),(150,180),(250,220),(350,250),(450,280),(530,300),(560,310)],
   seat=[(120,35),(125,5),(150,0),(180,15),(215,30),(250,45),(255,70),(240,95),(225,115),(200,120),(175,100),(150,80),(125,60)],
   hood=[(270,100),(300,70),(340,60),(400,70),(430,85),(450,120),(480,160),(510,200),(520,230),(480,240),(440,230),(380,210),(320,180),(270,140)]),
}
# por moto: forma y clase de píxel que se pinta en cada pieza
CFG = {
 'avispa': ('yam1', dict(hull='sat', side='mid', hood='mid', stripe='sat', seat='mid')),
 'inferno': ('yam1', dict(hull='sat', side='mid', hood='mid', stripe='sat', seat='mid')),
 'oceano': ('yam1', dict(hull='sat', side='mid', hood='mid', stripe='sat', seat='mid')),
 'marea': ('yam1', dict(hull='sat', side='mid', hood='mid', stripe='sat', seat='mid')),
 'brava': ('yam2', dict(hull='sat', side='sat', hood='sat', stripe='light', seat='light')),
 'sombra': ('yam3', dict(hull='mid', side='dark', hood='dark', stripe='light', seat='mid')),
 'veneno': ('kawa', dict(hull='mid', side='dark', hood='sat', stripe='sat', seat='mid')),
 'gris': ('sd', dict(hull='grey', side='grey', hood='dark', stripe='sat', seat='grey')),
 'solar': ('sd', dict(hull='yel', side='yel', hood='dark', stripe='red', seat='red')),
 'blanca': ('vx', dict(hull='white', side='white', hood='white', stripe='greyg', seat='white')),
 'dorada': ('sd', dict(hull='beige', side='beige', hood='dark', stripe='red', seat='red')),
}

def load(k):
    b = base64.b64decode(PH[k]['src'].split(',')[1])
    return np.array(Image.open(io.BytesIO(b)).convert('RGBA'))

def classes(rgba):
    rgb = rgba[..., :3].astype(np.uint8)
    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV).astype(np.float32)
    H, S, V = hsv[..., 0] * 2, hsv[..., 1] / 255, hsv[..., 2] / 255
    L = (rgb[..., 0] * .299 + rgb[..., 1] * .587 + rgb[..., 2] * .114) / 255
    on = rgba[..., 3] > 100
    C = {
     'sat': on & (S > .32) & (L > .1),
     'dark': on & (S < .3) & (L < .4) & (L > .03),
     'mid': on & (S < .3) & (L < .62) & (L > .03),
     'light': on & (S < .28) & (L >= .45),
     'grey': on & (S < .3) & (L > .3),
     'yel': on & (S > .3) & (H > 35) & (H < 75),
     'red': on & (S > .35) & ((H < 25) | (H > 330)),
     'white': on & (S < .25) & (L > .62),
     'greyg': on & (S < .2) & (L > .38) & (L < .64),
     'beige': on & (S > .08) & (S < .45) & (L > .42) & (H > 20) & (H < 60),
    }
    return C, on

def polymask(pts, shape):
    m = np.zeros(shape, np.uint8); cv2.fillPoly(m, [np.array(pts, np.int32)], 1); return m.astype(bool)

def below(rail, shape):
    h, w = shape; xs = np.arange(w); ry = np.interp(xs, [p[0] for p in rail], [p[1] for p in rail])
    return np.arange(h)[:, None] > ry[None, :]

def build(k):
    geo, cfg = CFG[k]; G = GEO[geo]
    rgba = load(k); C, on = classes(rgba); sh = on.shape
    seat = polymask(G['seat'], sh); hood = polymask(G['hood'], sh); low = below(G['rail'], sh)
    lab = np.zeros(sh, np.uint8)
    up = on & ~low
    lab[up & ~seat & ~hood & C[cfg['side']]] = 2
    lab[up & hood & ~seat & C[cfg['hood']]] = 3
    lab[up & ~seat & C[cfg['stripe']] & (lab == 0)] = 4
    lab[seat & C[cfg['seat']]] = 5
    if cfg['stripe'] in ('sat', 'red', 'light'):
        lab[seat & C[cfg['stripe']] & (lab == 0)] = 4
    lab[low & on & C[cfg['hull']]] = 1
    if 'bar' in G: lab[polymask(G['bar'], sh)] = 0
    # suavizar: cada píxel toma la pieza mayoritaria de su alrededor
    sg = 2.6 if k == 'sombra' else 1.3
    st = np.stack([cv2.GaussianBlur((lab == v).astype(np.float32), (0, 0), sg) for v in range(6)], 0)
    out = np.argmax(st, 0).astype(np.uint8)
    out[~on] = 0
    return rgba, out

if __name__ == '__main__':
    COL = {1: (255, 60, 60), 2: (60, 160, 255), 3: (255, 200, 0), 4: (60, 220, 90), 5: (220, 80, 255)}
    res = {}; tiles = []
    for k in CFG:
        rgba, lab = build(k)
        png = Image.fromarray((lab * 40).astype(np.uint8), 'L'); b = io.BytesIO(); png.save(b, 'PNG', optimize=True)
        res[k] = 'data:image/png;base64,' + base64.b64encode(b.getvalue()).decode()
        vis = rgba[..., :3].astype(np.float32).copy()
        for v, c in COL.items():
            m = lab == v; vis[m] = vis[m] * .35 + np.array(c) * .65
        bg = np.full_like(vis, 235); a = (rgba[..., 3:4] / 255.)
        tiles.append((k, (vis * a + bg * (1 - a)).astype(np.uint8)))
        print(k, len(b.getvalue()), [(v, int((lab == v).sum())) for v in range(1, 6)])
    json.dump(res, open('moto_masks.json', 'w'))
    W = 560; rows = []
    for i in range(0, len(tiles), 2):
        pair = [t[1] for t in tiles[i:i + 2]]
        hh = max(p.shape[0] for p in pair)
        row = np.full((hh, W * 2, 3), 255, np.uint8)
        for j, p in enumerate(pair): row[:p.shape[0], j * W:j * W + p.shape[1]] = p
        rows.append(row)
    Image.fromarray(np.vstack(rows)).save('masks_vis.png')
