// Costa Turbo 3D: menú, piloto, taller, mapa de pantallas, 3 pantallas jugables (EL PUERTO, LA CALA, EL MAGO),
// rivales, resultados, TOP 10, dinero y pausa. Se apoya en la escena y la física de play.html (ctx).
import * as THREE from 'three';

// ---------- datos (nombres y precios del juego 2D) ----------
export const AVATARS = [
  { id: 'alex', name: 'Álex', vest: '#ff7a1a' }, { id: 'dani', name: 'Dani', vest: '#33d6ff' },
  { id: 'marc', name: 'Marc', vest: '#7be35a' }, { id: 'leo', name: 'Leo', vest: '#e3202b' },
  { id: 'lucia', name: 'Lucía', vest: '#ff3f8e' }, { id: 'sara', name: 'Sara', vest: '#1e5eff' },
  { id: 'nerea', name: 'Nerea', vest: '#ffd21a' }, { id: 'vega', name: 'Vega', vest: '#7b3fe4' }];
export const GEAR = {
  helm: [{ id: 'h0', n: 'Casco de serie', b: 'De serie', p: 0, c: '#f4f6f9' },
    { id: 'h1', n: 'S-M3 Morado', b: 'Alpinestars', p: 3000, c: '#7b5cff' }, { id: 'h2', n: 'S-M5 Rojo', b: 'Alpinestars', p: 4500, c: '#d0151f' },
    { id: 'h3', n: 'S-M5 Azul', b: 'Alpinestars', p: 6000, c: '#1e4fd8' }, { id: 'h4', n: 'S-M7 Negro', b: 'Alpinestars', p: 9000, c: '#24262c' },
    { id: 'h5', n: 'S-M8 Amarillo', b: 'Alpinestars', p: 12000, c: '#ffd21a' }, { id: 'h6', n: 'Supertech Flúor', b: 'Alpinestars', p: 16000, c: '#ff6a1a' }],
  gog: [{ id: 'g0', n: 'Gafas básicas', b: 'De serie', p: 0, c: '#1d2027' },
    { id: 'g1', n: 'Strata 2', b: '100%', p: 2000, c: '#ffd21a' }, { id: 'g2', n: 'Racecraft 2', b: '100%', p: 3500, c: '#1e5eff' },
    { id: 'g3', n: 'Armega', b: '100%', p: 5500, c: '#f4f6f9' }, { id: 'g4', n: 'Vision 8', b: 'Alpinestars', p: 2500, c: '#ff3f8e' },
    { id: 'g5', n: 'Supertech', b: 'Alpinestars', p: 5000, c: '#1d2027' }, { id: 'g6', n: 'Front Line MX', b: 'Oakley', p: 4500, c: '#e3202b' },
    { id: 'g7', n: 'Airbrake MX', b: 'Oakley', p: 6500, c: '#ff7a1a' }],
  glove: [{ id: 'gl0', n: 'Guantes negros', b: 'De serie', p: 0, c: '#1d2027' },
    { id: 'gl1', n: 'Matrix Race', b: 'Jet Pilot', p: 2000, c: '#e3202b' }, { id: 'gl2', n: 'RX Race', b: 'Jet Pilot', p: 3500, c: '#ffd21a' },
    { id: 'gl3', n: 'Radar', b: 'Alpinestars', p: 1500, c: '#1e5eff' }, { id: 'gl4', n: 'Techstar', b: 'Alpinestars', p: 4000, c: '#f4f6f9' },
    { id: 'gl5', n: 'Superlite', b: "O'Neill", p: 1200, c: '#33a3ff' }, { id: 'gl6', n: 'Reactor', b: "O'Neill", p: 2500, c: '#ff7a1a' }],
  vest: [{ id: 'v0', n: 'Chaleco de serie', b: 'De serie', p: 0, c: null },
    { id: 'v1', n: 'Venture', b: 'Jet Pilot', p: 2500, c: '#ff7a1a' }, { id: 'v2', n: 'Matrix Race', b: 'Jet Pilot', p: 5000, c: '#1e5eff' },
    { id: 'v3', n: 'RX Vault', b: 'Jet Pilot', p: 8500, c: '#16181d' }, { id: 'v4', n: 'Cause Neo', b: 'Jet Pilot', p: 12000, c: '#f4f6f9' },
    { id: 'v5', n: 'F-86 Carbon', b: 'Jet Pilot', p: 18000, c: '#25282e' }],
  suit: [{ id: 's0', n: 'Licra y bañador', b: 'De serie', p: 0, c: null },
    { id: 's1', n: 'Neopreno negro', b: 'Neopreno', p: 500, c: '#1d2027' }, { id: 's2', n: 'Neopreno azul océano', b: 'Neopreno', p: 900, c: '#1e5eff' },
    { id: 's3', n: 'Neopreno rojo racing', b: 'Neopreno', p: 1300, c: '#e3202b' }, { id: 's4', n: 'Neopreno flúor', b: 'Neopreno', p: 1800, c: '#b6f01e' },
    { id: 's5', n: 'Neopreno camuflaje marino', b: 'Neopreno', p: 2400, c: '#2f6f8f' }, { id: 's6', n: 'Neopreno carbono y oro', b: 'Neopreno', p: 3200, c: '#2a2d33' }]};
const CAT = [['helm', 'CASCO'], ['gog', 'GAFAS'], ['glove', 'GUANTES'], ['vest', 'CHALECO'], ['suit', 'NEOPRENO']];
const MOTOS = [['kawasaki', 'KAWASAKI ULTRA 310'], ['yamahafx', 'YAMAHA FX (BLENDER)'], ['yamahafxia', 'YAMAHA FX NEGRA']];
// pantallas: recorridos comprobados en agua profunda
export const ZONES = [
  { id: 'puerto', name: 'EL PUERTO', obj: 'time', goal: 'Llega a la meta antes de que se acabe el tiempo. Cada punto de control te da más tiempo.', xa: 300, xb: -300, off: 32, amp: 5, per: 85, prize: 1500, riv: 0 },
  { id: 'cala', name: 'LA CALA', obj: 'slalom', goal: 'Pasa por dentro de las boyas. Cada una que falles te quita 1 segundo.', xa: -290, xb: 270, off: 42, amp: 0, per: 1, prize: 1200, riv: 0 },
  { id: 'mago', name: 'EL MAGO', obj: 'race3', goal: 'Llega a la meta entre los 3 primeros. Cinco rivales salen contigo.', xa: 300, xb: -305, off: 62, amp: 16, per: 120, prize: [3000, 2000, 1000], riv: 5 }];

// ---------- guardado ----------
const SAVE_KEY = 'ct3d_save';
function load() { try { const s = JSON.parse(localStorage.getItem(SAVE_KEY)); if (s && s.v === 1) return s; } catch (e) {} return { v: 1, cash: 2000, unlocked: 1, pilot: 0, name: 'JUGADOR', own: ['h0', 'g0', 'gl0', 'v0', 's0'], eq: { helm: 'h0', gog: 'g0', glove: 'gl0', vest: 'v0', suit: 's0' }, top: {}, done: {} }; }
const S = load();
function save() { try { localStorage.setItem(SAVE_KEY, JSON.stringify(S)); } catch (e) {} }
const gearById = id => { for (const k in GEAR) { const g = GEAR[k].find(x => x.id === id); if (g) return g; } return null; };
const fmtT = t => { t = Math.max(0, t); const m = Math.floor(t / 60), s = t - m * 60; return (m ? m + ':' + (s < 10 ? '0' : '') : '') + s.toFixed(2); };

// ---------- estilos ----------
const CSS = `
@import url('https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@600;800;900&display=swap');
#ui{position:fixed;inset:0;z-index:20;font-family:"Saira Condensed","Arial Narrow",Arial,sans-serif;color:#fff;display:none;pointer-events:auto}
#ui.on{display:block}
#ui .bg{position:absolute;inset:0;background:radial-gradient(120% 90% at 50% 10%,rgba(4,30,60,.25),rgba(2,10,24,.86))}
#ui .scr{position:absolute;inset:0;display:none;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:20px 16px;box-sizing:border-box;overflow:auto}
#ui .scr.on{display:flex}
#ui h1{margin:0;font-weight:900;font-style:italic;font-size:clamp(56px,11vw,128px);line-height:.86;letter-spacing:.01em;text-align:center;
  background:linear-gradient(180deg,#fff7c2 0%,#ffd21a 38%,#ff7a1a 70%,#e3202b 100%);-webkit-background-clip:text;background-clip:text;color:transparent;
  filter:drop-shadow(0 4px 0 #0b1630) drop-shadow(0 10px 24px rgba(0,0,0,.6))}
#ui h1 small{display:block;font-size:.26em;letter-spacing:.42em;color:#9fe6ff;-webkit-text-fill-color:#9fe6ff;font-style:normal;font-weight:800;margin-top:10px}
#ui h2{margin:0;font-weight:900;font-style:italic;font-size:clamp(34px,6vw,58px);letter-spacing:.02em;text-shadow:0 4px 0 #0b1630}
#ui .sub{opacity:.85;font-weight:600;font-size:18px;max-width:640px;text-align:center}
#ui .row{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}
#ui .btn{appearance:none;border:3px solid rgba(255,255,255,.75);background:rgba(11,22,48,.6);color:#fff;font:800 22px "Saira Condensed","Arial Narrow",Arial;letter-spacing:.06em;
  padding:10px 26px;border-radius:999px;cursor:pointer;min-width:200px;transition:transform .12s,background .12s,border-color .12s}
#ui .btn.main{background:linear-gradient(180deg,#ffb02e,#ff6a1a);border-color:#ffe14d;font-size:28px;min-width:260px;text-shadow:0 2px 0 rgba(0,0,0,.25)}
#ui .btn:focus,#ui .btn:hover,#ui .card:focus,#ui .card:hover{outline:none;transform:scale(1.06);border-color:#ffe14d}
#ui .btn[disabled]{opacity:.4;pointer-events:none}
#ui .cash{position:absolute;top:14px;right:18px;font-weight:900;font-size:26px;color:#ffe14d;text-shadow:0 2px 0 #0b1630}
#ui .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:12px;width:min(1100px,96vw)}
#ui .card{appearance:none;border:3px solid rgba(255,255,255,.35);background:rgba(11,22,48,.65);color:#fff;border-radius:16px;padding:10px;cursor:pointer;text-align:center;font-family:inherit;transition:transform .12s,border-color .12s}
#ui .card.sel{border-color:#ffe14d;box-shadow:0 0 0 3px rgba(255,225,77,.35)}
#ui .card .img{width:100%;aspect-ratio:1;border-radius:10px;background:#05070b center/cover no-repeat;margin-bottom:8px;position:relative;overflow:hidden}
#ui .card .sw{position:absolute;inset:18%;border-radius:50%;box-shadow:0 0 40px rgba(255,255,255,.12) inset}
#ui .card b{display:block;font-size:19px;font-weight:800;line-height:1.05}
#ui .card i{display:block;font-style:normal;font-size:14px;opacity:.75}
#ui .card em{display:block;font-style:normal;font-weight:900;font-size:17px;color:#ffe14d;margin-top:4px}
#ui .tabs{display:flex;gap:8px;flex-wrap:wrap;justify-content:center}
#ui .tabs .btn{min-width:0;font-size:18px;padding:6px 16px}
#ui .tabs .btn.sel{background:#ffe14d;color:#0b1630;border-color:#ffe14d}
#ui .zone{width:min(900px,94vw);display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px}
#ui .zone .card{padding:18px 14px;text-align:left}
#ui .zone .card b{font-size:30px;font-style:italic}
#ui .zone .card.lock{opacity:.45}
#ui table{border-collapse:collapse;font-size:20px;font-weight:700;min-width:300px}
#ui td{padding:2px 10px}#ui tr.me td{color:#ffe14d}
#ui input{font:800 24px "Saira Condensed","Arial Narrow",Arial;padding:6px 14px;border-radius:12px;border:3px solid #ffe14d;background:#0b1630;color:#fff;text-align:center;width:240px}
#rh{position:fixed;left:0;right:0;top:10px;z-index:15;pointer-events:none;font-family:"Saira Condensed","Arial Narrow",Arial,sans-serif;color:#fff;display:none;text-align:center}
#rh .t{font-weight:900;font-size:54px;line-height:1;text-shadow:0 3px 0 #0b1630,0 0 18px rgba(0,0,0,.4)}
#rh .z{font-weight:800;font-size:16px;letter-spacing:.2em;opacity:.9}
#rh .pos{position:fixed;right:20px;top:12px;font-weight:900;font-size:44px;text-shadow:0 3px 0 #0b1630}
#rh .pos small{font-size:22px;opacity:.8}
#msg3{position:fixed;left:0;right:0;top:34%;z-index:16;text-align:center;pointer-events:none;font-family:"Saira Condensed","Arial Narrow",Arial,sans-serif;font-weight:900;font-style:italic;
  font-size:clamp(60px,12vw,150px);color:#ffe14d;text-shadow:0 6px 0 #0b1630,0 0 30px rgba(0,0,0,.5);display:none}
#msg3.small{font-size:clamp(28px,5vw,52px);top:22%}
`;

export async function createGame(ctx) {
  const { scene, P, env, heightAt, coastZ, makeBuoy, Wake, Snd } = ctx;
  const st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
  const ui = document.createElement('div'); ui.id = 'ui'; ui.innerHTML = '<div class="bg"></div>'; document.body.appendChild(ui);
  const rh = document.createElement('div'); rh.id = 'rh'; rh.innerHTML = '<div class="z"></div><div class="t">0.00</div><div class="pos"></div>'; document.body.appendChild(rh);
  const msg = document.createElement('div'); msg.id = 'msg3'; document.body.appendChild(msg);
  const scr = {}; const mk = (id, html) => { const d = document.createElement('div'); d.className = 'scr'; d.innerHTML = html; ui.appendChild(d); scr[id] = d; return d; };
  let state = 'menu', zone = null, R = null, msgT = 0;
  const show = id => { for (const k in scr) scr[k].classList.toggle('on', k === id); ui.classList.toggle('on', !!id); const f = id && scr[id].querySelector('.btn.main,.card:not(.lock),.btn'); if (f) setTimeout(() => f.focus(), 30); };
  const flash = (txt, t = 1.2, small = false) => { msg.textContent = txt; msg.className = small ? 'small' : ''; msg.style.display = 'block'; msgT = t; };
  const click = () => { if (Snd.ok()) Snd.click(); };

  // ---------- portada ----------
  mk('menu', `<h1>COSTA TURBO<small>JET SKI RACING 3D</small></h1><div class="cash"></div>
    <div class="row" style="margin-top:22px"><button class="btn main" data-a="map">JUGAR</button></div>
    <div class="row"><button class="btn" data-a="pilot">PILOTO Y MOTO</button><button class="btn" data-a="taller">TALLER</button></div>
    <div class="sub" style="margin-top:10px;font-size:15px;opacity:.7">Teclado: flechas, Shift turbo, Espacio derrape, C cámara, P pausa · Mando: RT acelerar, X turbo, A derrape, START pausa</div>`);
  // ---------- mapa ----------
  mk('map', `<h2>ELIGE PANTALLA</h2><div class="cash"></div><div class="zone"></div><div class="row"><button class="btn" data-a="menu">VOLVER</button></div>`);
  // ---------- piloto ----------
  mk('pilot', `<h2>PILOTO Y MOTO</h2><div class="cash"></div><div class="grid av"></div><div class="tabs mo"></div><div class="row"><button class="btn main" data-a="menu">LISTO</button></div>`);
  // ---------- taller ----------
  mk('taller', `<h2>TALLER</h2><div class="cash"></div><div class="tabs cat"></div><div class="grid it"></div><div class="row"><button class="btn" data-a="menu">VOLVER</button></div>`);
  // ---------- briefing ----------
  mk('brief', `<h2 class="zn"></h2><div class="sub zg"></div><div class="sub zb" style="color:#ffe14d"></div><div class="row"><button class="btn main" data-a="go">¡A CORRER!</button><button class="btn" data-a="map">VOLVER</button></div>`);
  // ---------- resultados ----------
  mk('result', `<h2 class="rt"></h2><div class="sub rs" style="font-size:24px"></div><div class="sub rp" style="color:#ffe14d;font-size:30px;font-weight:900"></div>
    <div class="nm" style="display:none;text-align:center"><div class="sub" style="font-weight:800">¡TOP 10! TU NOMBRE:</div><input maxlength="12"><div class="row" style="margin-top:8px"><button class="btn" data-a="savename">GUARDAR</button></div></div>
    <div><div class="sub" style="font-weight:900;letter-spacing:.1em">TOP 10</div><table class="tt"></table></div>
    <div class="row"><button class="btn main" data-a="retry">REPETIR</button><button class="btn nx" data-a="next">SIGUIENTE PANTALLA</button><button class="btn" data-a="map">MAPA</button></div>`);
  // ---------- pausa ----------
  mk('pause', `<h2>PAUSA</h2><div class="row"><button class="btn main" data-a="resume">CONTINUAR</button></div><div class="row"><button class="btn" data-a="retry">REPETIR</button><button class="btn" data-a="map">MAPA</button></div>`);

  const refreshCash = () => ui.querySelectorAll('.cash').forEach(e => e.textContent = S.cash.toLocaleString('es-ES') + ' PTA');
  function renderMap() {
    const z = scr.map.querySelector('.zone'); z.innerHTML = '';
    ZONES.forEach((Z, i) => { const lock = i >= S.unlocked; const b = document.createElement('button'); b.className = 'card' + (lock ? ' lock' : '');
      const best = S.top[Z.id] && S.top[Z.id][0] ? 'Récord: ' + fmtT(S.top[Z.id][0].t) + ' · ' + S.top[Z.id][0].n : 'Sin récord';
      b.innerHTML = `<i>ZONA ${i + 1}</i><b>${Z.name}</b><i style="margin-top:6px">${lock ? 'Bloqueada: supera la anterior' : Z.goal}</i><em>${lock ? '' : best}</em>`;
      if (!lock) b.onclick = () => { click(); openBrief(i); }; z.appendChild(b); });
    refreshCash();
  }
  function renderPilot() {
    const g = scr.pilot.querySelector('.av'); g.innerHTML = '';
    AVATARS.forEach((A, i) => { const b = document.createElement('button'); b.className = 'card' + (S.pilot === i ? ' sel' : '');
      b.innerHTML = `<div class="img" style="background:radial-gradient(circle at 50% 40%,${A.vest} 0 34%,#05070b 35%)"></div><b>${A.name}</b><i>Chaleco ${A.vest.toUpperCase()}</i>`;
      b.onclick = async () => { click(); S.pilot = i; save(); renderPilot(); await ctx.applyGear(gearLook()); }; g.appendChild(b); });
    const mo = scr.pilot.querySelector('.mo'); mo.innerHTML = '';
    MOTOS.forEach(([k, n]) => { const b = document.createElement('button'); b.className = 'btn' + (ctx.PAINT === k ? ' sel' : ''); b.textContent = n;
      b.onclick = () => { click(); if (ctx.PAINT !== k) { try { localStorage.setItem('ct3d_moto', k); } catch (e) {} location.search = '?paint=' + k; } }; mo.appendChild(b); });
    refreshCash();
  }
  let tCat = 'helm';
  function renderTaller() {
    const tb = scr.taller.querySelector('.cat'); tb.innerHTML = '';
    CAT.forEach(([k, n]) => { const b = document.createElement('button'); b.className = 'btn' + (tCat === k ? ' sel' : ''); b.textContent = n; b.onclick = () => { click(); tCat = k; renderTaller(); }; tb.appendChild(b); });
    const g = scr.taller.querySelector('.it'); g.innerHTML = '';
    GEAR[tCat].forEach(it => { const own = S.own.includes(it.id), eq = S.eq[tCat] === it.id; const b = document.createElement('button'); b.className = 'card' + (eq ? ' sel' : '');
      const col = it.c || AVATARS[S.pilot].vest;
      b.innerHTML = `<div class="img" style="background-image:url('assets/taller/${it.id}.jpg'),radial-gradient(circle at 50% 45%,${col} 0 30%,#0b0d12 31%,#05070b 70%)"></div><b>${it.n}</b><i>${it.b}</i><em>${eq ? 'EQUIPADO' : own ? 'EQUIPAR' : it.p.toLocaleString('es-ES') + ' PTA'}</em>`;
      b.onclick = async () => {
        if (!own) { if (S.cash < it.p) { flash('NO TIENES BASTANTES PTA', 1.2, true); if (Snd.ok()) Snd.miss(); return; } S.cash -= it.p; S.own.push(it.id); if (Snd.ok()) Snd.cash(); }
        else click();
        S.eq[tCat] = it.id; save(); renderTaller(); await ctx.applyGear(gearLook()); };
      g.appendChild(b); });
    refreshCash();
  }
  const gearLook = () => { const v = gearById(S.eq.vest), h = gearById(S.eq.helm), s = gearById(S.eq.suit);
    return { vest: (v && v.c) || AVATARS[S.pilot].vest, helmet: h && h.id !== 'h0' ? h.c : null, suit: s && s.c ? s.c : null }; };

  function openBrief(i) { zone = i; const Z = ZONES[i];
    scr.brief.querySelector('.zn').textContent = 'ZONA ' + (i + 1) + ' · ' + Z.name; scr.brief.querySelector('.zg').textContent = Z.goal;
    scr.brief.querySelector('.zb').textContent = 'Premio: ' + (Array.isArray(Z.prize) ? Z.prize.map((p, k) => (k + 1) + 'º ' + p.toLocaleString('es-ES')).join(' · ') : Z.prize.toLocaleString('es-ES')) + ' PTA';
    state = 'brief'; show('brief'); }

  // ---------- recorrido ----------
  const added = [];   // objetos de la pantalla actual
  function clearZone() { for (const o of added) { scene.remove(o); o.traverse && o.traverse(m => { if (m.geometry) m.geometry.dispose(); }); } added.length = 0; }
  const add = o => { scene.add(o); added.push(o); return o; };
  function buildPath(Z) { const pts = []; const n = 700; let s = 0;
    for (let i = 0; i <= n; i++) { const x = Z.xa + (Z.xb - Z.xa) * i / n, z = coastZ(x) - Z.off + Z.amp * Math.sin(x / Z.per);
      if (i) s += Math.hypot(x - pts[i - 1].x, z - pts[i - 1].z); pts.push({ x, z, s }); }
    for (let i = 0; i <= n; i++) { const a = pts[Math.max(0, i - 1)], b = pts[Math.min(n, i + 1)], L = Math.hypot(b.x - a.x, b.z - a.z) || 1; pts[i].tx = (b.x - a.x) / L; pts[i].tz = (b.z - a.z) / L; }
    return { pts, L: s }; }
  function at(path, s) { const p = path.pts; s = Math.max(0, Math.min(path.L, s)); let lo = 0, hi = p.length - 1; while (hi - lo > 1) { const m = (lo + hi) >> 1; if (p[m].s < s) lo = m; else hi = m; }
    const a = p[lo], b = p[hi], u = (s - a.s) / Math.max(1e-6, b.s - a.s); return { x: a.x + (b.x - a.x) * u, z: a.z + (b.z - a.z) * u, tx: a.tx + (b.tx - a.tx) * u, tz: a.tz + (b.tz - a.tz) * u }; }
  // lateral: + = izquierda mirando hacia delante (normal (tz,-tx) girada); usamos n = (-tz, tx)
  function locate(path, x, z, hint) { const p = path.pts; let best = 1e9, bi = hint || 0; const a = Math.max(0, bi - 60), b = Math.min(p.length - 1, bi + 60);
    for (let i = a; i <= b; i++) { const d = (p[i].x - x) ** 2 + (p[i].z - z) ** 2; if (d < best) { best = d; bi = i; } }
    const q = p[bi], dx = x - q.x, dz = z - q.z, along = dx * q.tx + dz * q.tz, lat = dx * -q.tz + dz * q.tx;
    return { i: bi, s: q.s + along, lat }; }
  const place = (o, path, s, lat, y = 0) => { const q = at(path, s); o.position.set(q.x - q.tz * lat, y, q.z + q.tx * lat); o.rotation.y = Math.atan2(q.tx, q.tz); return q; };

  function textTex(lines, w = 1024, h = 256, bg = '#0b1630', fg = '#ffe14d', check = false) {
    const c = document.createElement('canvas'); c.width = w; c.height = h; const x = c.getContext('2d');
    if (check) { const n = 16; for (let i = 0; i < n * 4; i++) { x.fillStyle = ((i % n) + Math.floor(i / n)) % 2 ? '#111' : '#fff'; x.fillRect((i % n) * w / n, Math.floor(i / n) * h / 4, w / n, h / 4); } x.fillStyle = 'rgba(11,22,48,.85)'; x.fillRect(w * .2, h * .18, w * .6, h * .64); }
    else { x.fillStyle = bg; x.fillRect(0, 0, w, h); }
    x.fillStyle = fg; x.textAlign = 'center'; x.textBaseline = 'middle';
    lines.forEach((t, i) => { x.font = `italic 900 ${i ? h * .22 : h * .46}px "Saira Condensed","Arial Narrow",Arial`; x.fillText(t, w / 2, h * (lines.length > 1 ? (i ? .78 : .4) : .52)); });
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; return t; }
  function arch(label, path, s, half = 16, check = true) {
    const g = new THREE.Group(); const poleM = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: .4 }), redM = new THREE.MeshStandardMaterial({ color: 0xe3202b, roughness: .4 });
    for (const sg of [-1, 1]) { const p = new THREE.Mesh(new THREE.CylinderGeometry(.22, .3, 7, 12), sg > 0 ? poleM : redM); p.position.set(sg * half, 3.2, 0); p.castShadow = true; g.add(p);
      const fl = new THREE.Mesh(new THREE.CylinderGeometry(1.1, 1.4, .9, 16), new THREE.MeshPhysicalMaterial({ color: 0xff7a1a, roughness: .35, clearcoat: .6 })); fl.position.set(sg * half, .1, 0); g.add(fl); }
    const bm = new THREE.MeshStandardMaterial({ map: textTex([label], 1024, 128, '#0b1630', '#ffe14d', check), roughness: .6 });
    for (const ry of [0, Math.PI]) { const ban = new THREE.Mesh(new THREE.PlaneGeometry(half * 2 + .6, 2.6), bm); ban.position.y = 6.2; ban.rotation.y = ry; ban.castShadow = true; g.add(ban); }   // dos caras: el texto se lee desde los dos lados
    place(g, path, s, 0); return add(g); }
  function jjBar() {   // JJ'S SPORTS LOUNGE, en la costa de la izquierda al salir del puerto
    const g = new THREE.Group(), x = 262, z = coastZ(262) + 15, y = heightAt(x, z);
    const wall = new THREE.MeshStandardMaterial({ color: 0xf2efe6, roughness: .8 }), wood = new THREE.MeshStandardMaterial({ color: 0x8a5a33, roughness: .7 });
    const base = new THREE.Mesh(new THREE.BoxGeometry(14, 4, 8), wall); base.position.y = 2; base.castShadow = base.receiveShadow = true; g.add(base);
    const roof = new THREE.Mesh(new THREE.BoxGeometry(16, .5, 10), wood); roof.position.y = 4.3; roof.castShadow = true; g.add(roof);
    const deck = new THREE.Mesh(new THREE.BoxGeometry(16, .3, 5), wood); deck.position.set(0, .2, -6.4); deck.receiveShadow = true; g.add(deck);
    const sign = new THREE.Mesh(new THREE.PlaneGeometry(12, 2.4), new THREE.MeshStandardMaterial({ map: textTex(["JJ'S SPORTS LOUNGE", 'EL BAR DEL PUERTO'], 1024, 210, '#0b1630', '#ffe14d'), emissive: 0x332200, roughness: .5 }));
    sign.position.set(0, 5.9, -5.05); sign.rotation.y = Math.PI; g.add(sign);
    const pole = new THREE.Mesh(new THREE.BoxGeometry(.3, 2.2, .3), wood); for (const sx of [-5.5, 5.5]) { const p = pole.clone(); p.position.set(sx, 5, -5); g.add(p); }
    for (let i = 0; i < 4; i++) { const u = ctx.makeUmbrella ? ctx.makeUmbrella(i % 2 ? '#ffd21a' : '#1e5eff') : null; if (u) { u.position.set(-6 + i * 4, .3, -9); g.add(u); } }
    g.position.set(x, y, z); return add(g); }

  // ---------- rivales ----------
  const RIVC = ['#e3202b', '#1e5eff', '#7be35a', '#ffd21a', '#ff3f8e'], RIVN = ['Toni Marín', 'Carla Ruiz', 'El Tito', 'Sandra Vidal', 'Javi Rubio'];
  let rivPool = null;
  async function makeRivals(n) {
    if (!rivPool) { rivPool = []; for (let i = 0; i < 5; i++) { const sk = await ctx.loadSki('kawasaki'); const rd = await ctx.makeRider({ vest: RIVC[i] });
        rd.position.set(0, 0.74, -0.75); rd.userData.barY = 0.13; sk.body.add(rd); rd.userData.pose({ barY: .13, k: .6 }); const wk = new Wake(env);
        rivPool.push({ sk, rd, wk, name: RIVN[i] }); } }
    return rivPool.slice(0, n).map((o, i) => ({ ...o, s: 0, lane: 0, laneT: 0, v: 0, vmax: 19.2 + i * .55 + Math.random() * .8, fin: null, tl: 0, steer: 0 }));
  }

  // ---------- carrera ----------
  async function startRace(i) {
    state = 'loading'; show(null); flash('CARGANDO…', 99, true);
    clearZone(); const Z = ZONES[i]; const path = buildPath(Z);
    R = { Z, path, t: 0, pen: 0, time: 0, cps: [], gates: [], rivals: [], hint: 0, s: 0, lat: 0, done: false, count: 3.6, lastCount: 4, maxS: 0, finished: [] };
    // salida y meta
    arch('META', path, path.L - 4, 16, true);
    if (Z.obj === 'time') { jjBar(); R.time = 21; R.cps = [path.L / 3, path.L * 2 / 3].map(s => ({ s, hit: false, add: 16 }));
      for (const c of R.cps) arch('CHECKPOINT', path, c.s, 18, false);
      for (let s = 40; s < path.L - 20; s += 55) for (const sg of [-1, 1]) { const b = makeBuoy(sg > 0 ? '#ff7a1a' : '#ffffff'); place(b, path, s, sg * 20, .05); add(b); } }
    if (Z.obj === 'slalom') { let k = 0; for (let s = 60; s < path.L - 30; s += 46, k++) { const c = (k % 2 ? 1 : -1) * 5.5; R.gates.push({ s, c, done: false });
        for (const sg of [-1, 1]) { const b = makeBuoy(sg > 0 ? '#ff7a1a' : '#ffd21a'); b.scale.setScalar(1.6); place(b, path, s, c + sg * 4.5, .2); add(b); } } }
    if (Z.riv) { R.rivals = await makeRivals(Z.riv); R.rivals.forEach((r, k) => { r.s = 12 - Math.floor((k + 1) / 2) * 7 - ((k + 1) % 2) * 3.5; r.lane = r.laneT = (k % 2 ? 1 : -1) * (4 + Math.floor(k / 2) * 4); scene.add(r.sk.root); scene.add(r.wk.mesh); added.push(r.sk.root, r.wk.mesh); r.wk.pts.length = 0; }); }
    // jugador a la salida
    const q = at(path, 14); P.x = q.x; P.z = q.z; P.th = Math.atan2(q.tx, q.tz); P.v = 0; P.slip = 0; P.steer = 0; P.energy = 1; P.dc = 0; ctx.resetFx && ctx.resetFx();
    rh.querySelector('.z').textContent = 'ZONA ' + (i + 1) + ' · ' + Z.name; rh.style.display = 'block';
    msg.style.display = 'none'; ctx.setPaused(false); state = 'count';
  }
  function finishRace(ok, title) {
    if (R.done) return; R.done = true; state = 'result'; rh.style.display = 'none'; const Z = R.Z;
    let prize = 0, line = '', t = R.t + R.pen;
    if (Z.obj === 'time') { line = ok ? 'Tiempo: ' + fmtT(R.t) : 'Te has quedado a ' + Math.max(0, Math.round(R.path.L - R.s)) + ' m de la meta'; if (ok) prize = Z.prize; }
    if (Z.obj === 'slalom') { const miss = R.gates.filter(g => g.miss).length; line = 'Tiempo ' + fmtT(R.t) + ' + ' + miss + ' s de boyas = ' + fmtT(t); if (ok) prize = Math.max(300, Z.prize - miss * 100); }
    if (Z.obj === 'race3') { const pos = R.pos; line = 'Has quedado ' + pos + 'º de ' + (R.rivals.length + 1) + ' · ' + fmtT(R.t); ok = ok && pos <= 3; if (ok) prize = Z.prize[pos - 1]; title = ok ? (pos === 1 ? '¡HAS GANADO!' : '¡PODIO!') : 'FUERA DEL PODIO'; }
    if (ok) { S.cash += prize; S.done[Z.id] = 1; S.unlocked = Math.max(S.unlocked, Math.min(ZONES.length, zone + 2)); if (Snd.ok()) Snd.win(); } else if (Snd.ok()) Snd.fail();
    save();
    scr.result.querySelector('.rt').textContent = title; scr.result.querySelector('.rs').textContent = line;
    scr.result.querySelector('.rp').textContent = ok ? '+' + prize.toLocaleString('es-ES') + ' PTA' : '';
    const nx = scr.result.querySelector('.nx'); nx.disabled = !(zone + 1 < ZONES.length && zone + 1 < S.unlocked);
    const list = S.top[Z.id] || []; const qual = ok && (list.length < 10 || t < list[list.length - 1].t);
    R.final = t; R.qual = qual; scr.result.querySelector('.nm').style.display = qual ? 'block' : 'none';
    const inp = scr.result.querySelector('input'); inp.value = S.name || 'JUGADOR';
    renderTop(); show('result'); if (qual) setTimeout(() => inp.focus(), 60);
  }
  function renderTop(me) { const list = S.top[R.Z.id] || []; scr.result.querySelector('.tt').innerHTML = list.length ? list.map((e, k) => `<tr class="${k === me ? 'me' : ''}"><td>${k + 1}.</td><td>${e.n}</td><td>${fmtT(e.t)}</td></tr>`).join('') : '<tr><td>Aún no hay tiempos</td></tr>'; }
  function saveName() { if (!R || !R.qual) return; const n = (scr.result.querySelector('input').value || 'JUGADOR').toUpperCase().slice(0, 12); S.name = n;
    const list = S.top[R.Z.id] || (S.top[R.Z.id] = []); list.push({ n, t: R.final }); list.sort((a, b) => a.t - b.t); list.length = Math.min(10, list.length);
    const me = list.findIndex(e => e.n === n && e.t === R.final); save(); R.qual = false; scr.result.querySelector('.nm').style.display = 'none'; renderTop(me); scr.result.querySelector('.btn.main').focus(); }

  // ---------- acciones de botones ----------
  ui.addEventListener('click', async e => { const b = e.target.closest('[data-a]'); if (!b) return; const a = b.dataset.a; click();
    if (a === 'menu') { state = 'menu'; refreshCash(); show('menu'); }
    if (a === 'map') { clearZone(); R = null; rh.style.display = 'none'; ctx.setPaused(false); state = 'map'; renderMap(); show('map'); }
    if (a === 'pilot') { state = 'pilot'; renderPilot(); show('pilot'); }
    if (a === 'taller') { state = 'taller'; renderTaller(); show('taller'); }
    if (a === 'go') await startRace(zone);
    if (a === 'retry') await startRace(zone);
    if (a === 'next') { if (zone + 1 < S.unlocked) openBrief(zone + 1); }
    if (a === 'resume') { ctx.setPaused(false); state = R && R.started ? 'race' : 'count'; show(null); }
    if (a === 'savename') saveName(); });
  scr.result.querySelector('input').addEventListener('keydown', e => { e.stopPropagation(); if (e.key === 'Enter') saveName(); });

  // ---------- navegación de menús con teclado y mando ----------
  const focusables = () => [...ui.querySelectorAll('.scr.on .btn:not([disabled]), .scr.on .card:not(.lock), .scr.on input')].filter(e => e.offsetParent !== null);
  function nav(d) { const f = focusables(); if (!f.length) return; let i = f.indexOf(document.activeElement); i = i < 0 ? 0 : (i + d + f.length) % f.length; f[i].focus(); }
  function back() { if (state === 'pause') { ctx.setPaused(false); state = R && R.started ? 'race' : 'count'; show(null); return; }
    if (['map', 'pilot', 'taller'].includes(state)) { state = 'menu'; show('menu'); } else if (state === 'brief') { state = 'map'; renderMap(); show('map'); } }
  addEventListener('keydown', e => { if (!ui.classList.contains('on') || document.activeElement && document.activeElement.tagName === 'INPUT') return;
    if (['ArrowDown', 'ArrowRight'].includes(e.code)) { nav(1); e.preventDefault(); } if (['ArrowUp', 'ArrowLeft'].includes(e.code)) { nav(-1); e.preventDefault(); }
    if (e.code === 'Escape' || e.code === 'Backspace' || e.code === 'KeyP') { back(); e.preventDefault(); }
    e.stopImmediatePropagation(); }, true);   // con un menú abierto las teclas no llegan a la moto
  const pad = { prev: [] };
  function pollPad() { const gp = (navigator.getGamepads ? [...navigator.getGamepads()] : []).find(g => g && g.connected); if (!gp) return;
    const now = gp.buttons.map(b => b.pressed); const ax = gp.axes[1] || 0, ax0 = gp.axes[0] || 0; const edge = i => now[i] && !pad.prev[i];
    const st = (ax > .6 ? 1 : ax < -.6 ? -1 : 0) || (ax0 > .6 ? 1 : ax0 < -.6 ? -1 : 0);
    if (ui.classList.contains('on')) { if (edge(13) || edge(15) || (st > 0 && pad.st <= 0)) nav(1); if (edge(12) || edge(14) || (st < 0 && pad.st >= 0)) nav(-1);
      if (edge(0) && document.activeElement && document.activeElement.click) document.activeElement.click(); if (edge(1)) back(); }
    pad.st = st; pad.prev = now; }

  // ---------- pausa ----------
  function togglePause() { if (state === 'race' || state === 'count') { ctx.setPaused(true); R.prevState = state; state = 'pause'; show('pause'); }
    else if (state === 'pause') { ctx.setPaused(false); state = R.prevState || 'race'; show(null); } }

  // ---------- bucle ----------
  function update(dt) {
    pollPad();
    if (msgT > 0) { msgT -= dt; if (msgT <= 0) msg.style.display = 'none'; }
    if (!R || state === 'pause' || R.done) return;
    const Z = R.Z, path = R.path;
    if (state === 'count') { R.count -= dt; const c = Math.ceil(R.count - .6);
      if (c !== R.lastCount && c >= 0) { R.lastCount = c; if (c > 0) { flash(String(c), .9); if (Snd.ok()) Snd.beep(false); } else { flash('¡YA!', .8); if (Snd.ok()) Snd.beep(true); state = 'race'; R.started = true; } }
      rh.querySelector('.t').textContent = Z.obj === 'time' ? fmtT(R.time) : fmtT(0); P.v = 0; return; }
    // jugador en el recorrido
    const L = locate(path, P.x, P.z, R.hint); R.hint = L.i; const prevS = R.s; R.s = L.s; R.lat = L.lat; R.maxS = Math.max(R.maxS, R.s);
    if (Z.obj === 'time') { R.time -= dt; R.t += dt;
      for (const c of R.cps) if (!c.hit && prevS < c.s && R.s >= c.s) { c.hit = true; R.time += c.add; flash('+' + c.add + ' s', 1.2, true); if (Snd.ok()) Snd.check(); }
      if (R.time <= 0) { R.time = 0; return finishRace(false, '¡SE ACABÓ EL TIEMPO!'); } }
    else R.t += dt;
    if (Z.obj === 'slalom') for (const g of R.gates) if (!g.done && prevS < g.s && R.s >= g.s) { g.done = true;
      if (Math.abs(R.lat - g.c) <= 4.6) { if (Snd.ok()) Snd.gate(); } else { g.miss = true; R.pen += 1; flash('+1 s', .9, true); if (Snd.ok()) Snd.miss(); } }
    // rivales
    if (R.rivals.length) {
      for (const r of R.rivals) {
        const ahead = r.s - R.s, rub = ahead > 25 ? -.08 : ahead < -25 ? .07 : 0, vt = r.fin ? 8 : r.vmax * (1 + rub);
        r.v += (vt - r.v) * .55 * dt; r.s += r.v * dt;
        r.tl -= dt; if (r.tl <= 0) { r.tl = 2 + Math.random() * 3; r.laneT = (Math.random() * 2 - 1) * 9; }
        // apartarse del jugador y de los demás
        const q0 = at(path, r.s), px = q0.x - q0.tz * r.lane, pz = q0.z + q0.tx * r.lane, dpl = Math.hypot(px - P.x, pz - P.z);
        if (dpl < 4.5) { r.laneT = r.lane + (r.lane >= R.lat ? 3 : -3); if (dpl < 2.4) { r.v *= .985; P.v *= .99; } }
        const dl = (r.laneT - r.lane) * Math.min(1, dt * .9); r.lane += dl; r.steer += ((dl / Math.max(dt, 1e-3)) * .25 - r.steer) * Math.min(1, dt * 4);
        const q = place(r.sk.root, path, r.s, r.lane); r.sk.root.rotation.y -= r.steer * .15;
        r.sk.body.rotation.z = -r.steer * .25; r.sk.body.position.y = -.05 + Math.sin(P.t * 3 + r.vmax) * .02;
        r.rd.userData.pose({ barY: .13, steer: Math.max(-1, Math.min(1, r.steer)), k: Math.min(1, r.v / 24), t: P.t });
        const f = { x: q.tx, z: q.tz }; r.wk.update(dt, r.sk.root.position.x - f.x * 1.5, r.sk.root.position.z - f.z * 1.5, Math.min(1, r.v / 10), r.v);
        if (!r.fin && r.s >= path.L - 4) { r.fin = R.t; R.finished.push(r.name); }
      }
      const ahead = R.rivals.filter(r => (r.fin && (!R.pfin || r.fin < R.pfin)) || (!r.fin && r.s > R.s)).length; R.pos = ahead + 1;
      rh.querySelector('.pos').innerHTML = R.pos + '<small>º/' + (R.rivals.length + 1) + '</small>';
    } else rh.querySelector('.pos').innerHTML = '';
    rh.querySelector('.t').textContent = Z.obj === 'time' ? fmtT(R.time) : fmtT(R.t + R.pen);
    if (Math.abs(R.lat) > 45 && msgT <= 0) flash('VUELVE AL RECORRIDO', 1, true);
    if (R.s >= path.L - 4) { R.pfin = R.t; if (R.rivals.length) { const ahead = R.rivals.filter(r => r.fin && r.fin < R.t).length; R.pos = ahead + 1; } finishRace(true, Z.obj === 'time' ? '¡META!' : '¡META!'); }
  }

  // estado inicial: portada
  refreshCash(); show('menu');
  await ctx.applyGear(gearLook());
  return { update, drive: () => state === 'race', togglePause, state: () => state, uiOpen: () => ui.classList.contains('on'), dbg: { R: () => R, at, S } };
}
