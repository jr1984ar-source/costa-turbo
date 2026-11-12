// Aligera y escala modelos descargados -> models/<nombre>.glb
// uso: node prep.mjs nombre modo medida [texMax] [ratio]   (modo: largo | alto)
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import { dedup, prune, flatten, join, weld, simplify, textureCompress, getBounds, resample } from '@gltf-transform/functions';
import { MeshoptSimplifier } from 'meshoptimizer';
import sharp from 'sharp';
import fs from 'fs';

const [name, mode = 'largo', size = '3.3', texMax = '1024', ratio = '0.3'] = process.argv.slice(2);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS);
const doc = await io.read(process.env.SRC || `assets/sketchfab/${name}/scene.gltf`);
await MeshoptSimplifier.ready;
if (process.env.UNSKIN) { // modelos con esqueleto: se quita el skin y se anula la rotacion del Armature
  for (const n of doc.getRoot().listNodes()) { if (n.getSkin()) n.setSkin(null); if (n.getName() === 'Armature') n.setRotation([0, 0, 0, 1]); }
  for (const sk of doc.getRoot().listSkins()) sk.dispose();
  for (const m of doc.getRoot().listMeshes()) for (const p of m.listPrimitives()) for (const a of ['JOINTS_0', 'WEIGHTS_0']) { const acc = p.getAttribute(a); if (acc) { p.setAttribute(a, null); } }
}
await doc.transform(
  flatten(), dedup(), prune(),
  weld(),
  simplify({ simplifier: MeshoptSimplifier, ratio: +ratio, error: 0.002 }),
  textureCompress({ encoder: sharp, targetFormat: 'webp', quality: 82, resize: [+texMax, +texMax] }),
  prune(),
);
const scene = doc.getRoot().getDefaultScene() || doc.getRoot().listScenes()[0];
const b = getBounds(scene);
const dx = b.max[0] - b.min[0], dy = b.max[1] - b.min[1], dz = b.max[2] - b.min[2];
const ref = mode === 'alto' ? dy : Math.max(dx, dz);
const s = +size / ref;
const cx = (b.min[0] + b.max[0]) / 2, cz = (b.min[2] + b.max[2]) / 2;
// nodo envoltorio: escala + centrado en suelo
const wrap = doc.createNode('norm').setScale([s, s, s]).setTranslation([-cx * s, -b.min[1] * s, -cz * s]);
for (const n of scene.listChildren()) { scene.removeChild(n); wrap.addChild(n); }
scene.addChild(wrap);
fs.mkdirSync('models', { recursive: true });
await io.write(`models/${name}.glb`, doc);
let tris = 0;
for (const m of doc.getRoot().listMeshes()) for (const p of m.listPrimitives()) tris += (p.getIndices()?.getCount() ?? p.getAttribute('POSITION').getCount()) / 3;
console.log(name, 'dims', dx.toFixed(2), dy.toFixed(2), dz.toFixed(2), '-> escala', s.toFixed(4), 'tris', Math.round(tris), 'KB', Math.round(fs.statSync(`models/${name}.glb`).size / 1024));
