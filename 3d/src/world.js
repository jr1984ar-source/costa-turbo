// Mundo: relieve de la costa, terreno con arena procedural, agua y cielo
import * as THREE from 'three';
import { smooth, fbm, rng, GLSL_NOISE } from './noise.js';

export const WORLD = 800;           // metros de lado
const HALF = WORLD / 2;

// ---------- Forma de la costa ----------
export function coastZ(x) {
  return 30 + 38 * Math.sin(x * 0.0062 + 0.4) + 13 * Math.sin(x * 0.017 + 1.3) + 4 * Math.sin(x * 0.051 + 0.2);
}
// Distancia aproximada a la orilla: + tierra, - mar
export function signedDist(x, z) {
  let d = (z - coastZ(x)) * 0.85;
  const ix = x + 130, iz = z + 150, r = Math.hypot(ix, iz), th = Math.atan2(iz, ix);
  const R = 46 * (1 + 0.18 * Math.sin(3 * th + 0.7) + 0.1 * Math.sin(5 * th + 2.1));
  d = Math.max(d, R - r);
  d += (fbm(x * 0.02, z * 0.02, 3) - 0.5) * 9;
  return d;
}
export function heightAt(x, z) {
  const d = signedDist(x, z);
  if (d > 0) {
    return 0.15 + d * 0.045 + smooth(18, 70, d) * (1.0 + 3.2 * fbm(x * 0.015 + 7, z * 0.015 - 3, 4));
  }
  const e = -d;
  let h = 0.15 - (0.03 * e + 8.5 * (1 - Math.exp(-e / 110)));
  h += (fbm(x * 0.03 - 11, z * 0.03 + 5, 3) - 0.5) * 0.6 * Math.min(1, e / 20);
  h += 6.8 * Math.exp(-(((x - 70) / 48) ** 2) - (((z + 40) / 13) ** 2));   // banco de arena
  return h;
}

// Textura RG (altura, distancia a la orilla) para los shaders
export function makeHeightTexture(N = 512) {
  const data = new Uint16Array(N * N * 2);
  const toH = THREE.DataUtils.toHalfFloat;
  for (let j = 0; j < N; j++) {
    const z = -HALF + (j + 0.5) / N * WORLD;
    for (let i = 0; i < N; i++) {
      const x = -HALF + (i + 0.5) / N * WORLD;
      const k = (j * N + i) * 2;
      data[k] = toH(heightAt(x, z));
      data[k + 1] = toH(signedDist(x, z));
    }
  }
  const t = new THREE.DataTexture(data, N, N, THREE.RGFormat, THREE.HalfFloatType);
  t.magFilter = t.minFilter = THREE.LinearFilter;
  t.wrapS = t.wrapT = THREE.ClampToEdgeWrapping;
  t.needsUpdate = true;
  return t;
}

// Mapa de pendientes de oleaje, repetible (suma de ondas)
export function makeWaveTexture(size = 256, seed = 7) {
  const R = rng(seed), waves = [];
  while (waves.length < 40) {
    const kx = Math.round((R() * 2 - 1) * 16), ky = Math.round((R() * 2 - 1) * 16), k = Math.hypot(kx, ky);
    if (k < 2 || k > 16) continue;
    waves.push([kx, ky, 1 / Math.pow(k, 1.45), R() * Math.PI * 2]);
  }
  const sx = new Float32Array(size * size), sy = new Float32Array(size * size);
  let mx = 0;
  for (let y = 0; y < size; y++) for (let x = 0; x < size; x++) {
    let ax = 0, ay = 0; const u = x / size, v = y / size;
    for (const [kx, ky, A, ph] of waves) { const c = Math.cos(2 * Math.PI * (kx * u + ky * v) + ph) * A; ax += c * kx; ay += c * ky; }
    const i = y * size + x; sx[i] = ax; sy[i] = ay; mx = Math.max(mx, Math.abs(ax), Math.abs(ay));
  }
  const data = new Uint8Array(size * size * 4);
  for (let i = 0; i < size * size; i++) {
    data[i * 4] = Math.round((sx[i] / mx * 0.5 + 0.5) * 255);
    data[i * 4 + 1] = Math.round((sy[i] / mx * 0.5 + 0.5) * 255);
    data[i * 4 + 2] = 255; data[i * 4 + 3] = 255;
  }
  const t = new THREE.DataTexture(data, size, size, THREE.RGBAFormat);
  t.wrapS = t.wrapT = THREE.RepeatWrapping;
  t.magFilter = THREE.LinearFilter; t.minFilter = THREE.LinearMipmapLinearFilter;
  t.generateMipmaps = true; t.anisotropy = 8; t.needsUpdate = true;
  return t;
}

// ---------- Ambiente compartido ----------
export function makeEnv(opts = {}) {
  const sunDir = new THREE.Vector3(...(opts.sunDir || [0.55, 0.78, -0.30])).normalize();
  return {
    time: { value: opts.time ?? 12.0 },
    sunDir,
    sunCol: new THREE.Color(1.0, 0.93, 0.82).multiplyScalar(opts.sun ?? 4.2),
    zen: new THREE.Color(0.10, 0.28, 0.70),
    hor: new THREE.Color(0.62, 0.76, 0.90),
    scatter: new THREE.Color(0.0, 0.10, 0.14),
    absorb: new THREE.Vector3(0.52, 0.10, 0.075),
    fogNear: opts.fogNear ?? 260, fogFar: opts.fogFar ?? 900,
  };
}

// ---------- Terreno ----------
// T: texturas reales {dry, dryN, wet, wetN, trk} (Poly Haven, CC0). Se usan como detalle sobre la paleta del juego.
export function makeTerrain(env, hdTex, seg = 400, T = null) {
  const g = new THREE.PlaneGeometry(WORLD, WORLD, seg, seg);
  g.rotateX(-Math.PI / 2);
  const p = g.attributes.position;
  for (let i = 0; i < p.count; i++) p.setY(i, heightAt(p.getX(i), p.getZ(i)));
  g.computeVertexNormals();
  const mat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.93, metalness: 0 });
  mat.onBeforeCompile = (sh) => {
    Object.assign(sh.uniforms, {
      uTime: env.time, uHD: { value: hdTex }, uWorld: { value: WORLD },
      uScatter: { value: env.scatter }, uAbsorb: { value: env.absorb },
      tDry: { value: T.dry }, tDryN: { value: T.dryN }, tWet: { value: T.wet }, tWetN: { value: T.wetN }, tTrk: { value: T.trk },
    });
    sh.vertexShader = sh.vertexShader
      .replace('#include <common>', '#include <common>\nvarying vec3 vWPos; varying vec3 vWN;')
      .replace('#include <project_vertex>', '#include <project_vertex>\nvWPos = (modelMatrix * vec4(transformed, 1.0)).xyz; vWN = normalize(mat3(modelMatrix) * objectNormal);');
    sh.fragmentShader = sh.fragmentShader
      .replace('#include <common>', `#include <common>
uniform float uTime; uniform sampler2D uHD; uniform float uWorld; uniform vec3 uScatter; uniform vec3 uAbsorb;
uniform sampler2D tDry; uniform sampler2D tDryN; uniform sampler2D tWet; uniform sampler2D tWetN; uniform sampler2D tTrk;
varying vec3 vWPos; varying vec3 vWN;
${GLSL_NOISE}
vec3 ct_rel(sampler2D t, vec2 uv){ vec3 a = textureLod(t, vec2(0.5), 12.0).rgb; return clamp(texture2D(t, uv).rgb / max(a, vec3(0.02)), 0.35, 2.2); }
float ct_caustic(vec2 p, float t){
  vec2 i = p; float c = 1.0; float inten = 0.005;
  for (int n = 0; n < 4; n++) {
    float tt = t * (1.0 - (3.5 / float(n + 1)));
    i = p + vec2(cos(tt - i.x) + sin(tt + i.y), sin(tt - i.y) + cos(tt + i.x));
    c += 1.0 / length(vec2(p.x / (sin(i.x + tt) / inten), p.y / (cos(i.y + tt) / inten)));
  }
  c /= 4.0; c = 1.17 - pow(c, 1.4);
  return clamp(pow(abs(c), 8.0), 0.0, 2.0);
}`)
      .replace('#include <color_fragment>', `#include <color_fragment>
{
  vec2 wp = vWPos.xz; float hh = vWPos.y;
  float sd = texture2D(uHD, wp / uWorld + 0.5).g;
  vec2 uA = vec2(wp.x, -wp.y) / 6.0, uB = vec2(wp.x, -wp.y) / 19.0 + 0.37;
  float bl = smoothstep(0.35, 0.65, ct_fbm(wp * 0.03 + 5.0));
  float nL = ct_fbm(wp * 0.018), nM = ct_fbm(wp * 0.11 + 3.1);
  vec3 base = mix(vec3(0.66, 0.38, 0.13), vec3(0.80, 0.50, 0.20), smoothstep(0.3, 0.75, nL));
  vec3 rel = mix(ct_rel(tDry, uA), ct_rel(tDry, uB), bl);
  float trkK = smoothstep(0.5, 0.65, ct_fbm(wp * 0.02 + 11.0)) * smoothstep(3.0, 8.0, sd) * (1.0 - smoothstep(30.0, 50.0, sd));
  rel = mix(rel, ct_rel(tTrk, vec2(wp.x, -wp.y) / 9.0), trkK * 0.8);
  vec3 sandC = base * mix(vec3(1.0), rel, 0.85);
  sandC = mix(sandC, sandC * vec3(0.80, 0.74, 0.62), smoothstep(25.0, 70.0, sd) * smoothstep(0.42, 0.62, nM));
  float wetK = 1.0 - smoothstep(0.05, 0.45, hh);
  vec3 wetC = vec3(0.42, 0.26, 0.11) * mix(vec3(1.0), ct_rel(tWet, vec2(wp.x, -wp.y) / 5.0), 0.7);
  sandC = mix(sandC, wetC, wetK * 0.8);
  if (hh < 0.0) {
    float dep = -hh;
    vec3 bed = vec3(0.72, 0.56, 0.31) * (0.9 + 0.2 * nL) * mix(vec3(1.0), ct_rel(tDry, vec2(wp.x, -wp.y) / 11.0), 0.9);
    float weed = smoothstep(0.56, 0.66, ct_fbm(wp * 0.022 + 9.0)) * smoothstep(2.5, 5.5, dep);
    bed = mix(bed, vec3(0.05, 0.09, 0.035) * (0.7 + 0.6 * ct_n(wp * 3.0)), weed * 0.9);
    sandC = mix(sandC, bed, smoothstep(0.0, 0.35, dep));
  }
  diffuseColor.rgb = sandC;
}`)
      .replace('#include <normal_fragment_maps>', `#include <normal_fragment_maps>
{
  vec2 wp = vWPos.xz; float hh = vWPos.y;
  vec2 uA = vec2(wp.x, -wp.y) / 6.0, uB = vec2(wp.x, -wp.y) / 19.0 + 0.37;
  float bl = smoothstep(0.35, 0.65, ct_fbm(wp * 0.03 + 5.0));
  vec3 nD = mix(texture2D(tDryN, uA).xyz, texture2D(tDryN, uB).xyz, bl) * 2.0 - 1.0;
  vec3 nW = texture2D(tWetN, vec2(wp.x, -wp.y) / 5.0).xyz * 2.0 - 1.0;
  vec3 nB = texture2D(tDryN, vec2(wp.x, -wp.y) / 11.0).xyz * 2.0 - 1.0;
  float wetK = 1.0 - smoothstep(0.05, 0.45, hh);
  vec3 nt = mix(nD * 1.3, nW * 0.8, wetK);
  nt = mix(nt, nB * 1.1, smoothstep(0.0, 0.3, -hh));
  vec3 wn = normalize(normalize(vWN) + vec3(nt.x, 0.0, -nt.y));
  normal = normalize((viewMatrix * vec4(wn, 0.0)).xyz);
}`)
      .replace('#include <opaque_fragment>', `
{
  float hh = vWPos.y;
  if (hh < 0.0) {
    float dep = -hh;
    vec3 V = normalize(cameraPosition - vWPos);
    float c1 = ct_caustic(mod(vWPos.xz * 0.21, 6.2831853) - 250.0, uTime * 0.55);
    float c2 = ct_caustic(mod(vWPos.xz * 0.13 + 1.7, 6.2831853) - 250.0, uTime * 0.42 + 3.0);
    float ck = min(c1, c2) * 1.5 + 0.22 * (c1 + c2);
    outgoingLight *= 1.0 + ck * 0.75 * exp(-dep * 0.28) * smoothstep(0.0, 0.5, dep);
    outgoingLight += diffuseColor.rgb * 0.55 * smoothstep(0.0, 1.5, dep);
    float path = dep * (1.0 + 1.0 / max(V.y, 0.25));
    vec3 T = exp(-path * uAbsorb);
    outgoingLight = outgoingLight * T + uScatter * (1.0 - T);
  } else {
    // orilla: el agua sube por la arena rápido y baja despacio, cada tramo con su ritmo
    float ph = fract(uTime / 7.0 + ct_n(vWPos.xz * 0.02) * 0.6);                       // mismo ritmo que las olas del agua
    float up = smoothstep(0.0, 0.16, ph), down = 1.0 - smoothstep(0.16, 0.85, ph);
    float sw = 0.015 + 0.24 * min(up, down) * (0.7 + 0.6 * ct_n(vWPos.xz * 0.07));
    float wet = 1.0 - smoothstep(0.0, 0.24, hh);                                       // arena mojada
    outgoingLight *= 1.0 - 0.26 * wet;
    float film = 1.0 - smoothstep(sw - 0.035, sw, hh);                                 // lámina de agua sobre la arena
    outgoingLight = mix(outgoingLight, outgoingLight * vec3(0.74, 0.90, 0.92) + uScatter * 0.16, film * 0.55);
    float lace = smoothstep(0.42, 0.74, ct_n(vWPos.xz * 3.0 + uTime * 0.35) * 0.6 + ct_n(vWPos.xz * 9.0 - uTime * 0.5) * 0.4);
    float lead = (1.0 - smoothstep(0.0, 0.05, abs(hh - sw + 0.012))) * lace * (0.4 + 0.6 * up * (1.0 - 0.6 * (1.0 - down)));
    outgoingLight = mix(outgoingLight, vec3(0.86, 0.90, 0.92), lead * 0.65);         // espuma rota del borde, sin línea blanca dura
  }
}
#include <opaque_fragment>`);
  };
  const m = new THREE.Mesh(g, mat);
  m.receiveShadow = true;
  return m;
}

// ---------- Mar de fondo: olas largas que suben y bajan (misma fórmula en el shader y en la física) ----------
const SW = [[.30, 34, .2, .98], [.17, 19, -.5, .87], [.07, 9, .8, .6]].map(([a, l, dx, dz]) => { const n = Math.hypot(dx, dz), k = 2 * Math.PI / l; return [a, k, dx / n, dz / n, Math.sqrt(9.8 * k)]; });
export function swell(x, z, t) { const off = coastZ(x) - z, f = Math.min(1, Math.max(0, (off - 8) / 37)), ff = f * f * (3 - 2 * f); if (ff <= 0) return [0, 0, 0];
  let h = 0, gx = 0, gz = 0; for (const [a, k, dx, dz, w] of SW) { const ph = k * (x * dx + z * dz) - w * t, c = Math.cos(ph); h += a * Math.sin(ph); gx += a * k * dx * c; gz += a * k * dz * c; }
  return [h * ff, gx * ff, gz * ff]; }
const SWGL = SW.map(([a, k, dx, dz, w]) => `{ float ph = ${k.toFixed(5)} * dot(p, vec2(${dx.toFixed(4)}, ${dz.toFixed(4)})) - ${w.toFixed(5)} * t; float c = cos(ph); h += ${a.toFixed(3)} * sin(ph); g += ${(a * k).toFixed(5)} * vec2(${dx.toFixed(4)}, ${dz.toFixed(4)}) * c; }`).join(' ');

// ---------- Agua ----------
export function makeWater(env, hdTex, waveTex) {
  const mat = new THREE.ShaderMaterial({
    transparent: true, depthWrite: false,
    blending: THREE.CustomBlending, blendEquation: THREE.AddEquation,
    blendSrc: THREE.OneFactor, blendDst: THREE.OneMinusSrcAlphaFactor,
    blendSrcAlpha: THREE.OneFactor, blendDstAlpha: THREE.OneMinusSrcAlphaFactor,
    uniforms: {
      uTime: env.time, uHD: { value: hdTex }, uNrm: { value: waveTex }, uWorld: { value: WORLD },
      uSunDir: { value: env.sunDir }, uSunCol: { value: env.sunCol },
      uZen: { value: env.zen }, uHor: { value: env.hor }, uScatter: { value: env.scatter },
      uFogNear: { value: env.fogNear }, uFogFar: { value: env.fogFar },
      uSky: { value: env.skyTex || null }, uSkyOn: { value: env.skyTex ? 1 : 0 }, uSkyRot: { value: env.skyRot || new THREE.Matrix3() }, uSkyK: { value: env.skyK ?? 1 },
      uOuter: { value: 0 },
    },
    vertexShader: /* glsl */`
      uniform float uTime; uniform sampler2D uHD; uniform float uWorld; uniform float uOuter;
      varying vec3 vWPos; varying vec2 vSg;
      void main(){ vec4 w = modelMatrix * vec4(position, 1.0); vSg = vec2(0.0);
        if (uOuter < 0.5) { vec2 p = w.xz, huv = p / uWorld + 0.5; float off = -texture2D(uHD, clamp(huv, 0.001, 0.999)).g; float f = smoothstep(8.0, 45.0, off);
          float t = uTime, h = 0.0; vec2 g = vec2(0.0);
          ${SWGL}
          w.y += h * f; vSg = g * f; }
        vWPos = w.xyz; gl_Position = projectionMatrix * viewMatrix * w; }`,
    fragmentShader: /* glsl */`
      uniform float uTime; uniform sampler2D uHD; uniform sampler2D uNrm; uniform float uWorld;
      uniform vec3 uSunDir; uniform vec3 uSunCol; uniform vec3 uZen; uniform vec3 uHor; uniform vec3 uScatter;
      uniform float uFogNear; uniform float uFogFar; uniform sampler2D uSky; uniform float uSkyOn; uniform mat3 uSkyRot; uniform float uSkyK; uniform float uOuter;
      varying vec3 vWPos; varying vec2 vSg;
      ${GLSL_NOISE}
      vec3 skyCol(vec3 d){ float t = clamp(d.y, 0.0, 1.0); vec3 g = mix(uHor, uZen, pow(t, 0.45));
        if (uSkyOn < 0.5) return g; vec3 r = uSkyRot * d; r.y = max(r.y, 0.02); r = normalize(r);
        vec2 uv = vec2(atan(r.z, r.x) * 0.15915494 + 0.5, asin(clamp(r.y, -1.0, 1.0)) * 0.31830989 + 0.5);
        return texture2D(uSky, uv).rgb * uSkyK; }
      void main(){
        vec2 wp = vWPos.xz;
        if (uOuter > 0.5 && abs(wp.x) < uWorld * 0.5 - 1.0 && abs(wp.y) < uWorld * 0.5 - 1.0) discard;   // el centro lo pinta la malla con olas
        vec2 huv = wp / uWorld + 0.5;
        float inside = step(0.002, huv.x) * step(huv.x, 0.998) * step(0.002, huv.y) * step(huv.y, 0.998);
        vec2 hd = mix(vec2(-30.0, -400.0), texture2D(uHD, huv).rg, inside);
        float dep = max(-hd.x, 0.0), sd = hd.y;
        float calm = 0.35 + 0.65 * smoothstep(0.0, 2.0, dep);
        vec2 s1 = texture2D(uNrm, wp * 0.019 + vec2(uTime * 0.010, uTime * 0.006)).rg * 2.0 - 1.0;
        vec2 s2 = texture2D(uNrm, wp * 0.061 + vec2(-uTime * 0.017, uTime * 0.013)).rg * 2.0 - 1.0;
        vec2 s3 = texture2D(uNrm, wp * 0.21 + vec2(uTime * 0.035, -uTime * 0.030)).rg * 2.0 - 1.0;
        vec2 s4 = texture2D(uNrm, wp * 0.73 + vec2(-uTime * 0.06, -uTime * 0.05)).rg * 2.0 - 1.0;
        vec2 sl = (s1 * 0.26 + s2 * 0.20 + s3 * 0.14 + s4 * 0.08) * calm + vSg;
        vec3 N = normalize(vec3(-sl.x, 1.0, -sl.y));
        vec3 V = normalize(cameraPosition - vWPos);
        float F = 0.02 + 0.98 * pow(1.0 - max(dot(N, V), 0.0), 5.0);
        vec3 R = reflect(-V, N);
        float rs = max(dot(R, uSunDir), 0.0);
        vec3 spec = min(uSunCol * (pow(rs, 3000.0) * 30.0 + pow(rs, 260.0) * 0.25), vec3(24.0));
        vec3 col = skyCol(R) * F + spec;
        float a = clamp(F + dot(spec, vec3(0.05)), 0.0, 1.0);
        // espuma de la orilla
        float fn = ct_n(wp * 0.55 + vec2(uTime * 0.15, 0.0)) * 0.55 + ct_n(wp * 1.9 - uTime * 0.2) * 0.45;
        // oleaje de orilla: crestas que avanzan hacia la playa cada ~7 s, rompen en espuma y dejan un rastro que se deshace
        float n0 = ct_n(wp * 0.02) * 0.6;
        float d0 = max(-sd, 0.0);                                                           // metros mar adentro
        float cyc = fract(uTime / 7.0 + n0);
        float dc = 22.0 * (1.0 - cyc);                                                      // posición de la cresta
        float cw = 0.8 + 0.06 * d0;
        float crest = exp(-pow((d0 - dc) / cw, 2.0)) * (1.0 - smoothstep(14.0, 22.0, d0));
        float brk = smoothstep(10.0, 2.5, d0);                                              // rompe al acercarse
        float trough = exp(-pow((d0 - dc + cw * 1.7) / cw, 2.0)) * (1.0 - smoothstep(14.0, 22.0, d0));
        col *= 1.0 + crest * 0.30 - trough * 0.14;                                          // volumen: cresta clara y seno oscuro delante
        float fe = ct_n(wp * 2.6 + uTime * 0.3) * 0.5 + ct_n(wp * 7.0 - uTime * 0.4) * 0.3 + ct_n(wp * 0.6) * 0.2;
        float lace = smoothstep(0.34, 0.70, fn * 0.5 + fe * 0.5);
        float band = crest * brk * (0.35 + 0.65 * lace);                                   // espuma de la ola rompiendo
        float trail = exp(-max(d0 - dc, 0.0) / 3.5) * step(dc, d0) * brk * lace * (1.0 - cyc * 0.6);   // espuma que queda detrás
        float edge = (1.0 - smoothstep(0.0, 0.10, dep)) * smoothstep(0.38, 0.66, fe);
        float foam = clamp(band * 0.95 + trail * 0.45 + edge * 0.7, 0.0, 1.0);
        vec3 foamCol = vec3(0.95, 0.97, 1.0) * (uSunCol.g * 0.42 + 0.35);
        col = col * (1.0 - foam) + foamCol * foam;
        a = a * (1.0 - foam) + foam;
        // fuera del terreno: mar abierto
        col += uScatter * (1.0 - a) * (1.0 - inside);
        a = mix(1.0, a, inside);
        float fog = smoothstep(uFogNear, uFogFar, length(cameraPosition - vWPos));
        col = col * (1.0 - fog) + uHor * fog;
        a = a * (1.0 - fog) + fog;
        gl_FragColor = vec4(col, a);
      }`,
  });
  const g = new THREE.PlaneGeometry(WORLD, WORLD, 220, 220); g.rotateX(-Math.PI / 2);   // malla con olas en la zona de juego
  const m = new THREE.Mesh(g, mat); m.renderOrder = 2; m.frustumCulled = false;
  const mo = mat.clone(); mo.uniforms = Object.assign({}, mat.uniforms, { uOuter: { value: 1 } });
  const go = new THREE.PlaneGeometry(6000, 6000, 1, 1); go.rotateX(-Math.PI / 2); const outer = new THREE.Mesh(go, mo); outer.renderOrder = 2; m.add(outer);   // mar lejano, plano
  return m;
}

// ---------- Cielo (cúpula visible + mapa de reflejos) ----------
function skyMaterial(env, withSun = true) {
  return new THREE.ShaderMaterial({
    side: THREE.BackSide, depthWrite: false, fog: false,
    uniforms: { uZen: { value: env.zen }, uHor: { value: env.hor }, uSunDir: { value: env.sunDir }, uSunCol: { value: env.sunCol }, uSunK: { value: withSun ? 1 : 0 } },
    vertexShader: `varying vec3 vDir; void main(){ vDir = normalize(position); vec4 p = projectionMatrix * modelViewMatrix * vec4(position, 1.0); gl_Position = p; }`,
    fragmentShader: `uniform vec3 uZen; uniform vec3 uHor; uniform vec3 uSunDir; uniform vec3 uSunCol; uniform float uSunK; varying vec3 vDir;
      void main(){ vec3 d = normalize(vDir); float t = clamp(d.y, 0.0, 1.0);
        vec3 c = mix(uHor, uZen, pow(t, 0.45));
        if (d.y < 0.0) c = mix(uHor, vec3(0.42, 0.36, 0.27), smoothstep(0.0, -0.25, d.y));
        float s = max(dot(d, uSunDir), 0.0);
        c += uSunCol * (pow(s, 900.0) * 8.0 + pow(s, 12.0) * 0.08) * uSunK;
        gl_FragColor = vec4(c, 1.0); }`,
  });
}
export function makeSkyDome(env) {
  const m = new THREE.Mesh(new THREE.SphereGeometry(2500, 32, 16), skyMaterial(env));
  m.renderOrder = -1; m.frustumCulled = false;
  return m;
}
export function makeEnvMap(renderer, env) {
  const s = new THREE.Scene();
  s.add(new THREE.Mesh(new THREE.SphereGeometry(50, 32, 16), skyMaterial(env, false)));
  const pm = new THREE.PMREMGenerator(renderer);
  const rt = pm.fromScene(s, 0.02);
  pm.dispose();
  return rt.texture;
}

// Tiñe de agua la parte sumergida de cualquier objeto (cascos, boyas...)
export function addUnderwater(mat, env) {
  if (mat.userData.uw) return; mat.userData.uw = true;
  mat.onBeforeCompile = (sh) => {
    sh.uniforms.uScatter = { value: env.scatter }; sh.uniforms.uAbsorb = { value: env.absorb };
    sh.vertexShader = sh.vertexShader.replace('#include <common>', '#include <common>\nvarying vec3 vWPosU;')
      .replace('#include <project_vertex>', '#include <project_vertex>\nvWPosU = (modelMatrix * vec4(transformed, 1.0)).xyz;');
    sh.fragmentShader = sh.fragmentShader.replace('#include <common>', '#include <common>\nuniform vec3 uScatter; uniform vec3 uAbsorb; varying vec3 vWPosU;')
      .replace('#include <opaque_fragment>', `if (vWPosU.y < 0.0) { float dep = -vWPosU.y; vec3 V = normalize(cameraPosition - vWPosU);
        float path = dep * (1.0 + 1.0 / max(V.y, 0.25)) + 0.25; vec3 T = exp(-path * uAbsorb);
        outgoingLight = outgoingLight * T + uScatter * (1.0 - T); }
      #include <opaque_fragment>`);
  };
  mat.customProgramCacheKey = () => 'uw';
}
