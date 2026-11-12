// Comprime los modelos de models/ con meshopt (más ligeros para cargar rápido). Guarda copia en /tmp por si acaso.
import { NodeIO } from '@gltf-transform/core';
import { ALL_EXTENSIONS, EXTMeshoptCompression } from '@gltf-transform/extensions';
import { reorder, quantize } from '@gltf-transform/functions';
import { MeshoptEncoder, MeshoptDecoder } from 'meshoptimizer';
import fs from 'fs';
await MeshoptEncoder.ready; await MeshoptDecoder.ready;
const io = new NodeIO().registerExtensions(ALL_EXTENSIONS).registerDependencies({ 'meshopt.encoder': MeshoptEncoder, 'meshopt.decoder': MeshoptDecoder });
for (const f of fs.readdirSync('models').filter(f => f.endsWith('.glb'))) {
  const p = 'models/' + f, before = fs.statSync(p).size; const doc = await io.read(p);
  if (doc.getRoot().listExtensionsUsed().some(e => e.extensionName === 'EXT_meshopt_compression')) { console.log('ya', f); continue; }
  await doc.transform(reorder({ encoder: MeshoptEncoder }), quantize());
  doc.createExtension(EXTMeshoptCompression).setRequired(true).setEncoderOptions({ method: EXTMeshoptCompression.EncoderMethod.QUANTIZE });
  fs.copyFileSync(p, 'C:/Users/JOSERA~2/AppData/Local/Temp/bak_' + f);
  await io.write(p, doc); console.log(f, Math.round(before / 1024), '->', Math.round(fs.statSync(p).size / 1024), 'KB');
}
