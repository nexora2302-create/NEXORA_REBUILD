// Projets réels du studio (motion design et sites web). Images tirées des vidéos livrées et des sites.
// Ne jamais ajouter de projet, de client ou de chiffre inventé.
export type Discipline = 'motion' | 'web'

export type Project = {
  slug: string
  title: string
  client: string
  discipline: Discipline
  tag: string
  year: string
  img: string
  width: number
  height: number
  blur: string
  alt: string
  idea: string
  done: string[]
  pos?: string
  // Projet pas encore livré (maquette, développement en cours).
  status?: string
}

export const DISCIPLINES: { id: Discipline; label: string }[] = [
  { id: 'motion', label: 'Motion design' },
  { id: 'web', label: 'Sites web' },
]

export const PROJECTS: Project[] = [
  {"slug": "sin-nunu", "title": "SIN NUNU", "client": "SIN NUNU, Abomey-Calavi", "discipline": "motion", "tag": "Film de marque", "year": "2026", "alt": "Image du film SIN NUNU : deux mains se passent une bouteille d’eau sur fond bleu, titre « elle est là »", "idea": "Le film de marque d’une eau minérale béninoise : l’ambition, les trois formats et la promesse, « L’eau de qualité pour tous », entre animation et photographies du produit.", "done": ["Film 16:9, 1 min 20", "Photos produit animées", "Musique"], "img": "/work/sin-nunu.webp", "width": 1600, "height": 900, "blur": "data:image/webp;base64,UklGRo4AAABXRUJQVlA4IIIAAAAwBACdASoYAA4APu1iqU2ppaOiMAgBMB2JbACdMoRwN5AAQSzx39Hv4AAA99yst+M0LiL2zhUISAe7U5HbdzWh2DkkXY0fglsfvAO8xBhSSAZkTGL/jQRSkO7aGVEXwLg7RQRcPwGQ+YbGw/s1jf/1FNx+QQ/8LT//0m31GNd/ydAA"},
  {"slug": "inf", "title": "Institut National de la Femme", "client": "Institut National de la Femme (INF), Bénin", "discipline": "motion", "tag": "Film de présentation", "year": "2026", "alt": "Image du film de l’INF : un téléphone affiche le numéro 114, texte « Quelqu’un l’écoute, sans la juger »", "idea": "Un film d’animation pour faire connaître l’accompagnement des femmes victimes de violences : le numéro 114, l’écoute, l’orientation et la défense en justice.", "done": ["Film 16:9, 1 min 43", "Voix off", "Sous-titres"], "img": "/work/inf.webp", "width": 1600, "height": 900, "blur": "data:image/webp;base64,UklGRmIAAABXRUJQVlA4IFYAAAAQBACdASoYAA4APu1iqU2ppaOiMAgBMB2JQBOmUI7gBEEZwJXm4hnHMAD+7qGahijjdvJJwFiVNWfZpsbGkNHtVsaWbn7JfA/mNZaWVdLR8B7mJEAAAA=="},
  {"slug": "cnsr", "title": "Le nouveau Code de la route", "client": "Centre National de Sécurité Routière (CNSR), Bénin", "discipline": "motion", "tag": "Vidéo pour les réseaux", "year": "2026", "alt": "Image verticale de la vidéo du CNSR : « 3 morts par jour sur nos routes »", "idea": "Une vidéo verticale pour les réseaux sociaux : cinq règles à retenir, de vraies photos de nos routes, des pictogrammes animés et des sous-titres mot à mot.", "done": ["Vidéo 9:16, 1 min 08", "Photos réelles", "Sous-titres mot à mot"], "img": "/work/cnsr.webp", "width": 720, "height": 1280, "blur": "data:image/webp;base64,UklGRnAAAABXRUJQVlA4IGQAAADwAwCdASoNABgAPu1kqU2ppaQiMAgBMB2JZQCsACHe28mu/2d1wM5AAP7wz87koUv0gRyLeFmjRmvidkGnICSpQB2chhUI/nLjqYGJcWJdsSRsYyxqpQmkvfXaDtRvrA0gAAAA", "pos": "50% 35%"},
  {"slug": "mara-academy", "title": "Mara Academy", "client": "Mara Academy", "discipline": "motion", "tag": "Vidéo de présentation", "year": "2026", "alt": "Image de la vidéo Mara Academy : « Un diplôme, c’est important », trois cartes de compétences", "idea": "La vidéo de présentation d’une académie de formation et de ses deux programmes, YEA et SHIFT, écrite d’après le script du client : une histoire d’abord, puis l’offre.", "done": ["Film 16:9, 1 min 59", "Voix off", "Sous-titres"], "img": "/work/mara.webp", "width": 1600, "height": 900, "blur": "data:image/webp;base64,UklGRnIAAABXRUJQVlA4IGYAAACwAwCdASoYAA4APu1iqk2ppaQiMAgBMB2JZQAAW91Mq3eYncSIAAD+7dezCdwRYw7YmSbYMDD3/qhGKoH1kZMyMwNQBtjz0+STiKp5wZoNHu/Na5zq5Be5ZHs/lWd+yL2V5XqUUAA="},
  {"slug": "bluestone-connect", "title": "Blue’Ston Connect", "client": "Blue’Ston Connect, Bénin", "discipline": "motion", "tag": "Film de lancement", "year": "2026", "alt": "Image du film Blue’Ston Connect : une carte de visite intelligente bleue, titre « La carte de visite intelligente »", "idea": "Le film de lancement d’une carte de visite intelligente (NFC et QR code) : le problème, le geste, les fonctions, les offres. Une version horizontale et une version courte verticale.", "done": ["Film 16:9 et version 9:16", "Voix off", "Musique"], "img": "/work/blueston.webp", "width": 953, "height": 536, "blur": "data:image/webp;base64,UklGRmAAAABXRUJQVlA4IFQAAABQAwCdASoYAA4APu1iqU2ppaQiMAgBMB2JYgCdAC0H4+7+AAD+715OvRi7qDv/KNztOxoh5W7V0OxhFzHAf7lX2kPrTSTngN82+OVwiMaQFzcgAAA="},
  {"slug": "nexora", "title": "NEXORA", "client": "Notre propre site", "discipline": "web", "tag": "Site web", "year": "2026", "alt": "Page d’accueil du site NEXORA : grand logotype et sculpture 3D d’un X en verre", "idea": "Notre site de studio : une sculpture 3D animée en temps réel à l’ouverture, des sections qui réagissent au défilement, une version mobile pensée à part.", "done": ["Next.js et three.js", "Mobile et bureau", "Performance soignée"], "img": "/work/nexora-site.webp", "width": 1600, "height": 900, "blur": "data:image/webp;base64,UklGRnwAAABXRUJQVlA4IHAAAABwAwCdASoYAA4APu1iqk2ppaQiMAgBMB2JZwC7ACFnsxSE2QAA/vDL9MrnGLyrUPMwQTnZ3n2qivfu01Q5FarraSXXhor+67yniObmQ+RmoZiH2pD9m7txnSnzWV2wr7kv69P60Z/UY6pk4dCf6AAA"},
  {"slug": "agis-concept", "title": "AGIS Concept", "client": "AGIS Concept, Cotonou et Parakou", "discipline": "web", "tag": "Site web, en cours", "year": "2026", "alt": "Maquette du site AGIS Concept : un bâtiment en 3D sur fond lilas, titre « Vous avez un projet ? Nous avons votre solution »", "idea": "Direction artistique et maquette interactive du site d’un bureau d’études (architecture, urbanisme, ingénierie) : un bâtiment en 3D à l’ouverture, des expertises claires et une demande de devis toujours à portée de main.", "done": ["Direction artistique", "Maquette interactive", "3D en temps réel"], "img": "/work/agis.webp", "width": 1360, "height": 940, "blur": "data:image/webp;base64,UklGRlgAAABXRUJQVlA4IEwAAACwAwCdASoYABEAPuVgpE2pJaMiMAwBIByJQBhuBDhaL7EpwQAgKAD9yygzGqrp8+pEE5hZHrQ09ms8zzOE3T91Xdn1nxFYpXbfAAAA", "status": "En cours"},
]
