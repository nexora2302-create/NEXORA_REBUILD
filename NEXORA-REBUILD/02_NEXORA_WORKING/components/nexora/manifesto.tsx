'use client'

import Image from 'next/image'
import { useEffect, useRef } from 'react'
import { fr } from './fr'
import { Reveal, SplitWords } from './reveal'

type Token = { t: 'w'; v: string } | { t: 'img'; src: string; alt: string }

// [clé] = une image qui s'ouvre dans la phrase au fil de la lecture
const RAW =
  'Nous dessinons des identités [poster] qui se lisent, des images [motion] qui bougent et des sites [interface] qui se vivent, pour les marques qui refusent de rester immobiles.'

const IMAGES: Record<string, { src: string; alt: string }> = {
  poster: { src: '/work/poster.webp', alt: 'Affiche d’identité visuelle' },
  motion: { src: '/work/motion.webp', alt: 'Image de motion design' },
  interface: { src: '/work/interface.webp', alt: 'Interface de site web' },
}

const TOKENS: Token[] = RAW.split(' ').map((part) => {
  const img = part.match(/^\[(\w+)\]$/)
  return img ? { t: 'img', ...IMAGES[img[1]] } : { t: 'w', v: part }
})

const PRINCIPLES = [
  { title: 'Une idée d’abord.', text: 'Chaque projet part d’une idée tirée de votre marque, jamais d’une tendance du moment.' },
  { title: 'Trois métiers, une équipe.', text: 'Identité, motion et web conçus ensemble : votre image reste cohérente sur chaque support.' },
  { title: 'D’ici, pour partout.', text: 'Entreprises, institutions et créateurs, au Bénin, en Afrique et à l’international, en français comme en anglais.' },
]

export function Manifesto() {
  const ref = useRef<HTMLParagraphElement>(null)

  // Progression de lecture de la phrase (0 → 1) pendant qu'elle traverse l'écran.
  useEffect(() => {
    const el = ref.current
    if (!el) return
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      el.style.setProperty('--p', '1.2')
      return
    }
    let raf = 0
    const update = () => {
      raf = 0
      const r = el.getBoundingClientRect()
      const vh = window.innerHeight
      const p = (vh * 0.92 - r.top) / (vh * 0.92 - vh * 0.3 + r.height * 0.6)
      el.style.setProperty('--p', Math.min(1.2, Math.max(0, p)).toFixed(3))
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

  const total = TOKENS.length

  return (
    <section id="studio" data-header="paper" aria-labelledby="studio-title" className="theme-paper relative px-4 py-28 md:px-8 md:py-40">
      <Reveal className="grid gap-8 md:grid-cols-12 md:items-end">
        <h2 id="studio-title" className="t-section md:col-span-12">
          <SplitWords text="Né à Cotonou," />
          <br className="hidden md:block" />
          <SplitWords text="pensé pour le monde." offset={3} />
        </h2>
        <p className="max-w-sm text-[17px] leading-relaxed md:col-span-4 md:col-start-9">
          Studio créatif basé à Cotonou, au Bénin : identité, motion design et web.
        </p>
      </Reveal>

      <p
        ref={ref}
        className="font-wide mt-20 text-[clamp(1.85rem,4vw,4.1rem)] font-extrabold leading-[1.08] tracking-[-0.03em] md:mt-32"
        style={{ '--p': 0 } as React.CSSProperties}
      >
        {TOKENS.map((tok, i) => {
          const style = { '--w': (i / total).toFixed(3) } as React.CSSProperties
          if (tok.t === 'img') {
            return (
              <span key={i} className="mf-open relative inline-block h-[0.82em] translate-y-[0.08em] overflow-hidden rounded-full align-baseline" style={style}>
                <Image src={tok.src} alt={tok.alt} fill sizes="12vw" className="object-cover" />
              </span>
            )
          }
          return (
            <span key={i} className="mf-word" style={style}>
              {tok.v}{' '}
            </span>
          )
        })}
      </p>

      <Reveal as="ul" className="mt-20 grid gap-12 md:mt-28 lg:grid-cols-3 lg:gap-8">
        {PRINCIPLES.map((p, i) => (
          <li key={p.title} className="rv-up" style={{ '--i': i } as React.CSSProperties}>
            <h3 className="font-wide text-[1.75rem] font-extrabold leading-[1.02] tracking-[-0.025em] md:text-[2rem]">{fr(p.title)}</h3>
            <p className="mt-4 max-w-sm text-[17px] leading-relaxed">{fr(p.text)}</p>
          </li>
        ))}
      </Reveal>
    </section>
  )
}
