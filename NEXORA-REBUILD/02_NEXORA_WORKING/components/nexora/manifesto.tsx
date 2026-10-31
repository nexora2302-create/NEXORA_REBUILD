'use client'

import Image from 'next/image'
import { useEffect, useRef } from 'react'

type Token = { t: 'w'; v: string; serif?: boolean } | { t: 'img'; src: string; alt: string }

const RAW =
  'NEXORA est un studio créatif né à Cotonou. Nous dessinons des *identités* qui se lisent [poster] des *images* qui bougent [motion] et des *sites* qui se vivent [interface] — pour les marques qui refusent de rester immobiles.'

const IMAGES: Record<string, { src: string; alt: string }> = {
  poster: { src: '/work/poster.webp', alt: 'Affiche' },
  motion: { src: '/work/motion.webp', alt: 'Image de motion design' },
  interface: { src: '/work/interface.webp', alt: 'Interface web' },
}

const TOKENS: Token[] = RAW.split(' ').map((part) => {
  const img = part.match(/^\[(\w+)\]$/)
  if (img) return { t: 'img', ...IMAGES[img[1]] }
  const serif = part.match(/^\*(.+)\*$/)
  return serif ? { t: 'w', v: serif[1], serif: true } : { t: 'w', v: part }
})

export function Manifesto() {
  const ref = useRef<HTMLElement>(null)

  useEffect(() => {
    const el = ref.current
    if (!el) return
    let raf = 0
    const update = () => {
      const r = el.getBoundingClientRect()
      const vh = window.innerHeight
      const p = (vh * 0.85 - r.top) / (r.height * 0.75)
      el.style.setProperty('--p', Math.min(1.05, Math.max(0, p)).toFixed(3))
    }
    const onScroll = () => {
      cancelAnimationFrame(raf)
      raf = requestAnimationFrame(update)
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

  const total = TOKENS.length

  return (
    <section id="studio" ref={ref} aria-labelledby="studio-title" className="manifesto relative px-4 py-28 md:px-8 md:py-44">
      <div className="grid grid-cols-1 gap-10 md:grid-cols-12">
        <div className="flex items-start justify-between font-mono text-[11px] uppercase tracking-[0.16em] opacity-70 md:col-span-2 md:flex-col md:gap-4">
          <h2 id="studio-title">(Le studio)</h2>
          <span>001 / Manifeste</span>
        </div>

        <p className="text-[9.5vw] font-semibold leading-[0.98] tracking-[-0.02em] [font-variation-settings:'wdth'_88] md:col-span-10 md:text-[5.6vw]">
          {TOKENS.map((tok, i) => {
            const style = { '--w': (i / total).toFixed(3) } as React.CSSProperties
            if (tok.t === 'img') {
              return (
                <span key={i} className="mf-word relative mx-[0.1em] inline-block h-[0.78em] w-[1.7em] translate-y-[0.08em] overflow-hidden rounded-full align-baseline" style={style}>
                  <Image src={tok.src} alt={tok.alt} fill sizes="12vw" className="object-cover" />
                </span>
              )
            }
            return (
              <span key={i} className={`mf-word ${tok.serif ? 'font-serif font-normal italic' : ''}`} style={style}>
                {tok.v}{' '}
              </span>
            )
          })}
        </p>
      </div>

      <div className="mt-20 grid grid-cols-2 gap-8 border-t border-current/20 pt-8 md:mt-32 md:grid-cols-12">
        {[
          ['03', 'expertises intégrées, un seul regard'],
          ['01', 'studio, ancré au Bénin'],
          ['FR·EN', 'langues de travail'],
        ].map(([n, label]) => (
          <div key={label} className="md:col-span-4">
            <p className="font-serif text-6xl italic leading-none md:text-7xl">{n}</p>
            <p className="mt-3 max-w-[16ch] text-sm opacity-80">{label}</p>
          </div>
        ))}
      </div>
    </section>
  )
}
