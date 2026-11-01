// Casco de 3/4 mirando a la izquierda (estilo foto Alpinestars / Arai) — boceto
function helmetL(o, uid) {
  const H = o.helm, GG = o.gog || { brand: 'oakley', strap: '#1d2027', lens: 'prizm' };
  const hx = (c) => { c = c.replace('#', ''); return [parseInt(c.slice(0, 2), 16), parseInt(c.slice(2, 4), 16), parseInt(c.slice(4, 6), 16)]; };
  const mix = (a, b, t) => { const A = hx(a), B = hx(b); return '#' + A.map((v, i) => Math.round(v + (B[i] - v) * t).toString(16).padStart(2, '0')).join(''); };
  const L = (c, t) => mix(c, '#ffffff', t), D = (c, t) => mix(c, '#000000', t);
  const lum = (c) => { const [r, g, b] = hx(c); return (r * .3 + g * .59 + b * .11) / 255; };
  const id = (n) => n + uid;
  const OL = 'stroke="rgba(8,12,22,.6)" stroke-width="2.2" stroke-linejoin="round"';
  const c = H.c, c2 = H.c2 || '#ffffff', chrome = H.pat === 'chrome', full = H.st === 'full', arai = H.brand === 'Arai', c3 = H.c3 || '#e6f01a', chinC = H.chin || null;
  const logoC = chrome ? '#1d2027' : lum(c) > .62 ? '#15171c' : '#ffffff';
  const LZ = (typeof LENSES !== 'undefined' ? LENSES : {})[GG.lens] || ['#ffd166', '#ff7a3c', '#e2366e', '#5b3cff'];
  const star = (x, y, r, col) => { let p = ''; for (let k = 0; k < 10; k++) { const a = -Math.PI / 2 + k * Math.PI / 5 + .25, d = k % 2 ? r * .42 : r; p += (k ? 'L' : 'M') + (x + Math.cos(a) * d).toFixed(1) + ',' + (y + Math.sin(a) * d).toFixed(1); } return `<path d="${p}Z" fill="${col}"/>`; };
  const aStar = (x, y, r, col, rot, sw) => { let p = ''; for (let k = 0; k < 10; k++) { const a = -Math.PI / 2 + k * Math.PI / 5, d = k % 2 ? r * .4 : r; p += (k ? 'L' : 'M') + (Math.cos(a) * d).toFixed(1) + ',' + (Math.sin(a) * d).toFixed(1); } return `<g transform="translate(${x} ${y}) rotate(${rot || -12}) skewX(-12)"><path d="${p}Z" fill="${sw ? 'none' : col}" ${sw ? `stroke="${col}" stroke-width="${sw}" stroke-linejoin="round"` : ''}/><path d="M${-r * .5},${r * .34} C${-r * 1.2},${r * .9} ${-r * 2.2},${r * .9} ${-r * 3},${r * .5} C${-r * 2.1},${r * 1.25} ${-r * 1.1},${r * 1.3} ${-r * .2},${r * .62} Z" fill="${col}"/></g>`; };
  const shellP = full ? 'M96,86 C92,48 120,18 160,16 C200,14 232,40 236,76 C240,108 228,134 206,148 C186,158 150,160 126,152 C106,144 96,120 96,86 Z'
    : 'M108,44 C126,24 160,14 192,18 C220,22 238,44 240,72 C242,98 236,122 222,138 C210,150 190,154 172,152 L140,150 C122,146 110,134 104,118 C100,100 100,70 108,44 Z';
  let d = `<defs>
  ${chrome
    ? `<radialGradient id="${id('sh')}" cx=".38" cy=".22" r=".95"><stop offset="0" stop-color="#ffffff"/><stop offset=".28" stop-color="#e3e9f0"/><stop offset=".5" stop-color="#8d99a8"/><stop offset=".72" stop-color="#f2f6fa"/><stop offset="1" stop-color="#5d6876"/></radialGradient>`
    : `<radialGradient id="${id('sh')}" cx=".36" cy=".22" r=".95"><stop offset="0" stop-color="${L(c, .5)}"/><stop offset=".3" stop-color="${L(c, .14)}"/><stop offset=".7" stop-color="${c}"/><stop offset="1" stop-color="${D(c, .5)}"/></radialGradient>`}
  <linearGradient id="${id('pk')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${chrome ? '#ffffff' : L(H.peak || c, .32)}"/><stop offset=".7" stop-color="${chrome ? '#aab4c0' : (H.peak || c)}"/><stop offset="1" stop-color="${D(H.peak || c, .3)}"/></linearGradient>
  <linearGradient id="${id('ln')}" x1="0" x2="1" y1="0" y2="1">${LZ.map((q, i) => `<stop offset="${i / (LZ.length - 1)}" stop-color="${q}"/>`).join('')}</linearGradient>
  <linearGradient id="${id('st')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${L(GG.strap, .22)}"/><stop offset=".5" stop-color="${GG.strap}"/><stop offset="1" stop-color="${D(GG.strap, .35)}"/></linearGradient>
  <linearGradient id="${id('vi')}" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#4a5f85"/><stop offset=".45" stop-color="#16202f"/><stop offset="1" stop-color="#070b12"/></linearGradient>
  <linearGradient id="${id('mt')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#f1f4f8"/><stop offset=".5" stop-color="#a7afba"/><stop offset="1" stop-color="#6c7480"/></linearGradient>
  <pattern id="${id('cb')}" width="7" height="7" patternUnits="userSpaceOnUse"><rect width="7" height="7" fill="#22252b"/><rect width="3.5" height="3.5" fill="#363a42"/><rect x="3.5" y="3.5" width="3.5" height="3.5" fill="#363a42"/></pattern>
  <clipPath id="${id('cl')}"><path d="${shellP}"/></clipPath><clipPath id="${id('cl2')}"><path d="${shellP}"/><path d="M90,114 C104,120 128,124 156,122 L180,116 C188,128 184,144 172,152 L128,156 C108,156 90,150 76,140 C72,130 80,120 90,114 Z"/></clipPath></defs>`;
  let g = '';
  // collarín
  g += `<path d="M120,148 C140,160 182,162 210,146 L208,158 C182,172 140,170 118,160 Z" fill="#17191e" ${OL}/>`;
  // carcasa
  g += `<path d="${shellP}" fill="url(#${id('sh')})" ${OL}/>`;
  g += `<g clip-path="url(#${id('cl')})">`;
  if (H.pat === 'carbon') g += `<rect x="90" y="0" width="160" height="170" fill="url(#${id('cb')})" opacity=".92"/>`;
  // facetas tipo foto: panel claro arriba y panel oscuro detrás
  g += `<path d="M118,40 C140,24 172,18 200,22 L210,44 C184,44 152,48 128,56 Z" fill="${chrome ? 'rgba(255,255,255,.35)' : L(c, .18)}" opacity=".85"/>`;
  g += `<path d="M206,40 C224,52 236,72 238,96 L214,104 C214,82 210,60 200,46 Z" fill="${chrome ? 'rgba(0,0,0,.12)' : D(c, .22)}"/>`;
  if (H.pat === 'flame') g += `<path d="M110,150 C130,128 150,134 166,116 C162,128 166,134 172,136 C178,118 196,112 206,94 C206,110 212,118 222,120 C226,104 236,98 244,90 L250,170 L100,170 Z" fill="${c2}"/><path d="M130,160 C146,144 160,148 172,134 C172,144 178,148 186,148 C192,134 204,128 212,116 C214,128 220,134 228,134 L250,170 L120,170 Z" fill="#ffd21a" opacity=".9"/>`;
  else if (H.pat === 'twin') g += `<path d="M150,10 C176,30 196,70 196,160" stroke="${c2}" stroke-width="8" fill="none"/><path d="M168,8 C194,30 214,70 214,160" stroke="${c2}" stroke-width="8" fill="none"/>`;
  else if (H.pat === 'split') g += `<path d="M196,0 C186,40 186,100 200,170 L260,170 L260,0 Z" fill="${c2}"/>`;
  else if (H.pat === 'star') g += star(212, 72, 26, c2);
  else if (H.pat === 'chrome') g += `<path d="M150,10 C178,30 200,70 202,160" stroke="${c2}" stroke-width="9" fill="none"/>`;
  else if (H.pat === 'carbon') g += `<path d="M150,10 C178,30 200,70 202,160" stroke="${c2}" stroke-width="5" fill="none"/>`;
  else if (H.pat === 'jettson') g += `<path d="M150,90 L250,60 L250,92 L160,120 Z" fill="#1d2027"/><path d="M120,124 L250,96 L250,108 L124,136 Z" fill="${c2}"/><path d="M196,20 L240,40 L236,60 L200,46 Z" fill="#1d2027"/>${aStar(216, 124, 15, '#1d2027', -14, 2.4)}`;
  else if (H.pat === 'blaster') g += `<path d="M100,104 C150,118 210,112 260,90 L260,170 L100,170 Z" fill="${c2}"/><path d="M100,100 C150,114 210,108 260,86" stroke="#ff3f8e" stroke-width="6" fill="none"/><path d="M196,14 L250,30 L250,58 L210,44 Z" fill="#ff3f8e"/><path d="M110,30 C130,22 150,22 160,26 L150,40 C136,38 122,40 112,44 Z" fill="rgba(160,170,190,.4)"/>${aStar(216, 126, 19, c3, -10)}`;
  else if (H.pat === 'bigstar') g += `<path d="M110,136 C160,146 210,138 260,116 L260,128 C210,150 160,158 112,148 Z" fill="#f4f6f9"/><path d="M196,12 L250,26 L250,40 L204,28 Z" fill="#f4f6f9"/>${aStar(216, 124, 21, '#f4f6f9', -8)}`;
  else if (H.pat === 'force') g += `<defs><linearGradient id="${id('fg')}" x1="0" x2="1"><stop offset="0" stop-color="#ff7a1a"/><stop offset=".5" stop-color="#ff3f8e"/><stop offset="1" stop-color="#7a5cff"/></linearGradient></defs><path d="M110,120 C160,132 210,126 260,104 L260,112 C210,136 160,142 112,130 Z" fill="url(#${id('fg')})"/>${aStar(216, 124, 20, `url(#${id('fg')})`, -10)}`;
  else if (H.pat === 'fluor') g += `<path d="M100,96 C150,106 200,100 260,76 L260,170 L100,170 Z" fill="${c2}"/><path d="M150,40 l40,-18 M156,52 l44,-20 M162,64 l46,-22" stroke="#7be35a" stroke-width="5" stroke-linecap="round"/>${aStar(218, 128, 14, '#15171c', -10)}`;
  else if (H.pat === 'yam') g += `<path d="M100,110 C150,124 210,118 260,96 L260,170 L100,170 Z" fill="#f4f6f9"/><path d="M100,108 C150,122 210,116 260,94" stroke="#7fc8ff" stroke-width="5" fill="none"/><path d="M196,14 L250,30 L250,56 L206,40 Z" fill="#f4f6f9"/>${aStar(216, 124, 20, '#1e4fd8', -8)}`;
  else if (H.pat === 'stars') g += `<path d="M196,10 L260,10 L260,110 L214,120 C206,90 200,50 196,10 Z" fill="${c2}"/><path d="M100,118 C150,130 200,128 260,112 L260,170 L100,170 Z" fill="#1e3fae"/>
    ${[[150, 70, 30], [212, 46, 20], [120, 40, 16]].map(([x, y, r]) => { let p = ''; for (let k = 0; k < 10; k++) { const a = -Math.PI / 2 + k * Math.PI / 5 + .2, d = k % 2 ? r * .42 : r; p += (k ? 'L' : 'M') + (x + Math.cos(a) * d).toFixed(1) + ',' + (y + Math.sin(a) * d).toFixed(1); } return `<path d="${p}Z" fill="none" stroke="${c3}" stroke-width="3" stroke-linejoin="round"/>`; }).join('')}
    <path d="M110,128 C160,140 210,136 250,120 M118,138 C168,150 214,146 252,130" stroke="${c3}" stroke-width="3" fill="none"/>`;
  else if (H.pat === 'frog') g += `<rect x="90" y="0" width="170" height="170" fill="${c}"/><path d="M90,60 C150,70 210,66 260,54 L260,84 C210,96 150,98 90,90 Z" fill="#2b1f8f"/><path d="M90,96 C150,104 210,100 260,88 L260,118 C210,130 150,134 90,124 Z" fill="${c2}"/><path d="M90,126 C150,136 210,132 260,120 L260,170 L90,170 Z" fill="#6a2bd8"/>
    <path d="M90,58 C150,68 210,64 260,52 M90,94 C150,102 210,98 260,86 M90,124 C150,134 210,130 260,118 M100,150 C150,158 210,152 260,140" stroke="${c3}" stroke-width="3.4" fill="none"/>`;
  else if (H.pat === 'blocks') g += `<path d="M100,20 L160,10 L150,60 L104,70 Z" fill="#1d2027"/><path d="M160,10 L214,16 L206,64 L150,60 Z" fill="${c2}"/><path d="M214,16 L250,30 L250,80 L206,64 Z" fill="#f4f6f9"/><path d="M104,70 L150,60 L146,110 L100,118 Z" fill="#1e5eff"/><path d="M150,60 L206,64 L200,112 L146,110 Z" fill="#1d2027"/><path d="M206,64 L250,80 L250,120 L200,112 Z" fill="${c2}"/><path d="M100,118 L146,110 L140,160 L96,160 Z" fill="${c2}"/><path d="M146,110 L200,112 L196,160 L140,160 Z" fill="#f4f6f9"/><path d="M200,112 L250,120 L250,170 L196,170 Z" fill="#1e5eff"/><path d="M130,90 L170,84 L166,100 L128,104 Z" fill="${c3}"/>`;
  // franjas traseras
  if (!['stars', 'frog', 'blocks', 'jettson', 'blaster', 'bigstar', 'force', 'fluor', 'yam'].includes(H.pat) && !(arai && !H.pat)) g += `<path d="M214,116 L240,100 L242,110 L218,126 Z M206,130 L238,112 L238,122 L210,140 Z" fill="${c2}" opacity=".95"/>`;
  // brillo
  g += `<path d="M130,30 C150,20 176,16 200,20" stroke="rgba(255,255,255,.6)" stroke-width="5" stroke-linecap="round" fill="none"/>`;
  g += `</g>`;
  if (!full) {
    // logo grande lateral
    if (!arai && (!H.pat || H.pat === 'radium')) g += aStar(212, 48, 10, logoC, -10);
    // goma de las gafas por el lateral
    g += `<g clip-path="url(#${id('cl')})"><path d="M172,68 C196,64 222,66 242,74 L242,98 C222,92 196,90 172,94 Z" fill="url(#${id('st')})" ${OL}/></g>`;
    const bt = GG.brand === 'oakley' ? 'OAKLEY' : GG.brand === '100' ? '100%' : 'alpinestars', tc = lum(GG.strap) > .6 ? '#15171c' : '#ffffff';
    g += `<text x="210" y="86" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="${GG.brand === '100' ? 11 : 9}" ${GG.brand === 'oakley' ? 'font-style="italic" letter-spacing="1"' : ''} fill="${tc}" transform="rotate(4 210 86)">${bt}</text>`;
    // gafas en el ojo del casco
    const fr = GG.frame || '#1b1d22';
    g += `<path d="M80,68 C100,60 148,56 176,62 C186,74 186,98 178,110 C166,116 150,116 142,110 C138,106 130,106 126,110 C116,116 98,116 88,110 C78,98 76,82 80,68 Z" fill="${fr}" ${OL}/>
    <path d="M87,72 C104,65 146,62 170,66 C177,76 177,96 171,105 C161,110 151,110 145,105 C140,100 128,100 123,105 C114,110 100,110 93,106 C86,96 85,84 87,72 Z" fill="url(#${id('ln')})"/>
    <path d="M100,70 L114,68 L100,106 L92,104 Z" fill="rgba(255,255,255,.45)"/><path d="M120,67 L126,67 L113,106 L108,106 Z" fill="rgba(255,255,255,.28)"/>
    <circle cx="178" cy="86" r="5" fill="${GG.strap}" ${OL}/>`;
    // visera larga con rejillas
    g += `<path d="M56,52 C72,36 100,26 130,20 C150,16 172,16 188,20 L196,40 C178,42 154,46 134,54 C116,60 96,66 82,68 C70,64 60,60 56,52 Z" fill="url(#${id('pk')})" ${OL}/>
    <path d="M82,68 C96,66 116,60 134,54 C154,46 178,42 196,40 L198,47 C180,49 156,53 136,61 C118,67 98,73 84,75 Z" fill="${D(c, .45)}" ${OL}/>
    <path d="M62,50 C90,34 140,22 186,22" stroke="${c2}" stroke-width="4" fill="none" stroke-linecap="round"/>
    ${[[72, 52], [79, 49], [86, 46], [76, 57], [83, 54], [90, 51]].map(([x, y]) => `<ellipse cx="${x}" cy="${y}" rx="2.4" ry="1.6" fill="#15171c"/>`).join('')}
    ${[[140, 34], [148, 36], [156, 33], [146, 41]].map(([x, y]) => `<path d="M${x - 3},${y} l3,-2.4 3,2.4 -3,2.4z" fill="${D(c, .3)}"/>`).join('')}
    ${arai ? `<ellipse cx="128" cy="38" rx="15" ry="7" fill="#15171c" transform="rotate(-13 128 38)"/><text x="128" y="41" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="9" fill="#ffffff" transform="rotate(-13 128 41)">Arai</text>` : `<text x="138" y="36" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="10.5" fill="${logoC}" transform="rotate(-13 138 36)">alpinestars</text>`}
    ${H.pat === 'frog' ? `<g transform="translate(160 30) rotate(-14)"><ellipse cx="0" cy="0" rx="14" ry="7" fill="#7be35a" stroke="#15171c" stroke-width="1.2"/><circle cx="-10" cy="-6" r="4" fill="#7be35a" stroke="#15171c" stroke-width="1.2"/><circle cx="-10" cy="-6" r="1.6" fill="#e3202b"/><circle cx="-2" cy="-7" r="4" fill="#7be35a" stroke="#15171c" stroke-width="1.2"/><circle cx="-2" cy="-7" r="1.6" fill="#e3202b"/><path d="M8,4 l8,6 M-6,5 l-6,7" stroke="#7be35a" stroke-width="2.6" stroke-linecap="round"/></g>` : ''}
    ${H.pat === 'stars' ? `<path d="M100,46 l4,8 9,1 -7,6 2,9 -8,-5 -8,5 2,-9 -7,-6 9,-1z" fill="none" stroke="${c3}" stroke-width="2"/>` : ''}
    <circle cx="190" cy="40" r="3.4" fill="#15171c"/>`;
    // mentonera en punta con toma de aire
    g += `<path d="M90,114 C104,120 128,124 156,122 L180,116 C188,128 184,144 172,152 L128,156 C108,156 90,150 76,140 C72,130 80,120 90,114 Z" fill="${chinC || `url(#${id('sh')})`}" ${OL}/>`;
    if (arai) g += `<path d="M78,138 C82,128 90,122 98,120 L104,146 C96,150 86,150 78,144 Z" fill="#2a2e35" ${OL}/><path d="M82,130 h16 M81,136 h20 M82,142 h20" stroke="#8a93a0" stroke-width="1.6" stroke-dasharray="2 2"/><rect x="110" y="132" width="16" height="12" rx="3" fill="#2a2e35" ${OL}/><path d="M113,135 h10 M113,139 h10" stroke="#8a93a0" stroke-width="1.4" stroke-dasharray="2 2"/>`;
    else g += `<path d="M74,134 L90,120 L104,136 L88,152 Z" fill="${c2}" ${OL}/><path d="M84,130 l6,-4 M86,136 l8,-6 M89,142 l8,-6" stroke="rgba(0,0,0,.45)" stroke-width="2" stroke-linecap="round"/>
    <path d="M104,132 L124,128 M108,142 L128,138" stroke="#15171c" stroke-width="4.5" stroke-linecap="round"/>`;
    g += `
    <circle cx="176" cy="122" r="3.2" fill="#15171c"/>`;
    if (arai) g += `<g transform="translate(200 128) rotate(-18)"><ellipse cx="0" cy="0" rx="27" ry="14" fill="${H.badge || '#15171c'}" stroke="${H.badge === '#e6f01a' ? '#15171c' : '#f4f6f9'}" stroke-width="2.4"/><text x="0" y="3" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="15" fill="${H.badge === '#e6f01a' ? '#15171c' : '#ffffff'}">Arai</text><text x="6" y="10" text-anchor="middle" font-family="Arial,sans-serif" font-weight="800" font-size="4.4" letter-spacing=".6" fill="${H.badge === '#e6f01a' ? '#15171c' : '#ffffff'}">HELMET</text></g>`;
    else if (!H.pat || H.pat === 'radium' || H.pat === 'flame') g += `<g clip-path="url(#${id('cl2')})"><text x="180" y="142" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="17" letter-spacing="-.6" fill="${logoC}" stroke="rgba(0,0,0,.2)" stroke-width=".8" transform="rotate(-22 180 142)">alpinestars</text></g>`;
  } else {
    // integral Arai
    g += `<g clip-path="url(#${id('cl')})"><text x="194" y="138" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="20" fill="${chrome ? '#1d2027' : lum(c) > .62 ? '#c8102e' : '#ffffff'}" transform="rotate(-14 194 138)">Arai</text></g>`;
    g += `<path d="M84,60 C108,50 150,46 180,52 C188,66 188,92 180,106 C152,112 116,112 94,106 C84,92 82,74 84,60 Z" fill="url(#${id('vi')})" ${OL}/>
    <path d="M94,62 C116,55 150,52 170,56" stroke="rgba(255,255,255,.5)" stroke-width="5" stroke-linecap="round" fill="none"/><path d="M100,102 C124,106 152,106 172,100" stroke="rgba(120,200,255,.35)" stroke-width="3" stroke-linecap="round" fill="none"/>
    <circle cx="188" cy="78" r="8" fill="url(#${id('mt')})" ${OL}/><ellipse cx="150" cy="24" rx="9" ry="4" fill="#15171c"/><ellipse cx="182" cy="24" rx="7" ry="3.4" fill="#15171c"/>
    <path d="M96,118 h26 v12 h-26 z" fill="#15171c"/><path d="M100,121 v6 M105,121 v6 M110,121 v6 M115,121 v6" stroke="#6c7480" stroke-width="1.6"/>
    <path d="M226,90 L240,86 L238,100 L226,104 Z" fill="#15171c"/>`;
  }
  return { defs: d, body: g };
}
if (typeof module !== 'undefined') module.exports = { helmetL };
