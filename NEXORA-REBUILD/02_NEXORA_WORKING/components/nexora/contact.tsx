import { ContactForm } from './contact-form'
import { LocalTime } from './local-time'
import { Reveal, SplitWords } from './reveal'

export function Contact() {
  return (
    <section id="contact" aria-labelledby="contact-title" className="theme-paper relative overflow-hidden px-4 pb-24 pt-24 md:px-8 md:pb-32 md:pt-32">
      <Reveal>
        <p className="font-mono text-[11px] uppercase tracking-[0.18em] opacity-60">(06) — Contact</p>
        <h2 id="contact-title" className="font-wide mt-8 text-[11.5vw] font-black leading-[0.85] tracking-[-0.05em] md:text-[9vw]">
          <SplitWords text="Un" />
          <span className="inline-block overflow-hidden pb-[0.08em] align-bottom">
            <span className="rv-word" style={{ '--i': 1 } as React.CSSProperties}>
              projet<span className="text-accent">?</span>
            </span>
          </span>
          <br />
          <span className="font-serif font-normal italic tracking-normal">
            <SplitWords text="Mettons-le" offset={2} />
          </span>
          <SplitWords text="en mouvement." offset={3} />
        </h2>

        <div className="rv-fade mt-12 flex flex-wrap items-center justify-between gap-6 border-t border-line pt-8">
          <a href="mailto:bonjour@nexora.bj" className="font-serif text-3xl italic transition-colors hover:text-accent md:text-5xl">
            bonjour@nexora.bj <span aria-hidden>↗</span>
          </a>
        </div>

        <div className="rv-fade mt-14 max-w-4xl md:mt-20">
          <ContactForm />
        </div>

        <div className="rv-fade mt-20 grid gap-10 border-t border-line pt-8 md:grid-cols-3">
          <div>
            <p className="font-mono text-[11px] uppercase tracking-[0.18em] opacity-60">Studio</p>
            <p className="mt-3 font-serif text-2xl italic">Cotonou, Bénin</p>
            <p className="mt-1 font-mono text-[11px] uppercase tracking-[0.18em] opacity-60">
              <LocalTime /> — heure locale
            </p>
          </div>
          <div>
            <p className="font-mono text-[11px] uppercase tracking-[0.18em] opacity-60">Nouveaux projets</p>
            <p className="mt-3 font-serif text-2xl italic">Réponse sous 48 h</p>
            <p className="mt-1 font-mono text-[11px] uppercase tracking-[0.18em] opacity-60">Français · English</p>
          </div>
        </div>
      </Reveal>
    </section>
  )
}

export function Footer() {
  return (
    <footer className="theme-paper relative overflow-hidden border-t border-line px-4 pt-10 md:px-8">
      <div className="grid grid-cols-2 gap-8 font-mono text-[11px] uppercase tracking-[0.16em] md:grid-cols-12">
        <p className="col-span-2 opacity-70 md:col-span-4">
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
          <p className="mt-2 opacity-70">Cotonou, Bénin</p>
        </div>
      </div>
      <div className="mt-10 flex flex-col justify-between gap-2 border-t border-line pt-4 font-mono text-[11px] uppercase tracking-[0.16em] opacity-70 md:flex-row">
        <p>© 2026 NEXORA</p>
        <p>Conçu et animé au Bénin</p>
        <a href="#top" className="link-line self-start">Retour en haut ↑</a>
      </div>
      <p aria-hidden className="ghost-word font-wide mt-6 translate-y-[12%] select-none text-center text-[17vw] font-black leading-[0.8] tracking-[-0.05em] opacity-10" />
    </footer>
  )
}
