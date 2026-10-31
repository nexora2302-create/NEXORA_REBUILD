'use client'

import { useEffect, useRef, useState } from 'react'
import { ArrowIcon } from './icons'
import { Silk } from './silk'

const LETTERS = ['N', 'E', 'X', 'O', 'R', 'A']
const VERBS = ['les marques', 'les images', 'le web', 'les idées']

export function Hero() {
  const sectionRef = useRef<HTMLElement>(null)
  const lettersRef = useRef<(HTMLSpanElement | null)[]>([])

  // Progression de sortie du hero (0 → 1), transform/opacity uniquement.
  useEffect(() => {
    const el = sectionRef.current
    if (!el || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
    let raf = 0
    const update = () => {
      raf = 0
      const h = el.offsetHeight || 1
      const p = Math.min(1, Math.max(0, window.scrollY / h))
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

  // Les lettres s'élargissent près du pointeur (souris uniquement).
  const handleMove = (e: React.PointerEvent) => {
    if (e.pointerType !== 'mouse') return
    const range = window.innerWidth * 0.3
    lettersRef.current.forEach((letter) => {
      if (!letter) return
      const r = letter.getBoundingClientRect()
      const dx = Math.abs(e.clientX - (r.left + r.width / 2))
      const k = Math.max(0, 1 - dx / range)
      const eased = k * k * (3 - 2 * k)
      letter.style.setProperty('--wdth', String(100 + eased * 25))
      letter.style.setProperty('--wght', String(800 + eased * 100))
    })
  }
  const handleLeave = () => {
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
      className="relative isolate flex min-h-svh flex-col overflow-hidden"
      style={{ '--p': 0 } as React.CSSProperties}
    >
      <div
        aria-hidden
        className="absolute inset-0 -z-10 bg-[radial-gradient(ellipse_at_85%_85%,#5c1a09_0%,transparent_60%)]"
        style={{ transform: 'scale(calc(1 + var(--p) * 0.12))' }}
      >
        <Silk className="hero-silk" />
        <div className="absolute inset-x-0 bottom-0 h-1/3 bg-gradient-to-t from-background to-transparent" />
      </div>

      <div
        className="flex flex-1 flex-col justify-end px-4 pb-8 pt-24 md:px-8 md:pb-10"
        style={{ transform: 'translate3d(0, calc(var(--p) * -10vh), 0)', opacity: 'calc(1 - var(--p) * 1.1)' }}
      >
        <p className="fade-in mb-auto self-end text-right font-mono text-xs leading-relaxed text-foreground/70" style={{ '--delay': '700ms' } as React.CSSProperties}>
          Cotonou, Bénin
          <br />
          6.37°N 2.43°E
        </p>

        <h1
          aria-label="NEXORA"
          className="relative mt-10 flex justify-between text-[23.5vw] uppercase leading-none tracking-[-0.02em] [@media(max-height:560px)]:justify-start [@media(max-height:560px)]:text-[15vw]"
        >
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

        <div className="mt-8 grid grid-cols-1 items-end gap-6 md:mt-10 md:grid-cols-12">
          <p className="fade-in font-serif text-[2rem] italic leading-[1.05] md:col-span-5 md:text-5xl" style={{ '--delay': '350ms' } as React.CSSProperties}>
            Nous faisons bouger <KineticVerb />
          </p>
          <p
            className="fade-in max-w-md text-[17px] leading-relaxed text-foreground/80 md:col-span-4 [@media(max-height:560px)]:hidden"
            style={{ '--delay': '450ms' } as React.CSSProperties}
          >
            Identité, motion design et sites web, pensés ensemble par un studio de Cotonou pour les marques du Bénin, d’Afrique et d’ailleurs.
          </p>
          <div className="fade-in flex flex-wrap items-center gap-x-6 gap-y-3 md:col-span-3 md:flex-col md:items-end md:justify-end lg:flex-row lg:items-center" style={{ '--delay': '550ms' } as React.CSSProperties}>
            <a
              href="#contact"
              className="group inline-flex min-h-12 items-center gap-3 whitespace-nowrap rounded-full bg-accent px-6 text-[15px] font-semibold text-accent-foreground transition-[transform,background-color] duration-500 ease-[var(--ease-out-expo)] hover:scale-[1.03]"
            >
              Démarrer un projet
              <ArrowIcon className="size-4 transition-transform duration-500 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
            </a>
            <a href="#travaux" className="link-line inline-flex min-h-12 items-center whitespace-nowrap text-[15px]">
              Voir les réalisations
            </a>
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
    const id = setInterval(() => setI((v) => (v + 1) % VERBS.length), 2400)
    return () => clearInterval(id)
  }, [])

  return (
    <span className="relative inline-flex overflow-hidden pb-[0.1em] align-bottom">
      <span className="sr-only">les marques, les images, le web et les idées.</span>
      <span key={i} aria-hidden className="word-swap inline-block text-accent">
        {VERBS[i]}.
      </span>
    </span>
  )
}
