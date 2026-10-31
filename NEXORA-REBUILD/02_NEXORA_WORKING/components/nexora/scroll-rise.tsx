'use client'

import { useEffect, useRef, type ReactNode } from 'react'

/*
 * Apparition liée au scroll : l'élément monte, se redresse (rotateX) et grandit
 * à mesure qu'il entre dans l'écran. Un seul écouteur pour tous les éléments.
 */
const items = new Map<HTMLElement, number>()
let raf = 0
let bound = false

function update() {
  raf = 0
  const vh = window.innerHeight
  items.forEach((delay, el) => {
    const r = el.getBoundingClientRect()
    if (r.top > vh + 200 || r.bottom < -200) return
    const p = Math.min(1, Math.max(0, (vh - r.top) / (vh * 0.65) - delay))
    const e = 1 - Math.pow(1 - p, 3)
    el.style.setProperty('--rise', e.toFixed(4))
  })
}
const schedule = () => {
  if (!raf) raf = requestAnimationFrame(update)
}

export function ScrollRise({ children, className = '', delay = 0 }: { children: ReactNode; className?: string; delay?: number }) {
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const el = ref.current
    if (!el || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      el?.style.setProperty('--rise', '1')
      return
    }
    items.set(el, delay)
    if (!bound) {
      bound = true
      window.addEventListener('scroll', schedule, { passive: true })
      window.addEventListener('resize', schedule)
    }
    schedule()
    return () => {
      items.delete(el)
      if (!items.size && bound) {
        bound = false
        window.removeEventListener('scroll', schedule)
        window.removeEventListener('resize', schedule)
      }
    }
  }, [delay])

  return (
    <div ref={ref} className={`rise ${className}`} style={{ '--rise': 0 } as React.CSSProperties}>
      {children}
    </div>
  )
}
