/* Logo 3D animé : mêmes rubans que la sculpture du hero (three.js r128, build UMD). */
(function () {
  if (!window.THREE) return;
  var T3 = window.THREE;
  var RINGS = 160, SIDES = 48, L = 330, W = 62, TH = 15;
  var SECTION = [];
  for (var i = 0; i < SIDES; i++) {
    var a = (i / SIDES) * Math.PI * 2, c = Math.cos(a), s = Math.sin(a);
    SECTION.push({ x: (W / 2) * Math.sign(c) * Math.pow(Math.abs(c), 0.5), z: (TH / 2) * Math.sign(s) * Math.pow(Math.abs(s), 0.5), side: Math.pow(Math.abs(c), 6) });
  }
  function clamp01(v) { return Math.min(1, Math.max(0, v)); }
  function easeOut(t) { return 1 - Math.pow(1 - t, 4); }

  function makeRibbon(mat, phase, twist, bend) {
    var count = RINGS * SIDES, pos = new Float32Array(count * 3), along = new Float32Array(count), side = new Float32Array(count), index = [];
    for (var r = 0; r < RINGS; r++) for (var k = 0; k < SIDES; k++) { along[r * SIDES + k] = r / (RINGS - 1); side[r * SIDES + k] = SECTION[k].side; }
    for (r = 0; r < RINGS - 1; r++) for (k = 0; k < SIDES; k++) {
      var A = r * SIDES + k, B = r * SIDES + ((k + 1) % SIDES), Cc = (r + 1) * SIDES + k, D = (r + 1) * SIDES + ((k + 1) % SIDES);
      index.push(A, Cc, B, B, Cc, D);
    }
    var geo = new T3.BufferGeometry();
    geo.setAttribute('position', new T3.BufferAttribute(pos, 3));
    geo.setAttribute('aT', new T3.BufferAttribute(along, 1));
    geo.setAttribute('aSide', new T3.BufferAttribute(side, 1));
    geo.setIndex(index);
    var mesh = new T3.Mesh(geo, mat); mesh.frustumCulled = false;
    return { mesh: mesh, pos: pos, phase: phase, twist: twist, bend: bend };
  }
  function shape(rb, time, unfold) {
    var pos = rb.pos;
    for (var r = 0; r < RINGS; r++) {
      var t = r / (RINGS - 1), s = t - 0.5;
      var y = L * s * (0.35 + 0.65 * unfold);
      var cx = rb.bend * Math.sin(Math.PI * t * 1.1 + rb.phase) * unfold + Math.sin(time * 0.7 + t * 5 + rb.phase) * 4;
      var cz = 18 * Math.sin(Math.PI * 2 * t + rb.phase + time * 0.5);
      var th = (rb.twist * s + 0.5 * Math.sin(time * 0.9 + t * 4.2 + rb.phase)) * unfold;
      var co = Math.cos(th), si = Math.sin(th);
      var taper = 0.1 + 0.9 * Math.pow(Math.sin(Math.PI * t), 0.4);
      var br = 1 + 0.04 * Math.sin(time * 1.3 + t * 6 + rb.phase);
      for (var k = 0; k < SIDES; k++) {
        var p = SECTION[k], lx = p.x * taper * br, lz = p.z * taper, i = (r * SIDES + k) * 3;
        pos[i] = cx + lx * co - lz * si; pos[i + 1] = y; pos[i + 2] = cz + lx * si + lz * co;
      }
    }
    rb.mesh.geometry.attributes.position.needsUpdate = true;
    rb.mesh.geometry.computeVertexNormals();
  }

  function mount(canvas, opts) {
    var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var renderer;
    try { renderer = new T3.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true }); } catch (e) { return; }
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.setClearColor(0x000000, 0);
    renderer.outputEncoding = T3.sRGBEncoding;
    renderer.toneMapping = T3.ACESFilmicToneMapping;
    renderer.physicallyCorrectLights = true;

    var scene = new T3.Scene();
    // Environnement de reflets : un grand panneau os en haut à gauche, une bande braise en bas.
    var envScene = new T3.Scene();
    envScene.background = new T3.Color(0x0d0c0b);
    function panel(color, w, h, x, y, z, ry) { var m = new T3.Mesh(new T3.PlaneGeometry(w, h), new T3.MeshBasicMaterial({ color: color, side: T3.DoubleSide })); m.position.set(x, y, z); m.lookAt(0, 0, 0); envScene.add(m); }
    panel(0xcfc7ba, 5, 3, -6, 5, 6); panel(0xff4a1c, 10, 1.2, 4, -4, 3); panel(0x4a1a0c, 8, 3, 6, 2, -6);
    var pmrem = new T3.PMREMGenerator(renderer);
    var env = pmrem.fromScene(envScene, 0.02).texture;
    scene.environment = env;

    var camera = new T3.PerspectiveCamera(30, 1, 10, 3000);
    camera.position.set(0, 0, 640);
    scene.add(new T3.AmbientLight(0xffffff, 0.08));
    var key = new T3.DirectionalLight(0xf4efe8, 1.6); key.position.set(-260, 320, 300); scene.add(key);
    var rim = new T3.PointLight(0xff4a1c, 160000, 1400, 1.6); rim.position.set(220, -120, -260); scene.add(rim);
    var under = new T3.PointLight(0xff6a2a, 26000, 900, 1.6); under.position.set(-60, -300, 160); scene.add(under);

    var uniforms = { uTime: { value: 0 }, uGlow: { value: 0 } };
    var mat = new T3.MeshPhysicalMaterial({ color: opts.color || 0x0c0a09, roughness: 0.2, metalness: 0.05, clearcoat: 1, clearcoatRoughness: 0.05, envMapIntensity: 0.75, side: T3.DoubleSide });
    mat.onBeforeCompile = function (sh) {
      sh.uniforms.uTime = uniforms.uTime; sh.uniforms.uGlow = uniforms.uGlow;
      sh.vertexShader = sh.vertexShader.replace('#include <common>', '#include <common>\nattribute float aT;\nattribute float aSide;\nvarying float vT;\nvarying float vSide;')
        .replace('#include <begin_vertex>', '#include <begin_vertex>\nvT = aT;\nvSide = aSide;');
      sh.fragmentShader = sh.fragmentShader.replace('#include <common>', '#include <common>\nuniform float uTime;\nuniform float uGlow;\nvarying float vT;\nvarying float vSide;')
        .replace('#include <emissivemap_fragment>', '#include <emissivemap_fragment>\nfloat wave = pow(0.5 + 0.5 * sin(vT * 11.0 - uTime * 1.7), 4.0);\nfloat ends = smoothstep(0.0, 0.12, vT) * smoothstep(1.0, 0.88, vT);\nfloat g = (vSide * (0.9 + 1.4 * wave) + wave * 0.12) * ends * uGlow;\ntotalEmissiveRadiance += vec3(1.0, 0.29, 0.11) * g * 2.2;');
    };
    var rig = new T3.Group(); scene.add(rig);
    var a = makeRibbon(mat, 0, 3.4, 26), b = makeRibbon(mat, 2.1, -3.0, -22);
    var armA = new T3.Group(), armB = new T3.Group();
    armA.add(a.mesh); armB.add(b.mesh); armA.rotation.z = -0.68; armB.rotation.z = 0.68; armA.position.z = 8; armB.position.z = -8;
    rig.add(armA, armB);

    function resize() {
      var r = canvas.getBoundingClientRect(), w = Math.max(1, r.width), h = Math.max(1, r.height);
      renderer.setSize(w, h, false); camera.aspect = w / h;
      camera.position.z = 640 * Math.max(1, 0.85 / camera.aspect) * (opts.zoom || 1);
      camera.updateProjectionMatrix();
    }
    resize();
    if (window.ResizeObserver) new ResizeObserver(resize).observe(canvas);

    var target = { x: 0, y: 0 }, look = { x: 0, y: 0 };
    canvas.parentElement.addEventListener('pointermove', function (e) {
      var r = canvas.getBoundingClientRect();
      target.x = ((e.clientX - r.left) / r.width) * 2 - 1; target.y = ((e.clientY - r.top) / r.height) * 2 - 1;
    });
    canvas.parentElement.addEventListener('pointerleave', function () { target.x = 0; target.y = 0; });

    var start = performance.now(), running = false, raf = 0;
    function frame(now) {
      var t = reduced ? 4 : (now - start) / 1000;
      var unfold = reduced ? 1 : easeOut(clamp01((t - 0.2) / 1.8));
      var glow = reduced ? 1 : clamp01((t - 0.6) / 1.4);
      shape(a, t, unfold); shape(b, t, unfold);
      uniforms.uTime.value = t; uniforms.uGlow.value = glow * (0.85 + 0.15 * Math.sin(t * 1.6));
      look.x += (target.x - look.x) * 0.05; look.y += (target.y - look.y) * 0.05;
      var cyc = (((t - 2.2) % 9) + 9) % 9, k = t < 2.2 ? 0 : clamp01(cyc / 1.9);
      var spin = k < 0.5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2;
      rig.rotation.y = Math.sin(t * 0.32) * 0.28 + look.x * 0.45 + spin * Math.PI * 2;
      rig.rotation.x = Math.sin(t * 0.45) * 0.08 + look.y * 0.3;
      rig.scale.setScalar(0.35 + 0.65 * unfold);
      renderer.render(scene, camera);
      if (running && !reduced) raf = requestAnimationFrame(frame);
    }
    var io = new IntersectionObserver(function (en) {
      if (en[0].isIntersecting) { if (!running) { running = true; raf = requestAnimationFrame(frame); } }
      else { running = false; cancelAnimationFrame(raf); }
    });
    io.observe(canvas);
    frame(start);
    canvas.classList.add('on');
    var fb = canvas.parentElement.querySelector('.stage-fallback'); if (fb) fb.style.visibility = 'hidden';
  }
  document.querySelectorAll('canvas[data-x3d]').forEach(function (cv) {
    mount(cv, { color: parseInt(cv.dataset.color || '0c0a09', 16), zoom: parseFloat(cv.dataset.zoom || '1') });
  });
})();
