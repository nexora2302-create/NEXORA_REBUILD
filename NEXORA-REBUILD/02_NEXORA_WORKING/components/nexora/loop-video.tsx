'use client'

import Image from 'next/image'
import { useEffect, useRef, useState } from 'react'
import type { Picture } from '@/lib/projects'

/*
 * Extrait muet en boucle : l'affiche s'affiche tout de suite, la vidéo ne se charge
 * qu'à l'approche de l'écran et ne joue que lorsqu'elle est visible.
 * Rien ne bouge si le visiteur a réduit les animations ou économise ses données.
 */
export function LoopVideo({
  src,
  poster,
  alt,
  sizes,
  className = 'relative',
  fit = 'cover',
}: {
  src: string
  poster: Picture
  alt: string
  sizes: string
  className?: string
  fit?: 'cover' | 'contain'
}) {
  const box = useRef<HTMLDivElement>(null)
  const vid = useRef<HTMLVideoElement>(null)
  const [playing, setPlaying] = useState(false)

  useEffect(() => {
    const el = box.current
    const v = vid.current
    if (!el || !v) return
    const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    const save = (navigator as Navigator & { connection?: { saveData?: boolean } }).connection?.saveData
    if (reduce || save) return
    const io = new IntersectionObserver(
      ([e]) => {
        if (e.isIntersecting) {
          if (!v.dataset.loaded) {
            v.src = src
            v.dataset.loaded = '1'
          }
          v.play().catch(() => {})
        } else v.pause()
      },
      { threshold: 0.2, rootMargin: '120px 0px' },
    )
    io.observe(el)
    return () => io.disconnect()
  }, [src])

  const obj = fit === 'cover' ? 'object-cover' : 'object-contain'
  return (
    <div ref={box} className={`overflow-hidden ${className}`}>
      <div className="lv-inner absolute inset-0">
      <Image src={poster.src} alt={alt} fill sizes={sizes} placeholder="blur" blurDataURL={poster.blur} quality={82} className={obj} />
      <video
        ref={vid}
        muted
        loop
        playsInline
        preload="none"
        aria-hidden
        tabIndex={-1}
        onPlaying={() => setPlaying(true)}
        className={`absolute inset-0 size-full ${obj} transition-opacity duration-700 ${playing ? 'opacity-100' : 'opacity-0'}`}
      />
      </div>
    </div>
  )
}
