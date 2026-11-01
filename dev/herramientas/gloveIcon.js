function gloveIcon(gl, uid) {
  const id = (n) => n + uid, c = gl.c, a = gl.a, tx = gl.t || '';
  const lum = (h) => { h = h.replace('#', ''); return (parseInt(h.slice(0, 2), 16) * .3 + parseInt(h.slice(2, 4), 16) * .59 + parseInt(h.slice(4, 6), 16) * .11) / 255; };
  return `<svg viewBox="0 0 80 60"><defs><linearGradient id="${id('g')}" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stop-color="#ffffff" stop-opacity=".25"/><stop offset=".5" stop-color="#ffffff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".25"/></linearGradient></defs>
  <g transform="rotate(-8 40 30)">
  <path d="M6,22 C6,16 10,14 16,14 L30,14 L30,46 L16,46 C10,46 6,42 6,36 Z" fill="${a}" stroke="rgba(0,0,0,.55)" stroke-width="1.4"/>
  <path d="M28,12 C40,8 54,9 60,12 L74,13 C78,14 78,19 74,20 L62,20 L76,22 C80,23 80,28 76,29 L62,29 L74,31 C78,32 78,37 74,38 L60,38 L70,40 C74,41 74,46 70,47 L56,47 C46,50 36,50 28,48 Z" fill="${c}" stroke="rgba(0,0,0,.55)" stroke-width="1.4" stroke-linejoin="round"/>
  <path d="M28,12 C40,8 54,9 60,12 L74,13 C78,14 78,19 74,20 L62,20 L76,22 C80,23 80,28 76,29 L62,29 L74,31 C78,32 78,37 74,38 L60,38 L70,40 C74,41 74,46 70,47 L56,47 C46,50 36,50 28,48 Z" fill="url(#${id('g')})"/>
  <path d="M44,14 C50,13 56,14 58,16 L58,44 C54,46 48,46 44,45 Z" fill="${a}" opacity=".95"/>
  <path d="M60,16 h8 M62,25 h9 M62,34 h8 M58,43 h7" stroke="${a}" stroke-width="2.4" stroke-linecap="round"/>
  <text x="17" y="33" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="7" fill="${lum(a) > .6 ? '#15171c' : '#ffffff'}" transform="rotate(-90 17 31)">${tx}</text>
  </g></svg>`;
}
