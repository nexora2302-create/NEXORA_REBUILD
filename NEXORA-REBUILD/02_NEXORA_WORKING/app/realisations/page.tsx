import type { Metadata } from 'next'
import { Footer } from '@/components/nexora/contact'
import { Header } from '@/components/nexora/header'
import { ArrowIcon } from '@/components/nexora/icons'
import { ProjectsIndex } from '@/components/nexora/projects-index'
import { Reveal, SplitWords } from '@/components/nexora/reveal'

export const metadata: Metadata = {
  title: 'Réalisations, concepts du studio | NEXORA',
  description:
    'Identité visuelle, motion design et sites web : les concepts d’exploration du studio NEXORA à Cotonou, présentés projet par projet.',
  alternates: { canonical: '/realisations' },
  openGraph: { url: '/realisations', title: 'Réalisations | NEXORA' },
}

export default function RealisationsPage() {
  return (
    <>
      <a href="#contenu" className="sr-only z-[80] bg-accent px-4 py-2 text-accent-foreground focus:not-sr-only focus:fixed focus:left-4 focus:top-4">
        Aller au contenu
      </a>
      <Header base="/" />
      <main id="contenu">
        <section id="top" className="px-4 pb-12 pt-32 md:px-8 md:pb-16 md:pt-40">
          <a href="/#travaux" className="group inline-flex min-h-11 items-center gap-2 text-[15px] text-foreground/80 transition-colors hover:text-foreground">
            <ArrowIcon className="size-4 -rotate-[135deg] transition-transform duration-500 group-hover:-translate-x-0.5" />
            Retour à l’accueil
          </a>
          <Reveal className="mt-8 grid gap-8 md:grid-cols-12 md:items-end">
            <h1 className="t-section md:col-span-7">
              <SplitWords text="Réalisations" />
            </h1>
            <p className="max-w-md text-[17px] leading-relaxed text-foreground/85 md:col-span-5 md:text-lg">
              Huit concepts d’exploration imaginés par le studio pour montrer sa façon de travailler, en identité, en motion et sur le web. Ils laisseront bientôt leur place aux projets clients.
            </p>
          </Reveal>
        </section>

        <ProjectsIndex />

        <section data-header="signal" aria-labelledby="next-title" className="theme-signal mt-32 px-4 py-24 md:mt-40 md:px-8 md:py-32">
          <h2 id="next-title" className="t-section max-w-[16ch]">
            La prochaine, c’est la vôtre.
          </h2>
          <a
            href="/#contact"
            className="group mt-10 inline-flex min-h-14 items-center gap-4 rounded-full bg-foreground pl-7 pr-2 text-[16px] font-semibold text-background transition-transform duration-500 hover:scale-[1.03]"
          >
            Parler de votre projet
            <span className="grid size-10 place-items-center rounded-full bg-background text-foreground transition-transform duration-500 group-hover:rotate-45">
              <ArrowIcon className="size-4" />
            </span>
          </a>
        </section>
      </main>
      <Footer base="/" />
    </>
  )
}
