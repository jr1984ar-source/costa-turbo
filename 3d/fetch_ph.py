# Descarga recursos CC0 de Poly Haven (texturas, cielos HDRI y modelos glTF)
import json, os, sys, urllib.request
UA = {'User-Agent': 'CostaTurbo3D-asset-fetch/1.0'}
def op(url, t=60): return urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=t)
OUT = 'assets'
def get(url, path):
    if os.path.exists(path) and os.path.getsize(path) > 0: return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    for i in range(4):
        try:
            with op(url, 120) as r, open(path, 'wb') as f: f.write(r.read()); return
        except Exception as e: print('retry', url, e)
    raise SystemExit('fail ' + url)
def files(aid): return json.load(op(f'https://api.polyhaven.com/files/{aid}'))
def texture(aid, res='2k', maps=('Diffuse', 'nor_gl', 'Rough')):
    f = files(aid)
    for m in maps:
        if m in f and res in f[m]:
            u = f[m][res]['jpg']['url'] if 'jpg' in f[m][res] else f[m][res]['png']['url']
            get(u, f'{OUT}/tex/{aid}_{m}_{res}.' + u.split('.')[-1]); print('tex', aid, m)
def hdri(aid, res='2k'):
    f = files(aid); u = f['hdri'][res]['hdr']['url']; get(u, f'{OUT}/hdri/{aid}_{res}.hdr'); print('hdri', aid)
def model(aid, res='1k'):
    f = files(aid); g = f['gltf'][res]['gltf']; base = f'{OUT}/models/{aid}'
    get(g['url'], f'{base}/{aid}.gltf')
    for p, inc in g.get('include', {}).items(): get(inc['url'], f'{base}/{p}')
    print('model', aid)
for a in sys.argv[1:]:
    kind, aid, *r = a.split(':')
    {'t': texture, 'h': hdri, 'm': model}[kind](aid, *r)
