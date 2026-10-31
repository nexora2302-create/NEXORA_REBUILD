import { Contact, Footer } from '@/components/nexora/contact'
import { Cursor } from '@/components/nexora/cursor'
import { Expertises } from '@/components/nexora/expertises'
import { Faq } from '@/components/nexora/faq'
import { Header } from '@/components/nexora/header'
import { Hero } from '@/components/nexora/hero'
import { Manifesto } from '@/components/nexora/manifesto'
import { Marquee } from '@/components/nexora/marquee'
import { Method } from '@/components/nexora/method'
import { Work } from '@/components/nexora/work'

export default function Page() {
  return (
    <>
      <a href="#contenu" className="sr-only z-[80] bg-accent px-4 py-2 text-accent-foreground focus:not-sr-only focus:fixed focus:left-4 focus:top-4">
        Aller au contenu
      </a>
      <Header />
      <main id="contenu">
        <Hero />
        <Manifesto />
        <Expertises />
        <Work />
        <Marquee />
        <Method />
        <Faq />
        <Contact />
      </main>
      <Footer />
      <Cursor />
    </>
  )
}
