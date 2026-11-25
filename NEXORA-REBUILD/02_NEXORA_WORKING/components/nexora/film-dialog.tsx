'use client'

import { useEffect, useRef } from 'react'
import type { Project } from '@/lib/projects'
import { CloseIcon } from './icons'

/* La vidéo complète, avec le son, en plein écran. Il ne se charge qu'à l'ouverture. */
export function FilmDialog({ project, onClose }: { project: Project | null; onClose: () => void }) {
  const ref = useRef<HTMLDialogElement>(null)

  useEffect(() => {
    const d = ref.current
    if (!d) return
    if (project && !d.open) d.showModal()
    if (!project && d.open) d.close()
  }, [project])

  const film = project?.film
  return (
    <dialog
      ref={ref}
      onClose={onClose}
      onClick={(e) => {
        if (e.target === e.currentTarget) ref.current?.close()
      }}
      aria-labelledby="film-title"
      className="film-dialog fixed inset-0 m-0 h-svh max-h-none w-screen max-w-none bg-transparent p-4 text-foreground open:grid open:place-items-center md:p-10"
    >
      {project && film && (
        <div className={`film-box flex flex-col ${film.vertical ? 'w-auto' : 'w-full max-w-[min(100%,calc((100svh-9rem)*16/9))]'}`}>
          <div className="flex items-center justify-between gap-6 pb-4">
            <p id="film-title" className="min-w-0 text-[15px] leading-snug">
              <span className="font-semibold">{project.title}</span>
              <span className="text-muted-foreground"> · {film.duration}</span>
            </p>
            <button
              type="button"
              onClick={() => ref.current?.close()}
              className="grid size-12 shrink-0 place-items-center rounded-full border border-line transition-colors duration-300 hover:border-foreground/60 hover:bg-foreground/5"
            >
              <CloseIcon className="size-4" />
              <span className="sr-only">Fermer la vidéo</span>
            </button>
          </div>
          <video
            key={project.slug}
            src={film.src}
            poster={project.poster.src}
            controls
            autoPlay
            playsInline
            className={`bg-black ${film.vertical ? 'aspect-[9/16] h-[calc(100svh-9rem)] w-auto max-w-full' : 'aspect-video w-full'}`}
          />
        </div>
      )}
    </dialog>
  )
}
