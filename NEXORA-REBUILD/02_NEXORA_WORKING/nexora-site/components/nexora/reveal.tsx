'use client'

import { useEffect, useRef, useState, type ElementType, type ReactNode } from 'react'

export function Reveal({
  as: Tag = 'div',
  className,
  children,
  threshold = 0.2,
  ...rest
}: {
  as?: ElementType
  className?: string
  children: ReactNode
  threshold?: number
  [key: string]: unknown
}) {
  const ref = useRef<HTMLElement>(null)
  const [inView, setInView] = useState(false)

  useEffect(() => {
    const el = ref.current
    if (!el) return
    const io = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setInView(true)
          io.disconnect()
        }
      },
      { threshold, rootMargin: '0px 0px -8% 0px' },
    )
    io.observe(el)
    return () => io.disconnect()
  }, [threshold])

  return (
    <Tag ref={ref} data-reveal="" data-inview={inView} className={className} {...rest}>
      {children}
    </Tag>
  )
}

export function SplitWords({ text, offset = 0 }: { text: string; offset?: number }) {
  return (
    <>
      {text.split(' ').map((word, i) => (
        <span key={i} className="inline-block overflow-hidden pb-[0.08em] align-bottom">
          <span className="rv-word" style={{ '--i': i + offset } as React.CSSProperties}>
            {word}
            {'\u00A0'}
          </span>
        </span>
      ))}
    </>
  )
}
