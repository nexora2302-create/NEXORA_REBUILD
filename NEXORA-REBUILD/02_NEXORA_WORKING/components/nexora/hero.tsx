'use client'

import { useEffect, useRef, useState } from 'react'
import { ArrowIcon } from './icons'
import { LocalTime } from './local-time'

const LETTERS = ['N', 'E', 'X', 'O', 'R', 'A']
const VERBS = ['les marques', 'les images', 'le web', 'les idées']

export function Hero() {
  const sectionRef = useRef<HTMLElement>(null)
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const [ready, setReady] = useState(false)

  // Progression de sortie du hero (0 → 1), transform/opacité uniquement.
  useEffect(() => {
    const el = sectionRef.current
    if (!el || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
    let raf = 0
    const update = () => {
      raf = 0
      const p = Math.min(1, Math.max(0, window.scrollY / (el.offsetHeight || 1)))
      el.style.setProperty('--p', p.toFixed(4))
    }
    const onScroll = () => {
      if (!raf) raf = requestAnimationFrame(update)
    }
    update()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => {
      window.removeEventListener('scroll', onScroll)
      cancelAnimationFrame(raf)
    }
  }, [])

  // Scène 3D chargée après le premier rendu (import dynamique, hors du chemin critique).
  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    let dispose: (() => void) | undefined
    let cancelled = false
    // Mouvement réduit ou rendu logiciel (pas de carte graphique) : l'affiche suffit.
    // ?scene force le rendu (fabrication de l'affiche).
    const force = new URLSearchParams(window.location.search).has('scene')
    if (!force && (window.matchMedia('(prefers-reduced-motion: reduce)').matches || !hasHardwareGL())) return
    const start = () =>
      import('./nx-scene').then(({ mountNxScene }) => {
        if (cancelled) return
        try {
          dispose = mountNxScene(canvas, { reduced: false, force })
          setReady(true)
        } catch {
          /* WebGL indisponible : le hero reste lisible sans la pièce */
        }
      })
    const ric = (window as Window & { requestIdleCallback?: (cb: () => void, o?: { timeout: number }) => number }).requestIdleCallback
    const id = ric ? ric(start, { timeout: 1200 }) : window.setTimeout(start, 300)
    return () => {
      cancelled = true
      if (!ric) clearTimeout(id)
      dispose?.()
    }
  }, [])

  // Les lettres s'élargissent près du pointeur (souris uniquement).
  const lettersRef = useRef<(HTMLSpanElement | null)[]>([])
  const handleMove = (e: React.PointerEvent) => {
    if (e.pointerType !== 'mouse') return
    const range = window.innerWidth * 0.28
    lettersRef.current.forEach((letter) => {
      if (!letter) return
      const r = letter.getBoundingClientRect()
      const k = Math.max(0, 1 - Math.abs(e.clientX - (r.left + r.width / 2)) / range)
      const eased = k * k * (3 - 2 * k)
      letter.style.setProperty('--wdth', String(100 + eased * 10))
      letter.style.setProperty('--wght', String(800 + eased * 80))
    })
  }
  const handleLeave = () =>
    lettersRef.current.forEach((l) => {
      l?.style.removeProperty('--wdth')
      l?.style.removeProperty('--wght')
    })

  return (
    <section
      id="top"
      ref={sectionRef}
      onPointerMove={handleMove}
      onPointerLeave={handleLeave}
      className="relative isolate flex min-h-svh flex-col overflow-hidden"
      style={{ '--p': 0 } as React.CSSProperties}
    >
      {/* Chaleur sous la sculpture */}
      <div
        aria-hidden
        className="absolute inset-0 -z-20 bg-[radial-gradient(ellipse_42%_50%_at_50%_86%,rgb(122_36_16/0.55),transparent_70%)] max-md:bg-[radial-gradient(ellipse_75%_30%_at_50%_45%,rgb(122_36_16/0.5),transparent_70%)]"
      />

      {/* Le mot, derrière la sculpture ; il s'écarte au scroll */}
      <h1
        aria-label="NEXORA"
        className="absolute inset-x-0 top-[27svh] z-0 flex -translate-y-1/2 justify-between px-4 text-[20.5vw] uppercase leading-none tracking-[-0.02em] md:top-[47%] md:px-8 md:text-[19vw] [@media(max-height:560px)]:top-[30%] [@media(max-height:560px)]:text-[13vw]"
      >
        {LETTERS.map((l, i) => (
          <span
            key={l}
            aria-hidden
            className="block overflow-hidden"
            style={{ transform: `translate3d(calc(var(--p) * ${i < 3 ? -1 : 1} * ${12 + Math.abs(i - 2.5) * 4}vw), 0, 0)` }}
          >
            <span
              ref={(node) => {
                lettersRef.current[i] = node
              }}
              className={`hero-line hero-glyph block ${l === 'X' ? 'text-accent' : ''}`}
              style={{ '--i': i } as React.CSSProperties}
            >
              {l}
            </span>
          </span>
        ))}
      </h1>

      {/* La sculpture X, devant le mot */}
      <div
        aria-hidden
        className="hero-sculpt pointer-events-none absolute left-1/2 top-[25svh] z-10 aspect-[4/5] h-[min(42svh,100vw)] md:bottom-[-6svh] md:top-auto md:h-[68svh]"
        style={{ transform: 'translate3d(-50%, calc(var(--p) * -18vh), 0)' }}
      >
        <img src="/hero/x-sculpt.webp" srcSet="/hero/x-sculpt-sm.webp 560w, /hero/x-sculpt.webp 950w" sizes="(min-width: 768px) 72vh, 42vh" alt="" fetchPriority="high" width={633} height={792} className={`absolute inset-0 h-full w-full object-contain transition-opacity duration-700 ${ready ? 'opacity-0' : 'opacity-100'}`} />
        <canvas ref={canvasRef} className={`absolute inset-0 h-full w-full transition-opacity duration-700 ${ready ? 'opacity-100' : 'opacity-0'}`} />
      </div>

      <div
        className="relative z-20 mt-auto grid grid-cols-1 gap-8 px-4 pb-6 md:grid-cols-12 md:items-end md:px-8 md:pb-8"
        style={{ transform: 'translate3d(0, calc(var(--p) * -6vh), 0)', opacity: 'calc(1 - var(--p) * 1.2)' }}
      >
        <div className="md:col-span-5">
          <p className="fade-in t-lead-hero" style={{ '--delay': '900ms' } as React.CSSProperties}>
            Nous faisons bouger <KineticVerb />
          </p>
          <div className="fade-in mt-6 flex flex-wrap items-center gap-3 md:mt-8" style={{ '--delay': '1050ms' } as React.CSSProperties}>
            <a
              href="#contact"
              className="group inline-flex min-h-13 items-center gap-3 whitespace-nowrap rounded-full bg-accent px-7 text-[15px] font-semibold text-accent-foreground transition-[transform,background-color] duration-500 ease-[var(--ease-out-expo)] hover:scale-[1.03]"
            >
              Démarrer un projet
              <ArrowIcon className="size-4 transition-transform duration-500 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
            </a>
            <a
              href="#travaux"
              className="group inline-flex min-h-13 items-center gap-3 whitespace-nowrap rounded-full border border-line bg-background/50 px-7 text-[15px] font-medium transition-[border-color,background-color] duration-500 hover:border-foreground/40 hover:bg-foreground/5"
            >
              Voir les réalisations
              <ArrowIcon className="size-4 opacity-70 transition-transform duration-500 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
            </a>
          </div>
        </div>
        <div
          className="fade-in flex justify-between gap-4 text-[14px] text-foreground/75 md:col-span-3 md:col-start-10 md:flex-col md:items-end md:text-right md:text-[15px]"
          style={{ '--delay': '1200ms' } as React.CSSProperties}
        >
          <p>Identité · Motion · Web</p>
          <p>
            Cotonou, Bénin · <LocalTime />
          </p>
        </div>
      </div>
    </section>
  )
}

function hasHardwareGL() {
  try {
    const c = document.createElement('canvas')
    const gl = (c.getContext('webgl2') || c.getContext('webgl')) as WebGLRenderingContext | null
    if (!gl) return false
    const dbg = gl.getExtension('WEBGL_debug_renderer_info')
    const name = dbg ? String(gl.getParameter(dbg.UNMASKED_RENDERER_WEBGL)) : ''
    gl.getExtension('WEBGL_lose_context')?.loseContext()
    return !/swiftshader|llvmpipe|softpipe|software|basic render/i.test(name)
  } catch {
    return false
  }
}

function KineticVerb() {
  const [i, setI] = useState(0)

  useEffect(() => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
    const id = setInterval(() => setI((v) => (v + 1) % VERBS.length), 3000)
    return () => clearInterval(id)
  }, [])

  return (
    <span className="relative inline-flex overflow-hidden pb-[0.12em] pr-[0.1em] align-bottom">
      <span className="sr-only">les marques, les images, le web et les idées.</span>
      <span key={i} aria-hidden className="word-swap inline-block font-serif font-normal italic tracking-[-0.01em] text-accent" style={{ fontVariationSettings: 'normal' }}>
        {VERBS[i]}.
      </span>
    </span>
  )
}
