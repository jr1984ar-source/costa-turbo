# Reduce polígonos y texturas de un modelo glTF y lo guarda como GLB ligero
import bpy, sys, os
a = sys.argv[sys.argv.index('--') + 1:]
src, dst, ratio, texmax = a[0], a[1], float(a[2]), int(a[3])
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=src)
for ob in [o for o in bpy.context.scene.objects if o.type == 'MESH']:
    m = ob.modifiers.new('dec', 'DECIMATE'); m.ratio = ratio; m.use_collapse_triangulate = True
for im in bpy.data.images:
    if im.size[0] > texmax: im.scale(texmax, int(im.size[1] * texmax / im.size[0]))
bpy.ops.export_scene.gltf(filepath=dst, export_format='GLB', export_apply=True, export_image_format='JPEG', export_jpeg_quality=85)
tris = sum(len(o.evaluated_get(bpy.context.evaluated_depsgraph_get()).data.loop_triangles) for o in bpy.context.scene.objects if o.type == 'MESH')
print('DONE', os.path.basename(dst), 'tris', tris, 'MB', round(os.path.getsize(dst) / 1e6, 1))
