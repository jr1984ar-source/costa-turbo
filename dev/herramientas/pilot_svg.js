// Piloto de pie, vista frontal, para la pantalla de EQUIPO (boceto)
function pilotSVG(o, uid) {
  uid = uid || 'p' + Math.floor(Math.random() * 1e6);
  const H = o.helm || {c:'#ffffff'}, V = o.vest, S = o.suit, glove = o.glove || '#1b1d22';
  const hx = (c) => { c = c.replace('#', ''); return [parseInt(c.slice(0, 2), 16), parseInt(c.slice(2, 4), 16), parseInt(c.slice(4, 6), 16)]; };
  const mix = (a, b, t) => { const A = hx(a), B = hx(b); return '#' + A.map((v, i) => Math.round(v + (B[i] - v) * t).toString(16).padStart(2, '0')).join(''); };
  const L = (c, t) => mix(c, '#ffffff', t), D = (c, t) => mix(c, '#000000', t);
  const lum = (c) => { const [r, g, b] = hx(c); return (r * .3 + g * .59 + b * .11) / 255; };
  const id = (n) => n + uid;
  const OL = 'stroke="rgba(8,12,22,.6)" stroke-width="2.2" stroke-linejoin="round"';
  const cyl = (n, c, k) => `<linearGradient id="${id(n)}" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="${D(c, .45 * k)}"/><stop offset=".3" stop-color="${L(c, .16 * k)}"/><stop offset=".55" stop-color="${c}"/><stop offset="1" stop-color="${D(c, .5 * k)}"/></linearGradient>`;
  const BARE = o.bare || null;
  const suitC = BARE ? BARE.skin : (S.c || '#1d2027'), suitA = BARE ? BARE.skin : (S.a || '#3a3f4a');
  const helmC = H.c, helmC2 = H.c2 || '#ffffff', chrome = H.pat === 'chrome', full = H.st === 'full';
  const vestC = V.c, vestC2 = V.c2 || '#ffffff', vestTxt = lum(vestC) > .62 ? '#15171c' : '#ffffff';

  // ---------- defs ----------
  let defs = `<defs>
  ${cyl('leg', suitC, BARE ? .55 : 1)}${cyl('arm', suitC, BARE ? .55 : 1)}${cyl('pad', D(suitC, .25), 1)}${BARE ? cyl('sh', BARE.shorts, 1) + cyl('ly', BARE.lycra, 1) : ''}
  <radialGradient id="${id('vest')}" cx=".38" cy=".25" r=".85"><stop offset="0" stop-color="${L(vestC, .28)}"/><stop offset=".55" stop-color="${vestC}"/><stop offset="1" stop-color="${D(vestC, .42)}"/></radialGradient>
  <linearGradient id="${id('vside')}" x1="0" x2="1"><stop offset="0" stop-color="${D(vestC2, .35)}"/><stop offset="1" stop-color="${vestC2}"/></linearGradient>
  ${chrome
    ? `<radialGradient id="${id('shell')}" cx=".36" cy=".26" r=".9"><stop offset="0" stop-color="#ffffff"/><stop offset=".3" stop-color="#dfe6ee"/><stop offset=".55" stop-color="#8d99a8"/><stop offset=".75" stop-color="#eef3f8"/><stop offset="1" stop-color="#5d6876"/></radialGradient>`
    : `<radialGradient id="${id('shell')}" cx=".36" cy=".28" r=".85"><stop offset="0" stop-color="${L(helmC, .55)}"/><stop offset=".35" stop-color="${L(helmC, .12)}"/><stop offset=".75" stop-color="${helmC}"/><stop offset="1" stop-color="${D(helmC, .45)}"/></radialGradient>`}
  <linearGradient id="${id('lens')}" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#ffd166"/><stop offset=".35" stop-color="#ff7a3c"/><stop offset=".7" stop-color="#e2366e"/><stop offset="1" stop-color="#5b3cff"/></linearGradient>
  <linearGradient id="${id('visor')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#3b4d6e"/><stop offset=".5" stop-color="#151d2d"/><stop offset="1" stop-color="#0a0f19"/></linearGradient>
  <linearGradient id="${id('metal')}" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#f1f4f8"/><stop offset=".5" stop-color="#a7afba"/><stop offset="1" stop-color="#6c7480"/></linearGradient>
  <pattern id="${id('carb')}" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#22252b"/><rect width="4" height="4" fill="#33373f"/><rect x="4" y="4" width="4" height="4" fill="#33373f"/><rect width="8" height="1" fill="rgba(255,255,255,.05)"/></pattern>
  <pattern id="${id('camo')}" width="60" height="60" patternUnits="userSpaceOnUse"><rect width="60" height="60" fill="${suitC}"/><path d="M5 8c10-6 18 2 14 10s-16 6-14-10zM34 30c9-4 20 4 14 12s-20 2-14-12zM10 44c6-3 12 2 9 7s-12 3-9-7zM40 4c5-2 10 2 7 6s-9 1-7-6z" fill="${D(suitC, .35)}"/><path d="M22 22c6-2 10 4 6 7s-10-1-6-7zM48 50c4-2 8 2 5 5s-8 0-5-5z" fill="${L(suitA, .1)}" opacity=".7"/></pattern>
  <filter id="${id('blur')}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
  <clipPath id="${id('vclip')}"><path d="${'M100,128 C94,132 88,140 86,152 C84,170 84,190 86,215 C88,245 90,275 92,300 C110,306 130,310 150,310 C170,310 190,306 208,300 C210,275 212,245 214,215 C216,190 216,170 214,152 C212,140 206,132 200,128 C192,124 184,124 178,126 C174,140 164,152 150,156 C136,152 126,140 122,126 C116,124 108,124 100,128 Z'}"/></clipPath>
  <clipPath id="${id('hclip')}"><path d="${full ? 'M150,12 C190,12 212,42 212,76 C212,106 203,128 187,142 C170,152 130,152 113,142 C97,128 88,106 88,76 C88,42 110,12 150,12 Z' : 'M150,14 C188,14 208,40 210,72 C212,98 205,118 190,130 L110,130 C95,118 88,98 90,72 C92,40 112,14 150,14 Z'}"/></clipPath>
  <clipPath id="${id('lclip')}"><path d="M98,312 C92,350 90,400 88,446 C86,492 86,540 84,584 L114,584 C116,540 120,500 126,460 C132,420 142,380 150,352 Z M202,312 C208,350 210,400 212,446 C214,492 214,540 216,584 L186,584 C184,540 180,500 174,460 C168,420 158,380 150,352 Z"/></clipPath>
  <clipPath id="${id('aclip')}"><path d="M98,136 C84,136 72,144 64,158 C54,176 47,200 43,222 C41,236 44,246 52,254 C62,266 74,278 86,290 L102,276 C92,264 82,250 72,236 C74,214 80,196 90,180 C96,170 102,160 106,150 Z M202,136 C216,136 228,144 236,158 C246,176 253,200 257,222 C259,236 256,246 248,254 C238,266 226,278 214,290 L198,276 C208,264 218,250 228,236 C226,214 220,196 210,180 C204,170 198,160 194,150 Z"/></clipPath>
  </defs>`;

  const suitFill = S.pat === 'camo' ? `url(#${id('camo')})` : S.pat === 'carbon' ? `url(#${id('carb')})` : `url(#${id('leg')})`;
  const armFill = S.pat === 'camo' ? `url(#${id('camo')})` : S.pat === 'carbon' ? `url(#${id('carb')})` : `url(#${id('arm')})`;

  // ---------- sombra ----------
  let g = `<ellipse cx="150" cy="630" rx="78" ry="11" fill="rgba(0,0,0,.45)" filter="url(#${id('blur')})"/>`;

  // ---------- piernas ----------
  const legL = 'M98,312 C92,350 90,400 88,446 C86,492 86,540 84,584 L114,584 C116,540 120,500 126,460 C132,420 142,380 150,352 Z';
  const legR = 'M202,312 C208,350 210,400 212,446 C214,492 214,540 216,584 L186,584 C184,540 180,500 174,460 C168,420 158,380 150,352 Z';
  g += `<path d="M92,292 C92,312 96,328 100,338 L150,358 L200,338 C204,328 208,312 208,292 Z" fill="${S.pat ? suitFill : D(suitC, .15)}" ${OL}/>`;
  g += `<path d="${legL}" fill="${suitFill}" ${OL}/><path d="${legR}" fill="${suitFill}" ${OL}/>`;
  if (BARE) {
    // bañador hasta encima de la rodilla
    const shL = 'M92,292 L208,292 C209,330 211,380 212,420 L178,424 C174,400 164,376 150,356 C140,376 128,400 122,424 L88,420 C89,380 91,330 92,292 Z';
    g += `<path d="${shL}" fill="url(#${id('sh')})" ${OL}/>`;
    g += `<path d="M90,300 C90,340 89,380 88,418 M210,300 C211,340 211,380 212,418" stroke="${BARE.shorts2}" stroke-width="7" fill="none"/>`;
    g += `<path d="M88,412 L122,416 M178,416 L212,412" stroke="${D(BARE.shorts, .35)}" stroke-width="3"/><path d="M96,300 h108" stroke="${D(BARE.shorts, .3)}" stroke-width="4"/><path d="M146,302 l4,10 l4,-10" stroke="${L(BARE.shorts, .5)}" stroke-width="2" fill="none"/>`;
    g += `<path d="M112,330 C110,360 108,390 106,412 M188,330 C190,360 192,390 194,412" stroke="rgba(255,255,255,.18)" stroke-width="6" stroke-linecap="round" fill="none"/>`;
    // rodillas y espinillas
    g += `<path d="M98,452 q8 6 18 2 M184,454 q10 4 18 -2" stroke="${D(BARE.skin, .25)}" stroke-width="2" fill="none" stroke-linecap="round"/><path d="M104,480 C102,520 100,550 99,576 M196,480 C198,520 200,550 201,576" stroke="rgba(255,255,255,.18)" stroke-width="5" stroke-linecap="round" fill="none"/>`;
  } else {
  g += `<g clip-path="url(#${id('lclip')})">
    <path d="M96,318 C90,360 88,410 86,450 C84,500 84,545 83,588" fill="none" stroke="${suitA}" stroke-width="8"/>
    <path d="M204,318 C210,360 212,410 214,450 C216,500 216,545 217,588" fill="none" stroke="${suitA}" stroke-width="8"/>
    <path d="M112,340 C108,390 106,420 104,446 M188,340 C192,390 194,420 196,446 M104,500 C102,530 100,560 99,584 M196,500 C198,530 200,560 201,584" stroke="rgba(255,255,255,.2)" stroke-width="6" stroke-linecap="round" fill="none"/>
    <path d="M130,360 C126,400 120,430 116,456 M170,360 C174,400 180,430 184,456" stroke="rgba(0,0,0,.22)" stroke-width="1.8" fill="none"/>
    <rect x="80" y="296" width="140" height="26" fill="rgba(0,0,0,.28)"/>
  </g>`;
  }
  // rodilleras
  if (!BARE) for (const [x, r] of [[87, 4], [175, -4]]) {
    const kp = D(suitA === '#ffc93c' ? '#2a2d33' : suitA, .35);
    g += `<g transform="rotate(${r} ${x + 19} 460)"><rect x="${x}" y="434" width="38" height="54" rx="15" fill="${kp}" ${OL}/>
    <path d="M${x + 6},449 h26 M${x + 6},460 h26 M${x + 6},471 h26" stroke="rgba(255,255,255,.16)" stroke-width="2.6" stroke-linecap="round"/>
    <rect x="${x + 4}" y="437" width="12" height="47" rx="6" fill="rgba(255,255,255,.1)"/><circle cx="${x + 19}" cy="441" r="2.2" fill="${suitA}"/></g>`;
  }
  // escarpines
  if (BARE) g += `<path d="M86,578 L114,578 C117,592 119,602 119,612 C119,622 113,628 103,628 L70,628 C62,628 60,620 66,612 C74,602 82,594 86,578 Z" fill="url(#${id('leg')})" ${OL}/><path d="M214,578 L186,578 C183,592 181,602 181,612 C181,622 187,628 197,628 L230,628 C238,628 240,620 234,612 C226,602 218,594 214,578 Z" fill="url(#${id('leg')})" ${OL}/>
  <path d="M68,622 l5,-5 M76,624 l4,-6 M84,625 l3,-6 M232,622 l-5,-5 M224,624 l-4,-6 M216,625 l-3,-6" stroke="${D(BARE.skin, .3)}" stroke-width="1.6" stroke-linecap="round"/>`;
  else g += `<path d="M84,580 L115,580 C118,592 120,602 120,612 C120,622 114,628 104,628 L68,628 C60,628 58,620 64,612 C72,602 80,594 84,580 Z" fill="#17191e" ${OL}/>
  <path d="M216,580 L185,580 C182,592 180,602 180,612 C180,622 186,628 196,628 L232,628 C240,628 242,620 236,612 C228,602 220,594 216,580 Z" fill="#17191e" ${OL}/>
  <path d="M62,622 h58 M180,622 h58" stroke="#4a505c" stroke-width="5" stroke-linecap="round"/>
  <path d="M84,594 h30 M186,594 h30" stroke="${suitA}" stroke-width="4" stroke-linecap="round"/>
  <path d="M70,612 q14 -6 30 -4 M230,612 q-14 -6 -30 -4" stroke="rgba(255,255,255,.18)" stroke-width="2.4" fill="none" stroke-linecap="round"/>`;

  // ---------- brazos ----------
  const armL = 'M98,136 C84,136 72,144 64,158 C54,176 47,200 43,222 C41,236 44,246 52,254 C62,266 74,278 86,290 L102,276 C92,264 82,250 72,236 C74,214 80,196 90,180 C96,170 102,160 106,150 Z';
  const armR = 'M202,136 C216,136 228,144 236,158 C246,176 253,200 257,222 C259,236 256,246 248,254 C238,266 226,278 214,290 L198,276 C208,264 218,250 228,236 C226,214 220,196 210,180 C204,170 198,160 194,150 Z';
  g += `<path d="${armL}" fill="${armFill}" ${OL}/><path d="${armR}" fill="${armFill}" ${OL}/>`;
  if (BARE) {
    g += `<g clip-path="url(#${id('aclip')})"><rect x="30" y="120" width="240" height="84" fill="url(#${id('ly')})"/><path d="M40,200 L110,196 M190,196 L260,200" stroke="${D(BARE.lycra, .4)}" stroke-width="4"/><path d="M60,150 C56,170 54,186 52,198 M240,150 C244,170 246,186 248,198" stroke="rgba(255,255,255,.25)" stroke-width="5" stroke-linecap="round" fill="none"/>
      <path d="M60,214 C54,230 50,240 48,248 M240,214 C246,230 250,240 252,248" stroke="rgba(255,255,255,.2)" stroke-width="4" stroke-linecap="round" fill="none"/><path d="M48,238 q6 2 10 -2 M252,238 q-6 2 -10 -2" stroke="${D(BARE.skin, .3)}" stroke-width="1.8" fill="none"/></g>`;
    g += `<path d="M120,118 C130,106 170,106 180,118 L178,134 C168,126 132,126 122,134 Z" fill="${BARE.lycra}" ${OL}/>`;
  } else {
  g += `<g clip-path="url(#${id('aclip')})">
    <path d="M50,150 C70,132 98,132 110,146 L96,186 C82,174 66,174 50,186 Z M250,150 C230,132 202,132 190,146 L204,186 C218,174 234,174 250,186 Z" fill="${suitA}"/>
    <path d="M60,184 C54,200 50,214 47,228 M240,184 C246,200 250,214 253,228" stroke="rgba(255,255,255,.22)" stroke-width="5" stroke-linecap="round" fill="none"/>
    <ellipse cx="52" cy="238" rx="14" ry="17" fill="${D(suitC === '#2a2d33' ? '#3a3f4a' : suitC, .38)}" transform="rotate(30 52 238)"/><ellipse cx="248" cy="238" rx="14" ry="17" fill="${D(suitC === '#2a2d33' ? '#3a3f4a' : suitC, .38)}" transform="rotate(-30 248 238)"/>
    <path d="M44,232 q6 -3 12 2 M46,241 q6 -3 12 2 M244,234 q-6 -3 -12 2 M242,243 q-6 -3 -12 2" stroke="rgba(255,255,255,.2)" stroke-width="2" fill="none"/>
    <path d="M74,270 L90,256 L100,266 L84,280 Z M226,270 L210,256 L200,266 L216,280 Z" fill="${suitA}"/>
  </g>`;
  }

  // ---------- chaleco ----------
  const vestP = 'M100,128 C94,132 88,140 86,152 C84,170 84,190 86,215 C88,245 90,275 92,300 C110,306 130,310 150,310 C170,310 190,306 208,300 C210,275 212,245 214,215 C216,190 216,170 214,152 C212,140 206,132 200,128 C192,124 184,124 178,126 C174,140 164,152 150,156 C136,152 126,140 122,126 C116,124 108,124 100,128 Z';
  // cuello del neopreno y del chaleco
  if (!BARE) g += `<path d="M120,118 C130,106 170,106 180,118 L178,134 C168,126 132,126 122,134 Z" fill="${D(vestC, .3)}" ${OL}/>`;
  g += `<path d="${vestP}" fill="${V.pat === 'carbon' ? `url(#${id('carb')})` : `url(#${id('vest')})`}" ${OL}/>`;
  g += `<g clip-path="url(#${id('vclip')})">`;
  // laterales de color
  g += `<path d="M86,150 C84,175 85,200 87,225 C89,252 90,278 92,300 L108,304 C106,276 104,248 103,222 C102,196 102,172 106,148 Z" fill="url(#${id('vside')})"/>
        <path d="M214,150 C216,175 215,200 213,225 C211,252 210,278 208,300 L192,304 C194,276 196,248 197,222 C198,196 198,172 194,148 Z" fill="url(#${id('vside')})"/>`;
  if (V.pat === 'vault') g += `<path d="M84,236 L150,272 L216,236 L216,256 L150,292 L84,256 Z" fill="${vestC2}"/><path d="M84,236 L150,272 L216,236" stroke="rgba(255,255,255,.35)" stroke-width="2" fill="none"/>`;
  else if (V.pat === 'race') g += `<rect x="114" y="120" width="9" height="200" fill="${vestC2}"/><rect x="177" y="120" width="9" height="200" fill="${vestC2}"/>`;
  else if (V.pat === 'band') g += `<rect x="80" y="192" width="140" height="18" fill="${vestC2}"/>`;
  else if (V.pat === 'carbon') g += `<path d="${vestP}" fill="none" stroke="${vestC2}" stroke-width="7"/>`;
  // segmentos de espuma
  for (const y of [196, 238, 280]) g += `<path d="M84,${y} C120,${y + 7} 180,${y + 7} 216,${y}" stroke="rgba(0,0,0,.32)" stroke-width="3.2" fill="none"/><path d="M84,${y + 3} C120,${y + 10} 180,${y + 10} 216,${y + 3}" stroke="rgba(255,255,255,.14)" stroke-width="2" fill="none"/>`;
  // brillo de volumen
  g += `<path d="M112,140 C104,170 104,220 110,280" stroke="rgba(255,255,255,.22)" stroke-width="8" stroke-linecap="round" fill="none"/>`;
  // correas y hebillas
  for (const y of [214, 258]) g += `<rect x="80" y="${y}" width="140" height="11" fill="#14161a"/><rect x="80" y="${y}" width="140" height="2" fill="rgba(255,255,255,.12)"/>`;
  g += `</g>`;
  // cremallera
  g += `<path d="M150,156 L150,309" stroke="#23262c" stroke-width="5"/><path d="M150,160 L150,306" stroke="#9aa3ae" stroke-width="1.6" stroke-dasharray="2 3"/><rect x="146" y="164" width="8" height="15" rx="3" fill="url(#${id('metal')})" ${OL}/>`;
  for (const y of [214, 258]) g += `<rect x="135" y="${y - 3}" width="30" height="17" rx="5" fill="url(#${id('metal')})" ${OL}/><rect x="141" y="${y + 1}" width="18" height="8" rx="3" fill="#2a2e35"/>`;
  // hombreras
  g += `<path d="M101,130 C103,116 112,110 124,111 L124,128 Z" fill="${D(vestC, .22)}" ${OL}/><path d="M199,130 C197,116 188,110 176,111 L176,128 Z" fill="${D(vestC, .22)}" ${OL}/>`;
  // logotipos
  g += `<g transform="translate(118 182) rotate(-6)"><path d="M-2,-11 l10,4 l-10,4 z" fill="${vestC2 === vestC ? vestTxt : vestC2}"/><text x="10" y="0" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="11" fill="${vestTxt}">JET PILOT</text></g>`;
  if (V.name) g += `<rect x="155" y="190" width="56" height="13" rx="3" fill="rgba(10,12,18,.82)"/><text x="183" y="199.5" text-anchor="middle" font-family="Arial,sans-serif" font-weight="800" font-size="7.6" letter-spacing=".6" fill="#ffffff">${V.name.toUpperCase()}</text>`;

  // puños en la cadera (guantes)
  for (const f of [1, -1]) {
    const X = (x) => 150 + f * (x - 150);
    g += `<path d="M${X(80)},282 C${X(78)},270 ${X(88)},264 ${X(98)},266 C${X(110)},268 ${X(116)},278 ${X(114)},290 C${X(112)},302 ${X(102)},308 ${X(92)},306 C${X(83)},304 ${X(80)},294 ${X(80)},282 Z" fill="${glove}" ${OL}/>
    <path d="M${X(86)},272 C${X(94)},268 ${X(104)},270 ${X(110)},276" stroke="${o.gloveA || suitA}" stroke-width="4.5" fill="none" stroke-linecap="round"/>${o.gloveA ? `<path d="M${X(86)},284 C${X(94)},280 ${X(104)},281 ${X(112)},286 L${X(112)},292 C${X(104)},288 ${X(94)},288 ${X(86)},292 Z" fill="${o.gloveA}"/>` : ''}
    <path d="M${X(88)},286 q${f * 8} 3 ${f * 18} -1 M${X(88)},294 q${f * 8} 3 ${f * 17} -1" stroke="rgba(255,255,255,.22)" stroke-width="1.8" fill="none" stroke-linecap="round"/>
    <path d="M${X(82)},279 C${X(80)},268 ${X(76)},262 ${X(74)},260" stroke="${suitA}" stroke-width="7" fill="none"/>`;
  }
  // sombra del casco sobre el chaleco
  g += `<ellipse cx="150" cy="150" rx="50" ry="10" fill="rgba(0,0,0,.35)" filter="url(#${id('blur')})"/>`;
  // ---------- casco ----------
  if (!o.noHelm) {
  const shellP = full ? 'M150,12 C190,12 212,42 212,76 C212,106 203,128 187,142 C170,152 130,152 113,142 C97,128 88,106 88,76 C88,42 110,12 150,12 Z'
    : 'M150,14 C188,14 208,40 210,72 C212,98 205,118 190,130 L110,130 C95,118 88,98 90,72 C92,40 112,14 150,14 Z';
  g += `<path d="${shellP}" fill="url(#${id('shell')})" ${OL}/>`;
  g += `<g clip-path="url(#${id('hclip')})">`;
  if (H.pat === 'flame') {
    for (const s of [-1, 1]) g += `<path d="M${150 + s * 64},140 C${150 + s * 64},110 ${150 + s * 40},96 ${150 + s * 30},62 C${150 + s * 44},84 ${150 + s * 50},92 ${150 + s * 48},104 C${150 + s * 58},88 ${150 + s * 56},70 ${150 + s * 50},50 C${150 + s * 70},74 ${150 + s * 72},98 ${150 + s * 70},140 Z" fill="${helmC2}"/><path d="M${150 + s * 62},140 C${150 + s * 60},118 ${150 + s * 50},108 ${150 + s * 44},94 C${150 + s * 52},106 ${150 + s * 56},112 ${150 + s * 56},120 Z" fill="#ffd21a" opacity=".9"/>`;
  } else if (H.pat === 'twin') g += `<rect x="134" y="0" width="10" height="160" fill="${helmC2}"/><rect x="156" y="0" width="10" height="160" fill="${helmC2}"/>`;
  else if (H.pat === 'split') g += `<rect x="80" y="0" width="70" height="160" fill="${helmC2}"/>`;
  else if (H.pat === 'star') g += `<path d="M150,22 l7,15 16,2 -12,11 3,16 -14,-8 -14,8 3,-16 -12,-11 16,-2z" fill="${helmC2}"/><rect x="80" y="104" width="140" height="8" fill="${helmC2}"/>`;
  else if (H.pat === 'carbon') g += `<rect x="80" y="0" width="140" height="160" fill="url(#${id('carb')})" opacity=".9"/><rect x="80" y="100" width="140" height="5" fill="${helmC2}"/><rect x="146" y="0" width="8" height="160" fill="${helmC2}"/>`;
  else if (H.pat === 'chrome') g += `<rect x="146" y="0" width="8" height="160" fill="${helmC2}"/><path d="M106,40 C112,26 126,18 140,16" stroke="#ffffff" stroke-width="6" stroke-linecap="round" fill="none" opacity=".8"/>`;
  g += `<path d="M112,30 C124,18 140,15 152,15" stroke="rgba(255,255,255,.55)" stroke-width="5" stroke-linecap="round" fill="none"/></g>`;
  if (!full) {
    // visera de cross
    g += `<path d="M86,46 C108,30 192,30 214,46 L226,30 C204,8 96,8 74,30 Z" fill="url(#${id('shell')})" ${OL}/>
    <path d="M78,32 C100,14 200,14 222,32" stroke="${helmC2}" stroke-width="5" fill="none"/>
    <rect x="122" y="22" width="12" height="5" rx="2" fill="#15171c"/><rect x="166" y="22" width="12" height="5" rx="2" fill="#15171c"/>
    <text x="150" y="40" text-anchor="middle" font-family="Arial,sans-serif" font-weight="800" font-size="9.5" fill="${lum(helmC) > .6 ? '#15171c' : '#ffffff'}">${H.brand === 'Arai' ? 'Arai' : 'alpinestars'}</text>`;
    // gafas
    g += `<path d="M90,62 C120,56 180,56 210,62 L210,88 C180,94 120,94 90,88 Z" fill="${helmC2 === '#ffffff' ? '#1d2027' : helmC2}"/>
    <rect x="108" y="56" width="84" height="40" rx="14" fill="#16181d" ${OL}/>
    <path d="M114,62 h72 a8,8 0 0 1 8,8 v12 a8,8 0 0 1 -8,8 h-24 c-4,-6 -20,-6 -24,0 h-24 a8,8 0 0 1 -8,-8 v-12 a8,8 0 0 1 8,-8 z" fill="url(#${id('lens')})"/>
    <path d="M120,66 L138,66 L126,86 L118,86 Z" fill="rgba(255,255,255,.45)"/><path d="M142,66 L148,66 L136,86 L131,86 Z" fill="rgba(255,255,255,.3)"/>`;
    // mentonera
    g += `<path d="M108,98 C110,118 126,138 150,148 C174,138 190,118 192,98 C176,104 124,104 108,98 Z" fill="url(#${id('shell')})" ${OL}/>
    <path d="M136,112 h28 v18 c-6,6 -22,6 -28,0 z" fill="#2a2e35" ${OL}/><path d="M140,117 h20 M140,122 h20 M141,127 h18" stroke="#6c7480" stroke-width="2"/>
    <rect x="112" y="108" width="14" height="5" rx="2.5" fill="#15171c" transform="rotate(28 119 110)"/><rect x="174" y="108" width="14" height="5" rx="2.5" fill="#15171c" transform="rotate(-28 181 110)"/>`;
  } else {
    // pantalla del integral
    g += `<path d="M102,58 C120,48 180,48 198,58 C204,70 204,88 197,100 C180,106 120,106 103,100 C96,88 96,70 102,58 Z" fill="url(#${id('visor')})" ${OL}/>
    <path d="M110,62 C126,55 160,54 176,58" stroke="rgba(255,255,255,.45)" stroke-width="5" stroke-linecap="round" fill="none"/>
    <path d="M118,96 C140,99 168,99 186,94" stroke="rgba(120,200,255,.35)" stroke-width="3" stroke-linecap="round" fill="none"/>
    <circle cx="97" cy="80" r="7" fill="url(#${id('metal')})" ${OL}/><circle cx="203" cy="80" r="7" fill="url(#${id('metal')})" ${OL}/>
    <ellipse cx="130" cy="30" rx="7" ry="4" fill="#15171c"/><ellipse cx="170" cy="30" rx="7" ry="4" fill="#15171c"/>
    <rect x="138" y="112" width="24" height="12" rx="4" fill="#15171c"/><path d="M142,115 v6 M147,115 v6 M152,115 v6 M157,115 v6" stroke="#6c7480" stroke-width="1.6"/>
    <text x="150" y="141" text-anchor="middle" font-family="Arial Black,Arial,sans-serif" font-weight="900" font-style="italic" font-size="13" fill="${lum(helmC) > .6 && !chrome ? '#c8102e' : '#ffffff'}">Arai</text>`;
  }
  }
  g += `<path d="${legR}" fill="none" stroke="rgba(120,225,255,.45)" stroke-width="2.4" stroke-dasharray="0 150 260 999"/><path d="M202,138 C220,138 236,150 246,170" stroke="rgba(120,225,255,.5)" stroke-width="2.4" fill="none" stroke-linecap="round"/>`;
  return `<svg viewBox="0 0 300 640" xmlns="http://www.w3.org/2000/svg">${defs}${g}</svg>`;
}
if (typeof module !== 'undefined') module.exports = { pilotSVG };
