(() => {
  const $ = (s, c = document) => c.querySelector(s), $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const RM = matchMedia('(prefers-reduced-motion: reduce)');
  const D = 5.6;                       // décalage de repos de chaque moitié (unités du symbole)
  const q12 = t => Math.floor(t * 12) / 12;   // cadence 12 images par seconde
  const cl = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
  const bez = (x1, y1, x2, y2) => t => { // courbe de Bézier cubique (comme en CSS)
    if (t <= 0) return 0; if (t >= 1) return 1;
    let u = t; for (let i = 0; i < 8; i++) { const x = 3*(1-u)*(1-u)*u*x1 + 3*(1-u)*u*u*x2 + u*u*u - t; const dx = 3*(1-u)*(1-u)*x1 + 6*(1-u)*u*(x2-x1) + 3*u*u*(1-x2); if (Math.abs(dx) < 1e-6) break; u = cl(u - x / dx) }
    return 3*(1-u)*(1-u)*u*y1 + 3*(1-u)*u*u*y2 + u*u*u;
  };
  const OUT = bez(.16, 1, .3, 1), INOUT = bez(.7, 0, .2, 1);
  const ph = (t, a, b) => cl((t - a) / (b - a));     // avancement 0..1 d'une phase

  // Calques d'une scène
  const L = svg => ({
    sym: $('.sym', svg), ht: $('.sym .ht', svg), hb: $('.sym .hb', svg), ring: $('.ring', svg),
    e: $$('.esym', svg), wm: $('.wmk', svg), letters: $$('.wmk .L', svg), ot: $('.wmk .ot', svg), ob: $('.wmk .ob', svg),
    we: $$('.wecho', svg), slogan: $('.slogan', svg), sl: $$('.slogan tspan', svg), url: $('.url', svg), clip: $('.clipr', svg),
    pa: $('.pa', svg), pb: $('.pb', svg), slit: $('.slit', svg), scB: $('.scB', svg)
  });
  const show = (el, v) => el && el.setAttribute('visibility', v ? 'visible' : 'hidden');
  const op = (el, v) => el && el.setAttribute('opacity', v.toFixed(3));
  const off = (l, d, o = 1) => { l.ht.setAttribute('transform', `translate(${-d} 0)`); l.hb.setAttribute('transform', `translate(${d} 0)`); if (l.ot) { l.ot.setAttribute('transform', `translate(${-d * o * 15.24} 0)`); l.ob.setAttribute('transform', `translate(${d * o * 15.24} 0)`) } };
  const place = (el, x, y, s, r = 0) => el.setAttribute('transform', `translate(${x} ${y}) rotate(${r} ${50*s} ${50*s}) scale(${s})`);

  const ANIMS = {
    // 1. Révélation d'ouverture : le disque tourne image par image derrière ses fentes, s'arrête net, puis le mot s'enchaîne.
    reveal: { dur: 2.2, render(l, t) {
      const tq = q12(t);
      const k = Math.round(tq * 12);
      if (t < 0.9) {
        show(l.ring, 1); place(l.ring, 250, 110, 1.4, k * 30);
        const seq = [-1, -.5, 0, .5, 1, .5, 0, -.5];                     // phases du mouvement, une par image
        off(l, D * 2 * seq[k % 8]); place(l.sym, 250, 110, 1.4);
        l.letters.forEach(x => show(x, 0)); show(l.ot, 0); show(l.ob, 0); l.we.forEach(x => op(x, 0));
      } else {
        show(l.ring, 0); off(l, D, 0);
        const m = ph(tq, .9, 1.25);                                       // le symbole glisse à gauche, image par image
        place(l.sym, 250 - m * 168, 110 + m * 35, 1.4 - m * .7);
        const n = Math.floor((tq - 1.0) * 12) + 1;                        // une lettre par image
        l.letters.forEach((x, i) => show(x, i < n)); show(l.ot, n > 3); show(l.ob, n > 3); off(l, D, 1);
        const e = 1 - OUT(ph(t, 1.5, 2.2));                               // les échos du mot s'éteignent, fluide
        l.we.forEach((x, i) => op(x, n >= 6 ? e * [.35, .12][i] : 0));
      }
    }},
    // 2. Boucle discrète : les deux moitiés respirent de ± 1,6, à 12 i/s.
    loop: { dur: 2.4, loop: true, render(l, t) {
      const d = D + 1.6 * Math.sin(2 * Math.PI * q12(t) / 2.4); off(l, d, 1);
    }},
    // 3. Transition : la fente s'ouvre, puis les deux moitiés de l'image glissent en sens contraire.
    wipe: { dur: 0.6, render(l, t) {
      const s = OUT(ph(t, 0, .15)), m = INOUT(ph(t, .12, .6));
      l.slit.setAttribute('height', (14 * s * (1 - m)).toFixed(2)); l.slit.setAttribute('y', (180 - 7 * s * (1 - m)).toFixed(2));
      l.pa.setAttribute('transform', `translate(${-660 * m} 0)`); l.pb.setAttribute('transform', `translate(${660 * m} 0)`);
    }},
    // 4. Carte de fin : trois échos convergent, le mot sort de la fente, le slogan s'écrit image par image.
    end: { dur: 4, render(l, t) {
      const tq = q12(t); const a = ph(tq, 0, .75);
      const xs = [-150, -75, 0].map(x => x * (1 - a));
      l.e.forEach((g, i) => { place(g, 285 + xs[i], 46, .7); op(g, a < 1 ? [.12, .35][i] : 0) }); off(l, D, 1);
      place(l.sym, 285 + xs[2], 46, .7);
      const w = OUT(ph(t, .75, 1.5)); l.clip.setAttribute('y', (178 - 40 * w).toFixed(1)); l.clip.setAttribute('height', (80 * w).toFixed(1));
      const n = Math.max(0, Math.floor((tq - 1.5) * 12)); l.sl.forEach((x, i) => show(x, i < n));
      show(l.url, tq >= 2.4);
    }},
    // 5. Avatar : les moitiés traversent l'instant (3 images), puis reviennent, fluide.
    avatar: { dur: 0.8, render(l, t) {
      let d; if (t < .25) { const f = Math.floor(t * 12); d = D * [1, 0, -1][Math.min(2, f)] } else d = -D + 2 * D * OUT(ph(t, .25, .8));
      off(l, d, 0);
    }},
    // 6. Chargement : le disque tourne de 30° par image, 12 images par tour, comme les disques de 1833.
    loader: { dur: 1, loop: true, render(l, t) { place(l.sym, 270, 130, 1, Math.floor(t * 12) * 30) } },
  };

  // Lecture
  const cards = $$('.anim');
  const state = new Map();
  function draw(card, t) { const a = ANIMS[card.dataset.anim]; a.render(L($('.stage svg', card)), a.loop ? t % a.dur : Math.min(t, a.dur)); const c = $('.clock', card); if (c) c.textContent = (a.loop ? t % a.dur : Math.min(t, a.dur)).toFixed(2).replace('.', ',') + ' s' }
  function play(card, withSound) {
    const a = ANIMS[card.dataset.anim]; if (RM.matches) { draw(card, a.loop ? 0 : a.dur); return }
    const st = { t0: performance.now(), raf: 0 }; cancelAnimationFrame((state.get(card) || {}).raf || 0); state.set(card, st);
    if (withSound) sting(0.9);
    const step = now => { const t = (now - st.t0) / 1000; draw(card, t); if (a.loop || t < a.dur) st.raf = requestAnimationFrame(step) };
    st.raf = requestAnimationFrame(step);
  }
  // Frises d'images clés (même fonction de rendu, temps figés)
  cards.forEach(card => {
    const a = ANIMS[card.dataset.anim], strip = $('.strip', card), src = $('.stage svg', card);
    const n = +card.dataset.frames || 8;
    for (let i = 0; i < n; i++) {
      const t = a.dur * i / (a.loop ? n : n - 1);
      const f = document.createElement('figure'); const c = src.cloneNode(true); c.removeAttribute('id'); c.setAttribute('aria-hidden', 'true');
      $$('[id]', c).forEach(x => x.id = x.id + '-f' + i); $$('[clip-path]', c).forEach(x => x.setAttribute('clip-path', x.getAttribute('clip-path').replace(')', '-f' + i + ')')));
      f.appendChild(c); const cap = document.createElement('figcaption'); cap.textContent = String(i + 1).padStart(2, '0') + ' · ' + t.toFixed(2).replace('.', ',') + ' s'; f.appendChild(cap);
      strip.appendChild(f); a.render(L(c), t);
    }
    draw(card, a.loop ? 0 : a.dur);                                         // repos : image finale, complète
    $('.replay', card).addEventListener('click', () => play(card, false));
    const sb = $('.withsound', card); if (sb) sb.addEventListener('click', () => play(card, true));
  });
  // Les boucles tournent seulement à l'écran
  const io = new IntersectionObserver(es => es.forEach(e => { const card = e.target; if (!ANIMS[card.dataset.anim].loop) return; if (e.isIntersecting) play(card); else cancelAnimationFrame((state.get(card) || {}).raf || 0) }), { threshold: .2 });
  cards.forEach(c => io.observe(c));
  $$('.anim[data-anim="avatar"] .stage').forEach(s => s.addEventListener('pointerenter', () => play(s.closest('.anim'))));

  // Signature sonore (v1), recalée : le déclenchement tombe sur l'arrêt du disque.
  let AC; const ac = () => { if (!AC) AC = new (window.AudioContext || window.webkitAudioContext)(); if (AC.state === 'suspended') AC.resume(); return AC };
  function sting(T) {
    const a = ac(), t = a.currentTime + .02, out = a.createGain(), comp = a.createDynamicsCompressor(); out.gain.value = .8; out.connect(comp); comp.connect(a.destination);
    const o = a.createOscillator(), g = a.createGain(); o.type = 'sine'; o.frequency.setValueAtTime(1400, t); o.frequency.exponentialRampToValueAtTime(4800, t + T);
    g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(.035, t + T * .85); g.gain.exponentialRampToValueAtTime(.0001, t + T + .02); o.connect(g).connect(out); o.start(t); o.stop(t + T + .05);
    const k = t + T, len = Math.floor(a.sampleRate * .07), buf = a.createBuffer(1, len, a.sampleRate), dd = buf.getChannelData(0);
    for (let i = 0; i < len; i++) dd[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / len, 3);
    const n = a.createBufferSource(), bp = a.createBiquadFilter(), ng = a.createGain(); n.buffer = buf; bp.type = 'bandpass'; bp.frequency.value = 2400; ng.gain.value = .5; n.connect(bp).connect(ng).connect(out); n.start(k);
    const lp = a.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.setValueAtTime(4000, k); lp.frequency.exponentialRampToValueAtTime(500, k + 1.2); lp.connect(out);
    [[220, .09], [329.63, .06], [440, .04]].forEach(([f, v]) => { const o2 = a.createOscillator(), g2 = a.createGain(); o2.type = 'triangle'; o2.frequency.value = f; g2.gain.setValueAtTime(.0001, k); g2.gain.exponentialRampToValueAtTime(v, k + .012); g2.gain.exponentialRampToValueAtTime(.0001, k + 1.2); o2.connect(g2).connect(lp); o2.start(k); o2.stop(k + 1.25) });
  }

  // Thème
  const r = document.documentElement, tb = $('#themeBtn');
  const cur = () => r.dataset.theme || (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
  const lab = () => { tb.textContent = cur() === 'dark' ? 'Thème clair' : 'Thème sombre' };
  try { const t = localStorage.getItem('s5'); if (t) r.dataset.theme = t } catch (e) {} lab();
  tb.addEventListener('click', () => { r.dataset.theme = cur() === 'dark' ? 'light' : 'dark'; lab(); try { localStorage.setItem('s5', r.dataset.theme) } catch (e) {} });
})();
