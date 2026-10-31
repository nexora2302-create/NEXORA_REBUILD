import { ContactForm } from './contact-form'
import { UpIcon } from './icons'
import { LocalTime } from './local-time'
import { Reveal, SplitWords } from './reveal'

export function Contact() {
  return (
    <section id="contact" aria-labelledby="contact-title" className="theme-signal relative px-4 py-24 md:px-8 md:py-32">
      <div className="grid gap-14 md:grid-cols-12">
        <div className="md:col-span-6">
          <Reveal>
            <h2 id="contact-title" className="font-wide text-[12vw] font-black leading-[0.9] tracking-[-0.045em] md:text-[clamp(3.2rem,6.2vw,6.6rem)]">
              <SplitWords text="Un" />
              <span className="inline-block overflow-hidden pb-[0.08em] align-bottom">
                <span className="rv-word" style={{ '--i': 1 } as React.CSSProperties}>
                  {'projet\u00A0?'}
                </span>
              </span>
              <br />
              <span className="font-serif font-normal italic tracking-normal">
                <SplitWords text="Mettons-le en mouvement." offset={2} />
              </span>
            </h2>
          </Reveal>
          <a href="mailto:bonjour@nexora.bj" className="link-line mt-10 inline-block font-serif text-3xl italic md:text-4xl">
            bonjour@nexora.bj
          </a>
          <dl className="mt-10 grid max-w-md grid-cols-2 gap-6 text-[15px]">
            <div>
              <dt className="font-medium">Studio</dt>
              <dd className="mt-1 text-muted-foreground">
                Cotonou, Bénin
                <br />
                <span className="font-mono text-[14px]">
                  <LocalTime /> heure locale
                </span>
              </dd>
            </div>
            <div>
              <dt className="font-medium">Langues</dt>
              <dd className="mt-1 text-muted-foreground">Français et anglais</dd>
            </div>
          </dl>
        </div>
        <div className="md:col-span-6 md:pt-4">
          <ContactForm />
        </div>
      </div>
    </section>
  )
}

const LINKS: [string, string][] = [
  ['Expertises', '#expertises'],
  ['Réalisations', '#travaux'],
  ['Méthode', '#methode'],
  ['FAQ', '#faq'],
]

export function Footer() {
  return (
    <footer className="px-4 pb-8 pt-10 md:px-8">
      <div className="flex flex-col gap-6 md:flex-row md:items-center md:justify-between">
        <a href="#top" className="font-wide inline-flex min-h-11 items-center text-lg font-black tracking-tight" aria-label="NX® NEXORA, retour en haut">
          NX<sup className="text-[0.55em] font-bold">®</sup>
        </a>
        <nav aria-label="Pied de page">
          <ul className="flex flex-wrap gap-x-6 text-[14px] text-foreground/80">
            {LINKS.map(([l, h]) => (
              <li key={h}>
                <a href={h} className="link-line inline-flex min-h-11 items-center">
                  {l}
                </a>
              </li>
            ))}
          </ul>
        </nav>
        <a href="#top" className="group inline-flex min-h-11 items-center gap-2 self-start text-[14px] text-foreground/80 md:self-auto">
          Retour en haut
          <span className="grid size-9 place-items-center rounded-full border border-line transition-colors group-hover:border-accent group-hover:text-accent">
            <UpIcon className="size-3.5" />
          </span>
        </a>
      </div>
      <div className="mt-6 flex flex-col gap-1 border-t border-line pt-6 text-[13px] text-muted-foreground sm:flex-row sm:justify-between">
        <p>© 2026 NEXORA, studio créatif à Cotonou</p>
        <a href="mailto:bonjour@nexora.bj" className="link-line self-start">bonjour@nexora.bj</a>
      </div>
    </footer>
  )
}
