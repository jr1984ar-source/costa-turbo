// Prueba automática: play.html?test=1&mudo=1 juega las 3 pantallas con piloto automático (teclado) y enseña el resultado.
export async function runAutotest(G) {
  const wait = ms => new Promise(r => setTimeout(r, ms)), kd = (c, t) => dispatchEvent(new KeyboardEvent(t, { code: c, key: c }));
  const box = Object.assign(document.body.appendChild(document.createElement('pre')), { id: 'autotest' });
  Object.assign(box.style, { position: 'fixed', left: '12px', bottom: '12px', zIndex: 99, background: 'rgba(0,0,0,.75)', color: '#7be35a', font: '14px monospace', padding: '10px', margin: 0, maxWidth: '60vw', whiteSpace: 'pre-wrap' });
  const log = t => { box.textContent += t + '\n'; console.log('[autotest] ' + t); };
  const errs = []; addEventListener('error', e => errs.push(e.message));
  const P = window.__P, res = [];
  for (let z = 0; z < 3; z++) {
    G.dbg.S.lives = 6; G.dbg.S.fuel = 100;
    (document.querySelector('.scr.on [data-a=map]') || document.querySelector('[data-a=map]')).click(); for (let i = 0; i < 50 && G.state() !== 'map'; i++) await wait(100);
    document.querySelectorAll('.zone .card')[z].click(); await wait(300); document.querySelector('[data-a=go]').click();
    for (let i = 0; i < 400 && !(G.state() === 'race' && G.dbg.R()); i++) await wait(100);
    for (const m of G.dbg.R().movers || []) { m.sp = 0; m.u = 0; }   // el piloto automático no esquiva barcos: los aparta del recorrido
    kd('ArrowUp', 'keydown'); let L = null, Rt = null; const t0 = performance.now();
    while (G.state() === 'race' && performance.now() - t0 < 90000) {
      const R = G.dbg.R(), g = R.gates.find(q => !q.done), isl = R.Z.id === 'mago' && Math.abs(R.s + 20 - R.path.L * .5) < 40;
      const lat = isl ? 24 : g && g.s - R.s < 40 ? g.c : 0, q = G.dbg.at(R.path, R.s + 18), qx = q.x - q.tz * lat, qz = q.z + q.tx * lat;
      let d = Math.atan2(qx - P.x, qz - P.z) - P.th; while (d > Math.PI) d -= 2 * Math.PI; while (d < -Math.PI) d += 2 * Math.PI;
      const l = d > .04, r = d < -.04; if (l !== L) { kd('ArrowLeft', l ? 'keydown' : 'keyup'); L = l; } if (r !== Rt) { kd('ArrowRight', r ? 'keydown' : 'keyup'); Rt = r; }
      if (((performance.now() - t0) / 1000 | 0) % 6 === 2) kd('ShiftLeft', 'keydown'); else kd('ShiftLeft', 'keyup');   // usa los turbos como un jugador
      await wait(40); }
    ['ArrowUp', 'ArrowLeft', 'ArrowRight', 'ShiftLeft'].forEach(k => kd(k, 'keyup'));
    const t = document.querySelector('.scr.on .rt')?.textContent, s = document.querySelector('.scr.on .rs')?.textContent;
    const ok = G.state() === 'result' && /META|GANADO|^¡PODIO/.test(t || ''); res.push(ok); log(`${ok ? 'OK ' : 'MAL'} pantalla ${z + 1}: ${t} · ${s}`);
  }
  log(errs.length ? 'ERRORES: ' + errs.join(' | ') : 'Sin errores en la consola');
  log(res.every(Boolean) && !errs.length ? 'TODO BIEN' : 'HAY FALLOS');
  window.__autotest = { ok: res.every(Boolean) && !errs.length, res, errs };
}
