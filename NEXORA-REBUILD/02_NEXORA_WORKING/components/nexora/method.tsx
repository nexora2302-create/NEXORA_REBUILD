import { Reveal, SplitWords } from './reveal'

const STEPS = [
  { n: '01', title: 'Écouter', text: 'Un premier échange pour comprendre votre marque, votre public et ce que le projet doit accomplir.' },
  { n: '02', title: 'Concevoir', text: 'Une direction créative claire, présentée et ajustée avec vous avant toute production.' },
  { n: '03', title: 'Créer', text: 'Identité, mouvement, interface : nous produisons et itérons, avec des points d’étape réguliers.' },
  { n: '04', title: 'Livrer', text: 'Des fichiers prêts à l’emploi, un site en ligne et un accompagnement pour la suite.' },
]

export function Method() {
  return (
    <section id="methode" aria-labelledby="methode-title" className="relative px-4 py-28 md:px-8 md:py-40">
      <Reveal className="mb-16 grid grid-cols-1 gap-6 md:mb-24 md:grid-cols-12">
        <p className="font-mono text-[11px] uppercase tracking-[0.16em] text-muted-foreground md:col-span-2">(Méthode)</p>
        <h2 id="methode-title" className="text-[13vw] font-extrabold uppercase leading-[0.85] tracking-[-0.03em] [font-variation-settings:'wdth'_72] md:col-span-10 md:text-[8vw]">
          <SplitWords text="Du brief" />
          <br />
          <span className="font-serif font-normal normal-case italic tracking-normal text-accent [font-variation-settings:normal]">
            <SplitWords text="à l’image." offset={2} />
          </span>
        </h2>
      </Reveal>

      <ol className="grid grid-cols-1 border-t border-line md:grid-cols-4">
        {STEPS.map((s) => (
          <Reveal as="li" key={s.n} className="border-b border-line py-8 md:border-b-0 md:border-r md:px-6 md:first:pl-0 md:last:border-r-0">
            <div className="rv-fade">
              <span className="font-serif text-3xl italic text-accent">{s.n}</span>
              <h3 className="mt-6 text-3xl font-extrabold uppercase tracking-[-0.02em] [font-variation-settings:'wdth'_80]">{s.title}</h3>
              <p className="mt-3 max-w-xs text-sm leading-relaxed text-muted-foreground">{s.text}</p>
            </div>
          </Reveal>
        ))}
      </ol>
    </section>
  )
}
