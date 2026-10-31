'use client'

import Image from 'next/image'
import { useRef, useState } from 'react'
import { Reveal, SplitWords } from './reveal'

const EXPERTISES = [
  {
    n: '01',
    title: 'Communication visuelle',
    short: 'Visuel',
    line: 'Des identités qui se reconnaissent au premier regard.',
    items: ['Identité de marque', 'Direction artistique', 'Affiches & campagnes', 'Packaging', 'Contenus réseaux sociaux'],
    img: '/work/poster.png',
  },
  {
    n: '02',
    title: 'Motion design',
    short: 'Motion',
    line: 'Des images qui respirent, des marques qui prennent vie.',
    items: ['Logos animés', 'Films de marque', 'Génériques & titrages', 'Formats sociaux animés', 'Habillage vidéo'],
    img: '/work/motion.png',
  },
  {
    n: '03',
    title: 'Sites web',
    short: 'Web',
    line: 'Des interfaces rapides, sensibles et mémorables.',
    items: ['Sites vitrines', 'E-commerce', 'Design d’interface', 'Expériences interactives', 'Développement & maintenance'],
    img: '/work/interface.png',
  },
]

export function Expertises() {
  const [active, setActive] = useState<number | null>(null)
  const previewRef = useRef<HTMLDivElement>(null)
  const listRef = useRef<HTMLUListElement>(null)

  const onMove = (e: React.PointerEvent) => {
    const list = listRef.current
    const preview = previewRef.current
    if (!list || !preview || e.pointerType !== 'mouse') return
    const r = list.getBoundingClientRect()
    preview.style.transform = `translate3d(${e.clientX - r.left}px, ${e.clientY - r.top}px, 0) translate(-50%, -50%)`
  }

  return (
    <section id="expertises" aria-labelledby="expertises-title" className="relative px-4 py-28 md:px-8 md:py-40">
      <Reveal className="mb-16 grid grid-cols-1 items-end gap-6 md:mb-24 md:grid-cols-12">
        <p className="text-[11px] uppercase tracking-[0.16em] text-muted-foreground md:col-span-2">(Expertises)</p>
        <h2 id="expertises-title" className="text-[13vw] font-extrabold uppercase leading-[0.85] tracking-[-0.03em] [font-variation-settings:'wdth'_72] md:col-span-7 md:text-[8vw]">
          <SplitWords text="Trois métiers," />
          <br />
          <span className="font-serif font-normal normal-case italic tracking-normal [font-variation-settings:normal]">
            <SplitWords text="un seul mouvement." offset={2} />
          </span>
        </h2>
        <p className="rv-fade max-w-xs text-sm leading-relaxed text-muted-foreground md:col-span-3">
          Chaque projet traverse nos trois disciplines : l’identité donne le ton, le mouvement donne le rythme, le web donne la scène.
        </p>
      </Reveal>

      <ul ref={listRef} onPointerMove={onMove} onPointerLeave={() => setActive(null)} className="relative border-t border-line">
        {/* Cursor-following preview (desktop) */}
        <div
          ref={previewRef}
          aria-hidden
          className="pointer-events-none absolute left-0 top-0 z-20 hidden h-[22vw] w-[17vw] md:block"
        >
          {EXPERTISES.map((x, i) => (
            <div
              key={x.n}
              className="absolute inset-0 overflow-hidden transition-[clip-path] duration-700 ease-[cubic-bezier(0.77,0,0.18,1)]"
              style={{ clipPath: active === i ? 'inset(0 0 0 0)' : 'inset(50% 50% 50% 50%)' }}
            >
              <Image src={x.img} alt="" fill sizes="17vw" className="object-cover" />
            </div>
          ))}
        </div>

        {EXPERTISES.map((x, i) => (
          <Reveal as="li" key={x.n} className="group relative border-b border-line" onPointerEnter={() => setActive(i)}>
            <div className="rv-line absolute inset-x-0 bottom-0 h-px bg-foreground" aria-hidden />
            <div className="grid grid-cols-12 gap-x-4 gap-y-6 py-8 md:py-12">
              <span className="col-span-2 font-serif text-2xl italic text-accent md:col-span-1 md:text-3xl">{x.n}</span>

              <h3 className="col-span-10 overflow-hidden md:col-span-6">
                <span className="rv-word block" style={{ '--i': 0 } as React.CSSProperties}>
                  <span className="block text-[11vw] font-extrabold uppercase leading-[0.88] tracking-[-0.03em] transition-[font-variation-settings,color,transform] duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] [font-variation-settings:'wdth'_70] group-hover:translate-x-4 group-hover:text-accent group-hover:[font-variation-settings:'wdth'_110] md:text-[5.2vw]">
                    {x.title}
                  </span>
                </span>
              </h3>

              <div className="relative col-span-12 aspect-[16/9] overflow-hidden md:hidden">
                <div className="rv-clip absolute inset-0">
                  <Image src={x.img} alt="" fill sizes="100vw" className="art-img object-cover" />
                </div>
              </div>

              <div className="rv-fade col-span-12 grid grid-cols-2 gap-4 md:col-span-5 md:grid-cols-5">
                <p className="col-span-2 font-serif text-2xl italic leading-tight md:col-span-3 md:text-3xl">{x.line}</p>
                <ul className="col-span-2 space-y-1 text-sm text-muted-foreground md:col-span-2">
                  {x.items.map((it) => (
                    <li key={it} className="flex gap-2">
                      <span aria-hidden className="text-accent">/</span>
                      {it}
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </Reveal>
        ))}
      </ul>
    </section>
  )
}
