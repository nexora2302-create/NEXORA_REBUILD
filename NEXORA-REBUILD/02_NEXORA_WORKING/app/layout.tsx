import { Analytics } from '@vercel/analytics/next'
import type { Metadata, Viewport } from 'next'
import { Archivo, JetBrains_Mono, Mr_Dafoe, Unbounded } from 'next/font/google'
import { FAQ_ITEMS } from '@/components/nexora/faq'
import './globals.css'

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL ?? 'https://nexora.bj'

const archivo = Archivo({ subsets: ['latin'], axes: ['wdth'], variable: '--font-archivo', display: 'swap' })
const unbounded = Unbounded({ subsets: ['latin'], variable: '--font-unbounded', display: 'swap' })
const dafoe = Mr_Dafoe({ subsets: ['latin'], weight: '400', variable: '--font-dafoe', display: 'swap' })
const jetbrains = JetBrains_Mono({ subsets: ['latin'], variable: '--font-jetbrains', display: 'swap' })

const TITLE = 'NEXORA Studio, motion design et sites web à Cotonou, Bénin'
const DESCRIPTION =
  'NEXORA Studio est un studio créatif et digital basé à Cotonou : communication visuelle, motion design et création de sites web pour les marques au Bénin, en Afrique et à l’international.'

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: '/' },
  openGraph: { type: 'website', locale: 'fr_FR', siteName: 'NEXORA Studio', title: TITLE, description: DESCRIPTION, url: '/', images: [{ url: '/og.png', width: 1200, height: 630, alt: 'NEXORA Studio, studio créatif en mouvement à Cotonou' }] },
  twitter: { card: 'summary_large_image', title: TITLE, description: DESCRIPTION, images: ['/og.png'] },
  icons: { icon: '/icon.svg', apple: '/apple-icon.png' },
}

export const viewport: Viewport = { themeColor: '#0d0c0b' }

const jsonLd = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'Organization',
      name: 'NEXORA Studio',
      url: SITE_URL,
      email: 'bonjour@nexora.bj',
      description: DESCRIPTION,
      address: { '@type': 'PostalAddress', addressLocality: 'Cotonou', addressCountry: 'BJ' },
    },
    {
      '@type': 'FAQPage',
      mainEntity: FAQ_ITEMS.map((f) => ({ '@type': 'Question', name: f.q, acceptedAnswer: { '@type': 'Answer', text: f.a } })),
    },
  ],
}

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="fr" className={`${archivo.variable} ${unbounded.variable} ${dafoe.variable} ${jetbrains.variable}`}>
      <body className="antialiased">
        {children}
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
        {process.env.NODE_ENV === 'production' && <Analytics />}
      </body>
    </html>
  )
}
