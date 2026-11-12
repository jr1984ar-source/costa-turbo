// Vegetación, aves, barcos, boyas y sombrillas
import * as THREE from 'three';
import { rng, fbm, smooth } from './noise.js';
import { heightAt, signedDist } from './world.js';
import { hullShape, hullGeometry } from './jetski.js';

const col = (hex) => new THREE.Color(hex);

// Mata de hierba seca (como la del vídeo): hojas curvas que salen del centro
function grassClumpGeometry(seed = 3, blades = 30) {
  const R = rng(seed), pos = [], cols = [], idx = [];
  const base = col('#8a6a3c'), mid = col('#d2b27a'), tip = col('#f6ead0');
  for (let b = 0; b < blades; b++) {
    const th = R() * Math.PI * 2, tilt = 0.2 + R() * 1.1, len = 0.45 + R() * 0.6, w0 = 0.012 + R() * 0.012;
    const dx = Math.cos(th), dz = Math.sin(th), px = -dz, pz = dx;
    const segs = 3, start = pos.length / 3;
    for (let k = 0; k <= segs; k++) {
      const t = k / segs, r = Math.sin(tilt) * len * t + 0.25 * len * t * t * tilt, y = Math.cos(tilt) * len * t - 0.35 * len * t * t * tilt;
      const w = w0 * (0.35 + 1.6 * Math.sin(Math.PI * Math.min(1, t * 1.08)));
      const cx = dx * r, cz = dz * r;
      pos.push(cx + px * w, y, cz + pz * w, cx - px * w, y, cz - pz * w);
      const c = t < 0.5 ? base.clone().lerp(mid, t * 2) : mid.clone().lerp(tip, (t - 0.5) * 2);
      cols.push(c.r, c.g, c.b, c.r, c.g, c.b);
    }
    for (let k = 0; k < segs; k++) { const a = start + k * 2; idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
  }
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute('color', new THREE.Float32BufferAttribute(cols, 3));
  g.setIndex(idx); g.computeVertexNormals();
  return g;
}

export function makeGrass(area, count = 9000, seed = 11) {
  const R = rng(seed), mats = [], dummy = new THREE.Object3D();
  const geo = grassClumpGeometry(5);
  const mat = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.9, side: THREE.DoubleSide });
  const list = [];
  for (let i = 0; i < count * 6 && list.length < count; i++) {
    const x = area.x0 + R() * (area.x1 - area.x0), z = area.z0 + R() * (area.z1 - area.z0);
    const d = signedDist(x, z);
    if (d < 5 || d > 160) continue;
    const band = 0.5 + 0.5 * Math.sin(d * 0.11 + fbm(x * 0.02, z * 0.02, 2) * 4);
    const clump = smooth(0.42, 0.62, fbm(x * 0.045 + 3, z * 0.045 - 1, 3));
    const near = Math.exp(-(((d - 20) / 9) ** 2));
    const dens = smooth(6, 11, d) * Math.min(1, (0.25 + 0.75 * clump) * (0.35 + 0.65 * band) + near * 0.55);
    if (R() > dens) continue;
    list.push([x, z]);
  }
  const m = new THREE.InstancedMesh(geo, mat, list.length);
  const c = new THREE.Color();
  list.forEach(([x, z], i) => {
    dummy.position.set(x, heightAt(x, z) - 0.05, z);
    dummy.rotation.set((R() - 0.5) * 0.15, R() * Math.PI * 2, (R() - 0.5) * 0.15);
    const s = 0.8 + R() * 1.1; dummy.scale.set(s, s * (0.8 + R() * 0.5), s);
    dummy.updateMatrix(); m.setMatrixAt(i, dummy.matrix);
    c.setRGB(0.85 + R() * 0.3, 0.85 + R() * 0.25, 0.8 + R() * 0.25); m.setColorAt(i, c);
  });
  m.castShadow = true; m.receiveShadow = true;
  m.instanceMatrix.needsUpdate = true;
  return m;
}

// Palmera: tronco curvo con anillos + hojas tipo pluma
function palmGeometry(R) {
  const H = 6.5 + R() * 4, lean = 0.6 + R() * 1.6, lx = R() * Math.PI * 2;
  const pts = [];
  for (let i = 0; i <= 10; i++) { const t = i / 10; pts.push(new THREE.Vector3(Math.cos(lx) * lean * t * t, H * t, Math.sin(lx) * lean * t * t)); }
  const curve = new THREE.CatmullRomCurve3(pts);
  const trunkPos = [], trunkCol = [], trunkIdx = [], RS = 10, LS = 40;
  const bark = col('#7b6248'), barkD = col('#4f3d2b');
  for (let i = 0; i <= LS; i++) {
    const t = i / LS, p = curve.getPoint(t), tan = curve.getTangent(t);
    const nrm = new THREE.Vector3(1, 0, 0).cross(tan).normalize(), bin = tan.clone().cross(nrm).normalize();
    const r = (0.24 - 0.1 * t) * (1 + 0.08 * Math.sin(t * 120));
    const c = bark.clone().lerp(barkD, 0.5 + 0.5 * Math.sin(t * 120));
    for (let j = 0; j <= RS; j++) {
      const a = j / RS * Math.PI * 2, o = nrm.clone().multiplyScalar(Math.cos(a) * r).addScaledVector(bin, Math.sin(a) * r);
      trunkPos.push(p.x + o.x, p.y + o.y, p.z + o.z); trunkCol.push(c.r, c.g, c.b);
    }
  }
  for (let i = 0; i < LS; i++) for (let j = 0; j < RS; j++) { const a = i * (RS + 1) + j, b = a + RS + 1; trunkIdx.push(a, b, a + 1, a + 1, b, b + 1); }
  const trunk = new THREE.BufferGeometry();
  trunk.setAttribute('position', new THREE.Float32BufferAttribute(trunkPos, 3));
  trunk.setAttribute('color', new THREE.Float32BufferAttribute(trunkCol, 3));
  trunk.setIndex(trunkIdx); trunk.computeVertexNormals();
  // hojas
  const top = curve.getPoint(1), fp = [], fc = [], fi = [];
  const g1 = col('#2f5a1c'), g2 = col('#6f9a34'), g3 = col('#a7a04a');
  const NF = 11;
  for (let f = 0; f < NF; f++) {
    const az = f / NF * Math.PI * 2 + R() * 0.4, len = 3.2 + R() * 1.6, lift = 0.6 + R() * 0.8, droop = 2.2 + R() * 1.2;
    const dx = Math.cos(az), dz = Math.sin(az), px = -dz, pz = dx;
    const S = 16, start = fp.length / 3;
    for (let k = 0; k <= S; k++) {
      const t = k / S, r = len * t, y = lift * t * 2.0 - droop * t * t;
      const sx = top.x + dx * r, sy = top.y + y, sz = top.z + dz * r;
      const w = Math.sin(Math.PI * Math.min(1, t * 1.15)) * (0.75 + 0.15 * R()) * (k % 2 ? 0.75 : 1);
      const dropL = 0.25 + 0.3 * t;
      fp.push(sx, sy, sz, sx + px * w, sy - dropL, sz + pz * w, sx - px * w, sy - dropL, sz - pz * w);
      const c = g1.clone().lerp(g2, t).lerp(g3, Math.max(0, t - 0.75) * 2);
      fc.push(c.r * 0.85, c.g * 0.85, c.b * 0.85, c.r, c.g, c.b, c.r, c.g, c.b);
    }
    for (let k = 0; k < S; k++) {
      const a = start + k * 3, b = a + 3;
      fi.push(a, a + 1, b, a + 1, b + 1, b, a, b, a + 2, a + 2, b, b + 2);
    }
  }
  const fr = new THREE.BufferGeometry();
  fr.setAttribute('position', new THREE.Float32BufferAttribute(fp, 3));
  fr.setAttribute('color', new THREE.Float32BufferAttribute(fc, 3));
  fr.setIndex(fi); fr.computeVertexNormals();
  return { trunk, fr };
}

export function makePalms(spots, seed = 21) {
  const R = rng(seed), grp = new THREE.Group();
  const tm = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.95 });
  const fm = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.75, side: THREE.DoubleSide });
  for (const [x, z] of spots) {
    const { trunk, fr } = palmGeometry(R);
    const t = new THREE.Mesh(trunk, tm), f = new THREE.Mesh(fr, fm);
    for (const m of [t, f]) { m.position.set(x, heightAt(x, z) - 0.1, z); m.castShadow = true; m.receiveShadow = true; grp.add(m); }
  }
  return grp;
}

// Gaviota planeando
export function makeGull(flap = 0.2) {
  const g = new THREE.Group();
  const white = new THREE.MeshStandardMaterial({ color: 0xf2f2ee, roughness: 0.8 });
  const body = new THREE.Mesh(new THREE.SphereGeometry(0.1, 14, 10), white); body.scale.set(1, 0.9, 3.0); g.add(body);
  const head = new THREE.Mesh(new THREE.SphereGeometry(0.07, 12, 8), white); head.position.set(0, 0.04, 0.3); g.add(head);
  const beak = new THREE.Mesh(new THREE.ConeGeometry(0.018, 0.08, 6), new THREE.MeshStandardMaterial({ color: 0xe0a020 })); beak.rotation.x = Math.PI / 2; beak.position.set(0, 0.03, 0.39); g.add(beak);
  const wingGeo = (side) => {
    const pos = [0, 0, 0.08, 0, 0, -0.12, side * 0.45, 0.06, -0.1, side * 0.45, 0.06, 0.1, side * 0.85, 0.0, -0.05];
    const c1 = col('#f0f0ec'), c2 = col('#9aa0a6'), c3 = col('#202225');
    const cols = [c1, c1, c2, c2, c3].flatMap(c => [c.r, c.g, c.b]);
    const gg = new THREE.BufferGeometry();
    gg.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); gg.setAttribute('color', new THREE.Float32BufferAttribute(cols, 3));
    gg.setIndex([0, 1, 2, 0, 2, 3, 3, 2, 4]); gg.computeVertexNormals(); return gg;
  };
  const wm = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.8, side: THREE.DoubleSide });
  const wl = new THREE.Mesh(wingGeo(1), wm), wr = new THREE.Mesh(wingGeo(-1), wm);
  wl.rotation.z = flap; wr.rotation.z = -flap; g.add(wl, wr);
  g.traverse(o => { if (o.isMesh) o.castShadow = true; });
  g.scale.setScalar(1.3);
  return g;
}

// Yate fondeado
export function makeYacht(seed = 1) {
  const g = new THREE.Group();
  const shape = hullShape({ L: 13, B: 4.0, sheer0: 1.6, sheerK: 0.5, rocker: 1.2, bowPow: 0.8, vs: 3.4 });
  const white = new THREE.MeshPhysicalMaterial({ color: 0xf6f7f8, roughness: 0.3, clearcoat: 1 });
  const hull = new THREE.Mesh(hullGeometry(shape, 40), white); hull.castShadow = true; g.add(hull);
  const teak = new THREE.MeshStandardMaterial({ color: 0xa57a4c, roughness: 0.7 });
  const deck = new THREE.Mesh(new THREE.BoxGeometry(3.2, 0.1, 9.5), teak); deck.position.set(0, shape.deckAt(0.4) - 0.05, -0.6); g.add(deck);
  const cabin = new THREE.Mesh(new THREE.BoxGeometry(2.8, 1.2, 4.6), white); cabin.position.set(0, shape.deckAt(0.5) + 0.55, 0.2); cabin.castShadow = true; g.add(cabin);
  const glass = new THREE.Mesh(new THREE.BoxGeometry(2.84, 0.45, 3.6), new THREE.MeshPhysicalMaterial({ color: 0x0c1218, roughness: 0.05, metalness: 0.5 }));
  glass.position.set(0, shape.deckAt(0.5) + 0.75, 0.3); g.add(glass);
  const top = new THREE.Mesh(new THREE.BoxGeometry(3.0, 0.12, 5.4), white); top.position.set(0, shape.deckAt(0.5) + 1.2, -0.1); top.castShadow = true; g.add(top);
  return g;
}

export function makeBuoy(color = '#ff7a1a') {
  const m = new THREE.Mesh(new THREE.SphereGeometry(0.45, 20, 14), new THREE.MeshPhysicalMaterial({ color, roughness: 0.35, clearcoat: 0.6 }));
  m.castShadow = true;
  return m;
}

export function makeUmbrella(c1 = '#ff5a0a', c2 = '#ffffff') {
  const g = new THREE.Group();
  const N = 12, pos = [], cols = [], A = col(c1), B = col(c2);
  for (let i = 0; i < N; i++) {
    const a0 = i / N * Math.PI * 2, a1 = (i + 1) / N * Math.PI * 2, c = i % 2 ? A : B;
    pos.push(0, 2.45, 0, Math.cos(a0) * 1.3, 2.0, Math.sin(a0) * 1.3, Math.cos(a1) * 1.3, 2.0, Math.sin(a1) * 1.3);
    for (let k = 0; k < 3; k++) cols.push(c.r, c.g, c.b);
  }
  const gg = new THREE.BufferGeometry(); gg.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); gg.setAttribute('color', new THREE.Float32BufferAttribute(cols, 3)); gg.computeVertexNormals();
  const top = new THREE.Mesh(gg, new THREE.MeshStandardMaterial({ vertexColors: true, roughness: 0.8, side: THREE.DoubleSide })); top.castShadow = true; g.add(top);
  const pole = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 2.45, 8), new THREE.MeshStandardMaterial({ color: 0xdddddd, roughness: 0.4 })); pole.position.y = 1.22; pole.castShadow = true; g.add(pole);
  const towel = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.02, 1.8), new THREE.MeshStandardMaterial({ color: c1 === '#ff5a0a' ? 0x2a6fdb : 0xffc83d, roughness: 0.9 }));
  towel.position.set(1.3, 0.02, 0.4); towel.rotation.y = 0.3; towel.receiveShadow = true; g.add(towel);
  return g;
}
