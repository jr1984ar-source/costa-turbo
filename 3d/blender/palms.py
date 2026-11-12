# Palmeras realistas: Phoenix canariensis y Washingtonia robusta (texturas pintadas con PIL, hojas con transparencia)
import bpy, bmesh, math, random, sys, os
from mathutils import Vector, Matrix
from PIL import Image, ImageDraw, ImageFilter
OUT = sys.argv[sys.argv.index('--') + 1]
TEX = os.path.join(OUT, 'palmtex'); os.makedirs(TEX, exist_ok=True)

# ---------- texturas ----------
def frond_texture(path, seed, dead=False):
    R = random.Random(seed); W, H = 256, 2048
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); g = ImageDraw.Draw(im)
    cx = W // 2
    for y in range(40, H - 20, 9):
        t = y / H
        L = (W * 0.48) * (0.35 + 0.65 * math.sin(math.pi * min(1, (1 - t) * 1.15 + 0.05)))
        for s in (-1, 1):
            ang = math.radians(28 + R.uniform(-6, 6))
            x2 = cx + s * L * math.cos(ang) * 0.98; y2 = y - L * math.sin(ang) * 0.35
            if dead: col = (R.randint(120, 150), R.randint(90, 110), R.randint(55, 70), 255)
            else:
                k = R.uniform(0.85, 1.12); col = (int(58 * k), int(92 * k), int(34 * k), 255)
            g.line([(cx, y), (x2, y2)], fill=col, width=5)
            g.line([(cx, y + 1), (x2, y2 + 2)], fill=tuple(int(c * 0.8) for c in col[:3]) + (255,), width=2)
    g.line([(cx, 0), (cx, H)], fill=(150, 140, 80, 255) if not dead else (140, 110, 70, 255), width=7)
    im.save(path)

def fan_texture(path, seed, dead=False):
    R = random.Random(seed); S = 1024
    im = Image.new('RGBA', (S, S), (0, 0, 0, 0)); g = ImageDraw.Draw(im)
    c = (S // 2, int(S * 0.92)); N = 56
    for i in range(N):
        a0 = math.radians(-120 + 240 * i / N); a1 = math.radians(-120 + 240 * (i + 1) / N)
        r = S * 0.86 * R.uniform(0.9, 1.0); rs = r * R.uniform(0.62, 0.78)
        k = R.uniform(0.85, 1.1)
        col = (int(140 * k), int(112 * k), int(70 * k), 255) if dead else (int(70 * k), int(118 * k), int(44 * k), 255)
        pts = [c, (c[0] + math.sin(a0) * rs, c[1] - math.cos(a0) * rs), (c[0] + math.sin((a0 + a1) / 2) * r, c[1] - math.cos((a0 + a1) / 2) * r), (c[0] + math.sin(a1) * rs, c[1] - math.cos(a1) * rs)]
        g.polygon(pts, fill=col)
        g.line([c, pts[2]], fill=tuple(int(v * 0.75) for v in col[:3]) + (255,), width=2)
        if not dead and R.random() < 0.6:  # hilos en las puntas
            g.line([pts[2], (pts[2][0] + math.sin((a0 + a1) / 2) * 30, pts[2][1] - math.cos((a0 + a1) / 2) * 30 + 25)], fill=(190, 180, 150, 255), width=1)
    im = im.filter(ImageFilter.SMOOTH)
    im.save(path)

def bark_texture(path, kind):
    W, H = 512, 1024; im = Image.new('RGB', (W, H)); g = ImageDraw.Draw(im); R = random.Random(3)
    if kind == 'phoenix':   # rombos de las bases de las hojas
        g.rectangle([0, 0, W, H], fill=(96, 84, 68))
        for row in range(0, 26):
            for col in range(0, 9):
                x = col * 64 + (32 if row % 2 else 0); y = row * 42
                k = R.uniform(0.8, 1.2)
                g.polygon([(x, y - 22), (x + 30, y), (x, y + 22), (x - 30, y)], fill=(int(130 * k), int(112 * k), int(88 * k)), outline=(60, 50, 40))
                g.line([(x - 18, y), (x + 18, y)], fill=(70, 58, 45), width=3)
    else:                   # anillos finos y fibras
        g.rectangle([0, 0, W, H], fill=(118, 108, 96))
        for y in range(0, H, 6):
            k = R.uniform(0.75, 1.15); g.line([(0, y), (W, y + R.randint(-2, 2))], fill=(int(100 * k), int(92 * k), int(82 * k)), width=2)
        for i in range(400):
            x = R.randint(0, W); y = R.randint(0, H); g.line([(x, y), (x + R.randint(-3, 3), y + R.randint(6, 18))], fill=(84, 76, 66), width=1)
    im.save(path)

def mat(name, tex, alpha=False, rough=0.75):
    m = bpy.data.materials.new(name)
    try: m.use_nodes = True
    except Exception: pass
    nt = m.node_tree; bs = nt.nodes.get('Principled BSDF'); bs.inputs['Roughness'].default_value = rough
    tx = nt.nodes.new('ShaderNodeTexImage'); tx.image = bpy.data.images.load(tex)
    nt.links.new(tx.outputs['Color'], bs.inputs['Base Color'])
    if alpha:
        nt.links.new(tx.outputs['Alpha'], bs.inputs['Alpha'])
        try: m.surface_render_method = 'DITHERED'
        except Exception: pass
        m.blend_method = 'CLIP' if hasattr(m, 'blend_method') else None
    return m

# ---------- geometría ----------
def add_mesh(name, verts, faces, uvs, m):
    me = bpy.data.meshes.new(name); me.from_pydata(verts, [], faces); me.update()
    lay = me.uv_layers.new(name='UVMap')
    for p in me.polygons:
        p.use_smooth = True
        for li in p.loop_indices: lay.data[li].uv = uvs[me.loops[li].vertex_index]
    ob = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(ob); ob.data.materials.append(m); return ob

def trunk(name, pts, r0, r1, m, bulge=None, seg=14):
    verts, faces, uvs = [], [], []; n = len(pts)
    for i, p in enumerate(pts):
        t = i / (n - 1); r = r0 + (r1 - r0) * t
        if bulge: r *= bulge(t)
        d = (pts[min(n - 1, i + 1)] - pts[max(0, i - 1)]).normalized()
        a = d.orthogonal().normalized(); b = d.cross(a).normalized()
        for j in range(seg + 1):
            ang = 2 * math.pi * j / seg
            verts.append(tuple(p + (a * math.cos(ang) + b * math.sin(ang)) * r)); uvs.append((j / seg * 2, t * (pts[-1] - pts[0]).length / 2.0))
    for i in range(n - 1):
        for j in range(seg):
            a0 = i * (seg + 1) + j; faces.append((a0, a0 + 1, a0 + seg + 2, a0 + seg + 1))
    return add_mesh(name, verts, faces, uvs, m)

def frond(verts, faces, uvs, base, dirv, length, droop, width, fold, R):
    # cinta en V a lo largo del raquis, curvada hacia abajo
    up = Vector((0, 0, 1)); side = dirv.cross(up).normalized(); N = 14; st = len(verts)
    for k in range(N + 1):
        t = k / N
        p = base + dirv * (length * t) + up * (length * 0.35 * t - droop * length * t * t)
        w = width * (0.25 + 0.75 * math.sin(math.pi * min(1, t * 1.1 + 0.05)))
        ftw = up * (w * fold)
        verts += [tuple(p + side * w + ftw), tuple(p), tuple(p - side * w + ftw)]
        uvs += [(0.0, t), (0.5, t), (1.0, t)]
    for k in range(N):
        a = st + k * 3; b = a + 3
        faces += [(a, b, b + 1, a + 1), (a + 1, b + 1, b + 2, a + 2)]

def fan(verts, faces, uvs, base, dirv, R, dead=False, size=1.25, elev=0.3, pet=None):
    # abanico plegado al final de un peciolo; dirv = dirección horizontal hacia fuera
    up = Vector((0, 0, 1)); d = Vector((dirv.x, dirv.y, 0)).normalized(); side = d.cross(up).normalized()
    if dead:
        fwd = (d * 0.15 - up).normalized(); tip = base + d * 0.25
    else:
        fwd = (d * math.cos(elev) + up * math.sin(elev)).normalized(); tip = base + fwd * (pet or 1.2)
        if pet_list is not None: pet_list.append((base, tip))
    nrm = fwd.cross(side).normalized()
    st = len(verts); M = 18
    verts.append(tuple(tip)); uvs.append((0.5, 0.08))
    for k in range(M + 1):
        a = math.radians(-110 + 220 * k / M); pl = 0.07 * size * (1 if k % 2 else -1)
        for rr, vv in ((0.5, 0.5), (1.0, 1.0)):
            dd = side * math.sin(a) + fwd * math.cos(a)
            p = tip + dd * size * rr + nrm * pl * rr - up * (0.0 if dead else 0.35 * size * rr * rr * (0.6 + 0.4 * abs(math.sin(a))))
            verts.append(tuple(p)); uvs.append((0.5 + math.sin(a) * 0.43 * vv, 0.08 + math.cos(a) * 0.84 * vv))
    for k in range(M):
        i0 = st + 1 + k * 2; i1 = i0 + 2
        faces += [(st, i0, i1), (i0, i0 + 1, i1 + 1, i1)]
    return tip

pet_list = None

def build_phoenix(seed):
    R = random.Random(seed); H = R.uniform(6.0, 9.0); lean = R.uniform(0, 0.4)
    pts = [Vector((math.sin(seed) * lean * (i / 12) ** 2, math.cos(seed) * lean * (i / 12) ** 2, H * i / 12)) for i in range(13)]
    tr = trunk('phoenix_trunk', pts, 0.48, 0.42, mT_ph, bulge=lambda t: 1.0 + 0.35 * max(0, t - 0.85) / 0.15)
    top = pts[-1] + Vector((0, 0, 0.3))
    v, f, uv = [], [], []
    NF = 95
    for i in range(NF):
        a = i * 2.39996 + R.uniform(-0.1, 0.1); tier = (i % 7) / 7
        elev = 0.95 - tier * 1.25 + R.uniform(-0.1, 0.1)
        d = Vector((math.cos(a) * math.cos(elev), math.sin(a) * math.cos(elev), math.sin(elev))).normalized()
        frond(v, f, uv, top + d * 0.25, d, R.uniform(4.0, 5.2), R.uniform(0.3, 0.55), R.uniform(0.55, 0.7), 0.35, R)
    add_mesh('phoenix_fronds', v, f, uv, mF_ph)
    # piña de bases de hojas
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.75, location=tuple(pts[-1] + Vector((0, 0, 0.1))), segments=18, ring_count=10)
    p = bpy.context.active_object; p.name = 'phoenix_crown'; p.scale = (1, 1, 0.8); p.data.materials.append(mT_ph)

def build_washingtonia(seed):
    R = random.Random(seed); H = R.uniform(11, 17); lean = R.uniform(0.2, 1.2)
    pts = [Vector((math.sin(seed) * lean * (i / 16) ** 2, math.cos(seed) * lean * (i / 16) ** 2, H * i / 16)) for i in range(17)]
    trunk('wash_trunk', pts, 0.36, 0.22, mT_wa, bulge=lambda t: 1.25 if t < 0.04 else 1.0)
    top = pts[-1]
    global pet_list
    v, f, uv = [], [], []; pet_list = []
    for i in range(28):
        a = i * 2.39996; d = Vector((math.cos(a), math.sin(a), 0))
        fan(v, f, uv, top + d * 0.12, d, R, size=R.uniform(1.1, 1.45), elev=R.uniform(-0.35, 1.15), pet=R.uniform(1.0, 1.5))
    add_mesh('wash_leaves', v, f, uv, mF_wa)
    pv, pf, pu = [], [], []
    for (a, b) in pet_list:
        dd = (b - a); sd = dd.cross(Vector((0, 0, 1))).normalized() * 0.03; st = len(pv)
        pv += [tuple(a - sd), tuple(a + sd), tuple(b + sd * 0.5), tuple(b - sd * 0.5), tuple(a + Vector((0, 0, 0.03))), tuple(b + Vector((0, 0, 0.02)))]
        pu += [(0, 0), (1, 0), (1, 1), (0, 1), (0.5, 0), (0.5, 1)]; pf += [(st, st + 1, st + 2, st + 3), (st, st + 4, st + 5, st + 3)]
    add_mesh('wash_petioles', pv, pf, pu, mT_wa); pet_list = None
    # falda de hojas secas colgando
    v, f, uv = [], [], []
    for i in range(30):
        a = i * 2.39996 + R.uniform(-0.2, 0.2); d = Vector((math.cos(a), math.sin(a), 0))
        fan(v, f, uv, top + d * 0.22 - Vector((0, 0, 0.3 + R.uniform(0, 1.6))), d, R, dead=True, size=R.uniform(0.9, 1.25))
    add_mesh('wash_skirt', v, f, uv, mD_wa)

for k in ('phoenix', 'wash'): bark_texture(f'{TEX}/{k}_bark.png', 'phoenix' if k == 'phoenix' else 'wash')
frond_texture(f'{TEX}/phoenix_frond.png', 1); fan_texture(f'{TEX}/wash_fan.png', 2); fan_texture(f'{TEX}/wash_dead.png', 3, dead=True)
for kind, n in (('phoenix', 3), ('washingtonia', 3)):
    for s in range(n):
        bpy.ops.wm.read_factory_settings(use_empty=True)
        mT_ph = mat('bark', f'{TEX}/phoenix_bark.png', rough=0.9); mF_ph = mat('frond', f'{TEX}/phoenix_frond.png', alpha=True)
        mT_wa = mat('bark', f'{TEX}/wash_bark.png', rough=0.9); mF_wa = mat('fan', f'{TEX}/wash_fan.png', alpha=True); mD_wa = mat('dead', f'{TEX}/wash_dead.png', alpha=True, rough=0.9)
        (build_phoenix if kind == 'phoenix' else build_washingtonia)(s * 7 + 3)
        bpy.ops.export_scene.gltf(filepath=os.path.join(OUT, f'{kind}_{s}.glb'), export_format='GLB', export_yup=True, export_image_format='JPEG' if False else 'AUTO')
        print('OK', kind, s)
