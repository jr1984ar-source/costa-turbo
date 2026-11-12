// Sonido del juego con Web Audio (sin archivos): motor, agua, viento, turbo y golpe en la orilla.
// El navegador solo deja sonar tras un gesto del usuario (tecla, clic o toque): se activa solo.
export function createSound() {
  let ctx = null, g = null;
  const S = {};
  function noiseBuf(c) { const b = c.createBuffer(1, c.sampleRate * 2, c.sampleRate), d = b.getChannelData(0); for (let i = 0; i < d.length; i++) d[i] = Math.random() * 2 - 1; return b; }
  function start() {
    if (ctx) { if (ctx.state === 'suspended') ctx.resume(); return; }
    const AC = window.AudioContext || window.webkitAudioContext; if (!AC) return;
    ctx = new AC(); const nb = noiseBuf(ctx);
    g = { master: ctx.createGain() }; g.master.gain.value = 0.9; g.master.connect(ctx.destination);
    // motor: dos dientes de sierra + temblor de cilindros
    g.eng = ctx.createGain(); g.eng.gain.value = 0; g.engLP = ctx.createBiquadFilter(); g.engLP.type = 'lowpass'; g.engLP.frequency.value = 400;
    g.o1 = ctx.createOscillator(); g.o1.type = 'sawtooth'; g.o2 = ctx.createOscillator(); g.o2.type = 'square';
    g.lfo = ctx.createOscillator(); g.lfoG = ctx.createGain(); g.lfoG.gain.value = 0.35; g.lfo.connect(g.lfoG); g.lfoG.connect(g.eng.gain);
    g.o1.connect(g.engLP); g.o2.connect(g.engLP); g.engLP.connect(g.eng); g.eng.connect(g.master);
    // agua: ruido filtrado que crece con la velocidad
    g.wat = ctx.createGain(); g.wat.gain.value = 0; g.watBP = ctx.createBiquadFilter(); g.watBP.type = 'bandpass'; g.watBP.frequency.value = 900; g.watBP.Q.value = 0.7;
    g.n1 = ctx.createBufferSource(); g.n1.buffer = nb; g.n1.loop = true; g.n1.connect(g.watBP); g.watBP.connect(g.wat); g.wat.connect(g.master);
    // viento
    g.wnd = ctx.createGain(); g.wnd.gain.value = 0; g.wndLP = ctx.createBiquadFilter(); g.wndLP.type = 'lowpass'; g.wndLP.frequency.value = 500;
    g.n2 = ctx.createBufferSource(); g.n2.buffer = nb; g.n2.loop = true; g.n2.playbackRate.value = 0.6; g.n2.connect(g.wndLP); g.wndLP.connect(g.wnd); g.wnd.connect(g.master);
    // turbo: silbido ascendente + soplido
    g.tur = ctx.createGain(); g.tur.gain.value = 0; g.o3 = ctx.createOscillator(); g.o3.type = 'sine'; g.o3.connect(g.tur);
    g.turBP = ctx.createBiquadFilter(); g.turBP.type = 'bandpass'; g.turBP.frequency.value = 2400; g.turBP.Q.value = 1.2; g.n3 = ctx.createBufferSource(); g.n3.buffer = nb; g.n3.loop = true; g.n3.connect(g.turBP); g.turBP.connect(g.tur);
    g.tur.connect(g.master);
    S.nb = nb;
    [g.o1, g.o2, g.o3, g.lfo, g.n1, g.n2, g.n3].forEach(n => n.start());
  }
  ['keydown', 'pointerdown', 'touchstart'].forEach(e => addEventListener(e, start, { passive: true }));
  document.addEventListener('visibilitychange', () => { if (ctx) document.hidden ? ctx.suspend() : ctx.resume(); });
  let hitCool = 0;
  S.hit = () => {   // golpe sordo al rozar la orilla
    if (!ctx || ctx.state !== 'running' || hitCool > ctx.currentTime) return; hitCool = ctx.currentTime + 0.6;
    const t = ctx.currentTime, o = ctx.createOscillator(), og = ctx.createGain(); o.type = 'sine'; o.frequency.setValueAtTime(120, t); o.frequency.exponentialRampToValueAtTime(40, t + 0.25);
    og.gain.setValueAtTime(0.5, t); og.gain.exponentialRampToValueAtTime(0.001, t + 0.3); o.connect(og); og.connect(g.master); o.start(t); o.stop(t + 0.35);
    const n = ctx.createBufferSource(); n.buffer = S.nb; const ng = ctx.createGain(), nf = ctx.createBiquadFilter(); nf.type = 'lowpass'; nf.frequency.value = 900;
    ng.gain.setValueAtTime(0.35, t); ng.gain.exponentialRampToValueAtTime(0.001, t + 0.4); n.connect(nf); nf.connect(ng); ng.connect(g.master); n.start(t, Math.random()); n.stop(t + 0.45);
  };
  // v en m/s (0..31), acc 0..1, turbo bool, paused bool
  S.update = (v, acc, turbo, paused) => {
    if (!ctx || ctx.state !== 'running') return; const t = ctx.currentTime, k = Math.min(1, v / 31), tc = 0.08;
    g.master.gain.setTargetAtTime(paused ? 0 : 0.9, t, 0.05);
    const f = 38 + k * 78 + (acc ? 14 : 0) + (turbo ? 20 : 0);
    g.o1.frequency.setTargetAtTime(f, t, tc); g.o2.frequency.setTargetAtTime(f * 0.5, t, tc);
    g.lfo.frequency.setTargetAtTime(14 + k * 22, t, tc);
    g.engLP.frequency.setTargetAtTime(260 + k * 900 + (acc ? 300 : 0) + (turbo ? 500 : 0), t, tc);
    g.eng.gain.setTargetAtTime(0.18 + (acc ? 0.14 : 0) + k * 0.1, t, tc);
    g.watBP.frequency.setTargetAtTime(700 + k * 1800, t, tc); g.wat.gain.setTargetAtTime(k * k * 0.32 + (v > 1 ? 0.02 : 0), t, tc);
    g.wndLP.frequency.setTargetAtTime(300 + k * 1400, t, tc); g.wnd.gain.setTargetAtTime(k * 0.14, t, tc);
    g.tur.gain.setTargetAtTime(turbo ? 0.09 : 0, t, turbo ? 0.05 : 0.25); g.o3.frequency.setTargetAtTime(turbo ? 900 + k * 700 : 500, t, 0.3);
  };
  return S;
}
