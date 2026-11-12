# Yamaha FX Cruiser SVHO (modelo propio, hecho a partir de las fotos de referencia de JRAR).
# Uso: blender -b --python yamaha_fx.py -- salida.glb [render.png]
# Ejes de Blender: X lateral, Y largo (proa hacia -Y para que en glTF la proa mire a +Z), Z arriba. Línea de flotación en Z=0.
import bpy, bmesh, math, sys
from mathutils import Vector

argv = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
OUT = argv[0] if argv else 'yamaha_fx.glb'
PNG = argv[1] if len(argv) > 1 and argv[1] != '-' else None
COLOR = argv[2] if len(argv) > 2 else 'azul'
bpy.ops.wm.read_factory_settings(use_empty=True)

def srgb(h):
    h = h.lstrip('#'); c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    return [((v + 0.055) / 1.055) ** 2.4 if v > 0.04045 else v / 12.92 for v in c]
def mat(name, hexc, rough=0.3, metal=0.0, coat=0.0, emit=None):
    m = bpy.data.materials.new(name); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*srgb(hexc), 1); b.inputs['Roughness'].default_value = rough
    b.inputs['Metallic'].default_value = metal; b.inputs['Clearcoat'].default_value = coat
    if emit: b.inputs['Emission'].default_value = (*srgb(emit), 1); b.inputs['Emission Strength'].default_value = 1.2
    m.diffuse_color = (*srgb(hexc), 1); return m
M_TEAL = mat('azul', '#0a8db3' if COLOR == 'azul' else '#0c0d10', 0.18, 0.0, 1.0)
M_NAVY = mat('azul_oscuro', '#0b4468' if COLOR == 'azul' else '#08090b', 0.30, 0.0, 0.6)
M_BLK = mat('negro_brillo', '#0d0e11', 0.22, 0.0, 0.8)
M_MAT = mat('negro_mate', '#16171a', 0.8)
M_SILV = mat('plata', '#b7bcc4', 0.25, 0.9)
M_GLASS = mat('cristal', '#10151c', 0.05, 0.0, 1.0)
M_SCR = mat('pantalla', '#1b5fae', 0.3, 0.0, 0.0, '#1b5fae')
M_WHITE = mat('blanco', '#e8ecf0', 0.4)

def interp(kn, t):
    if t <= kn[0][0]: return kn[0][1]
    for (t0, v0), (t1, v1) in zip(kn, kn[1:]):
        if t <= t1:
            u = (t - t0) / (t1 - t0); u = u * u * (3 - 2 * u); return v0 + (v1 - v0) * u
    return kn[-1][1]

L = 3.5                      # eslora (m): del popa (t=0) a proa (t=1)
Y0 = -1.55                   # posición hacia delante de la popa
def yb(t): return -(Y0 + L * t)                                  # Y de Blender (proa = -Y)
W = lambda t: interp([(0, .56), (.1, .59), (.35, .61), (.6, .60), (.78, .50), (.92, .28), (.985, .10), (1, .03)], t)       # media manga
ZG = lambda t: interp([(0, .27), (.2, .31), (.5, .35), (.8, .38), (1, .40)], t)                      # borde de cubierta
ZD = lambda t: ZG(t) + interp([(0, .01), (.3, .05), (.6, .07), (.9, .03), (1, .0)], t)                                       # centro de cubierta
ZK = lambda t: interp([(0, -.12), (.4, -.16), (.75, -.10), (.93, .05), (1, .22)], t)                                          # quilla

def obj_from(name, verts, faces, mats, matidx=None, smooth=True):
    me = bpy.data.meshes.new(name); me.from_pydata(verts, [], faces); me.update()
    for m in mats: me.materials.append(m)
    if matidx:
        for p, i in zip(me.polygons, matidx): p.material_index = i
    if smooth:
        for p in me.polygons: p.use_smooth = True
    o = bpy.data.objects.new(name, me); bpy.context.collection.objects.link(o); return o

# ---------- casco: cuadernas de 14 puntos, 60 estaciones ----------
N = 60; ring_n = 14; verts = []; faces = []; midx = []
for i in range(N + 1):
    t = i / N; w = W(t); zk = ZK(t); zg = ZG(t); zd = ZD(t)
    half = [(0, zk), (.42 * w, zk + .05), (.86 * w, zk + .22), (w, zg - .20), (w, zg), (.84 * w, zg + .05), (.45 * w, zd - .01), (0, zd)]
    pts = [(x, z) for x, z in half] + [(-x, z) for x, z in reversed(half[1:-1])]
    for x, z in pts: verts.append((x, yb(t), z))
for i in range(N):
    for k in range(ring_n):
        a = i * ring_n + k; b = i * ring_n + (k + 1) % ring_n
        faces.append((a, b, b + ring_n, a + ring_n)); midx.append(1 if k in (0, 1, 12, 13) else 0)
faces.append(tuple(range(ring_n - 1, -1, -1)) if False else tuple(range(ring_n))); midx.append(0)
faces.append(tuple(range(N * ring_n + ring_n - 1, N * ring_n - 1, -1))); midx.append(0)
hull = obj_from('casco', verts, faces, [M_TEAL, M_NAVY], midx)
sm = hull.modifiers.new('sub', 'SUBSURF'); sm.levels = 1; sm.render_levels = 1

# ---------- capó oscuro con parabrisas ----------
def dome(name, t0, t1, wfun, hfun, mats, n=26, m=14, base=ZD):
    vs = []; fs = []
    for i in range(n + 1):
        t = t0 + (t1 - t0) * i / n; a = wfun((t - t0) / (t1 - t0)); h = hfun((t - t0) / (t1 - t0)); zb = base(t) - .01
        for j in range(m + 1):
            ang = math.pi * j / m; vs.append((a * math.cos(ang), yb(t), zb + h * math.sin(ang) ** 0.8))
    for i in range(n):
        for j in range(m):
            a_ = i * (m + 1) + j; fs.append((a_, a_ + 1, a_ + 1 + m + 1, a_ + m + 1))
    fs.append(tuple(range(m, -1, -1)))
    fs.append(tuple(range(n * (m + 1), n * (m + 1) + m + 1)))
    return obj_from(name, vs, fs, mats)
hood = dome('capo', .64, .99, lambda u: .27 * (1 - u) ** .5 * (1 - .15 * u) + .03, lambda u: (.27 * (1 - u) ** 1.25 + .02 * (1 - u)) * min(1, u * 5 + .25), [M_BLK])
screen = dome('parabrisas', .70, .80, lambda u: .13 * (1 - .45 * u) + .02, lambda u: .12 * math.sin(math.pi * (u * .8 + .1)) + .20, [M_GLASS], base=lambda t: ZD(t) + .08)
# ---------- raíles/defensas negras laterales y de proa ----------
def tube(name, pts, rad=.035, mat_=M_BLK, closed=False, flat=1.0):
    cu = bpy.data.curves.new(name, 'CURVE'); cu.dimensions = '3D'; cu.bevel_depth = rad; cu.bevel_resolution = 3; cu.resolution_u = 12
    sp = cu.splines.new('POLY'); sp.points.add(len(pts) - 1)
    for p, v in zip(sp.points, pts): p.co = (*v, 1)
    sp.use_cyclic_u = closed; o = bpy.data.objects.new(name, cu); o.data.materials.append(mat_); bpy.context.collection.objects.link(o); return o
side = []
for i in range(0, 41):
    t = .02 + .93 * i / 40; side.append((W(t) + .012, yb(t), ZG(t) + .005))
nose = [(.07, yb(1.0) - .01, ZG(1.0) + .0), (0, yb(1.0) - .02, ZG(1.0) + .0), (-.07, yb(1.0) - .01, ZG(1.0) + .0)]
rail = side + [(.16, yb(.985), ZG(.985)), (.07, yb(1.0), ZG(1.0))]
tube('defensa_d', rail, .042); tube('defensa_i', [(-x, y, z) for x, y, z in rail], .042)
tube('proa', [(.16, yb(.985), ZG(.985)), (.07, yb(1.0), ZG(1.0)), (-.07, yb(1.0), ZG(1.0)), (-.16, yb(.985), ZG(.985))], .042)
# listón plateado en la defensa
tube('liston_d', [(W(t) + .03, yb(t), ZG(t) - .045) for t in [x / 20 * .62 + .3 for x in range(21)]], .012, M_SILV)
tube('liston_i', [(-W(t) - .03, yb(t), ZG(t) - .045) for t in [x / 20 * .62 + .3 for x in range(21)]], .012, M_SILV)

# ---------- plataforma trasera negra antideslizante ----------
def slab(name, t0, t1, wf, thick=.012, mat_=M_MAT, dz=.012):
    vs = []; fs = []; n = 14
    for i in range(n + 1):
        t = t0 + (t1 - t0) * i / n; w = wf(t); z = ZD(t) + dz
        vs += [(-w, yb(t), z), (w, yb(t), z), (-w, yb(t), z + thick), (w, yb(t), z + thick)]
    for i in range(n):
        a = i * 4; b = a + 4
        fs += [(a + 2, a + 3, b + 3, b + 2), (a, b, b + 1, a + 1), (a, a + 2, b + 2, b), (a + 1, b + 1, b + 3, a + 3)]
    fs += [(0, 1, 3, 2), (n * 4, n * 4 + 2, n * 4 + 3, n * 4 + 1)]
    return obj_from(name, vs, fs, [mat_], smooth=False)
slab('plataforma', .005, .20, lambda t: W(t) * .88)
slab('alfombra_proa', .62, .88, lambda t: W(t) * .30, .008)

# ---------- asientos (cajas con bisel) ----------
def box(name, cx, cy, cz, sx, sy, sz, mat_=M_BLK, bev=.045, rot=0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(cx, cy, cz)); o = bpy.context.active_object; o.name = name
    o.scale = (sx, sy, sz); o.rotation_euler[0] = rot; bpy.ops.object.transform_apply(scale=True, rotation=True)
    bv = o.modifiers.new('b', 'BEVEL'); bv.width = bev; bv.segments = 4; bv.limit_method = 'NONE'
    o.data.materials.append(mat_)
    for p in o.data.polygons: p.use_smooth = True
    return o
def seat(name, t, ln, top, wd, hh, bev):
    box(name, 0, yb(t), top - hh / 2, wd, ln, hh, bev=bev)
# pedestal del asiento (carrocería del color del casco) para que no floten
base = box('base_asiento', 0, yb(.31), .37, .34, 1.42, .40, M_TEAL, .09)
box('base_asiento_proa', 0, yb(.46), .40, .38, .70, .26, M_TEAL, .08)
seat('asiento_piloto', .43, .58, .56, .30, .22, .07)
seat('asiento_pasajero1', .31, .42, .66, .31, .30, .08)
seat('asiento_pasajero2', .21, .30, .75, .30, .36, .08)
box('respaldo', 0, yb(.155), .84, .30, .09, .26, bev=.05)
# asa de pasajero (arco trasero)
tube('asa', [(.28, yb(.12), ZD(.12) + .02), (.29, yb(.095), ZD(.1) + .30), (.18, yb(.07), ZD(.1) + .38), (-.18, yb(.07), ZD(.1) + .38), (-.29, yb(.095), ZD(.1) + .30), (-.28, yb(.12), ZD(.12) + .02)], .026)

# carenados laterales junto al cuadro (pods angulares) y retrovisores
for s_ in (1, -1):
    box('pod_%d' % s_, s_ * .30, yb(.70), ZD(.70) + .09, .11, .16, .12, M_BLK, .035, 0)
    box('espejo_%d' % s_, s_ * .35, yb(.65), ZD(.65) + .21, .07, .08, .05, M_BLK, .02, 0)

# ---------- altavoces / cajones laterales junto al asiento ----------
for s in (1, -1):
    box('caja_%d' % s, s * .44, yb(.50), ZD(.5) + .07, .13, .26, .14, M_BLK, .04)
    cyl = bpy.ops.mesh.primitive_cylinder_add(radius=.055, depth=.06, location=(s * .50, yb(.62), ZD(.62) + .08), rotation=(0, math.pi / 2, 0)); c = bpy.context.active_object; c.data.materials.append(M_SILV)
    for p in c.data.polygons: p.use_smooth = True

# ---------- manillar, columna y cuadro ----------
bpy.ops.mesh.primitive_cylinder_add(radius=.028, depth=.28, location=(0, yb(.585), ZD(.585) + .18), rotation=(math.radians(-18), 0, 0)); post = bpy.context.active_object; post.data.materials.append(M_BLK)
tube('manillar', [(.34, yb(.555) + 0.0, ZD(.585) + .36), (.27, yb(.56), ZD(.585) + .385), (0, yb(.565), ZD(.585) + .385), (-.27, yb(.56), ZD(.585) + .385), (-.34, yb(.555), ZD(.585) + .36)], .017)
for s in (1, -1):
    tube('puño_%d' % s, [(s * .34, yb(.545), ZD(.585) + .36), (s * .40, yb(.535), ZD(.585) + .335)], .026, M_MAT)
    tube('palanca_%d' % s, [(s * .30, yb(.578), ZD(.585) + .345), (s * .31, yb(.60), ZD(.585) + .31)], .008, M_SILV)
box('cuadro', 0, yb(.60), ZD(.60) + .29, .20, .10, .10, M_BLK, .03, math.radians(-25))
box('pantalla', 0, yb(.576), ZD(.60) + .30, .16, .01, .065, M_SCR, .004, math.radians(-25))
box('tapa_direccion', 0, yb(.54), ZD(.55) + .05, .34, .18, .09, M_BLK, .05)

box('parachoques_popa', 0, yb(-.005), ZD(0) + .02, W(0) * 2 * .96, .08, .07, M_BLK, .03)
bpy.ops.mesh.primitive_cylinder_add(radius=.07, depth=.22, location=(0, yb(-.02) + .08, -.03), rotation=(math.pi / 2, 0, 0)); nz = bpy.context.active_object; nz.data.materials.append(M_SILV)
# ---------- logos: FX en la plataforma, YAMAHA a los lados ----------
def text(name, body, size, loc, rot, mat_, ext=.004):
    cu = bpy.data.curves.new(name, 'FONT'); cu.body = body; cu.size = size; cu.extrude = ext; cu.align_x = 'CENTER'; cu.align_y = 'CENTER'
    o = bpy.data.objects.new(name, cu); o.location = loc; o.rotation_euler = rot; o.data.materials.append(mat_); bpy.context.collection.objects.link(o); return o
text('fx', 'FX', .22, (0, yb(.10), ZD(.10) + .03), (0, 0, math.pi), M_SILV)
text('yamaha_d', 'YAMAHA', .075, (W(.18) + .02, yb(.18), ZG(.18) - .09), (math.pi / 2, 0, math.pi / 2), M_BLK if COLOR == 'azul' else mat('rojo', '#c3162a', .4), .003)
text('yamaha_i', 'YAMAHA', .075, (-W(.18) - .02, yb(.18), ZG(.18) - .09), (math.pi / 2, 0, -math.pi / 2), M_BLK, .003)
text('wr_d', 'WAVERUNNER', .045, (W(.36) + .02, yb(.36), ZG(.36) - .01), (math.pi / 2, 0, math.pi / 2), M_SILV, .002)
text('wr_i', 'WAVERUNNER', .045, (-W(.36) - .02, yb(.36), ZG(.36) - .01), (math.pi / 2, 0, -math.pi / 2), M_SILV, .002)

# ---------- luces y detalles ----------
box('rejilla_toma', 0, yb(.09), ZD(.09) + .01, .18, .22, .04, M_BLK, .015)
tube('argolla', [(0, yb(1.0) - .02, ZG(1.0) - .03), (0, yb(1.0) - .09, ZG(1.0) - .09), (0, yb(1.0) - .02, ZG(1.0) - .15)], .012, M_SILV)

# ---------- exportar ----------
for o in bpy.data.objects:
    if o.type in ('CURVE', 'FONT'):
        bpy.context.view_layer.objects.active = o
bpy.ops.export_scene.gltf(filepath=OUT, export_format='GLB', export_apply=True, export_yup=True, export_materials='EXPORT')
print('GLB', OUT)

if PNG:
    sc = bpy.context.scene; sc.render.engine = 'CYCLES'; sc.cycles.samples = 24; sc.cycles.device = 'CPU'
    sc.render.resolution_x = 900; sc.render.resolution_y = 560; sc.render.filepath = PNG
    w = bpy.data.worlds.new('w'); w.use_nodes = True; w.node_tree.nodes['Background'].inputs[0].default_value = (.35, .38, .42, 1); sc.world = w
    bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 0, -.02)); pl = bpy.context.active_object; pl.data.materials.append(mat('suelo', '#33363b', .9))
    sun = bpy.data.lights.new('s', 'SUN'); sun.energy = 4; so = bpy.data.objects.new('s', sun); so.rotation_euler = (math.radians(50), 0, math.radians(35)); bpy.context.collection.objects.link(so)
    for k, (loc, tgt) in enumerate([((3.6, -3.6, 2.2), (0, 0, .35)), ((-3.2, 4.0, 2.3), (0, 0, .35)), ((0, 0.01, 6.5), (0, 0, .3)), ((9, 0.0, .45), (0, 0, .45)), ((0, -8.0, .8), (0, 0, .55))]):
        cam = bpy.data.cameras.new('c%d' % k); cam.lens = 38
        if k == 3: cam.type = 'ORTHO'; cam.ortho_scale = 4.6
        co = bpy.data.objects.new('c%d' % k, cam); co.location = loc; bpy.context.collection.objects.link(co)
        d = Vector(tgt) - Vector(loc); co.rotation_euler = d.to_track_quat('-Z', 'Y').to_euler(); sc.camera = co
        sc.render.filepath = PNG.replace('.png', '_%d.png' % k); bpy.ops.render.render(write_still=True)
