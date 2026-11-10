(function () {
  var root = document.documentElement;
  try { var t = localStorage.getItem('volta-theme'); if (t) root.setAttribute('data-theme', t); } catch (e) {}
  document.getElementById('themeBtn').addEventListener('click', function () {
    var cur = root.getAttribute('data-theme') || (matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark');
    var next = cur === 'light' ? 'dark' : 'light';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('volta-theme', next); } catch (e) {}
  });
  var views = ['identite', 'site'];
  var siteIds = ['poles', 'signature', 'travaux', 'contact'];
  function show() {
    var h = (location.hash || '#identite').slice(1);
    var v = views.indexOf(h) >= 0 ? h : (siteIds.indexOf(h) >= 0 ? 'site' : 'identite');
    views.forEach(function (k) { document.getElementById('v-' + k).hidden = k !== v; });
    document.querySelectorAll('.sw a').forEach(function (a) { var on = a.dataset.v === v; a.classList.toggle('on', on); if (on) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); });
    if (views.indexOf(h) >= 0) window.scrollTo(0, 0);
  }
  window.addEventListener('hashchange', show); show();
  document.getElementById('replay').addEventListener('click', function () {
    var s = document.querySelector('.igs'); var p = s.parentNode; var c = s.cloneNode(true); p.replaceChild(c, s);
  });
  document.getElementById('cf').addEventListener('submit', function (e) {
    e.preventDefault();
    var f = e.target, st = document.getElementById('cf-s');
    if (!f.n.value.trim() || !/\S+@\S+\.\S+/.test(f.e.value)) { st.textContent = 'Indiquez votre nom et une adresse e-mail valide.'; (f.n.value.trim() ? f.e : f.n).focus(); return; }
    st.textContent = 'Maquette : le message n’est pas envoyé. Sur le site réel, il partira vers l’équipe.';
  });
})();
