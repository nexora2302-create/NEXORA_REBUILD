"""Catalogue NEXORA 2026 (motion design et sites web). Génère catalogue.html, puis le PDF avec pdf.js.
Sources des faits : présentation NEXORA du 17/11/2026 (Drive), fiches clients du dépôt motion-design-brain,
politique tarifaire 1.0 (prix recommandés motion et web). Aucun client, chiffre ni projet inventé."""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '07-REBRANDING', 'v4', 'sources'))
from typo import fr_typo

IMG = '../img'
X = '<span class="x">X</span>'
def nx(cls='nx'): return f'<span class="{cls}">NE{X}ORA</span>'
def head(n, label, dark=True):
    return f'<header class="ph"><span class="lg">{nx("nx small")}</span><span class="mono">{label}</span><span class="mono pn">{n:02d} / 15</span></header>'

def case(n, kicker, title, client, what, facts, imgs, layout='a', theme='dark'):
    f = ''.join(f'<div><span class="mono">{k}</span><b>{v}</b></div>' for k, v in facts)
    if layout == 'v':   # vertical (9:16)
        pics = '<div class="vrow">' + ''.join(f'<img src="{IMG}/{i}.jpg" alt="">' for i in imgs) + '</div>'
    else:
        big, *small = imgs
        pics = f'<div class="grid-{layout}"><img class="big" src="{IMG}/{big}.jpg" alt="">' + ''.join(f'<img src="{IMG}/{i}.jpg" alt="">' for i in small) + '</div>'
    return f'''<section class="pg {theme} case {layout}">{head(n, kicker)}
<div class="ct"><p class="mono kick">{client}</p><h2>{title}</h2><p class="what">{what}</p><div class="facts">{f}</div></div>
{pics}</section>'''

MOTION = [
 ('Visuel publicitaire animé', '6 à 15 s. Animation d’un visuel existant, musique libre de droits.', '3 jours', '40 000'),
 ('Animation de logo', '5 à 8 s en 2D, versions fond clair et fond sombre, effet sonore.', '4 à 5 jours', '60 000'),
 ('Déclinaison de format', 'Adaptation verticale, carrée ou horizontale d’une vidéo validée.', '2 jours', '25 000'),
 ('Présentation animée', '10 à 15 slides animées, en PowerPoint, Keynote ou vidéo.', '5 à 7 jours', '120 000'),
 ('Habillage vidéo', 'Intro, outro, deux bandeaux de titre et des transitions, réutilisables.', '7 jours', '130 000'),
 ('Vidéo pour les réseaux', '15 à 30 s. Motion typographique et graphique sur votre script.', '7 à 10 jours', '150 000'),
 ('Vidéo promotionnelle', '30 à 60 s. Script, storyboard validé, éléments graphiques, musique.', '12 à 15 jours', '300 000'),
 ('Vidéo explicative illustrée', '60 à 90 s. Script, storyboard, illustrations sur mesure, voix off.', '3 à 5 semaines', 'dès 600 000'),
]
WEB = [
 ('Landing page', 'Une page en 5 à 7 sections, maquette sur mesure, formulaire, WhatsApp et carte, référencement de base.', '2 à 3 semaines', '250 000'),
 ('Site vitrine', 'Jusqu’à 5 pages, maquette sur mesure, formulaire, WhatsApp et carte, référencement de base, 1 h de formation, 30 jours de suivi.', '3 à 5 semaines', '450 000'),
 ('Site institutionnel', '6 à 12 pages, actualités ou blog, administration par vos équipes, performance optimisée, 2 h de formation, 2 mois de suivi.', '6 à 8 semaines', 'dès 900 000'),
 ('Sur mesure', 'Catalogue, réservation, paiement : sur cahier des charges.', '8 à 12 semaines', 'dès 1 200 000'),
]
OPTIONS = [('Page supplémentaire', '40 000'), ('Actualités ou blog', '80 000'), ('Version bilingue (traduction fournie)', '+ 35 %'), ('Catalogue jusqu’à 30 fiches', '150 000'), ('Fiche Google Business Profile', '25 000'), ('Domaine et hébergement, à votre nom', 'coût réel + 15 000 / an'), ('Paiement Mobile Money', 'sur devis')]
MAINT = [('Sérénité', 'Mises à jour, sauvegarde mensuelle, surveillance, 1 h de modifications, intervention sous 72 h.', '20 000 / mois'), ('Évolution', 'Sauvegarde hebdomadaire, 3 h de modifications, rapport mensuel, intervention sous 48 h.', '45 000 / mois')]

def rows(items):
    return ''.join(f'<li><div><b>{a}</b><span>{b}</span></div><span class="mono dl">{c}</span><span class="pr">{d}</span></li>' for a, b, c, d in items)

FLORE = ['Le consentement', 'Le harcèlement sexuel', 'Les survivantes', 'Trois gestes', 'Impliquer les hommes', 'Les 16 jours d’activisme']

HTML = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>NEXORA, catalogue 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="catalogue.css"></head><body>

<section class="pg dark cover">
<header class="ph"><span class="mono">Studio créatif · Cotonou, Bénin</span><span class="mono">Catalogue 2026</span><span class="mono">Motion design · Sites web</span></header>
<div class="cv-strip">{''.join(f'<figure><img src="{IMG}/{i}.jpg" alt=""><figcaption class="mono">{c}</figcaption></figure>' for i, c in [('inf-presentation-02', 'Institut National de la Femme'), ('sin-nunu-09', 'SIN NUNU'), ('mara-presentation-00', 'Mara Academy'), ('blueston-intelligente', 'Blue’Ston Connect')])}</div>
<h1 class="cv-word">{nx("nx huge")}</h1>
<p class="cv-lead serif">Nous faisons bouger les marques.</p>
</section>

<section class="pg light studio">{head(2, 'Le studio')}
<h2 class="big">Né à Cotonou,<br>pensé pour le monde.</h2>
<div class="cols">
<p class="lead">NEXORA est un studio créatif basé à Cotonou. Nous concevons des vidéos en motion design et des sites web pour les institutions, les entreprises et les marques qui doivent être comprises vite, et retenues longtemps.</p>
<ul class="prin">
<li><b>Une idée d’abord.</b><span>Chaque projet part d’une idée tirée de votre marque, jamais d’une tendance du moment.</span></li>
<li><b>Un seul interlocuteur.</b><span>Du script à la mise en ligne, la même équipe porte votre projet.</span></li>
<li><b>D’ici, pour partout.</b><span>Institutions, entreprises et créateurs, au Bénin et à l’international.</span></li></ul></div>
<div class="duo"><div><span class="mono">01</span><b>Motion design</b><span>Vidéos de présentation, vidéos pour les réseaux, animation de logo, habillage vidéo.</span></div><div><span class="mono">02</span><b>Sites web</b><span>Landing pages, sites vitrines et sites institutionnels, mis en ligne et suivis.</span></div></div>
</section>

<section class="pg dark refs">{head(3, 'Motion design')}
<h2 class="big">Ils nous ont<br>fait <em class="serif">confiance.</em></h2>
<ul class="names">
<li><b>Institut National de la Femme</b><span>Vidéo de présentation</span></li>
<li><b>Mara Academy</b><span>Vidéo de présentation</span></li>
<li><b>CNSR</b><span>Le nouveau Code de la route</span></li>
<li><b>SIN NUNU</b><span>Vidéo de marque</span></li>
<li><b>Blue’Ston Connect</b><span>Vidéo de lancement</span></li>
<li><b>Flore Djinou</b><span>Série vidéo</span></li>
<li><b>Aurélia</b><span>Vidéos produit</span></li></ul>
<p class="mono note">Réalisations 2026. Les pages suivantes montrent des images tirées des vidéos livrées.</p>
</section>

{case(4, 'Motion design · Institution', 'Écouter, accompagner, défendre.', 'Institut National de la Femme (INF) · Bénin · 2026',
  'Une vidéo d’animation pour faire connaître l’accompagnement des femmes victimes de violences : le numéro 114, l’écoute, l’orientation et la défense en justice.',
  [('Format', '16:9'), ('Durée', '1 min 43'), ('Avec', 'voix off, sous-titres')],
  ['inf-presentation-02', 'inf-presentation-03', 'inf-presentation-05', 'inf-presentation-10'])}

{case(5, 'Motion design · Formation', 'Construire les compétences de demain.', 'Mara Academy · 2026',
  'La vidéo de présentation d’une académie de formation et de ses deux programmes, YEA et SHIFT, écrite d’après le script du client : une histoire d’abord, puis l’offre.',
  [('Format', '16:9'), ('Durée', '1 min 59'), ('Avec', 'voix off, sous-titres')],
  ['mara-presentation-04', 'mara-presentation-00', 'mara-presentation-07', 'mara-presentation-11'])}

{case(6, 'Motion design · Institution', 'Le nouveau Code de la route.', 'Centre National de Sécurité Routière (CNSR) · Bénin · 2026',
  'Une vidéo verticale pour les réseaux sociaux : cinq règles à retenir, de vraies photos de nos routes, des pictogrammes animés et des sous-titres mot à mot.',
  [('Format', '9:16'), ('Durée', '1 min 08'), ('Avec', 'voix off, photos réelles')],
  ['cnsr-code-route-00', 'cnsr-code-route-01', 'cnsr-code-route-03', 'cnsr-code-route-04', 'cnsr-code-route-09'], 'v')}

{case(7, 'Motion design · Marque', 'L’eau de qualité pour tous.', 'SIN NUNU · Abomey-Calavi · 2026',
  'La vidéo de marque d’une eau minérale béninoise : l’ambition, les trois formats et la promesse, entre animation et photographies du produit.',
  [('Format', '16:9'), ('Durée', '1 min 20'), ('Avec', 'photos produit, musique')],
  ['sin-nunu-09', 'sin-nunu-00', 'sin-nunu-02', 'sin-nunu-07', 'sin-nunu-11'], 'c', 'light')}

{case(8, 'Motion design · Produit', 'La carte de visite, ici et maintenant.', 'Blue’Ston Connect · Bénin · 2026',
  'La vidéo de lancement d’une carte de visite intelligente (NFC et QR code) : le problème, le geste, les fonctions, les offres. Une version horizontale et une version courte verticale.',
  [('Formats', '16:9 et 9:16'), ('Écrans', '9 scènes'), ('Avec', 'voix off, musique')],
  ['blueston-intelligente', 'blueston-perd', 'blueston-seconde', 'blueston-appeler', 'blueston-fin'], 'c')}

<section class="pg flore">{head(9, 'Motion design · Série')}
<div class="ct"><p class="mono kick">Flore Djinou · 2026</p><h2>Une parole, une vidéo par thème.</h2>
<p class="what">Une série de vidéos verticales pour les réseaux sociaux, à l’occasion des 16 jours d’activisme contre les violences faites aux femmes et aux filles : prise de parole face caméra, habillage animé aux couleurs de sa marque, sous-titres mot à mot.</p>
<div class="facts"><div><span class="mono">Format</span><b>9:16</b></div><div><span class="mono">Série</span><b>{len(FLORE)} vidéos</b></div><div><span class="mono">Avec</span><b>tournage, montage, motion</b></div></div></div>
<ol class="flist">{''.join(f'<li><span class="mono">{i+1:02d}</span><b>{t}</b></li>' for i, t in enumerate(FLORE))}</ol>
</section>

<section class="pg light webcase">{head(10, 'Sites web')}
<div class="ct"><p class="mono kick">NEXORA · Notre propre site · 2026</p><h2>Un site qui bouge, et qui reste rapide.</h2>
<p class="what">Notre site de studio : une sculpture 3D animée en temps réel à l’ouverture, des sections qui réagissent au défilement, une version mobile pensée à part. Conçu et développé par l’équipe.</p>
<div class="facts"><div><span class="mono">Technologie</span><b>Next.js, three.js</b></div><div><span class="mono">Écrans</span><b>mobile et bureau</b></div><div><span class="mono">En ligne</span><b>nexoraa-nu.vercel.app</b></div></div></div>
<div class="screens"><div class="browser"><i></i><img src="{IMG}/web-nexora-1.jpg" alt=""></div><div class="browser b2"><i></i><img src="{IMG}/web-nexora-2.jpg" alt=""></div><div class="phone"><img src="{IMG}/web-nexora-mob.jpg" alt=""></div></div>
</section>

<section class="pg dark webcase agis">{head(11, 'Sites web')}
<div class="ct"><p class="mono kick">AGIS Concept · Cotonou et Parakou · en cours</p><h2>Un bureau d’études, raconté en volume.</h2>
<p class="what">Direction artistique et maquette interactive du site d’un bureau d’études (architecture, urbanisme, ingénierie) : un bâtiment en 3D à l’ouverture, des expertises claires et une demande de devis toujours à portée de main.</p>
<div class="facts"><div><span class="mono">Étape</span><b>maquette interactive</b></div><div><span class="mono">Écrans</span><b>bureau et mobile</b></div><div><span class="mono">Avec</span><b>3D en temps réel</b></div></div></div>
<div class="screens one"><div class="browser"><i></i><img src="{IMG}/web-agis-1.jpg" alt=""></div></div>
</section>

<section class="pg light price">{head(12, 'Tarifs · Motion design')}
<div class="prh"><h2>Motion design</h2><p>Le prix suit le travail, pas la durée : écriture, storyboard, illustrations, complexité de l’animation, son et formats. Deux séries de retours incluses, trois pour la vidéo promotionnelle et la vidéo explicative.</p></div>
<ul class="plist"><li class="hd"><span class="mono">Prestation</span><span class="mono">Délai, jours ouvrés</span><span class="mono">FCFA</span></li>{rows(MOTION)}</ul>
<p class="mono foot">Prix en FCFA, hors TVA éventuelle. Voix off au coût réel. Au-delà de 90 s, le devis s’ajuste à la durée et aux illustrations.</p>
</section>

<section class="pg light price">{head(13, 'Tarifs · Sites web')}
<div class="prh"><h2>Sites web</h2><p>Maquette sur mesure, adaptée au mobile, mise en ligne et suivie. Deux séries de retours sur la maquette et une sur l’intégration.</p></div>
<ul class="plist web"><li class="hd"><span class="mono">Formule</span><span class="mono">Délai</span><span class="mono">FCFA</span></li>{rows(WEB)}</ul>
<div class="two"><div><h3>Options</h3><ul class="opts">{''.join(f'<li><span>{a}</span><b>{b}</b></li>' for a, b in OPTIONS)}</ul></div>
<div><h3>Maintenance</h3><ul class="opts m">{''.join(f'<li><span><b>{a}</b> {b}</span><b>{c}</b></li>' for a, b, c in MAINT)}</ul><p class="mono foot2">Engagement de six mois. Paiement annuel : dix mois facturés.</p></div></div>
</section>

<section class="pg dark method">{head(14, 'Méthode et conditions')}
<h2 class="big">Comment<br>nous travaillons.</h2>
<ol class="steps">
<li><span class="mono">01</span><b>Échange</b><span>Nous écoutons votre besoin, vos objectifs et votre public.</span></li>
<li><span class="mono">02</span><b>Proposition</b><span>Nous présentons une direction et une offre claires.</span></li>
<li><span class="mono">03</span><b>Création</b><span>Nous concevons, vous validez chaque étape : script, storyboard ou maquette.</span></li>
<li><span class="mono">04</span><b>Livraison</b><span>Vous recevez des fichiers prêts à l’emploi, ou un site en ligne.</span></li></ol>
<ul class="conds">
<li><b>50 %</b><span>d’acompte à la commande. Au-delà de 500 000 : 40 / 30 / 30.</span></li>
<li><b>2</b><span>séries de retours incluses. Une série, c’est une liste de corrections regroupée.</span></li>
<li><b>30 jours</b><span>de garantie : nos erreurs corrigées gratuitement.</span></li>
<li><b>Au solde</b><span>remise des fichiers finaux et cession des droits d’utilisation.</span></li>
<li><b>+30 %</b><span>pour une urgence (délai divisé par deux), selon nos disponibilités.</span></li></ul>
</section>

<section class="pg ember contact">
<header class="ph"><span class="lg">{nx("nx small")}</span><span class="mono">Contact</span><span class="mono pn">15 / 15</span></header>
<h2 class="cbig">Un projet ?<br><em class="serif">Mettons-le en mouvement.</em></h2>
<div class="clist"><div><span class="mono">WhatsApp</span><b>+229 01 51 33 74 15</b></div><div><span class="mono">Site</span><b>nexoraa-nu.vercel.app</b></div><div><span class="mono">Studio</span><b>Cotonou, Bénin</b></div></div>
<h1 class="cv-word end">{nx("nx huge")}</h1>
</section>
</body></html>'''
open(os.path.join(HERE, 'catalogue.html'), 'w').write(fr_typo(HTML))
print('ok')
