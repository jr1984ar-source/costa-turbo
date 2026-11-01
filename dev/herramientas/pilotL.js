// Piloto de 3/4 mirando a la izquierda con el casco nuevo
function pilotLSVG(o, uid) {
  uid = uid || 'L' + Math.floor(Math.random() * 1e6);
  const body = pilot34SVG(Object.assign({}, o, { noHelm: true, mir: true }), uid + 'b').replace(/^<svg[^>]*>/, '').replace(/<\/svg>$/, '');
  const h = helmetL(o, uid + 'h');
  return `<svg viewBox="0 0 300 640" xmlns="http://www.w3.org/2000/svg">${h.defs}<g transform="translate(300,0) scale(-1,1)">${body}</g><g transform="translate(-2,2) scale(.86)">${h.body}</g></svg>`;
}
