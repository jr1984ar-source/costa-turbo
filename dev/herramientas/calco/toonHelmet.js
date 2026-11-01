// Casco estilo ilustración: tonos lisos calcados + contorno + brillo limpio + gafas
const { tracedHelmet } = require('./tracedHelmet.js');
function toonHelmet(J, gog, uid, opt) {
  opt = opt || {};
  const ow = opt.ow || 7;
  const T = tracedHelmet(J, gog, uid);
  const id = (n) => n + uid;
  const base = J.layers.slice().sort((a, b) => b.area - a.area)[0].col;
  let defs = T.defs + `<clipPath id="${id('sc')}"><path d="${J.sil}"/></clipPath>`;
  // capas con bordes oscuros finos entre zonas (aspecto dibujado)
  let g = `<path d="${J.sil}" fill="${base}"/>`;
  g += J.layers.map(l => `<path d="${l.d}" fill="${l.col}" fill-rule="evenodd" stroke="${l.col}" stroke-width="1.6" stroke-linejoin="round"/>`).join('');
  if (opt.inner) g += `<g clip-path="url(#${id('sc')})">` + J.layers.filter(l => l.area > 1500).map(l => `<path d="${l.d}" fill="none" stroke="rgba(10,12,20,.35)" stroke-width="${opt.inner}" stroke-linejoin="round"/>`).join('') + `</g>`;
  // brillo limpio arriba (curva blanca) y sombra suave abajo
  const w = J.w, h = J.h;
  g += `<g clip-path="url(#${id('sc')})"><ellipse cx="${w * .48}" cy="${h * .12}" rx="${w * .3}" ry="${h * .07}" fill="#ffffff" opacity=".22"/><path d="M${w * .3},${h * .1} C${w * .42},${h * .04} ${w * .6},${h * .03} ${w * .72},${h * .07}" stroke="#ffffff" stroke-width="${w * .016}" stroke-linecap="round" fill="none" opacity=".75"/><rect x="0" y="${h * .78}" width="${w}" height="${h * .22}" fill="#000" opacity=".12"/></g>`;
  // gafas (las mismas que el calco) encima
  g += T.body.split('<!--GOG-->')[1] || '';
  // contorno exterior grueso
  g += `<path d="${J.sil}" fill="none" stroke="#11141c" stroke-width="${ow}" stroke-linejoin="round"/>`;
  return { defs, body: g, w, h };
}
module.exports = { toonHelmet };
