// Piloto de pie de medio lado (3/4, girado a la derecha) — boceto
var LENSES = {
  clear: ['#eaf7ff', '#cfe9f7', '#9fcde6'], smoke: ['#7b8696', '#3d4552', '#1f242c'],
  red: ['#ffd166', '#ff5a3c', '#c2185b'], blue: ['#9ff3ff', '#2f8cff', '#3a2aa8'],
  gold: ['#fff3b0', '#ffc93c', '#b8741a'], silver: ['#ffffff', '#b9c3cf', '#6f7a88'],
  jade: ['#c8ffd8', '#2fbf71', '#0e6b4a'], prizm: ['#ffd166', '#ff7a3c', '#e2366e', '#5b3cff']
};
function pilot34SVG(o, uid) {
  uid = uid || 'q' + Math.floor(Math.random() * 1e6);
  const H = o.helm, V = o.vest, S = o.suit, GG = o.gog || { brand: 'oakley', strap: '#1d2027', lens: 'prizm' };
  const glove = o.glove || '#1b1d22', gloveA = o.gloveA || null;
  const hx = (c) => { c = c.replace('#', ''); return [parseInt(c.slice(0, 2), 16), parseInt(c.slice(2, 4), 16), parseInt(c.slice(4, 6), 16)]; };
  const mix = (a, b, t) => { const A = hx(a), B = hx(b); return '#' + A.map((v, i) => Math.round(v + (B[i] - v) * t).toString(16).padStart(2, '0')).join(''); };
  const L = (c, t) => mix(c, '#ffffff', t), D = (c, t) => mix(c, '#000000', t);
  const lum = (c) => { const [r, g, b] = hx(c); return (r * .3 + g * .59 + b * .11) / 255; };
  const id = (n) => n + uid;
  const OL = 'stroke="rgba(8,12,22,.6)" stroke-width="2.2" stroke-linejoin="round"';
  const cyl = (n, c, k) => `<linearGradient id="${id(n)}" x1="0" x2="1"><stop offset="0" stop-color="${D(c, .42 * k)}"/><stop offset=".32" stop-color="${L(c, .2 * k)}"/><stop offset=".6" stop-color="${c}"/><stop offset="1" stop-color="${D(c, .5 * k)}"/></linearGradient>`;
  const suitC = S.c || '#1d2027', suitA = S.a || '#3a3f4a', farC = D(suitC, .28);
  const helmC = H.c, helmC2 = H.c2 || '#ffffff', chrome = H.pat === 'chrome', full = H.st === 'full';
  const vestC = V.c, vestC2 = V.c2 || '#ffffff', vestTxt = lum(vestC) > .62 ? '#15171c' : '#ffffff';
  const lens = LENSES[GG.lens] || LENSES.prizm;
  const pat = (k) => k === 'camo' ? `url(#${id('camo')})` : k === 'carbon' ? `url(#${id('carb')})` : null;
  const kpad = D(suitA === '#ffc93c' ? '#2a2d33' : suitA, .35);

  const shellP = full ? 'M98,82 C96,44 122,16 156,16 C192,16 214,42 214,76 C214,104 204,126 186,140 C166,150 132,150 116,140 C102,128 98,106 98,82 Z'
    : 'M98,82 C96,46 122,18 156,18 C188,18 208,40 210,66 C212,92 204,114 188,128 L118,130 C104,118 98,100 98,82 Z';
  const vestP = 'M104,126 C94,134 88,146 86,160 C84,190 86,220 90,250 C92,272 94,288 96,302 C120,310 156,312 184,308 C196,306 204,302 208,298 C210,270 214,240 216,210 C218,180 214,152 204,134 C196,124 186,122 178,124 C174,138 166,150 160,154 C146,150 136,140 132,126 C122,122 112,122 104,126 Z';
  const legN = 'M100,318 C94,360 90,410 86,450 C82,494 80,540 76,584 L108,584 C112,540 118,500 124,460 C130,420 142,382 150,356 Z';
  const legF = 'M206,316 C212,358 214,404 214,448 C214,492 216,540 218,584 L190,584 C188,540 184,500 180,458 C174,420 164,382 154,356 Z';
  const armN = 'M100,136 C86,138 76,148 72,166 C66,198 64,228 66,256 C68,286 74,312 82,336 L104,332 C98,306 94,282 94,258 C94,230 98,204 104,182 Z';
  const armF = 'M200,136 C214,138 226,148 232,166 C240,190 246,210 244,228 C242,240 236,250 228,260 C220,270 212,280 204,290 L190,278 C200,266 210,254 216,240 C214,218 210,196 204,176 Z';

  const defs = `<defs>${cyl('leg', suitC, 1)}${cyl('legf', farC, 1)}${cyl('arm', suitC, 1)}${cyl('armf', farC, 1)}
  <linearGradient id="${id('vest')}" x1="0" x2="1" y1="0" y2=".25"><stop offset="0" stop-color="${D(vestC, .3)}"/><stop offset=".38" stop-color="${L(vestC, .24)}"/><stop offset=".7" stop-color="${vestC}"/><stop offset="1" stop-color="${D(vestC, .45)}"/></linearGradient>
  <linearGradient id="${id('vside')}" x1="0" x2="1"><stop offset="0" stop-color="${D(vestC2, .38)}"/><stop offset="1" stop-color="${vestC2}"/></linearGradient>
  ${chrome
    ? `<radialGradient id="${id('shell')}" cx=".42" cy=".26" r=".9"><stop offset="0" stop-color="#ffffff"/><stop offset=".3" stop-color="#dfe6ee"/><stop offset=".55" stop-color="#8d99a8"/><stop offset=".75" stop-color="#eef3f8"/><stop offset="1" stop-color="#5d6876"/></radialGradient>`
    : `<radialGradient id="${id('shell')}" cx=".42" cy=".28" r=".85"><stop offset="0" stop-color="${L(helmC, .55)}"/><stop offset=".35" stop-color="${L(helmC, .12)}"/><stop offset=".75" stop-color="${helmC}"/><stop offset="1" stop-color="${D(helmC, .45)}"/></radialGradient>`}
  <linearGradient id="${id('lens')}" x1="0" x2="1" y1="0" y2="1">${lens.map((c, i) => `<stop offset="${i / (lens.length - 1)}" stop-color="${c}"/>`).join('')}</linearGradient>
  <linearGradient id="${id('visor')}" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#3b4d6e"/><stop offset=".5" stop-color="#151d2d"/><stop offset="1" stop-color="#0a0f19"/></linearGradient>
  <linearGradient id="${id('metal')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#f1f4f8"/><stop offset=".5" stop-color="#a7afba"/><stop offset="1" stop-color="#6c7480"/></linearGradient>
  <linearGradient id="${id('strap')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${L(GG.strap, .22)}"/><stop offset=".5" stop-color="${GG.strap}"/><stop offset="1" stop-color="${D(GG.strap, .35)}"/></linearGradient>
  <pattern id="${id('carb')}" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#22252b"/><rect width="4" height="4" fill="#33373f"/><rect x="4" y="4" width="4" height="4" fill="#33373f"/></pattern>
  <pattern id="${id('camo')}" width="60" height="60" patternUnits="userSpaceOnUse"><rect width="60" height="60" fill="${suitC}"/><path d="M5 8c10-6 18 2 14 10s-16 6-14-10zM34 30c9-4 20 4 14 12s-20 2-14-12zM10 44c6-3 12 2 9 7s-12 3-9-7z" fill="${D(suitC, .35)}"/></pattern>
  <filter id="${id('blur')}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
  <clipPath id="${id('vclip')}"><path d="${vestP}"/></clipPath><clipPath id="${id('hclip')}"><path d="${shellP}"/></clipPath>
  <clipPath id="${id('nclip')}"><path d="${legN}"/></clipPath><clipPath id="${id('fclip')}"><path d="${legF}"/></clipPath><clipPath id="${id('aclip')}"><path d="${armN}"/></clipPath>
  </defs>`;

  let g = `<ellipse cx="160" cy="628" rx="96" ry="12" fill="rgba(0,0,0,.45)" filter="url(#${id('blur')})"/>`;
  // ---- pierna de atrás (derecha) ----
  g += `<path d="${legF}" fill="${pat(S.pat) || `url(#${id('legf')})`}" ${OL}/>`;
  g += `<g clip-path="url(#${id('fclip')})"><path d="M208,320 C214,380 214,440 214,470 C214,520 216,560 218,590" stroke="${D(suitA, .25)}" stroke-width="7" fill="none"/></g>`;
  g += `<g transform="rotate(-3 195 460)"><rect x="177" y="434" width="34" height="52" rx="14" fill="${D(kpad, .2)}" ${OL}/><path d="M183,449 h22 M183,460 h22 M183,471 h22" stroke="rgba(255,255,255,.12)" stroke-width="2.4" stroke-linecap="round"/></g>`;
  g += `<path d="M190,580 L218,580 C222,592 232,598 246,602 C256,605 258,616 252,624 L186,624 C182,612 184,594 190,580 Z" fill="#121418" ${OL}/><path d="M184,619 h70" stroke="#3a3f4a" stroke-width="5" stroke-linecap="round"/>`;
  // ---- brazo de atrás (mano en la cadera) ----
  g += `<path d="${armF}" fill="${pat(S.pat) || `url(#${id('armf')})`}" ${OL}/>`;
  g += `<ellipse cx="238" cy="228" rx="12" ry="16" fill="${D(suitC === '#2a2d33' ? '#3a3f4a' : suitC, .5)}" transform="rotate(-25 238 228)"/>`;
  // ---- cadera ----
  g += `<path d="M94,292 C92,312 96,330 104,340 L156,360 L206,338 C210,326 212,310 210,294 Z" fill="${pat(S.pat) || D(suitC, .14)}" ${OL}/>`;
  // ---- pierna de delante (izquierda) ----
  g += `<path d="${legN}" fill="${pat(S.pat) || `url(#${id('leg')})`}" ${OL}/>`;
  g += `<g clip-path="url(#${id('nclip')})"><path d="M98,318 C92,370 88,420 86,452 C84,500 82,546 80,590" stroke="${suitA}" stroke-width="8" fill="none"/>
    <path d="M114,336 C110,390 106,420 104,446 M104,500 C102,530 100,560 99,584" stroke="rgba(255,255,255,.22)" stroke-width="6" stroke-linecap="round" fill="none"/>
    <path d="M132,360 C128,400 124,430 120,456" stroke="rgba(0,0,0,.22)" stroke-width="1.8" fill="none"/><rect x="60" y="296" width="120" height="24" fill="rgba(0,0,0,.28)"/></g>`;
  g += `<g transform="rotate(5 104 460)"><rect x="85" y="434" width="38" height="54" rx="15" fill="${kpad}" ${OL}/><path d="M91,449 h26 M91,460 h26 M91,471 h26" stroke="rgba(255,255,255,.16)" stroke-width="2.6" stroke-linecap="round"/><rect x="89" y="437" width="12" height="47" rx="6" fill="rgba(255,255,255,.1)"/><circle cx="104" cy="441" r="2.2" fill="${suitA}"/></g>`;
  g += `<path d="M76,580 L108,580 C112,592 122,600 136,604 C146,607 148,618 142,626 L72,626 C66,616 68,596 76,580 Z" fill="#17191e" ${OL}/>
  <path d="M70,621 h74" stroke="#4a505c" stroke-width="5" stroke-linecap="round"/><path d="M78,594 h28" stroke="${suitA}" stroke-width="4" stroke-linecap="round"/><path d="M112,602 q12 4 24 5" stroke="rgba(255,255,255,.2)" stroke-width="2.2" fill="none" stroke-linecap="round"/>`;

  // ---- chaleco 3/4 ----
  g += `<path d="M128,118 C140,108 170,108 182,118 L180,134 C168,126 140,126 130,134 Z" fill="${D(suitC, .2)}" ${OL}/>`;
  g += `<path d="${vestP}" fill="${V.pat === 'carbon' ? `url(#${id('carb')})` : `url(#${id('vest')})`}" ${OL}/>`;
  g += `<g clip-path="url(#${id('vclip')})">`;
  g += `<path d="M86,158 C84,190 86,222 90,252 C92,274 94,290 96,302 L120,306 C116,276 112,240 112,206 C112,184 114,168 118,152 Z" fill="url(#${id('vside')})"/>`;
  g += `<path d="M206,150 C212,180 212,240 208,300 L216,300 L220,150 Z" fill="${D(vestC2, .25)}"/>`;
  if (V.pat === 'vault') g += `<path d="M110,236 L166,268 L216,240 L216,260 L166,288 L110,256 Z" fill="${vestC2}"/>`;
  else if (V.pat === 'race') g += `<rect x="134" y="120" width="9" height="200" fill="${vestC2}"/><rect x="186" y="120" width="7" height="200" fill="${vestC2}"/>`;
  else if (V.pat === 'band') g += `<rect x="80" y="192" width="150" height="18" fill="${vestC2}"/>`;
  else if (V.pat === 'carbon') g += `<path d="${vestP}" fill="none" stroke="${vestC2}" stroke-width="7"/>`;
  for (const y of [196, 238, 280]) g += `<path d="M84,${y - 2} C120,${y + 6} 170,${y + 8} 220,${y}" stroke="rgba(0,0,0,.3)" stroke-width="3" fill="none"/><path d="M84,${y + 1} C120,${y + 9} 170,${y + 11} 220,${y + 3}" stroke="rgba(255,255,255,.14)" stroke-width="2" fill="none"/>`;
  g += `<path d="M130,140 C122,180 122,230 128,290" stroke="rgba(255,255,255,.22)" stroke-width="8" stroke-linecap="round" fill="none"/>`;
  for (const y of [214, 258]) g += `<path d="M82,${y} C120,${y + 6} 170,${y + 8} 222,${y + 1} L222,${y + 11} C170,${y + 18} 120,${y + 16} 82,${y + 10} Z" fill="#14161a"/>`;
  g += `</g>`;
  g += `<path d="M166,154 C166,200 166,260 168,310" stroke="#23262c" stroke-width="5" fill="none"/><path d="M166,158 C166,200 166,260 168,306" stroke="#9aa3ae" stroke-width="1.6" stroke-dasharray="2 3" fill="none"/><rect x="162" y="162" width="8" height="15" rx="3" fill="url(#${id('metal')})" ${OL}/>`;
  for (const y of [222, 266]) g += `<rect x="152" y="${y - 3}" width="30" height="16" rx="5" fill="url(#${id('metal')})" ${OL}/><rect x="158" y="${y + 1}" width="18" height="8" rx="3" fill="#2a2e35"/>`;
  g += `<path d="M104,128 C106,116 114,110 126,111 L128,128 Z" fill="${D(vestC, .25)}" ${OL}/><path d="M200,130 C198,118 190,112 180,113 L180,128 Z" fill="${D(vestC, .35)}" ${OL}/>`;
  if (o.mir) g += `<g transform="translate(135 184) scale(-1,1) rotate(2) skewY(-4)"><text x="0" y="0" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="9.6" fill="${vestTxt}" stroke="rgba(0,0,0,.25)" stroke-width=".6">JET PILOT</text><path d="M-40,-9 l9,3.6 l-9,3.6 z" fill="${vestC2 === vestC ? vestTxt : vestC2}"/></g>`;
  else g += `<g transform="translate(120 184) rotate(-2) skewY(4)"><path d="M0,-10 l10,4 l-10,4 z" fill="${vestC2 === vestC ? vestTxt : vestC2}"/><text x="12" y="0" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="11" fill="${vestTxt}" stroke="rgba(0,0,0,.25)" stroke-width=".6">JET PILOT</text></g>`;
  if (V.name) g += `<rect x="172" y="190" width="40" height="12" rx="3" fill="rgba(10,12,18,.82)"/><text x="${o.mir ? -192 : 192}" y="199" text-anchor="middle" font-family="Arial,sans-serif" font-weight="800" font-size="6.8" fill="#fff" ${o.mir ? 'transform="scale(-1,1)"' : ''}>${V.name.toUpperCase()}</text>`;

  // ---- puño en la cadera (brazo de atrás) ----
  g += `<path d="M186,280 C184,270 192,264 202,266 C212,268 216,278 214,290 C212,300 202,306 194,304 C186,302 186,290 186,280 Z" fill="${D(glove, .1)}" ${OL}/><path d="M190,272 C198,268 206,270 212,276" stroke="${gloveA || suitA}" stroke-width="4.5" fill="none" stroke-linecap="round"/>${gloveA ? `<path d="M190,286 C196,282 206,282 212,286" stroke="${gloveA}" stroke-width="4" fill="none" stroke-linecap="round"/>` : ''}`;
  // ---- brazo de delante ----
  g += `<path d="${armN}" fill="${pat(S.pat) || `url(#${id('arm')})`}" ${OL}/>`;
  g += `<g clip-path="url(#${id('aclip')})"><path d="M60,146 C78,130 104,132 112,146 L104,184 C90,174 74,174 60,186 Z" fill="${suitA}"/><rect x="60" y="318" width="60" height="16" fill="${suitA}"/>
    <ellipse cx="80" cy="256" rx="14" ry="18" fill="${D(suitC === '#2a2d33' ? '#3a3f4a' : suitC, .38)}"/><path d="M74,248 q6 -3 12 1 M74,258 q6 -3 12 1 M74,268 q6 -3 12 1" stroke="rgba(255,255,255,.2)" stroke-width="2" fill="none"/>
    <path d="M82,176 C76,200 74,224 74,240" stroke="rgba(255,255,255,.24)" stroke-width="5" stroke-linecap="round" fill="none"/></g>`;
  g += `<path d="M80,334 C74,346 76,364 86,372 C96,378 106,370 106,358 L104,332 Z" fill="${glove}" ${OL}/><path d="M84,348 q4 10 10 14 M90,344 q4 10 10 14" stroke="rgba(255,255,255,.22)" stroke-width="1.8" fill="none"/>`;
  if (gloveA) g += `<path d="M79,338 L104,335 L105,343 L78,346 Z" fill="${gloveA}"/><path d="M82,352 C88,348 98,348 105,352 L105,360 C98,357 88,357 82,360 Z" fill="${gloveA}" opacity=".95"/><circle cx="90" cy="366" r="2" fill="${gloveA}"/><circle cx="97" cy="368" r="2" fill="${gloveA}"/>`;
  g += `<ellipse cx="156" cy="146" rx="48" ry="10" fill="rgba(0,0,0,.32)" filter="url(#${id('blur')})"/>`;

  // ---- casco 3/4 ----
  if (!o.noHelm) {
  if (!full) g += `<path d="M112,124 C124,140 170,142 186,128 L184,142 L116,142 Z" fill="#1d2027" ${OL}/>`;
  g += `<path d="${shellP}" fill="url(#${id('shell')})" ${OL}/>`;
  g += `<g clip-path="url(#${id('hclip')})">`;
  if (H.pat === 'flame') g += `<path d="M220,112 C196,104 174,112 156,104 C168,98 172,92 170,86 C156,92 140,90 124,80 C140,78 150,70 148,62 C132,70 114,66 96,54 L92,150 L220,150 Z" fill="${helmC2}"/><path d="M220,120 C200,114 182,120 162,114 C172,110 176,106 174,100 C162,104 148,104 134,98 L128,150 L220,150 Z" fill="#ffd21a" opacity=".9"/>`;
  else if (H.pat === 'twin') g += `<path d="M118,128 C108,80 124,34 168,20" stroke="${helmC2}" stroke-width="7" fill="none"/><path d="M132,128 C122,84 140,38 182,24" stroke="${helmC2}" stroke-width="7" fill="none"/>`;
  else if (H.pat === 'split') g += `<path d="M90,0 L150,0 C134,40 128,90 140,150 L90,150 Z" fill="${helmC2}"/>`;
  else if (H.pat === 'star') g += `<path d="M120,46 l7,15 16,2 -12,11 3,16 -14,-8 -14,8 3,-16 -12,-11 16,-2z" fill="${helmC2}"/><path d="M96,108 C140,118 180,116 214,100" stroke="${helmC2}" stroke-width="6" fill="none"/>`;
  else if (H.pat === 'carbon') g += `<rect x="90" y="0" width="140" height="150" fill="url(#${id('carb')})" opacity=".9"/><path d="M96,104 C140,114 180,112 214,96" stroke="${helmC2}" stroke-width="5" fill="none"/>`;
  else if (H.pat === 'chrome') g += `<path d="M126,128 C116,84 132,38 176,22" stroke="${helmC2}" stroke-width="7" fill="none"/>`;
  g += `<path d="M112,44 C126,28 146,22 166,22" stroke="rgba(255,255,255,.55)" stroke-width="5" stroke-linecap="round" fill="none"/><path d="M104,100 C102,80 104,64 110,52" stroke="rgba(130,225,255,.45)" stroke-width="3" stroke-linecap="round" fill="none"/></g>`;
  if (!full) {
    // visera de cross
    g += `<path d="M146,42 C174,26 214,26 240,36 L234,52 C212,46 178,46 156,54 Z" fill="url(#${id('shell')})" ${OL}/><path d="M150,38 C178,26 214,28 238,38" stroke="${helmC2}" stroke-width="4" fill="none"/>
    <text x="196" y="45" text-anchor="middle" font-family="Arial,sans-serif" font-weight="800" font-size="7.5" fill="${lum(helmC) > .6 ? '#15171c' : '#ffffff'}" transform="rotate(-4 196 45)">${H.brand === 'Arai' ? 'Arai' : 'alpinestars'}</text>`;
    // goma
    g += `<path d="M98,60 C112,56 128,58 142,62 L142,90 C128,88 112,88 99,90 Z" fill="url(#${id('strap')})" ${OL}/>`;
    const bt = GG.brand === 'oakley' ? 'OAKLEY' : GG.brand === '100' ? '100%' : 'alpinestars', tc = lum(GG.strap) > .6 ? '#15171c' : '#ffffff';
    g += `<g transform="translate(120 79) skewY(3)"><text x="0" y="0" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="${GG.brand === 'alpinestars' ? 6 : GG.brand === 'oakley' ? 6.8 : 8}" ${GG.brand === 'oakley' ? 'font-style="italic"' : ''} fill="${tc}">${bt}</text></g>`;
    // montura y lente (de 3/4)
    const fr = GG.frame || '#1b1d22';
    g += `<path d="M138,60 C160,52 198,50 216,56 C226,64 226,88 216,98 C204,102 190,102 184,96 C180,92 172,92 168,96 C162,102 148,102 140,96 C134,86 134,70 138,60 Z" fill="${fr}" ${OL}/>
    <path d="M143,64 C162,57 196,55 211,60 C218,67 218,86 211,93 C202,96 192,96 187,91 C182,86 170,86 165,91 C160,96 149,96 144,92 C139,84 139,72 143,64 Z" fill="url(#${id('lens')})"/>
    <path d="M152,62 L162,60 L152,92 L145,90 Z" fill="rgba(255,255,255,.48)"/><path d="M168,60 L172,59 L163,90 L160,90 Z" fill="rgba(255,255,255,.3)"/><circle cx="140" cy="77" r="4.2" fill="${GG.strap}" ${OL}/>`;
    // mentonera
    g += `<path d="M146,100 C162,106 196,106 216,100 C226,110 228,124 218,134 C204,142 176,144 160,138 C148,130 144,114 146,100 Z" fill="url(#${id('shell')})" ${OL}/>
    <path d="M158,112 l12 3 M156,120 l14 3 M158,128 l12 2" stroke="#15171c" stroke-width="3.4" stroke-linecap="round"/><path d="M196,112 h18 v16 c-5,5 -14,5 -18,0 z" fill="#2a2e35" ${OL}/><path d="M199,116 h12 M199,121 h12 M200,126 h10" stroke="#6c7480" stroke-width="1.8"/>`;
  } else {
    g += `<path d="M134,54 C160,46 198,46 214,56 C220,70 218,90 210,100 C190,104 156,104 138,98 C130,86 130,66 134,54 Z" fill="url(#${id('visor')})" ${OL}/><path d="M142,58 C164,52 192,52 206,58" stroke="rgba(255,255,255,.45)" stroke-width="4.5" stroke-linecap="round" fill="none"/><path d="M146,96 C170,99 192,98 206,94" stroke="rgba(120,200,255,.35)" stroke-width="3" fill="none" stroke-linecap="round"/>
    <circle cx="126" cy="78" r="7" fill="url(#${id('metal')})" ${OL}/><ellipse cx="150" cy="30" rx="8" ry="4" fill="#15171c"/><ellipse cx="184" cy="32" rx="6" ry="3.4" fill="#15171c"/>
    <rect x="178" y="114" width="22" height="11" rx="4" fill="#15171c"/><path d="M182,117 v5 M187,117 v5 M192,117 v5 M197,117 v5" stroke="#6c7480" stroke-width="1.5"/>
    <text x="172" y="140" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="13" fill="${lum(helmC) > .6 && !chrome ? '#c8102e' : '#ffffff'}">Arai</text>`;
  }
  }
  g += `<path d="M212,200 C216,240 214,270 210,298" stroke="rgba(130,225,255,.45)" stroke-width="2.4" fill="none" stroke-linecap="round"/>`;
  return `<svg viewBox="0 0 300 640" xmlns="http://www.w3.org/2000/svg">${defs}${g}</svg>`;
}
if (typeof module !== 'undefined') module.exports = { pilot34SVG, LENSES };
