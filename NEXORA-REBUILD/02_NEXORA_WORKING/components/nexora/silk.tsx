'use client'

import { useEffect, useRef } from 'react'

/*
 * Fond « soie » : plis d'encre traversés par une lumière braise.
 * WebGL brut (aucune dépendance), rendu à demi-résolution, en pause hors écran,
 * une seule image fixe si l'utilisateur réduit les animations.
 */

const VERT = `
attribute vec2 p;
void main() { gl_Position = vec4(p, 0.0, 1.0); }
`

const FRAG = `
precision mediump float;
uniform vec2 uRes;
uniform float uTime;
uniform vec2 uMouse;

void main() {
  vec2 uv = gl_FragCoord.xy / uRes;
  float aspect = uRes.x / uRes.y;
  vec2 q = vec2(uv.x * aspect, uv.y);

  float a = -0.62;
  mat2 R = mat2(cos(a), -sin(a), sin(a), cos(a));
  vec2 tex = R * q * 1.9;
  float t = uTime * 0.32;

  tex.y += 0.07 * sin(5.0 * tex.x - t);
  tex.x += 0.05 * sin(3.0 * tex.y + t * 0.6);
  float s = sin(5.0 * (tex.x + tex.y + cos(3.0 * tex.x + 5.0 * tex.y) + 0.02 * t)
              + sin(12.0 * (tex.x + tex.y - 0.07 * t)));
  float pattern = 0.5 + 0.5 * s;
  float fold = pattern * pattern * pattern;

  // La couleur vit en bas à droite ; le haut gauche reste encre pour le texte.
  float band = smoothstep(0.2, 1.05, uv.x * 0.85 + (1.0 - uv.y) * 0.55);
  vec2 m = vec2(uMouse.x * aspect, uMouse.y);
  float d = length(q - m);
  float glow = exp(-5.0 * d * d);

  vec3 ink = vec3(0.051, 0.047, 0.043);
  vec3 rust = vec3(0.36, 0.10, 0.04);
  vec3 ember = vec3(1.0, 0.29, 0.11);
  vec3 bone = vec3(0.925, 0.898, 0.847);

  vec3 col = ink;
  col = mix(col, rust, fold * (0.25 + 0.75 * band) * (0.75 + 0.5 * glow));
  col = mix(col, ember, pow(pattern, 10.0) * band * (0.42 + 0.48 * glow));
  col += bone * pow(pattern, 30.0) * band * 0.12;

  float v = smoothstep(1.3, 0.2, length(uv - vec2(0.6, 0.4)));
  col *= mix(0.45, 1.0, v);
  gl_FragColor = vec4(col, 1.0);
}
`

function compile(gl: WebGLRenderingContext, type: number, src: string) {
  const s = gl.createShader(type)
  if (!s) return null
  gl.shaderSource(s, src)
  gl.compileShader(s)
  return gl.getShaderParameter(s, gl.COMPILE_STATUS) ? s : null
}

export function Silk({ className = '' }: { className?: string }) {
  const ref = useRef<HTMLCanvasElement>(null)

  useEffect(() => {
    // Démarre après le chargement pour ne pas concurrencer l'hydratation.
    let cleanup: (() => void) | undefined
    const ric = window.requestIdleCallback ?? ((cb: () => void) => window.setTimeout(cb, 300))
    const cancel = window.cancelIdleCallback ?? window.clearTimeout
    const id = ric(() => {
      cleanup = setup()
    })
    return () => {
      cancel(id)
      cleanup?.()
    }
  }, [])

  const setup = () => {
    const canvas = ref.current
    if (!canvas) return
    const gl = canvas.getContext('webgl', { antialias: false, alpha: false, powerPreference: 'low-power' })
    if (!gl) return

    const vs = compile(gl, gl.VERTEX_SHADER, VERT)
    const fs = compile(gl, gl.FRAGMENT_SHADER, FRAG)
    const prog = gl.createProgram()
    if (!vs || !fs || !prog) return
    gl.attachShader(prog, vs)
    gl.attachShader(prog, fs)
    gl.linkProgram(prog)
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) return
    gl.useProgram(prog)

    const buf = gl.createBuffer()
    gl.bindBuffer(gl.ARRAY_BUFFER, buf)
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW)
    const loc = gl.getAttribLocation(prog, 'p')
    gl.enableVertexAttribArray(loc)
    gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0)

    const uRes = gl.getUniformLocation(prog, 'uRes')
    const uTime = gl.getUniformLocation(prog, 'uTime')
    const uMouse = gl.getUniformLocation(prog, 'uMouse')

    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    const coarse = window.matchMedia('(pointer: coarse)').matches
    const scale = coarse ? 0.4 : 0.55
    const mouse = { x: 0.72, y: 0.35, tx: 0.72, ty: 0.35 }

    const resize = () => {
      const w = Math.max(1, Math.round(canvas.clientWidth * scale))
      const h = Math.max(1, Math.round(canvas.clientHeight * scale))
      if (canvas.width !== w || canvas.height !== h) {
        canvas.width = w
        canvas.height = h
        gl.viewport(0, 0, w, h)
      }
      gl.uniform2f(uRes, w, h)
    }

    let raf = 0
    let visible = true
    let last = 0
    const start = performance.now()
    const frameGap = coarse ? 1000 / 30 : 0

    const draw = (now: number) => {
      raf = 0
      if (now - last >= frameGap) {
        last = now
        mouse.x += (mouse.tx - mouse.x) * 0.05
        mouse.y += (mouse.ty - mouse.y) * 0.05
        gl.uniform1f(uTime, (now - start) / 1000 + 8)
        gl.uniform2f(uMouse, mouse.x, mouse.y)
        gl.drawArrays(gl.TRIANGLES, 0, 3)
      }
      if (visible && !reduced && !document.hidden) raf = requestAnimationFrame(draw)
    }
    const play = () => {
      if (!raf && visible && !reduced && !document.hidden) raf = requestAnimationFrame(draw)
    }

    const onMove = (e: PointerEvent) => {
      const r = canvas.getBoundingClientRect()
      mouse.tx = (e.clientX - r.left) / r.width
      mouse.ty = 1 - (e.clientY - r.top) / r.height
    }

    resize()
    gl.uniform1f(uTime, 8)
    gl.uniform2f(uMouse, mouse.x, mouse.y)
    gl.drawArrays(gl.TRIANGLES, 0, 3)

    const io = new IntersectionObserver(([entry]) => {
      visible = !!entry?.isIntersecting
      play()
    })
    io.observe(canvas)
    const ro = new ResizeObserver(() => {
      resize()
      if (reduced) gl.drawArrays(gl.TRIANGLES, 0, 3)
    })
    ro.observe(canvas)
    const onVis = () => play()
    document.addEventListener('visibilitychange', onVis)
    if (!coarse) window.addEventListener('pointermove', onMove, { passive: true })
    play()

    return () => {
      cancelAnimationFrame(raf)
      io.disconnect()
      ro.disconnect()
      document.removeEventListener('visibilitychange', onVis)
      window.removeEventListener('pointermove', onMove)
    }
  }

  return <canvas ref={ref} aria-hidden className={`block h-full w-full ${className}`} />
}
