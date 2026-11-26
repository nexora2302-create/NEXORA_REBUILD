// Exporte en PNG 1920 x 1080 les pages du brand book utiles en planches (03-COLOR-PALETTE-TYPOGRAPHY).
// Usage : node planches.js   (après python3 bb.py)
const {chromium} = require('playwright');
const path = require('path');
const OUT = path.join(__dirname, '..', '..', '03-COLOR-PALETTE-TYPOGRAPHY');
const PAGES = {8: 'logo-principal', 9: 'logo-construction', 12: 'logo-versions', 13: 'symbole-ns', 15: 'palette-principale', 16: 'palette-declinaisons', 17: 'contrastes', 18: 'typographies-familles', 19: 'typographies-echelle', 20: 'geste-manuscrit'};
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({viewport: {width: 1920, height: 1080}});
  await p.goto('file://' + path.join(__dirname, 'brandbook.html'), {waitUntil: 'networkidle'});
  await p.evaluate(() => document.fonts.ready);
  for (const [n, name] of Object.entries(PAGES)) {
    const file = `NEXORA-Studio-${String(n).padStart(2, '0')}-${name}.png`;
    await p.locator('.pg').nth(n - 1).screenshot({path: path.join(OUT, file)});
    console.log(file);
  }
  await b.close();
})();
