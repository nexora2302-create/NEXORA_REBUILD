'use client'

import { useEffect, useState } from 'react'

const NAV = [
  { href: '#expertises', label: 'Expertises', n: '01' },
  { href: '#travaux', label: 'Travaux', n: '02' },
  { href: '#studio', label: 'Studio', n: '03' },
  { href: '#contact', label: 'Contact', n: '04' },
]

export function Header() {
  const [open, setOpen] = useState(false)

  useEffect(() => {
    document.body.style.overflow = open ? 'hidden' : ''
    if (!open) return
    const onKey = (e: KeyboardEvent) => e.key === 'Escape' && setOpen(false)
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [open])

  return (
    <>
      <header className="fixed inset-x-0 top-0 z-40 text-white mix-blend-difference">
        <div className="flex items-center justify-between px-4 py-4 md:px-8 md:py-6">
          <a href="#top" className="flex items-baseline gap-2" aria-label="NEXORA, retour en haut">
            <span className="text-lg font-extrabold tracking-tight [font-variation-settings:'wdth'_112]">
              NEXORA
            </span>
            <span className="hidden font-serif text-sm italic opacity-70 sm:inline">
              studio en mouvement
            </span>
          </a>

          <nav aria-label="Navigation principale" className="hidden md:block">
            <ul className="flex items-center gap-8 text-sm">
              {NAV.map((item) => (
                <li key={item.href}>
                  <a href={item.href} className="group flex items-baseline gap-1.5">
                    <span className="text-[10px] opacity-50">{item.n}</span>
                    <span className="link-line">{item.label}</span>
                  </a>
                </li>
              ))}
            </ul>
          </nav>

          <a
            href="#contact"
            className="hidden rounded-full border border-white/60 px-4 py-2 text-sm transition-colors hover:bg-white hover:text-black md:inline-block"
          >
            Démarrer un projet
          </a>

          <button
            type="button"
            className="text-sm uppercase tracking-[0.2em] md:hidden"
            aria-expanded={open}
            aria-controls="mobile-menu"
            onClick={() => setOpen(true)}
          >
            Menu
          </button>
        </div>
      </header>

      <div
        id="mobile-menu"
        role="dialog"
        aria-modal="true"
        aria-label="Menu"
        hidden={!open}
        className="fixed inset-0 z-[60] flex flex-col bg-accent px-4 py-4 text-accent-foreground md:hidden"
      >
        <div className="flex items-center justify-between">
          <span className="text-lg font-extrabold tracking-tight">NEXORA</span>
          <button
            type="button"
            onClick={() => setOpen(false)}
            className="text-sm uppercase tracking-[0.2em]"
          >
            Fermer
          </button>
        </div>
        <nav aria-label="Navigation mobile" className="mt-auto">
          <ul className="flex flex-col">
            {NAV.map((item, i) => (
              <li key={item.href} className="overflow-hidden border-b border-current/20">
                <a
                  href={item.href}
                  onClick={() => setOpen(false)}
                  className="flex items-baseline justify-between py-3"
                  style={
                    open
                      ? {
                          animation: `word-swap 0.9s cubic-bezier(0.16,1,0.3,1) ${i * 70}ms both`,
                        }
                      : undefined
                  }
                >
                  <span className="text-[15vw] font-extrabold uppercase leading-[0.85] tracking-tight [font-variation-settings:'wdth'_75]">
                    {item.label}
                  </span>
                  <span className="font-serif text-xl italic">{item.n}</span>
                </a>
              </li>
            ))}
          </ul>
        </nav>
        <p className="mt-8 font-serif text-xl italic">Cotonou, Bénin — bonjour@nexora.bj</p>
      </div>
    </>
  )
}
