// Piloto de pie mirando de lado (hacia la derecha) — boceto
const LENSES = {
  clear: ['#eaf7ff', '#cfe9f7', '#9fcde6'], smoke: ['#7b8696', '#3d4552', '#1f242c'],
  red: ['#ffd166', '#ff5a3c', '#c2185b'], blue: ['#9ff3ff', '#2f8cff', '#3a2aa8'],
  gold: ['#fff3b0', '#ffc93c', '#b8741a'], silver: ['#ffffff', '#b9c3cf', '#6f7a88'],
  jade: ['#c8ffd8', '#2fbf71', '#0e6b4a'], prizm: ['#ffd166', '#ff7a3c', '#e2366e', '#5b3cff']
};
function pilotSideSVG(o, uid) {
  uid = uid || 's' + Math.floor(Math.random() * 1e6);
  const H = o.helm, V = o.vest, S = o.suit, GG = o.gog || { brand: 'oakley', strap: '#1d2027', lens: 'prizm', frame: '#1b1d22' };
  const glove = o.glove || '#1b1d22';
  const hx = (c) => { c = c.replace('#', ''); return [parseInt(c.slice(0, 2), 16), parseInt(c.slice(2, 4), 16), parseInt(c.slice(4, 6), 16)]; };
  const mix = (a, b, t) => { const A = hx(a), B = hx(b); return '#' + A.map((v, i) => Math.round(v + (B[i] - v) * t).toString(16).padStart(2, '0')).join(''); };
  const L = (c, t) => mix(c, '#ffffff', t), D = (c, t) => mix(c, '#000000', t);
  const lum = (c) => { const [r, g, b] = hx(c); return (r * .3 + g * .59 + b * .11) / 255; };
  const id = (n) => n + uid;
  const OL = 'stroke="rgba(8,12,22,.6)" stroke-width="2.2" stroke-linejoin="round"';
  const cyl = (n, c, k) => `<linearGradient id="${id(n)}" x1="0" x2="1"><stop offset="0" stop-color="${D(c, .45 * k)}"/><stop offset=".35" stop-color="${L(c, .18 * k)}"/><stop offset=".6" stop-color="${c}"/><stop offset="1" stop-color="${D(c, .5 * k)}"/></linearGradient>`;
  const suitC = S.c || '#1d2027', suitA = S.a || '#3a3f4a', farC = D(suitC, .3);
  const helmC = H.c, helmC2 = H.c2 || '#ffffff', chrome = H.pat === 'chrome', full = H.st === 'full';
  const vestC = V.c, vestC2 = V.c2 || '#ffffff', vestTxt = lum(vestC) > .62 ? '#15171c' : '#ffffff';
  const lens = LENSES[GG.lens] || LENSES.prizm;
  const pat = (k) => k === 'camo' ? `url(#${id('camo')})` : k === 'carbon' ? `url(#${id('carb')})` : null;

  const shellP = full ? 'M104,84 C100,50 122,20 156,20 C190,20 212,44 214,78 C216,104 206,124 190,134 L128,136 C112,126 106,106 104,84 Z'
    : 'M104,86 C100,52 122,24 156,22 C186,22 204,40 206,64 L200,92 C196,110 184,124 166,128 L124,128 C112,120 106,104 104,86 Z';
  const vestP = 'M120,128 C112,150 108,190 110,230 C110,262 110,284 112,300 C136,306 166,306 188,300 C190,270 192,240 194,210 C196,180 192,150 180,130 C168,122 132,120 120,128 Z';
  const legN = 'M134,316 C142,370 158,420 166,456 C162,500 170,546 178,588 L206,588 C204,546 202,500 204,456 C208,412 204,360 190,314 Z';
  const legF = 'M112,316 C104,370 100,420 102,456 C94,500 88,546 88,588 L116,588 C118,546 124,500 138,456 C150,412 160,360 164,314 Z';
  const armN = 'M124,138 C110,168 108,210 112,246 C116,280 128,304 142,322 L166,312 C152,292 144,266 142,240 C142,206 150,172 160,144 Z';

  let defs = `<defs>${cyl('leg', suitC, 1)}${cyl('legf', farC, 1)}${cyl('arm', suitC, 1)}
  <linearGradient id="${id('vest')}" x1="0" x2="1" y1="0" y2=".3"><stop offset="0" stop-color="${D(vestC, .4)}"/><stop offset=".45" stop-color="${L(vestC, .2)}"/><stop offset=".8" stop-color="${vestC}"/><stop offset="1" stop-color="${D(vestC, .35)}"/></linearGradient>
  <linearGradient id="${id('vside')}" x1="0" x2="1"><stop offset="0" stop-color="${D(vestC2, .3)}"/><stop offset=".5" stop-color="${L(vestC2, .1)}"/><stop offset="1" stop-color="${D(vestC2, .25)}"/></linearGradient>
  ${chrome
    ? `<radialGradient id="${id('shell')}" cx=".45" cy=".25" r=".9"><stop offset="0" stop-color="#ffffff"/><stop offset=".3" stop-color="#dfe6ee"/><stop offset=".55" stop-color="#8d99a8"/><stop offset=".75" stop-color="#eef3f8"/><stop offset="1" stop-color="#5d6876"/></radialGradient>`
    : `<radialGradient id="${id('shell')}" cx=".5" cy=".28" r=".85"><stop offset="0" stop-color="${L(helmC, .55)}"/><stop offset=".35" stop-color="${L(helmC, .12)}"/><stop offset=".75" stop-color="${helmC}"/><stop offset="1" stop-color="${D(helmC, .45)}"/></radialGradient>`}
  <linearGradient id="${id('lens')}" x1="0" x2="1" y1="0" y2="1">${lens.map((c, i) => `<stop offset="${i / (lens.length - 1)}" stop-color="${c}"/>`).join('')}</linearGradient>
  <linearGradient id="${id('visor')}" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#3b4d6e"/><stop offset=".5" stop-color="#151d2d"/><stop offset="1" stop-color="#0a0f19"/></linearGradient>
  <linearGradient id="${id('metal')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#f1f4f8"/><stop offset=".5" stop-color="#a7afba"/><stop offset="1" stop-color="#6c7480"/></linearGradient>
  <linearGradient id="${id('strap')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${L(GG.strap, .2)}"/><stop offset=".5" stop-color="${GG.strap}"/><stop offset="1" stop-color="${D(GG.strap, .35)}"/></linearGradient>
  <pattern id="${id('carb')}" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#22252b"/><rect width="4" height="4" fill="#33373f"/><rect x="4" y="4" width="4" height="4" fill="#33373f"/></pattern>
  <pattern id="${id('camo')}" width="60" height="60" patternUnits="userSpaceOnUse"><rect width="60" height="60" fill="${suitC}"/><path d="M5 8c10-6 18 2 14 10s-16 6-14-10zM34 30c9-4 20 4 14 12s-20 2-14-12zM10 44c6-3 12 2 9 7s-12 3-9-7z" fill="${D(suitC, .35)}"/></pattern>
  <filter id="${id('blur')}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
  <clipPath id="${id('vclip')}"><path d="${vestP}"/></clipPath>
  <clipPath id="${id('hclip')}"><path d="${shellP}"/></clipPath>
  <clipPath id="${id('nclip')}"><path d="${legN}"/></clipPath>
  <clipPath id="${id('aclip')}"><path d="${armN}"/></clipPath>
  </defs>`;

  let g = `<ellipse cx="156" cy="628" rx="84" ry="11" fill="rgba(0,0,0,.45)" filter="url(#${id('blur')})"/>`;
  // ---- pierna de atrás ----
  g += `<path d="${legF}" fill="${pat(S.pat) || `url(#${id('legf')})`}" ${OL}/>`;
  g += `<path d="M132,436 C142,436 146,446 144,458 C142,472 136,480 128,480 C122,470 122,444 132,436 Z" fill="${D(suitA === '#ffc93c' ? '#2a2d33' : suitA, .5)}" ${OL}/>`;
  g += `<path d="M86,584 L116,584 C120,596 130,604 144,608 C152,611 154,620 148,626 L86,626 C82,614 82,598 86,584 Z" fill="#121418" ${OL}/>`;
  // ---- cadera ----
  g += `<path d="M110,290 C106,310 110,326 120,334 L186,330 C192,318 192,304 190,290 Z" fill="${pat(S.pat) || D(suitC, .12)}" ${OL}/>`;
  // ---- pierna de delante ----
  g += `<path d="${legN}" fill="${pat(S.pat) || `url(#${id('leg')})`}" ${OL}/>`;
  g += `<g clip-path="url(#${id('nclip')})"><path d="M162,316 C172,370 184,420 186,456 C184,500 188,546 192,590" stroke="${suitA}" stroke-width="8" fill="none"/>
    <path d="M194,330 C200,380 200,420 198,446 M198,470 C196,510 198,550 200,584" stroke="rgba(255,255,255,.22)" stroke-width="5" stroke-linecap="round" fill="none"/>
    <rect x="100" y="296" width="120" height="24" fill="rgba(0,0,0,.28)"/></g>`;
  // rodillera de perfil
  const kp = D(suitA === '#ffc93c' ? '#2a2d33' : suitA, .35);
  g += `<path d="M196,430 C210,432 216,446 214,462 C212,476 204,486 194,486 C186,476 184,440 196,430 Z" fill="${kp}" ${OL}/><path d="M198,442 q8 2 10 8 M198,454 q9 2 11 8 M197,466 q8 2 9 8" stroke="rgba(255,255,255,.18)" stroke-width="2.2" fill="none"/>`;
  // escarpín de delante
  g += `<path d="M176,584 L206,584 C210,596 222,604 238,608 C248,611 250,620 244,626 L176,626 C172,614 172,598 176,584 Z" fill="#17191e" ${OL}/>
  <path d="M174,621 h72" stroke="#4a505c" stroke-width="5" stroke-linecap="round"/><path d="M178,596 h26" stroke="${suitA}" stroke-width="4" stroke-linecap="round"/><path d="M212,604 q12 4 24 6" stroke="rgba(255,255,255,.2)" stroke-width="2.2" fill="none" stroke-linecap="round"/>`;

  // ---- chaleco de perfil ----
  g += `<path d="M138,112 C150,106 166,108 176,116 L178,134 L132,136 Z" fill="${D(suitC, .2)}" ${OL}/>`;
  g += `<path d="${vestP}" fill="${V.pat === 'carbon' ? `url(#${id('carb')})` : `url(#${id('vest')})`}" ${OL}/>`;
  g += `<g clip-path="url(#${id('vclip')})">`;
  g += `<path d="M126,140 C122,190 122,250 124,306 L152,306 C150,250 150,190 152,136 Z" fill="url(#${id('vside')})"/>`;
  if (V.pat === 'vault') g += `<path d="M150,236 L200,262 L200,282 L150,256 Z" fill="${vestC2}"/>`;
  else if (V.pat === 'race') g += `<rect x="166" y="120" width="8" height="200" fill="${vestC2}"/>`;
  else if (V.pat === 'band') g += `<rect x="100" y="194" width="110" height="16" fill="${vestC2}"/>`;
  else if (V.pat === 'carbon') g += `<path d="${vestP}" fill="none" stroke="${vestC2}" stroke-width="7"/>`;
  for (const y of [196, 238, 280]) g += `<path d="M106,${y} C140,${y + 4} 170,${y + 4} 200,${y - 2}" stroke="rgba(0,0,0,.3)" stroke-width="3" fill="none"/><path d="M106,${y + 3} C140,${y + 7} 170,${y + 7} 200,${y + 1}" stroke="rgba(255,255,255,.14)" stroke-width="2" fill="none"/>`;
  g += `<path d="M180,140 C190,170 190,230 184,290" stroke="rgba(255,255,255,.25)" stroke-width="7" stroke-linecap="round" fill="none"/>`;
  for (const y of [214, 258]) g += `<rect x="100" y="${y}" width="110" height="10" fill="#14161a"/>`;
  g += `</g>`;
  for (const y of [214, 258]) g += `<rect x="186" y="${y - 3}" width="14" height="16" rx="4" fill="url(#${id('metal')})" ${OL}/>`;
  g += `<g transform="translate(150 176) rotate(-4) scale(.92)"><path d="M0,-10 l10,4 l-10,4 z" fill="${vestC2 === vestC ? vestTxt : vestC2}"/><text x="12" y="0" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="11" fill="${vestTxt}" stroke="rgba(0,0,0,.25)" stroke-width=".6">JET PILOT</text></g>`;
  if (V.name) g += `<rect x="146" y="282" width="46" height="12" rx="3" fill="rgba(10,12,18,.82)"/><text x="169" y="291" text-anchor="middle" font-family="Arial,sans-serif" font-weight="800" font-size="7.4" fill="#fff">${V.name.toUpperCase()}</text>`;

  // ---- brazo de delante ----
  g += `<path d="${armN}" fill="${pat(S.pat) || `url(#${id('arm')})`}" ${OL}/>`;
  g += `<g clip-path="url(#${id('aclip')})"><path d="M106,134 C126,124 160,128 168,142 L158,180 C144,170 128,170 112,180 Z" fill="${suitA}"/><rect x="128" y="302" width="50" height="16" fill="${suitA}" transform="rotate(-30 153 310)"/>
    <ellipse cx="124" cy="246" rx="14" ry="18" fill="${D(suitC === '#2a2d33' ? '#3a3f4a' : suitC, .38)}" transform="rotate(-15 124 246)"/><path d="M118,238 q6 -3 12 1 M118,248 q6 -3 12 1" stroke="rgba(255,255,255,.2)" stroke-width="2" fill="none"/>
    <path d="M146,170 C140,200 138,224 140,240" stroke="rgba(255,255,255,.22)" stroke-width="5" stroke-linecap="round" fill="none"/></g>`;
  g += `<path d="M142,318 C136,334 142,350 156,354 C168,356 176,346 174,334 L166,310 Z" fill="${glove}" ${OL}/><path d="M154,324 q8 4 12 12 M150,332 q8 4 11 12" stroke="rgba(255,255,255,.22)" stroke-width="1.8" fill="none"/><path d="M144,318 l18 -9" stroke="${suitA}" stroke-width="5" stroke-linecap="round"/>`;
  g += `<ellipse cx="160" cy="140" rx="34" ry="9" fill="rgba(0,0,0,.32)" filter="url(#${id('blur')})"/>`;

  // ---- casco de perfil ----
  if (!full) g += `<path d="M118,122 C130,136 162,140 172,128 L170,142 L122,142 Z" fill="#1d2027" ${OL}/>`;
  g += `<path d="${shellP}" fill="url(#${id('shell')})" ${OL}/>`;
  g += `<g clip-path="url(#${id('hclip')})">`;
  if (H.pat === 'flame') g += `<path d="M214,104 C190,96 168,104 150,96 C162,92 168,86 166,80 C154,86 140,84 126,74 C142,72 152,64 150,56 C136,64 118,62 100,50 L96,140 L214,140 Z" fill="${helmC2}"/><path d="M214,112 C196,106 178,112 160,106 C170,102 174,98 172,94 C162,98 148,98 136,92 L130,140 L214,140 Z" fill="#ffd21a" opacity=".9"/>`;
  else if (H.pat === 'twin') g += `<path d="M106,60 C120,30 160,18 200,36" stroke="${helmC2}" stroke-width="7" fill="none"/><path d="M110,72 C126,42 164,30 204,48" stroke="${helmC2}" stroke-width="7" fill="none"/>`;
  else if (H.pat === 'split') g += `<rect x="90" y="0" width="64" height="150" fill="${helmC2}"/>`;
  else if (H.pat === 'star') g += `<path d="M150,46 l7,15 16,2 -12,11 3,16 -14,-8 -14,8 3,-16 -12,-11 16,-2z" fill="${helmC2}"/>`;
  else if (H.pat === 'carbon') g += `<rect x="90" y="0" width="140" height="150" fill="url(#${id('carb')})" opacity=".9"/><path d="M100,100 L214,92" stroke="${helmC2}" stroke-width="5"/>`;
  else if (H.pat === 'chrome') g += `<path d="M108,60 C122,32 160,20 196,34" stroke="${helmC2}" stroke-width="7" fill="none"/>`;
  g += `<path d="M118,40 C134,26 152,22 170,24" stroke="rgba(255,255,255,.55)" stroke-width="5" stroke-linecap="round" fill="none"/></g>`;
  if (!full) {
    // visera
    g += `<path d="M180,42 C202,32 228,30 248,34 L244,48 C226,48 206,52 194,62 Z" fill="url(#${id('shell')})" ${OL}/><path d="M186,40 C206,33 228,32 246,36" stroke="${helmC2}" stroke-width="4" fill="none"/>
    <text x="214" y="46" text-anchor="middle" font-family="Arial,sans-serif" font-weight="800" font-size="7" fill="${lum(helmC) > .6 ? '#15171c' : '#ffffff'}" transform="rotate(-6 214 46)">${H.brand === 'Arai' ? 'Arai' : 'alpinestars'}</text>`;
    // goma de las gafas
    g += `<path d="M104,61 C130,55 170,55 196,58 L196,84 C170,79 130,79 104,85 Z" fill="url(#${id('strap')})" ${OL}/>`;
    const bt = GG.brand === 'oakley' ? 'OAKLEY' : GG.brand === '100' ? '100%' : 'alpinestars', tc = lum(GG.strap) > .6 ? '#15171c' : '#ffffff';
    g += `<text x="150" y="74" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="${GG.brand === 'alpinestars' ? 9 : 10.5}" letter-spacing="${GG.brand === 'oakley' ? 1.5 : .5}" fill="${tc}" ${GG.brand === 'oakley' ? 'font-style="italic"' : ''}>${bt}</text>`;
    if (GG.brand === 'oakley') g += `<ellipse cx="116" cy="69.5" rx="6" ry="4" fill="none" stroke="${tc}" stroke-width="1.8"/>`;
    if (GG.brand === 'alpinestars') g += `<path d="M112,64 l2,4 4.4,.6 -3.2,3 .8,4.4 -4,-2.2 -4,2.2 .8,-4.4 -3.2,-3 4.4,-.6z" fill="${tc}"/>`;
    // montura y lente
    const fr = GG.frame || '#1b1d22';
    g += `<path d="M192,52 L220,54 C231,60 233,82 224,92 L192,92 Z" fill="${fr}" ${OL}/><path d="M203,57 L221,58 C228,65 228,82 222,88 L203,88 Z" fill="url(#${id('lens')})"/><path d="M207,59 L212,59 L208,86 L204,86 Z" fill="rgba(255,255,255,.5)"/><path d="M215,60 L217,60 L214,84 L212,84 Z" fill="rgba(255,255,255,.3)"/><circle cx="197" cy="72" r="3.8" fill="${GG.strap}" ${OL}/>`;
    // mentonera
    g += `<path d="M190,92 C206,96 222,100 232,110 C232,120 222,128 208,130 L170,130 C182,120 188,106 190,92 Z" fill="url(#${id('shell')})" ${OL}/>
    <path d="M198,104 l14 4 M196,112 l16 4 M194,120 l14 3" stroke="#15171c" stroke-width="3.4" stroke-linecap="round"/><path d="M226,104 C232,108 234,116 232,122" stroke="#6c7480" stroke-width="4" fill="none" stroke-linecap="round"/>`;
  } else {
    g += `<path d="M178,50 C196,52 208,62 212,76 C212,86 208,94 202,98 L178,96 C172,82 172,62 178,50 Z" fill="url(#${id('visor')})" ${OL}/><path d="M184,56 C196,58 204,64 207,72" stroke="rgba(255,255,255,.45)" stroke-width="4" stroke-linecap="round" fill="none"/>
    <circle cx="174" cy="74" r="7" fill="url(#${id('metal')})" ${OL}/><path d="M196,112 l12 2 M194,118 l12 2" stroke="#15171c" stroke-width="3" stroke-linecap="round"/><ellipse cx="150" cy="30" rx="8" ry="4" fill="#15171c"/>
    <text x="170" y="128" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="13" fill="${lum(helmC) > .6 && !chrome ? '#c8102e' : '#ffffff'}">Arai</text>`;
  }
  // luz de contorno del estudio
  g += `<path d="M110,100 C104,80 106,56 118,40" stroke="rgba(130,225,255,.45)" stroke-width="2.4" fill="none" stroke-linecap="round"/><path d="M190,200 C194,240 192,270 188,300" stroke="rgba(130,225,255,.45)" stroke-width="2.4" fill="none" stroke-linecap="round"/>`;
  return `<svg viewBox="0 0 300 640" xmlns="http://www.w3.org/2000/svg">${defs}${g}</svg>`;
}
if (typeof module !== 'undefined') module.exports = { pilotSideSVG, LENSES };
