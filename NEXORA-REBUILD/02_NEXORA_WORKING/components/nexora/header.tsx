'use client'

import { useEffect, useState } from 'react'
import { ArrowIcon } from './icons'
import { LocalTime } from './local-time'

const NAV = [
  { href: '#studio', label: 'Studio' },
  { href: '#expertises', label: 'Expertises' },
  { href: '#travaux', label: 'Réalisations' },
  { href: '#methode', label: 'Méthode' },
  { href: '#contact', label: 'Contact' },
]

export function Header() {
  const [open, setOpen] = useState(false)
  const [scrolled, setScrolled] = useState(false)
  const [pastHero, setPastHero] = useState(false)

  useEffect(() => {
    const on = () => {
      setScrolled(window.scrollY > 24)
      setPastHero(window.scrollY > window.innerHeight * 0.75)
    }
    on()
    window.addEventListener('scroll', on, { passive: true })
    return () => window.removeEventListener('scroll', on)
  }, [])

  useEffect(() => {
    document.body.style.overflow = open ? 'hidden' : ''
    if (!open) return
    const onKey = (e: KeyboardEvent) => e.key === 'Escape' && setOpen(false)
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  }, [open])

  return (
    <>
      <header
        className={`fixed inset-x-0 top-0 z-40 transition-[background-color,backdrop-filter] duration-500 ${
          scrolled ? 'bg-background/75 backdrop-blur-md' : 'bg-transparent'
        }`}
      >
        <div className="flex h-16 items-center justify-between px-4 md:px-8">
          <a href="#top" className="font-wide inline-flex min-h-11 items-center text-lg font-black tracking-tight" aria-label="NX® NEXORA, retour en haut">
            NX<sup className="text-[0.55em] font-bold">®</sup>
          </a>

          <nav aria-label="Navigation principale" className="hidden md:block">
            <ul className="flex items-center gap-7 text-[14px]">
              {NAV.map((item) => (
                <li key={item.href}>
                  <a href={item.href} className="link-line py-2 text-foreground/85 transition-colors hover:text-foreground">
                    {item.label}
                  </a>
                </li>
              ))}
            </ul>
          </nav>

          <div className="hidden items-center gap-6 md:flex">
            <p className="hidden items-center gap-2 font-mono text-xs text-foreground/70 lg:flex">
              <svg viewBox="0 0 8 8" className="live-dot size-2 text-accent" aria-hidden>
                <circle cx="4" cy="4" r="4" fill="currentColor" />
              </svg>
              Cotonou <LocalTime />
            </p>
            <a
              href="#contact"
              tabIndex={pastHero ? undefined : -1}
              aria-hidden={!pastHero}
              className={`group inline-flex min-h-11 items-center gap-2 rounded-full bg-accent px-5 text-[14px] font-semibold text-accent-foreground transition-[transform,opacity] duration-500 hover:scale-[1.03] ${
                pastHero ? 'opacity-100' : 'pointer-events-none translate-y-1 opacity-0'
              }`}
            >
              Démarrer un projet
              <ArrowIcon className="size-3.5" />
            </a>
          </div>

          <button
            type="button"
            className="inline-flex min-h-11 min-w-11 items-center justify-end text-[15px] font-medium md:hidden"
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
        className="theme-signal fixed inset-0 z-[60] flex flex-col px-4 pb-8 md:hidden"
      >
        <div className="flex h-16 items-center justify-between">
          <span className="font-wide text-lg font-black tracking-tight">NX®</span>
          <button type="button" onClick={() => setOpen(false)} className="inline-flex min-h-11 min-w-11 items-center justify-end text-[15px] font-medium">
            Fermer
          </button>
        </div>
        <nav aria-label="Navigation mobile" className="mt-auto">
          <ul className="flex flex-col">
            {NAV.map((item, i) => (
              <li key={item.href} className="overflow-hidden border-b border-line">
                <a
                  href={item.href}
                  onClick={() => setOpen(false)}
                  className="block py-3"
                  style={open ? { animation: `word-swap 0.9s cubic-bezier(0.16,1,0.3,1) ${i * 60}ms both` } : undefined}
                >
                  <span className="font-wide text-[10.5vw] font-black leading-[0.95] tracking-[-0.03em]">{item.label}</span>
                </a>
              </li>
            ))}
          </ul>
        </nav>
        <a href="mailto:bonjour@nexora.bj" className="mt-8 font-serif text-2xl italic">
          bonjour@nexora.bj
        </a>
      </div>
    </>
  )
}
