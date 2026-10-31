'use client'

import { useEffect, useRef, type ReactNode } from 'react'

// Un seul écouteur de scroll pour toutes les couches (au lieu d'un par image).
const layers = new Set<HTMLElement>()
let raf = 0
let bound = false

function update() {
  raf = 0
  const vh = window.innerHeight
  layers.forEach((el) => {
    const parent = el.parentElement
    if (!parent) return
    const r = parent.getBoundingClientRect()
    if (r.bottom < -120 || r.top > vh + 120) return
    const offset = (r.top + r.height / 2 - vh / 2) * -0.08
    el.style.transform = `translate3d(0, ${offset.toFixed(1)}px, 0)`
  })
}

function schedule() {
  if (!raf) raf = requestAnimationFrame(update)
}

export function ParallaxLayer({ children }: { children: ReactNode }) {
  const ref = useRef<HTMLDivElement>(null)

  useEffect(() => {
    const el = ref.current
    if (!el || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return
    layers.add(el)
    if (!bound) {
      bound = true
      window.addEventListener('scroll', schedule, { passive: true })
      window.addEventListener('resize', schedule)
    }
    schedule()
    return () => {
      layers.delete(el)
      if (layers.size === 0 && bound) {
        bound = false
        window.removeEventListener('scroll', schedule)
        window.removeEventListener('resize', schedule)
      }
    }
  }, [])

  return (
    <div ref={ref} className="absolute inset-x-0 top-[-7.5%] h-[115%] will-change-transform">
      {children}
    </div>
  )
}
