// Casco calcado (capas de color) + gafas encajadas en el ojo
var LENSES = {
  clear: ['#eaf7ff', '#cfe9f7', '#9fcde6'], smoke: ['#7b8696', '#3d4552', '#1f242c'],
  red: ['#ffd166', '#ff5a3c', '#c2185b'], blue: ['#9ff3ff', '#2f8cff', '#3a2aa8'],
  gold: ['#fff3b0', '#ffc93c', '#b8741a'], silver: ['#ffffff', '#b9c3cf', '#6f7a88'],
  jade: ['#c8ffd8', '#2fbf71', '#0e6b4a'], prizm: ['#ffd166', '#ff7a3c', '#e2366e', '#5b3cff']
};
function tracedHelmet(J, gog, uid) {
  const id = (n) => n + uid;
  const mix = (a, b, t) => { const f = (x) => [parseInt(x.slice(1, 3), 16), parseInt(x.slice(3, 5), 16), parseInt(x.slice(5, 7), 16)]; const A = f(a), B = f(b); return '#' + A.map((v, i) => Math.round(v + (B[i] - v) * t).toString(16).padStart(2, '0')).join(''); };
  const lum = (h) => { h = h.replace('#', ''); return (parseInt(h.slice(0, 2), 16) * .3 + parseInt(h.slice(2, 4), 16) * .59 + parseInt(h.slice(4, 6), 16) * .11) / 255; };
  const base = J.layers.slice().sort((a, b) => b.area - a.area)[0].col;
  let defs = `<clipPath id="${id('sil')}"><path d="${J.sil}"/></clipPath>`;
  let g = `<path d="${J.sil}" fill="${base}"/>` + J.layers.map(l => `<path d="${l.d}" fill="${l.col}" fill-rule="evenodd" stroke="${l.col}" stroke-width="1.4" stroke-linejoin="round"/>`).join('');
  // brillo general suave para dar volumen
  defs += `<radialGradient id="${id('gl')}" cx=".35" cy=".2" r=".7"><stop offset="0" stop-color="#ffffff" stop-opacity=".18"/><stop offset="1" stop-color="#ffffff" stop-opacity="0"/></radialGradient>`;
  g += `<g clip-path="url(#${id('sil')})"><rect width="${J.w}" height="${J.h}" fill="url(#${id('gl')})"/></g>`;
  g += '<!--GOG-->';
  if (gog && J.port) {
    const [px, py, pw, ph] = J.port;
    const LZ = LENSES[gog.lens] || LENSES.prizm, fr = gog.frame || '#1b1d22', st = gog.strap, acc = gog.acc || st;
    const gw = pw * 1.18, gh = Math.min(gw * .5, ph * .7), gx = px - pw * .13, gy = py + ph * .03;
    const P = (a, b) => `${(gx + gw * a).toFixed(1)},${(gy + gh * b).toFixed(1)}`;
    defs += `<linearGradient id="${id('ln')}" x1="0" x2="1" y1="0" y2="1">${LZ.map((q, i) => `<stop offset="${i / (LZ.length - 1)}" stop-color="${q}"/>`).join('')}</linearGradient>
    <linearGradient id="${id('lsh')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#000" stop-opacity=".35"/><stop offset=".35" stop-color="#000" stop-opacity="0"/><stop offset=".8" stop-color="#fff" stop-opacity=".08"/><stop offset="1" stop-color="#000" stop-opacity=".25"/></linearGradient>
    <linearGradient id="${id('fr')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${mix(fr, '#ffffff', .28)}"/><stop offset=".45" stop-color="${fr}"/><stop offset="1" stop-color="${mix(fr, '#000000', .45)}"/></linearGradient>
    <linearGradient id="${id('st')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${mix(st, '#ffffff', .25)}"/><stop offset=".5" stop-color="${st}"/><stop offset="1" stop-color="${mix(st, '#000000', .4)}"/></linearGradient>`;
    // goma ancha alrededor del casco
    const sy0 = gy + gh * .2, sh0 = gh * .5, xr = gx + gw * .9;
    const strapP = `M${xr},${sy0} C${xr + (J.w - xr) * .35},${sy0 - gh * .1} ${xr + (J.w - xr) * .75},${sy0 - gh * .02} ${J.w + 4},${sy0 + gh * .14} L${J.w + 4},${sy0 + gh * .14 + sh0} C${xr + (J.w - xr) * .75},${sy0 + sh0 - gh * .04} ${xr + (J.w - xr) * .35},${sy0 + sh0 - gh * .08} ${xr},${sy0 + sh0} Z`;
    g += `<g clip-path="url(#${id('sil')})"><path d="${strapP}" fill="url(#${id('st')})"/><path d="${strapP}" fill="none" stroke="#000" stroke-opacity=".45" stroke-width="2.5"/>
      <path d="M${xr},${sy0 + sh0 * .12} C${xr + (J.w - xr) * .35},${sy0 - gh * .02} ${xr + (J.w - xr) * .75},${sy0 + gh * .06} ${J.w + 4},${sy0 + gh * .22}" stroke="#fff" stroke-opacity=".25" stroke-width="2" fill="none"/></g>`;
    const bt = gog.brand === 'oakley' ? 'OAKLEY' : gog.brand === '100' ? '100%' : 'alpinestars', tc = lum(st) > .6 ? '#15171c' : '#ffffff';
    const lb = gx + gw * 1.07, rb = J.w * .95, room = (rb - lb) * .86, tx = (lb + rb) / 2, ty = sy0 + sh0 * .72 + gh * .01, fs = Math.min(sh0 * .66, room / (bt.length * .62));
    g += `<g clip-path="url(#${id('sil')})"><text x="${tx}" y="${ty}" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="${fs}" ${gog.brand === 'oakley' ? 'font-style="italic"' : ''} textLength="${Math.min(room, fs * bt.length * .75)}" lengthAdjust="spacingAndGlyphs" fill="${tc}" transform="rotate(4 ${tx} ${ty})">${bt}</text></g>`;
    // montura: forma de gafa de cross vista de 3/4 (lado derecho más estrecho)
    const frame = `M${P(.01, .16)} C${P(.18, -.06)} ${P(.7, -.08)} ${P(.93, .04)} C${P(1.02, .16)} ${P(1.04, .62)} ${P(.97, .86)} C${P(.86, 1.02)} ${P(.7, 1.04)} ${P(.6, .96)} C${P(.55, .86)} ${P(.47, .74)} ${P(.4, .74)} C${P(.33, .74)} ${P(.28, .86)} ${P(.22, .96)} C${P(.14, 1.04)} ${P(.03, 1.0)} ${P(-.01, .84)} C${P(-.04, .6)} ${P(-.03, .3)} ${P(.01, .16)} Z`;
    const lens = `M${P(.06, .2)} C${P(.22, .05)} ${P(.68, .03)} ${P(.88, .13)} C${P(.94, .26)} ${P(.95, .6)} ${P(.9, .76)} C${P(.82, .88)} ${P(.7, .88)} ${P(.63, .8)} C${P(.57, .7)} ${P(.48, .6)} ${P(.4, .6)} C${P(.32, .6)} ${P(.26, .7)} ${P(.21, .8)} C${P(.15, .88)} ${P(.07, .85)} ${P(.04, .72)} C${P(.02, .54)} ${P(.03, .32)} ${P(.06, .2)} Z`;
    defs += `<clipPath id="${id('lc')}"><path d="${lens}"/></clipPath>`;
    // sombra de la gafa sobre el casco
    g += `<path d="${frame}" transform="translate(${gw * .02} ${gh * .07})" fill="#000" opacity=".35"/>`;
    // montura con borde de color y espuma
    g += `<path d="${frame}" fill="url(#${id('fr')})" stroke="#0b0d12" stroke-width="${gw * .012}" stroke-linejoin="round"/>`;
    g += `<path d="M${P(.03, .14)} C${P(.2, -.03)} ${P(.7, -.05)} ${P(.92, .06)}" stroke="${acc}" stroke-width="${gh * .07}" fill="none" stroke-linecap="round"/>`;
    g += `<path d="M${P(.02, .86)} C${P(.08, .98)} ${P(.16, .98)} ${P(.22, .92)} M${P(.6, .92)} C${P(.7, 1.0)} ${P(.86, .98)} ${P(.95, .84)}" stroke="#2a2d33" stroke-width="${gh * .06}" fill="none" stroke-linecap="round"/>`;
    // lente con espejo, sombra interior y reflejos
    g += `<path d="${lens}" fill="url(#${id('ln')})"/><path d="${lens}" fill="url(#${id('lsh')})"/>`;
    g += `<g clip-path="url(#${id('lc')})"><path d="M${P(.12, -.1)} L${P(.3, -.1)} L${P(.14, 1.1)} L${P(-.04, 1.1)} Z" fill="#fff" opacity=".42"/><path d="M${P(.34, -.1)} L${P(.4, -.1)} L${P(.24, 1.1)} L${P(.18, 1.1)} Z" fill="#fff" opacity=".28"/><path d="M${P(.7, -.1)} L${P(.74, -.1)} L${P(.62, 1.1)} L${P(.58, 1.1)} Z" fill="#fff" opacity=".18"/>
      <ellipse cx="${(gx + gw * .78).toFixed(1)}" cy="${(gy + gh * .3).toFixed(1)}" rx="${gw * .08}" ry="${gh * .08}" fill="#fff" opacity=".35"/></g>`;
    g += `<path d="${lens}" fill="none" stroke="#0b0d12" stroke-width="${gw * .01}" stroke-linejoin="round"/>`;
    // pivotes (tear-off posts) y pieza lateral hacia la goma
    for (const [a, b] of [[.0, .46], [.95, .44]]) g += `<circle cx="${(gx + gw * a).toFixed(1)}" cy="${(gy + gh * b).toFixed(1)}" r="${gh * .075}" fill="#c9ced6" stroke="#0b0d12" stroke-width="2"/><circle cx="${(gx + gw * a).toFixed(1)}" cy="${(gy + gh * b).toFixed(1)}" r="${gh * .03}" fill="#5a606b"/>`;
    g += `<path d="M${P(.93, .2)} L${P(1.04, .24)} L${P(1.04, .7)} L${P(.95, .74)} Z" fill="${acc}" stroke="#0b0d12" stroke-width="2"/>`;
  }
  return { defs, body: g, w: J.w, h: J.h };
}
if (typeof module !== 'undefined') module.exports = { tracedHelmet, LENSES };
