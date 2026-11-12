# Descarga modelos de Sketchfab (la clave la añade el proxy del entorno) y guarda autor y licencia
import json, os, sys, io, zipfile, urllib.request
UA = {'User-Agent': 'CostaTurbo3D-asset-fetch/1.0'}
TOKEN = os.environ.get('SKETCHFAB_TOKEN') or (open(os.path.expanduser('~/Desktop/Api token.txt')).read().strip() if os.path.exists(os.path.expanduser('~/Desktop/Api token.txt')) else '')
def get(u, t=120):
    h = dict(UA)
    if TOKEN and 'api.sketchfab.com' in u: h['Authorization'] = 'Token ' + TOKEN
    return urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=t).read()
credits = json.load(open('assets/sketchfab/CREDITOS.json')) if os.path.exists('assets/sketchfab/CREDITOS.json') else {}
for a in sys.argv[1:]:
    name, uid = a.split('=')
    dst = f'assets/sketchfab/{name}'
    if os.path.isdir(dst) and os.listdir(dst): print('ya', name); continue
    try:
        info = json.loads(get(f'https://api.sketchfab.com/v3/models/{uid}'))
        dl = json.loads(get(f'https://api.sketchfab.com/v3/models/{uid}/download'))
        z = get(dl['gltf']['url'], 600)
        os.makedirs(dst, exist_ok=True); zipfile.ZipFile(io.BytesIO(z)).extractall(dst)
        credits[name] = {'titulo': info['name'], 'autor': info['user']['username'], 'licencia': (info.get('license') or {}).get('label'), 'url': info['viewerUrl']}
        print('OK', name, round(len(z) / 1e6, 1), 'MB')
    except Exception as e: print('ERR', name, e)
os.makedirs('assets/sketchfab', exist_ok=True)
json.dump(credits, open('assets/sketchfab/CREDITOS.json', 'w'), indent=1, ensure_ascii=False)
