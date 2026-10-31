import { ArrowUpRight } from 'lucide-react'
import { LocalTime } from './local-time'
import { Reveal, SplitWords } from './reveal'

const LINKS = [
  { label: 'Instagram', href: '#' },
  { label: 'Behance', href: '#' },
  { label: 'LinkedIn', href: '#' },
  { label: 'WhatsApp', href: '#' },
]

export function Contact() {
  return (
    <section id="contact" aria-labelledby="contact-title" className="relative px-4 pb-32 pt-28 md:px-8 md:pb-16 md:pt-40">
      <Reveal className="grid grid-cols-1 gap-12 md:grid-cols-12">
        <p className="text-[11px] uppercase tracking-[0.16em] text-muted-foreground md:col-span-2">(Contact)</p>

        <div className="md:col-span-10">
          <h2 id="contact-title" className="text-[17vw] font-extrabold uppercase leading-[0.8] tracking-[-0.04em] [font-variation-settings:'wdth'_66] md:text-[12vw]">
            <SplitWords text="Un projet ?" />
            <br />
            <span className="font-serif font-normal normal-case italic tracking-normal text-accent [font-variation-settings:normal]">
              <SplitWords text="Mettons-le en mouvement." offset={2} />
            </span>
          </h2>

          <div className="rv-fade mt-14 flex flex-col gap-10 md:mt-20 md:flex-row md:items-end md:justify-between">
            <a
              href="mailto:bonjour@nexora.bj"
              className="group inline-flex items-center gap-4 border-b-2 border-foreground pb-2 text-3xl font-semibold tracking-tight transition-colors hover:border-accent hover:text-accent md:text-6xl"
            >
              bonjour@nexora.bj
              <ArrowUpRight className="size-8 transition-transform duration-500 group-hover:-translate-y-1 group-hover:translate-x-1 md:size-14" aria-hidden />
            </a>

            <a
              href="mailto:bonjour@nexora.bj?subject=Nouveau%20projet"
              className="group relative flex size-36 shrink-0 items-center justify-center self-start rounded-full bg-accent text-center text-sm font-semibold uppercase tracking-wider text-accent-foreground transition-transform duration-500 hover:scale-105 md:size-44 md:self-auto"
            >
              <span className="transition-transform duration-500 group-hover:-rotate-6">
                Démarrer
                <br />
                un projet
              </span>
            </a>
          </div>

          <div className="rv-fade mt-20 grid grid-cols-2 gap-8 border-t border-line pt-8 text-sm md:grid-cols-4" style={{ '--delay': '400ms' } as React.CSSProperties}>
            <div>
              <p className="mb-2 text-[11px] uppercase tracking-[0.16em] text-muted-foreground">Studio</p>
              <p>Cotonou, Bénin</p>
              <p className="text-muted-foreground">
                <LocalTime /> — heure locale
              </p>
            </div>
            <div>
              <p className="mb-2 text-[11px] uppercase tracking-[0.16em] text-muted-foreground">Nouveaux projets</p>
              <p>Réponse sous 48 h</p>
              <p className="text-muted-foreground">Français · English</p>
            </div>
            <div className="col-span-2">
              <p className="mb-2 text-[11px] uppercase tracking-[0.16em] text-muted-foreground">Suivre le mouvement</p>
              <ul className="flex flex-wrap gap-x-6 gap-y-1">
                {LINKS.map((l) => (
                  <li key={l.label}>
                    <a href={l.href} className="link-line">
                      {l.label}
                    </a>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </Reveal>
    </section>
  )
}

export function Footer() {
  return (
    <footer className="relative overflow-hidden border-t border-line px-4 pt-8 md:px-8">
      <div className="flex flex-col justify-between gap-2 text-[11px] uppercase tracking-[0.16em] text-muted-foreground md:flex-row">
        <p>© 2026 NEXORA — Studio créatif en mouvement</p>
        <p>Conçu et animé au Bénin</p>
        <a href="#top" className="link-line self-start">
          Retour en haut ↑
        </a>
      </div>
      <p aria-hidden className="outline-text-fg mt-6 translate-y-[18%] select-none text-center text-[26vw] font-extrabold uppercase leading-[0.8] tracking-[-0.03em] [font-variation-settings:'wdth'_100]">
        Nexora
      </p>
    </footer>
  )
}
