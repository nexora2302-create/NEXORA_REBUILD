'use client'

import Image from 'next/image'
import { useEffect, useRef } from 'react'
import { PROJECTS } from '@/lib/projects'
import { fr } from './fr'
import { ArrowIcon } from './icons'
import { Reveal, SplitWords } from './reveal'

/*
 * Galerie « zoom » : sept images autour d'un centre. Au scroll (natif, section collante),
 * chacune grandit à sa vitesse ; l'image centrale finit plein écran, les autres sortent du cadre.
 */
const LAYOUT: { slug: string; box: string; scale: number }[] = [
  { slug: 'ganvie-heure-bleue', box: 'h-[25vh] w-[25vw]', scale: 4 },
  { slug: 'kpevi-records', box: 'h-[30vh] w-[35vw] -translate-y-[30vh] translate-x-[5vw]', scale: 5 },
  { slug: 'sons-d-ancetres', box: 'h-[45vh] w-[20vw] -translate-y-[10vh] -translate-x-[25vw]', scale: 6 },
  { slug: 'atelier-daxo', box: 'h-[25vh] w-[25vw] translate-x-[27.5vw]', scale: 5 },
  { slug: 'kora-cafe', box: 'h-[25vh] w-[20vw] translate-y-[27.5vh] translate-x-[5vw]', scale: 6 },
  { slug: 'biennale-cotonou-design', box: 'h-[25vh] w-[30vw] translate-y-[27.5vh] -translate-x-[22.5vw]', scale: 8 },
  { slug: 'flux', box: 'h-[15vh] w-[15vw] translate-y-[22.5vh] translate-x-[25vw]', scale: 9 },
]

export function Work() {
  const stageRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const el = stageRef.current
    if (!el || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
    let raf = 0
    const update = () => {
      raf = 0
      const r = el.getBoundingClientRect()
      const range = r.height - window.innerHeight
      const p = range > 0 ? Math.min(1, Math.max(0, -r.top / range)) : 0
      el.style.setProperty('--z', p.toFixed(4))
    }
    const onScroll = () => {
      if (!raf) raf = requestAnimationFrame(update)
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

  const bySlug = Object.fromEntries(PROJECTS.map((p) => [p.slug, p]))

  return (
    <section id="travaux" aria-labelledby="travaux-title" className="relative">
      <Reveal className="grid gap-6 px-4 pb-16 pt-28 md:grid-cols-12 md:items-end md:px-8 md:pb-20 md:pt-36">
        <h2 id="travaux-title" className="t-section md:col-span-8">
          <SplitWords text="Réalisations" />
        </h2>
        <p className="max-w-sm text-[17px] leading-relaxed text-foreground/80 md:col-span-4">
          {fr('Huit concepts d’exploration conçus par le studio pour montrer sa démarche, en attendant les premiers projets clients.')}
        </p>
      </Reveal>

      <div ref={stageRef} className="zoom-stage relative h-[300vh]" style={{ '--z': 0 } as React.CSSProperties}>
        <div className="sticky top-0 h-svh overflow-hidden">
          {LAYOUT.map(({ slug, box, scale }, i) => {
            const p = bySlug[slug]
            return (
              <div
                key={slug}
                className="absolute inset-0 flex items-center justify-center will-change-transform"
                style={{ transform: `scale(calc(1 + var(--z) * ${scale - 1}))` }}
              >
                <a
                  href={`/realisations#${slug}`}
                  className={`zoom-tile group relative block overflow-hidden ${box}`}
                  style={{ viewTransitionName: `work-${slug}` }}
                  aria-label={`${p.title}, ${p.tag}`}
                >
                  <div className="absolute inset-0" style={p.crop ? { transform: `scale(${p.crop})` } : undefined}>
                  <Image
                    src={p.img}
                    alt={p.alt}
                    fill
                    placeholder="blur"
                    blurDataURL={p.blur}
                    quality={82}
                    sizes={i === 0 ? '100vw' : '(min-width: 768px) 40vw, 60vw'}
                    className="object-cover transition-transform duration-[1.2s] ease-[var(--ease-out-expo)] group-hover:scale-[1.06]"
                    style={{ objectPosition: p.pos }}
                  />
                  </div>
                </a>
              </div>
            )
          })}

          <div className="pointer-events-none absolute inset-x-0 bottom-0 flex items-end justify-between gap-6 bg-gradient-to-t from-background/80 to-transparent px-4 pb-6 pt-24 md:px-8 md:pb-8">
            <p className="max-w-xs text-[15px] leading-snug text-foreground/90">Choisissez une image pour ouvrir son projet.</p>
          </div>
        </div>
      </div>

      <div className="flex flex-col items-start gap-6 px-4 py-20 md:flex-row md:items-center md:justify-between md:px-8 md:py-24">
        <p className="t-card max-w-[18ch]">Chaque concept, en détail.</p>
        <a
          href="/realisations"
          className="group inline-flex min-h-14 items-center gap-4 rounded-full bg-accent pl-7 pr-2 text-[16px] font-semibold text-accent-foreground transition-transform duration-500 hover:scale-[1.03]"
        >
          Voir toutes les réalisations
          <span className="grid size-10 place-items-center rounded-full bg-accent-foreground text-accent transition-transform duration-500 group-hover:rotate-45">
            <ArrowIcon className="size-4" />
          </span>
        </a>
      </div>
    </section>
  )
}
