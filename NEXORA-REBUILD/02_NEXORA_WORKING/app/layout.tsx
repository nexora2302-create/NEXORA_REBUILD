import { Analytics } from '@vercel/analytics/next'
import type { Metadata, Viewport } from 'next'
import { Archivo, Instrument_Serif, JetBrains_Mono } from 'next/font/google'
import { FAQ_ITEMS } from '@/components/nexora/faq'
import './globals.css'

const SITE_URL = process.env.NEXT_PUBLIC_SITE_URL ?? 'https://nexora.bj'

const archivo = Archivo({ subsets: ['latin'], axes: ['wdth'], variable: '--font-archivo', display: 'swap' })
const instrument = Instrument_Serif({ subsets: ['latin'], weight: '400', style: ['normal', 'italic'], variable: '--font-instrument', display: 'swap' })
const jetbrains = JetBrains_Mono({ subsets: ['latin'], variable: '--font-jetbrains', display: 'swap' })

const TITLE = 'NEXORA — Studio créatif en mouvement · Cotonou, Bénin'
const DESCRIPTION =
  'NEXORA est un studio créatif et digital basé à Cotonou : communication visuelle, motion design et création de sites web pour les marques au Bénin, en Afrique et à l’international.'

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: TITLE,
  description: DESCRIPTION,
  alternates: { canonical: '/' },
  openGraph: { type: 'website', locale: 'fr_FR', siteName: 'NEXORA', title: TITLE, description: DESCRIPTION, url: '/' },
  twitter: { card: 'summary_large_image', title: TITLE, description: DESCRIPTION },
  icons: { icon: '/icon.svg', apple: '/apple-icon.png' },
}

export const viewport: Viewport = { themeColor: '#0d0c0b' }

const jsonLd = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'Organization',
      name: 'NEXORA',
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
    <html lang="fr" className={`${archivo.variable} ${instrument.variable} ${jetbrains.variable}`}>
      <body className="antialiased">
        {children}
        <script type="application/ld+json" dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }} />
        {process.env.NODE_ENV === 'production' && <Analytics />}
      </body>
    </html>
  )
}
