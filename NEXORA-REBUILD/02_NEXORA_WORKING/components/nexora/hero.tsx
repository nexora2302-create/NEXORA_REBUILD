'use client'

import Image from 'next/image'
import { useEffect, useRef, useState } from 'react'

const LETTERS = ['N', 'E', 'X', 'O', 'R', 'A']
const VERBS = ['les marques', 'les images', 'le web', 'les idées', 'Cotonou']

const clamp = (v: number) => Math.min(1, Math.max(0, v))
const ease = (t: number) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2)

/**
 * Hero épinglé sur ~1 écran de scroll natif (pas de scroll détourné) :
 * une seule image, d'abord fenêtre centrale, qui s'ouvre jusqu'au plein cadre
 * pendant que le mot NEXORA dérive lettre par lettre.
 */
export function Hero() {
  const sectionRef = useRef<HTMLElement>(null)
  const lettersRef = useRef<(HTMLSpanElement | null)[]>([])
  const timeRef = useRef<HTMLSpanElement>(null)
  const [pointer, setPointer] = useState(false)

  useEffect(() => {
    const el = sectionRef.current
    if (!el) return
    let raf = 0
    const update = () => {
      const r = el.getBoundingClientRect()
      const range = r.height - window.innerHeight
      const p = range > 0 ? clamp(-r.top / range) : 0
      el.style.setProperty('--p', p.toFixed(4))
      el.style.setProperty('--e', ease(clamp(p / 0.8)).toFixed(4))
      if (timeRef.current) timeRef.current.textContent = `00:00:${String(Math.round(p * 12)).padStart(2, '0')}`
    }
    const onScroll = () => {
      cancelAnimationFrame(raf)
      raf = requestAnimationFrame(update)
    }
    update()
    window.addEventListener('scroll', onScroll, { passive: true })
    window.addEventListener('resize', onScroll)
    return () => {
      window.removeEventListener('scroll', onScroll)
      window.removeEventListener('resize', onScroll)
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
      aria-label="NEXORA, studio créatif en mouvement"
      className="hero-section relative h-[185svh] md:h-[200svh]"
      style={{ '--p': 0, '--e': 0 } as React.CSSProperties}
    >
      <div
        onPointerMove={handleMove}
        onPointerLeave={handleLeave}
        className={`sticky top-0 flex h-svh flex-col justify-between overflow-hidden px-4 pb-6 pt-20 md:px-8 md:pb-8 md:pt-24 ${pointer ? 'is-pointer' : ''}`}
      >
        {/* Image unique : fenêtre centrale → plein cadre */}
        <div className="clip-reveal absolute inset-0" style={{ '--delay': '500ms' } as React.CSSProperties}>
          <div className="hero-frame absolute inset-0 overflow-hidden">
            <div className="hero-img absolute inset-0">
              <Image
                src="/work/motion.webp"
                alt="Danseuse en mouvement drapée d’un tissu indigo, pose longue"
                fill
                priority
                sizes="100vw"
                className="object-cover"
              />
            </div>
            <div
              aria-hidden
              className="absolute inset-0 bg-gradient-to-t from-background via-background/20 to-background/40"
              style={{ opacity: 'calc(var(--e) * 0.9)' }}
            />
          </div>
        </div>

        {/* Meta row */}
        <div className="fade-in relative z-10 grid grid-cols-2 gap-y-2 font-mono text-[11px] uppercase tracking-[0.16em] text-muted-foreground md:grid-cols-12" style={{ '--delay': '900ms' } as React.CSSProperties}>
          <p className="md:col-span-4">Agence créative &amp; digitale</p>
          <p className="text-right md:col-span-4 md:text-center">Cotonou, Bénin — 6.37°N 2.43°E</p>
          <p className="col-span-2 md:col-span-4 md:text-right">Édition 2026 — Vol. 01</p>
        </div>

        {/* Mot-signature */}
        <h1 aria-label="NEXORA" className="relative z-10 my-auto flex justify-between text-[23.5vw] uppercase leading-none tracking-[-0.02em]">
          {LETTERS.map((l, i) => (
            <span
              key={l}
              aria-hidden
              className="block overflow-hidden"
              style={{ transform: `translate3d(0, calc(var(--p) * ${i % 2 ? -2.4 : 2.4}vw), 0)` }}
            >
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

        {/* Bas : phrase, texte, timecode lié au scroll */}
        <div className="relative z-10 grid grid-cols-1 items-end gap-5 md:grid-cols-12 md:gap-6">
          <p className="fade-in font-serif text-3xl italic leading-[1.05] md:col-span-5 md:text-5xl" style={{ '--delay': '1300ms' } as React.CSSProperties}>
            Nous faisons bouger <KineticVerb />
          </p>
          <p className="fade-in max-w-sm text-sm leading-relaxed text-foreground/80 md:col-span-4 md:col-start-7" style={{ '--delay': '1500ms' } as React.CSSProperties}>
            Communication visuelle, motion design et sites web. Un studio béninois qui pense chaque marque comme une image en mouvement.
          </p>
          <div className="fade-in hidden font-mono text-[11px] uppercase tracking-[0.16em] md:col-span-3 md:col-start-10 md:block" style={{ '--delay': '1700ms' } as React.CSSProperties}>
            <div className="flex items-center justify-between">
              <span>Fig. 01 — Motion</span>
              <span aria-hidden>
                ▶ <span ref={timeRef}>00:00:00</span>
              </span>
            </div>
            <div className="mt-2 h-px bg-foreground/25">
              <div className="h-full origin-left bg-accent" style={{ transform: 'scaleX(var(--p))' }} />
            </div>
            <p className="mt-3 text-muted-foreground">Défiler ↓</p>
          </div>
        </div>
      </div>
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
