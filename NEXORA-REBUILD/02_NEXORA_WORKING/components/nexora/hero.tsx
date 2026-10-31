'use client'

import { useEffect, useRef, useState } from 'react'
import { ArrowIcon } from './icons'
import { LocalTime } from './local-time'
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
      letter.style.setProperty('--wdth', String(100 + eased * 12))
      letter.style.setProperty('--wght', String(800 + eased * 80))
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
      className="relative min-h-svh p-2 md:p-3"
      style={{ '--p': 0 } as React.CSSProperties}
    >
      {/* Cadre : la soie vit dans un panneau, qui se resserre en quittant l'écran. */}
      <div
        className="hero-frame relative isolate flex min-h-[calc(100svh-1rem)] flex-col overflow-hidden rounded-[1.25rem] bg-background md:min-h-[calc(100svh-1.5rem)] md:rounded-[1.75rem]"
        style={{
          transform: 'scale(calc(1 - var(--p) * 0.08))',
          borderRadius: 'calc(1.75rem + var(--p) * 1.5rem)',
        }}
      >
        <div aria-hidden className="absolute inset-0 -z-10" style={{ transform: 'scale(calc(1 + var(--p) * 0.15))' }}>
          <Silk className="hero-silk" />
          {/* Voile neutre sous le texte, pour la lisibilité */}
          <div className="absolute inset-0 bg-[linear-gradient(to_bottom,rgb(13_12_11/0.55),transparent_32%,transparent_55%,rgb(13_12_11/0.7))]" />
        </div>

        <div
          className="flex flex-1 flex-col px-2 pb-3 pt-24 md:px-5 md:pb-5 md:pt-32 [@media(max-height:560px)]:pt-20"
          style={{ transform: 'translate3d(0, calc(var(--p) * -6vh), 0)', opacity: 'calc(1 - var(--p) * 0.9)' }}
        >
          <div className="grid grid-cols-1 gap-8 md:grid-cols-12 md:gap-6">
            <p
              className="fade-in font-serif text-[2.6rem] italic leading-[1] tracking-[-0.01em] md:col-span-7 md:text-[clamp(3rem,5.4vw,5.75rem)] [@media(max-height:560px)]:text-[2.25rem]"
              style={{ '--delay': '350ms' } as React.CSSProperties}
            >
              Nous faisons bouger
              <br />
              <KineticVerb />
            </p>
            <div className="fade-in flex flex-col gap-6 md:col-span-4 md:col-start-9 md:pt-3" style={{ '--delay': '480ms' } as React.CSSProperties}>
              <p className="max-w-sm text-[17px] leading-relaxed text-foreground/85 [@media(max-height:560px)]:hidden">
                Identité, motion design et sites web, pensés ensemble par un studio de Cotonou pour les marques du Bénin, d’Afrique et d’ailleurs.
              </p>
              <div className="flex flex-wrap items-center gap-x-6 gap-y-2">
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

          <div className="mt-auto pt-10">
            <div
              className="fade-in flex items-end justify-between gap-4 pb-4 text-[14px] text-foreground/80 md:pb-5 md:text-[15px]"
              style={{ '--delay': '650ms' } as React.CSSProperties}
            >
              <p>
                Identité visuelle, motion design
                <br className="sm:hidden" />
                <span className="hidden sm:inline">, </span>création web
              </p>
              <p className="text-right">
                Cotonou, Bénin
                <br className="sm:hidden" />
                <span className="hidden sm:inline"> · </span>
                <LocalTime />
              </p>
            </div>
            <h1
              aria-label="NEXORA"
              className="relative flex justify-between text-[20vw] uppercase leading-none tracking-[-0.02em] md:text-[19.6vw] [@media(max-height:560px)]:justify-start [@media(max-height:560px)]:text-[13vw]"
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
    const id = setInterval(() => setI((v) => (v + 1) % VERBS.length), 3000)
    return () => clearInterval(id)
  }, [])

  return (
    <span className="relative inline-flex overflow-hidden pb-[0.18em] pr-[0.08em] align-top leading-[1.1]">
      <span className="sr-only">les marques, les images, le web et les idées.</span>
      <span key={i} aria-hidden className="word-swap inline-block text-accent">
        {VERBS[i]}.
      </span>
    </span>
  )
}
