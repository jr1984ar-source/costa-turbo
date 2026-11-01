// Piloto de frente con casco calcado (boceto)
function pilotTSVG(o, J, uid) {
  const body = pilotSVG(Object.assign({}, o, { noHelm: true }), uid + 'b').replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, '');
  const H = tracedHelmet(J, o.gog, uid + 'h');
  const s = Math.min(196 / H.w, 186 / H.h), nx = H.w * .6, ny = H.h * .92, tx = 152 - nx * s, ty = 142 - ny * s;
  return `<svg viewBox="0 -40 300 680" xmlns="http://www.w3.org/2000/svg"><defs>${H.defs}</defs>${body}<g transform="translate(${tx.toFixed(1)} ${ty.toFixed(1)}) scale(${s.toFixed(4)})">${H.body}</g></svg>`;
}
