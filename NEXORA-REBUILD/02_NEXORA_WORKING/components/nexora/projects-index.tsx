'use client'

import Image from 'next/image'
import { useState } from 'react'
import { flushSync } from 'react-dom'
import { DISCIPLINES, PROJECTS, type Discipline } from '@/lib/projects'
import { fr } from './fr'
import { Reveal } from './reveal'

type Filter = Discipline | 'tout'

export function ProjectsIndex() {
  const [filter, setFilter] = useState<Filter>('tout')
  const list = filter === 'tout' ? PROJECTS : PROJECTS.filter((p) => p.discipline === filter)

  // Le changement de filtre passe par une View Transition quand le navigateur la propose.
  const choose = (f: Filter) => {
    if (f === filter) return
    const apply = () => setFilter(f)
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    if (!reduced && 'startViewTransition' in document) {
      ;(document as Document & { startViewTransition: (cb: () => void) => unknown }).startViewTransition(() => flushSync(apply))
    } else apply()
  }

  const chips: { id: Filter; label: string; count: number }[] = [
    { id: 'tout', label: 'Tout', count: PROJECTS.length },
    ...DISCIPLINES.map((d) => ({ id: d.id, label: d.label, count: PROJECTS.filter((p) => p.discipline === d.id).length })),
  ]

  return (
    <>
      <div role="group" aria-label="Filtrer par discipline" className="flex flex-wrap gap-2 px-4 md:px-8">
        {chips.map((c) => {
          const on = c.id === filter
          return (
            <button
              key={c.id}
              type="button"
              aria-pressed={on}
              onClick={() => choose(c.id)}
              className={`inline-flex min-h-11 items-center gap-2 rounded-full border px-5 text-[15px] font-medium transition-colors duration-300 ${
                on ? 'border-accent bg-accent text-accent-foreground' : 'border-line hover:border-foreground/50'
              }`}
            >
              {c.label}
              <span className={`text-[13px] tabular-nums ${on ? 'opacity-80' : 'text-muted-foreground'}`}>{c.count}</span>
            </button>
          )
        })}
      </div>

      <p role="status" className="sr-only">
        {list.length} {list.length > 1 ? 'projets affichés' : 'projet affiché'}
      </p>

      <ol className="mt-16 flex flex-col gap-28 px-4 md:mt-24 md:gap-40 md:px-8">
        {list.map((p, i) => {
          const flip = i % 2 === 1
          const tall = p.height > p.width
          return (
            <li key={p.slug} id={p.slug} className="scroll-mt-28" style={{ viewTransitionName: `case-${p.slug}` }}>
              <article aria-labelledby={`t-${p.slug}`} className="grid gap-8 md:grid-cols-12 md:items-center md:gap-x-8">
                <Reveal
                  threshold={0.12}
                  className={`group relative overflow-hidden ${tall ? 'aspect-[4/5] md:col-span-5' : 'aspect-[16/10] md:col-span-7'} ${
                    flip ? (tall ? 'md:col-start-8' : 'md:col-start-6') : ''
                  } ${flip ? 'md:order-2' : ''}`}
                  style={{ viewTransitionName: `work-${p.slug}` }}
                >
                  <div className="rv-curtain absolute inset-0">
                    <div className="absolute inset-0" style={p.crop ? { transform: `scale(${p.crop})` } : undefined}>
                    <Image
                      src={p.img}
                      alt={p.alt}
                      fill
                      placeholder="blur"
                      blurDataURL={p.blur}
                      quality={82}
                      sizes={tall ? '(min-width: 768px) 42vw, 100vw' : '(min-width: 768px) 58vw, 100vw'}
                      className="object-cover transition-transform duration-[1.2s] ease-[var(--ease-out-expo)] group-hover:scale-[1.04]"
                      style={{ objectPosition: p.pos }}
                    />
                    </div>
                  </div>
                </Reveal>

                <div className={`md:col-span-4 ${flip ? 'md:order-1 md:col-start-1' : tall ? 'md:col-start-8' : 'md:col-start-9'}`}>
                  <p className="text-[15px] font-medium text-accent">{p.tag}</p>
                  <h2 id={`t-${p.slug}`} className="t-card mt-3">
                    {p.title}
                  </h2>
                  <p className="mt-3 text-[14px] text-muted-foreground">Concept studio, {p.year}</p>
                  <p className="mt-6 text-[17px] leading-relaxed text-foreground/85">{fr(p.idea)}</p>
                  <h3 className="mt-8 text-[15px] font-semibold">Pistes explorées</h3>
                  <ul className="mt-3 flex flex-wrap gap-2">
                    {p.explored.map((e) => (
                      <li key={e} className="rounded-full border border-line px-3.5 py-1.5 text-[14px] text-foreground/85">
                        {e}
                      </li>
                    ))}
                  </ul>
                </div>
              </article>
            </li>
          )
        })}
      </ol>
    </>
  )
}
