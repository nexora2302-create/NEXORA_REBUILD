const WORDS = ['Communication visuelle', 'Motion design', 'Sites web', 'Cotonou', 'Bénin']

function Row({ outline, reverse }: { outline?: boolean; reverse?: boolean }) {
  const items = [...WORDS, ...WORDS]
  return (
    <div className="flex overflow-hidden">
      <div className={`marquee-track flex shrink-0 items-center whitespace-nowrap ${reverse ? 'reverse' : ''}`}>
        {[0, 1].map((dup) => (
          <div key={dup} className="flex shrink-0 items-center" aria-hidden={dup === 1}>
            {items.map((w, i) => (
              <span key={`${dup}-${i}`} className="flex items-center">
                <span
                  className={`px-6 text-[14vw] font-extrabold uppercase leading-[0.95] tracking-[-0.03em] [font-variation-settings:'wdth'_70] md:text-[8vw] ${
                    outline ? 'outline-text-fg' : ''
                  }`}
                >
                  {w}
                </span>
                <svg viewBox="0 0 40 40" className="h-[5vw] w-[5vw] shrink-0 text-accent md:h-[3vw] md:w-[3vw]" aria-hidden>
                  <path d="M20 0 L24 16 L40 20 L24 24 L20 40 L16 24 L0 20 L16 16 Z" fill="currentColor" />
                </svg>
              </span>
            ))}
          </div>
        ))}
      </div>
    </div>
  )
}

export function Marquee() {
  return (
    <section aria-label="Nos disciplines" className="marquee-band overflow-hidden border-y border-line py-6 md:py-10">
      <Row />
      <Row outline reverse />
    </section>
  )
}
