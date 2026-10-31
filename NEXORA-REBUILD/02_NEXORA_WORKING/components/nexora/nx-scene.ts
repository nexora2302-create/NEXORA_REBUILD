/*
 * Scène 3D du hero, « le X en fusion ».
 * Deux rubans de matière qui se croisent en X : laque d'encre à l'extérieur, braise
 * qui luit sur les tranches et pulse le long des rubans. Entrée : le X se déplie et
 * s'allume ; ensuite il respire, s'oriente vers le pointeur et pivote au scroll.
 * Fond transparent : le mot NEXORA (DOM) passe derrière.
 * Chargée à la demande (import dynamique), en pause hors écran, qualité adaptative.
 */
import * as THREE from 'three'
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js'

const RINGS = 200 // anneaux le long du ruban
const SIDES = 56 // points de la section
const L = 330 // longueur
const W = 62 // largeur
const T = 15 // épaisseur

const clamp01 = (v: number) => Math.min(1, Math.max(0, v))
const easeOut = (t: number) => 1 - Math.pow(1 - t, 4)

/* Section : rectangle aux angles très arrondis (superellipse). */
const SECTION = Array.from({ length: SIDES }, (_, i) => {
  const a = (i / SIDES) * Math.PI * 2
  const c = Math.cos(a)
  const s = Math.sin(a)
  const x = (W / 2) * Math.sign(c) * Math.pow(Math.abs(c), 0.5)
  const z = (T / 2) * Math.sign(s) * Math.pow(Math.abs(s), 0.5)
  // Les tranches (bords fins) portent la braise.
  const side = Math.pow(Math.abs(c), 6)
  return { x, z, side }
})

type Ribbon = {
  mesh: THREE.Mesh
  pos: Float32Array
  phase: number
  twist: number
  bend: number
}

function makeRibbon(material: THREE.Material, phase: number, twist: number, bend: number): Ribbon {
  const count = RINGS * SIDES
  const pos = new Float32Array(count * 3)
  const along = new Float32Array(count)
  const side = new Float32Array(count)
  for (let r = 0; r < RINGS; r++) {
    for (let k = 0; k < SIDES; k++) {
      along[r * SIDES + k] = r / (RINGS - 1)
      side[r * SIDES + k] = SECTION[k].side
    }
  }
  const index: number[] = []
  for (let r = 0; r < RINGS - 1; r++) {
    for (let k = 0; k < SIDES; k++) {
      const a = r * SIDES + k
      const b = r * SIDES + ((k + 1) % SIDES)
      const c = (r + 1) * SIDES + k
      const d = (r + 1) * SIDES + ((k + 1) % SIDES)
      index.push(a, c, b, b, c, d)
    }
  }
  const geo = new THREE.BufferGeometry()
  geo.setAttribute('position', new THREE.BufferAttribute(pos, 3).setUsage(THREE.DynamicDrawUsage))
  geo.setAttribute('aT', new THREE.BufferAttribute(along, 1))
  geo.setAttribute('aSide', new THREE.BufferAttribute(side, 1))
  geo.setIndex(index)
  const mesh = new THREE.Mesh(geo, material)
  mesh.frustumCulled = false
  return { mesh, pos, phase, twist, bend }
}

/* Déforme le ruban : ligne centrale courbe, torsion qui ondule, extrémités effilées. */
function shapeRibbon(rb: Ribbon, time: number, unfold: number) {
  const { pos, phase, twist, bend } = rb
  for (let r = 0; r < RINGS; r++) {
    const t = r / (RINGS - 1)
    const s = t - 0.5
    const y = L * s * (0.35 + 0.65 * unfold)
    const cx = bend * Math.sin(Math.PI * t * 1.1 + phase) * unfold + Math.sin(time * 0.7 + t * 5 + phase) * 4
    const cz = 18 * Math.sin(Math.PI * 2 * t + phase + time * 0.5)
    const theta = (twist * s + 0.35 * Math.sin(time * 0.9 + t * 4.2 + phase)) * unfold
    const cos = Math.cos(theta)
    const sin = Math.sin(theta)
    const taper = 0.1 + 0.9 * Math.pow(Math.sin(Math.PI * t), 0.4)
    const breathe = 1 + 0.04 * Math.sin(time * 1.3 + t * 6 + phase)
    for (let k = 0; k < SIDES; k++) {
      const p = SECTION[k]
      const lx = p.x * taper * breathe
      const lz = p.z * taper
      const i = (r * SIDES + k) * 3
      pos[i] = cx + lx * cos - lz * sin
      pos[i + 1] = y
      pos[i + 2] = cz + lx * sin + lz * cos
    }
  }
  const geo = rb.mesh.geometry
  geo.attributes.position.needsUpdate = true
  geo.computeVertexNormals()
}

export function mountNxScene(canvas: HTMLCanvasElement, opts: { reduced: boolean; force?: boolean; intro?: boolean }) {
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, premultipliedAlpha: false, preserveDrawingBuffer: !!opts.force })
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.75))
  renderer.setClearColor(0x000000, 0)
  renderer.outputColorSpace = THREE.SRGBColorSpace
  renderer.toneMapping = THREE.ACESFilmicToneMapping
  renderer.toneMappingExposure = 1.05

  // Sans carte graphique (rendu logiciel), une seule image : l'animer bloquerait la page.
  const gl = renderer.getContext()
  const dbg = gl.getExtension('WEBGL_debug_renderer_info')
  const gpu = dbg ? String(gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL)) : ''
  const software = /swiftshader|llvmpipe|softpipe|software|basic render/i.test(gpu)
  let still = opts.reduced || software

  const scene = new THREE.Scene()
  const pmrem = new THREE.PMREMGenerator(renderer)
  const env = pmrem.fromScene(new RoomEnvironment(), 0.03).texture
  scene.environment = env

  const camera = new THREE.PerspectiveCamera(30, 0.8, 10, 3000)
  camera.position.set(0, 0, 640)

  scene.add(new THREE.AmbientLight(0xffffff, 0.1))
  const key = new THREE.DirectionalLight(0xf4efe8, 1.6)
  key.position.set(-260, 320, 300)
  scene.add(key)
  const rim = new THREE.PointLight(0xff4a1c, 160000, 1400, 1.6)
  rim.position.set(220, -120, -260)
  scene.add(rim)
  const under = new THREE.PointLight(0xff6a2a, 26000, 900, 1.6)
  under.position.set(-60, -300, 160)
  scene.add(under)

  // Laque d'encre, avec la braise ajoutée en émission (tranches + pulsation le long du ruban).
  const uniforms = { uTime: { value: 0 }, uGlow: { value: 0 } }
  const lacquer = new THREE.MeshPhysicalMaterial({
    color: 0x0c0a09,
    roughness: 0.2,
    metalness: 0.05,
    clearcoat: 1,
    clearcoatRoughness: 0.05,
    envMapIntensity: 0.85,
    side: THREE.DoubleSide,
  })
  lacquer.onBeforeCompile = (shader) => {
    shader.uniforms.uTime = uniforms.uTime
    shader.uniforms.uGlow = uniforms.uGlow
    shader.vertexShader = shader.vertexShader
      .replace('#include <common>', '#include <common>\nattribute float aT;\nattribute float aSide;\nvarying float vT;\nvarying float vSide;')
      .replace('#include <begin_vertex>', '#include <begin_vertex>\nvT = aT;\nvSide = aSide;')
    shader.fragmentShader = shader.fragmentShader
      .replace('#include <common>', '#include <common>\nuniform float uTime;\nuniform float uGlow;\nvarying float vT;\nvarying float vSide;')
      .replace(
        '#include <emissivemap_fragment>',
        `#include <emissivemap_fragment>
        float wave = pow(0.5 + 0.5 * sin(vT * 11.0 - uTime * 1.7), 4.0);
        float ends = smoothstep(0.0, 0.12, vT) * smoothstep(1.0, 0.88, vT);
        float g = (vSide * (0.9 + 1.4 * wave) + wave * 0.12) * ends * uGlow;
        totalEmissiveRadiance += vec3(1.0, 0.29, 0.11) * g * 2.2;`,
      )
  }

  const rig = new THREE.Group()
  scene.add(rig)
  const a = makeRibbon(lacquer, 0, 3.4, 26)
  const b = makeRibbon(lacquer, 2.1, -3.0, -22)
  const armA = new THREE.Group()
  const armB = new THREE.Group()
  armA.add(a.mesh)
  armB.add(b.mesh)
  armA.rotation.z = -0.68
  armB.rotation.z = 0.68
  armA.position.z = 8
  armB.position.z = -8
  rig.add(armA, armB)

  // Cadrage : le X tient dans son cadre, quel que soit le format.
  const resize = () => {
    const r = canvas.getBoundingClientRect()
    const w = Math.max(1, r.width)
    const h = Math.max(1, r.height)
    renderer.setSize(w, h, false)
    camera.aspect = w / h
    const fit = Math.max(1, 0.82 / camera.aspect)
    camera.position.z = 640 * fit
    camera.updateProjectionMatrix()
  }
  resize()

  const target = { x: 0, y: 0 }
  const look = { x: 0, y: 0 }
  const onPointer = (e: PointerEvent) => {
    if (e.pointerType !== 'mouse') return
    target.x = (e.clientX / window.innerWidth) * 2 - 1
    target.y = (e.clientY / window.innerHeight) * 2 - 1
  }
  window.addEventListener('pointermove', onPointer, { passive: true })

  let scrollP = 0
  const onScroll = () => {
    scrollP = clamp01(window.scrollY / (window.innerHeight || 1))
  }
  onScroll()
  window.addEventListener('scroll', onScroll, { passive: true })

  const start = performance.now()
  let raf = 0
  let running = false
  let sScroll = 0

  const frame = (now: number) => {
    const t = still ? 4 : (now - start) / 1000
    const skip = still || opts.intro === false
    const unfold = skip ? 1 : easeOut(clamp01((t - 0.35) / 2))
    const glow = skip ? 1 : clamp01((t - 0.9) / 1.6)

    shapeRibbon(a, t, unfold)
    shapeRibbon(b, t, unfold)
    uniforms.uTime.value = t
    uniforms.uGlow.value = glow * (0.85 + 0.15 * Math.sin(t * 1.6))

    look.x += (target.x - look.x) * 0.045
    look.y += (target.y - look.y) * 0.045
    sScroll += (scrollP - sScroll) * 0.1
    rig.rotation.y = Math.sin(t * 0.32) * 0.28 + look.x * 0.35 + sScroll * Math.PI * 0.5
    rig.rotation.x = Math.sin(t * 0.45) * 0.08 + look.y * 0.25 - sScroll * 0.2
    rig.rotation.z = Math.sin(t * 0.25) * 0.05
    rig.scale.setScalar(0.35 + 0.65 * unfold)

    const t0 = performance.now()
    renderer.render(scene, camera)
    adapt(performance.now() - t0, now)
    if (running && !still) raf = requestAnimationFrame(frame)
  }

  // Qualité adaptative : résolution réduite, puis image fixe si l'appareil peine.
  let samples = 0
  let slow = 0
  let level = 0
  let last = 0
  function adapt(renderMs: number, now: number) {
    const gap = last ? now - last : 16
    last = now
    if (still) return
    samples++
    if (renderMs > 22 || gap > 50) slow++
    if (samples < 40) return
    if (slow > 16) {
      level++
      if (level === 1) {
        renderer.setPixelRatio(1)
        resize()
      } else {
        still = true
        requestAnimationFrame(() => frame(start))
      }
    }
    samples = 0
    slow = 0
  }

  const ro = new ResizeObserver(() => {
    resize()
    if (still) frame(start)
  })
  ro.observe(canvas)

  const play = () => {
    if (running) return
    running = true
    raf = requestAnimationFrame(frame)
  }
  const pause = () => {
    running = false
    cancelAnimationFrame(raf)
  }
  const io = new IntersectionObserver(([e]) => (e.isIntersecting ? play() : pause()))
  if (still) frame(start)
  else io.observe(canvas)

  return () => {
    pause()
    io.disconnect()
    ro.disconnect()
    window.removeEventListener('pointermove', onPointer)
    window.removeEventListener('scroll', onScroll)
    a.mesh.geometry.dispose()
    b.mesh.geometry.dispose()
    lacquer.dispose()
    env.dispose()
    pmrem.dispose()
    renderer.dispose()
  }
}
