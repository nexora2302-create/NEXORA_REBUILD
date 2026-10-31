'use client'

import { useState } from 'react'
import { fr } from './fr'
import { ArrowIcon } from './icons'

const EMAIL = 'bonjour@nexora.bj'
// Service d'envoi (Formspree, Basin, etc.) : renseigner l'URL dans NEXT_PUBLIC_FORM_ENDPOINT.
// Sans URL, le formulaire prépare un e-mail dans la messagerie du visiteur.
const ENDPOINT = process.env.NEXT_PUBLIC_FORM_ENDPOINT
const SERVICES = ['Communication visuelle', 'Motion design', 'Site web', 'Plusieurs, ou je ne sais pas encore']

type Errors = Partial<Record<'name' | 'email' | 'message', string>>
type Status = 'idle' | 'sending' | 'sent' | 'mail' | 'error'

export function ContactForm() {
  const [errors, setErrors] = useState<Errors>({})
  const [status, setStatus] = useState<Status>('idle')

  const onSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault()
    const form = e.currentTarget
    const data = new FormData(form)
    if (data.get('website')) return // anti-spam
    const name = String(data.get('name') ?? '').trim()
    const email = String(data.get('email') ?? '').trim()
    const service = String(data.get('service') ?? '')
    const message = String(data.get('message') ?? '').trim()

    const next: Errors = {}
    if (!name) next.name = 'Indiquez votre nom.'
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) next.email = 'Cette adresse e-mail semble incomplète.'
    if (message.length < 10) next.message = 'Décrivez votre projet en une ou deux phrases.'
    setErrors(next)
    if (Object.keys(next).length) {
      form.querySelector<HTMLElement>('[aria-invalid="true"]')?.focus()
      return
    }

    if (!ENDPOINT) {
      const body = `Nom : ${name}\nE-mail : ${email}\nBesoin : ${service}\n\n${message}`
      window.location.href = `mailto:${EMAIL}?subject=${encodeURIComponent(`Nouveau projet, ${name}`)}&body=${encodeURIComponent(body)}`
      setStatus('mail')
      return
    }

    setStatus('sending')
    try {
      const res = await fetch(ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
        body: JSON.stringify({ name, email, service, message }),
      })
      if (!res.ok) throw new Error(String(res.status))
      form.reset()
      setStatus('sent')
    } catch {
      setStatus('error')
    }
  }

  const field =
    'w-full border-b border-line bg-transparent py-3 text-[17px] outline-none transition-colors placeholder:text-muted-foreground focus:border-foreground focus-visible:outline-none'
  const label = 'text-[14px] font-medium'

  const message: Record<Status, string> = {
    idle: ENDPOINT ? '' : `Le message s’ouvre dans votre messagerie, prêt à être envoyé à ${EMAIL}.`,
    sending: 'Envoi en cours…',
    sent: 'Message envoyé. Nous revenons vers vous très vite.',
    mail: `Votre messagerie s’est ouverte. Si rien ne s’affiche, écrivez-nous à ${EMAIL}.`,
    error: `L’envoi n’a pas abouti. Réessayez, ou écrivez-nous directement à ${EMAIL}.`,
  }

  return (
    <form onSubmit={onSubmit} noValidate className="grid grid-cols-1 gap-7 sm:grid-cols-2">
      <div>
        <label htmlFor="name" className={label}>Nom</label>
        <input id="name" name="name" autoComplete="name" required aria-invalid={!!errors.name} aria-describedby={errors.name ? 'err-name' : undefined} className={field} placeholder="Votre nom" />
        {errors.name && <p id="err-name" className="mt-2 text-[14px] font-semibold text-danger">{errors.name}</p>}
      </div>
      <div>
        <label htmlFor="email" className={label}>E-mail</label>
        <input id="email" name="email" type="email" autoComplete="email" required aria-invalid={!!errors.email} aria-describedby={errors.email ? 'err-email' : undefined} className={field} placeholder="vous@exemple.com" />
        {errors.email && <p id="err-email" className="mt-2 text-[14px] font-semibold text-danger">{errors.email}</p>}
      </div>
      <div className="sm:col-span-2">
        <label htmlFor="service" className={label}>Besoin</label>
        <select id="service" name="service" className={`${field} cursor-pointer appearance-none`} defaultValue={SERVICES[0]}>
          {SERVICES.map((s) => (
            <option key={s} className="bg-background text-foreground">{s}</option>
          ))}
        </select>
      </div>
      <div className="sm:col-span-2">
        <label htmlFor="message" className={label}>Votre projet</label>
        <textarea id="message" name="message" rows={4} required aria-invalid={!!errors.message} aria-describedby={errors.message ? 'err-message' : undefined} className={`${field} resize-y`} placeholder="Contexte, objectifs, délais" />
        {errors.message && <p id="err-message" className="mt-2 text-[14px] font-semibold text-danger">{errors.message}</p>}
      </div>
      <input name="website" tabIndex={-1} autoComplete="off" aria-hidden className="absolute left-[-9999px] h-0 w-0 opacity-0" />
      <div className="flex flex-col gap-4 sm:col-span-2 sm:flex-row sm:items-center sm:justify-between">
        <button
          type="submit"
          disabled={status === 'sending'}
          className="group inline-flex min-h-12 items-center gap-3 self-start rounded-full bg-foreground px-7 text-[15px] font-semibold text-background transition-[transform,opacity] duration-500 hover:scale-[1.03] disabled:cursor-wait disabled:opacity-60"
        >
          {status === 'sending' ? 'Envoi…' : ENDPOINT ? 'Envoyer le message' : 'Préparer l’e-mail'}
          <ArrowIcon className="size-4 transition-transform duration-500 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
        </button>
        <p role="status" className="max-w-sm text-[14px] leading-snug text-muted-foreground">
          {fr(message[status])}
        </p>
      </div>
    </form>
  )
}
