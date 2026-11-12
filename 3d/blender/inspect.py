import bpy, sys, glob, os
from mathutils import Vector
for d in sys.argv[sys.argv.index('--') + 1:]:
    bpy.ops.wm.read_factory_settings(use_empty=True)
    f = glob.glob(os.path.join(d, '*.gltf')) + glob.glob(os.path.join(d, '*.glb'))
    bpy.ops.import_scene.gltf(filepath=f[0])
    dg = bpy.context.evaluated_depsgraph_get(); mn = Vector((1e9,) * 3); mx = Vector((-1e9,) * 3); tris = 0; arm = 0
    for o in bpy.context.scene.objects:
        if o.type == 'ARMATURE': arm += 1
        if o.type != 'MESH': continue
        e = o.evaluated_get(dg); tris += len(e.data.loop_triangles) if e.data.loop_triangles else 0
        for c in o.bound_box:
            w = o.matrix_world @ Vector(c); mn = Vector(map(min, mn, w)); mx = Vector(map(max, mx, w))
    s = mx - mn
    print(f'DIM {os.path.basename(d):24} size(x,y,z)=({s.x:.2f},{s.y:.2f},{s.z:.2f}) min=({mn.x:.2f},{mn.y:.2f},{mn.z:.2f}) tris={tris} armatures={arm} imgs={len(bpy.data.images)}')
