// Música del juego 2D (menú, carrera y final), hecha con el sintetizador del sonido, igual que en el 2D
import { Snd } from './sound.js?v=2';
const MEL = [
 [[0,76,2],[2,73,2],[4,76,2],[6,78,2],[8,76,4],[12,73,2],[14,71,2]],
 [[0,71,2],[2,68,2],[4,71,2],[6,73,2],[8,71,6],[14,68,2]],
 [[0,69,2],[2,73,2],[4,78,4],[8,76,2],[10,73,2],[12,69,4]],
 [[0,66,2],[2,69,2],[4,74,2],[6,76,2],[8,78,4],[12,76,2],[14,73,2]],
 [[0,76,2],[2,73,2],[4,76,2],[6,78,2],[8,81,4],[12,78,2],[14,76,2]],
 [[0,71,2],[2,68,2],[4,71,2],[6,76,2],[8,76,6],[14,73,2]],
 [[0,73,2],[2,76,2],[4,78,4],[8,76,2],[10,73,2],[12,71,4]],
 [[0,74,2],[2,73,2],[4,71,2],[6,69,2],[8,69,8]]];
export const Music2D = { timer: null, pat: null, step: 0, next: 0,
  play(p) { if (!Snd.ctx || this.pat === p) return; this.stop(); this.pat = p; this.step = 0; this.next = Snd.ctx.currentTime + .1; this.timer = setInterval(() => this.tick(), 25); },
  stop() { clearInterval(this.timer); this.timer = null; this.pat = null; },
  bpm() { return this.pat === 'final' ? 134 : this.pat === 'race' ? 124 : 100; },
  tick() { const c = Snd.ctx; if (!c || c.state !== 'running') { if (c) this.next = c.currentTime + .1; return; } const spb = 60 / this.bpm() / 4;
    while (this.next < c.currentTime + .15) { this.note(this.step, this.next); this.step++; this.next += spb; } },
  note(i, t) { if (!Snd.on) return; const s = i % 16, bar = ((i / 16) | 0) % 8, ci = [0, 1, 2, 3, 0, 1, 3, 1][bar], B = Snd.mus, mf = m => 440 * Math.pow(2, (m - 69) / 12), race = this.pat !== 'menu', spb = 60 / this.bpm() / 4;
    const roots = [45, 40, 42, 38], tri = [[69, 73, 76], [64, 68, 71], [66, 69, 73], [62, 66, 69]];
    if (race) { if (s % 2 === 0) Snd.tone({ at: t, w: 'sawtooth', f: mf(roots[ci] + (s % 4 === 2 ? 12 : 0)), t: spb * 1.8, v: .075, bus: B }); }
    else if (s % 4 === 0) Snd.tone({ at: t, w: 'triangle', f: mf(roots[ci]), t: spb * 3.6, v: .17, bus: B });
    if (race ? s % 4 === 0 : (s === 0 || s === 8)) Snd.tone({ at: t, w: 'sine', f: 150, f2: 42, t: .2, v: .38, bus: B });
    if (s === 4 || s === 12) Snd.hiss({ at: t, ft: 'bandpass', f: 1700, t: .15, v: race ? .2 : .12, q: .8, bus: B });
    if (race ? s % 2 === 1 : s % 4 === 2) Snd.hiss({ at: t, ft: 'highpass', f: 7500, t: .04, v: .06, bus: B });
    if (race && s % 4 === 2) Snd.hiss({ at: t, ft: 'highpass', f: 9500, t: .025, v: .03, bus: B });
    if (s % 4 === 2) for (const n of tri[ci]) Snd.tone({ at: t, w: 'triangle', f: mf(n), t: spb * 1.4, v: race ? .032 : .028, bus: B });
    for (const [st, n, len] of MEL[bar]) if (st === s) { const d = len * spb * .95; Snd.tone({ at: t, w: race ? 'square' : 'triangle', f: mf(n), t: d, v: race ? .042 : .06, a: .01, bus: B }); if (race) Snd.tone({ at: t, w: 'triangle', f: mf(n + 12), t: d * .7, v: .02, bus: B }); } } };
