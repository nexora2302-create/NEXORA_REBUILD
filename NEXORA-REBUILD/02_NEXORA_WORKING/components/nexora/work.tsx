import Image from 'next/image'
import { ArrowIcon } from './icons'
import { Reveal, SplitWords } from './reveal'
import { Stack } from './stack'

type Project = {
  title: string
  tag: string
  year: string
  img: string
  alt: string
  note: string
  pos?: string
}

const PROJECTS: Project[] = [
  {
    title: 'Kpèvi Records', tag: 'Identité visuelle', year: '2026', img: '/work/kpevi.webp',
    alt: 'Système d’identité pour un label afro-électronique : pochettes, affiches et autocollants bleu outremer',
    note: 'Un label afro-électronique et un logo-cercle qui tourne comme un vinyle, décliné de la pochette au sticker.',
  },
  {
    title: 'Ganvié, l’heure bleue', tag: 'Motion design, générique', year: '2026', img: '/work/ganvie.webp',
    alt: 'Image de film stylisée d’un village lacustre sur pilotis à l’heure bleue, soleil vermillon',
    note: 'Générique d’ouverture pour un festival de cinéma imaginaire : 45 secondes de lumière sur le lac Nokoué.',
  },
  {
    title: 'Atelier Dàxó', tag: 'Site e-commerce', year: '2026', img: '/work/daxo.webp',
    alt: 'Maquettes d’un site e-commerce pour un atelier textile, écrans mobile et desktop',
    note: 'Une boutique en ligne où chaque tissu se déroule au défilement, pensée d’abord pour le mobile.',
  },
  {
    title: 'Biennale Cotonou Design', tag: 'Campagne d’affichage', year: '2026', img: '/work/biennale.webp',
    alt: 'Affiches typographiques jaune acide collées sur un mur ensoleillé à Cotonou',
    note: 'Des lettres qui se déforment sous le soleil : une campagne pensée pour la rue, déclinée en motion.',
  },
  {
    title: 'Sons d’Ancêtres', tag: 'Affiche de festival', year: '2026', img: '/work/p1.webp', pos: '50% 20%',
    alt: 'Affiche typographique d’un festival de musiques africaines : portrait en bleu et orange, formes géométriques',
    note: 'Une affiche pour un festival imaginaire : portrait, typographie découpée et motifs géométriques.',
  },
  {
    title: 'Kora Café', tag: 'Identité et packaging', year: '2026', img: '/work/p4.webp',
    alt: 'Packaging de café artisanal Kora : sachet kraft, carte et boîte, tissu indigo',
    note: 'Un système d’identité et de packaging pour un café béninois imaginaire.',
  },
  {
    title: 'Flux', tag: 'Film de marque, motion', year: '2025', img: '/work/p2.webp',
    alt: 'Image de motion design : ruban de lumière orange et ambre sur fond noir',
    note: 'Une exploration de matière lumineuse pour un film de marque.',
  },
  {
    title: 'Éliore', tag: 'Site e-commerce', year: '2025', img: '/work/p3.webp',
    alt: 'Maquette d’un site e-commerce de mode sur ordinateur portable, interface sombre',
    note: 'Un concept de boutique en ligne de mode, sobre et éditoriale.',
  },
]

const CARD = 'grid overflow-hidden rounded-[1.75rem] border border-line bg-card md:h-[min(74svh,680px)] md:grid-cols-12 origin-top will-change-[transform]'

export function Work() {
  const total = String(PROJECTS.length).padStart(2, '0')
  return (
    <section id="travaux" aria-labelledby="travaux-title" className="relative px-4 py-28 md:px-8 md:py-36">
      <Reveal className="mb-12 grid gap-6 md:mb-16 md:grid-cols-12 md:items-end">
        <h2 id="travaux-title" className="font-wide text-[11vw] font-black leading-[0.9] tracking-[-0.04em] md:col-span-8 md:text-[clamp(3.5rem,8vw,7.5rem)]">
          <SplitWords text="Réalisations" />
        </h2>
        <p className="max-w-sm text-[17px] leading-relaxed text-foreground/75 md:col-span-4">
          Des concepts d’exploration conçus par le studio pour montrer sa démarche, en attendant les premiers projets clients.
        </p>
      </Reveal>

      <Stack className="flex flex-col gap-6 md:gap-[12vh]">
        {PROJECTS.map((p, i) => (
          <li key={p.title} className="md:sticky" style={{ top: `calc(5.5rem + ${i * 0.9}rem)` }}>
            <article data-stack-card aria-labelledby={`p-${i}`} className={CARD}>
              <div className="relative aspect-[4/3] md:col-span-7 md:aspect-auto">
                <Image src={p.img} alt={p.alt} fill sizes="(min-width: 768px) 58vw, 100vw" className="object-cover" style={{ objectPosition: p.pos }} />
              </div>
              <div className="flex flex-col justify-between gap-10 p-6 md:col-span-5 md:p-10">
                <div className="flex items-center justify-between font-mono text-xs text-foreground/60">
                  <span>
                    {String(i + 1).padStart(2, '0')} / {total}
                  </span>
                  <span>Concept {p.year}</span>
                </div>
                <div>
                  <p className="text-[15px] font-medium text-accent">{p.tag}</p>
                  <h3 id={`p-${i}`} className="font-wide mt-3 text-[2.1rem] font-black leading-[0.95] tracking-[-0.03em] md:text-[clamp(2.2rem,3.4vw,3.4rem)]">
                    {p.title}
                  </h3>
                  <p className="mt-5 max-w-md text-[17px] leading-relaxed text-foreground/75">{p.note}</p>
                </div>
              </div>
            </article>
          </li>
        ))}
        <li className="md:sticky" style={{ top: `calc(5.5rem + ${PROJECTS.length * 0.9}rem)` }}>
          <div data-stack-card className="flex flex-col items-start justify-between gap-10 rounded-[1.75rem] border border-line bg-card p-6 md:h-[min(52svh,480px)] md:p-10">
            <p className="font-wide text-[2.4rem] font-black leading-[0.95] tracking-[-0.03em] md:text-[clamp(2.5rem,5vw,5rem)]">
              La prochaine,{' '}
              <span className="font-serif font-normal italic tracking-normal">c’est la vôtre.</span>
            </p>
            <a
              href="#contact"
              className="group inline-flex min-h-12 items-center gap-3 rounded-full bg-accent px-6 text-[15px] font-semibold text-accent-foreground transition-transform duration-500 hover:scale-[1.03]"
            >
              Parler de votre projet
              <ArrowIcon className="size-4 transition-transform duration-500 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
            </a>
          </div>
        </li>
      </Stack>
    </section>
  )
}
