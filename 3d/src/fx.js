// Estela (espuma detrás de la moto) y salpicaduras
import * as THREE from 'three';
import { GLSL_NOISE, rng } from './noise.js';

const premult = {
  transparent: true, depthWrite: false,
  blending: THREE.CustomBlending, blendEquation: THREE.AddEquation,
  blendSrc: THREE.OneFactor, blendDst: THREE.OneMinusSrcAlphaFactor,
  blendSrcAlpha: THREE.OneFactor, blendDstAlpha: THREE.OneMinusSrcAlphaFactor,
};

export function wakeMaterial(env) {
  return new THREE.ShaderMaterial({
    ...premult, side: THREE.DoubleSide,
    uniforms: { uTime: env.time, uSunCol: { value: env.sunCol } },
    vertexShader: `attribute float aSide; attribute float aAge; attribute float aK; varying float vSide; varying float vAge; varying float vK; varying vec3 vW;
      void main(){ vSide = aSide; vAge = aAge; vK = aK; vec4 w = modelMatrix * vec4(position,1.0); vW = w.xyz; gl_Position = projectionMatrix * viewMatrix * w; }`,
    fragmentShader: `uniform float uTime; uniform vec3 uSunCol; varying float vSide; varying float vAge; varying float vK; varying vec3 vW;
      ${GLSL_NOISE}
      void main(){
        float s = abs(vSide);
        float n1 = ct_n(vW.xz * 1.6 + vec2(uTime * 0.3, 0.0)), n2 = ct_n(vW.xz * 5.0 - uTime * 0.5), n3 = ct_n(vW.xz * 0.5);
        float fade = exp(-vAge / 5.5) * smoothstep(0.0, 0.08, vAge) * vK;
        float arms = smoothstep(0.62, 0.9, s) * (1.0 - smoothstep(0.9, 1.0, s));
        float core = pow(1.0 - s, 1.6) * exp(-vAge / 2.2);
        float lace = smoothstep(0.42, 0.75, n1 * 0.6 + n2 * 0.4);
        float foam = clamp(arms * (0.45 + 0.55 * lace) * 0.85 + core * (0.55 + 0.45 * lace) + (1.0 - s) * 0.25 * lace * smoothstep(0.3, 0.7, n3), 0.0, 1.0) * fade;
        vec3 c = vec3(0.92, 0.97, 1.0) * (uSunCol.g * 0.42 + 0.35);
        gl_FragColor = vec4(c * foam, foam);
      }`,
  });
}
export function sprayMaterial(env) {
  return new THREE.ShaderMaterial({
    ...premult,
    uniforms: { uSunCol: { value: env.sunCol }, uScale: { value: 900 } },
    vertexShader: `attribute float aSize; attribute float aAlpha; uniform float uScale; varying float vA;
      void main(){ vA = aAlpha; vec4 mv = modelViewMatrix * vec4(position, 1.0); gl_PointSize = aSize * uScale / -mv.z; gl_Position = projectionMatrix * mv; }`,
    fragmentShader: `uniform vec3 uSunCol; varying float vA;
      void main(){ vec2 d = gl_PointCoord - 0.5; float r = length(d) * 2.0; if (r > 1.0) discard;
        float a = (1.0 - r * r) * vA; float lit = 0.75 + 0.25 * (0.5 - d.y);
        vec3 c = vec3(0.93, 0.97, 1.0) * (uSunCol.g * 0.38 + 0.4) * lit;
        gl_FragColor = vec4(c * a, a); }`,
  });
}
function wakeGeometry(path) {
  const n = path.length, pos = new Float32Array(n * 6), side = new Float32Array(n * 2), age = new Float32Array(n * 2), k = new Float32Array(n * 2), idx = [];
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.BufferAttribute(pos, 3)); g.setAttribute('aSide', new THREE.BufferAttribute(side, 1));
  g.setAttribute('aAge', new THREE.BufferAttribute(age, 1)); g.setAttribute('aK', new THREE.BufferAttribute(k, 1));
  for (let i = 0; i < n - 1; i++) { const a = i * 2; idx.push(a, a + 2, a + 1, a + 1, a + 2, a + 3); }
  g.setIndex(idx);
  return g;
}
function fillWake(g, path, n) {
  const pos = g.attributes.position.array, side = g.attributes.aSide.array, age = g.attributes.aAge.array, kk = g.attributes.aK.array;
  for (let i = 0; i < n; i++) {
    const p = path[i], q = path[Math.min(n - 1, i + 1)], o = path[Math.max(0, i - 1)];
    let tx = q.x - o.x, tz = q.z - o.z; const L = Math.hypot(tx, tz) || 1; tx /= L; tz /= L;
    const w = 0.55 + p.age * 1.9 * (p.k ?? 1);
    pos[i * 6] = p.x - tz * w; pos[i * 6 + 1] = 0.03; pos[i * 6 + 2] = p.z + tx * w;
    pos[i * 6 + 3] = p.x + tz * w; pos[i * 6 + 4] = 0.03; pos[i * 6 + 5] = p.z - tx * w;
    side[i * 2] = -1; side[i * 2 + 1] = 1; age[i * 2] = age[i * 2 + 1] = p.age; kk[i * 2] = kk[i * 2 + 1] = p.k ?? 1;
  }
  for (const a of ['position', 'aSide', 'aAge', 'aK']) g.attributes[a].needsUpdate = true;
  g.setDrawRange(0, Math.max(0, (n - 1) * 6));
}
// path: [{x,z,age}] desde la popa hacia atrás (imagen fija)
export function makeWake(env, path) {
  const g = wakeGeometry(path); fillWake(g, path, path.length);
  const m = new THREE.Mesh(g, wakeMaterial(env)); m.renderOrder = 3; m.frustumCulled = false; return m;
}
// Estela en vivo: guarda puntos de la popa y los envejece
export class Wake {
  constructor(env, max = 360) { this.max = max; this.pts = []; this.geo = wakeGeometry(new Array(max).fill(0)); this.mesh = new THREE.Mesh(this.geo, wakeMaterial(env)); this.mesh.renderOrder = 3; this.mesh.frustumCulled = false; this.mesh.userData.noAO = true; }
  update(dt, x, z, k) {
    for (const p of this.pts) p.age += dt;
    while (this.pts.length && this.pts[this.pts.length - 1].age > 14) this.pts.pop();
    const h = this.pts[0];
    if (k > 0.05 && (!h || Math.hypot(h.x - x, h.z - z) > 0.6)) { this.pts.unshift({ x, z, age: 0, k }); if (this.pts.length > this.max) this.pts.pop(); }
    else if (h) { h.x = x; h.z = z; }
    fillWake(this.geo, this.pts, this.pts.length);
  }
}
// Partículas de agua: lista de {p:Vector3, size, alpha}
export function makeSpray(env, parts) {
  const n = parts.length, pos = new Float32Array(n * 3), size = new Float32Array(n), alpha = new Float32Array(n);
  parts.forEach((q, i) => { pos.set([q.p.x, q.p.y, q.p.z], i * 3); size[i] = q.size; alpha[i] = q.alpha; });
  const g = new THREE.BufferGeometry();
  g.setAttribute('position', new THREE.BufferAttribute(pos, 3));
  g.setAttribute('aSize', new THREE.BufferAttribute(size, 1));
  g.setAttribute('aAlpha', new THREE.BufferAttribute(alpha, 1));
  const m = new THREE.Points(g, sprayMaterial(env)); m.renderOrder = 4; m.frustumCulled = false; return m;
}
// Salpicaduras en vivo (gotas con gravedad)
export class Spray {
  constructor(env, max = 2400) {
    this.max = max; this.n = 0;
    this.p = new Float32Array(max * 3); this.v = new Float32Array(max * 3); this.life = new Float32Array(max); this.age = new Float32Array(max); this.s0 = new Float32Array(max); this.a0 = new Float32Array(max);
    const g = new THREE.BufferGeometry();
    this.pos = new THREE.BufferAttribute(new Float32Array(max * 3), 3); this.size = new THREE.BufferAttribute(new Float32Array(max), 1); this.alpha = new THREE.BufferAttribute(new Float32Array(max), 1);
    g.setAttribute('position', this.pos); g.setAttribute('aSize', this.size); g.setAttribute('aAlpha', this.alpha);
    this.points = new THREE.Points(g, sprayMaterial(env)); this.points.renderOrder = 4; this.points.frustumCulled = false;
  }
  emit(x, y, z, vx, vy, vz, size, life, alpha) {
    if (this.n >= this.max) return; const i = this.n++;
    this.p[i * 3] = x; this.p[i * 3 + 1] = y; this.p[i * 3 + 2] = z; this.v[i * 3] = vx; this.v[i * 3 + 1] = vy; this.v[i * 3 + 2] = vz;
    this.life[i] = life; this.age[i] = 0; this.s0[i] = size; this.a0[i] = alpha;
  }
  update(dt) {
    let j = 0;
    for (let i = 0; i < this.n; i++) {
      const a = this.age[i] + dt; let y = this.p[i * 3 + 1] + this.v[i * 3 + 1] * dt;
      if (a > this.life[i] || y < -0.05) continue;
      this.v[i * 3 + 1] -= 9.8 * dt; this.v[i * 3] *= 1 - dt * 0.6; this.v[i * 3 + 2] *= 1 - dt * 0.6;
      this.p[j * 3] = this.p[i * 3] + this.v[i * 3] * dt; this.p[j * 3 + 1] = y; this.p[j * 3 + 2] = this.p[i * 3 + 2] + this.v[i * 3 + 2] * dt;
      this.v[j * 3] = this.v[i * 3]; this.v[j * 3 + 1] = this.v[i * 3 + 1]; this.v[j * 3 + 2] = this.v[i * 3 + 2];
      this.age[j] = a; this.life[j] = this.life[i]; this.s0[j] = this.s0[i]; this.a0[j] = this.a0[i]; j++;
    }
    this.n = j;
    const P = this.pos.array, S = this.size.array, A = this.alpha.array;
    for (let i = 0; i < j; i++) { const t = this.age[i] / this.life[i]; P[i * 3] = this.p[i * 3]; P[i * 3 + 1] = this.p[i * 3 + 1]; P[i * 3 + 2] = this.p[i * 3 + 2]; S[i] = this.s0[i] * (1 + t * 2.2); A[i] = this.a0[i] * (1 - t); }
    this.pos.needsUpdate = this.size.needsUpdate = this.alpha.needsUpdate = true;
    this.points.geometry.setDrawRange(0, j);
  }
}

// Chorro trasero (cola de gallo) y abanicos laterales para una pose fija
export function sprayForPose(origin, fwd, speed, turn, seed = 5) {
  const R = rng(seed), out = [], up = new THREE.Vector3(0, 1, 0);
  const right = new THREE.Vector3().crossVectors(fwd, up).normalize();
  const back = fwd.clone().multiplyScalar(-1);
  // cola de gallo
  for (let i = 0; i < 3200; i++) {
    const t = Math.pow(R(), 0.8) * 0.75;
    const v = back.clone().multiplyScalar(speed * (0.25 + R() * 0.2)).addScaledVector(up, 2.4 + R() * 2.6).addScaledVector(right, (R() - 0.5) * 1.8);
    const p = origin.clone().addScaledVector(v, t); p.y += -4.9 * t * t;
    if (p.y < 0.02) continue;
    out.push({ p, size: 0.025 + t * 0.2 + R() * 0.04, alpha: (0.22 + R() * 0.35) * (1 - t / 0.8) });
  }
  // abanicos laterales desde la proa (más fuerte por fuera de la curva)
  for (const s of [-1, 1]) {
    const k = s === Math.sign(turn) ? 0.5 : 1.25;
    for (let i = 0; i < 1500 * k; i++) {
      const t = R() * 0.5, along = R();
      const base = origin.clone().addScaledVector(fwd, 0.7 + along * 1.6).addScaledVector(right, s * 0.55);
      const v = right.clone().multiplyScalar(s * (2.2 + R() * 3.2) * k).addScaledVector(up, 1.4 + R() * 2.2).addScaledVector(back, speed * 0.15);
      const p = base.addScaledVector(v, t); p.y += -4.9 * t * t;
      if (p.y < 0.02) continue;
      out.push({ p, size: 0.02 + t * 0.16 + R() * 0.03, alpha: (0.25 + R() * 0.35) * (1 - t / 0.55) });
    }
  }
  return out;
}
