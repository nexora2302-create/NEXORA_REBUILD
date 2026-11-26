// Rend catalogue.html en PDF 1920 x 1080 et, en option, une image par page pour contrôle visuel.
// Usage : node pdf.js [dossier_images]
const {chromium} = require('playwright');
const path = require('path');
const HERE = __dirname, SHOTS = process.argv[2];
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1920, height: 1080}});
  await p.goto('file://' + path.join(HERE, 'catalogue.html'), {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  const fonts = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight));
  console.log('polices', [...new Set(fonts)].join(', '));
  if (SHOTS) {
    const n = await p.locator('.pg').count();
    for (let i = 0; i < n; i++) await p.locator('.pg').nth(i).screenshot({path: `${SHOTS}/p${String(i + 1).padStart(2, '0')}.jpg`, type: 'jpeg', quality: 80});
    const over = await p.evaluate(() => [...document.querySelectorAll('.pg')].map((pg, i) => { const r = pg.getBoundingClientRect(); const bad = [...pg.querySelectorAll('*')].filter(e => { const q = e.getBoundingClientRect(); return q.width && (q.bottom > r.bottom - 40 || q.right > r.right - 60) && !e.closest('.cv-word') && !e.closest('.screens') && getComputedStyle(e).position !== 'absolute' }).map(e => e.className || e.tagName); return bad.length ? `p${i + 1}: ${[...new Set(bad)].slice(0, 6)}` : null }).filter(Boolean));
    console.log('débords', over);
  }
  await p.pdf({path: path.join(HERE, '..', 'NEXORA-Studio-Catalogue-2026.pdf'), width: '1920px', height: '1080px', printBackground: true, preferCSSPageSize: true});
  await b.close();
})();
