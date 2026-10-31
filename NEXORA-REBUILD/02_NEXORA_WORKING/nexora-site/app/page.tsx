import { Contact, Footer } from '@/components/nexora/contact'
import { Cursor } from '@/components/nexora/cursor'
import { DirectionProvider, DirectionSwitch } from '@/components/nexora/direction'
import { Expertises } from '@/components/nexora/expertises'
import { Header } from '@/components/nexora/header'
import { Hero } from '@/components/nexora/hero'
import { Manifesto } from '@/components/nexora/manifesto'
import { Marquee } from '@/components/nexora/marquee'
import { Work } from '@/components/nexora/work'

export default function Page() {
  return (
    <DirectionProvider>
      <Header />
      <main>
        <Hero />
        <Manifesto />
        <Expertises />
        <Work />
        <Marquee />
        <Contact />
      </main>
      <Footer />
      <DirectionSwitch />
      <Cursor />
    </DirectionProvider>
  )
}
