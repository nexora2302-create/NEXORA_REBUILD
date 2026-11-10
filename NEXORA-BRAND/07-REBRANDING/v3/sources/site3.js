(() => {
  const R = document.documentElement, $ = (s, c = document) => c.querySelector(s), $$ = (s, c = document) => [...c.querySelectorAll(s)];
  const RM = matchMedia('(prefers-reduced-motion: reduce)');
  const store = { get: k => { try { return localStorage.getItem(k) } catch (e) { return null } }, set: (k, v) => { try { localStorage.setItem(k, v) } catch (e) {} } };

  /* thème */
  const tb = $('#themeBtn');
  const cur = () => R.dataset.theme || (matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
  const lab = () => { tb.textContent = cur() === 'dark' ? 'Clair' : 'Sombre' };
  const t0 = store.get('rh-theme'); if (t0) R.dataset.theme = t0; lab();
  tb.addEventListener('click', () => { R.dataset.theme = cur() === 'dark' ? 'light' : 'dark'; store.set('rh-theme', R.dataset.theme); lab() });

  /* vues */
  const views = { identite: $('#v-identite'), site: $('#v-site') };
  const show = () => {
    const h = location.hash.slice(1); let v = views[h] ? h : null;
    if (!v) { const el = h && document.getElementById(h); v = el && el.closest('.view') ? el.closest('.view').id.slice(2) : 'identite' }
    Object.entries(views).forEach(([k, el]) => { el.hidden = k !== v });
    $$('.sw a').forEach(a => a.classList.toggle('on', a.dataset.v === v));
    if (views[h]) scrollTo(0, 0);
  };
  addEventListener('hashchange', show); show();

  /* langue (maquette) */
  const lb = $('#langBtn'), site = $('#v-site');
  const setLang = l => { site.dataset.lang = l; site.setAttribute('lang', l); lb.textContent = l === 'fr' ? 'EN' : 'FR'; lb.setAttribute('aria-label', l === 'fr' ? 'Switch to English' : 'Passer en français'); $$('option[data-fr]', site).forEach(o => o.textContent = o.dataset[l]); store.set('rh-lang', l) };
  setLang(store.get('rh-lang') || 'fr');
  lb.addEventListener('click', () => setLang(site.dataset.lang === 'fr' ? 'en' : 'fr'));

  /* son (bonus) */
  let AC; const ac = () => { if (!AC) AC = new (window.AudioContext || window.webkitAudioContext)(); if (AC.state === 'suspended') AC.resume(); return AC };
  function note(a, t, f, dur, v, type = 'triangle') {
    const o = a.createOscillator(), g = a.createGain(); o.type = type; o.frequency.value = f;
    g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(v, t + .01); g.gain.exponentialRampToValueAtTime(.0001, t + dur);
    o.connect(g).connect(a.destination); o.start(t); o.stop(t + dur + .05);
  }
  // Le dactyle : longue, brève, brève, puis une longue qui reste (la, mi, mi, la).
  function dactyl() { const a = ac(), t = a.currentTime + .03; note(a, t, 220, .55, .22); note(a, t, 440, .4, .05, 'sine'); note(a, t + .3, 329.63, .16, .14); note(a, t + .45, 329.63, .16, .14); note(a, t + .6, 440, 1.1, .16); note(a, t + .6, 220, 1.1, .08, 'sine'); }
  function tick(long) { const a = ac(), t = a.currentTime + .005; note(a, t, long ? 220 : 659.25, long ? .18 : .07, long ? .2 : .1) }
  $$('[data-sound-logo]').forEach(b => b.addEventListener('click', dactyl));

  /* le mètre : chaque lettre longue (125 %) ou brève (75 %) */
  const METERS = { dactyle: 'LSS', trochee: 'LS', iambe: 'SL', anapeste: 'SSL', spondee: 'LL' };
  const SIGNS = { L: '━', S: '◡' };
  function setMeter(word, pat, off) { [...word.children].forEach((s, i) => { const k = pat[(i + off) % pat.length]; s.dataset.q = k }) }
  // Hero
  const hw = $('#heroWord');
  if (hw) {
    let meter = 'dactyle', off = 0, taps = [], snd = false;
    const bpmEl = $('#bpm'), mEl = $$('[data-meter-name]'), sigEl = $('#meterSig');
    const render = () => { setMeter(hw, METERS[meter], off); sigEl.textContent = [...METERS[meter]].map(k => SIGNS[k]).join(' '); mEl.forEach(e => e.hidden = e.dataset.meterName !== meter) };
    render();
    const tap = () => {
      const now = performance.now(); taps.push(now); taps = taps.slice(-5);
      if (taps.length > 1) { const iv = (taps[taps.length - 1] - taps[0]) / (taps.length - 1); const bpm = Math.round(Math.min(220, Math.max(40, 60000 / iv))); bpmEl.textContent = bpm; hw.style.setProperty('--beat', Math.round(Math.min(600, iv * .8)) + 'ms') }
      off = (off + METERS[meter].length - 1) % METERS[meter].length;
      if (!RM.matches) render();
      if (snd) tick(METERS[meter][(off) % METERS[meter].length] === 'L');
    };
    $('#tapBtn').addEventListener('click', e => { e.stopPropagation(); tap() });
    $('#heroStage').addEventListener('click', e => { if (!e.target.closest('button, a')) tap() });
    $$('.mchip').forEach(c => c.addEventListener('click', e => { e.stopPropagation(); meter = c.dataset.m; off = 0; $$('.mchip').forEach(x => x.setAttribute('aria-pressed', x === c)); render() }));
    const sb = $('#soundBtn'); sb.addEventListener('click', e => { e.stopPropagation(); snd = !snd; sb.setAttribute('aria-pressed', snd); $$('[data-s]', sb).forEach(s => s.hidden = (s.dataset.s === 'on') !== snd); if (snd) dactyl() });
  }
  // Spécimen : écrire un mot en mètre
  const inp = $('#meterInput'), out = $('#meterOut'), sel = $('#meterSel');
  if (inp) {
    const draw = () => { out.textContent = ''; [...(inp.value || ' ')].forEach(ch => { const s = document.createElement('span'); s.textContent = ch; out.appendChild(s) }); setMeter(out, METERS[sel.value], 0) };
    inp.addEventListener('input', draw); sel.addEventListener('change', draw); draw();
  }

  /* rejouer le logo */
  $$('[data-replay]').forEach(b => b.addEventListener('click', () => { const el = $(b.dataset.replay); el.classList.remove('play'); void el.getBoundingClientRect(); el.classList.add('play'); if (b.hasAttribute('data-with-sound')) dactyl() }));

  /* formulaire (maquette) */
  const f = $('#briefForm');
  f.addEventListener('submit', e => { e.preventDefault(); if (!f.reportValidity()) return; const st = $('#formState'); st.hidden = false; st.focus() });
})();
