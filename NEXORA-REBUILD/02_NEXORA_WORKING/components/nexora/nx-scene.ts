/*
 * Scène 3D du hero, « la braise qui monte ».
 * Un sol de dalles d'encre, un chemin d'os, des marches qui s'élèvent vers la droite
 * et le monogramme NX dressé au sommet. Une braise roule sur le chemin, gravit les
 * marches une à une et rejoint le NX, en éclairant tout ce qu'elle frôle. Boucle.
 * Projecteur avec ombres douces, brouillard d'encre, légère parallaxe au pointeur.
 * Chargée à la demande (import dynamique), en pause hors écran.
 */
import * as THREE from 'three'
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js'

type Pt = [number, number]

// Mêmes tracés que le logo (components/nexora/logo.tsx), en points absolus.
const N_PTS: Pt[] = [
  [0, 0], [15, 0], [39, 38], [39, 0], [53, 0], [53, 64], [38, 64], [15, 26], [15, 64], [0, 64],
]
const X_PTS: Pt[] = [
  [59, 0], [75, 0], [86.5, 20], [98, 0], [114, 0], [94.5, 31.5], [115, 64], [99, 64],
  [86.5, 43], [74, 64], [58, 64], [78.5, 31.5],
]

function letter(pts: Pt[], material: THREE.Material) {
  const shape = new THREE.Shape()
  pts.forEach(([x, y], i) => (i === 0 ? shape.moveTo(x - 57.5, 64 - y) : shape.lineTo(x - 57.5, 64 - y)))
  shape.closePath()
  const geo = new THREE.ExtrudeGeometry(shape, {
    depth: 14,
    bevelEnabled: true,
    bevelThickness: 1.6,
    bevelSize: 1.2,
    bevelSegments: 4,
    curveSegments: 1,
  })
  geo.translate(0, 0, -7)
  const m = new THREE.Mesh(geo, material)
  m.castShadow = true
  m.receiveShadow = true
  return m
}

// Géométrie de la scène (unités monde)
const TILE = 40
const GAP = 1.6
const R = 8 // rayon de la braise
const STEPS = [22, 46, 70, 94, 118] // hauteur des marches
const STEP_X0 = 20 // bord gauche de la première marche
const PATH_START = -300
const LOOP = 7.5 // secondes

const easeInOut = (t: number) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2)
const clamp01 = (v: number) => Math.min(1, Math.max(0, v))

/* Trajet de la braise : position (x, y) et visibilité selon la phase 0 → 1 de la boucle. */
function trajectory(phase: number) {
  // 0.00–0.08 : apparition ; 0.08–0.42 : roule sur le chemin ;
  // 0.42–0.86 : saute de marche en marche ; 0.86–1 : se pose au pied du NX et s'éteint.
  const groundEnd = STEP_X0 - R - 2
  let x: number
  let y = R
  if (phase < 0.42) {
    const t = easeInOut(clamp01(phase / 0.42))
    x = PATH_START + (groundEnd - PATH_START) * t
  } else if (phase < 0.86) {
    const k = (phase - 0.42) / 0.44
    const n = STEPS.length
    const seg = Math.min(n - 1, Math.floor(k * n))
    const t = easeInOut(k * n - seg)
    const fromX = seg === 0 ? groundEnd : STEP_X0 + (seg - 1) * TILE + TILE / 2
    const toX = STEP_X0 + seg * TILE + TILE / 2
    const fromY = (seg === 0 ? 0 : STEPS[seg - 1]) + R
    const toY = STEPS[seg] + R
    x = fromX + (toX - fromX) * t
    y = fromY + (toY - fromY) * t + Math.sin(Math.PI * t) * 22
  } else {
    x = STEP_X0 + (STEPS.length - 1) * TILE + TILE / 2
    y = STEPS[STEPS.length - 1] + R
  }
  const appear = clamp01(phase / 0.08)
  const fade = 1 - clamp01((phase - 0.9) / 0.1)
  return { x, y, s: Math.min(appear, fade) }
}

export function mountNxScene(canvas: HTMLCanvasElement, opts: { reduced: boolean }) {
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, powerPreference: 'high-performance' })
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5))
  renderer.outputColorSpace = THREE.SRGBColorSpace
  renderer.toneMapping = THREE.ACESFilmicToneMapping
  renderer.toneMappingExposure = 1.1
  renderer.shadowMap.enabled = true
  renderer.shadowMap.type = THREE.PCFSoftShadowMap

  // Sans carte graphique (rendu logiciel), la scène s'affiche en une image fixe :
  // l'animer bloquerait la page sur les appareils modestes.
  const gl = renderer.getContext()
  const dbg = gl.getExtension('WEBGL_debug_renderer_info')
  const gpu = dbg ? String(gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL)) : ''
  const software = /swiftshader|llvmpipe|softpipe|software|basic render/i.test(gpu)
  let still = opts.reduced || software

  const INK = 0x0d0c0b
  const scene = new THREE.Scene()
  scene.background = new THREE.Color(INK)
  scene.fog = new THREE.Fog(INK, 600, 1300)
  const pmrem = new THREE.PMREMGenerator(renderer)
  const env = pmrem.fromScene(new RoomEnvironment(), 0.04).texture
  scene.environment = env
  scene.environmentIntensity = 0.18

  const camera = new THREE.PerspectiveCamera(26, 1, 10, 3000)
  const lookAt = new THREE.Vector3()

  // ---------- Matières ----------
  const slab = new THREE.MeshStandardMaterial({ color: 0x1b1815, roughness: 0.82, metalness: 0 })
  const path = new THREE.MeshStandardMaterial({ color: 0xd9d1c3, roughness: 0.55, metalness: 0 })
  const stone = new THREE.MeshPhysicalMaterial({ color: 0x24201c, roughness: 0.35, metalness: 0.1, clearcoat: 0.8, clearcoatRoughness: 0.25 })
  const stoneTop = new THREE.MeshPhysicalMaterial({ color: 0xe6dfd2, roughness: 0.45, clearcoat: 0.4 })
  const bone = new THREE.MeshPhysicalMaterial({ color: 0xece5d8, roughness: 0.32, clearcoat: 0.7, clearcoatRoughness: 0.2 })
  const ember = new THREE.MeshPhysicalMaterial({
    color: 0xff4a1c,
    roughness: 0.28,
    clearcoat: 1,
    clearcoatRoughness: 0.1,
    emissive: 0xe0360c,
    emissiveIntensity: 0.4,
    envMapIntensity: 0.6,
  })
  const coal = new THREE.MeshBasicMaterial({ color: 0xff4a1c, toneMapped: false })

  // ---------- Sol de dalles (instancié) ----------
  const COLS = 22
  const ROWS = 16
  const slabGeo = new THREE.BoxGeometry(TILE - GAP, 6, TILE - GAP)
  const slabs = new THREE.InstancedMesh(slabGeo, slab, COLS * ROWS)
  slabs.receiveShadow = true
  const m4 = new THREE.Matrix4()
  let idx = 0
  for (let i = 0; i < COLS; i++) {
    for (let j = 0; j < ROWS; j++) {
      const x = -460 + i * TILE + TILE / 2
      const z = -320 + j * TILE + TILE / 2
      m4.makeTranslation(x, -3 - (((i * 7 + j * 13) % 5) === 0 ? 1.2 : 0), z)
      slabs.setMatrixAt(idx++, m4)
    }
  }
  scene.add(slabs)

  // ---------- Chemin d'os ----------
  const pathGeo = new THREE.BoxGeometry(TILE - GAP, 6, TILE - GAP)
  const pathCount = Math.ceil((STEP_X0 - PATH_START) / TILE) + 2
  const pathMesh = new THREE.InstancedMesh(pathGeo, path, pathCount)
  pathMesh.receiveShadow = true
  for (let i = 0; i < pathCount; i++) {
    m4.makeTranslation(STEP_X0 - TILE / 2 - i * TILE, -2.4, 0)
    pathMesh.setMatrixAt(i, m4)
  }
  scene.add(pathMesh)

  // ---------- Marches ----------
  STEPS.forEach((hgt, i) => {
    const g = new THREE.BoxGeometry(TILE - GAP, hgt, TILE * 1.6)
    const block = new THREE.Mesh(g, [stone, stone, stoneTop, stone, stone, stone])
    block.position.set(STEP_X0 + i * TILE + TILE / 2, hgt / 2, 0)
    block.castShadow = true
    block.receiveShadow = true
    scene.add(block)
  })

  // ---------- Socle et monogramme ----------
  const topH = STEPS[STEPS.length - 1]
  const plinthX = STEP_X0 + STEPS.length * TILE + 46
  const plinth = new THREE.Mesh(new THREE.BoxGeometry(92 - GAP, topH + 14, 92), [stone, stone, stoneTop, stone, stone, stone])
  plinth.position.set(plinthX, (topH + 14) / 2, -10)
  plinth.castShadow = true
  plinth.receiveShadow = true
  scene.add(plinth)

  const nx = new THREE.Group()
  nx.add(letter(N_PTS, bone), letter(X_PTS, ember))
  nx.scale.setScalar(0.95)
  nx.position.set(plinthX, topH + 14, -10)
  nx.rotation.y = -0.62
  scene.add(nx)

  // ---------- Braise ----------
  const coalMesh = new THREE.Mesh(new THREE.SphereGeometry(R, 48, 48), coal)
  coalMesh.castShadow = false
  scene.add(coalMesh)
  // Halo : un sprite additif au dégradé radial, dessiné une fois dans un canvas.
  const haloCanvas = document.createElement('canvas')
  haloCanvas.width = haloCanvas.height = 128
  const hc = haloCanvas.getContext('2d')!
  const grad = hc.createRadialGradient(64, 64, 0, 64, 64, 64)
  grad.addColorStop(0, 'rgba(255,120,60,0.9)')
  grad.addColorStop(0.25, 'rgba(255,74,28,0.45)')
  grad.addColorStop(1, 'rgba(255,74,28,0)')
  hc.fillStyle = grad
  hc.fillRect(0, 0, 128, 128)
  const haloTex = new THREE.CanvasTexture(haloCanvas)
  const haloMat = new THREE.SpriteMaterial({ map: haloTex, blending: THREE.AdditiveBlending, depthWrite: false, transparent: true })
  const halo = new THREE.Sprite(haloMat)
  halo.scale.setScalar(R * 7)
  scene.add(halo)
  const glow = new THREE.PointLight(0xff5a24, 2600, 260, 1.7)
  glow.castShadow = false
  scene.add(glow)

  // ---------- Lumières ----------
  scene.add(new THREE.HemisphereLight(0xf2ece2, 0x0d0c0b, 0.55))
  const spot = new THREE.SpotLight(0xfff3e4, 900000, 1600, 0.5, 0.7, 1.7)
  spot.position.set(-140, 560, 320)
  spot.target.position.set(110, 40, 0)
  spot.castShadow = true
  spot.shadow.mapSize.set(1536, 1536)
  spot.shadow.bias = -0.0004
  spot.shadow.radius = 6
  spot.shadow.camera.near = 200
  spot.shadow.camera.far = 1100
  scene.add(spot, spot.target)
  const rim = new THREE.DirectionalLight(0xff6a30, 0.9)
  rim.position.set(400, 120, -300)
  scene.add(rim)

  // ---------- Cadrage ----------
  const base = new THREE.Vector3()
  const resize = () => {
    const r = canvas.getBoundingClientRect()
    const w = Math.max(1, r.width)
    const h = Math.max(1, r.height)
    renderer.setSize(w, h, false)
    camera.aspect = w / h
    // Desktop : la scène glisse à droite, le texte garde la gauche. Portrait : la scène monte.
    if (camera.aspect >= 1) {
      base.set(-360, 250, 600)
      lookAt.set(90, 70, 0)
      camera.fov = 30
      camera.setViewOffset(w, h, -w * 0.17, 0, w, h)
    } else {
      base.set(-430, 300, 780)
      lookAt.set(110, 80, 0)
      camera.fov = 36
      camera.setViewOffset(w, h, w * 0.17, h * 0.17, w, h)
    }
    camera.updateProjectionMatrix()
  }
  resize()
  const ro = new ResizeObserver(() => {
    resize()
    if (still) frame(start + 5000)
  })
  ro.observe(canvas)

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

  // ---------- Boucle ----------
  const start = performance.now()
  let raf = 0
  let running = false
  let sScroll = 0
  let prevX = PATH_START
  let roll = 0

  const frame = (now: number) => {
    const t = (now - start) / 1000
    const intro = still ? 1 : 1 - Math.pow(1 - clamp01(t / 2.2), 3)
    const phase = still ? 0.93 : ((t + LOOP * 0.25) % LOOP) / LOOP

    const p = trajectory(phase)
    const s = still ? 1 : p.s
    coalMesh.position.set(p.x, p.y, 0)
    roll -= (p.x - prevX) / R
    prevX = p.x
    coalMesh.rotation.z = roll
    coalMesh.scale.setScalar(Math.max(0.001, s))
    halo.position.set(p.x, p.y, 0)
    halo.scale.setScalar(R * 7 * Math.max(0.001, s) * (1 + Math.sin(t * 6) * 0.06))
    glow.position.set(p.x, p.y + 6, 0)
    glow.intensity = 2600 * s
    // Le X du monogramme s'embrase quand la braise arrive.
    ember.emissiveIntensity = 0.4 + 0.9 * clamp01((phase - 0.82) / 0.08) * (1 - clamp01((phase - 0.92) / 0.08))

    // Caméra : arrivée en travelling, parallaxe au pointeur, recul au scroll.
    look.x += (target.x - look.x) * 0.04
    look.y += (target.y - look.y) * 0.04
    sScroll += (scrollP - sScroll) * 0.1
    const dolly = 1 + (1 - intro) * 0.35 + sScroll * 0.25
    camera.position.set(
      base.x * dolly + look.x * 40,
      base.y * dolly - look.y * 25 + sScroll * 80,
      base.z * dolly,
    )
    camera.lookAt(lookAt.x, lookAt.y + sScroll * 30, lookAt.z)

    const t0 = performance.now()
    renderer.render(scene, camera)
    adapt(performance.now() - t0, now)
    if (running && !still) raf = requestAnimationFrame(frame)
  }

  // Qualité adaptative : si les images sont lentes, on baisse la résolution et les ombres,
  // et si cela ne suffit pas, la scène se fige sur une image.
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
        renderer.shadowMap.type = THREE.PCFShadowMap
        spot.shadow.mapSize.set(768, 768)
        spot.shadow.map?.dispose()
        spot.shadow.map = null
        resize()
      } else {
        still = true
        requestAnimationFrame(() => frame(start + 5000))
      }
    }
    samples = 0
    slow = 0
  }

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
  if (still) frame(start + 5000)
  else io.observe(canvas)

  return () => {
    pause()
    io.disconnect()
    ro.disconnect()
    window.removeEventListener('pointermove', onPointer)
    window.removeEventListener('scroll', onScroll)
    scene.traverse((o) => {
      if (o instanceof THREE.Mesh) o.geometry.dispose()
    })
    ;[slab, path, stone, stoneTop, bone, ember, coal, haloMat].forEach((m) => m.dispose())
    haloTex.dispose()
    env.dispose()
    pmrem.dispose()
    renderer.dispose()
  }
}
