'use client'

import { useEffect, useRef, useState } from 'react'
import { fr } from './fr'
import { Reveal, SplitWords } from './reveal'

const STEPS = [
  {
    title: 'Écouter',
    text: 'Un premier échange pour comprendre votre marque, votre public et ce que le projet doit accomplir.',
    out: ['Objectifs', 'Public', 'Calendrier'],
  },
  {
    title: 'Concevoir',
    text: 'Une direction créative claire, présentée et ajustée avec vous avant toute production.',
    out: ['Pistes créatives', 'Direction artistique', 'Validation'],
  },
  {
    title: 'Créer',
    text: 'Identité, mouvement, interface : nous produisons et itérons, avec des points d’étape réguliers.',
    out: ['Production', 'Itérations', 'Points d’étape'],
  },
  {
    title: 'Livrer',
    text: 'Des fichiers prêts à l’emploi, un site en ligne et un accompagnement pour la suite.',
    out: ['Fichiers sources', 'Mise en ligne', 'Suivi'],
  },
]

export function Method() {
  const [active, setActive] = useState(0)
  const stepsRef = useRef<(HTMLLIElement | null)[]>([])

  useEffect(() => {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) setActive(Number((e.target as HTMLElement).dataset.step))
        })
      },
      { rootMargin: '-45% 0px -45% 0px' },
    )
    stepsRef.current.forEach((el) => el && io.observe(el))
    return () => io.disconnect()
  }, [])

  return (
    <section id="methode" aria-labelledby="methode-title" className="relative border-t border-line px-4 py-28 md:px-8 md:py-36">
      <div className="grid gap-12 md:grid-cols-12">
        <div className="md:sticky md:top-28 md:col-span-5 md:h-fit">
          <Reveal>
            <h2 id="methode-title" className="t-section">
              <SplitWords text="Du brief" />
              <br />
              <SplitWords text="à l’image." offset={2} />
            </h2>
          </Reveal>

          <div className="mt-14 hidden md:block" aria-hidden>
            <div className="font-wide h-[0.9em] overflow-hidden text-[clamp(6rem,11vw,10rem)] font-black leading-[0.9] tracking-[-0.05em]">
              <div className="transition-transform duration-700 ease-[var(--ease-out-expo)]" style={{ transform: `translateY(${-active * 0.9}em)` }}>
                {STEPS.map((_, i) => (
                  <div key={i} className={`h-[0.9em] ${i === active ? 'text-accent' : 'text-foreground/20'}`}>
                    {String(i + 1).padStart(2, '0')}
                  </div>
                ))}
              </div>
            </div>
            <div className="mt-8 grid max-w-sm grid-cols-4 gap-2">
              {STEPS.map((_, i) => (
                <span key={i} className="h-1 overflow-hidden rounded-full bg-foreground/15">
                  <span
                    className="block h-full origin-left rounded-full bg-accent transition-transform duration-700 ease-[var(--ease-out-expo)]"
                    style={{ transform: `scaleX(${i <= active ? 1 : 0})` }}
                  />
                </span>
              ))}
            </div>
          </div>
        </div>

        <ol className="md:col-span-6 md:col-start-7">
          {STEPS.map((s, i) => (
            <li
              key={s.title}
              ref={(el) => {
                stepsRef.current[i] = el
              }}
              data-step={i}
              className="relative border-l border-line py-10 pl-8 md:flex md:min-h-[58svh] md:items-center md:border-l-0 md:py-0 md:pl-0"
            >
              <span aria-hidden className="absolute -left-[5px] top-12 size-[9px] rounded-full bg-accent md:hidden" />
              <div>
                <p className="font-mono text-[14px] text-accent md:hidden">Étape {i + 1} sur {STEPS.length}</p>
                <h3
                  className={`t-card mt-3 transition-colors duration-700 md:mt-0 ${
                    i === active ? '' : 'md:text-foreground/45'
                  }`}
                >
                  {s.title}
                </h3>
                <p className="mt-5 max-w-md text-[17px] leading-relaxed text-foreground/80 md:text-lg">{fr(s.text)}</p>
                <ul className="mt-6 flex flex-wrap gap-2">
                  {s.out.map((o) => (
                    <li key={o} className="rounded-full border border-line px-3.5 py-1.5 text-[14px] text-foreground/85">
                      {o}
                    </li>
                  ))}
                </ul>
              </div>
            </li>
          ))}
        </ol>
      </div>
    </section>
  )
}
