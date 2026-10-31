import Image from 'next/image'
import { Reveal, SplitWords } from './reveal'

type Project = {
  n: string
  name: string
  serif: string
  discipline: string
  year: string
  img: string
  alt: string
  layout: 'wide' | 'cinema' | 'offset' | 'tall'
  note: string
}

const PROJECTS: Project[] = [
  {
    n: '01',
    name: 'Kpèvi',
    serif: 'Records',
    discipline: 'Identité visuelle',
    year: '2026',
    img: '/work/kpevi.png',
    alt: 'Système d’identité pour un label afro-électronique : pochettes, affiches et autocollants bleu outremer',
    layout: 'wide',
    note: 'Un label afro-électronique et un logo-cercle qui tourne comme un vinyle — décliné de la pochette au sticker.',
  },
  {
    n: '02',
    name: 'Ganvié',
    serif: 'l’heure bleue',
    discipline: 'Motion design — Générique',
    year: '2026',
    img: '/work/ganvie.png',
    alt: 'Image de film stylisée d’un village lacustre sur pilotis à l’heure bleue, soleil vermillon',
    layout: 'cinema',
    note: 'Générique d’ouverture pour un festival de cinéma imaginaire : 45 secondes de lumière sur le lac Nokoué.',
  },
  {
    n: '03',
    name: 'Atelier',
    serif: 'Dàxó',
    discipline: 'Site e-commerce',
    year: '2026',
    img: '/work/daxo.png',
    alt: 'Maquettes d’un site e-commerce pour un atelier textile, écrans mobile et desktop',
    layout: 'offset',
    note: 'Une boutique en ligne où chaque tissu se déroule au défilement, pensée d’abord pour le mobile.',
  },
  {
    n: '04',
    name: 'Biennale',
    serif: 'Cotonou Design',
    discipline: 'Campagne d’affichage',
    year: '2026',
    img: '/work/biennale.png',
    alt: 'Affiches typographiques jaune acide collées sur un mur ensoleillé à Cotonou',
    layout: 'tall',
    note: 'Des lettres qui se déforment sous le soleil : une campagne pensée pour la rue, déclinée en motion.',
  },
]

const LAYOUT: Record<Project['layout'], { figure: string; ratio: string; text: string }> = {
  wide: { figure: 'md:col-span-8', ratio: 'aspect-[4/3] md:aspect-[16/11]', text: 'md:col-span-4 md:self-end' },
  cinema: { figure: 'md:col-span-12', ratio: 'aspect-[4/3] md:aspect-[21/9]', text: 'md:col-span-6 md:col-start-7' },
  offset: { figure: 'md:col-span-7 md:col-start-6 md:order-2', ratio: 'aspect-[4/3] md:aspect-[4/3]', text: 'md:col-span-4 md:order-1 md:self-start md:pt-24' },
  tall: { figure: 'md:col-span-5 md:col-start-2', ratio: 'aspect-[4/5]', text: 'md:col-span-5 md:col-start-8 md:self-center' },
}

export function Work() {
  return (
    <section id="travaux" aria-labelledby="travaux-title" className="relative px-4 py-28 md:px-8 md:py-40">
      <Reveal className="mb-20 flex flex-col gap-8 md:mb-32 md:flex-row md:items-end md:justify-between">
        <h2 id="travaux-title" className="text-[16vw] font-extrabold uppercase leading-[0.82] tracking-[-0.04em] [font-variation-settings:'wdth'_68] md:text-[11vw]">
          <SplitWords text="Travaux" />
          <sup className="ml-2 align-top font-serif text-[0.25em] font-normal normal-case italic tracking-normal text-accent [font-variation-settings:normal]">
            (04)
          </sup>
        </h2>
        <div className="rv-fade max-w-sm border-l-2 border-accent pl-4 text-sm leading-relaxed text-muted-foreground">
          <p className="mb-1 text-[11px] font-semibold uppercase tracking-[0.16em] text-foreground">Concepts studio</p>
          Les projets présentés ci-dessous sont des concepts d’exploration conçus par NEXORA pour illustrer sa démarche. Ils seront remplacés par les réalisations clients.
        </div>
      </Reveal>

      <div className="flex flex-col gap-28 md:gap-44">
        {PROJECTS.map((p) => {
          const l = LAYOUT[p.layout]
          return (
            <Reveal as="article" key={p.n} threshold={0.15} className="group grid grid-cols-1 gap-6 md:grid-cols-12 md:gap-x-6" aria-labelledby={`p-${p.n}`}>
              <figure className={`${l.figure}`} data-cursor="Concept">
                <div className={`rv-clip relative overflow-hidden ${l.ratio}`}>
                  <Image src={p.img} alt={p.alt} fill sizes="(min-width: 768px) 70vw, 100vw" className="art-img object-cover" />
                  <span className="absolute left-3 top-3 rounded-full bg-background/85 px-3 py-1 text-[10px] font-semibold uppercase tracking-[0.16em] text-foreground backdrop-blur">
                    Concept
                  </span>
                </div>
              </figure>

              <div className={`flex flex-col gap-4 ${l.text}`}>
                <div className="rv-fade flex items-center justify-between border-b border-line pb-3 text-[11px] uppercase tracking-[0.16em] text-muted-foreground">
                  <span>
                    <span className="text-accent">{p.n}</span> — {p.discipline}
                  </span>
                  <span>{p.year}</span>
                </div>
                <h3 id={`p-${p.n}`} className="text-[12vw] font-extrabold uppercase leading-[0.86] tracking-[-0.03em] [font-variation-settings:'wdth'_74] md:text-[5vw]">
                  <SplitWords text={p.name} />
                  <br />
                  <span className="font-serif font-normal normal-case italic tracking-normal [font-variation-settings:normal]">
                    <SplitWords text={p.serif} offset={1} />
                  </span>
                </h3>
                <p className="rv-fade max-w-sm text-sm leading-relaxed text-muted-foreground" style={{ '--delay': '350ms' } as React.CSSProperties}>
                  {p.note}
                </p>
              </div>
            </Reveal>
          )
        })}
      </div>
    </section>
  )
}
