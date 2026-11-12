// Moto de agua 3D procedural: casco por secciones, decoración pintada, piloto
import * as THREE from 'three';

// ---------- Casco (también sirve para barcos) ----------
// s: 0 popa → 1 proa. Anillo: centro de cubierta → lado izquierdo (+x) → quilla → lado derecho → centro.
export function hullShape({ L = 3.3, B = 1.18, sheer0 = 0.50, sheerK = 0.10, rocker = 0.38, bowPow = 0.95, vs = 1, crown = 0.03 } = {}) {
  const half = (s) => {
    const w = B / 2 * (s < 0.5 ? 0.9 + 0.1 * Math.sin(s / 0.5 * Math.PI / 2) : Math.pow(Math.max(0, 1 - ((s - 0.5) / 0.5) ** 2), bowPow));
    const k = s > 0.62 ? ((s - 0.62) / 0.38) ** 2 * rocker : 0;
    const sh = sheer0 + sheerK * Math.pow(s, 1.5);
    const deck = sh + crown * vs * (1 - 0.6 * s);
    return [[0, deck], [0.70 * w, sh + 0.065 * vs], [0.96 * w, sh], [1.03 * w, (sh + k + 0.24 * vs) / 2 + 0.03 * vs],
      [1.0 * w, k + 0.23 * vs], [0.80 * w, k + 0.17 * vs], [0.40 * w, k + 0.085 * vs], [0, k]];
  };
  const ring = (s) => { const h = half(s); const r = h.map(([x, y]) => [x, y]); for (let j = h.length - 2; j >= 0; j--) r.push([-h[j][0], h[j][1]]); return r; };
  const deckAt = (s) => half(s)[0][1];
  const sheerAt = (s) => half(s)[2][1];
  const halfW = (s) => half(s)[2][0];
  return { L, B, half, ring, deckAt, sheerAt, halfW, z: (s) => (s - 0.5) * L };
}

export function hullGeometry(shape, NS = 56) {
  const ref = shape.ring(0.35), RN = ref.length;
  const vAt = [0]; let tot = 0;
  for (let j = 1; j < RN; j++) { tot += Math.hypot(ref[j][0] - ref[j - 1][0], ref[j][1] - ref[j - 1][1]); vAt.push(tot); }
  for (let j = 0; j < RN; j++) vAt[j] /= tot;
  const pos = [], uv = [], idx = [];
  for (let i = 0; i <= NS; i++) {
    const s = i / NS, r = shape.ring(s), z = shape.z(s);
    for (let j = 0; j < RN; j++) { pos.push(r[j][0], r[j][1], z); uv.push(s, vAt[j]); }
  }
  for (let i = 0; i < NS; i++) for (let j = 0; j < RN - 1; j++) {
    const a = i * RN + j, b = a + 1, c = a + RN, d = c + 1;
    idx.push(a, c, b, b, c, d);
  }
  // espejo de popa
  const r0 = shape.ring(0), z0 = shape.z(0), base = pos.length / 3;
  let cy = 0; r0.forEach(p => cy += p[1]); cy /= r0.length;
  pos.push(0, cy, z0); uv.push(0.004, 0.45);
  for (let j = 0; j < RN; j++) { pos.push(r0[j][0], r0[j][1], z0); uv.push(0.004, 0.45); }
  for (let j = 0; j < RN - 1; j++) idx.push(base, base + 1 + j, base + 2 + j);
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2));
  g.setIndex(idx);
  g.computeVertexNormals();
  g.userData.vAt = vAt;
  return g;
}

// ---------- Decoración (pintura por zonas, franjas y rótulo) ----------
function liveryTexture(vAt, p) {
  const W = 2048, H = 1024, c = document.createElement('canvas'); c.width = W; c.height = H;
  const g = c.getContext('2d');
  const V = (j) => vAt[j] * H, Vr = (j) => (1 - vAt[j]) * H;     // lado izq. / lado der.
  g.fillStyle = p.hull; g.fillRect(0, 0, W, H);
  // cubierta + costado alto (pintura principal)
  g.fillStyle = p.paint;
  g.fillRect(0, 0, W, V(3) - 6); g.fillRect(0, Vr(3) + 6, W, H - Vr(3) - 6);
  // franja de acento a la altura de la manga máxima
  g.fillStyle = p.accent;
  g.fillRect(0, V(3) - 10, W, 22); g.fillRect(0, Vr(3) - 12, W, 22);
  // flecha de velocidad en la parte baja, de proa hacia atrás
  const swoosh = (yTop, yBot, dir) => {
    g.beginPath(); g.moveTo(W * 0.98, yTop); g.lineTo(W * 0.42, yTop + dir * 4); g.lineTo(W * 0.30, yTop + (yBot - yTop) * 0.45);
    g.lineTo(W * 0.62, yTop + (yBot - yTop) * 0.55); g.lineTo(W * 0.98, yBot); g.closePath(); g.fill();
  };
  g.fillStyle = p.accent; swoosh(V(3) + 14, V(4) + 10, 1); swoosh(Vr(3) - 14, Vr(4) - 10, -1);
  g.fillStyle = p.paint; swoosh(V(3) + 30, V(4) - 2, 1); swoosh(Vr(3) - 30, Vr(4) + 2, -1);
  // rótulo en el costado alto (izq. invertido en horizontal, der. en vertical)
  const label = (yMid, flipX, flipY) => {
    g.save(); g.translate(W * 0.47, yMid); g.scale(flipX ? -1 : 1, flipY ? -1 : 1);
    g.font = `italic 900 ${Math.round((V(3) - V(2)) * 0.62)}px "Arial Black", Arial, sans-serif`;
    g.textAlign = 'center'; g.textBaseline = 'middle';
    g.lineWidth = 6; g.strokeStyle = p.accent; g.strokeText(p.name, 0, 0);
    g.fillStyle = p.text; g.fillText(p.name, 0, 0); g.restore();
  };
  label((V(2) + V(3)) / 2, true, false);
  label((Vr(2) + Vr(3)) / 2, false, true);
  // antideslizante oscuro en el centro de la cubierta (zona de pies)
  g.fillStyle = 'rgba(20,22,26,0.88)';
  g.fillRect(W * 0.12, V(0), W * 0.46, (V(1) - V(0)) * 0.95); g.fillRect(W * 0.12, Vr(1) + (Vr(0) - Vr(1)) * 0.05, W * 0.46, (Vr(0) - Vr(1)) * 0.95);
  const t = new THREE.CanvasTexture(c);
  t.flipY = false; t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8;
  return t;
}


function upperBodyGeometry(shape, P) {
  const NS = 64, s0 = 0.03, s1 = 0.985;
  const top = (s) => {
    if (s < 0.12) return 0.05 + (s - s0) / (0.12 - s0) * 0.11;
    if (s < 0.50) return 0.16;
    if (s < 0.60) { const t = (s - 0.5) / 0.1; return 0.16 + 0.29 * (t * t * (3 - 2 * t)); }
    const t = (s - 0.6) / (s1 - 0.6); return 0.45 - 0.41 * Math.pow(t, 1.35);
  };
  const wu = (s) => shape.halfW(s) * (s < 0.6 ? 0.56 : 0.56 + 0.34 * ((s - 0.6) / 0.4));
  const cP = new THREE.Color(P.paint), cA = new THREE.Color(P.accent), cG = new THREE.Color('#0b0f15'), cK = new THREE.Color('#1a1c20');
  const pos = [], cols = [], idx = []; let RN = 0;
  for (let i = 0; i <= NS; i++) {
    const s = s0 + (s1 - s0) * i / NS, b = shape.sheerAt(s) - 0.03, t = top(s), w = wu(s), z = shape.z(s);
    const half = [[0, b + t], [0.5 * w, b + t - 0.008], [0.82 * w, b + t - 0.03], [0.97 * w, b + t - 0.075], [w, b + Math.max(0.03, t * 0.45)], [w, b]];
    const ring = half.slice(); for (let j = half.length - 1; j >= 0; j--) ring.push([-half[j][0], half[j][1]]);
    RN = ring.length;
    for (let j = 0; j < RN; j++) {
      const [x, y] = ring[j];
      pos.push(x, y, z);
      let c = cP;
      const rel = y - b;
      if (s > 0.5 && s < 0.61 && rel > 0.2 && Math.abs(x) < 0.85 * w) c = cG;            // parabrisas oscuro
      else if (s > 0.6 && Math.abs(x) < 0.075) c = cA;                                    // franja del capó
      else if (rel < 0.05 && s < 0.55) c = cK;                                            // zócalo oscuro
      cols.push(c.r, c.g, c.b);
    }
  }
  for (let i = 0; i < NS; i++) for (let j = 0; j < RN - 1; j++) { const a = i * RN + j, b2 = a + 1, c = a + RN, d = c + 1; idx.push(a, c, b2, b2, c, d); }
  // tapa trasera
  const base = pos.length / 3, r0 = []; for (let j = 0; j < RN; j++) r0.push([pos[j * 3], pos[j * 3 + 1], pos[j * 3 + 2]]);
  let cy = 0; r0.forEach(p => cy += p[1]); cy /= RN; pos.push(0, cy, r0[0][2]); cols.push(cP.r, cP.g, cP.b);
  for (let j = 0; j < RN - 1; j++) idx.push(base, j, j + 1);
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3));
  g.setAttribute('color', new THREE.Float32BufferAttribute(cols, 3));
  g.setIndex(idx); g.computeVertexNormals();
  return { g, top, wu };
}

export const PAINTS = {
  naranja: { paint: '#ff5a0a', accent: '#13244a', hull: '#f3f5f8', text: '#ffffff', name: 'COSTA TURBO', seat: '#121418', vest: '#ff5a0a' },
  negra: { paint: '#15171b', accent: '#ffb000', hull: '#22252b', text: '#ffb000', name: 'RIVA RACING', seat: '#0c0d10', vest: '#1c1f24' },
  dorada: { paint: '#c9a038', accent: '#151515', hull: '#f2f2f2', text: '#151515', name: 'SEA-DOO', seat: '#151515', vest: '#c9a038' },
};

function capsuleBetween(a, b, r, mat) {
  const d = new THREE.Vector3().subVectors(b, a), len = d.length();
  const m = new THREE.Mesh(new THREE.CapsuleGeometry(r, Math.max(0.001, len), 6, 14), mat);
  m.position.copy(a).addScaledVector(d, 0.5);
  m.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), d.normalize());
  m.castShadow = true;
  return m;
}
const V3 = (x, y, z) => new THREE.Vector3(x, y, z);

export function makeJetSki(paintKey = 'naranja') {
  const P = PAINTS[paintKey];
  const shape = hullShape();
  const root = new THREE.Group();            // posición/rumbo en el mundo
  const body = new THREE.Group();            // cabeceo, alabeo y flotación
  root.add(body);
  const hullG = hullGeometry(shape);
  const paintMat = new THREE.MeshPhysicalMaterial({ map: liveryTexture(hullG.userData.vAt, P), roughness: 0.32, metalness: 0.0, clearcoat: 1.0, clearcoatRoughness: 0.06 });
  const hull = new THREE.Mesh(hullG, paintMat); hull.castShadow = true; hull.receiveShadow = true; body.add(hull);

  const glossy = (hex, rough = 0.3) => new THREE.MeshPhysicalMaterial({ color: hex, roughness: rough, clearcoat: 1, clearcoatRoughness: 0.08 });
  const paintSolid = glossy(P.paint, 0.3);
  const black = new THREE.MeshStandardMaterial({ color: 0x15171b, roughness: 0.55 });
  const seatMat = new THREE.MeshPhysicalMaterial({ color: P.seat, roughness: 0.5, sheen: 0.4, sheenColor: new THREE.Color(0x444444) });
  const metal = new THREE.MeshStandardMaterial({ color: 0x9aa3ad, roughness: 0.25, metalness: 0.9 });

  // cuerpo superior: asiento, consola y capó
  const ub = upperBodyGeometry(shape, P);
  const upper = new THREE.Mesh(ub.g, new THREE.MeshPhysicalMaterial({ vertexColors: true, roughness: 0.3, clearcoat: 1, clearcoatRoughness: 0.06 }));
  upper.castShadow = true; upper.receiveShadow = true; body.add(upper);
  const sS = 0.31, seat = new THREE.Mesh(new THREE.CapsuleGeometry(0.19, 0.86, 8, 20), seatMat);
  seat.rotation.x = Math.PI / 2; seat.scale.set(1.15, 1, 0.62);
  seat.position.set(0, shape.sheerAt(sS) - 0.03 + 0.16 + 0.08, shape.z(sS)); seat.castShadow = true; body.add(seat);
  // manillar
  const sB = 0.575, barY = shape.sheerAt(sB) - 0.03 + ub.top(sB) + 0.14, barZ = shape.z(sB);
  body.add(capsuleBetween(V3(0, barY - 0.16, barZ + 0.02), V3(0, barY, barZ), 0.04, black));
  body.add(capsuleBetween(V3(-0.34, barY + 0.02, barZ - 0.02), V3(0.34, barY + 0.02, barZ - 0.02), 0.017, metal));
  body.add(capsuleBetween(V3(-0.42, barY + 0.02, barZ - 0.02), V3(-0.29, barY + 0.02, barZ - 0.02), 0.03, black));
  body.add(capsuleBetween(V3(0.29, barY + 0.02, barZ - 0.02), V3(0.42, barY + 0.02, barZ - 0.02), 0.03, black));
  // retrovisores
  for (const sx of [-1, 1]) {
    const sm = 0.66, my = shape.sheerAt(sm) - 0.03 + ub.top(sm), mx = ub.wu(sm) * 0.8;
    body.add(capsuleBetween(V3(sx * mx, my - 0.02, shape.z(sm)), V3(sx * (mx + 0.12), my + 0.1, shape.z(sm) - 0.02), 0.012, black));
    const mir = new THREE.Mesh(new THREE.SphereGeometry(0.065, 12, 8), black); mir.scale.set(1.4, 0.7, 0.45);
    mir.position.set(sx * (mx + 0.14), my + 0.11, shape.z(sm) - 0.02); body.add(mir);
  }
  // agarre trasero, tobera y aletas
  const grab = new THREE.Mesh(new THREE.TorusGeometry(0.16, 0.022, 8, 20, Math.PI), black);
  grab.position.set(0, shape.sheerAt(0.07) + 0.06, shape.z(0.07)); body.add(grab);
  const noz = new THREE.Mesh(new THREE.CylinderGeometry(0.075, 0.09, 0.28, 16), metal);
  noz.rotation.x = Math.PI / 2; noz.position.set(0, 0.13, shape.z(0) - 0.06); body.add(noz);
  for (const sx of [-1, 1]) {
    const fin = new THREE.Mesh(new THREE.BoxGeometry(0.04, 0.09, 0.42), black);
    fin.position.set(sx * (shape.halfW(0.08) + 0.03), 0.2, shape.z(0.08)); body.add(fin);
  }

  // ---------- Piloto ----------
  const rider = new THREE.Group(); body.add(rider);
  const suit = new THREE.MeshStandardMaterial({ color: 0x14161a, roughness: 0.6 });
  const vestM = new THREE.MeshPhysicalMaterial({ color: P.vest, roughness: 0.55, sheen: 0.3 });
  const vestDark = new THREE.MeshStandardMaterial({ color: 0x1b1e23, roughness: 0.6 });
  const helmM = new THREE.MeshPhysicalMaterial({ color: 0xf4f4f4, roughness: 0.25, clearcoat: 1 });
  const D = shape.sheerAt(0.35);
  const J = {
    pelvis: V3(0, D + 0.63, -0.34), neck: V3(0, D + 1.12, -0.04), head: V3(0, D + 1.33, 0.05),
    hipL: V3(0.13, D + 0.62, -0.33), hipR: V3(-0.13, D + 0.62, -0.33),
    kneeL: V3(0.29, D + 0.42, 0.06), kneeR: V3(-0.29, D + 0.42, 0.06),
    ankL: V3(0.35, D + 0.07, -0.2), ankR: V3(-0.35, D + 0.07, -0.2),
    shL: V3(0.22, D + 1.07, -0.05), shR: V3(-0.22, D + 1.07, -0.05),
    elL: V3(0.45, D + 0.82, -0.02), elR: V3(-0.45, D + 0.82, -0.02),
    haL: V3(0.36, barY + 0.02, barZ - 0.02), haR: V3(-0.36, barY + 0.02, barZ - 0.02),
  };
  rider.add(capsuleBetween(J.pelvis, J.neck, 0.15, suit));
  const vest = capsuleBetween(V3(0, D + 0.73, -0.29), V3(0, D + 1.04, -0.07), 0.185, vestM); vest.scale.x = 1.12; rider.add(vest);
  const vestSide = capsuleBetween(V3(0, D + 0.71, -0.3), V3(0, D + 0.98, -0.1), 0.19, vestDark); vestSide.scale.set(1.13, 1, 0.55); rider.add(vestSide);
  for (const s of ['L', 'R']) {
    rider.add(capsuleBetween(J['hip' + s], J['knee' + s], 0.092, suit));
    rider.add(capsuleBetween(J['knee' + s], J['ank' + s], 0.072, suit));
    rider.add(capsuleBetween(J['sh' + s], J['el' + s], 0.066, suit));
    rider.add(capsuleBetween(J['el' + s], J['ha' + s], 0.056, suit));
    const foot = new THREE.Mesh(new THREE.BoxGeometry(0.11, 0.08, 0.27), black);
    foot.position.copy(J['ank' + s]).add(V3(0, -0.03, 0.08)); foot.castShadow = true; rider.add(foot);
    const glove = new THREE.Mesh(new THREE.SphereGeometry(0.055, 12, 8), black); glove.position.copy(J['ha' + s]); rider.add(glove);
  }
  const helmet = new THREE.Mesh(new THREE.SphereGeometry(0.155, 28, 18), helmM); helmet.scale.set(1, 1, 1.12);
  helmet.position.copy(J.head); helmet.castShadow = true; rider.add(helmet);
  const hStripe = new THREE.Mesh(new THREE.SphereGeometry(0.157, 28, 18, Math.PI / 2 - 0.25, 0.5), glossy(P.paint, 0.25));
  hStripe.scale.copy(helmet.scale); hStripe.position.copy(J.head); rider.add(hStripe);
  const goggles = new THREE.Mesh(new THREE.SphereGeometry(0.16, 24, 10, Math.PI / 2 - 0.9, 1.8, 1.2, 0.45), new THREE.MeshPhysicalMaterial({ color: 0x101820, roughness: 0.05, metalness: 0.6, clearcoat: 1, iridescence: 0.6 }));
  goggles.scale.copy(helmet.scale); goggles.position.copy(J.head); rider.add(goggles);

  return { root, body, rider, shape, paintKey };
}
