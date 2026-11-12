// Piloto sentado en la moto: cuerpo escaneado (Renderpeople, con esqueleto) recoloreado a neopreno + chaleco de color,
// casco de motocross y chaleco salvavidas. La pose se calcula con IK de dos huesos (cadera -> pies en los reposapiés,
// hombros -> manos en el manillar), así no depende de los ejes de cada hueso.
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const V = (x, y, z) => new THREE.Vector3(x, y, z);
const tmpQ = new THREE.Quaternion(), tmpQ2 = new THREE.Quaternion(), tmpV = new THREE.Vector3();

function wp(o) { return o.getWorldPosition(new THREE.Vector3()); }
// gira el hueso para que la dirección (hijo - hueso) apunte hacia 'to'
function aim(bone, child, to) {
  bone.updateWorldMatrix(true, true);
  const a = wp(bone), cur = wp(child).sub(a).normalize(); to = to.clone().normalize();
  const q = tmpQ.setFromUnitVectors(cur, to);
  const wq = bone.getWorldQuaternion(new THREE.Quaternion()).premultiply(q);
  const pq = bone.parent.getWorldQuaternion(new THREE.Quaternion());
  bone.quaternion.copy(pq.invert().multiply(wq));
  bone.updateWorldMatrix(true, true);
}
// IK de dos huesos: A (hombro/cadera) -> B (codo/rodilla) -> C (mano/tobillo) hacia el objetivo T con 'pole' (hacia donde apunta el codo/rodilla)
function ik2(A, B, C, T, pole) {
  A.updateWorldMatrix(true, true);
  const pa = wp(A), pb = wp(B), pc = wp(C), l1 = pa.distanceTo(pb), l2 = pb.distanceTo(pc);
  const dir = T.clone().sub(pa); let d = dir.length(); dir.normalize();
  d = Math.min(d, l1 + l2 - 1e-4);
  const a = (l1 * l1 - l2 * l2 + d * d) / (2 * d), h = Math.sqrt(Math.max(0, l1 * l1 - a * a));
  const pp = pole.clone().sub(dir.clone().multiplyScalar(pole.dot(dir))).normalize();
  const nb = pa.clone().addScaledVector(dir, a).addScaledVector(pp, h);
  aim(A, B, nb.clone().sub(pa));
  aim(B, C, pa.clone().addScaledVector(dir, d).sub(nb));
}

// recolorea el atlas del cuerpo: camisa blanca/chaleco gris -> color del chaleco; traje negro -> neopreno; piel y pelo igual
function recolor(mat, vestHex) {
  const img = mat.map && mat.map.image; if (!img) return;
  const w = img.width, h = img.height, cv = document.createElement('canvas'); cv.width = w; cv.height = h;
  const cx = cv.getContext('2d'); cx.drawImage(img, 0, 0); const id = cx.getImageData(0, 0, w, h), d = id.data;
  const vc = new THREE.Color(vestHex), vr = vc.r * 255, vg = vc.g * 255, vb = vc.b * 255;
  for (let i = 0; i < d.length; i += 4) {
    const r = d[i], g = d[i + 1], b = d[i + 2], mx = Math.max(r, g, b), mn = Math.min(r, g, b), lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255, sat = mx ? (mx - mn) / mx : 0;
    if (r >= g && g >= b && r - b > 35 && sat > 0.26) continue;                      // piel, pelo, ojos, boca
    if (lum > 0.5 && sat < 0.25) { const k = Math.min(1.15, lum / 0.82); d[i] = vr * k; d[i + 1] = vg * k; d[i + 2] = vb * k; }   // camisa blanca -> color
    else if (lum > 0.28 && sat < 0.16) { const k = lum / 0.5; d[i] = vr * k; d[i + 1] = vg * k; d[i + 2] = vb * k; }          // gris claro -> color
    else { d[i] = r * 0.8; d[i + 1] = g * 0.82; d[i + 2] = b * 0.9; }                // traje oscuro -> neopreno
  }
  cx.putImageData(id, 0, 0);
  const t = new THREE.CanvasTexture(cv); t.flipY = mat.map.flipY; t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; mat.map = t; mat.needsUpdate = true;
}

// chaleco salvavidas: el azul del original pasa al color elegido, las hebillas negras se quedan
function recolorVest(mat, hex) {
  const img = mat.map && mat.map.image; if (!img) { mat.color.set(hex); return; }
  const w = img.width, h = img.height, cv = document.createElement('canvas'); cv.width = w; cv.height = h;
  const cx = cv.getContext('2d'); cx.drawImage(img, 0, 0); const id = cx.getImageData(0, 0, w, h), d = id.data, c = new THREE.Color(hex);
  for (let i = 0; i < d.length; i += 4) { const r = d[i], g = d[i + 1], b = d[i + 2], mx = Math.max(r, g, b), mn = Math.min(r, g, b);
    if (mx - mn > 40 && b >= r && b >= g * 0.9) { const k = Math.min(1.3, mx / 190); d[i] = c.r * 255 * k; d[i + 1] = c.g * 255 * k; d[i + 2] = c.b * 255 * k; } }
  cx.putImageData(id, 0, 0); const t = new THREE.CanvasTexture(cv); t.flipY = mat.map.flipY; t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; mat.map = t; mat.needsUpdate = true;
}

export async function makeRider({ vest = '#ff7a1a', helmetColor = null, base = 'models/' } = {}) {
  const gl = new GLTFLoader();
  const [pg, hg, vg] = await Promise.all([gl.loadAsync(base + 'piloto_eric.glb'), gl.loadAsync(base + 'casco_motocross.glb'), gl.loadAsync(base + 'chaleco.glb')]);
  const root = new THREE.Group(), body = pg.scene; root.add(body);
  const B = {}; body.traverse(o => { if (o.isBone) B[o.name] = o; if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; o.frustumCulled = false; if (o.material.map) recolor(o.material, vest); } });
  const bn = p => { const k = Object.keys(B).find(n => n.startsWith(p)); if (!k) throw new Error('hueso ' + p); return B[k]; };
  root.updateMatrixWorld(true);
  // cadera en el origen
  const hip = bn('hip_'); body.position.sub(wp(hip)); root.updateMatrixWorld(true);
  // torso inclinado hacia delante (~22°)
  const lean = V(0, 0.93, 0.37);
  aim(bn('hip_'), bn('spine_01'), lean.clone().add(V(0, 0, -0.05)));
  aim(bn('spine_01'), bn('spine_02'), lean); aim(bn('spine_02'), bn('spine_03'), lean); aim(bn('spine_03'), bn('neck_'), lean);
  aim(bn('neck_'), bn('head_0'), V(0, 0.95, 0.22));
  // piernas: tobillos en los reposapiés, rodillas hacia delante y fuera
  for (const s of [1, -1]) {
    const side = s > 0 ? '_l' : '_r';
    ik2(bn('upperleg' + side), bn('lowerleg' + side), bn('foot' + side), V(0.30 * s, -0.50, 0.22), V(0.35 * s, 0.25, 1));
    // brazos: manos en el manillar
    ik2(bn('upperarm' + side), bn('lowerarm' + side), bn('hand' + side), V(0.23 * s, 0.13, 0.62), V(0.8 * s, -0.5, -0.1));
  }
  root.updateMatrixWorld(true);
  // casco: sobre la cabeza
  const head = bn('head_0'), hq = head.getWorldQuaternion(new THREE.Quaternion()), hpos = wp(head);
  const helm = hg.scene; helm.traverse(o => { if (o.isMesh) { o.castShadow = true; if (helmetColor) { o.material = o.material.clone(); o.material.color.set(helmetColor); } } });
  const hw = new THREE.Group(); hw.add(helm); helm.position.set(0, -0.12, -0.01); helm.scale.setScalar(1.32);
  hw.position.copy(hpos); hw.quaternion.setFromAxisAngle(V(1, 0, 0), 0.22); root.add(hw);
  // chaleco salvavidas sobre el torso (con el color elegido)
  const ch = vg.scene; ch.traverse(o => { if (o.isMesh) { o.castShadow = true; o.material = o.material.clone(); recolorVest(o.material, vest); } });
  const sp = bn('spine_02'), cw = new THREE.Group(); cw.add(ch); ch.position.set(0, -0.27, -0.01); ch.scale.setScalar(0.9);
  cw.position.copy(wp(sp)); cw.quaternion.setFromAxisAngle(V(1, 0, 0), 0.38); root.add(cw);
  root.userData = { bones: B, helm: hw, vest: cw };
  return root;
}
