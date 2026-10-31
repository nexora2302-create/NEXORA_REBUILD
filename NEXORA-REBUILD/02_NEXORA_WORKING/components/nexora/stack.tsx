'use client'

import { useEffect, useRef, type ReactNode } from 'react'

/*
 * Pile de cartes : chaque carte reste collée en haut ; quand la suivante la recouvre,
 * elle recule (échelle + assombrissement). Scroll natif, un seul écouteur, desktop uniquement.
 */
export function Stack({ children, className }: { children: ReactNode; className?: string }) {
  const ref = useRef<HTMLOListElement>(null)

  useEffect(() => {
    const list = ref.current
    if (!list) return
    const mq = window.matchMedia('(min-width: 768px) and (prefers-reduced-motion: no-preference)')
    let raf = 0

    const update = () => {
      raf = 0
      const cards = Array.from(list.querySelectorAll<HTMLElement>('[data-stack-card]'))
      cards.forEach((card, i) => {
        const next = cards[i + 1]
        if (!mq.matches || !next) {
          card.style.transform = ''
          card.style.filter = ''
          return
        }
        const a = card.getBoundingClientRect()
        const b = next.getBoundingClientRect()
        const cover = Math.min(1, Math.max(0, (a.bottom - b.top) / a.height))
        card.style.transform = `scale(${(1 - cover * 0.07).toFixed(4)})`
        card.style.filter = cover > 0.01 ? `brightness(${(1 - cover * 0.45).toFixed(3)})` : ''
      })
    }
    const onScroll = () => {
      if (!raf) raf = requestAnimationFrame(update)
    }
    update()
    window.addEventListener('scroll', onScroll, { passive: true })
    window.addEventListener('resize', onScroll)
    mq.addEventListener('change', onScroll)
    return () => {
      window.removeEventListener('scroll', onScroll)
      window.removeEventListener('resize', onScroll)
      mq.removeEventListener('change', onScroll)
      cancelAnimationFrame(raf)
    }
  }, [])

  return (
    <ol ref={ref} className={className}>
      {children}
    </ol>
  )
}
