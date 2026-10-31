'use client'

import { useEffect, useState } from 'react'

const format = () =>
  new Intl.DateTimeFormat('fr-FR', {
    hour: '2-digit',
    minute: '2-digit',
    timeZone: 'Africa/Porto-Novo',
  }).format(new Date())

export function LocalTime() {
  const [time, setTime] = useState<string | null>(null)

  useEffect(() => {
    setTime(format())
    const id = setInterval(() => setTime(format()), 20000)
    return () => clearInterval(id)
  }, [])

  return <span suppressHydrationWarning>{time ?? '--:--'}</span>
}
