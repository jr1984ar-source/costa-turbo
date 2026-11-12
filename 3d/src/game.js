// Costa Turbo 3D: menú, piloto, taller, mapa de pantallas, 3 pantallas jugables (EL PUERTO, LA CALA, EL MAGO),
// rivales, resultados, TOP 10, dinero y pausa. Se apoya en la escena y la física de play.html (ctx).
import * as THREE from 'three';
import { PAINTS } from './paint.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';
import * as SkeletonUtils from 'three/addons/utils/SkeletonUtils.js';
const GL = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder), GLC = {};
const GLA = {}, glbAnim = n => GLA[n] || (GLA[n] = GL.loadAsync('models/' + n + '.glb'));   // modelos con animación (delfines, tortugas)
const glb = n => GLC[n] || (GLC[n] = GL.loadAsync('models/' + n + '.glb').then(r => { r.scene.traverse(o => { if (o.isMesh) { o.castShadow = o.receiveShadow = true; const m = o.material; if (m && m.metalness > .9 && !m.metalnessMap) m.metalness = 0;
  if (!o.geometry.attributes.normal) o.geometry.computeVertexNormals();
  if (/^acantilado/.test(n) && m) o.material = new THREE.MeshStandardMaterial({ map: m.map, normalMap: m.normalMap || null, roughness: 1, metalness: 0, emissive: 0xffffff, emissiveMap: m.map, emissiveIntensity: .2 }); } }); return r.scene; }));

// ---------- datos (nombres y precios del juego 2D) ----------
export const AVATARS = [
  { id: 'alex', name: 'Álex', vest: '#ff7a1a', bio: 'Rápido en la salida. Corre en el puerto desde niño.', body: 'piloto_eric', skin: 1 }, { id: 'dani', name: 'Dani', vest: '#33d6ff', bio: 'Le encantan las curvas cerradas.', body: 'piloto_eric', skin: 0.78 },
  { id: 'marc', name: 'Marc', vest: '#7be35a', bio: 'Turbo largo y mucha cabeza.', body: 'piloto_eric', skin: 1 }, { id: 'leo', name: 'Leo', vest: '#e3202b', bio: 'Duro en los choques, no se rinde nunca.', body: 'piloto_eric', skin: 0.6 },
  { id: 'lucia', name: 'Lucía', vest: '#ff3f8e', bio: 'Reina del slalom: no falla una boya.', body: 'piloto_claudia', skin: 1 }, { id: 'sara', name: 'Sara', vest: '#1e5eff', bio: 'La más rápida en recta.', body: 'piloto_carla', skin: 1 },
  { id: 'nerea', name: 'Nerea', vest: '#ffd21a', bio: 'Derrapes perfectos.', body: 'piloto_claudia', skin: 0.9 }, { id: 'vega', name: 'Vega', vest: '#7b3fe4', bio: 'Arriesga en cada curva.', body: 'piloto_carla', skin: 1 }];
export const GEAR = {
  helm: [{ id: 'h0', n: 'Casco de serie', b: 'De serie', p: 0, c: '#f4f6f9' }, { id: 'hgold', n: 'Casco Dorado', b: 'Premio escondido', p: 0, c: '#d9b55a', hidden: true },
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
const CAT = [['helm', 'CASCO'], ['gog', 'GAFAS'], ['glove', 'GUANTES'], ['vest', 'CHALECO'], ['suit', 'NEOPRENO'], ['parts', 'PIEZAS STAGE']];
// piezas de la moto (nombres y precios del 2D); se desbloquean al ganar pantallas
export const PARTS = [
  { id: 'turbo', n: 'Turbo', ef: 'Más aceleración', price: [3000, 5000, 8000], ic: 'propeller' },
  { id: 'bov', n: 'Válvula de descarga', ef: '«Pssshh» y recarga el turbo', price: [1500, 2500, 4000], ic: 'wind' },
  { id: 'escape', n: 'Escape deportivo', ef: 'Más punta y más ruido', price: [2000, 3500, 5500], ic: 'flame' },
  { id: 'turbina', n: 'Turbina', ef: 'Más velocidad máxima', price: [2500, 4500, 7000], ic: 'engine' },
  { id: 'intercooler', n: 'Intercooler', ef: 'El turbo dura más', price: [1800, 3000, 4800], ic: 'snowflake' },
  { id: 'aletas', n: 'Aletas', ef: 'Gira mejor', price: [1200, 2200, 3500], ic: 'steering-wheel' }];
const PART_NEED = [0, 1, 3];   // pantallas ganadas para STAGE 1, 2 y 3
const MOTOS = [['kawasaki', 'KAWASAKI ULTRA 310']];
// pantallas: recorridos comprobados en agua profunda
const MEDAL_T = { puerto: [21, 23.5, 99], cala: [22, 26, 32] }, MEDAL_C = ['#ffd21a', '#d9dde3', '#d08a4a'], MEDAL_N = ['ORO', 'PLATA', 'BRONCE'];
export const VERSION = '1.0.0';   // número de versión (cambios en LEEME.md)
// 13 medallas con premio y 5 trofeos, como en el 2D
const ACH = [['win1', 'Primera victoria', 'Gana una pantalla', 300, 'flag'], ['oroP', 'Oro en EL PUERTO', 'Medalla de oro en EL PUERTO', 500, 'medal'], ['oroC', 'Oro en LA CALA', 'Medalla de oro en LA CALA', 500, 'medal'],
  ['oroM', 'Rey del Mago', 'Gana EL MAGO', 800, 'crown'], ['perf', 'Slalom perfecto', 'LA CALA sin fallar ni una boya', 600, 'target'], ['jump', 'A volar', 'Tu primer salto en rampa', 200, 'arrow-up-right'],
  ['combo', 'Acróbata', 'Haz un combo de trucos', 500, 'rotate-360'], ['coins', 'Hucha llena', 'Coge 100 monedas en total', 400, 'coin'], ['piri', 'Amigo del Piri-Piri', 'Pasa junto al Piri-Piri', 300, 'ship'],
  ['clean', 'Sin un rasguño', 'Acaba una carrera sin chocar', 500, 'shield-check'], ['stage3', 'Motor a tope', 'Sube una pieza a STAGE 3', 700, 'engine'], ['gear', 'Equipado', 'Lleva casco, gafas, guantes, chaleco y neopreno comprados', 400, 'shirt-sport'],
  ['turbo5', 'Turbo a reventar', 'Ten 5 turbos a la vez', 300, 'bolt']];
const TROF = [[3, 'BRONCE', '#d08a4a'], [6, 'PLATA', '#d9dde3'], [9, 'ORO', '#ffd21a'], [11, 'PLATINO', '#a8f0e8'], [13, 'DIAMANTE', '#9fe6ff']];
const CUPS = ['COPA BRONCE', 'COPA PLATA', 'COPA ORO', 'COPA PLATINO', 'COPA DIAMANTE'];   // una copa por dificultad; EL MAGO es La Final
export const ZONES = [
  { id: 'puerto', name: 'EL PUERTO', obj: 'time', goal: 'Llega a la meta antes de que se acabe el tiempo. Cada punto de control te da más tiempo.', xa: 300, xb: -300, off: 32, amp: 5, per: 85, prize: 1500, riv: 5, posPrize: [1500, 1000, 500] },
  { id: 'cala', name: 'LA CALA', obj: 'slalom', goal: 'Pasa por dentro de las boyas. Cada una que falles te quita 1 segundo.', xa: -290, xb: 270, off: 42, amp: 0, per: 1, prize: 1200, riv: 0 },
  { id: 'mago', name: 'EL MAGO', obj: 'race3', goal: 'Llega a la meta entre los 3 primeros. Cinco rivales salen contigo.', xa: 300, xb: -305, off: 62, amp: 16, per: 120, prize: [3000, 2000, 1000], riv: 5 }];

// ---------- guardado ----------
const SAVE_KEY = 'ct3d_save';
function load() { try { const s = JSON.parse(localStorage.getItem(SAVE_KEY)); if (s && s.v === 1) return s; } catch (e) {} return { v: 1, cash: 1500, unlocked: 3, pilot: 0, name: 'JUGADOR', own: ['h0', 'g0', 'gl0', 'v0', 's0'], eq: { helm: 'h0', gog: 'g0', glove: 'gl0', vest: 'v0', suit: 's0' }, top: {}, done: {} }; }
const S = load(); S.unlocked = Math.max(S.unlocked || 1, 3);
S.parts = Object.assign({ turbo: 0, bov: 0, escape: 0, turbina: 0, intercooler: 0, aletas: 0 }, S.parts || {}); window.__parts = S.parts;
S.medal = S.medal || {}; S.best = S.best || {}; S.cups = S.cups || {}; S.ach = S.ach || {}; S.coinsTot = S.coinsTot || 0;
S.fuel = S.fuel ?? 100; S.lives = S.lives ?? 3;
S.paint = S.paint || 'serie'; S.dorsal = S.dorsal ?? 7; S.logo = S.logo || 'ct'; S.ownPaint = S.ownPaint || ['serie'];
S.set = Object.assign({ snd: 1, mus: 1, mt: 'suno', vol: 0.8, vib: 1, dif: 2, hide: 0, q: 'alta' }, S.set || {});
if (!S.set.dif5) { S.set.dif = [1, 2, 3][S.set.dif] ?? 2; S.set.dif5 = 1; }   // 5 niveles de dificultad como en el 2D
function save() { try { localStorage.setItem(SAVE_KEY, JSON.stringify(S)); } catch (e) {} }
const gearById = id => { for (const k in GEAR) { const g = GEAR[k].find(x => x.id === id); if (g) return g; } return null; };
const fmtT = t => { t = Math.max(0, t); const m = Math.floor(t / 60), s = t - m * 60; return (m ? m + ':' + (s < 10 ? '0' : '') : '') + s.toFixed(2); };

// ---------- estilos ----------
const CSS = `
@import url('https://fonts.googleapis.com/css2?family=Saira+Condensed:wght@600;800;900&display=swap');
@import url('https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css');
#ui{position:fixed;inset:0;z-index:20;font-family:"Saira Condensed","Arial Narrow",Arial,sans-serif;color:#fff;display:none;pointer-events:auto}
#ui.on{display:block}
#ui .bg{position:absolute;inset:0;background:radial-gradient(120% 90% at 50% 10%,rgba(4,30,60,.25),rgba(2,10,24,.86))}
#ui .scr{position:absolute;inset:0;display:none;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:20px 16px;box-sizing:border-box;overflow:auto}
#ui .scr.on{display:flex;animation:ctin .28s ease-out}
@keyframes ctin{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
#ui .logo{width:120px;height:120px;border-radius:28px;box-shadow:0 10px 30px rgba(0,0,0,.55)}
#ui .btn .ti{margin-right:8px;font-size:1.05em;vertical-align:-2px}
#ui .setrow{display:grid;grid-template-columns:220px 1fr;align-items:center;gap:14px;width:min(640px,92vw);font-weight:800;font-size:20px}
#ui .setrow .row{justify-content:flex-start}#ui .setrow .btn{min-width:0;font-size:17px;padding:6px 16px}
#ui .setrow .btn.sel{background:#ffe14d;color:#0b1630;border-color:#ffe14d}
#ui input[type=range]{width:100%;accent-color:#ffb02e;border:0;background:none}
#ui .cred{max-width:720px;font-size:16px;line-height:1.5;text-align:left;opacity:.92}
#ui .moto{display:flex;gap:18px;align-items:center;flex-wrap:wrap;justify-content:center}
#ui .stats{display:grid;grid-template-columns:auto 160px auto;gap:4px 10px;font-weight:800;font-size:15px;align-items:center}
#ui .stats i{display:block;height:9px;border-radius:9px;background:rgba(255,255,255,.15);overflow:hidden}#ui .stats i b{display:block;height:100%;background:linear-gradient(90deg,#ffb02e,#ff6a1a)}
#ui .grid.pt{grid-template-columns:repeat(auto-fill,minmax(110px,1fr))}#ui .grid.pt .card .img{aspect-ratio:1.6}
#ui .keys{display:grid;grid-template-columns:repeat(3,minmax(160px,1fr));gap:14px;width:min(900px,94vw);font-size:16px}
#ui .keys div{background:rgba(11,22,48,.6);border:2px solid rgba(255,255,255,.3);border-radius:14px;padding:12px}#ui .keys b{display:block;color:#ffe14d;font-size:19px;margin-bottom:6px}
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
#ui .podio{display:none;align-items:flex-end;gap:8px;justify-content:center}
#ui .podio div{width:130px;text-align:center;font-weight:900;font-size:16px}
#ui .podio div b{display:block;border-radius:10px 10px 0 0;font-size:34px;color:#0b1630;padding-top:6px}
#ui .podio div.me span{color:#ffe14d}
#rh{position:fixed;left:0;right:0;top:10px;z-index:15;pointer-events:none;font-family:"Saira Condensed","Arial Narrow",Arial,sans-serif;color:#fff;display:none;text-align:center}
#rh .t{font-weight:900;font-size:54px;line-height:1;text-shadow:0 3px 0 #0b1630,0 0 18px rgba(0,0,0,.4)}
#rh .z{font-weight:800;font-size:16px;letter-spacing:.2em;opacity:.9}
#rh .pos{position:fixed;right:20px;top:12px;font-weight:900;font-size:44px;text-shadow:0 3px 0 #0b1630}
#rh .mini{position:fixed;right:16px;top:70px;width:190px;height:120px;border-radius:14px;background:rgba(6,30,52,.55);border:2px solid rgba(255,255,255,.55)}
#rh .pos small{font-size:22px;opacity:.8}
#rh .lf{position:fixed;left:20px;top:14px;text-align:left;font-weight:900}
#rh .hp{font-size:26px;color:#ff3b4e;text-shadow:0 2px 0 #0b1630;letter-spacing:2px}#rh .hp .off{color:rgba(255,255,255,.25)}
#rh .fu{display:flex;align-items:center;gap:8px;font-size:22px;margin-top:4px;text-shadow:0 2px 0 #0b1630}
#rh .fu span{display:block;width:120px;height:10px;border-radius:10px;background:rgba(0,0,0,.4);border:2px solid rgba(255,255,255,.7);overflow:hidden}#rh .fu b{display:block;height:100%;background:linear-gradient(90deg,#ff6a1a,#ffd21a)}
#rh .fu.low b{background:#ff3b4e}
#rh .pt{font-size:20px;color:#ffe14d;text-shadow:0 2px 0 #0b1630;margin-top:2px}
#rh .tu{font-size:22px;color:#33d6ff;text-shadow:0 2px 0 #0b1630;letter-spacing:1px}#rh .tu .off{color:rgba(255,255,255,.22)}
#rh .co{font-size:22px;color:#ffd21a;text-shadow:0 2px 0 #0b1630;margin-top:2px}#rh .co span{color:#fff;margin-left:6px}
#msg3{position:fixed;left:0;right:0;top:34%;z-index:16;text-align:center;pointer-events:none;font-family:"Saira Condensed","Arial Narrow",Arial,sans-serif;font-weight:900;font-style:italic;
  font-size:clamp(60px,12vw,150px);color:#ffe14d;text-shadow:0 6px 0 #0b1630,0 0 30px rgba(0,0,0,.5);display:none}
#toast{position:fixed;left:50%;top:16px;z-index:40;transform:translate(-50%,-20px);opacity:0;pointer-events:none;font:900 24px "Saira Condensed","Arial Narrow",Arial,sans-serif;letter-spacing:.05em;
  padding:10px 26px;border-radius:999px;color:#fff;background:#0b1630;border:3px solid #fff;box-shadow:0 10px 30px rgba(0,0,0,.5);transition:opacity .2s,transform .2s;white-space:nowrap}
#toast.on{opacity:1;transform:translate(-50%,0)}#toast.ok{background:#14833b;border-color:#7be35a}#toast.bad{background:#a3121f;border-color:#ff7a84}
#toast .ti{margin-right:8px;vertical-align:-2px}
#sem{position:fixed;left:50%;top:84px;transform:translateX(-50%);z-index:16;display:none;gap:12px;padding:10px 14px;background:#111418;border:3px solid #2a2f37;border-radius:18px;box-shadow:0 8px 24px rgba(0,0,0,.5)}
#sem i{width:38px;height:38px;border-radius:50%;background:#2b1214;display:block;box-shadow:inset 0 3px 6px rgba(0,0,0,.6)}#sem i.r{background:#ff2b3a;box-shadow:0 0 18px #ff2b3a}#sem i.g{background:#2bd94f;box-shadow:0 0 22px #2bd94f}
#rot{position:fixed;inset:0;z-index:60;display:none;flex-direction:column;align-items:center;justify-content:center;gap:16px;background:#061428;color:#fff;font:900 26px "Saira Condensed","Arial Narrow",Arial,sans-serif;letter-spacing:.06em;text-align:center}
#rot .ti{font-size:84px;color:#ffe14d;animation:rotph 1.6s ease-in-out infinite}@keyframes rotph{0%,30%{transform:rotate(0)}60%,100%{transform:rotate(-90deg)}}
@media (orientation:portrait) and (pointer:coarse){#rot{display:flex}}
#ui~.pop,.pop{position:fixed;left:50%;top:58%;z-index:17;pointer-events:none;font:900 italic 30px "Saira Condensed","Arial Narrow",Arial,sans-serif;text-shadow:0 3px 0 #0b1630;animation:popup 1s ease-out forwards}
@keyframes popup{from{opacity:0;transform:translate(-50%,10px) scale(.8)}20%{opacity:1;transform:translate(-50%,0) scale(1.1)}to{opacity:0;transform:translate(-50%,-70px) scale(1)}}
#msg3.small{font-size:clamp(28px,5vw,52px);top:22%}
`;

export async function createGame(ctx) {
  const { scene, P, env, heightAt, coastZ, makeBuoy, Wake, Snd } = ctx;
  const st = document.createElement('style'); st.textContent = CSS; document.head.appendChild(st);
  const ui = document.createElement('div'); ui.id = 'ui'; ui.innerHTML = '<div class="bg"></div>'; document.body.appendChild(ui);
  const rh = document.createElement('div'); rh.id = 'rh'; rh.innerHTML = '<div class="z"></div><div class="t">0.00</div><div class="pos"></div><canvas class="mini" width="380" height="240"></canvas><div class="lf"><div class="hp"></div><div class="fu"><i class="ti ti-gas-station"></i><span><b></b></span></div><div class="co"><i class="ti ti-coin-filled"></i><span>0</span></div><div class="tu"></div><div class="pt"></div></div>'; document.body.appendChild(rh);
  const msg = document.createElement('div'); msg.id = 'msg3'; document.body.appendChild(msg);
  const rot = document.createElement('div'); rot.id = 'rot'; rot.innerHTML = '<i class="ti ti-device-mobile-rotated"></i>GIRA EL MÓVIL<br>PARA JUGAR EN HORIZONTAL'; document.body.appendChild(rot);   // aviso en vertical
  const sem = document.createElement('div'); sem.id = 'sem'; sem.innerHTML = '<i></i><i></i><i></i>'; document.body.appendChild(sem);   // semáforo de salida
  const semSet = n => { sem.style.display = 'flex'; [...sem.children].forEach((l, k) => l.className = n < 0 ? 'g' : k < n ? 'r' : ''); };
  const homeB = document.createElement('button'); homeB.className = 'btn'; homeB.dataset.a = 'menu'; homeB.innerHTML = '<i class="ti ti-home"></i>INICIO'; Object.assign(homeB.style, { position: 'absolute', top: '14px', left: '18px', minWidth: '0', fontSize: '18px', padding: '6px 16px', zIndex: 2 }); ui.appendChild(homeB);   // botón INICIO en todas las pantallas
  const scr = {}; const mk = (id, html) => { const d = document.createElement('div'); d.className = 'scr'; d.innerHTML = html; ui.appendChild(d); scr[id] = d; return d; };
  let state = 'menu', zone = null, R = null, msgT = 0;
  const show = id => { if (id === 'menu' && typeof renderCard === 'function') try { renderCard(); } catch (e) {} for (const k in scr) scr[k].classList.toggle('on', k === id); ui.classList.toggle('on', !!id); homeB.style.display = id && id !== 'menu' ? '' : 'none'; const f = id && scr[id].querySelector('.btn.main,.card:not(.lock),.btn'); if (f) setTimeout(() => f.focus(), 30); };
  const flash = (txt, t = 1.2, small = false, col = '') => { msg.textContent = txt; msg.className = small ? 'small' : ''; msg.style.color = col; msg.style.display = 'block'; msgT = t; };
  const click = () => { if (Snd.ok()) Snd.click(); };
  const pop = (txt, col = '#ffe14d', dx = 0) => { const e = document.createElement('div'); e.className = 'pop'; e.textContent = txt; e.style.color = col; e.style.marginLeft = dx + 'px'; document.body.appendChild(e); setTimeout(() => e.remove(), 1000); };   // puntos emergentes
  // aviso de compra, equipado o dinero insuficiente (por encima de los menús)
  const tst = document.createElement('div'); tst.id = 'toast'; document.body.appendChild(tst); let tstT = 0;
  const toast = (txt, ok) => { tst.className = (ok ? 'ok' : 'bad') + ' on'; tst.innerHTML = `<i class="ti ti-${ok ? 'circle-check' : 'alert-circle'}"></i>` + txt; clearTimeout(tstT); tstT = setTimeout(() => tst.classList.remove('on'), 1800); };
  const noCash = p => { toast('NO TIENES BASTANTES PTA · TE FALTAN ' + (p - S.cash).toLocaleString('es-ES'), false); if (Snd.ok()) Snd.miss(); };

  // ---------- portada ----------
  mk('menu', `<div class="pcard" style="position:absolute;top:14px;left:18px;display:flex;gap:12px;align-items:center;background:rgba(11,22,48,.65);border:2px solid rgba(255,255,255,.35);border-radius:16px;padding:8px 14px 8px 8px;text-align:left"></div><img class="logo" src="assets/logo.png" alt=""><h1>COSTA TURBO<small>JET SKI RACING 3D</small></h1><div class="cash"></div>
    <div class="row" style="margin-top:14px"><button class="btn main" data-a="map"><i class="ti ti-player-play-filled"></i>JUGAR</button><button class="btn main" data-a="champ"><i class="ti ti-trophy"></i>CAMPEONATO</button><button class="btn main" data-a="map"><i class="ti ti-ghost-2"></i>CARRERA LIBRE</button></div>
    <div class="row"><button class="btn" data-a="pilot"><i class="ti ti-user"></i>PILOTO Y MOTO</button><button class="btn" data-a="taller"><i class="ti ti-tools"></i>TALLER</button></div>
    <div class="row"><button class="btn" data-a="rank"><i class="ti ti-list-numbers"></i>RANKING</button><button class="btn" data-a="ach"><i class="ti ti-trophy"></i>MEDALLAS</button><button class="btn" data-a="set"><i class="ti ti-settings"></i>AJUSTES</button><button class="btn" data-a="ctrl"><i class="ti ti-device-gamepad-2"></i>CONTROLES</button><button class="btn" data-a="cred"><i class="ti ti-info-circle"></i>CRÉDITOS</button><button class="btn" data-a="fs"><i class="ti ti-maximize"></i>PANTALLA COMPLETA</button></div>
    <div style="position:absolute;bottom:10px;right:16px;font-weight:800;font-size:14px;opacity:.6">v${VERSION}</div>`);
  // ---------- mapa ----------
  mk('map', `<h2>ELIGE PANTALLA</h2><div class="cash"></div><div class="zone"></div><div class="row"><button class="btn" data-a="menu">VOLVER</button></div>`);
  // ---------- piloto ----------
  mk('pilot', `<h2>PILOTO Y MOTO</h2><div class="cash"></div><div class="grid av"></div>
    <div class="row" style="align-items:center;gap:10px;font-weight:900;letter-spacing:.1em">TU NOMBRE <input class="pname" maxlength="12" style="width:200px"></div>
    <div class="moto"><div class="tabs mo"></div><div class="stats"></div></div>
    <div class="sub" style="font-weight:900;letter-spacing:.12em">PINTURA</div><div class="grid pt"></div>
    <div class="sub" style="font-weight:900;letter-spacing:.12em">A TU GUSTO: COLOR PRINCIPAL Y DETALLES</div><div class="row sw1"></div><div class="row sw2"></div>
    <div class="row" style="align-items:center;gap:10px;font-weight:900;letter-spacing:.1em">DORSAL <input class="dors" maxlength="2" style="width:80px"> LOGO <span class="tabs lg"></span></div>
    <div class="row"><button class="btn main" data-a="menu"><i class="ti ti-check"></i>LISTO</button></div>`);
  // ---------- taller ----------
  mk('taller', `<h2>TALLER</h2><div class="cash"></div><div class="tabs cat"></div><div class="grid it"></div><div class="row"><button class="btn" data-a="menu">VOLVER</button></div>`);
  // ---------- briefing ----------
  mk('brief', `<img class="bimg" alt="" style="width:min(640px,90vw);aspect-ratio:2.05;object-fit:cover;border-radius:16px;border:3px solid rgba(255,255,255,.6);box-shadow:0 10px 30px rgba(0,0,0,.5)"><h2 class="zn"></h2><div class="sub zg"></div><div class="sub zb" style="color:#ffe14d"></div><div class="row"><button class="btn main" data-a="go">¡A CORRER!</button><button class="btn" data-a="free"><i class="ti ti-ghost-2"></i>CARRERA LIBRE</button><button class="btn" data-a="map">VOLVER</button></div>`);
  // ---------- resultados ----------
  mk('result', `<div class="md" style="display:none;text-align:center;font-weight:900;font-size:22px;letter-spacing:.1em"></div><h2 class="rt"></h2><div class="sub rs" style="font-size:24px"></div><div class="sub rp" style="color:#ffe14d;font-size:30px;font-weight:900"></div>
    <div class="nm" style="display:none;text-align:center"><div class="sub" style="font-weight:800">¡TOP 10! TU NOMBRE:</div><input maxlength="12"><div class="row" style="margin-top:8px"><button class="btn" data-a="savename">GUARDAR</button></div></div>
    <table class="desg" style="font-size:17px;min-width:340px"></table>
    <div class="podio"></div>
    <div><div class="sub" style="font-weight:900;letter-spacing:.1em">TOP 10</div><table class="tt"></table></div>
    <div class="row"><button class="btn main" data-a="retry">REPETIR</button><button class="btn nx" data-a="next">SIGUIENTE PANTALLA</button><button class="btn" data-a="map">MAPA</button></div>`);
  // ---------- ranking: TOP 10 de las tres pantallas ----------
  mk('rank', `<h2>RANKING</h2><div class="zone rk"></div><div class="row"><button class="btn main" data-a="menu"><i class="ti ti-arrow-left"></i>VOLVER</button></div>`);
  function renderRank() { scr.rank.querySelector('.rk').innerHTML = ZONES.map(Z => { const l = S.top[Z.id] || []; return `<div class="card" style="text-align:left"><b>${Z.name}</b><table style="font-size:15px;min-width:0;width:100%">${l.length ? l.map((e, k) => `<tr><td>${k + 1}.</td><td>${e.n}</td><td>${fmtT(e.t)}</td><td style="color:#ffe14d">${e.p != null ? e.p.toLocaleString('es-ES') : ''}</td></tr>`).join('') : '<tr><td>Aún no hay tiempos</td></tr>'}</table></div>`; }).join(''); }
  function renderCard() { const A = AVATARS[S.pilot], won = Object.keys(S.done).length, nA = Object.keys(S.ach || {}).length, tr = TROF.filter(t => nA >= t[0]).pop();
    scr.menu.querySelector('.pcard').innerHTML = `<div style="width:58px;height:58px;border-radius:12px;background:#05070b url('assets/taller/p_${A.id}.jpg') center/cover"></div><div><b style="font-size:20px;display:block">${S.name || 'JUGADOR'}</b><span style="color:#ffe14d;font-weight:900">${S.cash.toLocaleString('es-ES')} PTA</span><br><span style="font-size:14px;opacity:.85">Pantallas ${won}/${ZONES.length} · Medallas ${nA}/13${tr ? ' · Trofeo ' + tr[1] : ''}</span></div>`; }
  // ---------- medallas y trofeos ----------
  mk('ach', `<h2>MEDALLAS Y TROFEOS</h2><div class="cash"></div><div class="tro row"></div><div class="grid ach" style="grid-template-columns:repeat(auto-fill,minmax(190px,1fr))"></div><div class="row"><button class="btn main" data-a="menu"><i class="ti ti-arrow-left"></i>VOLVER</button></div>`);
  function renderAch() { const n = Object.keys(S.ach).length;
    scr.ach.querySelector('.tro').innerHTML = CUPS.map((c, k) => `<div class="card" style="min-width:110px;${S.cups[k] ? '' : 'opacity:.35'}"><i class="ti ti-cup" style="font-size:40px;color:#ffe14d;opacity:1"></i><b>${c}</b><i>${S.cups[k] ? S.cups[k].toLocaleString('es-ES') + ' pts' : 'Sin ganar'}</i></div>`).join('') + TROF.map(([k, nm, c]) => `<div class="card" style="min-width:110px;${n >= k ? '' : 'opacity:.35'}"><i class="ti ti-trophy" style="font-size:40px;color:${c};opacity:1"></i><b>${nm}</b><i>${k} medallas</i></div>`).join('');
    scr.ach.querySelector('.ach').innerHTML = ACH.map(([id, nm, d, p, ic]) => `<div class="card" style="${S.ach[id] ? 'border-color:#ffe14d' : 'opacity:.45'}"><i class="ti ti-${ic}" style="font-size:38px;color:${S.ach[id] ? '#ffe14d' : '#fff'};opacity:1"></i><b>${nm}</b><i>${d}</i><em>${S.ach[id] ? 'CONSEGUIDA' : '+' + p + ' PTA'}</em></div>`).join(''); refreshCash(); }
  const award = id => { if (S.ach[id]) return; const a = ACH.find(x => x[0] === id); if (!a) return; S.ach[id] = 1; S.cash += a[3]; save(); toast('MEDALLA: ' + a[1].toUpperCase() + ' +' + a[3] + ' PTA', true); if (Snd.ok()) Snd.win();
    const n = Object.keys(S.ach).length, t = TROF.find(x => x[0] === n); if (t) setTimeout(() => toast('¡TROFEO DE ' + t[1] + '!', true), 1900); };
  // ---------- ajustes ----------
  mk('set', `<h2>AJUSTES</h2><div class="setrows"></div><div class="row"><button class="btn main" data-a="menu"><i class="ti ti-check"></i>LISTO</button></div>`);
  // ---------- controles ----------
  mk('ctrl', `<h2>CONTROLES</h2><div class="keys">
    <div><b><i class="ti ti-keyboard"></i> TECLADO</b>Flechas o WASD: acelerar, frenar y girar<br>Shift o X: turbo<br>Espacio o Z: derrape<br>C: cámara dron / onboard<br>P o Esc: pausa</div>
    <div><b><i class="ti ti-device-gamepad-2"></i> MANDO</b>Stick izquierdo: girar<br>RT o B: acelerar · LT: frenar<br>X: turbo · A: derrape<br>START: pausa<br>Menús: cruceta, A elegir, B volver</div>
    <div><b><i class="ti ti-hand-finger"></i> TÁCTIL</b>Flechas abajo a la izquierda: girar<br>ACELERAR: el botón grande<br>TURBO y DERRAPE encima<br>CÁMARA: botón de la izquierda<br>Se pueden ocultar en Ajustes</div></div>
    <div class="sub" style="font-size:15px">Derrape: mantén DERRAPE en la curva y suéltalo para un mini-turbo. En las rampas, en el aire: girar = 360, DERRAPE = mortal, TURBO = superman (juntos = combo). Suelta a tiempo para caer bien.</div>
    <div class="row"><button class="btn main" data-a="menu"><i class="ti ti-arrow-left"></i>VOLVER</button></div>`);
  // ---------- créditos ----------
  mk('cred', `<h2>CRÉDITOS</h2><div class="cred">
    <b>COSTA TURBO 3D</b> · un juego de JRAR.<br><br>
    Modelos 3D con licencia Creative Commons Attribution (CC BY 4.0), de Sketchfab:<br>
    · Kawasaki 310XUltra Jet Ski — XOIAL<br>· Motocross Helmet (Final) — Sharpsterman<br>· Life Vest / Life Jacket — DanTronMcTronDan<br>
    · Eric Rigged 001, Carla Rigged 001 y Claudia Rigged 002 — Renderpeople<br>· Realistic HD Mexican fan palm (8/10) y Canary Island date palm (31/40) — PlantCatalog<br>
    · Washingtonia Robusta Palm_03 — andre.arq.89<br>· Coconut Palm y Date Palm — evolveduk<br>
    · bateau RIVA boat — maxipub<br>· Yacht II — agt14032013<br>· Fishing Ship game-ready asset — crazyyuan<br>· Fisher boat — Batuhan13<br>· Fishing Boat — RafaelBR873D<br>· lighthouse — Lora_o<br>· Rocky coast of the Sea of Japan N5 y N7 — sepett<br>· lighthouse on a sea rock — Nikseno<br>· Tropical Stroll, Tropical Confidence y Tropical Leaf Bikini — restore50<br>· Bikini Swimsuit V4 — Fadly.W<br>· Game-Ready dolphin (Swimming) — Allie2k<br>· Model 53A - Flatback Sea Turtle — DigitalLife3D<br>· Day3_kayak — muru<br>· Sailboat — mr00T<br>· pine — local.yany<br><br>
    Texturas, rocas y cielos de Poly Haven (CC0). Música: «Jet-Ski Paradise», creada con Suno. Motor 3D: three.js.</div>
    <div class="row"><button class="btn main" data-a="menu"><i class="ti ti-arrow-left"></i>VOLVER</button></div>`);
  let wl = null; const keepAwake = on => { try { if (on && !wl && navigator.wakeLock) navigator.wakeLock.request('screen').then(l => { wl = l; l.addEventListener('release', () => wl = null); }).catch(() => {}); else if (!on && wl) { wl.release(); wl = null; } } catch (e) {} };
  document.addEventListener('visibilitychange', () => { if (document.hidden && (state === 'race' || state === 'count')) togglePause(); if (!document.hidden && (state === 'race' || state === 'count')) keepAwake(true); });
  // ---------- pausa ----------
  mk('pause', `<h2>PAUSA</h2><div class="row"><button class="btn main" data-a="resume"><i class="ti ti-player-play-filled"></i>CONTINUAR</button></div><div class="row"><button class="btn" data-a="retry"><i class="ti ti-reload"></i>REPETIR</button><button class="btn" data-a="map"><i class="ti ti-map"></i>MAPA</button><button class="btn" data-a="menu"><i class="ti ti-home"></i>MENÚ</button></div>
    <div class="row"><button class="btn" data-a="tsnd"></button><button class="btn" data-a="tmus"></button></div>`);

  // ---------- JJ'S SPORTS LOUNGE (bar del muelle en EL PUERTO) ----------
  mk('jj', `<h2>JJ'S SPORTS LOUNGE</h2><div class="cash"></div><div class="sub">Cada parada cuesta 3 s</div><div class="grid jjl" style="width:min(720px,94vw)"></div>
    <div class="row"><button class="btn main" data-a="jjout"><i class="ti ti-player-play-filled"></i>SEGUIR CORRIENDO</button></div>`);
  mk('roxy', `<h2>ROXY BAR</h2><div class="cash"></div><div class="sub">Piezas STAGE y gasolina · cada parada cuesta 3 s</div><div class="grid rxl" style="width:min(900px,94vw)"></div>
    <div class="row"><button class="btn main" data-a="jjout"><i class="ti ti-player-play-filled"></i>SEGUIR CORRIENDO</button></div>`);
  function renderRoxy() { const L0 = scr.roxy.querySelector('.rxl'); L0.innerHTML = ''; const won = Object.keys(S.done).length;
    const fb = document.createElement('button'); const fFull = S.fuel >= 99; fb.className = 'card' + (fFull ? ' sel' : ''); fb.innerHTML = `<div class="img" style="display:grid;place-items:center;aspect-ratio:1.4;background:radial-gradient(circle at 50% 45%,#3a1230,#05070b 70%)"><i class="ti ti-gas-station" style="font-size:56px;color:#ffe14d"></i></div><b>Llenar el depósito</b><i>Ahora: ${Math.ceil(S.fuel)} %</i><em>${fFull ? 'LLENO' : '300 PTA'}</em>`;
    fb.onclick = () => { if (fFull) return; if (S.cash < 300) return noCash(300); S.cash -= 300; S.fuel = 100; save(); toast('DEPÓSITO LLENO', true); if (Snd.ok()) Snd.cash(); hud(); renderRoxy(); }; L0.appendChild(fb);
    PARTS.forEach(pt => { const lv = S.parts[pt.id] | 0, nxt = lv < 3 ? pt.price[lv] : 0, lock = lv < 3 && won < PART_NEED[lv], b = document.createElement('button'); b.className = 'card' + (lv ? ' sel' : '');
      b.innerHTML = `<div class="img" style="display:grid;place-items:center;aspect-ratio:1.4;background:radial-gradient(circle at 50% 45%,#1d2b44,#05070b 70%)"><i class="ti ti-${pt.ic}" style="font-size:56px;color:#ffe14d"></i></div><b>${pt.n}</b><i>STAGE ${lv}/3</i><em>${lv >= 3 ? 'MÁX' : lock ? 'BLOQUEADA' : nxt.toLocaleString('es-ES') + ' PTA'}</em>`;
      b.onclick = () => { if (lv >= 3 || lock) { if (Snd.ok()) Snd.miss(); return; } if (S.cash < nxt) return noCash(nxt); S.cash -= nxt; S.parts[pt.id] = lv + 1; window.__parts = S.parts; save(); toast('COMPRADO: ' + pt.n.toUpperCase() + ' STAGE ' + (lv + 1), true); if (Snd.ok()) Snd.cash(); if (lv + 1 >= 3) award('stage3'); renderRoxy(); };
      L0.appendChild(b); }); refreshCash(); }
  const JJ_ITEMS = [{ id: 'fuel', n: 'Llenar el depósito', ef: 'Gasolina al 100 %', p: 300, ic: 'gas-station' }, { id: 'life', n: 'Vida extra', ef: '+1 corazón', p: 1500, ic: 'heart' }, { id: 'turbo', n: 'Refresco turbo', ef: '+1 turbo', p: 500, ic: 'bottle' }];
  function renderJJ() { const L0 = scr.jj.querySelector('.jjl'); L0.innerHTML = '';
    for (const it of JJ_ITEMS) { const full = it.id === 'fuel' ? S.fuel >= 99 : it.id === 'life' ? S.lives >= 6 : (P.turboU ?? 3) >= 5, b = document.createElement('button');
      const now = it.id === 'fuel' ? 'Ahora: ' + Math.ceil(S.fuel) + ' %' : it.id === 'life' ? 'Tienes ' + livesTxt() + ' corazones' : 'Tienes ' + (P.turboU ?? 3) + ' turbos';
      b.className = 'card' + (full ? ' sel' : ''); b.innerHTML = `<div class="img" style="display:grid;place-items:center;aspect-ratio:1.4;background:radial-gradient(circle at 50% 45%,#3a1220,#05070b 70%)"><i class="ti ti-${it.ic}" style="font-size:56px;color:#ffe14d"></i></div><b>${it.n}</b><i>${it.ef}</i><i>${now}</i><em>${full ? 'LLENO' : it.p.toLocaleString('es-ES') + ' PTA'}</em>`;
      b.onclick = () => { if (full) return; if (S.cash < it.p) return noCash(it.p);
        S.cash -= it.p; toast('COMPRADO: ' + it.n.toUpperCase(), true); if (it.id === 'fuel') S.fuel = 100; else if (it.id === 'life') S.lives = Math.min(6, S.lives + 1); else P.turboU = Math.min(5, (P.turboU ?? 3) + 1); save(); if (Snd.ok()) Snd.cash(); refreshCash(); renderJJ(); hud(); };
      L0.appendChild(b); } refreshCash(); }
  const livesTxt = () => { const f = Math.floor(S.lives + 1e-6), t = Math.round((S.lives - f) * 3); return f + (t ? ' y ' + t + '/3' : ''); };
  function hud() { const hp = rh.querySelector('.hp'), n = Math.max(3, Math.ceil(S.lives - 1e-6)); hp.innerHTML = Array.from({ length: n }, (_, k) => { const fr = Math.max(0, Math.min(1, S.lives - k)); return `<i class="ti ti-heart-filled" style="background:linear-gradient(90deg,#ff3b4e ${fr * 100}%,rgba(255,255,255,.25) ${fr * 100}%);-webkit-background-clip:text;background-clip:text;color:transparent;text-shadow:none;filter:drop-shadow(0 2px 0 #0b1630)"></i>`; }).join('');
    rh.querySelector('.tu').innerHTML = Array.from({ length: 5 }, (_, k) => `<i class="ti ti-bolt-filled${k < (P.turboU ?? 3) ? '' : ' off'}"></i>`).join('');
    rh.querySelector('.pt').textContent = S.cash.toLocaleString('es-ES') + ' PTA';
    const fu = rh.querySelector('.fu'); fu.querySelector('b').style.width = Math.max(0, S.fuel) + '%'; fu.classList.toggle('low', S.fuel < 18); }
  window.__onDrift = q => { if (state === 'race' && R) { const p = Math.round(q * 40) * 5; R.pts = (R.pts || 0) + p; R.drifts = (R.drifts || 0) + 1; pop('DERRAPE +' + p, '#ff8c1e'); } };
  window.__onTurboUnit = () => { if (state === 'race') pop('+1 TURBO', '#33d6ff'); };
  window.__onTrick = (spins, flips, sup) => { if (state !== 'race' || !R) return;
    if (spins < 0) { if (Snd.ok()) Snd.miss(); return loseLife(2 / 3, '¡VUELCO! −⅔ ♥'); }
    const names = []; if (flips) names.push(flips > 1 ? flips + ' MORTALES' : 'MORTAL'); if (spins) names.push(spins > 1 ? spins * 360 + '' : '360');
    if (sup) names.push('SUPERMAN'); if ((flips > 0) + (spins > 0) + !!sup > 1) award('combo'); let p = flips * 300 + spins * 200 + (sup ? 250 : 0); if ((flips > 0) + (spins > 0) + !!sup > 1) { p = Math.round(p * 1.5); names.push('COMBO ×1,5'); }
    R.pts = (R.pts || 0) + p; R.tricks = (R.tricks || 0) + 1; flash(names.join(' + '), 1.1, true, '#ffb02e'); pop('+' + p + ' PUNTOS', '#ffb02e'); if (Snd.ok()) Snd.cash(); };
  window.__onJump = () => { if (state === 'race') { R.jumps = (R.jumps || 0) + 1; R.pts = (R.pts || 0) + 100; if (window.__P && window.__P.y > 1) award('jump'); flash('¡SALTO!', .8, true, '#9fe6ff'); pop('+100 PUNTOS', '#9fe6ff'); } };
  // choque fuerte contra barco, roca o boya: se pierde un corazón
  // vidas como en el 2D: 1/3 de corazón por choque y 2/3 por volcar; sin corazones, GAME OVER
  const loseLife = (k, txt) => { if (state !== 'race' || !R || R.done || R.invT > R.t) return; R.crashed = true; R.invT = R.t + 1.6; S.lives = Math.max(0, S.lives - k); save(); hud();
    if (S.lives <= .01) { S.lives = 3; save(); if (Snd.ok()) Snd.thunder(); return finishRace(false, 'GAME OVER'); } flash(txt, 1, true, '#ff3b4e'); };
  window.__onCrash = () => loseLife(1 / 3, '¡CHOQUE! −⅓ ♥');

  const refreshCash = () => ui.querySelectorAll('.cash').forEach(e => e.textContent = S.cash.toLocaleString('es-ES') + ' PTA');
  function renderMap() {
    const z = scr.map.querySelector('.zone'); z.innerHTML = '';
    ZONES.forEach((Z, i) => { const lock = i >= S.unlocked; const b = document.createElement('button'); b.className = 'card' + (lock ? ' lock' : '');
      const best = S.top[Z.id] && S.top[Z.id][0] ? 'Récord: ' + fmtT(S.top[Z.id][0].t) + ' · ' + S.top[Z.id][0].n : 'Sin récord';
      const mg = S.medal[Z.id]; b.innerHTML = (mg != null ? `<i class="ti ti-medal" style="float:right;font-size:38px;opacity:1;color:${MEDAL_C[mg]}"></i>` : '') + `<i>ZONA ${i + 1}</i><b>${Z.name}</b><i style="margin-top:6px">${lock ? 'Bloqueada: supera la anterior' : Z.goal}</i><em>${lock ? '' : best}</em>`;
      if (!lock) b.onclick = () => { click(); openBrief(i); }; z.appendChild(b); });
    refreshCash();
  }
  function renderPilot() {
    { const pn = scr.pilot.querySelector('.pname'); pn.value = S.name || 'JUGADOR'; pn.onkeydown = e => e.stopPropagation(); pn.onchange = () => { S.name = (pn.value || 'JUGADOR').toUpperCase().slice(0, 12); pn.value = S.name; save(); toast('NOMBRE GUARDADO: ' + S.name, true); }; }
    const g = scr.pilot.querySelector('.av'); g.innerHTML = '';
    AVATARS.forEach((A, i) => { const b = document.createElement('button'); b.className = 'card' + (S.pilot === i ? ' sel' : '');
      b.innerHTML = `<div class="img" style="background-image:url('assets/taller/p_${A.id}.jpg')"></div><b>${A.name}</b><i>${A.bio}</i>`;
      b.onclick = async () => { click(); S.pilot = i; save(); renderPilot(); await ctx.applyGear(gearLook()); }; g.appendChild(b); });
    scr.pilot.querySelector('.stats').innerHTML = [['VELOCIDAD', .78, '120 km/h'], ['TURBO', .9, '150 km/h'], ['ACELERACIÓN', .72, ''], ['GIRO', .7, '']].map(([n, v, t]) => `<span>${n}</span><i><b style="width:${v * 100}%"></b></i><span>${t}</span>`).join('');
    const pt = scr.pilot.querySelector('.pt'); pt.innerHTML = '';
    PAINTS.forEach(P0 => { const own = S.ownPaint.includes(P0.id), on = S.paint === P0.id, b = document.createElement('button'); b.className = 'card' + (on ? ' sel' : '');
      const c1 = P0.main || '#16b3c7', c2 = P0.acc || '#d6e816';
      b.innerHTML = `<div class="img" style="background:linear-gradient(135deg,${c1} 0 58%,${c2} 58% 70%,#14161b 70%)"></div><b>${P0.n}</b><em>${on ? 'PUESTA' : own ? 'PONER' : P0.p + ' PTA'}</em>`;
      b.onclick = () => { if (!own) { if (S.cash < P0.p) return noCash(P0.p); S.cash -= P0.p; S.ownPaint.push(P0.id); if (Snd.ok()) Snd.cash(); toast('COMPRADA Y PUESTA: ' + P0.n.toUpperCase(), true); } else { click(); toast('PINTURA PUESTA: ' + P0.n.toUpperCase(), true); }
        S.paint = P0.id; save(); ctx.paintPlayer && ctx.paintPlayer(P0.main, P0.acc); renderPilot(); };
      pt.appendChild(b); });
    { const SW = ['#e3202b', '#ff7a1a', '#ffd21a', '#b6f01e', '#5fd31a', '#16b3c7', '#4d9bff', '#1e5eff', '#7b3fe4', '#ff3f8e', '#f5f6f8', '#8d9199', '#3a3f48', '#14161b'];
      S.pc = S.pc || { m: '#16b3c7', a: '#d6e816' };
      for (const [cls, key] of [['.sw1', 'm'], ['.sw2', 'a']]) { const row = scr.pilot.querySelector(cls); row.innerHTML = '';
        SW.forEach(c => { const b = document.createElement('button'); b.className = 'card' + (S.paint === 'custom' && S.pc[key] === c ? ' sel' : ''); b.style.cssText = `width:44px;height:44px;padding:0;border-radius:50%;background:${c}`; b.title = c;
          b.onclick = () => { click(); S.pc[key] = c; S.paint = 'custom'; save(); ctx.paintPlayer && ctx.paintPlayer(S.pc.m, S.pc.a); renderPilot(); }; row.appendChild(b); }); }
      const dn = scr.pilot.querySelector('.dors'); dn.value = S.dorsal || ''; dn.onkeydown = e => e.stopPropagation(); dn.onchange = () => { S.dorsal = Math.max(0, Math.min(99, parseInt(dn.value) || 0)); save(); ctx.setDecals && ctx.setDecals(S.dorsal, S.logo); toast('DORSAL ' + (S.dorsal || 'SIN NÚMERO'), true); };
      const lg = scr.pilot.querySelector('.lg'); lg.innerHTML = ''; for (const [id, n] of [['none', 'NINGUNO'], ['ct', 'COSTA TURBO'], ['jj', "JJ'S"], ['roxy', 'ROXY']]) { const b = document.createElement('button'); b.className = 'btn' + (S.logo === id ? ' sel' : ''); b.textContent = n;
        b.onclick = () => { click(); S.logo = id; save(); ctx.setDecals && ctx.setDecals(S.dorsal, S.logo); renderPilot(); }; lg.appendChild(b); } }
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
    if (tCat === 'parts') { const won = Object.keys(S.done).length;
      PARTS.forEach(pt => { const lv = S.parts[pt.id] | 0, nxt = lv < 3 ? pt.price[lv] : 0, need = lv < 3 ? PART_NEED[lv] : 0, lock = lv < 3 && won < need, b = document.createElement('button');
        b.className = 'card' + (lv ? ' sel' : '');
        b.innerHTML = `<div class="img" style="display:grid;place-items:center;background:radial-gradient(circle at 50% 45%,#1d2b44,#05070b 70%)"><i class="ti ti-${pt.ic}" style="font-size:64px;color:#ffe14d"></i></div><b>${pt.n}</b><i>${pt.ef}</i><i>STAGE ${lv}/3 ${'●'.repeat(lv)}${'○'.repeat(3 - lv)}</i><em>${lv >= 3 ? 'STAGE 3 · MÁX' : lock ? 'Gana ' + need + ' pantalla' + (need > 1 ? 's' : '') : 'STAGE ' + (lv + 1) + ' · ' + nxt.toLocaleString('es-ES') + ' PTA'}</em>`;
        b.onclick = () => { if (lv >= 3) { toast(pt.n.toUpperCase() + ' YA ESTÁ AL MÁXIMO', false); if (Snd.ok()) Snd.miss(); return; } if (lock) { toast('GANA ' + need + ' PANTALLA' + (need > 1 ? 'S' : '') + ' PARA DESBLOQUEARLO', false); if (Snd.ok()) Snd.miss(); return; } if (S.cash < nxt) return noCash(nxt);
          toast('COMPRADO: ' + pt.n.toUpperCase() + ' STAGE ' + (lv + 1), true); S.cash -= nxt; S.parts[pt.id] = lv + 1; if (lv + 1 >= 3) award('stage3'); window.__parts = S.parts; save(); if (Snd.ok()) Snd.cash(); renderTaller(); };
        g.appendChild(b); });
      refreshCash(); return; }
    GEAR[tCat].forEach(it => { const own = S.own.includes(it.id), eq = S.eq[tCat] === it.id; const b = document.createElement('button'); b.className = 'card' + (eq ? ' sel' : '');
      const col = it.c || AVATARS[S.pilot].vest;
      b.innerHTML = `<div class="img" style="background-image:url('assets/taller/${it.id}.jpg'),radial-gradient(circle at 50% 45%,${col} 0 30%,#0b0d12 31%,#05070b 70%)"></div><b>${it.n}</b><i>${it.b}</i><em>${eq ? 'EQUIPADO' : own ? 'EQUIPAR' : it.p.toLocaleString('es-ES') + ' PTA'}</em>`;
      if (it.hidden && !own) { b.innerHTML = `<div class="img" style="display:grid;place-items:center;background:radial-gradient(circle at 50% 45%,#3a2c10,#05070b 70%)"><i class="ti ti-lock" style="font-size:56px;color:#d9b55a"></i></div><b>${it.n}</b><i>Escondido en EL MAGO</i><em>¿DÓNDE ESTARÁ?</em>`; b.onclick = () => { if (Snd.ok()) Snd.miss(); }; g.appendChild(b); return; }
      b.onclick = async () => {
        if (!own) { if (S.cash < it.p) return noCash(it.p); S.cash -= it.p; S.own.push(it.id); if (Snd.ok()) Snd.cash(); toast('COMPRADO Y EQUIPADO: ' + it.n.toUpperCase(), true); }
        else { click(); toast(eq ? 'YA LO LLEVAS PUESTO' : 'EQUIPADO: ' + it.n.toUpperCase(), true); }
        S.eq[tCat] = it.id; save(); if (['helm', 'gog', 'glove', 'vest', 'suit'].every(k => S.eq[k] && !/0$/.test(S.eq[k]))) award('gear'); renderTaller(); await ctx.applyGear(gearLook()); };
      g.appendChild(b); });
    refreshCash();
  }
  function applySettings() { const s = S.set;
    Snd.on = !!s.snd && !ctx.MUDO; if (Snd.out) Snd.out.gain.value = Snd.on ? .8 * s.vol : 0;
    if (ctx.music) { ctx.music.muted = !s.mus || !!ctx.MUDO; }
    try { localStorage.setItem('ct3d_mus', s.mus ? '1' : '0'); } catch (e) {}
    window.__musVol = s.vol; window.__musType = s.mt; window.__musOnS = !!s.mus; window.__vibrate = ms => { if (!S.set.vib) return; try { navigator.vibrate && navigator.vibrate(ms); } catch (e) {}
      try { const gp = [...navigator.getGamepads()].find(x => x && x.connected); gp && gp.vibrationActuator && gp.vibrationActuator.playEffect('dual-rumble', { duration: ms, strongMagnitude: .8, weakMagnitude: .5 }); } catch (e) {} };
    ctx.setQuality && ctx.setQuality(s.q); ctx.setHideControls && ctx.setHideControls(!!s.hide);
    const ps = scr.pause.querySelector('[data-a=tsnd]'), pm = scr.pause.querySelector('[data-a=tmus]');
    if (ps) ps.innerHTML = '<i class="ti ti-volume' + (s.snd ? '' : '-off') + '"></i>SONIDO ' + (s.snd ? 'SÍ' : 'NO');
    if (pm) pm.innerHTML = '<i class="ti ti-music' + (s.mus ? '' : '-off') + '"></i>MÚSICA ' + (s.mus ? 'SÍ' : 'NO'); }
  function renderSet() { const s = S.set, box = scr.set.querySelector('.setrows');
    const opt = (k, vals) => vals.map(([v, n]) => `<button class="btn${s[k] === v ? ' sel' : ''}" data-set="${k}" data-v="${v}">${n}</button>`).join('');
    box.innerHTML = `<div class="setrow"><span><i class="ti ti-volume"></i> SONIDO</span><div class="row">${opt('snd', [[1, 'SÍ'], [0, 'NO']])}</div></div>
      <div class="setrow"><span><i class="ti ti-music"></i> MÚSICA</span><div class="row">${opt('mus', [[1, 'SÍ'], [0, 'NO']])}</div></div>
      <div class="setrow"><span><i class="ti ti-playlist"></i> TIPO DE MÚSICA</span><div class="row">${opt('mt', [['suno', 'JET-SKI PARADISE'], ['2d', 'LA DEL JUEGO 2D']])}</div></div>
      <div class="setrow"><span><i class="ti ti-adjustments"></i> VOLUMEN</span><input type="range" min="0" max="1" step="0.05" value="${s.vol}" data-range="vol"></div>
      <div class="setrow"><span><i class="ti ti-device-mobile-vibration"></i> VIBRACIÓN</span><div class="row">${opt('vib', [[1, 'SÍ'], [0, 'NO']])}</div></div>
      <div class="setrow"><span><i class="ti ti-gauge"></i> DIFICULTAD</span><div class="row">${opt('dif', [[0, 'MUY FÁCIL'], [1, 'FÁCIL'], [2, 'NORMAL'], [3, 'DIFÍCIL'], [4, 'EXPERTO']])}</div></div>
      <div class="setrow"><span><i class="ti ti-hand-off"></i> BOTONES TÁCTILES</span><div class="row">${opt('hide', [[0, 'VER'], [1, 'OCULTAR']])}</div></div>
      <div class="setrow"><span><i class="ti ti-photo"></i> GRÁFICOS</span><div class="row">${opt('q', [['alta', 'ALTA'], ['baja', 'BAJA (MÓVIL)']])}</div></div>
      <div class="setrow"><span><i class="ti ti-id-badge"></i> TU NOMBRE</span><input maxlength="12" data-name="1" value="${S.name || 'JUGADOR'}"></div>
      <div class="setrow"><span><i class="ti ti-transfer"></i> PASAR PARTIDA</span><div class="row"><button class="btn" data-a="exp"><i class="ti ti-copy"></i>COPIAR CÓDIGO</button><input data-imp="1" placeholder="PEGA AQUÍ EL CÓDIGO" style="width:220px;font-size:16px"></div></div>
      <div class="setrow"><span><i class="ti ti-trash"></i> PARTIDA</span><div class="row"><button class="btn" data-a="wipe">BORRAR PARTIDA</button></div></div>`;
    const im = box.querySelector('[data-imp]'); im.addEventListener('keydown', e => e.stopPropagation());
    im.onchange = () => { try { const o = JSON.parse(decodeURIComponent(escape(atob(im.value.trim())))); if (!o || o.v !== 1) throw 0; localStorage.setItem(SAVE_KEY, JSON.stringify(o)); toast('PARTIDA CARGADA', true); setTimeout(() => location.reload(), 900); } catch (e) { toast('ESE CÓDIGO NO VALE', false); } };
    box.querySelectorAll('[data-set]').forEach(b => b.onclick = () => { click(); const k = b.dataset.set, v = b.dataset.v; s[k] = isNaN(+v) ? v : +v; save(); applySettings(); renderSet(); });
    const r = box.querySelector('[data-range]'); r.oninput = () => { s.vol = +r.value; save(); applySettings(); };
    const nm = box.querySelector('[data-name]'); nm.addEventListener('keydown', e => e.stopPropagation()); nm.onchange = () => { S.name = (nm.value || 'JUGADOR').toUpperCase().slice(0, 12); save(); }; }
  const gearLook = () => { const v = gearById(S.eq.vest), h = gearById(S.eq.helm), s = gearById(S.eq.suit);
    const A = AVATARS[S.pilot], go = gearById(S.eq.gog), gv = gearById(S.eq.glove); return { vest: (v && v.c) || A.vest, helmet: h && h.id !== 'h0' ? h.c : null, suit: s && s.c ? s.c : null, body: A.body, skin: A.skin, gog: go ? go.c : '#1d2027', glove: gv ? gv.c : '#1d2027', boot: s && s.c ? s.c : '#16181d' }; };

  function openBrief(i) { zone = i; const Z = ZONES[i];
    scr.brief.querySelector('.zn').textContent = 'ZONA ' + (i + 1) + ' · ' + Z.name; scr.brief.querySelector('.zg').textContent = Z.goal;
    scr.brief.querySelector('.zb').textContent = 'Premio: ' + (Array.isArray(Z.prize) ? Z.prize.map((p, k) => (k + 1) + 'º ' + p.toLocaleString('es-ES')).join(' · ') : Z.prize.toLocaleString('es-ES')) + ' PTA';
    scr.brief.querySelector('.bimg').src = 'assets/brief_' + Z.id + '.jpg';
    state = 'brief'; show('brief'); }

  // ---------- recorrido ----------
  const added = [];   // objetos de la pantalla actual
  function clearZone() { if (typeof ghostSki !== 'undefined' && ghostSki) scene.remove(ghostSki.root); if (Snd.sirenStop) Snd.sirenStop(); ctx.setTime && ctx.setTime('mediodia'); sem.style.display = 'none'; window.__COLZ.length = 0; window.__RAMPS = []; window.__rivNear = [0, 0]; for (const o of added) { scene.remove(o); o.traverse && o.traverse(m => { if (m.geometry) m.geometry.dispose(); }); } added.length = 0; }
  const add = o => { scene.add(o); added.push(o); return o; };
  const solid = (x, z, r) => window.__COLZ.push({ x, z, r });
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
    place(g, path, s, 0); add(g); g.updateMatrixWorld(true); for (const sg of [-1, 1]) { const v = new THREE.Vector3(sg * half, 0, 0).applyMatrix4(g.matrixWorld); solid(v.x, v.z, 1.5); } return g; }
  function jjBar() {   // JJ'S SPORTS LOUNGE como en el 2D: edificio blanco de tejado gris, letrero en tres colores, terraza con velas y mesas, barandilla de madera
    const g = new THREE.Group(), x = 262, z = coastZ(262) + 16, y = heightAt(x, z);
    const M = c => new THREE.MeshStandardMaterial({ color: c, roughness: .75 }), box = (w, h, d, c, px, py, pz) => { const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), M(c)); m.position.set(px, py, pz); m.castShadow = m.receiveShadow = true; g.add(m); return m; };
    box(18, 4.4, 9, 0xf3f0ea, 0, 2.2, 0);                     // fachada blanca
    box(18.6, .45, 9.6, 0xd6dbe1, 0, 4.62, 0);                // tejado gris claro
    for (const [ax, az] of [[-5, 1], [-2, 1]]) { box(1.6, .9, 1.2, 0xc4cad2, ax, 5.3, az); }   // máquinas del aire en el tejado
    box(3.2, .5, 1.6, 0xa9bccc, 4.5, 5.05, -1.5);
    box(17.4, 1.3, .2, 0x141416, 0, 1.6, -4.55);             // franja de cristal oscuro
    // letrero en tres colores: JJ's (granate) · SPORTS (azul) · LOUNGE (negro)
    const sign = [["JJ'S", '#8e1f2c', 5.8, 5.2], ['SPORTS', '#1f3fb0', 0, 6.6], ['LOUNGE', '#1c1c1f', -6, 5.4]];
    for (const [t, col, sx, sw] of sign) { const m = new THREE.Mesh(new THREE.PlaneGeometry(sw, 1.3), new THREE.MeshStandardMaterial({ map: textTex([t], 512, 128, col, '#ffffff'), roughness: .5, emissive: 0x111111 }));
      m.position.set(sx, 3.55, -4.62); m.rotation.y = Math.PI; g.add(m); }
    // terraza de piedra con mesas y sillas de madera
    box(18.6, .25, 7, 0x6d665e, 0, .12, -8.1);
    for (const [tx, tz] of [[-6, -6.4], [-2, -6.4], [2, -6.4], [-6, -9.4], [-2, -9.4], [2, -9.4], [6, -7.9]]) {
      box(1.1, .08, 1.1, 0xf2efe6, tx, .95, tz); box(.12, .7, .12, 0x2a2522, tx, .6, tz);
      for (const s of [-1, 1]) { box(.5, .45, .5, 0x8a5530, tx + s * .95, .48, tz); box(.5, .55, .08, 0x4a2e18, tx + s * 1.18, .95, tz); } }
    // velas de sombra triangulares
    const sailM = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: .6, side: THREE.DoubleSide });
    for (const [p1, p2, p3] of [[[-9, 3.4, -4.8], [-3, 2.9, -5.2], [-7, 2.6, -11.4]], [[-4, 3.2, -4.8], [5, 3.3, -4.8], [0, 2.5, -11.5]], [[2, 2.6, -11.2], [9, 3.5, -7.5], [8.6, 2.6, -11.6]]]) {
      const gg = new THREE.BufferGeometry(); gg.setAttribute('position', new THREE.Float32BufferAttribute([...p1, ...p2, ...p3], 3)); gg.computeVertexNormals();
      const s = new THREE.Mesh(gg, sailM); s.castShadow = true; g.add(s);
      for (const pp of [p1, p2, p3]) if (pp[2] < -6) box(.1, pp[1], .1, 0xb7bfc8, pp[0], pp[1] / 2, pp[2]); }
    // barandilla de madera y jardineras
    box(18.6, .12, .12, 0xb5652e, 0, 1.05, -11.6); for (let px = -9.2; px <= 9.2; px += 1.15) box(.07, 1, .07, 0x8a4a20, px, .55, -11.6);
    for (const px of [-6, -1, 4]) { box(1.6, .7, .8, 0xffffff, px, .45, -12.6); const pl = new THREE.Mesh(new THREE.IcosahedronGeometry(.75, 1), M(0x3f8f4a)); pl.position.set(px, 1.2, -12.6); pl.scale.y = .7; pl.castShadow = true; g.add(pl); }
    // muelle de madera hacia el agua (aquí se para a repostar)
    for (let k = 0; k < 9; k++) box(3, .22, 2.2, 0xa57a4c, 0, -.05 + Math.max(0, .4 - k * .12), -14.6 - k * 2.2);
    for (let k = 0; k < 9; k += 2) for (const s of [-1, 1]) box(.25, 2.4, .25, 0x6b4a2c, s * 1.5, -.7, -14.6 - k * 2.2);
    for (let k = 0; k < 9; k++) solid(x, z - 14.6 - k * 2.2, 1.7);
    g.position.set(x, y, z); R.jjPos = { x: x + 4.5, z: z - 27 }; return add(g); }
  // ---------- escenario de EL PUERTO: muelle de salida, barcos amarrados, espigón con faro y yate fondeado ----------
  async function puertoScene() {
    const [riva, pesca, pesca2, barca, yate, faro, roca] = await Promise.all(['barco_riva', 'barco_pesca', 'barco_pesca2', 'barca', 'yate', 'faro_puerto', 'namaqualand_boulder_02'].map(glb));
    const M = (c, r = .85) => new THREE.MeshStandardMaterial({ color: c, roughness: r });
    const boat = (src, x, z, ry, y, r, bob = 1) => { const b = src.clone(); b.position.set(x, y, z); b.rotation.y = ry; b.userData.bob = { y, ph: x * .37 + z * .11, k: bob }; add(b); boats.push(b);
      // choque: círculos a lo largo de la eslora
      const L = r * 2.2; for (let k = -1; k <= 1; k++) solid(x + Math.sin(ry) * k * L, z + Math.cos(ry) * k * L, r); return b; };
    const boats = []; R.boats = boats;
    // muelle de salida de hormigón, detrás de la salida
    { const x = 318, z0 = coastZ(x) + 4, z1 = coastZ(x) - 46, L = z0 - z1, d = new THREE.Group();
      const deck = new THREE.Mesh(new THREE.BoxGeometry(6, 4.2, L), M(0xb9b2a4, .95)); deck.position.set(x, -1.05, (z0 + z1) / 2); deck.castShadow = deck.receiveShadow = true; d.add(deck);
      const edge = new THREE.Mesh(new THREE.BoxGeometry(6.3, .25, L), M(0xe9e4da, .9)); edge.position.set(x, 1.12, (z0 + z1) / 2); edge.receiveShadow = true; d.add(edge);
      for (let k = 0; k < L; k += 7) for (const s of [-1, 1]) { const b = new THREE.Mesh(new THREE.CylinderGeometry(.22, .28, .5, 10), M(0x2b2e33, .5)); b.position.set(x + s * 2.7, 1.45, z0 - 2 - k); b.castShadow = true; d.add(b);
        const t = new THREE.Mesh(new THREE.TorusGeometry(.42, .17, 10, 20), M(0x1a1a1a, .9)); t.rotation.y = Math.PI / 2; t.position.set(x + s * 3.17, .45, z0 - 4 - k); t.castShadow = true; d.add(t); }   // norays y neumáticos
      for (let z = z0 - 1; z > z1; z -= 2.2) solid(x, z, 3.3);
      add(d);
      boat(pesca, x + 7.6, coastZ(x) - 14, 0, -.55, 2.2); boat(pesca2, x + 7.4, coastZ(x) - 29, Math.PI, -.5, 2); boat(barca, x - 5.2, coastZ(x) - 22, .05, -.18, 1, 1.4); boat(riva, x - 5.6, coastZ(x) - 36, Math.PI, -.32, 1.6); }
    // Riva amarrada al muelle del JJ'S
    boat(riva, 257.4, coastZ(262) - 10, Math.PI + .03, -.32, 1.6);
    // espigón de rocas con camino de hormigón y faro en la punta, pasada la meta
    { const x = -326, z0 = coastZ(x) + 2, z1 = coastZ(x) - 78, L = z0 - z1;
      const cam = new THREE.Mesh(new THREE.BoxGeometry(4.4, 4.6, L), M(0xa49d90, .95)); cam.position.set(x, -.9, (z0 + z1) / 2); cam.castShadow = cam.receiveShadow = true; add(cam);
      const top = new THREE.Mesh(new THREE.BoxGeometry(4.6, .2, L), M(0xd2ccc0, .9)); top.position.set(x, 1.45, (z0 + z1) / 2); top.receiveShadow = true; add(top);
      for (let k = 0; k * 2.6 < L + 6; k++) for (const s of [-1, 1]) for (const row of [0, 1]) { const r0 = roca.clone(), h = (k * 13 + row * 7 + (s > 0 ? 5 : 0)) % 9 / 9, sc = 1.05 + h * .55;
        r0.scale.set(sc, sc * (1.3 - row * .3), sc); r0.rotation.set((h - .5) * .5, k * 2.3 + s + row, (h - .5) * .4); r0.position.set(x + s * (2.9 + row * 2.4 + h * .6), row ? -.7 : .1 + h * .4, z0 - 1 - k * 2.6 + row * 1.3); add(r0); }
      for (let z = z0; z > z1 - 4; z -= 3) solid(x, z, 6.4);
      const pl = new THREE.Mesh(new THREE.CylinderGeometry(6.5, 7.2, 4.6, 32), M(0xa49d90, .95)); pl.position.set(x, -.7, z1 - 4); pl.castShadow = pl.receiveShadow = true; add(pl);
      const f = faro.clone(); f.position.set(x, 1.6, z1 - 4); f.rotation.y = 2.2; add(f); solid(x, z1 - 4, 7.6);
      // luz del faro que gira
      const bm = new THREE.Mesh(new THREE.ConeGeometry(2.5, 40, 16, 1, true), new THREE.MeshBasicMaterial({ color: 0xfff2c0, transparent: true, opacity: .1, depthWrite: false, side: THREE.DoubleSide }));
      bm.geometry.translate(0, -20, 0); bm.rotation.z = Math.PI / 2; const piv = new THREE.Group(); piv.position.set(x, 14.2, z1 - 4); piv.add(bm); add(piv); R.beam = piv;
      boat(pesca2, x + 9, coastZ(x) - 30, .1, -.5, 2); boat(barca, x + 8.4, coastZ(x) - 50, -.1, -.18, 1, 1.4); boat(pesca, x + 9.6, coastZ(x) - 66, Math.PI + .1, -.55, 2.2); }
    // barcos que entran y salen del puerto cruzando el recorrido (con choque y estela)
    R.movers = [[pesca, 182, 7, 2.2, .3, -.55], [riva, -118, 11, 1.6, .65, -.32], [pesca2, 40, 6, 2, .1, -.5]].map(([src, x, sp, r, u, y]) => {
      const o = src.clone(); o.position.y = y; add(o); const wk = new Wake(env); add(wk.mesh); wk.pts.length = 0;
      const cols = [-1, 0, 1].map(() => { const c = { x: 0, z: 0, r }; window.__COLZ.push(c); return c; });
      return { o, wk, cols, x, za: coastZ(x) - 9, zb: coastZ(x) - 105, sp, r, u, dir: 1, wait: 0, y, ry: 0 }; });
    // yate grande fondeado mar adentro
    boat(yate, 150, coastZ(150) - 92, .35, -1.3, 4.2, .4);
  }

  // ---------- BAR ROXY (LA CALA): tienda de piezas y gasolina, como en el 2D ----------
  function roxyBar() {
    const g0 = new THREE.Group(), x = 20, z = coastZ(x) + 14, y = heightAt(x, z);
    const M = c => new THREE.MeshStandardMaterial({ color: c, roughness: .75 }), box = (w, h, d, c, px, py, pz) => { const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), M(c)); m.position.set(px, py, pz); m.castShadow = m.receiveShadow = true; g0.add(m); return m; };
    box(12, 3.6, 7, 0xfdf0f4, 0, 1.8, 0); box(12.6, .35, 7.6, 0xff3f8e, 0, 3.75, 0);
    const sg = new THREE.Mesh(new THREE.PlaneGeometry(8, 1.4), new THREE.MeshStandardMaterial({ map: textTex(['ROXY BAR'], 1024, 180, '#ff3f8e', '#ffffff'), roughness: .5, emissive: 0x220011 })); sg.position.set(0, 2.9, -3.56); sg.rotation.y = Math.PI; g0.add(sg);
    box(11, 1.2, .15, 0x141416, 0, 1.4, -3.55);
    for (const tx of [-3.5, 0, 3.5]) { const um = new THREE.Mesh(new THREE.ConeGeometry(1.6, .8, 10, 1, true), new THREE.MeshStandardMaterial({ color: tx ? 0xffffff : 0xff3f8e, side: THREE.DoubleSide })); um.position.set(tx, 2.4, -5.8); g0.add(um); box(.08, 2.4, .08, 0xcccccc, tx, 1.2, -5.8); box(.9, .06, .9, 0xffffff, tx, .8, -5.8); }
    for (let k = 0; k < 8; k++) box(2.6, .2, 2, 0xa57a4c, 0, -.05 + Math.max(0, .35 - k * .1), -8 - k * 2);
    for (let k = 0; k < 8; k += 2) for (const s of [-1, 1]) box(.22, 2.2, .22, 0x6b4a2c, s * 1.3, -.7, -8 - k * 2);
    g0.position.set(x, y, z); add(g0); for (let k = 0; k < 8; k++) solid(x, z - 8 - k * 2, 1.5); R.roxyPos = { x: x + 4, z: z - 20 }; }

  // ---------- escenario de LA CALA: rocas a los lados de la entrada y barcas fondeadas ----------
  async function calaScene() {
    const [roca, barca, pesca2, riva, acan5, acan7] = await Promise.all(['namaqualand_boulder_02', 'barca', 'barco_pesca2', 'barco_riva', 'acantilado_n5', 'acantilado_n7'].map(glb));
    const boats = R.boats = [];
    const rock = (x, z, sc, ry, sy = .8) => { const r0 = roca.clone(); r0.scale.set(sc, sc * sy, sc); r0.rotation.set((ry % 1) * .4 - .2, ry * 3, (ry % .7) * .5 - .17); r0.position.set(x, -sc * .25, z); add(r0); solid(x, z, sc * 1.05); };
    // dos cabos de roca que cierran la cala, uno a cada lado, metiéndose en el agua
    for (const [src, xc, s, sy] of [[acan5, -258, 1.15, 1.7], [acan7, 250, 1.35, 1.9]]) { const a = src.clone(), zc = coastZ(xc) + 1, len = (src === acan5 ? 40 : 30) * s;
      a.scale.set(s, s * sy, s); a.rotation.y = Math.PI; a.position.set(xc, -1.2, zc); add(a);
      for (let t = -.5; t <= .5; t += .08) solid(xc + t * len, coastZ(xc + t * len) - 1, 5);
      for (let k = 0; k < 9; k++) { const h = (k * 37 % 11) / 11, x = xc + (h - .5) * len * .9; rock(x, coastZ(x) - 5 - (k % 3) * 1.8, 1.3 + h * 1.5, k * .41 + h); } }   // acantilados reales a los lados de la cala
    // rocas sueltas por la orilla
    for (let k = 0; k < 10; k++) { const x = -200 + k * 43 + (k % 2) * 9, z = coastZ(x) + 1.5 + (k % 3); rock(x, z, 1.2 + (k % 4) * .35, k * .53); }
    // pinos sobre las rocas de los lados de la cala
    { const pino = await glb('pino'); for (const [x, dz, s, r] of [[-236, 9, 1, .3], [-222, 14, .85, 2], [-248, 18, 1.1, 4], [226, 10, .95, 1], [238, 16, 1.05, 3.3], [214, 19, .8, 5]]) { const p = pino.clone(); const z = coastZ(x) + dz; p.position.set(x, heightAt(x, z) - .2, z); p.scale.setScalar(s); p.rotation.y = r; add(p); } }
    roxyBar();
    // barcas y llaüts fondeados, fuera del recorrido
    const anch = (src, x, dz, ry, y, k = 1) => { const b = src.clone(); const z = coastZ(x) - dz; b.position.set(x, y, z); b.rotation.y = ry; b.userData.bob = { y, ph: x * .3, k }; add(b); boats.push(b); const r = src === barca ? 1.1 : src === riva ? 1.6 : 2.1; for (let j = -1; j <= 1; j++) solid(x + Math.sin(ry) * j * r * 2.2, z + Math.cos(ry) * j * r * 2.2, r); };
    anch(barca, -150, 16, .6, -.18, 1.4); anch(barca, -40, 14, -.8, -.18, 1.4); anch(pesca2, 60, 78, 2.2, -.5); anch(barca, 130, 15, 1.9, -.18, 1.4); anch(riva, 200, 74, -1.1, -.32); anch(pesca2, -210, 80, .9, -.5);
  }

  // ---------- escenario de EL MAGO: la isla del faro en mitad del recorrido (se rodea por los dos lados) y barcos fondeados antes de la meta ----------
  async function magoScene() {
    const [isla, yate, pesca, pesca2, barca, riva] = await Promise.all(['isla_mago', 'yate', 'barco_pesca', 'barco_pesca2', 'barca', 'barco_riva'].map(glb));
    const path = R.path, sI = path.L * .5, q = at(path, sI), i0 = isla.clone(); i0.position.set(q.x, -5, q.z); i0.rotation.y = Math.atan2(q.tx, q.tz) + .4; add(i0);
    for (const [a, b, r] of [[0, 0, 11], [6, 0, 8], [-6, 0, 8], [0, 7, 7], [0, -7, 7]]) solid(q.x - q.tz * b + q.tx * a, q.z + q.tx * b + q.tz * a, r);
    // letrero EL MAGO en la isla, mirando a la salida
    const sg = new THREE.Mesh(new THREE.PlaneGeometry(9, 2.2), new THREE.MeshStandardMaterial({ map: textTex(['EL MAGO'], 1024, 256, '#0b1630', '#ffe14d'), roughness: .5, side: THREE.DoubleSide }));
    sg.position.set(q.x - q.tx * 17, 4.6, q.z - q.tz * 17); sg.rotation.y = Math.atan2(q.tx, q.tz) + Math.PI; add(sg);
    for (const s of [-1, 1]) { const p = new THREE.Mesh(new THREE.CylinderGeometry(.18, .18, 8, 8), new THREE.MeshStandardMaterial({ color: 0x6b4a2c })); p.position.set(sg.position.x - q.tz * s * 4.3, 1.2, sg.position.z + q.tx * s * 4); add(p); }
    // barcos fondeados antes de la meta, dejando el canal libre
    const boats = R.boats = [];
    // barco Piri-Piri: al pasar a su lado, +1 corazón y +2 turbos (una vez por carrera)
    { const p0 = at(path, path.L * .3), x = p0.x - p0.tz * -22, z = p0.z + p0.tx * -22, b = riva.clone(); b.position.set(x, -.32, z); b.rotation.y = Math.atan2(p0.tx, p0.tz); b.userData.bob = { y: -.32, ph: 1, k: 1 }; add(b); boats.push(b);
      const tag = new THREE.Sprite(new THREE.SpriteMaterial({ map: textTex(['PIRI-PIRI'], 512, 128, '#ff3f8e', '#ffffff'), transparent: true, depthWrite: false, sizeAttenuation: false })); tag.scale.set(.12, .03, 1); tag.position.set(0, 3.2, 0); b.add(tag);
      R.piri = { x, z, got: false }; for (let k = -1; k <= 1; k++) solid(x + p0.tx * k * 3.4, z + p0.tz * k * 3.4, 1.6); }
    // Casco Dorado escondido: detrás de la isla, por el lado de mar abierto
    { const q = at(path, path.L * .5), lt = -30 * (Math.sign(q.tx) || 1), x = q.x - q.tz * lt, z = q.z + q.tx * lt; const h = new THREE.Mesh(new THREE.SphereGeometry(.7, 20, 14, 0, Math.PI * 2, 0, Math.PI / 1.7), new THREE.MeshStandardMaterial({ color: 0xd9b55a, metalness: .9, roughness: .2, emissive: 0x5a4200, emissiveIntensity: .5 }));
      h.position.set(x, 1.3, z); add(h); R.gold = { o: h, got: S.own.includes('hgold') }; h.visible = !R.gold.got; }
    // letrero EL MAGO en la meta
    { const e = at(path, path.L - 4), m = new THREE.Mesh(new THREE.PlaneGeometry(10, 2.4), new THREE.MeshStandardMaterial({ map: textTex(['EL MAGO'], 1024, 256, '#0b1630', '#ffe14d'), roughness: .5, side: THREE.DoubleSide }));
      m.position.set(e.x - e.tz * 22, 5.2, e.z + e.tx * 22); m.rotation.y = Math.atan2(e.tx, e.tz) + Math.PI; add(m);
      for (const s of [-1, 1]) { const pl = new THREE.Mesh(new THREE.CylinderGeometry(.2, .2, 9, 8), new THREE.MeshStandardMaterial({ color: 0xffffff })); pl.position.set(m.position.x + e.tx * s * 4.6, 1.5, m.position.z + e.tz * s * 4.6); add(pl); solid(pl.position.x, pl.position.z, .6); } }
    [[yate, 150, 34, .4, -1.3, 4.2], [pesca, 118, -26, 1.2, -.55, 2.2], [barca, 96, 23, -.6, -.18, 1], [riva, 80, -24, 2.2, -.32, 1.6], [pesca2, 64, 27, -1.4, -.5, 2], [barca, 52, -22, .9, -.18, 1], [riva, 40, 25, -2.6, -.32, 1.6], [pesca, 170, -30, -.2, -.55, 2.2]].forEach(([src, back, lat, ry, y, r]) => {
      const p0 = at(path, path.L - back), x = p0.x - p0.tz * lat, z = p0.z + p0.tx * lat, b = src.clone(); b.position.set(x, y, z); b.rotation.y = ry; b.userData.bob = { y, ph: x * .3, k: src === yate ? .4 : 1 }; add(b); boats.push(b);
      const L = r * 2.2; for (let k = -1; k <= 1; k++) solid(x + Math.sin(ry) * k * L, z + Math.cos(ry) * k * L, r); });
  }

  // ---------- rampas de salto (la física del salto está en play.html) ----------
  const RAMPC = { amarilla: ['#ffb21a', 7, 1.4], naranja: ['#ff7a1a', 8, 2], roja: ['#e3202b', 9, 2.7], mega: ['#9b30ff', 12, 4] };
  function ramp(path, s, lat, kind = 'amarilla', w = 4.2) { const [rc, len, h] = RAMPC[kind];
    const q = at(path, s), x = q.x - q.tz * lat, z = q.z + q.tx * lat, th = Math.atan2(q.tx, q.tz), g = new THREE.Group();
    const geo = new THREE.BufferGeometry(), hw = w / 2;   // cuña: sube de 0 a h a lo largo de len
    const v = [-hw, 0, 0, hw, 0, 0, hw, h, len, -hw, h, len, -hw, 0, len, hw, 0, len];
    geo.setAttribute('position', new THREE.Float32BufferAttribute(v, 3)); geo.setIndex([0, 2, 1, 0, 3, 2, 0, 4, 3, 1, 2, 5, 3, 4, 5, 3, 5, 2]); geo.computeVertexNormals();
    const top = new THREE.Mesh(geo, new THREE.MeshStandardMaterial({ map: textTex([''], 256, 256, rc, rc), color: 0xffffff, roughness: .35, side: THREE.DoubleSide })); top.castShadow = top.receiveShadow = true; g.add(top);
    for (let k = 0; k < 4; k++) { const st = new THREE.Mesh(new THREE.BoxGeometry(w + .02, .05, .35), new THREE.MeshStandardMaterial({ color: 0x14161b })); const u = (k + .5) / 4; st.position.set(0, h * u + .03, len * u); st.rotation.x = -Math.atan2(h, len); g.add(st); }   // franjas negras
    for (const sx of [-1, 1]) { const fl = new THREE.Mesh(new THREE.CylinderGeometry(.42, .42, len + 1, 14), new THREE.MeshStandardMaterial({ color: 0xe3202b, roughness: .4 })); fl.rotation.x = Math.PI / 2; fl.position.set(sx * (hw + .35), .1, len / 2); g.add(fl); }   // flotadores
    g.position.set(x, -.05, z); g.rotation.y = th; add(g);
    window.__RAMPS.push({ x, z, th, len, h, w });
  }

  // ---------- rivales ----------
  const RIVC = ['#e3202b', '#1e5eff', '#7be35a', '#ffd21a', '#ff3f8e'], RIVN = ['Toni Marín', 'Carla Ruiz', 'El Tito', 'Sandra Vidal', 'Javi Rubio'];
  let rivPool = null;
  async function makeRivals(n) {
    if (!rivPool) { rivPool = []; for (let i = 0; i < 5; i++) { const sk = await ctx.loadSki('kawasaki'); const rd = await ctx.makeRider({ vest: RIVC[i], body: ['piloto_eric', 'piloto_carla', 'piloto_eric', 'piloto_claudia', 'piloto_eric'][i], skin: [1, 1, .7, .92, 1][i] });
        rd.position.set(0, 0.74, -0.75); rd.userData.barY = 0.13; sk.body.add(rd); const pp = PAINTS[[1, 3, 2, 9, 6][i]]; ctx.paintSki && ctx.paintSki(sk.root, pp.main, pp.acc); rd.userData.pose({ barY: .13, k: .6 }); const wk = new Wake(env);
        const tag = new THREE.Sprite(new THREE.SpriteMaterial({ map: textTex([RIVN[i].toUpperCase()], 512, 128, RIVC[i], '#ffffff'), transparent: true, depthWrite: false, sizeAttenuation: false })); tag.scale.set(.11, .0275, 1); tag.position.set(0, 3.3, 0); tag.renderOrder = 5; sk.root.add(tag);   // nombre encima
        rivPool.push({ sk, rd, wk, name: RIVN[i] }); } }
    return rivPool.slice(0, n).map((o, i) => ({ ...o, s: 0, lane: 0, laneT: 0, v: 0, vmax: (30.2 + i * .85 + Math.random() * 1.2) * [.84, .9, 1, 1.07, 1.13][S.set.dif], fin: null, tl: 0, steer: 0 }));
  }

  // ---------- carrera ----------
  let freeMode = false, ghostSki = null, champ = null;
  async function startRace(i) {
    state = 'loading'; show(null); flash('CARGANDO…', 99, true);
    clearZone(); const Z = ZONES[i]; const path = buildPath(Z);
    R = { Z, path, t: 0, pen: 0, time: 0, cps: [], gates: [], rivals: [], hint: 0, s: 0, lat: 0, done: false, count: 3.6, lastCount: 4, maxS: 0, finished: [] };
    // salida y meta
    arch('META', path, path.L - 4, 16, true); arch('SALIDA', path, 22, 16, false);
    window.__RAMPS = []; ctx.setTime && ctx.setTime(Z.id === 'puerto' ? 'manana' : 'mediodia');
    if (Z.id === 'puerto') await puertoScene();
    if (Z.id === 'cala') await calaScene();
    if (Z.id === 'mago') await magoScene();
    if (Z.id === 'mago') jjBar();   // la salida de EL MAGO es desde el muelle del JJ'S
    if (Z.obj === 'time') { jjBar(); R.time = [16, 14, 11, 10, 9][S.set.dif]; R.cps = [path.L / 3, path.L * 2 / 3].map(s => ({ s, hit: false, add: [9, 8, 7, 6, 5.5][S.set.dif] }));   // ajustado: unos 25 s en total en normal
      for (const c of R.cps) arch('CHECKPOINT', path, c.s, 18, false);
      for (let s = 40; s < path.L - 20; s += 55) for (const sg of [-1, 1]) { const b = makeBuoy(sg > 0 ? '#ff7a1a' : '#ffffff'); place(b, path, s, sg * 20, .05); add(b); solid(b.position.x, b.position.z, .5); } }
    if (Z.obj === 'slalom') { let k = 0; for (let s = 60; s < path.L - 30; s += 46, k++) { const c = (k % 2 ? 1 : -1) * 5.5, gt = { s, c, done: false, b: [] }; R.gates.push(gt);
        for (const sg of [-1, 1]) { const b = makeBuoy(sg > 0 ? '#ff7a1a' : '#ffd21a'); b.scale.setScalar(1.6); place(b, path, s, c + sg * 4.5, .2); add(b); gt.b.push(b); solid(b.position.x, b.position.z, .75); } } }
    { const cg = new THREE.CylinderGeometry(.6, .6, .12, 28), cm = new THREE.MeshStandardMaterial({ color: 0xffc21a, metalness: .85, roughness: .22, emissive: 0x5a3a00, emissiveIntensity: .6 }); cg.rotateX(Math.PI / 2);
      R.coins = []; R.coinN = 0; let k = 0;
      for (let s = 50; s < R.path.L - 30; s += 64, k++) { const lat0 = [-9, 0, 9, -5, 5][k % 5], ln = Z.obj === 'slalom' ? (R.gates.find(q => Math.abs(q.s - s - 10) < 23)?.c ?? lat0) : lat0;
        for (let j = 0; j < 5; j++) { const c = new THREE.Mesh(cg, cm); c.castShadow = true; place(c, R.path, s + j * 4, ln); c.position.y = 1;
          if (window.__COLZ.some(o => Math.hypot(o.x - c.position.x, o.z - c.position.z) < o.r + 1.5)) continue; add(c); R.coins.push({ m: c, got: false }); } } }
    if (Z.obj === 'slalom') {   // flecha que marca la siguiente puerta de boyas
      const ar = new THREE.Group(), am = new THREE.MeshStandardMaterial({ color: 0x2bd94f, emissive: 0x2bd94f, emissiveIntensity: .6, roughness: .4 });
      const cone = new THREE.Mesh(new THREE.ConeGeometry(1.1, 2, 4), am); cone.rotation.x = Math.PI; ar.add(cone);
      const st = new THREE.Mesh(new THREE.BoxGeometry(.7, 1.6, .7), am); st.position.y = 1.7; ar.add(st); ar.traverse(o => o.castShadow = true); add(ar); R.gArrow = ar; }
    // rampas en cada pantalla, fuera de las puertas de boyas
    for (const [f, lat, k] of { puerto: [[.42, 7, 'amarilla'], [.78, -6, 'roja']], cala: [[.93, 0, 'naranja']], mago: [[.3, -8, 'naranja'], [.72, 8, 'mega']] }[Z.id] || []) { let s = path.L * f; while (R.gates.some(q => Math.abs(q.s - s) < 16)) s += 6; ramp(path, s, lat, k); }
    // recogibles como en el 2D: corazón, garrafa de gasolina, refresco turbo y una caja de equipo escondida
    { R.picks = []; const M = c => new THREE.MeshStandardMaterial({ color: c, roughness: .4, emissive: c, emissiveIntensity: .15 });
      const mkHeart = () => { const s = new THREE.Shape(); s.moveTo(0, -.6); s.bezierCurveTo(-.9, 0, -.6, .7, 0, .35); s.bezierCurveTo(.6, .7, .9, 0, 0, -.6); const m = new THREE.Mesh(new THREE.ExtrudeGeometry(s, { depth: .25, bevelEnabled: true, bevelSize: .06, bevelThickness: .06 }), M(0xff2b3a)); m.geometry.center(); return m; };
      const mkCan = () => { const gg = new THREE.Group(); const b = new THREE.Mesh(new THREE.BoxGeometry(.8, 1, .45), M(0xd8231c)); gg.add(b); const h = new THREE.Mesh(new THREE.TorusGeometry(.18, .05, 6, 12, Math.PI), M(0x222222)); h.position.y = .55; gg.add(h); return gg; };
      const mkDrink = () => { const gg = new THREE.Group(); const c = new THREE.Mesh(new THREE.CylinderGeometry(.28, .28, .8, 16), M(0x33d6ff)); gg.add(c); const t = new THREE.Mesh(new THREE.CylinderGeometry(.27, .27, .05, 16), M(0xcfd6dd)); t.position.y = .42; gg.add(t); return gg; };
      const mkBox = () => { const b = new THREE.Mesh(new THREE.BoxGeometry(1, 1, 1), new THREE.MeshStandardMaterial({ map: textTex(['?'], 128, 128, '#8a5530', '#ffe14d'), roughness: .8 })); return b; };
      const kinds = [['heart', mkHeart, .35, 0], ['fuel', mkCan, .55, 5], ['drink', mkDrink, .7, -5], ['box', mkBox, .85, 30]];
      for (const [k, mk, f, lat] of kinds) { const o = mk(); o.traverse(m => m.castShadow = true); place(o, R.path, R.path.L * f + (k === 'box' ? 0 : 23), lat); o.position.y = 1.2; o.scale.setScalar(1.3); add(o); R.picks.push({ k, o, got: false }); } }
    // penalizaciones como en el 2D: zona de baño con policía y multa, medusas, red de pesca y posidonia
    { const path = R.path, q0 = at(path, path.L * .8), sh = Math.sign(q0.tx) || 1; R.shore = sh; R.bano = { s0: path.L * .74, s1: path.L * .86, lat: 13 * sh };
      for (let s = R.bano.s0; s <= R.bano.s1; s += 9) { const b = makeBuoy('#ffe14d'); b.scale.setScalar(.8); place(b, path, s, R.bano.lat, .05); add(b); }
      const pol = (await glb('barco_riva')).clone(); pol.traverse(m => { if (m.isMesh) { m.material = m.material.clone(); m.material.color.lerp(new THREE.Color(0x1e5eff), .6); } }); pol.visible = false; add(pol);
      const tag = new THREE.Sprite(new THREE.SpriteMaterial({ map: textTex(['POLICÍA'], 512, 128, '#1e5eff', '#ffffff'), transparent: true, depthWrite: false, sizeAttenuation: false })); tag.scale.set(.1, .025, 1); tag.position.y = 3; pol.add(tag);
      const lamp = new THREE.PointLight(0x3a6bff, 0, 18); lamp.position.y = 2.4; pol.add(lamp); R.pol = { o: pol, lamp, on: false, t: 0 };
      const jm = new THREE.MeshPhysicalMaterial({ color: 0xff7ad9, transparent: true, opacity: .55, roughness: .2, emissive: 0xff4fc8, emissiveIntensity: .3 });
      R.haz = [];
      for (const [f, lat] of [[.22, -6], [.47, 7], [.82, -4]]) { const j = new THREE.Mesh(new THREE.SphereGeometry(.7, 16, 10, 0, Math.PI * 2, 0, Math.PI / 2), jm); place(j, path, path.L * f, lat, .02); add(j); R.haz.push({ k: 'medusa', o: j, r: 1.6 }); }
      { const net = new THREE.Group(), fl = new THREE.MeshStandardMaterial({ color: 0xff7a1a }); for (let i = 0; i < 14; i++) { const b = new THREE.Mesh(new THREE.SphereGeometry(.18, 8, 6), fl); b.position.set((i % 7 - 3) * 1.4, .05, (i < 7 ? -1 : 1) * 3); net.add(b); }
        const mesh = new THREE.Mesh(new THREE.PlaneGeometry(9, 6), new THREE.MeshBasicMaterial({ color: 0x2a2a2a, transparent: true, opacity: .25, depthWrite: false })); mesh.rotation.x = -Math.PI / 2; mesh.position.y = .03; net.add(mesh);
        place(net, path, path.L * .38, -10 * sh, 0); add(net); R.haz.push({ k: 'red', o: net, r: 4.5 }); }
      { const pos = new THREE.Mesh(new THREE.CircleGeometry(6, 24), new THREE.MeshBasicMaterial({ color: 0x1f4a2a, transparent: true, opacity: .5, depthWrite: false })); pos.rotation.x = -Math.PI / 2; place(pos, path, path.L * .7, 9 * sh, -.25); add(pos); R.haz.push({ k: 'posidonia', o: pos, r: 6 });
        const cor = new THREE.Mesh(new THREE.CircleGeometry(4, 20), new THREE.MeshBasicMaterial({ color: 0xff6f61, transparent: true, opacity: .45, depthWrite: false })); cor.rotation.x = -Math.PI / 2; place(cor, path, path.L * .12, -9 * sh, -.25); add(cor); R.haz.push({ k: 'coral', o: cor, r: 4 }); } }
    // tráfico que se mueve en las tres pantallas: yate de paseo con chicas que saludan y regalan un refresco, y una motora en sentido contrario
    { const [yt, rv, g1, g2] = await Promise.all(['yate', 'barco_riva', 'gente_tropical_confidence', 'gente_tropical_leaf_bikini'].map(glb)); const sh = R.shore || 1;
      const y = yt.clone(); add(y); for (const [gm, dx] of [[g1, -.8], [g2, .9]]) { const p = gm.clone(); p.scale.setScalar(.95); p.position.set(dx, 3.3, -3); p.rotation.y = dx > 0 ? 1.2 : -1.2; y.add(p); }
      const wy = new Wake(env); add(wy.mesh); wy.pts.length = 0; const m = rv.clone(); add(m); const wm = new Wake(env); add(wm.mesh); wm.pts.length = 0;
      R.traffic = [{ o: y, wk: wy, s: R.path.L * .15, lat: -34 * sh, v: 7, dir: 1, y: -1.3, girls: true, gave: false, cols: [] }, { o: m, wk: wm, s: R.path.L * .95, lat: -30 * sh, v: 12, dir: -1, y: -.32, cols: [] }];
      for (const t of R.traffic) for (let k = 0; k < 3; k++) { const c = { x: 0, z: 0, r: t.girls ? 4 : 1.7 }; window.__COLZ.push(c); t.cols.push(c); } }
    R.free = freeMode; R.rec = []; R.recT = 0;
    if (freeMode) { if (!ghostSki) { ghostSki = await ctx.loadSki('kawasaki'); ghostSki.root.traverse(o => { if (o.isMesh) { o.material = o.material.clone(); o.material.transparent = true; o.material.opacity = .38; o.material.depthWrite = false; o.castShadow = false; } }); }
      const gh = S.ghost && S.ghost[Z.id]; R.ghost = gh || null; ghostSki.root.visible = !!gh; if (gh) scene.add(ghostSki.root); }
    // vida en el mar: delfines que saltan (+1 turbo si los sigues), tortugas (no las pises), un velero y un kayak
    { const [dg, tg, vel, kay] = await Promise.all([glbAnim('delfin'), glbAnim('tortuga'), glb('velero'), glb('kayak')]); const sh = R.shore || 1; R.mixers = []; R.fauna = [];
      const anim = (gl, sc) => { const o = SkeletonUtils.clone(gl.scene); o.scale.setScalar(sc); o.traverse(m => { if (m.isMesh) { m.castShadow = true; m.frustumCulled = false; } }); const mx = new THREE.AnimationMixer(o); if (gl.animations[0]) mx.clipAction(gl.animations[0]).play(); R.mixers.push(mx); return o; };
      for (let k = 0; k < 3; k++) { const d = anim(dg, .0026); add(d); R.fauna.push({ k: 'delfin', o: d, s: R.path.L * .3 + k * 5, lat: -24 * sh - k * 3, v: 30, ph: k * 1.1 }); }
      const tm = new THREE.MeshStandardMaterial({ color: 0x5d6b3a, roughness: .7 });
      for (let k = 0; k < 2; k++) { const t = anim(tg, 1.3); t.traverse(m => { if (m.isMesh) m.material = tm; }); add(t); R.fauna.push({ k: 'tortuga', o: t, s: R.path.L * (.55 + k * .25), lat: (k ? 9 : -9) * sh, v: 1.2, ph: k }); }
      const v = vel.clone(); add(v); const kk = kay.clone(); add(kk); const wv = new Wake(env); add(wv.mesh); wv.pts.length = 0; const wk2 = new Wake(env); add(wk2.mesh); wk2.pts.length = 0;
      R.traffic = (R.traffic || []).concat([{ o: v, wk: wv, s: R.path.L * .6, lat: -75 * sh, v: 3, dir: -1, y: -2.1, cols: [{ x: 0, z: 0, r: 3 }, { x: 0, z: 0, r: 3 }, { x: 0, z: 0, r: 3 }] },
        { o: kk, wk: wk2, s: R.path.L * .45, lat: 16 * sh, v: 1.6, dir: 1, y: -.1, cols: [{ x: 0, z: 0, r: .9 }, { x: 0, z: 0, r: .9 }, { x: 0, z: 0, r: .9 }] }]);
      for (const t of R.traffic.slice(-2)) for (const c of t.cols) window.__COLZ.push(c); }
    if (Z.riv && !freeMode) { R.rivals = await makeRivals(Z.riv); R.rivals.forEach((r, k) => { r.s = 12 - Math.floor((k + 1) / 2) * 7 - ((k + 1) % 2) * 3.5; r.lane = r.laneT = (k % 2 ? 1 : -1) * (4 + Math.floor(k / 2) * 4); scene.add(r.sk.root); scene.add(r.wk.mesh); added.push(r.sk.root, r.wk.mesh); r.wk.pts.length = 0; r.wk.lx = null; r.wk.geo.setDrawRange(0, 0); }); }
    // jugador a la salida
    rh.querySelector('.co span').textContent = '0';
    if (S.fuel < 60) S.fuel = 60;   // cada salida con al menos 60 % de gasolina; en el JJ'S se llena al 100 % window.__noFuel = S.fuel <= 0; hud();
    window.__celebT = null; const q = at(path, 14); P.x = q.x; P.z = q.z; P.th = Math.atan2(q.tx, q.tz); P.v = 0; P.slip = 0; P.steer = 0; P.energy = 1; P.turboU = 2; P.boostT = 0; P._bovT = 0; P.y = 0; P.vy = 0; P.air = false; P.dc = 0; ctx.resetFx && ctx.resetFx();
    rh.querySelector('.z').textContent = 'ZONA ' + (i + 1) + ' · ' + Z.name; rh.style.display = 'block';
    msg.style.display = 'none'; ctx.setPaused(false); state = 'count'; keepAwake(true);
  }
  function finishRace(ok, title) {
    if (R.done) return; R.done = true; state = 'result'; keepAwake(false);
    if (R.free && ok) { S.ghost = S.ghost || {}; const old = S.ghost[R.Z.id]; if (!old || R.t < old.t) { S.ghost[R.Z.id] = { t: R.t, p: R.rec }; title = '¡NUEVO FANTASMA!'; } } if (Snd.sirenStop) Snd.sirenStop(); rh.style.display = 'none'; const Z = R.Z;
    let prize = 0, line = '', t = R.t + R.pen;
    const coinTxt = R.coinN ? ' · ' + R.coinN + ' monedas: +' + (R.coinN * 25).toLocaleString('es-ES') + ' PTA' : '';
    if (Z.obj === 'time') { const pp = ok && Z.posPrize && R.pos <= 3 ? Z.posPrize[R.pos - 1] : 0; line = (ok ? 'Tiempo: ' + fmtT(R.t) + (R.rivals.length ? ' · ' + R.pos + 'º de ' + (R.rivals.length + 1) + (pp ? ' (+' + pp.toLocaleString('es-ES') + ' PTA por puesto)' : '') : '') : 'Te has quedado a ' + Math.max(0, Math.round(R.path.L - R.s)) + ' m de la meta'); if (ok) prize = Z.prize + pp; }
    if (Z.obj === 'slalom') { const miss = R.gates.filter(g => g.miss).length; line = 'Tiempo ' + fmtT(R.t) + ' + ' + miss + ' s de boyas = ' + fmtT(t); if (ok) prize = Math.max(300, Z.prize - miss * 100);
      if (ok && !miss) { prize += 500; S.perfect = 1; line += ' · ¡SLALOM PERFECTO! +500 PTA'; } }
    if (Z.obj === 'race3') { const pos = R.pos; line = 'Has quedado ' + pos + 'º de ' + (R.rivals.length + 1) + ' · ' + fmtT(R.t); ok = ok && pos <= 3; if (ok) prize = Z.prize[pos - 1]; title = ok ? (pos === 1 ? '¡HAS GANADO!' : '¡PODIO!') : 'FUERA DEL PODIO'; }
    // bonus de tiempo como en el 2D: en EL PUERTO 50 PTA por segundo sobrante; en LA CALA 30 PTA por segundo por debajo de 30 s
    if (R.free) prize = 0;   // la carrera libre no da premio
    const tBonus = !ok || R.free ? 0 : Z.obj === 'time' ? Math.round(R.time) * 50 : Z.obj === 'slalom' ? Math.max(0, Math.round((30 - t) * 30)) : 0, base = prize; prize += tBonus;
    const unl = ok && zone + 1 < ZONES.length && !S.done[ZONES[zone + 1].id] && !S.done[Z.id] ? ZONES[zone + 1].name : '';
    if (ok && !R.free) { award('win1'); if (Z.id === 'mago' && R.pos === 1) award('oroM'); if (Z.obj === 'slalom' && !R.gates.some(q => q.miss)) award('perf'); if (!R.crashed) award('clean'); }
    if (ok) { window.__celebT = P.t; S.cash += prize; S.done[Z.id] = 1; S.unlocked = Math.max(S.unlocked, Math.min(ZONES.length, zone + 2)); if (Snd.ok()) Snd.win(); } else if (Snd.ok()) Snd.fail();
    // medalla y récord
    let md = -1; if (ok) { if (Z.obj === 'race3') md = R.pos - 1; else { const k = [1.2, 1.12, 1, .92, .86][S.set.dif]; md = MEDAL_T[Z.id].findIndex(v => t <= v * k); } }
    const rec = ok && (S.best[Z.id] == null || t < S.best[Z.id]) && Z.obj !== 'race3'; if (rec) S.best[Z.id] = t;
    if (md >= 0 && (S.medal[Z.id] == null || md < S.medal[Z.id])) S.medal[Z.id] = md;
    if (md === 0 && Z.id === 'puerto') award('oroP'); if (md === 0 && Z.id === 'cala') award('oroC');
    const mdE = scr.result.querySelector('.md'); mdE.style.display = md >= 0 || rec ? 'block' : 'none';
    mdE.innerHTML = (md >= 0 ? `<i class="ti ti-medal" style="font-size:64px;color:${MEDAL_C[md]};filter:drop-shadow(0 4px 0 #0b1630)"></i><div style="color:${MEDAL_C[md]}">MEDALLA DE ${MEDAL_N[md]}</div>` : '') + (rec ? '<div style="color:#5be37a">¡NUEVO RÉCORD!</div>' : '');
    // desglose como en el 2D
    { const rows = [['Monedas', R.coinN + ' × 25', R.coinN * 25]];
      if (Z.obj === 'race3') rows.push(['Puesto', R.pos + 'º', null]); else rows.push(['Tiempo', fmtT(R.t), null]);
      if (Z.obj === 'time') rows.push(['Tiempo sobrante', ok ? fmtT(R.time) : '—', tBonus]);
      if (Z.obj === 'slalom') { const miss = R.gates.filter(g => g.miss).length; rows.push(['Boyas', (R.gates.length - miss) + ' de ' + R.gates.length, null], ['Bonus de tiempo', '', tBonus]); }
      rows.push(['Saltos', String(R.jumps || 0), null], ['Trucos', String(R.tricks || 0), null], ['Derrapes', String(R.drifts || 0), null], ['Premio', '', base]);
      const pts = R.coinN * 25 + prize + (R.pts || 0); R.points = pts; rows.push(['PUNTOS', String(pts), null]); if (unl) rows.push(['Desbloqueado', unl, null]);
      scr.result.querySelector('.desg').innerHTML = rows.map(([a, b, c]) => `<tr><td style="text-align:left">${a}</td><td>${b}</td><td style="text-align:right;color:#ffe14d">${c == null ? '' : '+' + c.toLocaleString('es-ES') + ' PTA'}</td></tr>`).join(''); }
    // podio de EL MAGO: los que han llegado por tiempo y el resto por lo que les falta
    const pod = scr.result.querySelector('.podio'); pod.style.display = 'none';
    if (Z.obj === 'race3') { const all = [{ n: S.name || 'TÚ', me: 1, f: R.pfin ?? null, s: R.s }].concat(R.rivals.map(r => ({ n: r.name, f: r.fin, s: r.s })));
      const key = o => o.f != null ? o.f : 1e4 - o.s; all.sort((a, b) => key(a) - key(b));
      const top = all.slice(0, 3); pod.innerHTML = [1, 0, 2].map(k => top[k] ? `<div class="${top[k].me ? 'me' : ''}"><span>${top[k].n}</span><b style="height:${[96, 70, 52][k]}px;background:${MEDAL_C[k]}">${k + 1}</b></div>` : '').join(''); pod.style.display = 'flex'; }
    save();
    scr.result.querySelector('.rt').textContent = title; scr.result.querySelector('.rs').textContent = line + coinTxt;
    scr.result.querySelector('.rp').textContent = ok ? '+' + prize.toLocaleString('es-ES') + ' PTA' : '';
    const nx = scr.result.querySelector('.nx'); nx.disabled = !(zone + 1 < ZONES.length && zone + 1 < S.unlocked);
    // campeonato: suma puntos; si fallas una carrera se acaba; tras La Final, copa de la dificultad elegida
    if (champ) {
      if (!ok) { scr.result.querySelector('.rs').textContent = line + ' · CAMPEONATO TERMINADO'; champ = null; nx.innerHTML = 'SIGUIENTE PANTALLA'; }
      else { champ.pts += R.points || 0;
        if (zone + 1 < ZONES.length) { nx.disabled = false; nx.innerHTML = '<i class="ti ti-player-play-filled"></i>SIGUIENTE CARRERA'; }
        else { const cup = CUPS[S.set.dif], first = !S.cups[S.set.dif]; S.cups[S.set.dif] = Math.max(S.cups[S.set.dif] || 0, champ.pts); if (first) S.cash += 2000; save();
          scr.result.querySelector('.rt').textContent = '¡' + cup + ' GANADA!'; title = '¡' + cup + ' GANADA!'; scr.result.querySelector('.rp').textContent = 'TOTAL CAMPEONATO: ' + champ.pts.toLocaleString('es-ES') + ' PUNTOS' + (first ? ' · +2000 PTA' : '');
          champ = null; nx.innerHTML = 'SIGUIENTE PANTALLA'; } } }
    const list = S.top[Z.id] || []; const qual = ok && (list.length < 10 || t < list[list.length - 1].t);
    R.final = t; R.qual = qual; scr.result.querySelector('.nm').style.display = qual ? 'block' : 'none';
    const inp = scr.result.querySelector('input'); inp.value = S.name || 'JUGADOR';
    renderTop(); show('result'); if (qual) setTimeout(() => inp.focus(), 60);
  }
  function renderTop(me) { const list = S.top[R.Z.id] || []; scr.result.querySelector('.tt').innerHTML = list.length ? list.map((e, k) => `<tr class="${k === me ? 'me' : ''}"><td>${k + 1}.</td><td>${e.n}</td><td>${fmtT(e.t)}</td><td style="color:#ffe14d">${e.p != null ? e.p.toLocaleString('es-ES') + ' pts' : ''}</td><td style="opacity:.7">${e.m || ''}</td><td style="opacity:.7">${e.c || ''}</td></tr>`).join('') : '<tr><td>Aún no hay tiempos</td></tr>'; }
  function saveName() { if (!R || !R.qual) return; const n = (scr.result.querySelector('input').value || 'JUGADOR').toUpperCase().slice(0, 12); S.name = n;
    const list = S.top[R.Z.id] || (S.top[R.Z.id] = []); list.push({ n, t: R.final, p: R.points || 0, m: 'Kawasaki Ultra 310', c: CUPS[S.set.dif].replace('COPA ', '') }); list.sort((a, b) => a.t - b.t); list.length = Math.min(10, list.length);
    const me = list.findIndex(e => e.n === n && e.t === R.final); save(); R.qual = false; scr.result.querySelector('.nm').style.display = 'none'; renderTop(me); scr.result.querySelector('.btn.main').focus(); }

  // ---------- acciones de botones ----------
  ui.addEventListener('click', async e => { const b = e.target.closest('[data-a]'); if (!b) return; const a = b.dataset.a; click();
    if (a === 'menu') { if (R) { clearZone(); R = null; rh.style.display = 'none'; ctx.setPaused(false); } state = 'menu'; refreshCash(); show('menu'); }
    if (a === 'map') { clearZone(); R = null; rh.style.display = 'none'; ctx.setPaused(false); state = 'map'; renderMap(); show('map'); }
    if (a === 'pilot') { state = 'pilot'; renderPilot(); show('pilot'); }
    if (a === 'taller') { state = 'taller'; renderTaller(); show('taller'); }
    if (a === 'set') { state = 'set'; renderSet(); show('set'); }
    if (a === 'ach') { state = 'ach'; renderAch(); show('ach'); }
    if (a === 'rank') { state = 'rank'; renderRank(); show('rank'); }
    if (a === 'ctrl') { state = 'ctrl'; show('ctrl'); }
    if (a === 'cred') { state = 'cred'; show('cred'); }
    if (a === 'tsnd') { S.set.snd = S.set.snd ? 0 : 1; save(); applySettings(); }
    if (a === 'tmus') { S.set.mus = S.set.mus ? 0 : 1; save(); applySettings(); }
    if (a === 'wipe') { if (b.dataset.sure) { try { localStorage.removeItem(SAVE_KEY); } catch (e) {} location.reload(); } else { b.dataset.sure = 1; b.textContent = '¿SEGURO? PULSA OTRA VEZ'; } }
    if (a === 'go') { freeMode = false; champ = null; await startRace(zone); }
    if (a === 'champ') { freeMode = false; champ = { pts: 0 }; zone = 0; toast(CUPS[S.set.dif] + ': EL PUERTO, LA CALA Y LA FINAL EN EL MAGO', true); await startRace(0); }
    if (a === 'free') { freeMode = true; champ = null; await startRace(zone); }
    if (a === 'retry') await startRace(zone);
    if (a === 'next') { if (champ && zone + 1 < ZONES.length) { zone++; await startRace(zone); } else if (zone + 1 < S.unlocked) openBrief(zone + 1); }
    if (a === 'resume') { ctx.setPaused(false); state = R && R.started ? 'race' : 'count'; show(null); }
    if (a === 'jjout') { ctx.setPaused(false); state = 'race'; show(null); flash('-3 s', 1, true); }
    if (a === 'exp') { const code = btoa(unescape(encodeURIComponent(JSON.stringify(S)))); try { await navigator.clipboard.writeText(code); toast('CÓDIGO COPIADO: PÉGALO EN EL OTRO APARATO', true); } catch (e) { const im = scr.set.querySelector('[data-imp]'); im.value = code; im.select(); toast('CÓDIGO LISTO: CÓPIALO', true); } }
    if (a === 'fs') { try { document.fullscreenElement ? await document.exitFullscreen() : await document.documentElement.requestFullscreen({ navigationUI: 'hide' }); screen.orientation && screen.orientation.lock && screen.orientation.lock('landscape').catch(() => {}); } catch (e) {} }
    if (a === 'savename') saveName(); });
  scr.result.querySelector('input').addEventListener('keydown', e => { e.stopPropagation(); if (e.key === 'Enter') saveName(); });

  // ---------- navegación de menús con teclado y mando ----------
  const focusables = () => [...ui.querySelectorAll('.scr.on .btn:not([disabled]), .scr.on .card:not(.lock), .scr.on input')].filter(e => e.offsetParent !== null);
  function nav(d) { const f = focusables(); if (!f.length) return; let i = f.indexOf(document.activeElement); i = i < 0 ? 0 : (i + d + f.length) % f.length; f[i].focus(); }
  function back() { if (state === 'pause') { ctx.setPaused(false); state = R && R.started ? 'race' : 'count'; show(null); return; }
    if (state === 'jj') { scr[scr.roxy.classList.contains('on') ? 'roxy' : 'jj'].querySelector('[data-a=jjout]').click(); return; }
    if (['map', 'pilot', 'taller', 'set', 'ctrl', 'cred', 'ach', 'rank'].includes(state)) { state = 'menu'; show('menu'); } else if (state === 'brief') { state = 'map'; renderMap(); show('map'); } }
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
    if (!R || state === 'pause' || state === 'loading' || R.done) return;   // mientras carga la pantalla no corre el tiempo
    if (R.boats) for (const b of R.boats) { const u = b.userData.bob, t = P.t + u.ph; b.position.y = u.y + Math.sin(t * 1.1) * .06 * u.k + (window.__swell ? window.__swell(b.position.x, b.position.z) * (u.k > .5 ? .8 : .4) : 0); b.rotation.z = Math.sin(t * .9) * .025 * u.k; b.rotation.x = Math.sin(t * .7 + 1) * .015 * u.k; }
    if (R.beam) R.beam.rotation.y += dt * 1.1;
    if (R.piri && !R.piri.got && state === 'race' && Math.hypot(P.x - R.piri.x, P.z - R.piri.z) < 8) { R.piri.got = true; award('piri'); S.lives = Math.min(6, S.lives + 1); P.turboU = Math.min(5, (P.turboU ?? 3) + 2); save(); hud(); flash('¡PIRI-PIRI! +1 ♥ +2 TURBOS', 1.4, true, '#ff3f8e'); if (Snd.ok()) Snd.pickup(); }
    if (state === 'race' && !window.__autoQ && S.set.q === 'alta') { R.fpsT = (R.fpsT || 0) + dt; R.fpsN = (R.fpsN || 0) + 1;   // calidad automática: si va lento, baja los gráficos
      if (R.fpsT > 5) { window.__autoQ = 1; if (R.fpsN / R.fpsT < 38) { S.set.q = 'baja'; save(); applySettings(); toast('GRÁFICOS EN BAJA PARA IR MÁS FLUIDO', true); } } }
    if (R.gArrow) { const ng = R.gates.find(q => !q.done); R.gArrow.visible = !!ng; if (ng) { const q = at(R.path, ng.s); R.gArrow.position.set(q.x - q.tz * ng.c, 4.6 + Math.sin(P.t * 4) * .35, q.z + q.tx * ng.c); R.gArrow.rotation.y += dt * 2; } }
    if (R.gold && !R.gold.got) { R.gold.o.rotation.y += dt * 2; if (state === 'race' && Math.hypot(R.gold.o.position.x - P.x, R.gold.o.position.z - P.z) < 2.6) { R.gold.got = true; R.gold.o.visible = false; S.own.push('hgold'); save(); flash('¡HAS ENCONTRADO EL CASCO DORADO!', 2, true, '#d9b55a'); if (Snd.ok()) Snd.win(); } }
    if (R.picks) for (const pk of R.picks) { if (pk.got) continue; pk.o.rotation.y += dt * 2; pk.o.position.y = 1.2 + Math.sin(P.t * 2.5 + pk.o.position.x) * .2;
      if (state === 'race' && Math.hypot(pk.o.position.x - P.x, pk.o.position.z - P.z) < 2.6) { pk.got = true; pk.o.visible = false; if (Snd.ok()) Snd.pickup();
        if (pk.k === 'heart') { S.lives = Math.min(6, S.lives + 1); pop('+1 ♥', '#ff3b4e'); }
        if (pk.k === 'fuel') { S.fuel = Math.min(100, S.fuel + 40); pop('+40 % GASOLINA', '#ffb02e'); }
        if (pk.k === 'drink') { P.turboU = Math.min(5, (P.turboU ?? 3) + 1); pop('+1 TURBO', '#33d6ff'); }
        if (pk.k === 'box') { const all = Object.values(GEAR).flat().filter(it => !it.hidden && !S.own.includes(it.id)); if (all.length) { const it = all[Math.floor(Math.random() * all.length)]; S.own.push(it.id); flash('¡CAJA SORPRESA! ' + it.n.toUpperCase(), 1.6, true, '#ffe14d'); } else { S.cash += 500; pop('+500 PTA', '#ffe14d'); } }
        save(); hud(); } }
    if (R.haz && state === 'race') for (const h of R.haz) { const d = Math.hypot(h.o.position.x - P.x, h.o.position.z - P.z);
      if (d < h.r && !(h.t > R.t)) { h.t = R.t + 2.5;
        if (h.k === 'medusa') { P.v *= .5; loseLife(1 / 3, '¡MEDUSA! −⅓ ♥'); }
        if (h.k === 'red') { P.v *= .35; flash('¡RED DE PESCA!', 1, true, '#ff8c1e'); if (Snd.ok()) Snd.bump(); }
        if (h.k === 'posidonia') { P.v *= .6; flash('POSIDONIA: ¡NO LA PISES!', 1, true, '#5be37a'); }
        if (h.k === 'coral') { P.v *= .5; S.cash = Math.max(0, S.cash - 200); save(); flash('¡CORAL! MULTA −200 PTA', 1.2, true, '#ff6f61'); if (Snd.ok()) Snd.fine(); } } }
    if (R.pol && state === 'race') { const pl = R.pol, inB = R.s > R.bano.s0 && R.s < R.bano.s1 && R.lat * Math.sign(R.bano.lat) > Math.abs(R.bano.lat);
      if (inB && !pl.on && !(pl.cd > R.t)) { pl.on = true; pl.t = 0; const q = at(R.path, Math.max(0, R.s - 30)); pl.o.position.set(q.x, -.3, q.z); pl.o.visible = true; flash('¡ZONA DE BAÑO! ¡POLICÍA DETRÁS!', 1.4, true, '#33d6ff'); if (Snd.ok()) Snd.sirenStart && Snd.sirenStart(); }
      if (pl.on) { pl.t += dt; const dx = P.x - pl.o.position.x, dz = P.z - pl.o.position.z, d = Math.hypot(dx, dz) || 1, sp = Math.max(28, P.v + 4);
        pl.o.position.x += dx / d * sp * dt; pl.o.position.z += dz / d * sp * dt; pl.o.rotation.y = Math.atan2(dx, dz); pl.lamp.intensity = Math.sin(R.t * 18) > 0 ? 40 : 0;
        if (d < 5) { S.cash = Math.max(0, S.cash - 500); save(); flash('¡MULTA! −500 PTA', 1.5, true, '#ff3b4e'); if (Snd.ok()) Snd.fine(); pl.on = false; }
        else if (!inB && pl.t > 4) { pl.on = false; flash('¡TE HAS ESCAPADO!', 1, true, '#5be37a'); }
        if (!pl.on) { pl.cd = R.t + 8; pl.o.visible = false; pl.lamp.intensity = 0; if (Snd.sirenStop) Snd.sirenStop(); } } }
    if (R.mixers) for (const mx of R.mixers) mx.update(dt);
    if (R.fauna) for (const f of R.fauna) { f.s += f.v * dt * (f.k === 'delfin' ? 1 : .6); if (f.s > R.path.L + 30) f.s = -30;
      const q = at(R.path, Math.max(0, Math.min(R.path.L, f.s))), x = q.x - q.tz * f.lat, z = q.z + q.tx * f.lat, ry = Math.atan2(q.tx, q.tz);
      if (f.k === 'delfin') { const ph = (P.t * .9 + f.ph) % 3, jy = ph < 1 ? Math.sin(ph * Math.PI) * 2.2 - .3 : -1.2; f.o.position.set(x, jy, z); f.o.rotation.set(ph < 1 ? -Math.cos(ph * Math.PI) * .7 : 0, ry, 0);
        if (state === 'race' && Math.hypot(x - P.x, z - P.z) < 16) { R.dolT = (R.dolT || 0) + dt / 3; if (R.dolT > 3 && !R.dolGot) { R.dolGot = true; P.turboU = Math.min(5, (P.turboU ?? 2) + 1); S.cash += 300; save(); flash('¡AMIGO DE LOS DELFINES! +300 PTA +1 TURBO', 1.6, true, '#33d6ff'); if (Snd.ok()) Snd.pickup(); } } }
      else { f.o.position.set(x, -.25 + (window.__swell ? window.__swell(x, z) : 0), z); f.o.rotation.y = ry;
        if (state === 'race' && Math.hypot(x - P.x, z - P.z) < 2 && !(f.t > R.t)) { f.t = R.t + 3; P.v *= .45; flash('¡CUIDADO CON LA TORTUGA!', 1.1, true, '#5be37a'); if (Snd.ok()) Snd.bump(); } } }
    if (R.traffic) for (const t of R.traffic) { t.s += t.v * t.dir * dt; if (t.s > R.path.L + 40 || t.s < -40) t.dir *= -1;
      const q = at(R.path, Math.max(0, Math.min(R.path.L, t.s))), x = q.x - q.tz * t.lat, z = q.z + q.tx * t.lat, ry = Math.atan2(q.tx * t.dir, q.tz * t.dir);
      t.o.position.set(x, t.y + (window.__swell ? window.__swell(x, z) * .5 : 0), z); t.o.rotation.y = ry; const fx = Math.sin(ry), fz = Math.cos(ry), L = t.girls ? 8.5 : 3.5;
      t.cols.forEach((c, k) => { c.x = x + fx * (k - 1) * L; c.z = z + fz * (k - 1) * L; }); t.wk.update(dt, x - fx * L * 1.2, z - fz * L * 1.2, Math.min(1, t.v / 12), t.v);
      if (t.girls && !t.gave && state === 'race' && Math.hypot(x - P.x, z - P.z) < 26) { t.gave = true; P.turboU = Math.min(5, (P.turboU ?? 2) + 1); flash('¡LAS CHICAS DEL YATE TE SALUDAN! +1 TURBO (Y TE DISTRAES)', 1.8, true, '#ff7ad9'); if (Snd.ok()) Snd.girls(); P._distract = 1.6; } }
    if (R.coins) for (const c of R.coins) { if (c.got) { if (c.m.visible) { c.m.position.y += dt * 6; c.m.scale.multiplyScalar(1 - dt * 5); if (c.m.scale.x < .1) c.m.visible = false; } continue; }
      c.m.rotation.y += dt * 3; c.m.position.y = 1 + Math.sin(P.t * 3 + c.m.position.x) * .12;
      if (state === 'race' && Math.hypot(c.m.position.x - P.x, c.m.position.z - P.z) < 2.3) { c.got = true; R.coinN++; S.cash += 25; if (++S.coinsTot >= 100) award('coins'); if (Snd.ok()) Snd.coin(); pop('+25', '#ffd21a', (Math.random() - .5) * 80); rh.querySelector('.co span').textContent = R.coinN; } }
    if (R.movers) for (const m of R.movers) { const L = Math.abs(m.zb - m.za);
      if (m.wait > 0) { m.wait -= dt; m.ry += (m.dir > 0 ? Math.PI : 0) - m.ry > 0 ? Math.min(dt * 1.2, Math.abs((m.dir > 0 ? Math.PI : 0) - m.ry)) : -Math.min(dt * 1.2, Math.abs((m.dir > 0 ? Math.PI : 0) - m.ry)); }
      else { m.u += m.dir * m.sp * dt / L; if (m.u >= 1 || m.u <= 0) { m.u = Math.max(0, Math.min(1, m.u)); m.dir *= -1; m.wait = 3; } else m.ry = m.dir > 0 ? Math.PI : 0; }
      const z = m.za + (m.zb - m.za) * m.u, mv = m.wait > 0 ? 0 : m.sp; m.o.position.set(m.x, m.y + Math.sin(P.t * 1.3 + m.x) * .05 + (window.__swell ? window.__swell(m.x, z) * .7 : 0), z); m.o.rotation.set(Math.sin(P.t + m.x) * .015, m.ry, Math.sin(P.t * .9) * .02);
      const fx = Math.sin(m.ry), fz = Math.cos(m.ry); m.cols.forEach((c, k) => { c.x = m.x + fx * (k - 1) * m.r * 2.2; c.z = z + fz * (k - 1) * m.r * 2.2; });
      m.wk.update(dt, m.x - fx * m.r * 2.6, z - fz * m.r * 2.6, Math.min(1, mv / 8), mv); }
    const Z = R.Z, path = R.path;
    if (state === 'count') { R.count -= dt; const c = Math.ceil(R.count - .6);
      if (c !== R.lastCount && c >= 0) { R.lastCount = c; if (c > 0) { flash(String(c), .9); semSet(4 - c); if (Snd.ok()) Snd.beep(false); } else { flash('¡YA!', .8); semSet(-1); setTimeout(() => sem.style.display = 'none', 1200); if (Snd.ok()) Snd.beep(true); state = 'race'; R.started = true; } }
      rh.querySelector('.t').textContent = Z.obj === 'time' ? fmtT(R.time) : fmtT(0); P.v = 0; return; }
    // gasolina: se gasta al correr; sin gasolina la moto va muy lenta
    if (S.fuel > 0) { S.fuel = Math.max(0, S.fuel - (.12 + 1.13 * Math.min(1, P.v / 33)) * (P.v > 35 ? 2.2 : 1) * dt);
      if (S.fuel <= 0) { flash(R.jjPos ? '¡SIN GASOLINA! PARA EN EL JJ\'S' : '¡SIN GASOLINA!', 2.2, true); save(); } }
    window.__noFuel = S.fuel <= 0; R.lowT = (R.lowT || 0) - dt; if (S.fuel > 0 && S.fuel < 18 && R.lowT <= 0) { R.lowT = 4; if (Snd.ok()) Snd.warn(); }
    if ((R.hudT = (R.hudT || 0) - dt) <= 0) { R.hudT = .25; hud(); if ((P.turboU ?? 0) >= 5) award('turbo5'); }
    if (R.roxyPos) { const dr = Math.hypot(P.x - R.roxyPos.x, P.z - R.roxyPos.z);
      if (dr > 16) R.rxIn = false; else if (!R.rxIn && dr < 9 && P.v < 4) { R.rxIn = true; R.pen += 3; ctx.setPaused(true); state = 'jj'; save(); renderRoxy(); show('roxy'); return; } }
    if (R.jjPos) { const dj = Math.hypot(P.x - R.jjPos.x, P.z - R.jjPos.z);
      if (dj > 16) R.jjIn = false;
      else if (!R.jjIn && dj < 9 && P.v < 4) { R.jjIn = true; R.time = Math.max(.5, R.time - 3); ctx.setPaused(true); state = 'jj'; save(); renderJJ(); show('jj'); return; } }
    if ((R.miniT = (R.miniT || 0) - dt) <= 0) { R.miniT = .1; const cv = rh.querySelector('.mini'), c = cv.getContext('2d'), pts = R.path.pts || null;
      if (!R.mb) { let x0 = 1e9, x1 = -1e9, z0 = 1e9, z1 = -1e9; for (let s = 0; s <= R.path.L; s += 8) { const q = at(R.path, s); x0 = Math.min(x0, q.x); x1 = Math.max(x1, q.x); z0 = Math.min(z0, q.z); z1 = Math.max(z1, q.z); }
        const k = Math.min(340 / (x1 - x0 + 1), 200 / (z1 - z0 + 1)); R.mb = { x0, z0, k, ox: (380 - (x1 - x0) * k) / 2, oz: (240 - (z1 - z0) * k) / 2 }; }
      const mb = R.mb, X = x => 380 - (mb.ox + (x - mb.x0) * mb.k), Y = z => 240 - (mb.oz + (z - mb.z0) * mb.k);   // la costa queda arriba y se avanza de izquierda a derecha, como se ve desde el dron
      c.clearRect(0, 0, 380, 240); c.lineWidth = 7; c.strokeStyle = 'rgba(255,255,255,.35)'; c.lineCap = 'round'; c.beginPath();
      for (let s = 0; s <= R.path.L; s += 6) { const q = at(R.path, s); s ? c.lineTo(X(q.x), Y(q.z)) : c.moveTo(X(q.x), Y(q.z)); } c.stroke();
      const dot = (x, z, r, col) => { c.fillStyle = col; c.beginPath(); c.arc(X(x), Y(z), r, 0, 7); c.fill(); };
      const e = at(R.path, R.path.L - 4); dot(e.x, e.z, 9, '#ffffff');
      const nc = R.cps.find(q => !q.hit) || R.gates.find(q => !q.done); if (nc) { const q = at(R.path, nc.s); dot(q.x - q.tz * (nc.c || 0), q.z + q.tx * (nc.c || 0), 8, '#2bd94f'); }
      for (const r of R.rivals) dot(r.sk.root.position.x, r.sk.root.position.z, 7, r.fin ? 'rgba(255,255,255,.4)' : '#ff5a5a');
      c.save(); c.translate(X(P.x), Y(P.z)); c.rotate(Math.atan2(-Math.cos(P.th), -Math.sin(P.th))); c.fillStyle = '#ffe14d'; c.strokeStyle = '#0b1630'; c.lineWidth = 3; c.beginPath(); c.moveTo(14, 0); c.lineTo(-9, 9); c.lineTo(-5, 0); c.lineTo(-9, -9); c.closePath(); c.stroke(); c.fill(); c.restore(); }
    { const q = at(R.path, R.s), fx = Math.sin(P.th), fz = Math.cos(P.th); R.wrongT = (fx * q.tx + fz * q.tz < -.35 && P.v > 5) ? (R.wrongT || 0) + dt : 0;
      if (R.wrongT > 1 && msgT <= 0) flash('DIRECCIÓN CONTRARIA', 1, true, '#ff3b4e'); }
    // carrera libre: graba tu recorrido y mueve el fantasma del récord
    if (R.free && state === 'race') { R.recT += dt; if (R.recT >= .1) { R.recT -= .1; R.rec.push(+P.x.toFixed(2), +P.z.toFixed(2), +P.th.toFixed(3)); }
      if (R.ghost && ghostSki) { const k = R.t / .1, i = Math.min(Math.floor(k), R.ghost.p.length / 3 - 2), f = Math.min(1, k - i), a = R.ghost.p, j = i * 3;
        if (i >= 0) { ghostSki.root.position.set(a[j] + (a[j + 3] - a[j]) * f, 0, a[j + 1] + (a[j + 4] - a[j + 1]) * f); ghostSki.root.rotation.y = a[j + 2] + (a[j + 5] - a[j + 2]) * f; } } }
    // jugador en el recorrido
    const L = locate(path, P.x, P.z, R.hint); R.hint = L.i; const prevS = R.s; R.s = L.s; R.lat = L.lat; R.maxS = Math.max(R.maxS, R.s);
    if (Z.obj === 'time') { R.time -= dt; R.t += dt;
      for (const c of R.cps) if (!c.hit && prevS < c.s && R.s >= c.s) { c.hit = true; R.time += c.add; flash('+' + c.add + ' s', 1.2, true); if (Snd.ok()) Snd.check(); }
      if (R.time <= 0 && !R.free) { R.time = 0; return finishRace(false, '¡SE ACABÓ EL TIEMPO!'); } }
    else R.t += dt;
    if (Z.obj === 'slalom') for (const g of R.gates) if (!g.done && prevS < g.s && R.s >= g.s) { g.done = true;
      const okG = Math.abs(R.lat - g.c) <= 4.6, tint = okG ? 0x2bd94f : 0xff2b3a;
      for (const b of g.b) b.traverse(o => { if (o.isMesh && o.material && o.material.color && ['ff7a1a', 'ffd21a'].includes(o.material.color.getHexString())) { o.material = o.material.clone(); o.material.color.setHex(tint); if (o.material.emissive) { o.material.emissive.setHex(tint); o.material.emissiveIntensity = .55; } } });
      if (okG) { flash('¡BIEN!', .7, true, '#5be37a'); if (Snd.ok()) Snd.gate(); R.pts = (R.pts || 0) + 50; pop('+50', '#5be37a'); } else { g.miss = true; R.pen += 1; flash('+1 s', .9, true, '#ff3b4e'); if (Snd.ok()) Snd.miss(); } }
    // rivales
    if (R.rivals.length) {
      for (const r of R.rivals) {
        // IA como el 2D: usa turbo (más cuanto más difícil y si va por detrás) y se ajusta a tu ritmo
        r.tb = (r.tb || 0) - dt; r.tcd = (r.tcd ?? 3 + Math.random() * 4) - dt; if (r.tcd <= 0 && !r.fin) { r.tcd = [9, 8, 6, 5, 4][S.set.dif] + Math.random() * 4 - (r.s < R.s ? 2 : 0); r.tb = 2; }
        // boxes: en EL PUERTO y EL MAGO un rival para a repostar en el JJ'S (3 s), como en el 2D
        if (R.jjPos && r === R.rivals[R.rivals.length - 1]) { if (R.jjS == null) R.jjS = locate(R.path, R.jjPos.x, R.jjPos.z, 0).s;
          r.inPit = false; if (!r.pitDone && R.jjS > 120 && r.s > R.jjS - 45) { r.laneT = 18 * (Math.sign(at(R.path, r.s).tx) || 1); if (r.s > R.jjS - 40) r.v *= 1 - Math.min(1, dt * 2.5); if (r.s > R.jjS - 6) { r.inPit = true; r.pit = (r.pit || 0) + dt; if (r.pit > 3 || r.s > R.jjS + 10) r.pitDone = true; } } }
        const ahead = r.s - R.s, rub = ahead > 25 ? -.08 : ahead < -25 ? .07 : 0, vt = r.fin ? 8 : r.inPit ? 0 : r.vmax * (1 + rub) * (r.tb > 0 ? 1.22 : 1);
        r.v += (vt - r.v) * .55 * dt; r.s += r.v * dt;
        r.tl -= dt; if (r.tl <= 0) { r.tl = 2 + Math.random() * 3; r.laneT = (Math.random() * 2 - 1) * 9; }
        // choque con el jugador: los dos se empujan y pierden algo de velocidad
        const q0 = at(path, r.s), px = q0.x - q0.tz * r.lane, pz = q0.z + q0.tx * r.lane, dxp = P.x - px, dzp = P.z - pz, dpl = Math.hypot(dxp, dzp);
        if (dpl < 6 && Math.abs(r.lane - R.lat) < 5) r.laneT = r.lane + (r.lane >= R.lat ? 4 : -4);
        if (dpl < 2.6 && dpl > 1e-3) { const ov = 2.6 - dpl, nx = dxp / dpl, nz = dzp / dpl; P.x += nx * ov * .6; P.z += nz * ov * .6;
          r.lane += (r.lane >= R.lat ? 1 : -1) * ov * .4; P.v *= .93; r.v *= .93; if (Snd.ok() && !(R.bumpT > R.t)) { Snd.bump(); R.bumpT = R.t + .5; } }
        // evitar barcos, rocas y boyas que tenga delante
        for (const c of window.__COL.concat(window.__COLZ)) { const qa = at(path, r.s + 18), ax = qa.x - qa.tz * r.lane, az = qa.z + qa.tx * r.lane;
          if (Math.hypot(ax - c.x, az - c.z) < c.r + 3.5) { const cl = (c.x - qa.x) * -qa.tz + (c.z - qa.z) * qa.tx; r.laneT = cl + (r.lane >= cl ? 1 : -1) * (c.r + 4.5); }
          const dc = Math.hypot(px - c.x, pz - c.z); if (dc < c.r + 1.3) { const cl = (c.x - q0.x) * -q0.tz + (c.z - q0.z) * q0.tx; r.lane = cl + (r.lane >= cl ? 1 : -1) * (c.r + 1.3); r.v *= .7; } }
        const dl = (r.laneT - r.lane) * Math.min(1, dt * .9); r.lane += dl; r.steer += ((dl / Math.max(dt, 1e-3)) * .25 - r.steer) * Math.min(1, dt * 4);
        const q = place(r.sk.root, path, r.s, r.lane); r.sk.root.rotation.y -= r.steer * .15;
        r.sk.body.rotation.z = -r.steer * .25; r.sk.body.position.y = -.05 + Math.sin(P.t * 3 + r.vmax) * .02 + (window.__swell ? window.__swell(r.sk.root.position.x, r.sk.root.position.z) : 0);
        r.rd.userData.pose({ barY: .13, steer: Math.max(-1, Math.min(1, r.steer)), k: Math.min(1, r.v / 33), t: P.t });
        const f = { x: q.tx, z: q.tz }; r.wk.update(dt, r.sk.root.position.x - f.x * 1.5, r.sk.root.position.z - f.z * 1.5, Math.min(.55, r.v / 16), r.v);
        { const sp = window.__spray, rx = r.sk.root.position.x - f.x * 1.5, rz = r.sk.root.position.z - f.z * 1.5, Rn = Math.random;   // cola de gallo y cortina de proa de los rivales
          if (sp && r.v > 4 && Math.hypot(rx - P.x, rz - P.z) < 120) { const n = Math.floor(r.v * dt * 45 + Rn());
            for (let i = 0; i < n; i++) { const o = Rn() - .5; sp.emit(rx - f.z * o * .45, .22, rz + f.x * o * .45, -f.x * r.v * (.18 + Rn() * .22) - f.z * o * 2, 3 + Rn() * 4, -f.z * r.v * (.18 + Rn() * .22) + f.x * o * 2, .07 + Rn() * .1, .8 + Rn() * .7, .3 + Rn() * .3); }
            for (let i = 0; i < Math.floor(r.v * dt * 16); i++) { const sg = Rn() < .5 ? -1 : 1, bx = r.sk.root.position.x + f.x * 1.2, bz = r.sk.root.position.z + f.z * 1.2; sp.emit(bx - f.z * sg * .35, .12, bz + f.x * sg * .35, -f.z * sg * (2 + Rn() * 3) + f.x * r.v * .35, 1.5 + Rn() * 2, f.x * sg * (2 + Rn() * 3) + f.z * r.v * .35, .05 + Rn() * .07, .55 + Rn() * .5, .3); } } }
        if (!r.fin && r.s >= path.L - 4) { r.fin = R.t; R.finished.push(r.name); }
      }
      // rivales entre sí: no se atraviesan
      for (let a = 0; a < R.rivals.length; a++) for (let b = a + 1; b < R.rivals.length; b++) { const A = R.rivals[a], B = R.rivals[b];
        if (Math.abs(A.s - B.s) < 3.4 && Math.abs(A.lane - B.lane) < 2.6) { const ov = (2.6 - Math.abs(A.lane - B.lane)) * .5, sg = A.lane >= B.lane ? 1 : -1; A.lane += sg * ov; B.lane -= sg * ov;
          const back = A.s < B.s ? A : B; back.v *= .985; back.laneT = back.lane + sg * (back === A ? 3 : -3); } }
      { let best = 1e9, bv = 0; for (const r of R.rivals) { const d = Math.hypot(r.sk.root.position.x - P.x, r.sk.root.position.z - P.z); if (d < best) { best = d; bv = r.v; } }
        window.__rivNear = [Math.max(0, 1 - best / 45), Math.min(1, bv / 33)]; }   // para el sonido del rival más cercano
      const ahead = R.rivals.filter(r => (r.fin && (!R.pfin || r.fin < R.pfin)) || (!r.fin && r.s > R.s)).length; R.pos = ahead + 1;
      rh.querySelector('.pos').innerHTML = R.pos + '<small>º/' + (R.rivals.length + 1) + '</small>';
      if (R.prevPos && R.pos !== R.prevPos && R.t > 2 && !(R.posT > R.t)) { R.posT = R.t + .8; const up = R.pos < R.prevPos; R.prevPos = R.pos; if (up) { flash('¡ADELANTAS! ' + R.pos + 'º', .9, true, '#5be37a'); if (Snd.ok()) Snd.gate(); } else flash('TE ADELANTAN · ' + R.pos + 'º', .9, true, '#ff3b4e'); }
      if (!R.prevPos || R.t <= 2) R.prevPos = R.pos;
    } else rh.querySelector('.pos').innerHTML = Z.obj === 'slalom' ? R.gates.filter(q => q.done && !q.miss).length + '<small>/' + R.gates.length + ' boyas</small>' : (R.jumps ? R.jumps + '<small> saltos</small>' : '');
    rh.querySelector('.t').textContent = Z.obj === 'time' ? fmtT(R.time) : fmtT(R.t + R.pen);
    if (Math.abs(R.lat) > 45 && msgT <= 0) flash('VUELVE AL RECORRIDO', 1, true);
    if (R.s >= path.L - 4) { R.pfin = R.t; if (R.rivals.length) { const ahead = R.rivals.filter(r => r.fin && r.fin < R.t).length; R.pos = ahead + 1; } finishRace(true, Z.obj === 'time' ? '¡META!' : '¡META!'); }
  }

  // estado inicial: portada
  refreshCash(); applySettings(); show('menu');
  { const P0 = PAINTS.find(x => x.id === S.paint); if (P0 && P0.main && ctx.paintPlayer) ctx.paintPlayer(P0.main, P0.acc); if (S.paint === 'custom' && S.pc && ctx.paintPlayer) ctx.paintPlayer(S.pc.m, S.pc.a); ctx.setDecals && ctx.setDecals(S.dorsal, S.logo); }
  await ctx.applyGear(gearLook());
  return { update, drive: () => state === 'race', togglePause, state: () => state, uiOpen: () => ui.classList.contains('on'), dbg: { R: () => R, at, S } };
}
