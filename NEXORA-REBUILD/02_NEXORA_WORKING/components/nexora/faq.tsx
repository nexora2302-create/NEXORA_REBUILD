import { Reveal, SplitWords } from './reveal'

export const FAQ_ITEMS = [
  { q: 'Peut-on commander un seul service ?', a: 'Oui. Identité, motion design et site web peuvent être confiés séparément ou combinés selon vos besoins.' },
  { q: 'Travaillez-vous en dehors du Bénin ?', a: 'Oui. Le studio est basé à Cotonou et travaille avec des clients au Bénin, en Afrique et à l’international, en français comme en anglais.' },
  { q: 'Comment démarre un projet ?', a: 'Par un message via le formulaire ci-dessous ou par e-mail. Nous revenons vers vous sous 48 h pour cadrer le besoin.' },
  { q: 'Combien coûte un projet ?', a: 'Chaque projet est chiffré sur mesure après un premier échange, en fonction du périmètre, des formats et des délais.' },
  { q: 'Assurez-vous la maintenance des sites ?', a: 'Oui. Développement, évolution et maintenance de solutions web font partie de nos prestations.' },
]

export function Faq() {
  return (
    <section id="faq" aria-labelledby="faq-title" className="relative px-4 py-28 md:px-8 md:py-40">
      <Reveal className="grid grid-cols-1 gap-10 md:grid-cols-12">
        <div className="md:col-span-4">
          <p className="mb-6 font-mono text-[11px] uppercase tracking-[0.16em] text-muted-foreground">(05) — FAQ</p>
          <h2 id="faq-title" className="font-wide text-[11vw] font-black leading-[0.9] tracking-[-0.04em] md:text-[3.4vw]">
            <SplitWords text="Questions" />
            <br />
            <span className="font-serif font-normal normal-case italic tracking-normal text-accent [font-variation-settings:normal]">
              <SplitWords text="fréquentes" offset={1} />
            </span>
          </h2>
        </div>
        <div className="rv-fade md:col-span-8">
          {FAQ_ITEMS.map((f) => (
            <details key={f.q} className="group border-t border-line last:border-b">
              <summary className="flex cursor-pointer list-none items-center justify-between gap-6 py-6 text-xl font-semibold tracking-tight md:text-2xl [&::-webkit-details-marker]:hidden">
                {f.q}
                <span aria-hidden className="font-mono text-2xl text-accent transition-transform duration-500 group-open:rotate-45">+</span>
              </summary>
              <p className="max-w-2xl pb-6 text-sm leading-relaxed text-muted-foreground md:text-base">{f.a}</p>
            </details>
          ))}
        </div>
      </Reveal>
    </section>
  )
}
