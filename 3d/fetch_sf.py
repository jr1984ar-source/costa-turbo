# Descarga modelos de Sketchfab (la clave la añade el proxy del entorno) y guarda autor y licencia
import json, os, sys, io, zipfile, urllib.request
UA = {'User-Agent': 'CostaTurbo3D-asset-fetch/1.0'}
_tk = os.path.expanduser('~/Desktop/API token.txt')
if os.path.exists(_tk): UA['Authorization'] = 'Token ' + open(_tk).read().strip()
import time
def get(u, t=120):
    for i in range(8):
        try: return urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t).read()
        except urllib.error.HTTPError as e:
            if e.code != 429: raise
            time.sleep(70)
    raise Exception('429 persistente')
credits = json.load(open('assets/sketchfab/CREDITOS.json')) if os.path.exists('assets/sketchfab/CREDITOS.json') else {}
for a in sys.argv[1:]:
    name, uid = a.split('=')
    dst = f'assets/sketchfab/{name}'
    if os.path.isdir(dst) and os.listdir(dst): print('ya', name); continue
    try:
        info = json.loads(get(f'https://api.sketchfab.com/v3/models/{uid}'))
        dl = json.loads(get(f'https://api.sketchfab.com/v3/models/{uid}/download'))
        z = urllib.request.urlopen(urllib.request.Request(dl['gltf']['url'], headers={'User-Agent': UA['User-Agent']}), timeout=600).read()
        os.makedirs(dst, exist_ok=True); zipfile.ZipFile(io.BytesIO(z)).extractall(dst)
        credits[name] = {'titulo': info['name'], 'autor': info['user']['username'], 'licencia': (info.get('license') or {}).get('label'), 'url': info['viewerUrl']}
        print('OK', name, round(len(z) / 1e6, 1), 'MB')
    except Exception as e: print('ERR', name, e)
os.makedirs('assets/sketchfab', exist_ok=True)
json.dump(credits, open('assets/sketchfab/CREDITOS.json', 'w'), indent=1, ensure_ascii=False)
