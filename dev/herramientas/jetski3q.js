// Moto de agua de 3/4 (proa abajo-derecha), proporciones de las fotos FX — boceto
function jetSki3q(o, uid) {
  uid = uid || 'j' + Math.floor(Math.random() * 1e6);
  const hx = (c) => { c = c.replace('#', ''); return [parseInt(c.slice(0, 2), 16), parseInt(c.slice(2, 4), 16), parseInt(c.slice(4, 6), 16)]; };
  const mix = (a, b, t) => { const A = hx(a), B = hx(b); return '#' + A.map((v, i) => Math.round(v + (B[i] - v) * t).toString(16).padStart(2, '0')).join(''); };
  const L = (c, t) => mix(c, '#ffffff', t), D = (c, t) => mix(c, '#000000', t);
  const lum = (c) => { const [r, g, b] = hx(c); return (r * .3 + g * .59 + b * .11) / 255; };
  const id = (n) => n + uid;
  const OL = 'stroke="rgba(6,8,14,.72)" stroke-width="2" stroke-linejoin="round"';
  const hull = o.hull, deck = o.deck, acc = o.acc, seatA = o.seatA || deck, seatB = o.seatB || acc, name = o.name || 'BRAVA';
  const nameC = o.nameC || (lum(hull) > .55 ? D(deck, .05) : '#ffffff');
  const hullP = 'M34,150 C120,170 210,192 300,214 C390,236 480,256 570,276 L592,288 C588,300 576,312 560,318 C470,298 386,280 300,262 C210,242 128,222 50,198 C38,186 34,168 34,150 Z';
  const bandP = 'M32,124 C120,144 210,166 300,186 C390,208 480,230 566,250 L592,264 L592,288 L570,276 C480,256 390,236 300,214 C210,192 120,170 34,150 Z';
  const deckP = 'M32,124 C60,110 90,100 120,96 C190,110 260,124 330,140 C400,158 470,182 520,206 C552,222 576,242 592,264 L566,250 C480,230 390,208 300,186 C210,166 120,144 32,124 Z';
  let d = `<defs>
  <linearGradient id="${id('hs')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${L(hull, .32)}"/><stop offset=".4" stop-color="${hull}"/><stop offset="1" stop-color="${D(hull, .38)}"/></linearGradient>
  <linearGradient id="${id('bd')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${L(deck, .18)}"/><stop offset="1" stop-color="${D(deck, .35)}"/></linearGradient>
  <linearGradient id="${id('dk')}" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="${L(deck, .3)}"/><stop offset=".55" stop-color="${deck}"/><stop offset="1" stop-color="${D(deck, .3)}"/></linearGradient>
  <linearGradient id="${id('hd')}" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="${L(deck, .42)}"/><stop offset=".5" stop-color="${L(deck, .08)}"/><stop offset="1" stop-color="${D(deck, .3)}"/></linearGradient>
  <linearGradient id="${id('ac')}" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="${L(acc, .38)}"/><stop offset=".6" stop-color="${acc}"/><stop offset="1" stop-color="${D(acc, .3)}"/></linearGradient>
  <linearGradient id="${id('sA')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${L(seatA, .32)}"/><stop offset="1" stop-color="${D(seatA, .25)}"/></linearGradient>
  <linearGradient id="${id('sB')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="${L(seatB, .38)}"/><stop offset="1" stop-color="${D(seatB, .18)}"/></linearGradient>
  <linearGradient id="${id('gl')}" x1="0" x2="1"><stop offset="0" stop-color="rgba(255,255,255,0)"/><stop offset=".5" stop-color="rgba(255,255,255,.6)"/><stop offset="1" stop-color="rgba(255,255,255,0)"/></linearGradient>
  <filter id="${id('bl')}" x="-20%" y="-60%" width="140%" height="220%"><feGaussianBlur stdDeviation="8"/></filter>
  <clipPath id="${id('hc')}"><path d="${hullP}"/></clipPath><clipPath id="${id('bc')}"><path d="${bandP}"/></clipPath>
  </defs>`;
  let g = `<ellipse cx="320" cy="316" rx="290" ry="16" fill="rgba(0,10,30,.32)" filter="url(#${id('bl')})"/>`;
  // casco inferior
  g += `<path d="${hullP}" fill="url(#${id('hs')})" ${OL}/>`;
  g += `<g clip-path="url(#${id('hc')})"><path d="M40,190 C200,232 400,278 580,318 L580,330 L40,230 Z" fill="${D(hull, .5)}" opacity=".55"/>
    <path d="M70,172 C220,206 400,248 548,280" stroke="url(#${id('gl')})" stroke-width="6" fill="none"/>
    <text x="0" y="0" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="40" fill="none" stroke="${nameC}" stroke-width="1.8" letter-spacing="4" transform="translate(196 236) rotate(13) skewX(-12)">${name}</text></g>`;
  // patines y toma
  g += `<path d="M64,186 L122,200 L118,212 L68,198 Z" fill="${D(deck, .35)}" ${OL}/><path d="M72,192 h40" stroke="rgba(255,255,255,.2)" stroke-width="1.5"/>`;
  // banda alta oscura
  g += `<path d="${bandP}" fill="url(#${id('bd')})" ${OL}/>`;
  g += `<g clip-path="url(#${id('bc')})"><path d="M120,150 C240,178 380,212 520,248" stroke="${acc}" stroke-width="4" fill="none"/><path d="M380,206 C440,220 500,236 560,254 L560,262 C500,244 440,228 380,214 Z" fill="${acc}" opacity=".9"/></g>`;
  g += `<text x="0" y="0" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-size="9" fill="${lum(deck) > .5 ? '#15171c' : '#ffffff'}" transform="translate(52 142) rotate(13)">COSTA TURBO</text>`;
  // cubierta
  g += `<path d="${deckP}" fill="url(#${id('dk')})" ${OL}/>`;
  g += `<path d="M32,124 C60,110 90,100 120,96 L156,104 C124,112 94,124 70,138 Z" fill="${D(deck, .18)}"/><path d="M44,124 l22,-10 M54,128 l22,-10 M64,132 l22,-10" stroke="rgba(255,255,255,.12)" stroke-width="2"/>`;
  g += `<path d="M70,138 C94,124 124,112 156,104 L162,110 C132,118 104,130 80,144 Z" fill="${acc}"/><path d="M50,120 C58,106 76,100 92,102" stroke="#15171c" stroke-width="5" fill="none" stroke-linecap="round"/>`;
  // asiento alto escalonado
  g += `<path d="M146,116 C190,124 226,132 262,140 C300,148 340,156 378,162 L382,184 C340,176 300,168 262,160 C226,152 190,144 150,138 Z" fill="${D(seatA, .32)}" ${OL}/>`;
  g += `<path d="M146,116 C148,100 162,88 182,84 C206,86 228,90 248,96 C256,86 270,80 288,82 C322,90 354,102 384,116 C394,122 396,136 392,146 C388,154 384,160 378,162 C340,156 300,148 262,140 C226,132 190,124 146,116 Z" fill="url(#${id('sA')})" ${OL}/>`;
  g += `<path d="M170,108 C172,98 182,92 194,90 C214,92 232,96 248,102 C258,96 270,92 284,92 C314,100 344,112 370,126 C376,132 376,140 372,148 C340,140 300,132 262,124 C230,118 198,112 170,108 Z" fill="url(#${id('sB')})"/>`;
  g += `<path d="M248,96 C252,108 256,120 262,140" stroke="rgba(0,0,0,.45)" stroke-width="3" fill="none"/><path d="M182,90 C210,94 232,98 246,102 M292,88 C324,96 352,108 376,122" stroke="rgba(255,255,255,.38)" stroke-width="3" fill="none" stroke-linecap="round"/>`;
  g += `<path d="M150,118 C190,126 226,134 262,142 C300,150 340,158 378,164" stroke="${seatB}" stroke-width="2" fill="none" opacity=".7"/>`;
  // capó
  g += `<path d="M392,150 C400,126 418,110 440,104 C486,112 534,154 592,264 L566,250 C520,216 462,188 404,170 C396,164 390,158 392,150 Z" fill="url(#${id('hd')})" ${OL}/>`;
  g += `<path d="M408,168 C460,186 520,216 566,250 L574,252 C530,212 466,180 412,156 Z" fill="url(#${id('ac')})" ${OL}/>`;
  g += `<path d="M452,116 C482,126 512,150 534,182 L522,186 C500,156 474,136 446,126 Z" fill="${acc}" ${OL}/>`;
  g += `<path d="M420,120 C460,118 510,150 548,200" stroke="rgba(255,255,255,.4)" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M414,150 C470,170 524,204 566,246" stroke="rgba(0,0,0,.28)" stroke-width="2" fill="none"/>`;
  g += `<path d="M436,108 C452,98 474,98 488,106 L480,120 C466,114 452,114 442,120 Z" fill="#11141a" ${OL}/><path d="M446,106 C458,102 470,102 480,106" stroke="rgba(160,210,255,.45)" stroke-width="2" fill="none"/>`;
  g += `<text x="0" y="0" font-family="Arial,sans-serif" font-weight="800" font-style="italic" font-size="11" fill="${lum(deck) > .55 ? D(deck, .6) : '#ffffff'}" transform="translate(466 190) rotate(29)">${o.model || 'TURBO SVR'}</text>`;
  g += `<circle cx="566" cy="238" r="5" fill="${lum(deck) > .55 ? D(deck, .5) : '#ffffff'}" opacity=".9"/>`;
  // espejos
  g += `<path d="M478,128 l22,-12 l9,9 l-20,13 z" fill="url(#${id('ac')})" ${OL}/><path d="M432,112 l20,-13 l8,7 l-18,15 z" fill="url(#${id('ac')})" ${OL}/>`;
  // manillar
  g += `<path d="M430,134 L438,86 L452,86 L448,138 Z" fill="${D(deck, .25)}" ${OL}/>`;
  g += `<path d="M386,88 C420,80 470,72 512,66" stroke="#15171c" stroke-width="7" stroke-linecap="round" fill="none"/><path d="M380,90 l-12,4 M514,66 l13,-2" stroke="#2a2d33" stroke-width="10" stroke-linecap="round"/>`;
  g += `<path d="M418,84 C434,76 456,74 470,76 L466,90 C452,88 436,90 422,96 Z" fill="${acc}" ${OL}/><rect x="434" y="88" width="22" height="11" rx="3" fill="#0f1116" ${OL}/><rect x="437" y="91" width="16" height="5" rx="1.5" fill="#33d6ff" opacity=".85"/>`;
  return `<svg viewBox="0 0 610 336" xmlns="http://www.w3.org/2000/svg">${d}${g}</svg>`;
}
if (typeof module !== 'undefined') module.exports = { jetSki3q };
