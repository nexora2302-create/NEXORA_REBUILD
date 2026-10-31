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
  const [posterGone, setPosterGone] = useState(false)

  useEffect(() => {
    if (!ready) return
    const id = setTimeout(() => setPosterGone(true), 1000)
    return () => clearTimeout(id)
  }, [ready])

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
          // L'affiche a déjà joué l'entrée : la 3D reprend directement au repos.
          dispose = mountNxScene(canvas, { reduced: false, force, intro: false })
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

  return (
    <section
      id="top"
      ref={sectionRef}
      className="relative isolate flex min-h-svh flex-col overflow-hidden"
      style={{ '--p': 0 } as React.CSSProperties}
    >
      {/* Chaleur sous la sculpture */}
      <div
        aria-hidden
        className="absolute inset-0 -z-20 bg-[radial-gradient(ellipse_38%_48%_at_41%_58%,rgb(122_36_16/0.55),transparent_70%)] max-md:bg-[radial-gradient(ellipse_70%_32%_at_44%_42%,rgb(122_36_16/0.5),transparent_70%)]"
      />

      {/* Le mot, serré comme le logo ; la sculpture 3D tient la place du X. Il s'écarte au scroll. */}
      <h1
        aria-label="NEXORA"
        className="t-wordmark absolute inset-x-0 top-[33svh] z-0 flex -translate-y-1/2 flex-col items-center gap-[0.07em] px-4 md:top-[40%] md:flex-row md:justify-center md:gap-0 md:px-8 [@media(max-height:560px)]:top-[34%] [@media(max-height:560px)]:flex-row"
      >
        {[LETTERS.slice(0, 3), LETTERS.slice(3)].map((group, g) => (
          <span key={g} aria-hidden className="flex">
          {group.map((l) => {
              const i = LETTERS.indexOf(l)
              return (
            l === 'X' ? (
              <span key={l} aria-hidden className="relative z-10 block">
                <span className="invisible block">X</span>
                <span
                  className="hero-sculpt pointer-events-none absolute left-1/2 top-[-0.42em] aspect-[4/5] h-[2.05em] md:top-[-0.32em] md:h-[2.05em]"
                  style={{ transform: 'translate3d(-50%, calc(var(--p) * -14vh), 0)' }}
                >
                  {!posterGone && (
                  <span className="sculpt-poster absolute inset-0 block">
                  <img
                    src="/hero/x-sculpt.webp"
                    srcSet="/hero/x-sculpt-sm.webp 560w, /hero/x-sculpt.webp 950w"
                    sizes="(min-width: 768px) 44vw, 72vw"
                    alt=""
                    fetchPriority="high"
                    width={633}
                    height={792}
                    className={`absolute inset-0 h-full w-full object-contain transition-opacity duration-1000 ${ready ? 'opacity-0' : 'opacity-100'}`}
                  />
                  </span>
                  )}
                  <canvas ref={canvasRef} className={`absolute inset-0 h-full w-full transition-opacity duration-1000 ${ready ? 'opacity-100' : 'opacity-0'}`} />
                </span>
              </span>
            ) : (
              <span
                key={l}
                aria-hidden
                className="block overflow-hidden"
                style={{ transform: `translate3d(calc(var(--p) * ${i < 2 ? -1 : 1} * ${10 + Math.abs(i - 2) * 3}vw), 0, 0)` }}
              >
                <span className="hero-line block" style={{ '--i': i } as React.CSSProperties}>
                  {l}
                </span>
              </span>
            )
          )
          })}
          </span>
        ))}
      </h1>

      <div
        className="relative z-20 mt-auto grid grid-cols-1 gap-8 px-4 pb-6 md:grid-cols-12 md:items-end md:px-8 md:pb-8"
        style={{ transform: 'translate3d(0, calc(var(--p) * -6vh), 0)', opacity: 'calc(1 - var(--p) * 1.2)' }}
      >
        <div className="md:col-span-5">
          <p className="t-lead-hero">
            <span className="block overflow-hidden pb-[0.08em]">
              <span className="hero-line block" style={{ '--i': 6 } as React.CSSProperties}>
                Nous faisons bouger <KineticVerb />
              </span>
            </span>
          </p>
          <div className="fade-in mt-6 flex flex-wrap items-center gap-x-3 gap-y-2 md:mt-8" style={{ '--delay': '1050ms' } as React.CSSProperties}>
            <a
              href="#contact"
              className="group inline-flex min-h-13 items-center gap-3 whitespace-nowrap rounded-full bg-accent px-7 text-[15px] font-semibold text-accent-foreground transition-[transform,background-color] duration-500 ease-[var(--ease-out-expo)] hover:scale-[1.03]"
            >
              Démarrer un projet
              <ArrowIcon className="size-4 transition-transform duration-500 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
            </a>
            <a
              href="#travaux"
              className="group inline-flex min-h-13 items-center gap-2 whitespace-nowrap rounded-full px-2 text-[15px] font-medium max-md:underline max-md:decoration-foreground/40 max-md:underline-offset-4 md:gap-3 md:border md:border-line md:bg-background/50 md:px-7 transition-[border-color,background-color] duration-500 hover:border-foreground/40 hover:bg-foreground/5"
            >
              Voir les réalisations
              <ArrowIcon className="size-4 opacity-70 transition-transform duration-500 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
            </a>
          </div>
        </div>
        <div className="fade-in md:col-span-4 md:col-start-9 lg:col-span-3 lg:col-start-10" style={{ '--delay': '1200ms' } as React.CSSProperties}>
          <p className="max-w-[22rem] text-[16px] leading-relaxed text-foreground/85 md:text-[17px]">
            Studio créatif à Cotonou. Identité, motion design et sites web, pensés ensemble pour les marques du Bénin, d’Afrique et d’ailleurs.
          </p>
          <p className="mt-5 flex items-center gap-2 text-[14px] text-foreground/70 md:mt-6 md:text-[15px]">
            <span aria-hidden className="live-dot size-1.5 rounded-full bg-accent" />
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
