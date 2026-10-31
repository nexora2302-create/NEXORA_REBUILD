'use client'

import { useEffect, useState } from 'react'
import { LocalTime } from './local-time'

const NAV = [
  { href: '#studio', label: 'Studio', n: '01' },
  { href: '#expertises', label: 'Expertises', n: '02' },
  { href: '#travaux', label: 'Travaux', n: '03' },
  { href: '#methode', label: 'Méthode', n: '04' },
  { href: '#contact', label: 'Contact', n: '05' },
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
      <header className="fixed inset-x-0 top-0 z-40 bg-background/70 backdrop-blur">
        <div className="flex items-center justify-between px-4 py-3.5 md:px-8">
          <a href="#top" className="font-wide text-lg font-black tracking-tight" aria-label="NX® — NEXORA, retour en haut">
            NX<sup className="text-[0.55em] font-bold">®</sup>
          </a>

          <nav aria-label="Navigation principale" className="hidden md:block">
            <ul className="flex items-center gap-8">
              {NAV.map((item) => (
                <li key={item.href}>
                  <a href={item.href} className="link-line font-mono text-[11px] uppercase tracking-[0.18em]">
                    {item.label}
                  </a>
                </li>
              ))}
            </ul>
          </nav>

          <div className="hidden items-center gap-6 md:flex">
            <p className="hidden items-center gap-2 font-mono text-[11px] uppercase tracking-[0.18em] lg:flex">
              <span aria-hidden className="blink text-accent">●</span>
              REC · <LocalTime /> WAT
            </p>
            <a
              href="#contact"
              className="rounded-full border border-foreground/50 px-4 py-2 font-mono text-[11px] uppercase tracking-[0.18em] transition-colors hover:bg-foreground hover:text-background"
            >
              Démarrer un projet
            </a>
          </div>

          <button
            type="button"
            className="font-mono text-[11px] uppercase tracking-[0.2em] md:hidden"
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
          <span className="font-wide text-lg font-black tracking-tight">NX®</span>
          <button type="button" onClick={() => setOpen(false)} className="font-mono text-[11px] uppercase tracking-[0.2em]">
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
                  style={open ? { animation: `word-swap 0.9s cubic-bezier(0.16,1,0.3,1) ${i * 70}ms both` } : undefined}
                >
                  <span className="font-wide text-[11vw] font-black leading-[0.9] tracking-tight">{item.label}</span>
                  <span className="font-serif text-xl italic">{item.n}</span>
                </a>
              </li>
            ))}
          </ul>
        </nav>
        <p className="mt-8 font-mono text-[11px] uppercase tracking-[0.16em]">Cotonou, Bénin — bonjour@nexora.bj</p>
      </div>
    </>
  )
}
