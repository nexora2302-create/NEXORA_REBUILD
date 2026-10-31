'use client'

import { useEffect, useRef, useState } from 'react'
import { ArrowIcon } from './icons'
import { LocalTime } from './local-time'
import { Logo } from './logo'

type Item = { href: string; label: string; id: string }

// `base` vaut '' sur l'accueil et '/' sur les autres pages (liens vers les sections de l'accueil).
export function Header({ base = '' }: { base?: string }) {
  const NAV: Item[] = [
    { href: `${base}#studio`, label: 'Studio', id: 'studio' },
    { href: `${base}#expertises`, label: 'Expertises', id: 'expertises' },
    { href: base ? '/realisations' : '#travaux', label: 'Réalisations', id: 'travaux' },
    { href: `${base}#methode`, label: 'Méthode', id: 'methode' },
  ]
  const contactHref = `${base}#contact`

  const [open, setOpen] = useState(false)
  const [solid, setSolid] = useState(false)
  const [showCta, setShowCta] = useState(!!base)
  const [theme, setTheme] = useState<string | null>(null)
  const [current, setCurrent] = useState<string | null>(base ? 'travaux' : null)
  const menuRef = useRef<HTMLDivElement>(null)
  const closeRef = useRef<HTMLButtonElement>(null)
  const openRef = useRef<HTMLButtonElement>(null)

  // Fond plein une fois le haut quitté (la barre reste toujours visible),
  // et teintée selon la section qui passe sous la barre (data-header="paper" | "signal").
  useEffect(() => {
    let raf = 0
    const update = () => {
      raf = 0
      const y = window.scrollY
      setSolid(y > 24)
      if (!base) setShowCta(y > window.innerHeight * 0.75)
      let t: string | null = null
      document.querySelectorAll<HTMLElement>('[data-header]').forEach((el) => {
        const r = el.getBoundingClientRect()
        if (r.top <= 32 && r.bottom > 32) t = el.dataset.header ?? null
      })
      setTheme(t)
    }
    const onScroll = () => {
      if (!raf) raf = requestAnimationFrame(update)
    }
    update()
    window.addEventListener('scroll', onScroll, { passive: true })
    window.addEventListener('resize', onScroll)
    return () => {
      window.removeEventListener('scroll', onScroll)
      window.removeEventListener('resize', onScroll)
      cancelAnimationFrame(raf)
    }
  }, [base])

  // Section active (accueil uniquement).
  useEffect(() => {
    if (base) return
    const io = new IntersectionObserver(
      (entries) => entries.forEach((e) => e.isIntersecting && setCurrent(e.target.id)),
      { rootMargin: '-50% 0px -50% 0px' },
    )
    ;['top', 'studio', 'expertises', 'travaux', 'methode', 'faq', 'contact'].forEach((id) => {
      const el = document.getElementById(id)
      if (el) io.observe(el)
    })
    return () => io.disconnect()
  }, [base])

  // Menu mobile : focus dedans, piégé, rendu au bouton à la fermeture.
  useEffect(() => {
    document.body.style.overflow = open ? 'hidden' : ''
    if (!open) return
    closeRef.current?.focus()
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') return setOpen(false)
      if (e.key !== 'Tab' || !menuRef.current) return
      const items = menuRef.current.querySelectorAll<HTMLElement>('a, button')
      const first = items[0]
      const last = items[items.length - 1]
      if (e.shiftKey && document.activeElement === first) {
        e.preventDefault()
        last.focus()
      } else if (!e.shiftKey && document.activeElement === last) {
        e.preventDefault()
        first.focus()
      }
    }
    window.addEventListener('keydown', onKey)
    return () => {
      window.removeEventListener('keydown', onKey)
      openRef.current?.focus()
    }
  }, [open])

  const themeClass = theme === 'signal' ? 'theme-signal' : theme === 'paper' ? 'theme-paper' : solid ? 'bg-background' : 'bg-transparent'
  const ctaClass = theme === 'signal' ? 'bg-foreground text-background' : 'bg-accent text-accent-foreground'

  return (
    <>
      <header
        className={`fixed inset-x-0 top-0 z-40 transition-[background-color,color] duration-500 ease-[var(--ease-out-expo)] ${themeClass}`}
      >
        <div className={`grid grid-cols-12 items-center gap-4 px-4 md:px-8 transition-[height] duration-500 ease-[var(--ease-out-expo)] ${solid ? 'h-14' : 'h-16 md:h-20'}`}>
          <a href={base || '#top'} className="col-span-6 inline-flex min-h-11 items-center md:col-span-3" aria-label="NEXORA, accueil">
            <Logo className="text-[0.95rem]" />
          </a>

          <nav aria-label="Navigation principale" className="hidden md:col-span-6 md:block">
            <ul className="grid grid-cols-4 text-[15px] font-medium">
              {NAV.map((item) => {
                const active = current === item.id
                return (
                  <li key={item.href}>
                    <a href={item.href} aria-current={active ? 'true' : undefined} className="group/nav inline-flex min-h-11 items-center gap-2">
                      <span
                        aria-hidden
                        className={`size-1.5 rounded-full bg-accent transition-transform duration-500 ease-[var(--ease-out-expo)] ${active ? 'scale-100' : 'scale-0'}`}
                      />
                      <span className="relative block overflow-hidden">
                        <span className="block transition-transform duration-500 ease-[var(--ease-out-expo)] group-hover/nav:-translate-y-full">{item.label}</span>
                        <span aria-hidden className="absolute inset-0 block translate-y-full transition-transform duration-500 ease-[var(--ease-out-expo)] group-hover/nav:translate-y-0">
                          {item.label}
                        </span>
                      </span>
                    </a>
                  </li>
                )
              })}
            </ul>
          </nav>

          <div className="col-span-6 flex items-center justify-end gap-2 md:col-span-3">
            <a
              href={contactHref}
              tabIndex={showCta ? undefined : -1}
              aria-hidden={!showCta}
              className={`group inline-flex min-h-11 items-center gap-2 rounded-full px-4 text-[14px] font-semibold transition-[transform,opacity] duration-500 hover:scale-[1.03] md:px-5 md:text-[15px] ${ctaClass} ${
                showCta ? 'opacity-100' : 'pointer-events-none translate-y-1 opacity-0'
              }`}
            >
              <span className="md:hidden">Contact</span>
              <span className="hidden md:inline">Démarrer un projet</span>
              <ArrowIcon className="hidden size-3.5 md:block" />
            </a>
            <button
              ref={openRef}
              type="button"
              className="inline-flex min-h-11 min-w-11 items-center justify-end text-[15px] font-medium md:hidden"
              aria-expanded={open}
              aria-controls="mobile-menu"
              onClick={() => setOpen(true)}
            >
              Menu
            </button>
          </div>
        </div>
      </header>

      <div
        ref={menuRef}
        id="mobile-menu"
        role="dialog"
        aria-modal="true"
        aria-label="Menu"
        hidden={!open}
        className="theme-signal fixed inset-0 z-[60] flex flex-col px-4 pb-8 md:hidden"
        style={{ '--logo-x': '#0d0c0b' } as React.CSSProperties}
      >
        <div className="flex h-16 items-center justify-between">
          <Logo className="text-[0.95rem]" />
          <button ref={closeRef} type="button" onClick={() => setOpen(false)} className="inline-flex min-h-11 min-w-11 items-center justify-end text-[15px] font-medium">
            Fermer
          </button>
        </div>

        <div className="mt-6 grid grid-cols-2 gap-4 border-t border-line pt-6 text-[15px]">
          <p>
            Studio créatif
            <br />à Cotonou, Bénin
          </p>
          <p className="text-right font-mono text-[14px]">
            <LocalTime /> heure locale
          </p>
        </div>

        <nav aria-label="Navigation mobile" className="mt-auto">
          <ul className="flex flex-col">
            {[...NAV, { href: contactHref, label: 'Contact', id: 'contact' }].map((item, i) => (
              <li key={item.href} className="overflow-hidden border-b border-line">
                <a
                  href={item.href}
                  onClick={() => setOpen(false)}
                  className="block py-3"
                  style={open ? { animation: `word-swap 0.7s cubic-bezier(0.16,1,0.3,1) ${i * 60}ms both` } : undefined}
                >
                  <span className="font-wide text-[10.5vw] font-black leading-[0.95] tracking-[-0.03em]">{item.label}</span>
                </a>
              </li>
            ))}
          </ul>
        </nav>
        <a href="mailto:bonjour@nexora.bj" className="mt-8 inline-flex min-h-11 items-center font-serif text-2xl italic">
          bonjour@nexora.bj
        </a>
      </div>
    </>
  )
}
