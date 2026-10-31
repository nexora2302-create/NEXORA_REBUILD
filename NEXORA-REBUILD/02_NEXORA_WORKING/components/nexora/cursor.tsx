'use client'

import { useEffect, useRef } from 'react'

export function Cursor() {
  const ref = useRef<HTMLDivElement>(null)
  const labelRef = useRef<HTMLSpanElement>(null)

  useEffect(() => {
    if (!window.matchMedia('(pointer: fine)').matches) return
    const el = ref.current
    const label = labelRef.current
    if (!el || !label) return

    const target = { x: -100, y: -100 }
    const pos = { x: -100, y: -100 }
    let raf = 0

    const onMove = (e: PointerEvent) => {
      target.x = e.clientX
      target.y = e.clientY
      const hit = (e.target as HTMLElement).closest<HTMLElement>('[data-cursor], a, button')
      const text = hit?.dataset.cursor
      el.dataset.state = text ? 'label' : hit ? 'link' : 'idle'
      label.textContent = text ?? ''
    }
    const loop = () => {
      pos.x += (target.x - pos.x) * 0.2
      pos.y += (target.y - pos.y) * 0.2
      el.style.transform = `translate3d(${pos.x}px, ${pos.y}px, 0)`
      raf = requestAnimationFrame(loop)
    }

    el.style.display = 'block'
    window.addEventListener('pointermove', onMove, { passive: true })
    raf = requestAnimationFrame(loop)
    return () => {
      window.removeEventListener('pointermove', onMove)
      cancelAnimationFrame(raf)
    }
  }, [])

  return (
    <div ref={ref} aria-hidden data-state="idle" className="group pointer-events-none fixed left-0 top-0 z-[70] hidden">
      <div className="flex size-3 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full bg-accent transition-[width,height] duration-500 ease-[cubic-bezier(0.16,1,0.3,1)] group-data-[state=label]:size-24 group-data-[state=link]:size-8 group-data-[state=link]:opacity-60">
        <span ref={labelRef} className="text-[11px] font-semibold uppercase tracking-[0.16em] text-accent-foreground opacity-0 transition-opacity group-data-[state=label]:opacity-100" />
      </div>
    </div>
  )
}
