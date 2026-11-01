// Casco de motocross con proporciones reales, 3/4 mirando a la izquierda — boceto
function helmetMX(o, uid) {
  const H = o.helm, GG = o.gog || { brand: 'oakley', strap: '#1d2027', lens: 'prizm' };
  const hx = (c) => { c = c.replace('#', ''); return [parseInt(c.slice(0, 2), 16), parseInt(c.slice(2, 4), 16), parseInt(c.slice(4, 6), 16)]; };
  const mix = (a, b, t) => { const A = hx(a), B = hx(b); return '#' + A.map((v, i) => Math.round(v + (B[i] - v) * t).toString(16).padStart(2, '0')).join(''); };
  const L = (c, t) => mix(c, '#ffffff', t), D = (c, t) => mix(c, '#000000', t);
  const lum = (c) => { const [r, g, b] = hx(c); return (r * .3 + g * .59 + b * .11) / 255; };
  const id = (n) => n + uid;
  const OL = 'stroke="rgba(8,10,16,.7)" stroke-width="2" stroke-linejoin="round"';
  const c = H.c, c2 = H.c2 || '#ffffff', c3 = H.c3 || '#e6f01a', arai = H.brand === 'Arai', peakC = H.peak || c, chinC = H.chin || c;
  const logoC = lum(c) > .62 ? '#15171c' : '#ffffff';
  const LZ = (typeof LENSES !== 'undefined' ? LENSES : {})[GG.lens] || ['#ffd166', '#ff7a3c', '#e2366e', '#5b3cff'];
  const aStar = (x, y, r, col, rot, sw) => { let p = ''; for (let k = 0; k < 10; k++) { const a = -Math.PI / 2 + k * Math.PI / 5, d = k % 2 ? r * .4 : r; p += (k ? 'L' : 'M') + (Math.cos(a) * d).toFixed(1) + ',' + (Math.sin(a) * d).toFixed(1); } return `<g transform="translate(${x} ${y}) rotate(${rot || -12}) skewX(-12)"><path d="${p}Z" fill="${sw ? 'none' : col}" ${sw ? `stroke="${col}" stroke-width="${sw}" stroke-linejoin="round"` : ''}/><path d="M${-r * .5},${r * .34} C${-r * 1.2},${r * .9} ${-r * 2.2},${r * .9} ${-r * 3},${r * .5} C${-r * 2.1},${r * 1.25} ${-r * 1.1},${r * 1.3} ${-r * .2},${r * .62} Z" fill="${col}"/></g>`; };
  const star5 = (x, y, r, col, sw) => { let p = ''; for (let k = 0; k < 10; k++) { const a = -Math.PI / 2 + k * Math.PI / 5 + .2, d = k % 2 ? r * .42 : r; p += (k ? 'L' : 'M') + (x + Math.cos(a) * d).toFixed(1) + ',' + (y + Math.sin(a) * d).toFixed(1); } return `<path d="${p}Z" fill="${sw ? 'none' : col}" ${sw ? `stroke="${col}" stroke-width="${sw}" stroke-linejoin="round"` : ''}/>`; };

  // formas principales
  const shellP = 'M82,64 C84,40 100,22 124,10 C150,0 200,6 230,22 C246,34 254,60 254,90 C254,110 252,124 250,134 C222,156 198,170 178,180 C152,192 128,200 104,206 C90,210 76,206 70,196 C66,184 70,160 76,140 C77,132 78,126 78,121 C78,100 80,80 82,64 Z';
  const chinP = 'M92,120 C120,128 152,134 180,136 C188,140 192,146 194,152 C184,164 176,172 168,180 C148,192 128,200 104,206 C90,210 76,206 70,196 C66,184 70,160 76,140 C77,132 78,126 78,121 Z';
  const portP = 'M84,64 C120,58 162,60 186,66 C192,82 192,102 188,114 C186,124 184,130 180,136 C150,134 120,128 92,120 C88,102 85,84 84,64 Z';
  const peakTop = 'M10,34 C46,16 88,2 124,-2 C142,-4 156,-2 166,4 C176,12 182,20 186,30 C172,38 160,46 150,56 C132,62 112,62 92,58 C64,52 34,44 10,34 Z';
  const peakEdge = 'M10,34 C34,44 64,52 92,58 C112,62 132,62 150,56 L150,66 C132,71 110,71 90,67 C62,61 32,52 12,42 Z';

  let d = `<defs>
  <radialGradient id="${id('sh')}" cx=".42" cy=".2" r="1"><stop offset="0" stop-color="${L(c, .55)}"/><stop offset=".25" stop-color="${L(c, .18)}"/><stop offset=".62" stop-color="${c}"/><stop offset="1" stop-color="${D(c, .5)}"/></radialGradient>
  <linearGradient id="${id('ch')}" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="${L(chinC, .3)}"/><stop offset=".5" stop-color="${chinC}"/><stop offset="1" stop-color="${D(chinC, .45)}"/></linearGradient>
  <linearGradient id="${id('pk')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${L(peakC, .4)}"/><stop offset=".6" stop-color="${peakC}"/><stop offset="1" stop-color="${D(peakC, .25)}"/></linearGradient>
  <linearGradient id="${id('ln')}" x1="0" x2="1" y1="0" y2="1">${LZ.map((q, i) => `<stop offset="${i / (LZ.length - 1)}" stop-color="${q}"/>`).join('')}</linearGradient>
  <linearGradient id="${id('st')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${L(GG.strap, .25)}"/><stop offset=".5" stop-color="${GG.strap}"/><stop offset="1" stop-color="${D(GG.strap, .35)}"/></linearGradient>
  <linearGradient id="${id('fg')}" x1="0" x2="1"><stop offset="0" stop-color="#ff7a1a"/><stop offset=".5" stop-color="#ff3f8e"/><stop offset="1" stop-color="#7a5cff"/></linearGradient>
  <pattern id="${id('cb')}" width="7" height="7" patternUnits="userSpaceOnUse"><rect width="7" height="7" fill="#22252b"/><rect width="3.5" height="3.5" fill="#363a42"/><rect x="3.5" y="3.5" width="3.5" height="3.5" fill="#363a42"/></pattern>
  <clipPath id="${id('cs')}"><path d="${shellP}"/></clipPath>
  <clipPath id="${id('cc')}"><path d="${chinP}"/></clipPath>
  <clipPath id="${id('ca')}"><path d="${shellP}"/><path d="${chinP}"/></clipPath>
  </defs>`;

  let g = '';
  // collarín
  g += `<path d="M150,194 C182,182 212,164 240,144 L238,154 C212,172 184,190 156,203 Z" fill="#17191e" ${OL}/>`;
  // carcasa
  g += `<path d="${shellP}" fill="url(#${id('sh')})" ${OL}/>`;
  // gráficos del casco (sobre carcasa y mentonera)
  let gr = '';
  const P = H.pat;
  if (P === 'carbon') gr += `<rect x="60" y="0" width="200" height="210" fill="url(#${id('cb')})" opacity=".92"/><path d="M60,150 C120,160 200,140 260,100" stroke="${c2}" stroke-width="5" fill="none"/>`;
  else if (P === 'jettson') gr += `<path d="M150,92 L252,58 L252,90 L160,124 Z" fill="#1d2027"/><path d="M120,140 L252,100 L252,112 L124,152 Z" fill="${c2}"/><path d="M200,20 L246,42 L242,64 L204,48 Z" fill="#1d2027"/>${aStar(220, 128, 14, '#1d2027', -16, 2.4)}`;
  else if (P === 'blaster') gr += `<path d="M90,140 C150,150 210,130 260,96 L260,210 L90,210 Z" fill="${c2}"/><path d="M90,136 C150,146 210,126 260,92" stroke="#ff3f8e" stroke-width="6" fill="none"/><path d="M198,14 L252,32 L252,60 L212,44 Z" fill="#ff3f8e"/>${aStar(222, 128, 17, c3, -12)}`;
  else if (P === 'bigstar') gr += `<path d="M100,176 C160,170 220,140 260,110 L260,124 C220,156 160,186 102,190 Z" fill="#f4f6f9"/><path d="M198,12 L252,28 L252,42 L206,28 Z" fill="#f4f6f9"/>${aStar(222, 124, 19, '#f4f6f9', -10)}`;
  else if (P === 'force') gr += `<path d="M100,170 C160,164 220,136 260,104 L260,112 C220,146 160,176 102,180 Z" fill="url(#${id('fg')})"/>${aStar(222, 124, 18, `url(#${id('fg')})`, -12)}`;
  else if (P === 'fluor') gr += `<path d="M90,120 C150,124 210,104 260,72 L260,210 L90,210 Z" fill="${c2}"/><path d="M152,42 l40,-18 M158,54 l44,-20 M164,66 l46,-22" stroke="#7be35a" stroke-width="5" stroke-linecap="round"/>${aStar(224, 132, 13, '#15171c', -12)}`;
  else if (P === 'yam') gr += `<path d="M90,150 C150,160 210,140 260,104 L260,210 L90,210 Z" fill="#f4f6f9"/><path d="M90,146 C150,156 210,136 260,100" stroke="#7fc8ff" stroke-width="5" fill="none"/><path d="M198,14 L252,30 L252,56 L208,40 Z" fill="#f4f6f9"/>${aStar(222, 128, 17, '#1e4fd8', -10)}`;
  else if (P === 'flame') gr += `<path d="M90,200 C120,160 150,170 170,146 C166,160 170,166 178,168 C186,146 206,138 216,116 C216,134 222,142 234,144 C238,124 248,116 258,106 L262,210 Z" fill="${c2}"/><path d="M110,210 C136,184 158,188 174,168 C174,178 180,182 190,182 C196,166 210,158 220,144 C222,156 230,162 240,162 L262,210 Z" fill="#ffd21a" opacity=".9"/>`;
  else if (P === 'stars') gr += `<path d="M200,8 L260,8 L260,112 L218,124 C210,92 204,50 200,8 Z" fill="${c2}"/><path d="M90,160 C150,170 210,160 260,120 L260,210 L90,210 Z" fill="#1e3fae"/>${star5(160, 82, 28, c3, 3)}${star5(222, 52, 18, c3, 3)}<path d="M96,168 C150,178 210,166 256,132 M100,178 C154,188 214,176 258,142" stroke="${c3}" stroke-width="3" fill="none"/>`;
  else if (P === 'frog') gr += `<path d="M60,58 C130,74 200,66 260,48 L260,80 C200,98 130,104 60,90 Z" fill="#2b1f8f"/><path d="M60,94 C130,108 200,100 260,84 L260,116 C200,132 130,138 60,126 Z" fill="${c2}"/><path d="M60,128 C130,142 200,134 260,118 L260,210 L60,210 Z" fill="#6a2bd8"/><path d="M60,56 C130,72 200,64 260,46 M60,92 C130,106 200,98 260,82 M60,126 C130,140 200,132 260,116 M70,160 C130,172 200,160 260,140" stroke="${c3}" stroke-width="3.4" fill="none"/>`;
  else if (P === 'blocks') gr += `<path d="M100,20 L160,8 L150,60 L102,72 Z" fill="#1d2027"/><path d="M160,8 L216,14 L206,64 L150,60 Z" fill="${c2}"/><path d="M216,14 L254,30 L254,82 L206,64 Z" fill="#f4f6f9"/><path d="M102,72 L150,60 L146,112 L98,122 Z" fill="#1e5eff"/><path d="M150,60 L206,64 L200,114 L146,112 Z" fill="#1d2027"/><path d="M206,64 L254,82 L254,122 L200,114 Z" fill="${c2}"/><path d="M98,122 L146,112 L140,170 L90,180 Z" fill="${c2}"/><path d="M146,112 L200,114 L196,170 L140,170 Z" fill="#f4f6f9"/><path d="M200,114 L254,122 L254,180 L196,170 Z" fill="#1e5eff"/><path d="M128,92 L168,86 L164,102 L126,106 Z" fill="${c3}"/>`;
  else gr += `<path d="M200,30 C222,44 240,70 244,104 L222,112 C220,86 214,62 204,46 Z" fill="${D(c, .22)}"/><path d="M214,120 L246,102 L248,112 L218,130 Z M206,134 L244,114 L244,124 L210,144 Z" fill="${c2}" opacity=".95"/>`;
  // facetas de la carcasa (aristas reales)
  g += `<g clip-path="url(#${id('cs')})">${gr}<path d="M120,40 C150,22 188,14 214,20 L222,40 C190,36 156,42 128,54 Z" fill="rgba(255,255,255,.16)"/>
    <path d="M186,32 C204,52 212,90 206,132" stroke="rgba(0,0,0,.24)" stroke-width="2.2" fill="none"/><path d="M206,14 C232,30 246,58 248,100" stroke="rgba(255,255,255,.3)" stroke-width="2.4" fill="none"/>
    <path d="M190,40 l16,-4 l2,10 l-16,4 z" fill="#5a606b" stroke="#15171c" stroke-width="1"/><path d="M193,42 l10,-2 M194,46 l10,-2" stroke="#2a2e35" stroke-width="1"/>
    <path d="M232,40 l10,6 M234,52 l12,6" stroke="${D(c, .35)}" stroke-width="6" stroke-linecap="round"/></g>`;
  // goma de las gafas por el lateral
  g += `<g clip-path="url(#${id('cs')})"><path d="M180,74 C204,70 232,72 256,80 L256,104 C232,98 204,96 180,100 Z" fill="url(#${id('st')})" ${OL}/></g>`;
  const bt = GG.brand === 'oakley' ? 'OAKLEY' : GG.brand === '100' ? '100%' : 'alpinestars', tc = lum(GG.strap) > .6 ? '#15171c' : '#ffffff';
  g += `<text x="222" y="92" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="${GG.brand === '100' ? 11 : 9}" ${GG.brand === 'oakley' ? 'font-style="italic" letter-spacing="1"' : ''} fill="${tc}" transform="rotate(5 216 92)">${bt}</text>`;
  // hueco del ojo y gafas
  g += `<path d="${portP}" fill="#0c0e13" ${OL}/>`;
  const fr = GG.frame || '#1b1d22';
  g += `<path d="M82,70 C110,62 158,62 188,70 C196,84 194,104 186,114 C174,120 160,120 152,114 C148,110 138,110 134,114 C124,120 104,120 94,114 C84,102 80,86 82,70 Z" fill="${fr}" ${OL}/>
  <path d="M89,74 C114,67 156,67 181,74 C187,84 186,102 180,110 C170,115 160,115 154,110 C149,105 136,105 131,110 C122,115 106,115 99,111 C91,102 89,88 89,74 Z" fill="url(#${id('ln')})"/>
  <path d="M102,72 L118,70 L104,112 L96,110 Z" fill="rgba(255,255,255,.45)"/><path d="M124,70 L130,70 L117,112 L112,112 Z" fill="rgba(255,255,255,.28)"/>
  <circle cx="187" cy="92" r="5" fill="${GG.strap}" ${OL}/>`;
  // mentonera grande en punta
  g += `<path d="${chinP}" fill="url(#${id('ch')})" ${OL}/>`;
  g += `<g clip-path="url(#${id('cc')})">${P && !['flame', 'stars', 'blocks', 'frog'].includes(P) ? '' : gr}
    <path d="M98,124 C124,138 170,138 206,118" stroke="rgba(255,255,255,.3)" stroke-width="2.4" fill="none"/><path d="M96,150 C130,160 170,152 210,134" stroke="rgba(0,0,0,.25)" stroke-width="2" fill="none"/></g>`;
  if (arai) g += `<path d="M70,176 C70,164 78,154 90,150 L100,192 C90,200 80,200 74,194 Z" fill="#2a2e35" ${OL}/><path d="M84,162 h14 M83,170 h18 M84,178 h18 M86,186 h14" stroke="#8a93a0" stroke-width="1.6" stroke-dasharray="2 2"/><rect x="112" y="166" width="18" height="14" rx="3" fill="#2a2e35" ${OL}/><path d="M115,170 h12 M115,175 h12" stroke="#8a93a0" stroke-width="1.4" stroke-dasharray="2 2"/>`;
  else g += `<path d="M78,122 L106,126 L108,152 L80,154 Z" fill="${c2}" ${OL}/><path d="M86,132 l8,-4 l8,4 M86,140 l8,-4 l8,4 M86,148 l8,-4 l8,4" stroke="rgba(0,0,0,.4)" stroke-width="1.8" fill="none"/>
    <path d="M70,182 L94,174 L102,202 L84,207 C76,202 70,194 70,182 Z" fill="${c2}" ${OL}/>
    <path d="M118,150 L174,160 L170,172 L114,162 Z" fill="#15171c" ${OL}/><path d="M124,156 h40 M122,162 h40" stroke="#4a505c" stroke-width="1.4" stroke-dasharray="3 2"/>
    <circle cx="176" cy="142" r="3.4" fill="#15171c"/><circle cx="196" cy="152" r="3.4" fill="#15171c"/>`;
  // logo lateral
  if (arai) g += `<g transform="translate(214 146) rotate(-34)"><ellipse cx="0" cy="0" rx="29" ry="14" fill="${H.badge || '#15171c'}" stroke="${H.badge === '#e6f01a' ? '#15171c' : '#f4f6f9'}" stroke-width="2.4"/><text x="0" y="3" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="15" fill="${H.badge === '#e6f01a' ? '#15171c' : '#ffffff'}">Arai</text><text x="6" y="10" text-anchor="middle" font-family="Arial,sans-serif" font-weight="800" font-size="4.4" letter-spacing=".6" fill="${H.badge === '#e6f01a' ? '#15171c' : '#ffffff'}">HELMET</text></g>`;
  else if (!P || P === 'flame') g += `<g clip-path="url(#${id('ca')})"><text x="204" y="164" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="21" letter-spacing="-.8" fill="${logoC}" stroke="rgba(0,0,0,.2)" stroke-width=".8" transform="rotate(-36 204 164)">alpinestars</text></g>${aStar(226, 122, 10, logoC, -14)}`;
  // visera larga y gruesa con rejillas
  g += `<path d="${peakTop}" fill="url(#${id('pk')})" ${OL}/><path d="${peakEdge}" fill="${D(peakC, .45)}" ${OL}/>`;
  g += `<path d="M14,33 C52,15 94,3 126,0" stroke="${c2}" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M64,40 C96,30 140,16 176,20" stroke="rgba(255,255,255,.3)" stroke-width="2" fill="none"/><path d="M150,52 C162,42 174,34 184,30" stroke="rgba(0,0,0,.3)" stroke-width="2" fill="none"/>`;
  g += [[30, 40], [38, 37], [46, 34], [34, 46], [42, 43], [50, 40]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="2.4" ry="1.5" fill="#15171c"/>`).join('');
  g += [[126, 38], [136, 40], [146, 36], [131, 46], [141, 47]].map(([x, y]) => `<path d="M${x - 4},${y} l4,-3 4,3 -4,3z" fill="${D(peakC, .28)}"/>`).join('');
  g += arai ? `<g transform="translate(100 26) rotate(-15)"><ellipse rx="15" ry="7" fill="#15171c"/><text y="3" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="9" fill="#ffffff">Arai</text></g>` : `<text x="104" y="26" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="11" fill="${lum(peakC) > .62 ? '#15171c' : '#ffffff'}" transform="rotate(-17 104 26)">alpinestars</text>`;
  g += `<circle cx="176" cy="30" r="3.6" fill="#15171c"/><circle cx="176" cy="30" r="1.4" fill="#8a93a0"/>`;
  if (P === 'frog') g += `<g transform="translate(150 22) rotate(-14)"><ellipse cx="0" cy="0" rx="14" ry="7" fill="#7be35a" stroke="#15171c" stroke-width="1.2"/><circle cx="-10" cy="-6" r="4" fill="#7be35a" stroke="#15171c" stroke-width="1.2"/><circle cx="-10" cy="-6" r="1.6" fill="#e3202b"/><circle cx="-2" cy="-7" r="4" fill="#7be35a" stroke="#15171c" stroke-width="1.2"/><circle cx="-2" cy="-7" r="1.6" fill="#e3202b"/><path d="M8,4 l8,6 M-6,5 l-6,7" stroke="#7be35a" stroke-width="2.6" stroke-linecap="round"/></g>`;
  return { defs: d, body: `<g transform="translate(0 14) scale(1 .88)">${g}</g>` };
}
if (typeof module !== 'undefined') module.exports = { helmetMX };
