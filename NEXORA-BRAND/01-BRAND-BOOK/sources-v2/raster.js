// PNG du logo (2048 px de large) et du favicon (16 à 512) à partir des SVG.
const {chromium} = require('playwright'); const fs = require('fs'), path = require('path');
const B = path.join(__dirname, '..', '..', '02-LOGO-BRAND-ASSETS');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  const shot = async (svgFile, out, w, h) => {
    const svg = fs.readFileSync(svgFile, 'utf8').replace('<svg ', `<svg style="width:${w}px;height:${h}px;display:block" `);
    await p.setViewportSize({width: w, height: h});
    await p.setContent(`<html><body style="margin:0;background:transparent">${svg}</body></html>`);
    await p.screenshot({path: out, omitBackground: true});
  };
  for (const f of fs.readdirSync(path.join(B, 'svg'))) {
    const s = fs.readFileSync(path.join(B, 'svg', f), 'utf8'); const vb = s.match(/viewBox="([^"]+)"/)[1].split(' ').map(Number);
    const W = 2048, H = Math.round(W * vb[3] / vb[2]);
    await shot(path.join(B, 'svg', f), path.join(B, 'png', f.replace('.svg', '.png')), W, H);
  }
  const fav = path.join(B, 'favicon', 'favicon.svg');
  for (const n of [16, 32, 48, 180, 192, 512]) await shot(fav, path.join(B, 'favicon', n === 180 ? 'apple-touch-icon-180.png' : `favicon-${n}.png`), n, n);
  await b.close();
})();
