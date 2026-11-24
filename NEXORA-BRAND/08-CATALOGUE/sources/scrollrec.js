// Exemple : node scrollrec.js nexora dossier_images ; SCROLLER=.scroller CLIP=.frame node scrollrec.js agis dossier_images ; puis ffmpeg -framerate 30 -i dossier/f%05d.jpg -c:v libx264 -crf 20 -pix_fmt yuv420p -movflags +faststart sortie.mp4
// Vidéo de défilement image par image, à temps virtuel (rAF, horloges et animations CSS pilotés), donc sans saccade.
// Usage : node scrollrec.js <nexora|agis> <dossier_images> [largeur] [hauteur]
const {chromium} = require('playwright');
const fs = require('fs'), path = require('path');
const [, , SITE, OUT, W = 1920, H = 1080] = process.argv;
const FPS = 30, DT = 1000 / FPS;
const CLOCK = `(() => {
  let now = 0; const t0 = Date.now(); let q = [], id = 1, timers = [];
  performance.now = () => now; Date.now = () => t0 + now;
  window.requestAnimationFrame = cb => { q.push([id, cb]); return id++ };
  window.cancelAnimationFrame = i => { q = q.filter(e => e[0] !== i) };
  const st = window.setTimeout.bind(window);
  window.setTimeout = (cb, ms = 0, ...a) => { const i = id++; timers.push({i, at: now + ms, cb: () => cb(...a)}); return i };
  window.clearTimeout = i => { timers = timers.filter(t => t.i !== i) };
  window.setInterval = (cb, ms = 0) => { const i = id++; const tick = () => { timers.push({i, at: now + ms, cb: () => { cb(); tick() }}) }; tick(); return i };
  window.clearInterval = window.clearTimeout;
  const anims = new Map();
  window.__vt = dt => {
    now += dt;
    const due = timers.filter(t => t.at <= now); timers = timers.filter(t => t.at > now); due.forEach(t => { try { t.cb() } catch (e) {} });
    const cur = q; q = []; cur.forEach(([, cb]) => { try { cb(now) } catch (e) {} });
    for (const a of document.getAnimations()) {
      if (!anims.has(a)) { anims.set(a, (a.currentTime || 0) - dt); }
      a.pause(); const t = anims.get(a) + dt; anims.set(a, t); a.currentTime = t;
    }
  };
})();`;
const ease = x => x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
(async () => {
  const b = await chromium.launch();
  const ctx = await b.newContext({viewport: {width: +W, height: +H}, deviceScaleFactor: 1, reducedMotion: 'no-preference'});
  await ctx.addInitScript(CLOCK);
  let url = process.env.URL || 'https://nexoraa-nu.vercel.app/';
  if (SITE === 'agis') {
    const ROOT = '/home/user/agis-website';
    const types = {'.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.json': 'application/json', '.glb': 'model/gltf-binary', '.woff2': 'font/woff2', '.mp4': 'video/mp4'};
    await ctx.route('http://agis.local/**', r => {
      let u = new URL(r.request().url()).pathname; if (u === '/') u = '/index.html';
      const f = path.join(ROOT, decodeURIComponent(u));
      if (!f.startsWith(ROOT) || !fs.existsSync(f)) return r.fulfill({status: 404, body: ''});
      r.fulfill({status: 200, body: fs.readFileSync(f), contentType: types[path.extname(f).toLowerCase()] || 'application/octet-stream'});
    });
    url = 'http://agis.local/';
  }
  const p = await ctx.newPage();
  await p.goto(url, {waitUntil: 'load'});
  await p.waitForTimeout(2500);
  await p.addStyleTag({content: 'html{scroll-behavior:auto!important} ::-webkit-scrollbar{display:none}'});
  // préchauffage : faire défiler une fois pour charger les images paresseuses, puis revenir en haut
  const SEL = process.env.SCROLLER || '';
  await p.evaluate(sel => { window.__sc = sel ? document.querySelector(sel) : null; window.__go = y => { if (__sc) __sc.scrollTop = y; else scrollTo({top: y, behavior: 'instant'}) } }, SEL);
  const total = await p.evaluate(() => __sc ? __sc.scrollHeight - __sc.clientHeight : document.documentElement.scrollHeight - innerHeight);
  let clip;
  if (process.env.CLIP) { const r = await p.evaluate(s => { const q = document.querySelector(s).getBoundingClientRect(); return {x: q.x, y: q.y, width: q.width, height: q.height} }, process.env.CLIP); clip = {x: Math.round(r.x), y: Math.round(r.y), width: Math.floor(r.width / 2) * 2, height: Math.floor(r.height / 2) * 2}; console.log('clip', clip) }
  for (let y = 0; y <= total; y += 400) { await p.evaluate(y => __go(y), y); await p.waitForTimeout(60) }
  await p.evaluate(() => __go(0)); await p.waitForTimeout(1500);
  // plan : arrêts sur des points du défilement (fractions de la hauteur), mouvements adoucis entre eux
  const vh = await p.evaluate(() => __sc ? __sc.clientHeight : innerHeight), stops = JSON.parse(process.env.STOPS || 'null') || [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14].map(k => Math.min(total, k * vh));
  const plan = []; // [y_début, y_fin, durée_ms]
  plan.push([0, 0, 1800]);
  for (let i = 1; i < stops.length; i++) { if (stops[i] <= stops[i - 1]) continue; plan.push([stops[i - 1], stops[i], Math.max(1100, (stops[i] - stops[i - 1]) / vh * 1300)]); plan.push([stops[i], stops[i], 700]) }
  let f = 0;
  for (const [a, z, d] of plan) {
    const n = Math.round(d / DT);
    for (let k = 1; k <= n; k++) {
      const y = a + (z - a) * ease(k / n);
      await p.evaluate(y => __go(Math.round(y)), y);
      await p.waitForTimeout(25);
      await p.evaluate(dt => window.__vt(dt), DT);
      await p.screenshot({path: `${OUT}/f${String(f++).padStart(5, '0')}.jpg`, type: 'jpeg', quality: 92, clip});
    }
  }
  console.log(SITE, 'images', f, 'hauteur', total);
  await b.close();
})();
