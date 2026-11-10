(() => {
  const R = document.documentElement, $ = (s, c = document) => c.querySelector(s), $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const RM = matchMedia('(prefers-reduced-motion: reduce)');
  const store = { get: k => { try { return localStorage.getItem(k) } catch (e) { return null } }, set: (k, v) => { try { localStorage.setItem(k, v) } catch (e) {} } };

  /* ---------- thème ---------- */
  const tb = $('#themeBtn');
  const cur = () => R.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  const lab = () => { tb.textContent = cur() === 'dark' ? 'Clair' : 'Sombre'; tb.setAttribute('aria-label', cur() === 'dark' ? 'Passer en thème clair' : 'Passer en thème sombre') };
  const t0 = store.get('st-theme'); if (t0) R.dataset.theme = t0; lab();
  tb.addEventListener('click', () => { R.dataset.theme = cur() === 'dark' ? 'light' : 'dark'; store.set('st-theme', R.dataset.theme); lab() });

  /* ---------- vues (hash) ---------- */
  const views = { identite: $('#v-identite'), site: $('#v-site') };
  const show = () => {
    const h = location.hash.slice(1), v = views[h] ? h : (h && $('#' + CSS.escape(h)) && $('#' + CSS.escape(h)).closest('.view') ? $('#' + CSS.escape(h)).closest('.view').id.slice(2) : 'identite');
    Object.entries(views).forEach(([k, el]) => { el.hidden = k !== v });
    $$('.sw a').forEach(a => a.classList.toggle('on', a.dataset.v === v));
    if (views[h]) scrollTo(0, 0);
  };
  addEventListener('hashchange', show); show();

  /* ---------- langue ---------- */
  const lb = $('#langBtn'), site = $('#v-site');
  const setLang = l => { site.dataset.lang = l; site.setAttribute('lang', l); lb.textContent = l === 'fr' ? 'EN' : 'FR'; lb.setAttribute('aria-label', l === 'fr' ? 'Switch to English' : 'Passer en français'); $$('option[data-fr]', site).forEach(o => o.textContent = o.dataset[l]); store.set('st-lang', l) };
  setLang(store.get('st-lang') || 'fr');
  lb.addEventListener('click', () => setLang(site.dataset.lang === 'fr' ? 'en' : 'fr'));

  /* ---------- son : signature de marque (Web Audio, aucun fichier) ---------- */
  let AC;
  const ac = () => { if (!AC) AC = new (window.AudioContext || window.webkitAudioContext)(); if (AC.state === 'suspended') AC.resume(); return AC };
  // Renvoie le délai (ms) avant le déclenchement, pour caler le flash visuel.
  function sting(full = true) {
    const a = ac(), t = a.currentTime + .03, out = a.createGain(), comp = a.createDynamicsCompressor();
    out.gain.value = .85; out.connect(comp); comp.connect(a.destination);
    const T = full ? .6 : 0;
    if (full) { // 1. charge du flash : le sifflement qui monte
      const o = a.createOscillator(), g = a.createGain(); o.type = 'sine';
      o.frequency.setValueAtTime(1400, t); o.frequency.exponentialRampToValueAtTime(5200, t + T);
      g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(.045, t + T * .85); g.gain.exponentialRampToValueAtTime(.0001, t + T + .02);
      o.connect(g).connect(out); o.start(t); o.stop(t + T + .05);
    }
    const k = t + T;
    // 2. déclenchement : clac (bruit filtré) + coup sourd (mise sous tension de la sono)
    const len = Math.floor(a.sampleRate * .08), buf = a.createBuffer(1, len, a.sampleRate), d = buf.getChannelData(0);
    for (let i = 0; i < len; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / len, 3);
    const n = a.createBufferSource(), bp = a.createBiquadFilter(), ng = a.createGain();
    n.buffer = buf; bp.type = 'bandpass'; bp.frequency.value = 2600; bp.Q.value = .8; ng.gain.value = .6;
    n.connect(bp).connect(ng).connect(out); n.start(k);
    const b = a.createOscillator(), bg = a.createGain(); b.type = 'sine';
    b.frequency.setValueAtTime(140, k); b.frequency.exponentialRampToValueAtTime(42, k + .25);
    bg.gain.setValueAtTime(.0001, k); bg.gain.exponentialRampToValueAtTime(.9, k + .008); bg.gain.exponentialRampToValueAtTime(.0001, k + .45);
    b.connect(bg).connect(out); b.start(k); b.stop(k + .5);
    // 3. rémanence : une quinte (la, mi) qui s'assombrit et s'éteint
    const tail = full ? .9 : .35, lp = a.createBiquadFilter();
    lp.type = 'lowpass'; lp.frequency.setValueAtTime(5000, k); lp.frequency.exponentialRampToValueAtTime(500, k + tail); lp.connect(out);
    [[220, 'triangle', .1], [329.63, 'triangle', .07], [440, 'sine', .05], [221.2, 'sawtooth', .012]].forEach(([f, ty, v]) => {
      const o = a.createOscillator(), g = a.createGain(); o.type = ty; o.frequency.value = f;
      g.gain.setValueAtTime(.0001, k); g.gain.exponentialRampToValueAtTime(v, k + .012); g.gain.exponentialRampToValueAtTime(.0001, k + tail);
      o.connect(g).connect(lp); o.start(k); o.stop(k + tail + .05);
    });
    return (k - a.currentTime) * 1000;
  }

  /* ---------- le flash : un seul par séquence, jamais plus de 3 par seconde ---------- */
  function fire(stage, { sound = false, full = true } = {}) {
    if (stage.dataset.busy) return; stage.dataset.busy = '1';
    const delay = sound ? Math.max(0, sting(full)) : 140;
    stage.classList.remove('frozen'); stage.classList.add('charge');
    setTimeout(() => {
      stage.classList.remove('charge'); stage.classList.add('frozen');
      if (!RM.matches) { stage.classList.remove('fl'); void stage.offsetWidth; stage.classList.add('fl') }
    }, delay);
    setTimeout(() => { delete stage.dataset.busy }, delay + 1200);
    clearTimeout(stage._t); stage._t = setTimeout(() => { stage.classList.remove('fl'); if (!stage.dataset.rest) stage.classList.remove('frozen') }, delay + 4200);
  }

  // Identité : rejouer la signature
  $$('[data-replay]').forEach(btn => btn.addEventListener('click', () => fire($(btn.dataset.replay), { sound: btn.hasAttribute('data-sound'), full: true })));
  // Son seul (version longue et courte) avec tête de lecture
  $$('[data-play]').forEach(btn => btn.addEventListener('click', () => {
    const full = btn.dataset.play === 'full', ms = sting(full), ph = $('#playhead');
    if (ph && !RM.matches) { ph.style.transition = 'none'; ph.style.left = full ? '0%' : '40%'; void ph.offsetWidth; ph.style.transition = `left ${(full ? 1500 : 400) + ms - (full ? 600 : 0)}ms linear`; ph.style.left = '100%' }
    const st = $('#sigStage'); if (st) setTimeout(() => { if (!RM.matches) { st.classList.remove('fl'); void st.offsetWidth; st.classList.add('fl') } }, ms);
  }));

  // Site : hero à déclencher (bouton, clic dans la scène, touche Entrée sur le bouton)
  const hero = $('#heroStage'), sb = $('#soundBtn');
  let snd = false;
  sb.addEventListener('click', () => { snd = !snd; sb.setAttribute('aria-pressed', snd); sb.querySelectorAll('[data-s]').forEach(s => s.hidden = (s.dataset.s === 'on') !== snd); if (snd) ac() });
  $('#fireBtn').addEventListener('click', e => { e.stopPropagation(); fire(hero, { sound: snd }) });
  hero.addEventListener('click', e => { if (!e.target.closest('button, a')) fire(hero, { sound: snd }) });

  /* ---------- typo : curseur de largeur ---------- */
  const wr = $('#wdth'), ws = $('#wdthSample'), wv = $('#wdthVal');
  if (wr) wr.addEventListener('input', () => { ws.style.fontStretch = wr.value + '%'; wv.textContent = wr.value });

  /* ---------- typo cinétique au défilement ---------- */
  const kin = $$('[data-kin]');
  let raf = 0;
  const kinUpd = () => { raf = 0; const vh = innerHeight; kin.forEach(el => { if (el.closest('[hidden]')) return; const r = el.getBoundingClientRect(); const p = Math.min(1, Math.max(0, (vh - r.top) / (vh + r.height))); el.style.fontStretch = (60 + p * 90).toFixed(1) + '%' }) };
  if (!RM.matches) { addEventListener('scroll', () => { if (!raf) raf = requestAnimationFrame(kinUpd) }, { passive: true }); addEventListener('hashchange', kinUpd); kinUpd() }

  /* ---------- console : un canal à la fois au maximum ---------- */
  const strips = $$('.strip[data-ch]');
  const pick = s => strips.forEach(x => { const on = x === s; x.classList.toggle('on', on); x.querySelector('button').setAttribute('aria-pressed', on) });
  strips.forEach(s => { const b = s.querySelector('button'); b.addEventListener('click', () => pick(s)); s.addEventListener('pointerenter', e => { if (e.pointerType === 'mouse') pick(s) }) });

  /* ---------- formulaire (maquette) ---------- */
  const f = $('#briefForm');
  f.addEventListener('submit', e => {
    e.preventDefault();
    const ok = f.reportValidity(); const st = $('#formState');
    if (!ok) return;
    st.hidden = false; st.focus();
  });
})();
