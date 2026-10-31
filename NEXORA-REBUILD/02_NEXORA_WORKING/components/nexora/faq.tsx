import { PlusIcon } from './icons'
import { Reveal, SplitWords } from './reveal'

export const FAQ_ITEMS = [
  { q: 'Peut-on commander un seul service ?', a: 'Oui. Identité, motion design et site web peuvent être confiés séparément ou combinés selon vos besoins.' },
  { q: 'Travaillez-vous en dehors du Bénin ?', a: 'Oui. Le studio est basé à Cotonou et travaille avec des clients au Bénin, en Afrique et à l’international, en français comme en anglais.' },
  { q: 'Comment démarre un projet ?', a: 'Par un message via le formulaire ci-dessous ou par e-mail. Nous revenons vers vous pour un premier échange et cadrer le besoin.' },
  { q: 'Combien coûte un projet ?', a: 'Chaque projet est chiffré sur mesure après ce premier échange, en fonction du périmètre, des formats et des délais.' },
  { q: 'Assurez-vous la maintenance des sites ?', a: 'Oui. Développement, évolution et maintenance de solutions web font partie de nos prestations.' },
]

export function Faq() {
  return (
    <section id="faq" aria-labelledby="faq-title" className="relative border-t border-line px-4 py-28 md:px-8 md:py-36">
      <div className="grid grid-cols-1 gap-10 md:grid-cols-12">
        <Reveal className="md:col-span-4">
          <h2 id="faq-title" className="font-wide text-[11vw] font-black leading-[0.92] tracking-[-0.04em] md:text-[clamp(2.6rem,3.6vw,4rem)]">
            <SplitWords text="Questions" />
            <br />
            <span className="font-serif font-normal italic tracking-normal">
              <SplitWords text="fréquentes" offset={1} />
            </span>
          </h2>
        </Reveal>
        <div className="md:col-span-7 md:col-start-6">
          {FAQ_ITEMS.map((f) => (
            <details key={f.q} className="group border-t border-line last:border-b">
              <summary className="flex min-h-16 cursor-pointer list-none items-center justify-between gap-6 py-5 text-xl font-semibold tracking-tight transition-colors hover:text-accent md:text-2xl [&::-webkit-details-marker]:hidden">
                {f.q}
                <span className="grid size-10 shrink-0 place-items-center rounded-full border border-line transition-[transform,background-color,color] duration-500 ease-[var(--ease-out-expo)] group-open:rotate-45 group-open:bg-accent group-open:text-accent-foreground">
                  <PlusIcon className="size-4" />
                </span>
              </summary>
              <p className="max-w-2xl pb-7 text-[17px] leading-relaxed text-foreground/75">{f.a}</p>
            </details>
          ))}
        </div>
      </div>
    </section>
  )
}
