// Recolorea la foto de una moto por zonas (color principal, partes oscuras, partes claras)
// conservando luces, sombras y logos. p = {main, dark, light} (cada uno '#rrggbb' o null = original)
function paintPhoto(img, p) {
  const w = img.naturalWidth || img.width, h = img.naturalHeight || img.height;
  const c = document.createElement('canvas'); c.width = w; c.height = h;
  const g = c.getContext('2d'); g.drawImage(img, 0, 0);
  if (!p || (!p.main && !p.dark && !p.light)) return c;
  const d = g.getImageData(0, 0, w, h), a = d.data, n = w * h;
  const hx = (s) => [parseInt(s.slice(1, 3), 16), parseInt(s.slice(3, 5), 16), parseInt(s.slice(5, 7), 16)];
  const lumOf = (r, gg, b) => (r * .299 + gg * .587 + b * .114) / 255;
  const S = new Float32Array(n), Lm = new Float32Array(n);
  // 1) saturación y luminancia de cada píxel
  for (let i = 0, j = 0; i < n; i++, j += 4) {
    const r = a[j], gg = a[j + 1], b = a[j + 2], mx = Math.max(r, gg, b), mn = Math.min(r, gg, b);
    S[i] = mx ? (mx - mn) / mx : 0; Lm[i] = lumOf(r, gg, b);
  }
  const Lb = new Float32Array(n);
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) { let t = 0, c2 = 0; for (let dy = -2; dy <= 2; dy++) { const yy = y + dy; if (yy < 0 || yy >= h) continue; for (let dx = -2; dx <= 2; dx++) { const xx = x + dx; if (xx < 0 || xx >= w) continue; const q = yy * w + xx; t += Lm[q]; c2++; } } Lb[y * w + x] = t / c2; }
  // 2) luminancia de referencia de cada zona (mediana aproximada)
  const med = (sel) => { const hst = new Uint32Array(64); let t = 0; for (let i = 0, j = 0; i < n; i++, j += 4) { if (a[j + 3] < 128 || !sel(i)) continue; hst[Math.min(63, (Lm[i] * 64) | 0)]++; t++; } let acc = 0; for (let k = 0; k < 64; k++) { acc += hst[k]; if (acc >= t / 2) return (k + .5) / 64; } return .5; };
  const isMain = (i) => S[i] > .32 && Lm[i] > .12, isDark = (i) => S[i] < .22 && Lm[i] < .42, isLight = (i) => S[i] < .22 && Lm[i] >= .42;
  const ref = { main: med(isMain), dark: med(isDark), light: med(isLight) };
  const T = { main: p.main && hx(p.main), dark: p.dark && hx(p.dark), light: p.light && hx(p.light) };
  const tl = (t) => lumOf(t[0], t[1], t[2]);
  const shade = (t, l, lr, out, j, wgt) => {
    // misma luz relativa: más oscuro que la referencia -> escala; más claro -> hacia blanco
    const lt = Math.max(.04, tl(t)), damp = Math.abs(lt - lr) > .35 ? .45 : 1; let k = 1 + (l / lr - 1) * damp, r, gg, b; l = lr * k;
    if (k <= 1) { const s = Math.max(.08, k); r = t[0] * s; gg = t[1] * s; b = t[2] * s; }
    else { const u = Math.min(1, (l - lr) / Math.max(.05, 1 - lr)); r = t[0] + (255 - t[0]) * u; gg = t[1] + (255 - t[1]) * u; b = t[2] + (255 - t[2]) * u; }
    // conserva el contraste de la foto cuando el color destino es muy oscuro o muy claro
    if (lt < .15 || lt > .85) { const f = .5 + l; r *= f; gg *= f; b *= f; }
    out[j] = out[j] * (1 - wgt) + Math.min(255, r) * wgt; out[j + 1] = out[j + 1] * (1 - wgt) + Math.min(255, gg) * wgt; out[j + 2] = out[j + 2] * (1 - wgt) + Math.min(255, b) * wgt;
  };
  for (let i = 0, j = 0; i < n; i++, j += 4) {
    if (a[j + 3] < 8) continue;
    const s = S[i], l = Lm[i];
    // pesos suaves entre zonas para que no se vean bordes
    const wm = Math.min(1, Math.max(0, (s - .22) / .14)) * (l > .1 ? 1 : 0);
    const wn = 1 - wm;
    const wd = wn * Math.min(1, Math.max(0, (.48 - l) / .12)), wl = wn - wd;
    if (T.main && wm > 0) shade(T.main, l, ref.main, a, j, wm);
    const lb = l * .35 + Lb[i] * .65;
    if (T.dark && wd > 0) shade(T.dark, lb, ref.dark, a, j, wd);
    if (T.light && wl > 0) shade(T.light, lb, ref.light, a, j, wl);
  }
  g.putImageData(d, 0, 0);
  return c;
}
if (typeof module !== 'undefined') module.exports = { paintPhoto };
