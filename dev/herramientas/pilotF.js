// Piloto de frente con el casco de cross girado un poco (boceto)
function pilotFSVG(o, uid) {
  uid = uid || 'F' + Math.floor(Math.random() * 1e6);
  const body = pilotSVG(Object.assign({}, o, { noHelm: true }), uid + 'b').replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, '');
  const h = helmetMX(o, uid + 'h');
  return `<svg viewBox="0 0 300 640" xmlns="http://www.w3.org/2000/svg">${h.defs}${body}<g transform="translate(14,2) scale(.73)">${h.body}</g></svg>`;
}
