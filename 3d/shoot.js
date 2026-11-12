const { chromium } = require('playwright');
(async () => {
  const shots = process.argv.slice(2);
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  for (const s of shots) {
    const [name, w, h, dpr, q] = s.split(':');
    const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: +dpr });
    p.on('crash', () => console.log('CRASH ' + name)); const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') errs.push(m.text().slice(0, 400)); });
    const t0 = Date.now();
    await p.goto(`http://localhost:8765/shots.html?${q}`);
    await p.waitForFunction(() => window.__done === true, null, { timeout: 300000 }).catch(e => errs.push('TIMEOUT'));
    try { await p.screenshot({ path: `out/${name}.png` }); } catch (e) { console.log('shot fail', name, e.message.slice(0, 80)); }
    console.log(name, ((Date.now() - t0) / 1000).toFixed(1) + 's', errs.slice(0, 6));
    await p.close();
  }
  await b.close();
})();
