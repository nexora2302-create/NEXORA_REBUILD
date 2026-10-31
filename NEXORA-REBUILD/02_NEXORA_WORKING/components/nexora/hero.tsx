'use client'

import { useEffect, useRef, useState } from 'react'
import { ArrowIcon } from './icons'

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
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches || !hasHardwareGL()) return
    const start = () =>
      import('./nx-scene').then(({ mountNxScene }) => {
        if (cancelled) return
        try {
          dispose = mountNxScene(canvas, { reduced: false })
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
      {/* Scène 3D plein cadre : la braise qui monte vers le NX */}
      <div aria-hidden className="absolute inset-0 -z-10 bg-background">
        <picture>
          <source media="(max-aspect-ratio: 1/1)" srcSet="/hero/scene-mobile.webp" />
          <img src="/hero/scene-desktop.webp" alt="" fetchPriority="high" decoding="async" className="absolute inset-0 h-full w-full object-cover" />
        </picture>
        <canvas
          ref={canvasRef}
          className={`absolute inset-0 h-full w-full transition-opacity duration-[1.8s] ease-[var(--ease-out-expo)] ${ready ? 'opacity-100' : 'opacity-0'}`}
        />
        {/* Voile neutre côté texte, pour la lisibilité */}
        <div className="absolute inset-0 bg-[linear-gradient(to_top,rgb(13_12_11/0.95),rgb(13_12_11/0.55)_40%,transparent_70%)] md:bg-[linear-gradient(to_right,rgb(13_12_11/0.9),rgb(13_12_11/0.55)_38%,transparent_62%)]" />
        <div className="absolute inset-x-0 bottom-0 h-24 bg-gradient-to-t from-background to-transparent" />
      </div>

      <div
        className="flex flex-1 flex-col justify-end px-4 pb-12 pt-[42svh] md:justify-center md:px-8 md:pb-16 md:pt-28"
        style={{ transform: 'translate3d(0, calc(var(--p) * -8vh), 0)', opacity: 'calc(1 - var(--p) * 1.1)' }}
      >
        <div className="max-w-[46rem] md:max-w-[58%]">
          <p
            className="fade-in inline-flex min-h-10 items-center gap-3 rounded-full border border-line bg-background/50 px-4 text-[14px] text-foreground/85 md:text-[15px]"
            style={{ '--delay': '150ms' } as React.CSSProperties}
          >
            <span aria-hidden className="live-dot size-2 rounded-full bg-accent" />
            Studio créatif
            <span aria-hidden className="size-1 rounded-full bg-foreground/40" />
            <span className="text-foreground/70">Cotonou, Bénin</span>
          </p>

          <h1 className="t-hero mt-7 md:mt-9">
            <span className="block overflow-hidden pb-[0.06em]">
              <span className="hero-line block" style={{ '--i': 0 } as React.CSSProperties}>Nous faisons</span>
            </span>
            <span className="block overflow-hidden pb-[0.14em]">
              <span className="hero-line block" style={{ '--i': 1 } as React.CSSProperties}>
                bouger <KineticVerb />
              </span>
            </span>
          </h1>

          <p
            className="fade-in mt-6 max-w-xl text-[17px] leading-relaxed text-foreground/80 md:mt-8 md:text-[19px]"
            style={{ '--delay': '550ms' } as React.CSSProperties}
          >
            Identité, motion design et sites web, pensés ensemble par un studio de Cotonou pour les marques du Bénin, d’Afrique et d’ailleurs.
          </p>

          <div className="fade-in mt-8 flex flex-wrap items-center gap-3 md:mt-10 md:gap-4" style={{ '--delay': '680ms' } as React.CSSProperties}>
            <a
              href="#contact"
              className="group inline-flex min-h-13 items-center gap-3 whitespace-nowrap rounded-full bg-accent px-7 text-[15px] font-semibold text-accent-foreground transition-[transform,background-color] duration-500 ease-[var(--ease-out-expo)] hover:scale-[1.03] md:min-h-14 md:px-8 md:text-[16px]"
            >
              Démarrer un projet
              <ArrowIcon className="size-4 transition-transform duration-500 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
            </a>
            <a
              href="#travaux"
              className="group inline-flex min-h-13 items-center gap-3 whitespace-nowrap rounded-full border border-line bg-background/50 px-7 text-[15px] font-medium transition-[border-color,background-color] duration-500 hover:border-foreground/40 hover:bg-foreground/5 md:min-h-14 md:px-8 md:text-[16px]"
            >
              Voir les réalisations
              <ArrowIcon className="size-4 opacity-70 transition-transform duration-500 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
            </a>
          </div>
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
