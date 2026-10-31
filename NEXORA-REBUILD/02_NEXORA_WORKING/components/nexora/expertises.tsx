import Image from 'next/image'
import { Reveal, SplitWords } from './reveal'

const EXPERTISES = [
  {
    n: '01',
    word: 'Voir',
    title: 'Communication visuelle',
    line: 'Des identités qui se reconnaissent au premier regard.',
    items: ['Identité de marque', 'Direction artistique', 'Affiches & campagnes', 'Packaging', 'Contenus réseaux sociaux'],
    img: '/work/poster.webp',
  },
  {
    n: '02',
    word: 'Bouger',
    title: 'Motion design',
    line: 'Des images qui respirent, des marques qui prennent vie.',
    items: ['Logos animés', 'Films de marque', 'Génériques & titrages', 'Formats sociaux animés', 'Habillage vidéo'],
    img: '/work/motion.webp',
  },
  {
    n: '03',
    word: 'Habiter',
    title: 'Sites web',
    line: 'Des interfaces rapides, sensibles et mémorables.',
    items: ['Sites vitrines', 'E-commerce', 'Design d’interface', 'Expériences interactives', 'Développement & maintenance'],
    img: '/work/interface.webp',
  },
]

export function Expertises() {
  return (
    <section id="expertises" aria-labelledby="expertises-title" className="relative border-t border-line px-4 py-28 md:px-8 md:py-40">
      <div className="mb-6 flex items-baseline justify-between font-mono text-[11px] uppercase tracking-[0.18em] text-muted-foreground">
        <span aria-hidden>(02) — Expertises</span>
        <span className="hidden sm:inline">Un seul mouvement</span>
      </div>
      <Reveal>
        <h2 id="expertises-title" className="font-wide text-[11vw] font-black leading-[0.9] tracking-[-0.04em] md:text-[6vw]">
          <SplitWords text="Trois métiers," />
          <span className="font-serif font-normal italic tracking-normal">
            <SplitWords text="un seul" offset={2} />
          </span>
          <SplitWords text="mouvement." offset={4} />
        </h2>
        <p className="rv-fade mb-16 mt-6 max-w-xl text-sm leading-relaxed text-muted-foreground md:mb-20">
          Chaque projet traverse nos trois disciplines : l’identité donne le ton, le mouvement donne le rythme, le web donne la scène.
        </p>
      </Reveal>

      <ul>
        {EXPERTISES.map((x) => (
          <Reveal as="li" key={x.n} className="group relative border-t border-line">
            <div className="grid grid-cols-12 items-start gap-4 py-8 md:py-12">
              <span className="col-span-2 pt-3 font-mono text-[11px] tracking-[0.18em] text-muted-foreground md:col-span-1">{x.n}</span>

              <h3 className="col-span-10 overflow-hidden pb-[0.12em] md:col-span-6">
                <span className="rv-word block" style={{ '--i': 0 } as React.CSSProperties}>
                  <span
                    aria-hidden
                    className="font-wide block text-[16vw] font-black leading-[0.9] tracking-[-0.04em] transition-transform duration-700 ease-[cubic-bezier(0.16,1,0.3,1)] group-hover:translate-x-4 md:text-[8vw]"
                  >
                    {x.word}
                    <span className="text-accent">.</span>
                  </span>
                </span>
                <span className="sr-only">{x.word}. {x.title}</span>
              </h3>

              <div className="rv-fade col-span-12 md:col-span-4 md:col-start-9">
                <p className="font-serif text-2xl italic">{x.title}</p>
                <p className="mt-2 text-sm leading-relaxed text-muted-foreground">{x.line}</p>
                <ul className="mt-5 flex flex-wrap gap-2">
                  {x.items.map((it) => (
                    <li key={it} className="rounded-full border border-line px-3 py-1 font-mono text-[10px] uppercase tracking-[0.14em]">
                      <span aria-hidden className="text-accent">/</span>
                      {it}
                    </li>
                  ))}
                </ul>
              </div>

              <div className="relative col-span-12 aspect-[16/9] overflow-hidden md:hidden">
                <div className="rv-clip absolute inset-0">
                  <Image src={x.img} alt="" fill sizes="100vw" className="art-img object-cover" />
                </div>
              </div>
            </div>

            {/* Aperçu desktop : fixe, sans recouvrir le titre */}
            <div
              aria-hidden
              className="pointer-events-none absolute right-[36%] top-1/2 z-10 hidden aspect-[4/5] w-56 -translate-y-1/2 overflow-hidden transition-[clip-path,rotate] duration-700 ease-[cubic-bezier(0.77,0,0.18,1)] [clip-path:inset(50%)] group-hover:-rotate-[4deg] group-hover:[clip-path:inset(0)] md:block"
            >
              <Image src={x.img} alt="" fill sizes="224px" className="object-cover" />
            </div>
          </Reveal>
        ))}
        <li aria-hidden className="border-t border-line" />
      </ul>
    </section>
  )
}
