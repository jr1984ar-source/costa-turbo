// Paisaje de tierra adentro (EL PUERTO): montañas, colinas, acantilados con calas, pueblo blanco, hoteles, villas, carreteras y pinares
import * as THREE from 'three';
import { mergeGeometries } from 'three/addons/utils/BufferGeometryUtils.js';
import { smooth, fbm, rng } from './noise.js';
import { coastZ, heightAt } from './world.js?v=5';

const sm = smooth;
// distancia a la orilla (sin la isla del mar): + tierra adentro
const dco = (x, z) => (z - coastZ(x)) * 0.85 + (fbm(x * 0.02, z * 0.02, 3) - 0.5) * 9;
// acantilados: tramo oeste (con dos calas) y cabos a los dos lados de la bahía (con más calas)
function cliffK(x) {
  const ax = Math.abs(x);
  let c = Math.max(sm(-150, -190, x) * sm(-318, -296, x), sm(360, 430, ax));
  const cove = Math.exp(-(((x + 208) / 15) ** 2)) + Math.exp(-(((x + 265) / 12) ** 2)) + Math.exp(-(((ax - 520) / 20) ** 2)) + Math.exp(-(((ax - 650) / 16) ** 2));
  return c * (1 - Math.min(1, cove * 1.15));
}
// el pueblo blanco sube por la colina del puerto
const villK = x => sm(165, 235, x) * sm(470, 410, x);
function bump(x, z) {
  const d = dco(x, z);
  if (d < -6) return 0;
  const c = cliffK(x);
  let b = c * (sm(-3, 2.5, d) * .78 + sm(2, 16, d) * .22) * (24 + 16 * fbm(x * 0.01 + 4, z * 0.01, 3)) + c * sm(-3, 3, d) * (fbm(x * 0.09, z * 0.09, 4) - 0.5) * 9;   // pared de roca
  b += villK(x) * sm(30, 120, d) * 34;                                                      // colina del pueblo
  b += sm(45, 230, d) * (12 + 34 * fbm(x * 0.006 + 3, z * 0.006, 4));                     // colinas
  let r = 1 - Math.abs(2 * fbm(x * 0.0016 + 11, z * 0.0016 - 4, 5) - 1); r *= r;
  b += sm(220, 1300, d) * (110 + 420 * r) + sm(150, 700, d) * 70 * fbm(x * 0.004, z * 0.004, 4);   // sierra con crestas
  return b;
}
export const landH = (x, z) => heightAt(x, z) - 0.4 + bump(x, z);

// ---------- texturas de fachada (4 m de ancho x 3 m de alto por cuadro) ----------
function canvasTex(w, h, draw) { const c = document.createElement('canvas'); c.width = w; c.height = h; draw(c.getContext('2d'), w, h); const t = new THREE.CanvasTexture(c); t.wrapS = t.wrapT = THREE.RepeatWrapping; t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return t; }
function speck(x, w, h, a) { for (let i = 0; i < 900; i++) { x.fillStyle = `rgba(${Math.random() < .5 ? '0,0,0' : '255,255,255'},${Math.random() * a})`; x.fillRect(Math.random() * w, Math.random() * h, 2, 2); } }
function houseTex(wall, shut) { return canvasTex(256, 192, (x, w, h) => { x.fillStyle = wall; x.fillRect(0, 0, w, h); speck(x, w, h, .05);
  x.fillStyle = 'rgba(0,0,0,.08)'; x.fillRect(0, h - 10, w, 10);                                   // zócalo
  x.fillStyle = '#1d262e'; x.fillRect(104, 46, 48, 86); x.fillStyle = 'rgba(160,190,210,.35)'; x.fillRect(108, 50, 18, 78);   // ventana
  x.fillStyle = shut; for (const sx of [74, 154]) { x.fillRect(sx, 44, 28, 90); x.fillStyle = 'rgba(0,0,0,.22)'; for (let k = 48; k < 132; k += 7) x.fillRect(sx + 2, k, 24, 2); x.fillStyle = shut; }
  x.fillStyle = '#f4f2ec'; x.fillRect(98, 132, 60, 6); }); }
function hotelTex(wall, glass, rail) { return canvasTex(256, 192, (x, w, h) => { x.fillStyle = wall; x.fillRect(0, 0, w, h); speck(x, w, h, .04);
  const g = x.createLinearGradient(0, 22, 0, 172); g.addColorStop(0, glass); g.addColorStop(1, '#0e1822'); x.fillStyle = g; x.fillRect(16, 22, 224, 150);
  x.fillStyle = 'rgba(255,255,255,.18)'; x.fillRect(16, 22, 224, 10); x.fillStyle = 'rgba(0,0,0,.35)'; x.fillRect(126, 22, 4, 150);
  x.fillStyle = rail; x.fillRect(8, 112, 240, 60); x.fillStyle = '#e8ecef'; x.fillRect(8, 108, 240, 6);     // barandilla de cristal
  x.fillStyle = '#d9dcdf'; x.fillRect(0, 172, w, 20); x.fillStyle = 'rgba(0,0,0,.25)'; x.fillRect(0, 172, w, 3); }); }
function signTex(txt, bg, fg) { const t = canvasTex(1024, 192, (x, w, h) => { x.fillStyle = bg; x.fillRect(0, 0, w, h); x.fillStyle = fg; x.font = 'italic 900 128px "Saira Condensed", "Arial Narrow", Arial'; x.textAlign = 'center'; x.textBaseline = 'middle'; x.fillText(txt, w / 2, h / 2 + 6); }); t.wrapS = t.wrapT = THREE.ClampToEdgeWrapping; return t; }

// caja con la fachada repetida a escala real; techo y suelo de color liso
function boxGeo(w, h, d) { const g = new THREE.BoxGeometry(w, h, d), uv = g.attributes.uv, dims = [[d, h], [d, h], null, null, [w, h], [w, h]];
  for (let f = 0; f < 6; f++) for (let k = 0; k < 4; k++) { const i = f * 4 + k; if (!dims[f]) uv.setXY(i, .02, .92); else uv.setXY(i, uv.getX(i) * dims[f][0] / 4, uv.getY(i) * dims[f][1] / 3); }
  return g; }
const plain = (w, h, d) => { const g = new THREE.BoxGeometry(w, h, d), uv = g.attributes.uv; for (let i = 0; i < uv.count; i++) uv.setXY(i, .02, .92); return g; };   // zócalo liso hasta el suelo
const put = (g, x, y, z, ry) => g.applyMatrix4(new THREE.Matrix4().makeRotationY(ry)).translate(x, y, z);

export function buildLand({ pineless = false } = {}) {
  const root = new THREE.Group(), R = rng(2026);
  const TL = new THREE.TextureLoader(), lt = (f, srgb) => { const t = TL.load('assets/tex/' + f); t.wrapS = t.wrapT = THREE.RepeatWrapping; t.anisotropy = 8; if (srgb) t.colorSpace = THREE.SRGBColorSpace; return t; };
  const tG = lt('aerial_grass_rock_Diffuse_2k.jpg', 1), tR = lt('aerial_rocks_02_Diffuse_2k.jpg', 1);

  // ---------- relieve: malla fina cerca y malla gruesa para la sierra lejana ----------
  const NX0 = -460, NX1 = 460, NZ0 = -40, NZ1 = 500;
  const terrain = (x0, x1, z0, z1, sx, sz, far) => {
    const g = new THREE.PlaneGeometry(x1 - x0, z1 - z0, sx, sz); g.rotateX(-Math.PI / 2); g.translate((x0 + x1) / 2, 0, (z0 + z1) / 2);
    const p = g.attributes.position, n = p.count, rock = new Float32Array(n), col = new Float32Array(n * 3), D = new Float32Array(n);
    for (let i = 0; i < n; i++) { const x = p.getX(i), z = p.getZ(i); let y = landH(x, z);
      if (far && x > NX0 + 30 && x < NX1 - 30 && z < NZ1 - 30) y -= 25;   // debajo de la malla fina
      p.setY(i, y); D[i] = dco(x, z); }
    g.computeVertexNormals(); const nr = g.attributes.normal;
    for (let i = 0; i < n; i++) { const x = p.getX(i), z = p.getZ(i), y = p.getY(i), d = D[i], ny = nr.getY(i);
      const slope = 1 - ny, cl = cliffK(x) * sm(-3, 3, d);
      let rk = Math.max(sm(.35, .6, slope) * .85, cl * sm(.12, .3, slope), sm(520, 760, y) * .6);
      const v = fbm(x * .008 + 9, z * .008, 3), v2 = fbm(x * .05, z * .05, 2);
      // matorral mediterráneo: verde oliva con manchas secas y pinar más oscuro
      let c = [.34 + .1 * v, .39 + .07 * v, .21 + .04 * v];
      const forest = sm(.5, .62, fbm(x * .006 - 7, z * .006 + 2, 4)) * sm(60, 120, d);
      c = c.map((k, j) => k * (1 - forest * .45) + [.15, .22, .10][j] * forest * .45);
      const dry = sm(.55, .7, v2) * .5; c = c.map((k, j) => k * (1 - dry) + [.58, .51, .36][j] * dry);
      const sand = (1 - sm(30, 70, d)) * (1 - cliffK(x)); c = c.map((k, j) => k * (1 - sand) + [.82, .64, .42][j] * sand);   // une con la arena de la playa
      const rc = [.44 + .12 * v2, .42 + .1 * v2, .39 + .08 * v2];                                         // roca caliza
      c = c.map((k, j) => k * (1 - rk) + rc[j] * rk);
      col.set(c.map(k => Math.pow(k, 2.2)), i * 3); rock[i] = rk; }
    g.setAttribute('color', new THREE.BufferAttribute(col, 3)); g.setAttribute('aRock', new THREE.BufferAttribute(rock, 1));
    const m = new THREE.MeshStandardMaterial({ vertexColors: true, roughness: .95 });
    m.onBeforeCompile = sh => { sh.uniforms.tG = { value: tG }; sh.uniforms.tR = { value: tR };
      sh.vertexShader = sh.vertexShader.replace('#include <common>', '#include <common>\nattribute float aRock; varying float vRock; varying vec3 vWP; varying vec3 vWN;')
        .replace('#include <project_vertex>', '#include <project_vertex>\nvRock = aRock; vWP = (modelMatrix * vec4(transformed, 1.0)).xyz; vWN = normalize(mat3(modelMatrix) * objectNormal);');
      sh.fragmentShader = sh.fragmentShader.replace('#include <common>', `#include <common>
uniform sampler2D tG; uniform sampler2D tR; varying float vRock; varying vec3 vWP; varying vec3 vWN;
vec3 relT(sampler2D t, vec2 uv){ vec3 a = textureLod(t, vec2(.5), 12.).rgb; return clamp(texture2D(t, uv).rgb / max(a, vec3(.02)), .3, 2.2); }`)
        .replace('#include <color_fragment>', `#include <color_fragment>
{ vec3 bw = pow(abs(normalize(vWN)), vec3(4.)); bw /= bw.x + bw.y + bw.z;
  vec3 r = relT(tR, vWP.zy / 9.) * bw.x + relT(tR, vWP.xz / 9.) * bw.y + relT(tR, vWP.xy / 9.) * bw.z;
  vec3 g = mix(relT(tG, vWP.xz / 16.), relT(tG, vWP.xz / 61. + .3), .5);
  float dist = length(cameraPosition - vWP); float k = 1. - smoothstep(500., 2200., dist);
  diffuseColor.rgb *= mix(vec3(1.), mix(g, r, vRock), .85 * k); }`); };
    const mesh = new THREE.Mesh(g, m); mesh.receiveShadow = true; root.add(mesh); return mesh; };
  terrain(NX0, NX1, NZ0, NZ1, 368, 216, false);
  terrain(-3600, 3600, -120, 3900, 300, 168, true);

  const taken = [];                 // [x, z, r] ocupado por edificios
  const free = (x, z, r) => taken.every(([a, b, q]) => (a - x) ** 2 + (b - z) ** 2 > (q + r) ** 2);
  const baseY = (x, z, w, d, ry) => { let lo = Infinity, hi = -Infinity; const c = Math.cos(ry), s = Math.sin(ry);
    for (const [a, b] of [[0, 0], [w / 2, d / 2], [-w / 2, d / 2], [w / 2, -d / 2], [-w / 2, -d / 2]]) { const y = landH(x + a * c + b * s, z - a * s + b * c); lo = Math.min(lo, y); hi = Math.max(hi, y); } return [lo, hi]; };
  const faceSea = (x, z) => { const e = 2, dz = coastZ(x + e) - coastZ(x - e), L = Math.hypot(2 * e, dz), nx = dz / L, nz = -2 * e / L; return Math.atan2(-nx, -nz); };   // la fachada principal mira al mar

  // ---------- carreteras ----------
  const roads = [];
  const roadMat = new THREE.MeshStandardMaterial({ roughness: .85, map: canvasTex(64, 256, (x, w, h) => { x.fillStyle = '#3a3c3f'; x.fillRect(0, 0, w, h); speck(x, w, h, .12); x.fillStyle = '#e9e6dc'; x.fillRect(30, 0, 4, 120); x.fillRect(1, 0, 2, h); x.fillRect(w - 3, 0, 2, h); }) });
  function road(pts, wid = 7) {
    const pos = [], uv = [], idx = []; let s = 0;
    for (let i = 0; i < pts.length; i++) { const [x, z] = pts[i], [ax, az] = pts[Math.max(0, i - 1)], [bx, bz] = pts[Math.min(pts.length - 1, i + 1)], L = Math.hypot(bx - ax, bz - az) || 1, nx = -(bz - az) / L, nz = (bx - ax) / L;
      if (i) s += Math.hypot(x - pts[i - 1][0], z - pts[i - 1][1]);
      const yc = landH(x, z); for (const sd of [-1, 1]) { const px = x + nx * sd * wid / 2, pz = z + nz * sd * wid / 2; pos.push(px, Math.max(yc, landH(px, pz)) + .18, pz); uv.push(sd < 0 ? 0 : 1, s / 8); }
      if (i) { const k = i * 2; idx.push(k - 2, k, k - 1, k - 1, k, k + 1); }
      roads.push([x, z]); }
    const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setAttribute('uv', new THREE.Float32BufferAttribute(uv, 2)); g.setIndex(idx); g.computeVertexNormals();
    const m = new THREE.Mesh(g, roadMat); m.receiveShadow = true; root.add(m); }
  { const a = []; for (let x = -175; x <= 470; x += 4) a.push([x, coastZ(x) + 62 + 6 * Math.sin(x * .02)]); road(a); }                 // carretera de la costa, detrás de la playa
  { const a = []; let x = 236, z = coastZ(236) + 62; for (let k = 0; k < 120; k++) { a.push([x, z]); z += 2.2; x = 236 + 34 * Math.sin(k * .09); } road(a, 6); }     // sube al pueblo en curvas
  { const a = []; for (let k = 0; k < 220; k++) { const z = coastZ(-20) + 62 + k * 2.4, x = -20 + 46 * Math.sin(k * .055) + k * .25; a.push([x, z]); } road(a, 6); }    // sube a la montaña
  const nearRoad = (x, z, r) => roads.some(([a, b]) => (a - x) ** 2 + (b - z) ** 2 < r * r);

  // ---------- edificios ----------
  const MAT = {
    house: [houseTex('#f6f3ec', '#2f6fb0'), houseTex('#f3efe5', '#3f7d4a'), houseTex('#fbf8f2', '#7a5131'), houseTex('#f1e6d2', '#2e5f8c')].map(t => new THREE.MeshStandardMaterial({ map: t, roughness: .9 })),
    hotel: [hotelTex('#f2f2ee', '#3b6f95', 'rgba(210,235,245,.35)'), hotelTex('#efe4cf', '#2c5a78', 'rgba(255,255,255,.3)'), hotelTex('#e9d3bd', '#355d72', 'rgba(220,240,250,.3)'), hotelTex('#ffffff', '#1f4f73', 'rgba(255,255,255,.4)')].map(t => new THREE.MeshStandardMaterial({ map: t, roughness: .6, metalness: .05 })),
    roof: new THREE.MeshStandardMaterial({ color: 0xb4572f, roughness: .85 }),
    pool: new THREE.MeshStandardMaterial({ color: 0x23b5d8, roughness: .08, emissive: 0x06303a }),
  };
  const bins = new Map(); const bin = (m, g) => { if (!bins.has(m)) bins.set(m, []); bins.get(m).push(g); };

  // pueblo blanco en la colina del puerto
  let nh = 0;
  for (let i = 0; i < 9000 && nh < 260; i++) { const x = 172 + R() * 290, z = coastZ(x) + 40 + R() * 190, dd = dco(x, z);
    if (villK(x) < .5 || dd < 36 || dd > 230 || nearRoad(x, z, 9)) continue;
    const w = 4 * (1 + (R() * 3 | 0)), d = 4 * (1 + (R() * 2.4 | 0)), fl = 1 + (R() * 2.6 | 0), r = Math.hypot(w, d) / 2 + .4;
    if (!free(x, z, r)) continue; const ry = faceSea(x, z) + (R() - .5) * .3, [lo, hi] = baseY(x, z, w, d, ry); if (hi - lo > 7) continue;
    const drop = Math.ceil((hi - lo + .5) / 3) * 3, h = fl * 3 + drop, mi = (R() * 4) | 0;
    bin(MAT.house[mi], put(boxGeo(w, fl * 3, d), x, hi + fl * 1.5 + .4, z, ry)); bin(MAT.house[mi], put(plain(w, drop + .4, d), x, hi - drop / 2 + .2, z, ry));
    const top = hi + fl * 3 + .4;
    if (R() < .45) { const rf = new THREE.ConeGeometry(1, 1.4 + R() * .8, 4, 1); rf.rotateY(Math.PI / 4); rf.scale(w / Math.SQRT2 + .3, 1, d / Math.SQRT2 + .3); bin(MAT.roof, put(rf, x, top + .7, z, ry)); }
    else bin(MAT.house[mi], put(boxGeo(w + .2, .5, d + .2), x, top + .25, z, ry));
    taken.push([x, z, r]); nh++; }
  // iglesia del pueblo con campanario
  { const x = 300, z = coastZ(300) + 120, ry = faceSea(x, z), [lo, hi] = baseY(x, z, 10, 18, ry), y = lo - 3;
    bin(MAT.house[0], put(boxGeo(10, 12 + hi - lo, 18), x, y + (12 + hi - lo) / 2, z, ry));
    const tx = x + Math.sin(ry) * -7, tz = z + Math.cos(ry) * -7; bin(MAT.house[0], put(boxGeo(4, 24 + hi - lo, 4), tx, y + (24 + hi - lo) / 2, tz, ry));
    const dm = new THREE.SphereGeometry(2.2, 16, 8, 0, Math.PI * 2, 0, Math.PI / 2); bin(MAT.roof, put(dm, tx, y + 24 + hi - lo, tz, 0)); taken.push([x, z, 13]); }

  // hoteles en primera línea detrás de la carretera
  const HN = ['HOTEL MIRAMAR', 'GRAN HOTEL SOL', 'HOTEL AZUL', 'HOTEL LAS OLAS', 'HOTEL PALMERAS'], HC = [['#0b3a66', '#ffffff'], ['#ffd21a', '#0b1630'], ['#1e63d6', '#ffffff'], ['#ffffff', '#0b3a66'], ['#e3202b', '#ffffff']];
  [[-118, 8, 7, 0], [-58, 10, 11, 1], [4, 9, 8, 2], [66, 11, 13, 3], [124, 8, 6, 1]].forEach(([x0, k, fl, mi], i) => {
    const x = x0, z = coastZ(x) + 92 + (i % 2) * 8, w = 4 * k, d = 16, ry = faceSea(x, z), [lo, hi] = baseY(x, z, w, d, ry), drop = Math.ceil((hi - lo + .5) / 3) * 3, h = fl * 3 + drop;
    bin(MAT.hotel[mi], put(boxGeo(w, fl * 3, d), x, hi + fl * 1.5 + .3, z, ry)); bin(MAT.house[0], put(plain(w, drop + .3, d), x, hi - drop / 2 + .15, z, ry));
    const top = hi + fl * 3 + .3; bin(MAT.house[0], put(boxGeo(w + .4, .7, d + .4), x, top + .35, z, ry));
    const sg = new THREE.Mesh(new THREE.PlaneGeometry(w * .62, w * .62 * 192 / 1024), new THREE.MeshStandardMaterial({ map: signTex(HN[i], HC[i][0], HC[i][1]), roughness: .5, emissive: 0x222222 }));
    sg.position.set(x - Math.sin(ry) * (d / 2 + .3), top + 2.4, z - Math.cos(ry) * (d / 2 + .3)); sg.rotation.y = ry + Math.PI; root.add(sg);
    const pw = w * .5, px = x - Math.sin(ry) * (d / 2 + 7), pz = z - Math.cos(ry) * (d / 2 + 7);   // piscina delante del hotel
    bin(MAT.pool, put(new THREE.BoxGeometry(pw, .3, 7), px, landH(px, pz) + .2, pz, ry));
    taken.push([x, z, w / 2 + 6]); });

  // villas blancas con piscina por las colinas
  let nv = 0;
  for (let i = 0; i < 3000 && nv < 34; i++) { const x = -170 + R() * 330, z = coastZ(x) + 130 + R() * 260, dd = dco(x, z);
    if (dd < 120 || nearRoad(x, z, 14) || !free(x, z, 14)) continue;
    const ry = faceSea(x, z) + (R() - .5) * .4, w = 12 + 4 * (R() * 2 | 0), d = 8, [lo, hi] = baseY(x, z, w, d + 8, ry); if (hi - lo > 9) continue;
    const drop = Math.ceil((hi - lo + .5) / 3) * 3, mi = (R() * 4) | 0;
    bin(MAT.hotel[mi], put(boxGeo(w, 3, d), x, hi + 1.8, z, ry)); bin(MAT.house[0], put(plain(w, drop + .3, d), x, hi - drop / 2 + .15, z, ry));
    const ox = (R() - .5) * 4, ux = x + Math.cos(ry) * ox, uz = z - Math.sin(ry) * ox; bin(MAT.house[(mi + 1) % 4], put(boxGeo(w - 4, 3, d - 1), ux, hi + 3 + 1.5 + .3, uz, ry));
    bin(MAT.house[0], put(boxGeo(w - 3.6, .35, d - .6), ux, hi + 6.5, uz, ry));
    const px = x - Math.sin(ry) * (d / 2 + 4), pz = z - Math.cos(ry) * (d / 2 + 4); bin(MAT.pool, put(new THREE.BoxGeometry(w * .6, .4, 4), px, Math.max(hi, landH(px, pz)) + .2, pz, ry));
    taken.push([x, z, 12]); nv++; }
  for (const [m, gs] of bins) { const mesh = new THREE.Mesh(mergeGeometries(gs.map(g => g.index ? g.toNonIndexed() : g)), m); mesh.castShadow = mesh.receiveShadow = true; root.add(mesh); }

  // ---------- pinos piñoneros y cipreses (instanciados) ----------
  if (!pineless) {
    const blob = (sx, sy, sz, ox, oy, oz, sd) => { const g = new THREE.IcosahedronGeometry(1, 2), q = g.attributes.position;
      for (let i = 0; i < q.count; i++) { const x = q.getX(i), y = q.getY(i), z = q.getZ(i), k = .82 + .36 * fbm(x * 2 + sd, z * 2 + y, 2); q.setXYZ(i, x * k * sx + ox, y * k * sy * (y < 0 ? .55 : 1) + oy, z * k * sz + oz); } return g; };
    const crown = mergeGeometries([blob(3.6, 1.5, 3.6, 0, 7.3, 0, 1), blob(2.5, 1.2, 2.5, 2.3, 6.6, 1.1, 5), blob(2.7, 1.25, 2.7, -1.9, 6.8, -1.3, 9), blob(2.2, 1.1, 2.2, -.6, 6.3, 2.2, 13)]); crown.computeVertexNormals();
    const trunk = new THREE.CylinderGeometry(.34, .6, 7, 7); trunk.translate(0, 3.5, 0);
    const cyp = new THREE.ConeGeometry(1.3, 11, 8, 3); cyp.translate(0, 6.2, 0); const cpp = cyp.attributes.position;
    for (let i = 0; i < cpp.count; i++) { const y = cpp.getY(i), k = Math.sin(Math.min(1, (y - .7) / 11) * Math.PI) * .55 + .45 + .1 * Math.random(); cpp.setX(i, cpp.getX(i) * k); cpp.setZ(i, cpp.getZ(i) * k); } cyp.computeVertexNormals();
    const P = [], C = [];
    for (let i = 0; i < 26000 && P.length < 2600; i++) { const x = -1400 + R() * 2800, z = coastZ(x) + 45 + R() * (i % 3 ? 700 : 1600), dd = dco(x, z);
      if (dd < 58) continue; const f = sm(.45, .6, fbm(x * .006 - 7, z * .006 + 2, 4)); if (R() > .12 + f * .88) continue;
      if (!free(x, z, 3) || nearRoad(x, z, 5)) continue; const y = landH(x, z); if (y > 520) continue;
      const e = 2, sl = Math.hypot(landH(x + e, z) - landH(x - e, z), landH(x, z + e) - landH(x, z - e)) / (2 * e); if (sl > .8) continue;
      (R() < .1 && dd < 260 ? C : P).push([x, y - .2, z, .75 + R() * .6, R() * 6.28]); }
    const inst = (geo, mat, L, tint = true) => { const m = new THREE.InstancedMesh(geo, mat, L.length), o = new THREE.Object3D(), c = new THREE.Color();
      L.forEach(([x, y, z, s, r], i) => { o.position.set(x, y, z); o.rotation.set(0, r, 0); o.scale.setScalar(s); o.updateMatrix(); m.setMatrixAt(i, o.matrix); if (tint) c.setHSL(.22 + R() * .07, .32 + R() * .15, .13 + R() * .06); if (tint) m.setColorAt(i, c); });
      m.castShadow = true; m.receiveShadow = true; root.add(m); };
    inst(crown, new THREE.MeshStandardMaterial({ roughness: .95, flatShading: true }), P);
    inst(trunk, new THREE.MeshStandardMaterial({ color: 0x5a3e2b, roughness: .95 }), P, false);
    inst(cyp, new THREE.MeshStandardMaterial({ roughness: .95 }), C);
    { const bush = new THREE.IcosahedronGeometry(1, 1); bush.scale(1.7, 1, 1.7); bush.translate(0, .55, 0); const B = [];   // matorral bajo: lentisco y romero por las laderas
      for (let i = 0; i < 40000 && B.length < 7000; i++) { const x = -900 + R() * 1800, z = coastZ(x) + 40 + R() * 650, dd = dco(x, z); if (dd < 58) continue;
        if (R() > .25 + .75 * fbm(x * .02 + 3, z * .02, 3)) continue; if (nearRoad(x, z, 4.5) || !free(x, z, 1.5)) continue; B.push([x, landH(x, z) - .25, z, .6 + R() * 1.1, R() * 6.28]); }
      inst(bush, new THREE.MeshStandardMaterial({ roughness: 1, flatShading: true }), B); }
  }
  root.userData.blocks = taken;
  return root;
}
