'use client'

import { useState } from 'react'

const EMAIL = 'bonjour@nexora.bj'
const SERVICES = ['Communication visuelle', 'Motion design', 'Site web', 'Autre / plusieurs']

type Errors = Partial<Record<'name' | 'email' | 'message', string>>

export function ContactForm() {
  const [errors, setErrors] = useState<Errors>({})
  const [sent, setSent] = useState(false)

  const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const data = new FormData(e.currentTarget)
    if (data.get('website')) return // honeypot
    const name = String(data.get('name') ?? '').trim()
    const email = String(data.get('email') ?? '').trim()
    const service = String(data.get('service') ?? '')
    const message = String(data.get('message') ?? '').trim()

    const next: Errors = {}
    if (!name) next.name = 'Indiquez votre nom.'
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) next.email = 'Indiquez une adresse e-mail valide.'
    if (message.length < 10) next.message = 'Décrivez votre projet en quelques mots.'
    setErrors(next)
    if (Object.keys(next).length) return

    const body = `Nom : ${name}\nE-mail : ${email}\nService : ${service}\n\n${message}`
    window.location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(`Nouveau projet — ${name}`)}&body=${encodeURIComponent(body)}`
    setSent(true)
  }

  const field = 'w-full border-b border-line bg-transparent py-3 text-base outline-none transition-colors placeholder:text-muted-foreground focus:border-accent'
  const label = 'font-mono text-[11px] uppercase tracking-[0.16em] text-muted-foreground'

  return (
    <form onSubmit={onSubmit} noValidate className="grid grid-cols-1 gap-8 md:grid-cols-2" aria-describedby="form-status">
      <div>
        <label htmlFor="name" className={label}>Nom</label>
        <input id="name" name="name" autoComplete="name" required aria-invalid={!!errors.name} aria-describedby={errors.name ? 'err-name' : undefined} className={field} placeholder="Votre nom" />
        {errors.name && <p id="err-name" className="mt-2 text-sm text-accent">{errors.name}</p>}
      </div>
      <div>
        <label htmlFor="email" className={label}>E-mail</label>
        <input id="email" name="email" type="email" autoComplete="email" required aria-invalid={!!errors.email} aria-describedby={errors.email ? 'err-email' : undefined} className={field} placeholder="vous@exemple.com" />
        {errors.email && <p id="err-email" className="mt-2 text-sm text-accent">{errors.email}</p>}
      </div>
      <div className="md:col-span-2">
        <label htmlFor="service" className={label}>Besoin</label>
        <select id="service" name="service" className={`${field} appearance-none`} defaultValue={SERVICES[0]}>
          {SERVICES.map((s) => (
            <option key={s} className="bg-background text-foreground">{s}</option>
          ))}
        </select>
      </div>
      <div className="md:col-span-2">
        <label htmlFor="message" className={label}>Votre projet</label>
        <textarea id="message" name="message" rows={4} required aria-invalid={!!errors.message} aria-describedby={errors.message ? 'err-message' : undefined} className={`${field} resize-y`} placeholder="Contexte, objectifs, délais…" />
        {errors.message && <p id="err-message" className="mt-2 text-sm text-accent">{errors.message}</p>}
      </div>
      {/* Honeypot anti-spam */}
      <input name="website" tabIndex={-1} autoComplete="off" aria-hidden className="absolute left-[-9999px] h-0 w-0 opacity-0" />
      <div className="flex flex-col gap-4 md:col-span-2 md:flex-row md:items-center md:justify-between">
        <button type="submit" className="self-start rounded-full bg-accent px-8 py-4 font-mono text-xs font-semibold uppercase tracking-[0.16em] text-accent-foreground transition-transform duration-500 hover:scale-105 focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-foreground">
          Envoyer le message →
        </button>
        <p id="form-status" role="status" className="text-sm text-muted-foreground">
          {sent ? 'Votre messagerie s’ouvre avec le message prêt à envoyer.' : 'Le message s’ouvre dans votre application e-mail.'}
        </p>
      </div>
    </form>
  )
}
