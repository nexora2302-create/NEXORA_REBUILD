'use client'

import Image from 'next/image'
import { useEffect, useRef } from 'react'

type Style = 'serif' | 'accent' | 'outline'
type Token = { t: 'w'; v: string; tail: string; style?: Style } | { t: 'img'; src: string; alt: string }

// *mot* = serif italique · ^mot^ = serif orange · =mot= = contour
const RAW =
  'NEXORA est un studio créatif né à ^Cotonou^. Nous dessinons des *identités* qui se lisent [poster] des *images* qui bougent [motion] et des *sites* qui se vivent [interface] pour les marques qui refusent de rester =immobiles=.'

const IMAGES: Record<string, { src: string; alt: string }> = {
  poster: { src: '/work/poster.webp', alt: 'Affiche' },
  motion: { src: '/work/motion.webp', alt: 'Image de motion design' },
  interface: { src: '/work/interface.webp', alt: 'Interface web' },
}

const MARKS: [RegExp, Style][] = [
  [/^\*(.+)\*(\W*)$/, 'serif'],
  [/^\^(.+)\^(\W*)$/, 'accent'],
  [/^=(.+)=(\W*)$/, 'outline'],
]

const TOKENS: Token[] = RAW.split(' ').map((part) => {
  const img = part.match(/^\[(\w+)\]$/)
  if (img) return { t: 'img', ...IMAGES[img[1]] }
  for (const [re, style] of MARKS) {
    const m = part.match(re)
    if (m) return { t: 'w', v: m[1], tail: m[2], style }
  }
  return { t: 'w', v: part, tail: '' }
})

const STYLE_CLASS: Record<Style, string> = {
  serif: 'font-serif font-normal italic tracking-normal',
  accent: 'font-serif font-normal italic tracking-normal text-accent',
  outline: 'outline-text',
}

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
    <section id="studio" ref={ref} aria-labelledby="studio-title" className="relative px-4 py-28 md:px-8 md:py-40">
      <h2 id="studio-title" className="sr-only">Le studio</h2>
      <p className="font-wide text-[8vw] font-extrabold leading-[1] tracking-[-0.03em] md:text-[4.6vw]">
        {TOKENS.map((tok, i) => {
          const style = { '--w': (i / total).toFixed(3) } as React.CSSProperties
          if (tok.t === 'img') {
            return (
              <span key={i} className="mf-word relative mx-[0.1em] inline-block h-[0.8em] w-[1.6em] translate-y-[0.06em] overflow-hidden rounded-full align-baseline" style={style}>
                <Image src={tok.src} alt={tok.alt} fill sizes="12vw" className="object-cover" />
              </span>
            )
          }
          return (
            <span key={i} className={tok.style === 'accent' ? '' : 'mf-word'} style={style}>
              <span className={tok.style ? STYLE_CLASS[tok.style] : ''}>{tok.v}</span>
              {tok.tail}{' '}
            </span>
          )
        })}
      </p>

      <div className="mt-16 grid gap-6 border-t border-line pt-8 md:mt-24 md:grid-cols-12">
        <p className="font-serif text-2xl italic md:col-span-4">Cotonou, pour le monde.</p>
        <p className="max-w-xl text-[17px] leading-relaxed text-foreground/75 md:col-span-6 md:col-start-6">
          Entreprises, marques, institutions et créateurs : nous construisons leur image et leur présence numérique au Bénin, en Afrique et à l’international. Chaque prestation se commande seule ou se combine avec les autres.
        </p>
      </div>
    </section>
  )
}
