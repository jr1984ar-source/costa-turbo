// Pinta la foto de una moto por piezas usando su mapa de piezas (1 casco, 2 laterales, 3 capó, 4 rayas, 5 asiento).
// P = {1:'#rrggbb',...}; las piezas sin color se dejan como en la foto. Conserva luces, sombras y logos.
var WHITE_REF = [0.45, 0.639, 0.699, 0.727, 0.735, 0.748, 0.762, 0.776, 0.784, 0.795, 0.8, 0.808, 0.817, 0.831, 0.843, 0.855, 0.863, 0.872, 0.882, 0.886, 0.894, 0.898, 0.906, 0.91, 0.914, 0.918, 0.922, 0.925, 0.933, 0.937, 0.941, 0.953, 1.0];
function paintParts(img, mk, P) {
  const w = img.naturalWidth || img.width, h = img.naturalHeight || img.height;
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  const g = c.getContext('2d'); g.drawImage(img, 0, 0);
  const ks = P ? Object.keys(P).filter(k => P[k]) : [];
  if (!ks.length) return c;
  const d = g.getImageData(0, 0, w, h), a = d.data, n = w * h;
  const mc = document.createElement('canvas'); mc.width = w; mc.height = h; const mg = mc.getContext('2d'); mg.drawImage(mk, 0, 0, w, h);
  const md = mg.getImageData(0, 0, w, h).data, lab = new Uint8Array(n);
  for (let i = 0; i < n; i++) lab[i] = Math.round(md[i * 4] / 40);
  const lumOf = (r, gg, b) => (r * .299 + gg * .587 + b * .114) / 255;
  const Lm = new Float32Array(n); for (let i = 0, j = 0; i < n; i++, j += 4) Lm[i] = lumOf(a[j], a[j + 1], a[j + 2]);
  // luminancia suavizada (quita grano al aclarar)
  const Lb = new Float32Array(n);
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) { let t = 0, q = 0; for (let dy = -2; dy <= 2; dy++) { const yy = y + dy; if (yy < 0 || yy >= h) continue; for (let dx = -2; dx <= 2; dx++) { const xx = x + dx; if (xx < 0 || xx >= w) continue; t += Lm[yy * w + xx]; q++; } } Lb[y * w + x] = t / q; }
  const hx = (s) => [parseInt(s.slice(1, 3), 16), parseInt(s.slice(3, 5), 16), parseInt(s.slice(5, 7), 16)];
  for (const k of ks) {
    const K = +k, T = hx(P[k]), lt = Math.max(.04, lumOf(T[0], T[1], T[2]));
    // peso suave de la pieza (borde difuminado 1 px)
    const W8 = new Float32Array(n);
    for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) { let t = 0, q = 0; for (let dy = -1; dy <= 1; dy++) { const yy = y + dy; if (yy < 0 || yy >= h) continue; for (let dx = -1; dx <= 1; dx++) { const xx = x + dx; if (xx < 0 || xx >= w) continue; q++; if (lab[yy * w + xx] === K) t++; } } W8[y * w + x] = t / q; }
    // luz de referencia de la pieza (mediana)
    const hst = new Uint32Array(64); let tot = 0; for (let i = 0; i < n; i++) if (lab[i] === K) { hst[Math.min(63, (Lm[i] * 64) | 0)]++; tot++; }
    if (!tot) continue; let acc = 0, lr = .5; for (let b = 0; b < 64; b++) { acc += hst[b]; if (acc >= tot / 2) { lr = (b + .5) / 64; break; } }
    const damp = Math.abs(lt - lr) > .35 ? .5 : .9;
    // blanco o casi blanco: reparte la luz como en la Yamaha blanca (brillos y sombras de verdad)
    const light = lt > .7;
    let cdf = null;
    if (light) { const hb = new Float32Array(256); let tt = 0; for (let i = 0; i < n; i++) if (lab[i] === K) { hb[Math.min(255, (Lb[i] * 255) | 0)]++; tt++; } cdf = new Float32Array(256); let ac = 0; for (let b = 0; b < 256; b++) { ac += hb[b]; cdf[b] = ac / tt; } }
    const refQ = (p) => { const f = p * 32, i0 = Math.min(31, Math.floor(f)), t = f - i0; return WHITE_REF[i0] + (WHITE_REF[i0 + 1] - WHITE_REF[i0]) * t; };
    for (let i = 0, j = 0; i < n; i++, j += 4) {
      const wt = W8[i]; if (wt <= 0 || a[j + 3] < 8) continue;
      let r, gg, b;
      if (light) { const lv = Lm[i] * .3 + Lb[i] * .7, p = cdf[Math.min(255, (lv * 255) | 0)], lo = refQ(p), s2 = lo / .9; r = Math.min(255, T[0] * s2); gg = Math.min(255, T[1] * s2); b = Math.min(255, T[2] * s2); a[j] = a[j] * (1 - wt) + r * wt; a[j + 1] = a[j + 1] * (1 - wt) + gg * wt; a[j + 2] = a[j + 2] * (1 - wt) + b * wt; continue; }
      const kk = 1 + (Lm[i] / lr - 1) * damp, l = lr * kk;
      if (kk <= 1) { const s = Math.max(.1, kk); r = T[0] * s; gg = T[1] * s; b = T[2] * s; }
      else { const u = Math.min(1, (l - lr) / Math.max(.05, 1 - lr)) * .85; r = T[0] + (255 - T[0]) * u; gg = T[1] + (255 - T[1]) * u; b = T[2] + (255 - T[2]) * u; }
      if (lt < .12) { const f = .55 + Lm[i] * .9; r = Math.max(r, 30 * f); gg = Math.max(gg, 32 * f); b = Math.max(b, 36 * f); }
      a[j] = a[j] * (1 - wt) + r * wt; a[j + 1] = a[j + 1] * (1 - wt) + gg * wt; a[j + 2] = a[j + 2] * (1 - wt) + b * wt;
    }
  }
  g.putImageData(d, 0, 0);
  return c;
}
if (typeof module !== 'undefined') module.exports = { paintParts };
