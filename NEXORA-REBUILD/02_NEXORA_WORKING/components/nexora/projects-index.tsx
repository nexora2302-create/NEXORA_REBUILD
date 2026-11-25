'use client'

import Image from 'next/image'
import { useState, type CSSProperties, type PointerEvent } from 'react'
import { flushSync } from 'react-dom'
import { DISCIPLINES, PROJECTS, type Discipline, type Project } from '@/lib/projects'
import { FilmDialog } from './film-dialog'
import { fr } from './fr'
import { PlayIcon } from './icons'
import { LoopVideo } from './loop-video'
import { Reveal } from './reveal'

type Filter = Discipline | 'tout'
type Play = (p: Project) => void

const num = (i: number) => String(i + 1).padStart(2, '0')
const v = (i: number) => ({ '--i': i }) as CSSProperties

export function ProjectsIndex() {
  const [filter, setFilter] = useState<Filter>('tout')
  const [playing, setPlaying] = useState<Project | null>(null)
  const list = filter === 'tout' ? PROJECTS : PROJECTS.filter((p) => p.discipline === filter)

  // Le changement de filtre passe par une View Transition quand le navigateur la propose.
  const choose = (f: Filter) => {
    if (f === filter) return
    const apply = () => setFilter(f)
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    if (!reduced && 'startViewTransition' in document) {
      ;(document as Document & { startViewTransition: (cb: () => void) => unknown }).startViewTransition(() => flushSync(apply))
    } else apply()
  }

  const chips: { id: Filter; label: string; count: number }[] = [
    { id: 'tout', label: 'Tout', count: PROJECTS.length },
    ...DISCIPLINES.map((d) => ({ id: d.id, label: d.label, count: PROJECTS.filter((p) => p.discipline === d.id).length })),
  ]

  return (
    <>
      <div role="group" aria-label="Filtrer par discipline" className="flex flex-wrap gap-2 px-4 md:px-8">
        {chips.map((c) => {
          const on = c.id === filter
          return (
            <button
              key={c.id}
              type="button"
              aria-pressed={on}
              onClick={() => choose(c.id)}
              className={`inline-flex min-h-11 items-center gap-2 rounded-full border px-5 text-[15px] font-medium transition-colors duration-300 ${
                on ? 'border-accent bg-accent text-accent-foreground' : 'border-line hover:border-foreground/50'
              }`}
            >
              {c.label}
              <span className={`text-[13px] tabular-nums ${on ? 'opacity-80' : 'text-muted-foreground'}`}>{c.count}</span>
            </button>
          )
        })}
      </div>

      <p role="status" className="sr-only">
        {list.length} {list.length > 1 ? 'projets affichés' : 'projet affiché'}
      </p>

      <ol className="mt-16 flex flex-col gap-32 px-4 md:mt-24 md:gap-48 md:px-8">
        {list.map((p) => {
          const i = PROJECTS.indexOf(p)
          return (
            <li key={p.slug} id={p.slug} className="scroll-mt-28" style={{ viewTransitionName: `case-${p.slug}` }}>
              {p.web ? (
                <WebCase p={p} i={i} />
              ) : p.film?.vertical ? (
                <VerticalCase p={p} i={i} onPlay={setPlaying} />
              ) : (
                <FilmCase p={p} i={i} onPlay={setPlaying} />
              )}
            </li>
          )
        })}
      </ol>

      <FilmDialog project={playing} onClose={() => setPlaying(null)} />
    </>
  )
}

/* Ligne de repère : numéro, discipline, année. */
function Meta({ p, i }: { p: Project; i: number }) {
  return (
    <div className="flex items-baseline justify-between gap-6 border-t border-line pt-4 font-mono text-[12px] uppercase tracking-[0.08em] text-muted-foreground md:col-span-12">
      <span className="tabular-nums">
        <span className="text-accent">{num(i)}</span> / {num(PROJECTS.length - 1)}
      </span>
      <span className="truncate">
        {p.tag}
        {p.status ? ` · ${p.status}` : ''}
      </span>
      <span className="hidden md:inline">{p.year}</span>
    </div>
  )
}

function Info({ p, onPlay, className = '' }: { p: Project; onPlay?: Play; className?: string }) {
  return (
    <Reveal threshold={0.15} className={className}>
      <p className="rv-up text-[15px] font-medium text-accent" style={v(0)}>
        {p.client}
      </p>
      <h2 id={`t-${p.slug}`} className="t-card rv-up mt-3" style={v(1)}>
        {p.title}
      </h2>
      <p className="rv-up mt-6 max-w-[46ch] text-[17px] leading-relaxed text-foreground/85" style={v(2)}>
        {fr(p.idea)}
      </p>
      <dl className="rv-up mt-8 grid grid-cols-2 gap-x-6 border-t border-line" style={v(3)}>
        <div className="border-b border-line py-3">
          <dt className="font-mono text-[11px] uppercase tracking-[0.08em] text-muted-foreground">Format</dt>
          <dd className="mt-1 text-[15px] font-medium">{p.format}</dd>
        </div>
        <div className="border-b border-line py-3">
          <dt className="font-mono text-[11px] uppercase tracking-[0.08em] text-muted-foreground">{p.film ? 'Durée' : 'État'}</dt>
          <dd className="mt-1 text-[15px] font-medium">{p.film ? p.film.duration : (p.status ?? 'En ligne')}</dd>
        </div>
      </dl>
      <ul className="rv-up mt-5 flex flex-wrap gap-2" style={v(4)} aria-label="Ce que nous avons fait">
        {p.done.map((e) => (
          <li key={e} className="rounded-full border border-line px-3.5 py-1.5 text-[14px] text-foreground/85">
            {e}
          </li>
        ))}
      </ul>
      {p.film && onPlay && (
        <div className="rv-up mt-8" style={v(5)}>
          <button
            type="button"
            onClick={() => onPlay(p)}
            className="group inline-flex min-h-14 items-center gap-4 rounded-full bg-accent pl-2 pr-7 text-[16px] font-semibold text-accent-foreground transition-transform duration-500 hover:scale-[1.03]"
          >
            <span className="grid size-10 place-items-center rounded-full bg-accent-foreground text-accent transition-transform duration-500 group-hover:scale-110">
              <PlayIcon className="size-3.5 translate-x-px" />
            </span>
            Voir le film
            <span className="font-normal opacity-75">{p.film.duration}</span>
          </button>
        </div>
      )}
    </Reveal>
  )
}

/* Le média d'un film : extrait en boucle, pastille « Lecture » qui suit le pointeur. */
function FilmMedia({ p, onPlay, className = '', frame, sizes }: { p: Project; onPlay: Play; className?: string; frame: string; sizes: string }) {
  const follow = (e: PointerEvent<HTMLButtonElement>) => {
    const r = e.currentTarget.getBoundingClientRect()
    e.currentTarget.style.setProperty('--mx', `${e.clientX - r.left}px`)
    e.currentTarget.style.setProperty('--my', `${e.clientY - r.top}px`)
  }
  if (!p.film || !p.loop) return null
  return (
    <Reveal threshold={0.12} className={className}>
      <button
        type="button"
        onClick={() => onPlay(p)}
        onPointerEnter={follow}
        onPointerMove={follow}
        aria-label={`Voir le film ${p.title}, ${p.film.duration}`}
        className="film-media group relative block w-full text-left outline-offset-4 focus-visible:outline-2 focus-visible:outline-accent"
      >
        <div className={`rv-curtain relative overflow-hidden bg-card ${frame}`} style={{ viewTransitionName: `work-${p.slug}` }}>
          <LoopVideo
            src={p.loop}
            poster={p.poster}
            alt={p.alt}
            sizes={sizes}
            className="absolute inset-0 transition-transform duration-[1.2s] ease-[var(--ease-out-expo)] group-hover:scale-[1.03]"
          />
        </div>
        <span className="film-pill pointer-events-none absolute bottom-4 left-4 inline-flex items-center gap-2.5 rounded-full bg-background/80 py-2 pl-2.5 pr-4 text-[14px] font-medium text-foreground backdrop-blur-md md:bottom-5 md:left-5">
          <span className="grid size-6 place-items-center rounded-full bg-accent text-accent-foreground">
            <PlayIcon className="size-2.5 translate-x-px" />
          </span>
          Voir le film · {p.film.duration}
        </span>
        <span className="film-cursor" aria-hidden>
          <PlayIcon className="size-4" />
          Lecture
        </span>
      </button>
    </Reveal>
  )
}

function Stills({ p, className = '', vertical = false }: { p: Project; className?: string; vertical?: boolean }) {
  if (!p.stills) return null
  return (
    <Reveal threshold={0.15} className={`grid grid-cols-3 gap-2 md:gap-4 ${className}`}>
      {p.stills.map((s, k) => (
        <figure key={s.src} className={`rv-curtain relative overflow-hidden bg-card ${vertical ? 'aspect-[9/16]' : 'aspect-video'}`} style={v(k + 1)}>
          <Image src={s.src} alt={s.alt ?? ''} fill sizes={vertical ? '(min-width: 768px) 16vw, 33vw' : '(min-width: 768px) 22vw, 33vw'} placeholder="blur" blurDataURL={s.blur} quality={80} className="object-cover" />
        </figure>
      ))}
    </Reveal>
  )
}

function FilmCase({ p, i, onPlay }: { p: Project; i: number; onPlay: Play }) {
  const flip = i % 2 === 1
  return (
    <article aria-labelledby={`t-${p.slug}`} className="grid gap-y-8 md:grid-cols-12 md:gap-x-8 md:gap-y-6">
      <Meta p={p} i={i} />
      <FilmMedia
        p={p}
        onPlay={onPlay}
        frame="aspect-video"
        sizes="(min-width: 768px) 64vw, 100vw"
        className={`md:col-span-8 md:row-start-2 ${flip ? 'md:col-start-5' : 'md:col-start-1'}`}
      />
      <Stills p={p} className={`md:col-span-8 md:row-start-3 ${flip ? 'md:col-start-5' : 'md:col-start-1'}`} />
      <Info p={p} onPlay={onPlay} className={`md:sticky md:top-28 md:col-span-4 md:row-span-2 md:row-start-2 md:self-start md:pt-2 ${flip ? 'md:col-start-1 md:pr-6' : 'md:col-start-9 md:pl-2'}`} />
    </article>
  )
}

function VerticalCase({ p, i, onPlay }: { p: Project; i: number; onPlay: Play }) {
  return (
    <article aria-labelledby={`t-${p.slug}`} className="grid gap-y-8 md:grid-cols-12 md:gap-x-8 md:gap-y-10">
      <Meta p={p} i={i} />
      <FilmMedia
        p={p}
        onPlay={onPlay}
        frame="aspect-[9/16]"
        sizes="(min-width: 1536px) 24vw, (min-width: 768px) 32vw, 80vw"
        className="mx-auto w-[82%] md:col-span-4 md:col-start-1 md:row-span-2 md:row-start-2 md:w-full 2xl:col-span-3"
      />
      <Info p={p} onPlay={onPlay} className="md:col-span-7 md:col-start-6 md:row-start-2 2xl:col-span-6 2xl:col-start-6" />
      <Stills p={p} vertical className="md:col-span-7 md:col-start-6 md:row-start-3 md:self-end 2xl:col-span-6 2xl:col-start-6" />
    </article>
  )
}

function WebCase({ p, i }: { p: Project; i: number }) {
  const flip = i % 2 === 1
  if (!p.web) return null
  return (
    <article aria-labelledby={`t-${p.slug}`} className="grid gap-y-8 md:grid-cols-12 md:gap-x-8 md:gap-y-6">
      <Meta p={p} i={i} />
      <Reveal threshold={0.12} className={`md:col-span-8 md:row-start-2 ${flip ? 'md:col-start-5' : 'md:col-start-1'}`}>
        <figure className="rv-curtain overflow-hidden rounded-[10px] bg-card ring-1 ring-line" style={{ viewTransitionName: `work-${p.slug}` }}>
          <div className="flex h-9 items-center gap-1.5 border-b border-line px-4 md:h-10">
            <i className="size-2.5 rounded-full bg-foreground/20" />
            <i className="size-2.5 rounded-full bg-foreground/20" />
            <i className="size-2.5 rounded-full bg-foreground/20" />
            <span className="mx-auto max-w-[60%] truncate rounded-full bg-foreground/[0.06] px-4 py-1 font-mono text-[11px] text-muted-foreground">{p.web.url}</span>
            <span className="w-[42px]" aria-hidden />
          </div>
          <div className="relative" style={{ aspectRatio: p.web.ratio }}>
            <LoopVideo src={p.web.src} poster={p.poster} alt={p.alt} sizes="(min-width: 768px) 64vw, 100vw" className="absolute inset-0" />
          </div>
          <figcaption className="sr-only">Défilement de la page d’accueil, enregistré image par image.</figcaption>
        </figure>
      </Reveal>
      <Info p={p} className={`md:sticky md:top-28 md:col-span-4 md:row-start-2 md:self-start md:pt-2 ${flip ? 'md:col-start-1 md:pr-6' : 'md:col-start-9 md:pl-2'}`} />
    </article>
  )
}
