const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  for (const s of process.argv.slice(2)) {
    const [name, q] = s.split('|');
    const p = await b.newPage({ viewport: { width: 640, height: 400 } }); const errs = [];
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text().slice(0, 200)); });
    await p.goto('http://localhost:8765/view.html?' + q); await p.waitForFunction(() => window.__done, null, { timeout: 120000 }).catch(() => errs.push('TIMEOUT'));
    await p.screenshot({ path: 'out/' + name + '.png' }); console.log(name, errs.slice(0, 3)); await p.close();
  }
  await b.close();
})();
