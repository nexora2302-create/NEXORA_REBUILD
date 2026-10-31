'use client'

import type { ReactNode } from 'react'

// Un seul écouteur pour toutes les tuiles : la lumière suit le pointeur dans la tuile survolée.
export function SpotGrid({ className, children }: { className?: string; children: ReactNode }) {
  const onMove = (e: React.PointerEvent<HTMLDivElement>) => {
    if (e.pointerType !== 'mouse') return
    const tile = (e.target as HTMLElement).closest<HTMLElement>('.spot')
    if (!tile) return
    const r = tile.getBoundingClientRect()
    tile.style.setProperty('--mx', `${e.clientX - r.left}px`)
    tile.style.setProperty('--my', `${e.clientY - r.top}px`)
  }
  return (
    <div className={className} onPointerMove={onMove}>
      {children}
    </div>
  )
}
