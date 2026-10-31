'use client'

import { useEffect, useRef, type ReactNode } from 'react'

/*
 * Pile de cartes collantes (desktop) : quand la carte suivante monte vers sa place,
 * la précédente recule (échelle) et s'assombrit. Transform et opacité uniquement,
 * un seul écouteur de scroll cadencé par requestAnimationFrame.
 */
export function StackCards({ children }: { children: ReactNode }) {
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const root = ref.current
    if (!root) return
    const mq = window.matchMedia('(min-width: 768px) and (prefers-reduced-motion: no-preference)')
    const items = Array.from(root.querySelectorAll<HTMLElement>('[data-stack]'))
    let raf = 0

    const reset = () =>
      items.forEach((el) => {
        el.style.removeProperty('--s')
        el.style.removeProperty('--dim')
      })

    const update = () => {
      raf = 0
      if (!mq.matches) return reset()
      const vh = window.innerHeight
      // Avancée de chaque carte vers sa position collée (0 = loin, 1 = en place).
      const arrive = items.map((el) => {
        const top = parseFloat(getComputedStyle(el).top) || 0
        const d = el.getBoundingClientRect().top - top
        return Math.min(1, Math.max(0, 1 - d / (vh * 0.75)))
      })
      items.forEach((el, i) => {
        let covered = 0
        for (let j = i + 1; j < items.length; j++) covered += arrive[j]
        el.style.setProperty('--s', (1 - covered * 0.05).toFixed(4))
        el.style.setProperty('--dim', Math.min(0.6, covered * 0.38).toFixed(3))
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
    <div ref={ref} className="stack flex flex-col gap-4 md:gap-[12vh]">
      {children}
    </div>
  )
}
