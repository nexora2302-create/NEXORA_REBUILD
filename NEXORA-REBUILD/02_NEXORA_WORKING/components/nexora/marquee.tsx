const WORDS = ['Identité visuelle', 'Motion design', 'Sites web', 'Cotonou', 'Bénin']

export function Marquee() {
  return (
    <section aria-label="Nos disciplines" className="overflow-hidden border-y border-line py-5">
      <div className="marquee-track flex w-max whitespace-nowrap">
        {[0, 1].map((dup) => (
          <div key={dup} className="flex shrink-0 items-center" aria-hidden={dup === 1}>
            {[...WORDS, ...WORDS].map((w, i) => (
              <span key={`${dup}-${i}`} className="flex items-center">
                <span className="font-wide px-6 text-5xl font-black uppercase tracking-[-0.02em] md:text-7xl">{w}</span>
                <svg viewBox="0 0 40 40" className="h-8 w-8 shrink-0 text-accent md:h-12 md:w-12" aria-hidden>
                  <path d="M20 0 L24 16 L40 20 L24 24 L20 40 L16 24 L0 20 L16 16 Z" fill="currentColor" />
                </svg>
              </span>
            ))}
          </div>
        ))}
      </div>
    </section>
  )
}
