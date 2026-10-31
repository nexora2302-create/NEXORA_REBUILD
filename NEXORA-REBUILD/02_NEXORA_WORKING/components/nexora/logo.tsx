// Logo NEXORA : monogramme NX dessiné en tracés. N dans la couleur du texte, X en braise
// (var --logo-x : braise sur fond sombre, braise foncée sur fond os, encre sur fond braise).
export const NX_N = 'M0 0h15l24 38V0h14v64H38L15 26v38H0z'
export const NX_X = 'M59 0h16l11.5 20L98 0h16L94.5 31.5 115 64H99L86.5 43 74 64H58l20.5-32.5z'

export function Logo({ className = '' }: { className?: string }) {
  return (
    <svg viewBox="0 0 116 64" role="img" aria-label="NEXORA" className={`h-[1.1em] w-auto ${className}`}>
      <path fill="currentColor" d={NX_N} />
      <path fill="var(--logo-x, #ff4a1c)" d={NX_X} />
    </svg>
  )
}
