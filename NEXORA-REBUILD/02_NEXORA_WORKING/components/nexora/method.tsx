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

const DURATION = 5200

export function Method() {
  const [active, setActive] = useState(0)
  const [auto, setAuto] = useState(true)
  const [visible, setVisible] = useState(false)
  const listRef = useRef<HTMLOListElement>(null)

  // Lecture automatique tant que la section est visible et que personne n'a choisi d'étape.
  useEffect(() => {
    const el = listRef.current
    if (!el) return
    const io = new IntersectionObserver(([e]) => setVisible(e.isIntersecting), { threshold: 0.45 })
    io.observe(el)
    return () => io.disconnect()
  }, [])

  useEffect(() => {
    if (!auto || !visible || !window.matchMedia('(min-width: 1024px) and (prefers-reduced-motion: no-preference)').matches) return
    const id = setTimeout(() => setActive((a) => (a + 1) % STEPS.length), DURATION)
    return () => clearTimeout(id)
  }, [active, auto, visible])

  const choose = (i: number) => {
    setAuto(false)
    setActive(i)
  }

  return (
    <section id="methode" data-header="paper" aria-labelledby="methode-title" className="theme-paper relative px-4 py-28 md:px-8 md:py-36">
      <Reveal className="mb-12 grid gap-6 md:mb-16 md:grid-cols-12 md:items-end">
        <h2 id="methode-title" className="t-section md:col-span-8">
          <SplitWords text="Du brief" />
          <br />
          <SplitWords text="à l’image." offset={2} />
        </h2>
        <p className="max-w-xs text-[17px] leading-relaxed md:col-span-4 md:col-start-10 md:pb-3">
          Quatre temps, avec vous à chaque étape.
        </p>
      </Reveal>

      <ol
        ref={listRef}
        className="flex flex-col gap-3 lg:h-[min(68svh,600px)] lg:min-h-[480px] lg:flex-row"
        style={{ '--dur': `${DURATION}ms` } as React.CSSProperties}
      >
        {STEPS.map((s, i) => {
          const on = i === active
          return (
            <li
              key={s.title}
              data-on={on}
              className={`method-panel relative flex min-w-0 flex-col overflow-hidden rounded-[1.5rem] bg-[#e2dacb] transition-[flex-grow,background-color,color] duration-700 ease-[var(--ease-out-expo)] lg:basis-0 lg:rounded-[1.75rem] ${
                on ? 'lg:grow-[2.2] lg:bg-[#0d0c0b] lg:text-[#ece5d8]' : 'lg:grow'
              }`}
              onPointerEnter={(e) => e.pointerType === 'mouse' && choose(i)}
            >
              <h3 className="font-wide text-[2rem] font-extrabold leading-none tracking-[-0.03em] lg:text-[clamp(1.25rem,2vw,2.4rem)]">
                <button
                  type="button"
                  aria-pressed={on}
                  onClick={() => choose(i)}
                  className="flex w-full flex-col items-start gap-3 p-6 text-left lg:p-7"
                >
                  <span className="text-[15px] font-medium tracking-normal tabular-nums opacity-75" style={{ fontVariationSettings: "'wdth' 100" }}>
                    Étape {i + 1} sur {STEPS.length}
                  </span>
                  <span className="method-title">
                    {s.title}
                    <span className="method-dot">.</span>
                  </span>
                </button>
              </h3>

              <div className="method-copy mt-auto px-6 pb-6 lg:w-[min(34rem,40vw)] lg:px-7 lg:pb-8">
                <p aria-hidden className="font-wide mb-8 hidden text-[clamp(3.5rem,6.4vw,7rem)] font-black leading-[0.9] tracking-[-0.045em] lg:block">
                  {s.title}
                  <span className="text-[#ff4a1c]">.</span>
                </p>
                <p className="text-[17px] leading-relaxed lg:text-lg">{fr(s.text)}</p>
                <ul className="mt-5 flex flex-wrap gap-2">
                  {s.out.map((o) => (
                    <li key={o} className="rounded-full border border-current/25 px-3.5 py-1.5 text-[14px]">
                      {o}
                    </li>
                  ))}
                </ul>
              </div>

              {/* Avancée de la lecture automatique */}
              {on && auto && visible && (
                <span aria-hidden className="absolute inset-x-0 bottom-0 hidden h-1 bg-[#ece5d8]/10 lg:block">
                  <span key={active} className="method-progress block h-full origin-left bg-[#ff4a1c]" />
                </span>
              )}
            </li>
          )
        })}
      </ol>
    </section>
  )
}
