'use client'

import { useEffect, useRef, useState } from 'react'
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
  const [onSignal, setOnSignal] = useState(false)
  const [current, setCurrent] = useState<string | null>(null)
  const menuRef = useRef<HTMLDivElement>(null)
  const closeRef = useRef<HTMLButtonElement>(null)
  const openRef = useRef<HTMLButtonElement>(null)

  // État de l'en-tête : fond plein après le haut, orange au-dessus du bloc contact.
  useEffect(() => {
    let raf = 0
    const update = () => {
      raf = 0
      const y = window.scrollY
      setScrolled(y > 24)
      setPastHero(y > window.innerHeight * 0.75)
      const c = document.getElementById('contact')?.getBoundingClientRect()
      setOnSignal(!!c && c.top <= 64 && c.bottom > 64)
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
  }, [])

  // Section active : celle qui traverse le milieu de l'écran.
  useEffect(() => {
    const ids = NAV.map((n) => n.href.slice(1))
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) setCurrent(e.target.id)
        })
      },
      { rootMargin: '-50% 0px -50% 0px' },
    )
    ids.forEach((id) => {
      const el = document.getElementById(id)
      if (el) io.observe(el)
    })
    const top = document.getElementById('top')
    const topIo = new IntersectionObserver(([e]) => e?.isIntersecting && setCurrent(null), { rootMargin: '-50% 0px -50% 0px' })
    if (top) topIo.observe(top)
    return () => {
      io.disconnect()
      topIo.disconnect()
    }
  }, [])

  // Menu mobile : focus dedans, piégé, rendu au bouton à la fermeture.
  useEffect(() => {
    document.body.style.overflow = open ? 'hidden' : ''
    if (!open) return
    closeRef.current?.focus()
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        setOpen(false)
        return
      }
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

  const bar = onSignal ? 'theme-signal' : scrolled ? 'bg-background' : 'bg-transparent'

  return (
    <>
      <header className={`fixed inset-x-0 top-0 z-40 transition-colors duration-500 ${bar}`}>
        <div className="flex h-16 items-center justify-between px-4 md:px-8">
          <a href="#top" className="font-wide inline-flex min-h-11 items-center text-lg font-black tracking-tight" aria-label="NX® NEXORA, retour en haut">
            NX<sup className="text-[0.55em] font-bold">®</sup>
          </a>

          <nav aria-label="Navigation principale" className="hidden md:block">
            <ul className="flex items-center gap-7 text-[15px] font-medium">
              {NAV.map((item) => {
                const active = current === item.href.slice(1)
                return (
                  <li key={item.href}>
                    <a
                      href={item.href}
                      aria-current={active ? 'true' : undefined}
                      className={`relative inline-flex min-h-11 items-center transition-opacity ${active ? 'opacity-100' : 'opacity-75 hover:opacity-100'}`}
                    >
                      {item.label}
                      <span
                        aria-hidden
                        className={`absolute inset-x-0 bottom-2 h-[2px] origin-left rounded-full bg-accent transition-transform duration-500 ease-[var(--ease-out-expo)] ${
                          active ? 'scale-x-100' : 'scale-x-0'
                        }`}
                      />
                    </a>
                  </li>
                )
              })}
            </ul>
          </nav>

          <div className="hidden items-center gap-6 md:flex">
            <p className="hidden items-center gap-2 font-mono text-[13px] opacity-75 lg:flex">
              <svg viewBox="0 0 8 8" className="live-dot size-2 text-accent" aria-hidden>
                <circle cx="4" cy="4" r="4" fill="currentColor" />
              </svg>
              Cotonou <LocalTime />
            </p>
            <a
              href="#contact"
              tabIndex={pastHero ? undefined : -1}
              aria-hidden={!pastHero}
              className={`group inline-flex min-h-11 items-center gap-2 rounded-full px-5 text-[15px] font-semibold transition-[transform,opacity] duration-500 hover:scale-[1.03] ${
                onSignal ? 'bg-foreground text-background' : 'bg-accent text-accent-foreground'
              } ${pastHero ? 'opacity-100' : 'pointer-events-none translate-y-1 opacity-0'}`}
            >
              Démarrer un projet
              <ArrowIcon className="size-3.5" />
            </a>
          </div>

          <div className="flex items-center gap-2 md:hidden">
            <a
              href="#contact"
              tabIndex={pastHero ? undefined : -1}
              aria-hidden={!pastHero}
              className={`inline-flex min-h-11 items-center rounded-full px-4 text-[14px] font-semibold transition-opacity duration-500 ${
                onSignal ? 'bg-foreground text-background' : 'bg-accent text-accent-foreground'
              } ${pastHero ? 'opacity-100' : 'pointer-events-none opacity-0'}`}
            >
              Contact
            </a>
            <button
              ref={openRef}
              type="button"
              className="inline-flex min-h-11 min-w-11 items-center justify-end text-[15px] font-medium"
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
      >
        <div className="flex h-16 items-center justify-between">
          <span className="font-wide text-lg font-black tracking-tight">NX®</span>
          <button ref={closeRef} type="button" onClick={() => setOpen(false)} className="inline-flex min-h-11 min-w-11 items-center justify-end text-[15px] font-medium">
            Fermer
          </button>
        </div>

        <div className="mt-6 grid grid-cols-2 gap-4 border-t border-line pt-6 text-[15px]">
          <p>
            Studio créatif
            <br />
            à Cotonou, Bénin
          </p>
          <p className="text-right font-mono text-[14px]">
            <LocalTime /> heure locale
          </p>
        </div>

        <nav aria-label="Navigation mobile" className="mt-auto">
          <ul className="flex flex-col">
            {NAV.map((item, i) => (
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
