// Typographie française : espace fine insécable avant ? ! : ; (évite la ponctuation orpheline).
export const fr = (s: string) => s.replace(/ ([?!:;])/g, ' $1')
