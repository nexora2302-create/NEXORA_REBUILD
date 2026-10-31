'use client'

import { useEffect, useRef, useState } from 'react'

const WORDS = ['Identité visuelle', 'Motion design', 'Sites web', 'Cotonou', 'Bénin']

export function Marquee() {
  const ref = useRef<HTMLElement>(null)
  const [playing, setPlaying] = useState(false)

  // Le bandeau ne tourne que lorsqu'il est visible.
  useEffect(() => {
    const el = ref.current
    if (!el) return
    const io = new IntersectionObserver(([e]) => setPlaying(!!e?.isIntersecting))
    io.observe(el)
    return () => io.disconnect()
  }, [])

  return (
    <section ref={ref} aria-label="Nos disciplines" className="overflow-hidden border-y border-line py-4">
      <div className="marquee-track flex w-max whitespace-nowrap" style={{ animationPlayState: playing ? 'running' : 'paused' }}>
        {[0, 1].map((dup) => (
          <div key={dup} className="flex shrink-0 items-center" aria-hidden={dup === 1}>
            {[...WORDS, ...WORDS].map((w, i) => (
              <span key={`${dup}-${i}`} className="flex items-center">
                <span className="font-wide px-5 text-2xl font-black uppercase tracking-[-0.02em] md:text-4xl">{w}</span>
                <svg viewBox="0 0 40 40" className="h-4 w-4 shrink-0 text-accent md:h-6 md:w-6" aria-hidden>
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
