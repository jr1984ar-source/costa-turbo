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
function recolor(mat, vestHex, suitHex) {
  const img = mat.map && mat.map.image; if (!img) return;
  const w = img.width, h = img.height, cv = document.createElement('canvas'); cv.width = w; cv.height = h;
  const cx = cv.getContext('2d'); cx.drawImage(img, 0, 0); const id = cx.getImageData(0, 0, w, h), d = id.data;
  const vc = new THREE.Color(vestHex), vr = vc.r * 255, vg = vc.g * 255, vb = vc.b * 255, sc = suitHex ? new THREE.Color(suitHex) : null;
  for (let i = 0; i < d.length; i += 4) {
    const r = d[i], g = d[i + 1], b = d[i + 2], mx = Math.max(r, g, b), mn = Math.min(r, g, b), lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255, sat = mx ? (mx - mn) / mx : 0;
    if (r >= g && g >= b && r - b > 35 && sat > 0.26) continue;                      // piel, pelo, ojos, boca
    if (lum > 0.5 && sat < 0.25) { const k = Math.min(1.15, lum / 0.82); d[i] = vr * k; d[i + 1] = vg * k; d[i + 2] = vb * k; }   // camisa blanca -> color
    else if (lum > 0.28 && sat < 0.16) { const k = lum / 0.5; d[i] = vr * k; d[i + 1] = vg * k; d[i + 2] = vb * k; }          // gris claro -> color
    else if (sc) { const k = Math.min(1.4, 0.35 + lum * 2.2); d[i] = sc.r * 255 * k; d[i + 1] = sc.g * 255 * k; d[i + 2] = sc.b * 255 * k; }   // neopreno del color elegido
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

export async function makeRider({ vest = '#ff7a1a', helmetColor = null, suit = null, base = 'models/' } = {}) {
  const gl = new GLTFLoader();
  const [pg, hg, vg] = await Promise.all([gl.loadAsync(base + 'piloto_eric.glb'), gl.loadAsync(base + 'casco_motocross.glb'), gl.loadAsync(base + 'chaleco.glb')]);
  const root = new THREE.Group(), body = pg.scene; root.add(body);
  const B = {}; body.traverse(o => { if (o.isBone) B[o.name] = o; if (o.isMesh) { o.castShadow = true; o.receiveShadow = true; o.frustumCulled = false; if (o.material.map) recolor(o.material, vest, suit); } });
  const bn = p => { const k = Object.keys(B).find(n => n.startsWith(p)); if (!k) throw new Error('hueso ' + p); return B[k]; };
  root.updateMatrixWorld(true);
  // cadera en el origen
  const hip = bn('hip_'); body.position.sub(wp(hip)); root.updateMatrixWorld(true);
  // casco y chaleco (se recolocan en cada pose siguiendo los huesos)
  const helm = hg.scene; helm.traverse(o => { if (o.isMesh) { o.castShadow = true; if (helmetColor) { o.material = o.material.clone(); o.material.color.set(helmetColor); } } });
  const hw = new THREE.Group(); hw.add(helm); helm.position.set(0, -0.12, -0.01); helm.scale.setScalar(1.32); root.add(hw);
  const ch = vg.scene; ch.traverse(o => { if (o.isMesh) { o.castShadow = true; o.material = o.material.clone(); recolorVest(o.material, vest); } });
  const cw = new THREE.Group(); cw.add(ch); ch.position.set(0, -0.27, -0.01); ch.scale.setScalar(0.9); root.add(cw);
  const Y = V(0, 1, 0), qa = new THREE.Quaternion(), qb = new THREE.Quaternion();
  const S = { hip: bn('hip_'), s1: bn('spine_01'), s2: bn('spine_02'), s3: bn('spine_03'), neck: bn('neck_'), head: bn('head_0') };
  // pose viva: st = { steer -1..1 (+ = izquierda), k velocidad 0..1, drift 0/1, t tiempo }
  function pose(st = {}) {
    const steer = st.steer || 0, k = st.k || 0, dr = st.drift ? 1 : 0, t = st.t || 0;
    root.updateWorldMatrix(true, true);
    const D = v => v.clone().normalize().transformDirection(root.matrixWorld), P3 = v => root.localToWorld(v.clone());   // del sistema del piloto al mundo
    const lean = 0.30 + 0.26 * k + 0.10 * dr + Math.sin(t * 2.1) * 0.015;               // se echa hacia delante con la velocidad
    const sd = V(steer * (0.30 + 0.12 * dr), Math.cos(lean), Math.sin(lean)).normalize();   // y se inclina hacia dentro de la curva
    aim(S.hip, S.s1, D(sd.clone().multiplyScalar(0.8).add(V(0, 0, -0.05))));
    aim(S.s1, S.s2, D(sd)); aim(S.s2, S.s3, D(sd)); aim(S.s3, S.neck, D(sd));
    aim(S.neck, S.head, D(V(steer * 0.32, 0.95, 0.20 - 0.12 * k)));                             // mira hacia donde gira
    const shake = Math.sin(t * 17) * 0.012 * k;                                              // vibración del manillar a velocidad
    for (const s of [1, -1]) {
      const side = s > 0 ? '_l' : '_r';
      ik2(bn('upperleg' + side), bn('lowerleg' + side), bn('foot' + side), P3(V(0.30 * s, -0.50, 0.22)), D(V(0.35 * s - steer * 0.1, 0.25, 1)));
      // manillar: gira con el volante y las manos van agarradas
      const a = -steer * 0.38, c = Math.cos(a), si = Math.sin(a), px = 0, pz = 0.52, dx = 0.27 * s - px, dz = 0.64 - pz;
      const hx = px + dx * c + dz * si, hz = pz - dx * si + dz * c;
      ik2(bn('upperarm' + side), bn('lowerarm' + side), bn('hand' + side), P3(V(hx, (st.barY ?? 0.13) + shake + (s * steer > 0 ? 0.015 : 0), hz)), D(V(1.0 * s, -0.25, -0.25)));
    }
    root.updateMatrixWorld(true);
    // casco sobre la cabeza, girado hacia la curva
    hw.position.copy(root.worldToLocal(wp(S.head)));
    qa.setFromUnitVectors(Y, V(steer * 0.18, 1, 0.22 - 0.12 * k).normalize()); qb.setFromAxisAngle(Y, steer * 0.42); hw.quaternion.copy(qb.multiply(qa));
    // chaleco sobre el torso
    cw.position.copy(root.worldToLocal(wp(S.s2))); cw.quaternion.setFromUnitVectors(Y, sd);
  }
  pose({});
  root.userData = { bones: B, helm: hw, vest: cw, pose };
  return root;
}
