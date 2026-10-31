import Image from 'next/image'
import { ParallaxLayer } from './parallax'
import { Reveal, SplitWords } from './reveal'

type Project = {
  n: string
  title: string
  tag: string
  year: string
  img: string
  alt: string
  note: string
  cls: string
  ratio: string
  sizes: string
}

const WIDE = '(min-width: 768px) 62vw, 100vw'
const MID = '(min-width: 768px) 46vw, 100vw'
const NARROW = '(min-width: 768px) 34vw, 100vw'

const PROJECTS: Project[] = [
  {
    n: '01', title: 'Kpèvi Records', tag: 'Identité visuelle', year: '2026', img: '/work/kpevi.webp',
    alt: 'Système d’identité pour un label afro-électronique : pochettes, affiches et autocollants bleu outremer',
    note: 'Un label afro-électronique et un logo-cercle qui tourne comme un vinyle — décliné de la pochette au sticker.',
    cls: 'md:col-span-5', ratio: 'aspect-[4/5]', sizes: MID,
  },
  {
    n: '02', title: 'Ganvié l’heure bleue', tag: 'Motion design — Générique', year: '2026', img: '/work/ganvie.webp',
    alt: 'Image de film stylisée d’un village lacustre sur pilotis à l’heure bleue, soleil vermillon',
    note: 'Générique d’ouverture pour un festival de cinéma imaginaire : 45 secondes de lumière sur le lac Nokoué.',
    cls: 'md:col-span-6 md:col-start-7 md:mt-48', ratio: 'aspect-[4/5]', sizes: MID,
  },
  {
    n: '03', title: 'Atelier Dàxó', tag: 'Site e-commerce', year: '2026', img: '/work/daxo.webp',
    alt: 'Maquettes d’un site e-commerce pour un atelier textile, écrans mobile et desktop',
    note: 'Une boutique en ligne où chaque tissu se déroule au défilement, pensée d’abord pour le mobile.',
    cls: 'md:col-span-8 md:col-start-3', ratio: 'aspect-[16/10]', sizes: WIDE,
  },
  {
    n: '04', title: 'Biennale Cotonou Design', tag: 'Campagne d’affichage', year: '2026', img: '/work/biennale.webp',
    alt: 'Affiches typographiques jaune acide collées sur un mur ensoleillé à Cotonou',
    note: 'Des lettres qui se déforment sous le soleil : une campagne pensée pour la rue, déclinée en motion.',
    cls: 'md:col-span-7', ratio: 'aspect-[16/11]', sizes: WIDE,
  },
  {
    n: '05', title: 'Sons d’Ancêtres', tag: 'Affiche festival', year: '2026', img: '/work/p1.webp',
    alt: 'Affiche typographique d’un festival de musiques africaines : portrait en bleu et orange, formes géométriques',
    note: 'Une affiche pour un festival imaginaire : portrait, typographie découpée et motifs géométriques.',
    cls: 'md:col-span-4 md:col-start-9 md:mt-32', ratio: 'aspect-[4/5]', sizes: NARROW,
  },
  {
    n: '06', title: 'Kora Café', tag: 'Identité & packaging', year: '2026', img: '/work/p4.webp',
    alt: 'Packaging de café artisanal Kora : sachet kraft, carte et boîte, tissu indigo',
    note: 'Un système d’identité et de packaging pour un café béninois imaginaire.',
    cls: 'md:col-span-5', ratio: 'aspect-[4/5]', sizes: MID,
  },
  {
    n: '07', title: 'Flux', tag: 'Film de marque — Motion', year: '2025', img: '/work/p2.webp',
    alt: 'Image de motion design : ruban de lumière orange et ambre sur fond noir',
    note: 'Une exploration de matière lumineuse pour un film de marque.',
    cls: 'md:col-span-6 md:col-start-7 md:mt-40', ratio: 'aspect-[16/10]', sizes: MID,
  },
  {
    n: '08', title: 'Éliore', tag: 'Site e-commerce', year: '2025', img: '/work/p3.webp',
    alt: 'Maquette d’un site e-commerce de mode sur ordinateur portable, interface sombre',
    note: 'Un concept de boutique en ligne de mode, sobre et éditoriale.',
    cls: 'md:col-span-8 md:col-start-2', ratio: 'aspect-[16/11]', sizes: WIDE,
  },
]

export function Work() {
  return (
    <section id="travaux" aria-labelledby="travaux-title" className="relative px-4 pb-28 pt-28 md:px-8 md:pb-40 md:pt-40">
      <Reveal className="mb-12 md:mb-24">
        <p className="font-mono text-[11px] uppercase tracking-[0.18em] text-muted-foreground">(03) — Concepts studio</p>
        <h2 id="travaux-title" className="font-wide mt-4 text-[13vw] font-black leading-[0.85] tracking-[-0.04em] md:text-[9vw]">
          <SplitWords text="Travaux" />
          <sup className="ml-2 align-top font-mono text-[0.2em] font-normal tracking-normal text-accent">(08)</sup>
        </h2>
        <p className="rv-fade mt-6 max-w-xl text-sm leading-relaxed text-muted-foreground">
          Les projets présentés ci-dessous sont des concepts d’exploration conçus par NEXORA pour illustrer sa démarche. Ils seront remplacés par les réalisations clients.
        </p>
      </Reveal>

      <div className="grid gap-y-20 md:grid-cols-12 md:gap-x-8">
        {PROJECTS.map((p) => (
          <Reveal as="article" key={p.n} threshold={0.12} className={p.cls} aria-labelledby={`p-${p.n}`}>
            <a href="#contact" data-cursor="Concept" className="group block">
              <div className={`rv-clip relative overflow-hidden ${p.ratio}`}>
                <ParallaxLayer>
                  <Image src={p.img} alt={p.alt} fill sizes={p.sizes} className="art-img object-cover" />
                </ParallaxLayer>
                <span className="absolute left-4 top-4 z-10 rounded-full bg-background px-3 py-1 font-mono text-[11px] uppercase tracking-[0.16em]">
                  {p.n} / {p.year}
                </span>
                <span className="absolute right-4 top-4 z-10 rounded-full bg-accent px-3 py-1 font-mono text-[11px] font-semibold uppercase tracking-[0.16em] text-accent-foreground">
                  Concept
                </span>
              </div>
              <div className="rv-fade mt-4 border-b border-line pb-4">
                <div className="flex flex-wrap items-baseline justify-between gap-x-4 gap-y-1">
                  <h3 id={`p-${p.n}`} className="font-wide min-w-0 text-3xl font-black tracking-tight md:text-4xl xl:text-5xl">
                    {p.title}
                    <span aria-hidden className="inline-block text-accent transition-transform duration-500 group-hover:-translate-y-2 group-hover:translate-x-2">↗</span>
                  </h3>
                  <span className="hidden text-right font-mono text-[11px] uppercase tracking-[0.16em] text-muted-foreground sm:block">{p.tag}</span>
                </div>
                <p className="mt-3 max-w-lg text-sm leading-relaxed text-muted-foreground">{p.note}</p>
              </div>
            </a>
          </Reveal>
        ))}
      </div>
    </section>
  )
}
