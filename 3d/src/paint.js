// Pintura de la moto: cambia el turquesa del casco por el color principal y el amarillo de los detalles por el secundario.
import * as THREE from 'three';
const cache = new Map();
function hsv(r, g, b) { const mx = Math.max(r, g, b), mn = Math.min(r, g, b), d = mx - mn; let h = 0;
  if (d) { if (mx === r) h = ((g - b) / d) % 6; else if (mx === g) h = (b - r) / d + 2; else h = (r - g) / d + 4; h *= 60; if (h < 0) h += 360; }
  return [h, mx ? d / mx : 0, mx / 255]; }
export function paintSki(root, main, acc) {
  root.traverse(o => {
    if (!o.isMesh) return; const m0 = o.userData.mat0 || (o.userData.mat0 = o.material); if (!m0.map || !m0.map.image) return;
    const key = m0.uuid + main + acc; let tex = cache.get(key);
    if (!tex) {
      const img = m0.map.image, w = img.width, h = img.height, cv = document.createElement('canvas'); cv.width = w; cv.height = h;
      const cx = cv.getContext('2d'); cx.drawImage(img, 0, 0); const id = cx.getImageData(0, 0, w, h), d = id.data;
      const A = new THREE.Color(main), Bc = new THREE.Color(acc || main);
      for (let i = 0; i < d.length; i += 4) { const [hu, s, v] = hsv(d[i], d[i + 1], d[i + 2]);
        if (s > .35 && v > .25 && hu > 160 && hu < 205) { const k = v / .78; d[i] = A.r * 255 * k; d[i + 1] = A.g * 255 * k; d[i + 2] = A.b * 255 * k; }        // turquesa -> principal
        else if (s > .45 && v > .35 && hu > 45 && hu < 75) { const k = v / .85; d[i] = Bc.r * 255 * k; d[i + 1] = Bc.g * 255 * k; d[i + 2] = Bc.b * 255 * k; } } // amarillo -> secundario
      cx.putImageData(id, 0, 0); tex = new THREE.CanvasTexture(cv); tex.flipY = m0.map.flipY; tex.colorSpace = THREE.SRGBColorSpace; tex.anisotropy = 8; cache.set(key, tex);
    }
    const m = m0.clone(); m.map = tex; o.material = m;
  });
}
export const PAINTS = [
  { id: 'serie', n: 'De serie', main: null, acc: null, p: 0 },
  { id: 'brava', n: 'Brava', main: '#e3202b', acc: '#f5f6f8', p: 200 }, { id: 'avispa', n: 'Avispa', main: '#ffd21a', acc: '#25272e', p: 200 },
  { id: 'oceano', n: 'Océano', main: '#1e5eff', acc: '#16181d', p: 200 }, { id: 'marea', n: 'Marea', main: '#4d9bff', acc: '#ffffff', p: 200 },
  { id: 'solar', n: 'Solar', main: '#ffb21a', acc: '#2a2c33', p: 200 }, { id: 'veneno', n: 'Veneno', main: '#5fd31a', acc: '#111317', p: 200 },
  { id: 'sombra', n: 'Sombra', main: '#3a3f48', acc: '#8d9199', p: 200 }, { id: 'dorada', n: 'Dorada', main: '#d9b55a', acc: '#e3202b', p: 400 },
  { id: 'rosa', n: 'Flamenco', main: '#ff3f8e', acc: '#ffffff', p: 400 }];
