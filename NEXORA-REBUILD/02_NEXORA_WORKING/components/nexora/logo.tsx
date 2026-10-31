// Logo NEXORA : wordmark large, le X en braise comme dans le mot-signature du hero.
export function Logo({ className = '' }: { className?: string }) {
  return (
    <span className={`font-wide font-black uppercase leading-none tracking-[-0.02em] ${className}`}>
      NE<span className="text-[var(--logo-x,#ff4a1c)]">X</span>ORA
    </span>
  )
}
