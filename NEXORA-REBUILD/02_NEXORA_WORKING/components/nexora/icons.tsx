// Icônes dessinées, trait unique 1.5, coins arrondis.
type P = { className?: string }

export function ArrowIcon({ className }: P) {
  return (
    <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" aria-hidden className={className}>
      <path d="M4.5 11.5l7-7M5.5 4.5h6v6" />
    </svg>
  )
}

export function PlusIcon({ className }: P) {
  return (
    <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" aria-hidden className={className}>
      <path d="M8 3v10M3 8h10" />
    </svg>
  )
}

export function UpIcon({ className }: P) {
  return (
    <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round" aria-hidden className={className}>
      <path d="M8 13V3M4 7l4-4 4 4" />
    </svg>
  )
}

export function StarIcon({ className }: P) {
  return (
    <svg viewBox="0 0 40 40" aria-hidden className={className}>
      <path d="M20 0 L24 16 L40 20 L24 24 L20 40 L16 24 L0 20 L16 16 Z" fill="currentColor" />
    </svg>
  )
}
