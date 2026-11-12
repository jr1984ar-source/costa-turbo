# Moto de agua + piloto modelados en Blender (bpy) y exportados a GLB para el juego.
# Coordenadas "de juego": x (izq. del piloto +), y arriba, z hacia proa.  Blender: (x, -z, y).
import bpy, bmesh, math, sys, os
from mathutils import Vector
from PIL import Image, ImageDraw, ImageFont

OUT = sys.argv[sys.argv.index('--') + 1] if '--' in sys.argv else '/tmp'
PAINTS = {
    'naranja': dict(paint=(255, 90, 10), accent=(19, 36, 74), hull=(243, 245, 248), text=(255, 255, 255), name='COSTA TURBO', vest=(255, 90, 10)),
    'negra':   dict(paint=(21, 23, 27), accent=(255, 176, 0), hull=(34, 37, 43), text=(255, 176, 0), name='RIVA RACING', vest=(28, 31, 36)),
    'dorada':  dict(paint=(201, 160, 56), accent=(21, 21, 21), hull=(242, 242, 242), text=(21, 21, 21), name='SEA-DOO', vest=(201, 160, 56)),
}
L = 3.4
def B(x, y, z): return Vector((x, -z, y))
def zz(s): return (s - 0.5) * L
def lin(c): return tuple(((v / 255) ** 2.2) for v in c) + (1.0,)

def hb(s):
    if s < 0.55: return 0.62 * (0.92 + 0.08 * math.sin(s / 0.55 * math.pi / 2))
    return 0.62 * max(0.0, 1 - ((s - 0.55) / 0.45) ** 2) ** 0.85
def keel(s): return ((s - 0.6) / 0.4) ** 1.8 * 0.45 if s > 0.6 else 0.0
def gun(s): return 0.50 + 0.12 * s ** 1.6
def deck(s): return gun(s) - 0.02

def hull_half(s):
    w, k, g, d = hb(s), keel(s), gun(s), deck(s)
    c = k + 0.20
    return [(0, d), (0.55 * w, d), (0.80 * w, d + 0.005), (0.86 * w, g + 0.05), (0.97 * w, g + 0.05), (1.0 * w, g - 0.02),
            (1.025 * w, (g + c) / 2), (0.99 * w, c + 0.03), (0.93 * w, c), (0.80 * w, c - 0.015), (0.55 * w, k + 0.11), (0.28 * w, k + 0.05), (0, k)]
CHINE, KEELI, GUNO = 8, 12, 5

def ring_from_half(h):
    return h + [(-x, y) for (x, y) in reversed(h[1:-1])]

def shrink(r, k):
    cx = sum(p[0] for p in r) / len(r); cy = sum(p[1] for p in r) / len(r)
    return [(cx + (x - cx) * k, cy + (y - cy) * k) for (x, y) in r]

def loft(name, rings, zs, crease_idx=(), cap_start=True, cap_end=True, uv=None):
    rings, zs = list(rings), list(zs); n0 = len(rings); off = 0
    if cap_start: rings.insert(0, shrink(rings[0], 0.8)); zs.insert(0, zs[0] - 0.004 * (1 if zs[1] > zs[0] else -1)); off = 1
    if cap_end: rings.append(shrink(rings[-1], 0.8)); zs.append(zs[-1] + 0.004 * (1 if zs[-1] > zs[-2] else -1))
    N = len(rings[0]); verts = []; faces = []
    for r, z in zip(rings, zs):
        for (x, y) in r: verts.append(B(x, y, z))
    S = len(rings)
    for i in range(S - 1):
        for j in range(N):
            a, b2 = i * N + j, i * N + (j + 1) % N
            faces.append((a, a + N, b2 + N, b2))
    ncap = 0
    if cap_start: faces.append(tuple(range(N))); ncap += 1
    if cap_end: faces.append(tuple((S - 1) * N + j for j in range(N - 1, -1, -1))); ncap += 1
    me = bpy.data.meshes.new(name); me.from_pydata([tuple(v) for v in verts], [], faces); me.update()
    for p in me.polygons: p.use_smooth = True
    if crease_idx:
        att = me.attributes.get('crease_edge') or me.attributes.new('crease_edge', 'FLOAT', 'EDGE')
        want = set()
        for i in range(S - 1):
            for j in crease_idx: want.add(frozenset((i * N + j, (i + 1) * N + j)))
        for e in me.edges:
            if frozenset(e.vertices) in want: att.data[e.index].value = 1.0
    if uv:
        lay = me.uv_layers.new(name='UVMap')
        capF = set(range(len(me.polygons) - ncap, len(me.polygons)))
        for p in me.polygons:
            if p.index in capF:
                for li in p.loop_indices: lay.data[li].uv = uv(0, 'cap')
                continue
            idxs = [me.loops[li].vertex_index for li in p.loop_indices]
            wrap = any(v % N == N - 1 for v in idxs) and any(v % N == 0 for v in idxs) and len(idxs) == 4
            for li in p.loop_indices:
                vi = me.loops[li].vertex_index; i, j = divmod(vi, N)
                u, v = uv(min(n0 - 1, max(0, i - off)), j)
                if wrap and j == 0: v = 1.0
                lay.data[li].uv = (u, v)
    ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob)
    return ob

def subsurf(ob, lv=2):
    m = ob.modifiers.new('sub', 'SUBSURF'); m.levels = lv; m.render_levels = lv; return m

def mat(name, color, rough=0.4, metal=0.0, coat=0.0, sheen=0.0, image=None):
    m = bpy.data.materials.new(name)
    try: m.use_nodes = True
    except Exception: pass
    nt = m.node_tree; bs = nt.nodes.get('Principled BSDF')
    bs.inputs['Base Color'].default_value = lin(color) if isinstance(color, tuple) and max(color) > 1 else color
    bs.inputs['Roughness'].default_value = rough; bs.inputs['Metallic'].default_value = metal
    if coat: bs.inputs['Coat Weight'].default_value = coat; bs.inputs['Coat Roughness'].default_value = 0.05
    if sheen: bs.inputs['Sheen Weight'].default_value = sheen
    if image:
        tx = nt.nodes.new('ShaderNodeTexImage'); tx.image = bpy.data.images.load(image)
        nt.links.new(tx.outputs['Color'], bs.inputs['Base Color'])
    return m

def give(ob, m): ob.data.materials.append(m); return ob

def cyl(name, a, b, r, m, verts=16):
    a, b = B(*a), B(*b); d = b - a
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=d.length, location=(a + b) / 2)
    ob = bpy.context.active_object; ob.name = name
    ob.rotation_mode = 'QUATERNION'; ob.rotation_quaternion = Vector((0, 0, 1)).rotation_difference(d.normalized())
    for p in ob.data.polygons: p.use_smooth = True
    return give(ob, m)

def build(paint_key):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    P = PAINTS[paint_key]
    NS = 44; ss = [0.0 + 0.985 * i / NS for i in range(NS + 1)]
    # --- casco
    rings = [ring_from_half(hull_half(s)) for s in ss]
    N = len(rings[0])
    ref = rings[int(NS * 0.35)]
    acc = [0.0]
    for j in range(1, N): acc.append(acc[-1] + math.dist(ref[j], ref[j - 1]))
    tot = acc[-1] + math.dist(ref[-1], ref[0]); vAt = [a / tot for a in acc]
    tex = os.path.join(OUT, f'livery_{paint_key}.png'); livery(tex, P, vAt)
    hull = loft('hull', rings, [zz(s) for s in ss], crease_idx=(CHINE, N - CHINE, KEELI, 3, 4, N - 3, N - 4), uv=lambda i, j: (0.004, vAt[5] + 0.03) if j == 'cap' else (ss[i], vAt[j]))
    subsurf(hull); give(hull, mat('paint', (1, 1, 1, 1), rough=0.28, coat=1.0, image=tex))
    # --- cuerpo superior: pedestal del asiento, consola y capó
    def top(s):
        if s < 0.10: return 0.10 + (s - 0.05) / 0.05 * 0.10
        if s < 0.52: return 0.20
        if s < 0.62: t = (s - 0.52) / 0.10; return 0.20 + 0.30 * (t * t * (3 - 2 * t))
        t = (s - 0.62) / (0.965 - 0.62); return 0.50 - 0.40 * t ** 1.3
    def wu(s): return hb(s) * (0.50 if s < 0.6 else 0.50 + 0.30 * (s - 0.6) / 0.4)
    us = [0.05 + 0.915 * i / 40 for i in range(41)]
    urings = []
    for s in us:
        b, t, w = deck(s) - 0.03, top(s), wu(s)
        h = [(0, b + t + 0.03), (0.6 * w, b + t + 0.02), (0.92 * w, b + t - 0.03), (w, b + t - 0.12), (w, b), (0.0, b)]
        urings.append([h[0], h[1], h[2], h[3], h[4], (-h[4][0], h[4][1]), (-h[3][0], h[3][1]), (-h[2][0], h[2][1]), (-h[1][0], h[1][1])])
    upper = loft('upper', urings, [zz(s) for s in us], crease_idx=(4, 5))
    subsurf(upper)
    mP = mat('body', P['paint'], rough=0.28, coat=1.0); mA = mat('accent', P['accent'], rough=0.3, coat=1.0)
    mDark = mat('glass', (12, 16, 22), rough=0.05, metal=0.3, coat=1.0)
    give(upper, mP); upper.data.materials.append(mA); upper.data.materials.append(mDark)
    # franja central del capó y parabrisas oscuro (por caras)
    for p in upper.data.polygons:
        c = p.center; s = 0.5 - c.y / L; x = abs(c.x); hgt = c.z - (deck(s) - 0.03)
        if 0.52 < s < 0.62 and hgt > 0.28 and x < 0.8 * wu(s): p.material_index = 2
        elif s > 0.62 and x < 0.09 and hgt > top(s) - 0.05: p.material_index = 1
    # --- asiento
    srings, sz = [], []
    for i in range(17):
        s = 0.11 + 0.41 * i / 16; t = i / 16
        w = 0.24 + 0.03 * math.sin(t * math.pi); hgt = 0.11 * (0.85 + 0.15 * math.sin(t * math.pi))
        if t > 0.85: hgt *= 1.0 + (t - 0.85) * 1.2
        b = deck(s) - 0.03 + 0.17
        srings.append([(0, b + hgt), (0.55 * w, b + hgt - 0.01), (0.9 * w, b + hgt - 0.05), (w, b + 0.02), (-w, b + 0.02), (-0.9 * w, b + hgt - 0.05), (-0.55 * w, b + hgt - 0.01)])
        sz.append(zz(s))
    seat = loft('seat', srings, sz); subsurf(seat)
    give(seat, mat('seat', (14, 15, 18), rough=0.6, sheen=0.15))
    # --- defensa de goma en la borda
    pts = [B(hull_half(s)[GUNO][0] + 0.012, hull_half(s)[GUNO][1] + 0.01, zz(s)) for s in ss[1:]]
    pts = pts + [B(-p.x, p.z, -p.y) if False else Vector((-p.x, p.y, p.z)) for p in reversed(pts)]
    cu = bpy.data.curves.new('rail', 'CURVE'); cu.dimensions = '3D'; cu.bevel_depth = 0.022; cu.bevel_resolution = 3
    sp = cu.splines.new('POLY'); sp.points.add(len(pts) - 1)
    for i, p in enumerate(pts): sp.points[i].co = (p.x, p.y, p.z, 1)
    rail = bpy.data.objects.new('rail', cu); bpy.context.collection.objects.link(rail)
    rail.data.materials.append(mat('rubber', (30, 32, 36), rough=0.7))
    # --- manillar, puños, retrovisores, pantalla
    black = mat('black', (20, 21, 24), rough=0.5); metal = mat('metal', (170, 176, 184), rough=0.22, metal=1.0)
    sB = 0.585; by = deck(sB) - 0.03 + top(sB) + 0.12; bz = zz(sB) - 0.02
    cyl('column', (0, by - 0.14, bz + 0.03), (0, by, bz), 0.045, black)
    cyl('bar', (-0.31, by + 0.02, bz), (0.31, by + 0.02, bz), 0.016, metal)
    for sx in (-1, 1):
        cyl('grip', (sx * 0.29, by + 0.02, bz), (sx * 0.43, by + 0.02, bz), 0.029, black)
        sm = 0.68; my = deck(sm) - 0.03 + top(sm); mx = wu(sm) * 0.78
        cyl('stalk', (sx * mx, my - 0.02, zz(sm)), (sx * (mx + 0.12), my + 0.12, zz(sm) - 0.03), 0.011, black)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.07, location=B(sx * (mx + 0.15), my + 0.13, zz(sm) - 0.03), segments=20, ring_count=12)
        mir = bpy.context.active_object; mir.scale = (1.35, 0.45, 0.7); give(mir, black)
        for p in mir.data.polygons: p.use_smooth = True
    # --- popa: tobera, placa, agarre
    cyl('nozzle', (0, 0.14, zz(0) + 0.02), (0, 0.13, zz(0) - 0.24), 0.085, metal, 20)
    bpy.ops.mesh.primitive_torus_add(major_radius=0.13, minor_radius=0.02, location=B(0, gun(0.06) + 0.18, zz(0.06)))
    grab = bpy.context.active_object; grab.rotation_euler = (math.pi / 2, 0, 0); give(grab, black)
    for sx in (-1, 1):
        bpy.ops.mesh.primitive_cube_add(size=1, location=B(sx * (hb(0.06) + 0.025), keel(0.06) + 0.24, zz(0.06)))
        f = bpy.context.active_object; f.scale = (0.03, 0.40, 0.08); give(f, black)
    rider(P, by, bz)
    return tex

def rider(P, by, bz):
    D = deck(0.35)
    J = dict(pel=(0, D + 0.66, -0.34), spi=(0, D + 0.86, -0.26), che=(0, D + 1.04, -0.14), nec=(0, D + 1.17, -0.06), hea=(0, D + 1.30, 0.0),
             hipL=(0.12, D + 0.63, -0.33), kneL=(0.30, D + 0.48, 0.10), ankL=(0.35, D + 0.09, -0.18), toeL=(0.36, D + 0.04, 0.02),
             shoL=(0.21, D + 1.10, -0.10), elbL=(0.45, D + 0.87, -0.04), wriL=(0.39, by - 0.02, bz - 0.02), hanL=(0.37, by + 0.01, bz + 0.03))
    mid = lambda a, b, t=0.5: tuple(a[i] + (b[i] - a[i]) * t for i in range(3))
    J['thiL'] = mid(J['hipL'], J['kneL'], 0.45); J['calL'] = mid(J['kneL'], J['ankL'], 0.35)
    J['armL'] = mid(J['shoL'], J['elbL'], 0.45); J['foreL'] = mid(J['elbL'], J['wriL'], 0.35)
    for k in list(J):
        if k.endswith('L'): x, y, z = J[k]; J[k[:-1] + 'R'] = (-x, y, z)
    R = dict(pel=(0.20, 0.16), spi=(0.18, 0.14), che=(0.23, 0.16), nec=(0.075, 0.075), hea=(0.11, 0.12),
             hip=(0.13, 0.13), thi=(0.125, 0.125), kne=(0.085, 0.085), cal=(0.085, 0.085), ank=(0.06, 0.06), toe=(0.055, 0.05),
             sho=(0.09, 0.09), arm=(0.08, 0.08), elb=(0.065, 0.065), fore=(0.065, 0.065), wri=(0.05, 0.05), han=(0.055, 0.05))
    names = list(J); idx = {n: i for i, n in enumerate(names)}
    E = [('pel', 'spi'), ('spi', 'che'), ('che', 'nec'), ('nec', 'hea')]
    for s in 'LR':
        E += [('pel', 'hip' + s), ('hip' + s, 'thi' + s), ('thi' + s, 'kne' + s), ('kne' + s, 'cal' + s), ('cal' + s, 'ank' + s), ('ank' + s, 'toe' + s),
              ('che', 'sho' + s), ('sho' + s, 'arm' + s), ('arm' + s, 'elb' + s), ('elb' + s, 'fore' + s), ('fore' + s, 'wri' + s), ('wri' + s, 'han' + s)]
    me = bpy.data.meshes.new('rider'); me.from_pydata([tuple(B(*J[n])) for n in names], [(idx[a], idx[b]) for a, b in E], []); me.update()
    ob = bpy.data.objects.new('rider_body', me); bpy.context.collection.objects.link(ob)
    sk = ob.modifiers.new('skin', 'SKIN'); sk.use_smooth_shade = True
    for n in names:
        key = n[:-1] if n[-1] in 'LR' and n[:-1] in R else n
        r = tuple(v * 1.5 for v in R[key]); sv = me.skin_vertices[0].data[idx[n]]; sv.radius = r
        if n == 'pel': sv.use_root = True
    subsurf(ob, 2)
    give(ob, mat('neoprene', (20, 22, 26), rough=0.6, sheen=0.3))
    # chaleco
    vr, vz = [], []
    for i in range(9):
        t = i / 8; y = D + 0.72 + t * 0.40; z = -0.30 + t * 0.20
        rx, rz = 0.205 - 0.02 * abs(t - 0.5), 0.15
        vr.append([(math.cos(a) * rx, y) if False else None for a in []] or [(0, 0)])
        vz.append(z)
    # chaleco como anillos horizontales (eje vertical): se construye a mano
    verts, faces = [], []
    K = 20
    for i in range(9):
        t = i / 8; y = D + 0.70 + t * 0.42; zc = -0.31 + t * 0.21; rx = 0.27 - 0.03 * (t - 0.5) ** 2 * 4; rz = 0.21
        for k in range(K):
            a = k / K * 2 * math.pi; verts.append(tuple(B(math.cos(a) * rx, y, zc + math.sin(a) * rz)))
    for i in range(8):
        for k in range(K): a = i * K + k; b2 = i * K + (k + 1) % K; faces.append((a, b2, b2 + K, a + K))
    vme = bpy.data.meshes.new('vest'); vme.from_pydata(verts, [], faces); vme.update()
    for p in vme.polygons: p.use_smooth = True
    vest = bpy.data.objects.new('rider_vest', vme); bpy.context.collection.objects.link(vest)
    sol = vest.modifiers.new('sol', 'SOLIDIFY'); sol.thickness = 0.02; subsurf(vest, 2)
    give(vest, mat('vest', P['vest'], rough=0.55, sheen=0.2)); vest.data.materials.append(mat('vestdark', (28, 30, 34), rough=0.6))
    for p in vme.polygons:
        if abs(p.center.x) > 0.22: p.material_index = 1
    # casco integral con visera
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.15, location=B(*J['hea']), segments=40, ring_count=24)
    hel = bpy.context.active_object; hel.name = 'rider_helmet'; hel.scale = (1.0, 1.12, 1.02)
    for p in hel.data.polygons: p.use_smooth = True
    give(hel, mat('helmet', (244, 244, 244), rough=0.25, coat=1.0))
    hel.data.materials.append(mat('helmetpaint', P['paint'], rough=0.25, coat=1.0)); hel.data.materials.append(mat('visor', (10, 14, 20), rough=0.04, metal=0.6, coat=1.0))
    for p in hel.data.polygons:
        n = p.normal  # Blender: -y = adelante
        if -n.y > 0.42 and -0.30 < n.z < 0.38: p.material_index = 2
        elif abs(n.x) < 0.18 and n.z > -0.2: p.material_index = 1
    # botas y guantes
    black = bpy.data.materials.get('black')
    for s in 'LR':
        a = J['ank' + s]; t = J['toe' + s]
        bpy.ops.mesh.primitive_cube_add(size=1, location=B((a[0] + t[0]) / 2, D + 0.05, (a[2] + t[2]) / 2 + 0.03))
        bo = bpy.context.active_object; bo.name = 'rider_boot'; bo.scale = (0.11, 0.30, 0.10); sb = bo.modifiers.new('b', 'BEVEL'); sb.width = 0.03; sb.segments = 3; give(bo, black)
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.065, location=B(*J['han' + s]), segments=16, ring_count=10)
        gl = bpy.context.active_object; gl.name = 'rider_glove'; gl.scale = (0.8, 1.2, 0.9); give(gl, black)
        for p in gl.data.polygons: p.use_smooth = True

def livery(path, P, vAt):
    W, H = 4096, 2048
    im = Image.new('RGB', (W, H), P['hull']); g = ImageDraw.Draw(im)
    Y = lambda v: (1 - v) * H                     # imagen: v=0 abajo
    def band(v0, v1, col):
        for (a, b) in ((v0, v1), (1 - v1, 1 - v0)):
            g.rectangle([0, min(Y(a), Y(b)), W, max(Y(a), Y(b))], fill=col)
    band(0, vAt[3], (45, 47, 52))                 # cubierta (zona de pies) antideslizante
    band(vAt[3], vAt[7] - 0.004, P['paint'])      # borda y costado
    band(vAt[5] + 0.006, vAt[5] + 0.016, P['accent'])
    # flecha baja desde proa
    for side in (0, 1):
        f = (lambda v: Y(v)) if side == 0 else (lambda v: Y(1 - v))
        y0, y1 = f(vAt[7] + 0.002), f(vAt[8] + 0.012)
        g.polygon([(W * 0.99, y0), (W * 0.40, y0), (W * 0.26, (y0 + y1) / 2), (W * 0.55, y1), (W * 0.99, y1)], fill=P['accent'])
        y2 = f(vAt[7] + 0.008)
        g.polygon([(W * 0.99, y2), (W * 0.47, y2), (W * 0.40, (y2 + y1) / 2 + 2), (W * 0.99, y1 - (y1 - y2) * 0.35)], fill=P['paint'])
    bh = int((vAt[7] - vAt[5] - 0.02) * H)
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBoldOblique.ttf', int(bh * 0.95))
    for side in (0, 1):
        vm = (vAt[5] + 0.018 + vAt[7]) / 2
        t0 = Image.new('RGBA', (int(W * 0.42 / 1.5), bh), (0, 0, 0, 0)); tg = ImageDraw.Draw(t0)
        tg.text((t0.width / 2, bh / 2), P['name'], font=font, fill=P['text'] + (255,), anchor='mm', stroke_width=max(3, bh // 18), stroke_fill=P['accent'] + (255,))
        t0 = t0.resize((int(t0.width * 1.5), bh), Image.LANCZOS)
        txt = Image.new('RGBA', (W, bh), (0, 0, 0, 0)); txt.paste(t0, (int(W * 0.47 - t0.width / 2), 0), t0)
        if side == 0: txt = txt.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)
        y = Y(vm) if side == 0 else Y(1 - vm)
        im.paste(txt, (0, int(y - txt.height / 2)), txt)
    im.save(path)

if __name__ == '__main__':
    for k in (sys.argv[sys.argv.index('--') + 2:] if '--' in sys.argv and len(sys.argv) > sys.argv.index('--') + 2 else PAINTS):
        build(k)
        bpy.ops.export_scene.gltf(filepath=os.path.join(OUT, f'jetski_{k}.glb'), export_format='GLB', export_apply=True, export_yup=True)
        print('OK', k)
