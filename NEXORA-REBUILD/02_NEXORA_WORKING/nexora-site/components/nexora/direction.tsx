'use client'

import { createContext, useContext, useEffect, useState } from 'react'

export type Direction = 'nuit' | 'jour'

const DirectionContext = createContext<{
  direction: Direction
  setDirection: (d: Direction) => void
}>({ direction: 'nuit', setDirection: () => {} })

export function DirectionProvider({ children }: { children: React.ReactNode }) {
  const [direction, setDirection] = useState<Direction>('nuit')

  useEffect(() => {
    document.documentElement.dataset.direction = direction
    document
      .querySelector('meta[name="theme-color"]')
      ?.setAttribute('content', direction === 'nuit' ? '#0d0c0b' : '#eeeae0')
  }, [direction])

  return (
    <DirectionContext.Provider value={{ direction, setDirection }}>
      {children}
    </DirectionContext.Provider>
  )
}

export const useDirection = () => useContext(DirectionContext)

const OPTIONS: { id: Direction; code: string; name: string; note: string }[] = [
  { id: 'nuit', code: 'A', name: 'Nuit cinématique', note: 'Encre · Os · Vermillon' },
  { id: 'jour', code: 'B', name: 'Plein jour éditorial', note: 'Papier · Encre · Indigo' },
]

export function DirectionSwitch() {
  const { direction, setDirection } = useDirection()

  return (
    <div className="fixed inset-x-0 bottom-4 z-50 flex justify-center px-4 md:bottom-6">
      <div
        role="group"
        aria-label="Direction artistique"
        className="flex items-center gap-1 rounded-full border border-line bg-background/80 p-1 shadow-2xl backdrop-blur-md"
      >
        <span className="hidden pl-3 pr-2 text-[10px] uppercase tracking-[0.2em] text-muted-foreground sm:block">
          Direction
        </span>
        {OPTIONS.map((o) => {
          const active = direction === o.id
          return (
            <button
              key={o.id}
              type="button"
              aria-pressed={active}
              onClick={() => setDirection(o.id)}
              className={`flex items-center gap-2 rounded-full px-3 py-2 text-left transition-colors duration-500 md:px-4 ${
                active
                  ? 'bg-accent text-accent-foreground'
                  : 'text-foreground hover:bg-foreground/10'
              }`}
            >
              <span className="font-serif text-lg italic leading-none">{o.code}</span>
              <span className="flex flex-col">
                <span className="text-xs font-semibold uppercase leading-tight tracking-wide">
                  {o.name}
                </span>
                <span className="hidden text-[10px] leading-tight opacity-70 md:block">
                  {o.note}
                </span>
              </span>
            </button>
          )
        })}
      </div>
    </div>
  )
}
