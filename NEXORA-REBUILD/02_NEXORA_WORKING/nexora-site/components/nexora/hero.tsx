'use client'

import Image from 'next/image'
import { useEffect, useRef, useState } from 'react'
import { LocalTime } from './local-time'

const LETTERS = ['N', 'E', 'X', 'O', 'R', 'A']
const VERBS = ['les marques', 'les images', 'le web', 'les idées', 'Cotonou']

export function Hero() {
  const sectionRef = useRef<HTMLElement>(null)
  const lettersRef = useRef<(HTMLSpanElement | null)[]>([])
  const [pointer, setPointer] = useState(false)

  useEffect(() => {
    const el = sectionRef.current
    if (!el) return
    let raf = 0
    const onScroll = () => {
      cancelAnimationFrame(raf)
      raf = requestAnimationFrame(() => {
        el.style.setProperty('--sy', String(Math.min(window.scrollY, window.innerHeight * 1.2)))
      })
    }
    onScroll()
    window.addEventListener('scroll', onScroll, { passive: true })
    return () => {
      window.removeEventListener('scroll', onScroll)
      cancelAnimationFrame(raf)
    }
  }, [])

  const handleMove = (e: React.PointerEvent) => {
    if (e.pointerType !== 'mouse') return
    if (!pointer) setPointer(true)
    const range = window.innerWidth * 0.32
    lettersRef.current.forEach((letter) => {
      if (!letter) return
      const r = letter.getBoundingClientRect()
      const dx = Math.abs(e.clientX - (r.left + r.width / 2))
      const influence = Math.max(0, 1 - dx / range)
      const eased = influence * influence * (3 - 2 * influence)
      letter.style.setProperty('--wdth', String(68 + eased * 57))
      letter.style.setProperty('--wght', String(380 + eased * 520))
    })
  }

  const handleLeave = () => {
    setPointer(false)
    lettersRef.current.forEach((l) => {
      l?.style.removeProperty('--wdth')
      l?.style.removeProperty('--wght')
    })
  }

  return (
    <section
      id="top"
      ref={sectionRef}
      onPointerMove={handleMove}
      onPointerLeave={handleLeave}
      className={`relative flex min-h-[100svh] flex-col justify-between overflow-hidden px-4 pb-24 pt-20 md:px-8 md:pb-8 md:pt-28 ${
        pointer ? 'is-pointer' : ''
      }`}
      style={{ '--sy': 0 } as React.CSSProperties}
    >
      {/* Editorial grid — Direction B only */}
      <div aria-hidden className="only-jour pointer-events-none absolute inset-0 grid grid-cols-4 px-4 md:grid-cols-12 md:px-8">
        {Array.from({ length: 12 }).map((_, i) => (
          <div key={i} className={`border-l border-line ${i >= 4 ? 'hidden md:block' : ''}`} />
        ))}
      </div>

      {/* Meta row */}
      <div className="fade-in relative z-10 grid grid-cols-2 gap-y-2 text-[11px] uppercase tracking-[0.16em] text-muted-foreground md:grid-cols-12" style={{ '--delay': '900ms' } as React.CSSProperties}>
        <p className="md:col-span-3">Agence créative &amp; digitale</p>
        <p className="text-right md:col-span-3 md:text-left">Cotonou, Bénin — 6.37°N 2.43°E</p>
        <p className="md:col-span-3">
          <span className="only-nuit">REC </span>
          <span className="inline-block h-1.5 w-1.5 translate-y-[-1px] rounded-full bg-accent blink" aria-hidden />{' '}
          Studio ouvert · <LocalTime /> WAT
        </p>
        <p className="text-right md:col-span-3">Édition 2026 — Vol. 01</p>
      </div>

      {/* Signature: kinetic wordmark + fragments */}
      <div className="relative z-10 my-auto py-16 md:py-10">
        {/* Fragment 01 — Graphic design (behind type) */}
        <figure
          className="absolute left-[2%] top-[-4%] z-0 w-[30vw] md:left-[9%] md:top-[-18%] md:w-[13vw]"
          style={{ transform: 'translate3d(0, calc(var(--sy) * -0.25px), 0) rotate(-5deg)' }}
        >
          <div className="fragment-reveal relative aspect-[2/3] overflow-hidden" style={{ '--delay': '700ms' } as React.CSSProperties}>
            <Image src="/work/poster.png" alt="Fragment d'affiche aux formes géométriques découpées, vermillon et noir" fill sizes="(min-width: 768px) 13vw, 30vw" className="art-img object-cover" priority />
          </div>
          <figcaption className="fade-in mt-2 text-[10px] uppercase tracking-[0.16em] text-muted-foreground" style={{ '--delay': '1500ms' } as React.CSSProperties}>
            Fig. 01 — Affiche
          </figcaption>
        </figure>

        {/* Fragment 02 — Motion (in front) */}
        <figure
          className="absolute right-[2%] top-[-10%] z-20 w-[38vw] md:right-[18%] md:top-[-26%] md:w-[19vw]"
          style={{ transform: 'translate3d(0, calc(var(--sy) * -0.5px), 0) rotate(3deg)' }}
        >
          <div className="fragment-reveal relative aspect-[4/5] overflow-hidden" style={{ '--delay': '950ms' } as React.CSSProperties}>
            <Image src="/work/motion.png" alt="Danseuse en mouvement drapée d'un tissu indigo, pose longue" fill sizes="(min-width: 768px) 19vw, 38vw" className="art-img object-cover" priority />
            <div className="absolute inset-x-2 bottom-2 flex items-center gap-2 text-[9px] font-medium uppercase tracking-widest text-white mix-blend-difference">
              <span aria-hidden>▶</span>
              <span className="relative h-px flex-1 bg-white/30">
                <span className="scrub absolute inset-0 origin-left bg-white" />
              </span>
              <span>00:12:04</span>
            </div>
          </div>
          <figcaption className="fade-in mt-2 text-right text-[10px] uppercase tracking-[0.16em] text-muted-foreground" style={{ '--delay': '1600ms' } as React.CSSProperties}>
            Fig. 02 — Motion
          </figcaption>
        </figure>

        <h1 aria-label="NEXORA" className="relative z-10 flex justify-between text-[23.5vw] uppercase leading-none tracking-[-0.02em]">
          {LETTERS.map((l, i) => (
            <span key={l} aria-hidden className="block overflow-hidden">
              <span
                ref={(node) => {
                  lettersRef.current[i] = node
                }}
                className={`hero-letter ${l === 'X' ? 'text-accent' : ''}`}
                style={{ '--i': i } as React.CSSProperties}
              >
                {l}
              </span>
            </span>
          ))}
        </h1>

        {/* Fragment 03 — Interface (in front, bottom) */}
        <figure
          className="absolute bottom-[-14%] left-[24%] z-20 w-[50vw] md:bottom-[-24%] md:left-[38%] md:w-[24vw]"
          style={{ transform: 'translate3d(0, calc(var(--sy) * -0.12px), 0) rotate(-1.5deg)' }}
        >
          <div className="fragment-reveal relative aspect-[16/10] overflow-hidden border border-line bg-card" style={{ '--delay': '1200ms' } as React.CSSProperties}>
            <div className="flex items-center gap-1 border-b border-line px-2 py-1">
              <span className="h-1.5 w-1.5 rounded-full bg-foreground/30" />
              <span className="h-1.5 w-1.5 rounded-full bg-foreground/30" />
              <span className="h-1.5 w-1.5 rounded-full bg-accent" />
              <span className="ml-2 truncate text-[8px] tracking-wider text-muted-foreground">
                nexora.bj/concept<span className="blink">|</span>
              </span>
            </div>
            <div className="relative h-full">
              <Image src="/work/interface.png" alt="Interface d'un site e-commerce éditorial de mode" fill sizes="(min-width: 768px) 24vw, 50vw" className="art-img object-cover object-top" priority />
            </div>
          </div>
          <figcaption className="fade-in mt-2 text-[10px] uppercase tracking-[0.16em] text-muted-foreground" style={{ '--delay': '1800ms' } as React.CSSProperties}>
            Fig. 03 — Interface
          </figcaption>
        </figure>
      </div>

      {/* Bottom statement */}
      <div className="relative z-10 grid grid-cols-1 items-end gap-6 md:grid-cols-12">
        <p className="fade-in font-serif text-3xl italic leading-[1.05] md:col-span-5 md:text-5xl" style={{ '--delay': '1300ms' } as React.CSSProperties}>
          Nous faisons bouger{' '}
          <KineticVerb />
        </p>
        <p className="fade-in max-w-sm text-sm leading-relaxed text-muted-foreground md:col-span-4 md:col-start-7" style={{ '--delay': '1500ms' } as React.CSSProperties}>
          Communication visuelle, motion design et sites web. Un studio béninois qui pense chaque marque comme une image en mouvement.
        </p>
        <a
          href="#studio"
          className="fade-in hidden items-center justify-end gap-3 text-xs uppercase tracking-[0.2em] md:col-span-3 md:flex"
          style={{ '--delay': '1700ms' } as React.CSSProperties}
        >
          Défiler
          <span className="relative block h-10 w-px overflow-hidden bg-line">
            <span className="absolute inset-x-0 top-0 h-1/2 bg-foreground [animation:marquee-y_1.8s_ease-in-out_infinite]" />
          </span>
        </a>
      </div>

      <div aria-hidden className="only-nuit grain pointer-events-none absolute inset-0 opacity-[0.18]" />
    </section>
  )
}

function KineticVerb() {
  const [i, setI] = useState(0)

  useEffect(() => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
    const id = setInterval(() => setI((v) => (v + 1) % VERBS.length), 2200)
    return () => clearInterval(id)
  }, [])

  return (
    <span className="relative inline-flex overflow-hidden pb-[0.1em] align-bottom">
      <span className="sr-only">{VERBS.join(', ')}</span>
      <span key={i} aria-hidden className="word-swap inline-block text-accent">
        {VERBS[i]}.
      </span>
    </span>
  )
}
