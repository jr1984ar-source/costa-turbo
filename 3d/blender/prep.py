# Prepara un modelo descargado para el juego: orienta, escala, reduce polígonos y texturas, exporta GLB
# uso: prep.py -- carpeta salida.glb rotZgrados alto_o_largo_m eje(h|l) tris_obj tex_max
import bpy, sys, os, glob, math
from mathutils import Vector, Matrix
a = sys.argv[sys.argv.index('--') + 1:]
src, dst, rotz, size, axis, target, texmax = a[0], a[1], float(a[2]), float(a[3]), a[4], int(a[5]), int(a[6])
for o in list(bpy.data.objects): bpy.data.objects.remove(o, do_unlink=True)
f = (glob.glob(os.path.join(src, '*.gltf')) + glob.glob(os.path.join(src, '*.glb')))[0]
bpy.ops.import_scene.gltf(filepath=f)
meshes = [o for o in bpy.context.scene.objects if o.type == 'MESH']
def bbox():
    mn = Vector((1e9,) * 3); mx = Vector((-1e9,) * 3)
    for o in meshes:
        for c in o.bound_box: w = o.matrix_world @ Vector(c); mn = Vector(map(min, mn, w)); mx = Vector(map(max, mx, w))
    return mn, mx
mn, mx = bbox(); s = mx - mn
dg = bpy.context.evaluated_depsgraph_get()
tris = sum(len(o.evaluated_get(dg).data.loop_triangles) for o in meshes)
print(f'IN size=({s.x:.2f},{s.y:.2f},{s.z:.2f}) tris={tris} arm={sum(o.type=="ARMATURE" for o in bpy.context.scene.objects)}')
if dst == '-': raise SystemExit
# raíz común: rotar en Z, escalar y apoyar en el suelo (z=0) centrado en x,y
root = bpy.data.objects.new('root', None); bpy.context.collection.objects.link(root)
for o in bpy.context.scene.objects:
    if o.parent is None and o is not root: o.parent = root
k = size / (s.z if axis == 'h' else max(s.x, s.y))
root.matrix_world = Matrix.Rotation(math.radians(rotz), 4, 'Z') @ Matrix.Scale(k, 4) @ Matrix.Translation(-Vector(((mn.x + mx.x) / 2, (mn.y + mx.y) / 2, mn.z)))
if target and tris > target:
    r = target / tris
    for o in meshes:
        m = o.modifiers.new('dec', 'DECIMATE'); m.ratio = r
for im in bpy.data.images:
    if im.size[0] > texmax: im.scale(texmax, max(1, int(im.size[1] * texmax / im.size[0])))
bpy.ops.export_scene.gltf(filepath=dst, export_format='GLB', export_apply=True, export_image_format='JPEG', export_jpeg_quality=88, export_yup=True)
mn, mx = bbox(); s = mx - mn
print(f'OUT {os.path.basename(dst)} size=({s.x:.2f},{s.y:.2f},{s.z:.2f}) MB={os.path.getsize(dst)/1e6:.1f}')
