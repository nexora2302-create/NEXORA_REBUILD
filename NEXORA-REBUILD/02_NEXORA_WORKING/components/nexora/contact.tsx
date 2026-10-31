import { ContactForm } from './contact-form'
import { LocalTime } from './local-time'
import { Reveal, SplitWords } from './reveal'

export function Contact() {
  return (
    <section id="contact" aria-labelledby="contact-title" className="relative px-4 pb-32 pt-28 md:px-8 md:pb-16 md:pt-40">
      <Reveal className="grid grid-cols-1 gap-12 md:grid-cols-12">
        <p className="font-mono text-[11px] uppercase tracking-[0.16em] text-muted-foreground md:col-span-2">(Contact)</p>

        <div className="md:col-span-10">
          <h2 id="contact-title" className="text-[17vw] font-extrabold uppercase leading-[0.8] tracking-[-0.04em] [font-variation-settings:'wdth'_66] md:text-[12vw]">
            <SplitWords text="Un projet ?" />
            <br />
            <span className="font-serif font-normal normal-case italic tracking-normal text-accent [font-variation-settings:normal]">
              <SplitWords text="Mettons-le en mouvement." offset={2} />
            </span>
          </h2>

          <div className="rv-fade mt-14 md:mt-20">
            <a
              href="mailto:bonjour@nexora.bj"
              className="group inline-flex items-center gap-4 border-b-2 border-foreground pb-2 text-3xl font-semibold tracking-tight transition-colors hover:border-accent hover:text-accent md:text-6xl"
            >
              bonjour@nexora.bj
              <span aria-hidden className="transition-transform duration-500 group-hover:-translate-y-1 group-hover:translate-x-1">↗</span>
            </a>


          </div>

          <div className="rv-fade mt-16 md:mt-24">
            <ContactForm />
          </div>

          <div className="rv-fade mt-20 grid grid-cols-2 gap-8 border-t border-line pt-8 text-sm md:grid-cols-2" style={{ '--delay': '400ms' } as React.CSSProperties}>
            <div>
              <p className="mb-2 font-mono text-[11px] uppercase tracking-[0.16em] text-muted-foreground">Studio</p>
              <p>Cotonou, Bénin</p>
              <p className="text-muted-foreground">
                <LocalTime /> — heure locale
              </p>
            </div>
            <div>
              <p className="mb-2 font-mono text-[11px] uppercase tracking-[0.16em] text-muted-foreground">Nouveaux projets</p>
              <p>Réponse sous 48 h</p>
              <p className="text-muted-foreground">Français · English</p>
            </div>
          </div>
        </div>
      </Reveal>
    </section>
  )
}

export function Footer() {
  return (
    <footer className="relative overflow-hidden border-t border-line px-4 pt-10 md:px-8">
      <div className="grid grid-cols-2 gap-8 font-mono text-[11px] uppercase tracking-[0.16em] md:grid-cols-12">
        <p className="col-span-2 text-muted-foreground md:col-span-4">
          NEXORA — Studio créatif en mouvement
          <br />
          Communication visuelle · Motion design · Web
        </p>
        <nav aria-label="Pied de page" className="md:col-span-4 md:col-start-6">
          <ul className="space-y-2">
            {[['Expertises', '#expertises'], ['Travaux', '#travaux'], ['Méthode', '#methode'], ['FAQ', '#faq'], ['Contact', '#contact']].map(([l, h]) => (
              <li key={h}><a href={h} className="link-line">{l}</a></li>
            ))}
          </ul>
        </nav>
        <div className="md:col-span-3 md:text-right">
          <a href="mailto:bonjour@nexora.bj" className="link-line">bonjour@nexora.bj</a>
          <p className="mt-2 text-muted-foreground">Cotonou, Bénin</p>
        </div>
      </div>
      <div className="mt-10 flex flex-col justify-between gap-2 border-t border-line pt-4 font-mono text-[11px] uppercase tracking-[0.16em] text-muted-foreground md:flex-row">
        <p>© 2026 NEXORA</p>
        <p>Conçu et animé au Bénin</p>
        <a href="#top" className="link-line self-start">Retour en haut ↑</a>
      </div>
      <p aria-hidden className="outline-text-fg mt-6 translate-y-[18%] select-none text-center text-[26vw] font-extrabold uppercase leading-[0.8] tracking-[-0.03em] [font-variation-settings:'wdth'_100]">
        Nexora
      </p>
    </footer>
  )
}
