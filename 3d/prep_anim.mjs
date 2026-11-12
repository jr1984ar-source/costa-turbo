// Aligera modelos animados sin tocar huesos ni animaciones: solo texturas a webp
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS } from '@gltf-transform/extensions';
import { textureCompress, prune, dedup, getBounds } from '@gltf-transform/functions';
import sharp from 'sharp'; import fs from 'fs';
const [name, out, texMax = '1024'] = process.argv.slice(2);
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS);
const doc = await io.read(`assets/sketchfab/${name}/scene.gltf`);
await doc.transform(dedup(), prune(), textureCompress({ encoder: sharp, targetFormat: 'webp', quality: 82, resize: [+texMax, +texMax] }));
await io.write(`models/${out}.glb`, doc);
const b = getBounds(doc.getRoot().listScenes()[0]);
console.log(out, b.min.map(v => v.toFixed(2)), b.max.map(v => v.toFixed(2)), doc.getRoot().listAnimations().map(a => a.getName()), Math.round(fs.statSync(`models/${out}.glb`).size / 1024), 'KB');
