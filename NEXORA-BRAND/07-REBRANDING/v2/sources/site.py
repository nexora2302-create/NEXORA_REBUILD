import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from marks import wordmark, svg, symbol
from typo import fr_typo
X, N, F = '#22E1FF', '#0B0C0E', '#F3F5F2'
CSS = open(os.path.join(HERE, 'common.css')).read() + open(os.path.join(HERE, 'site.css')).read()
JS = open(os.path.join(HERE, 'site.js')).read()

def wm(fg='currentColor', cls='wm', label='Strobe'):
    i, W, H = wordmark(100, fg); return svg(i, W, H, cls, label, pad=110)
def sym(fg='currentColor', cls='sy', label='Symbole Strobe'):
    return f'<svg class="{cls}" viewBox="0 0 100 100" role="img" aria-label="{label}">{symbol(fg)}</svg>'

def stage(pid, fg=F):
    """Logotype en trois bandes animables + copie rémanente (xénon)."""
    i, W, H = wordmark(100, fg); d = re.search(r'd="([^"]+)"', i).group(1)
    pad = 260; h = H / 3
    clips = ''.join(f'<clipPath id="{pid}c{k}"><rect x="{-pad*2}" y="{k*h:.1f}" width="{W+pad*4:.0f}" height="{h+.6:.1f}"/></clipPath>' for k in range(3))
    bands = ''.join(f'<g clip-path="url(#{pid}c{k})"><g class="bd b{k}"><path fill="{fg}" d="{d}"/></g></g>' for k in range(3))
    return (f'<svg class="stg" viewBox="{-pad} 0 {W+2*pad:.0f} {H:.0f}" role="img" aria-label="Strobe"><defs>{clips}</defs>'
            f'<g class="ghost"><path fill="{X}" d="{d}"/></g>{bands}</svg>')

def t(fr, en, tag='span', cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<{tag}{c} lang="fr">{fr}</{tag}><{tag}{c} lang="en">{en}</{tag}>'

# Construction du symbole
r = 34; off = .17 * 2 * r
construct = f'''<svg class="cons" viewBox="-6 4 112 92" role="img" aria-label="Construction du symbole">
<circle cx="{50-off:.2f}" cy="50" r="{r}" fill="none" stroke="var(--mut)" stroke-width=".35" stroke-dasharray="1.2 1.2"/>
<circle cx="{50+off:.2f}" cy="50" r="{r}" fill="none" stroke="var(--mut)" stroke-width=".35" stroke-dasharray="1.2 1.2"/>
<g opacity=".9">{symbol('var(--fg)', d=.17)}</g>
<line x1="-2" y1="50" x2="102" y2="50" stroke="{X}" stroke-width=".5"/>
<circle cx="{50-off:.2f}" cy="50" r="1.1" fill="{X}"/><circle cx="{50+off:.2f}" cy="50" r="1.1" fill="{X}"/>
<g class="cl"><text x="-4" y="10">r 34 · carré de 100</text><text x="40" y="95">chaque moitié glisse de 17 % du diamètre</text></g></svg>'''

PAL = [
 ('Noir salle', '#0B0C0E', F, '55 %', 'La salle avant que la lumière arrive. Fond principal, scène, vidéo.', 'Blanc flash dessus : 17,9:1'),
 ('Blanc flash', '#F3F5F2', N, '35 %', 'Un blanc légèrement froid, comme la lumière d’un tube au xénon. Fond clair, texte sur noir.', 'Noir salle dessus : 17,9:1'),
 ('Xénon', '#22E1FF', N, '7 %', 'Le flash et la rémanence. Action, signature, moment fort. Jamais en texte sur blanc.', 'Sur noir : 12,4:1 · sur blanc : 1,4:1'),
 ('Xénon profond', '#006F84', F, 'texte', 'Le xénon pour les textes et liens en mode clair.', 'Sur blanc flash : 5,3:1'),
 ('Câble', '#8A9196', N, '3 %', 'Texte secondaire et filets sur noir. En mode clair : #596066.', 'Sur noir : 6,1:1 · #596066 sur blanc : 5,8:1'),
]
pal = ''.join(f'<div class="pc" style="background:{h};color:{c}"><b>{n}</b><code>{h}</code><span class="pp">{p}</span><span>{d}</span><span class="ct">{ct}</span></div>' for n, h, c, p, d, ct in PAL)

MOT = [
 ('1 · Dérive', 'en continu', 'ease-in-out, 7 à 11 s', 'Le mot glisse en trois bandes : l’objet bouge, la lumière est continue.'),
 ('2 · Charge', '0 → 600 ms avec le son, 0 → 140 ms sans', 'cubic-bezier(.7, 0, .84, 0)', 'Les bandes accélèrent. Le sifflement de charge monte.'),
 ('3 · Flash', 'à 600 ms, une image', 'coupe franche', 'Les bandes se calent net. Un seul flash blanc à 92 %, qui retombe en 260 ms.'),
 ('4 · Rémanence', '600 → 1 500 ms', 'cubic-bezier(.16, 1, .3, 1)', 'Une copie xénon décalée s’efface derrière le mot. C’est l’image qui reste.'),
]
mot = ''.join(f'<tr><th scope="row">{a}</th><td class="n">{b}</td><td><code>{c}</code></td><td>{d}</td></tr>' for a, b, c, d in MOT)

STRIPS = [
 ('1', 'Communication visuelle et audiovisuel', 'Visual communication and AV', 'Pas de deuxième prise.', 'No second takes.', 'Affiches, édition, photo · Captation, son, projection · Location de matériel', 'Posters, print, photography · Filming, sound, projection · Equipment rental', 72),
 ('2', 'Motion design', 'Motion design', 'Chaque image frappe.', 'Every frame hits.', 'Génériques, logos animés, contenus pour les réseaux, habillage des écrans d’événement', 'Title sequences, animated logos, social content, event screen graphics', 64),
 ('3', 'Sites web', 'Websites', 'Vite chargé, dur à oublier.', 'Loads fast. Lands hard.', 'Sites de marque, portfolios, pages de lancement, maintenance', 'Brand sites, portfolios, launch pages, maintenance', 58),
]
def strip(ch, fr, en, lfr, len_, sfr, sen, lvl, master=False):
    leds = ''.join(f'<i style="--k:{k}"></i>' for k in range(10))
    return f'''<li class="strip{' master' if master else ''}" data-ch="{ch}" style="--lvl:{lvl}">
<button type="button" aria-pressed="false"><span class="chn mono">{'MASTER' if master else 'CH ' + ch}</span>
<span class="chname">{t(fr, en)}</span></button>
<div class="meter" aria-hidden="true">{leds}</div>
<div class="fader" aria-hidden="true"><span class="slot"></span><span class="knob"></span></div>
<div class="chbody"><p class="chline">{t(lfr, len_)}</p><p class="small">{t(sfr, sen)}</p></div></li>'''
strips = ''.join(strip(*s) for s in STRIPS).replace('class="strip" data-ch="1"', 'class="strip on" data-ch="1"', 1) + strip('M', 'Brand design', 'Brand design', 'Ça marque.', 'Burned in.', 'Tout passe par le bus master : stratégie, nom, logo, règles. C’est lui qui fait sonner les trois canaux comme une seule marque.', 'Everything runs through the master bus: strategy, naming, logo, rules. It makes three channels sound like one brand.', 80, True)

FRAMES = [('12', 'Identité', 'Identity'), ('13', 'Motion', 'Motion'), ('14', 'Site web', 'Website'), ('15', 'Événement', 'Event'), ('16', 'Affiche', 'Poster'), ('17', 'Captation', 'Filming')]
frames = ''.join(f'<li class="fr{" mark" if k == 2 else ""}"><div class="frimg" aria-hidden="true"><span class="sy-w">{sym(N if k % 2 == 0 else F, "fs", "")}</span></div><p class="mono"><span>{n}</span><span>{n}A</span></p><p class="frl">{t("Exemple · " + a, "Example · " + b)}</p></li>' for k, (n, a, b) in enumerate(FRAMES))

STEPS = [('Écouter', 'Listen', 'Un échange pour comprendre la marque, le public, l’objectif.', 'One conversation to understand the brand, the audience, the goal.'),
         ('Concevoir', 'Design', 'Une direction claire, validée avec vous avant toute production.', 'One clear direction, signed off before production starts.'),
         ('Produire', 'Make', 'Identité, mouvement, interface, avec des points d’étape réguliers.', 'Identity, motion, interface, with regular check-ins.'),
         ('Livrer', 'Deliver', 'Fichiers prêts, site en ligne, suivi après le lancement.', 'Files ready, site live, support after launch.')]
steps = ''.join(f'<li><span class="tc mono">0{k+1}:00:00:00</span><h3 class="d2">{t(a, b)}</h3><p>{t(c, d)}</p></li>' for k, (a, b, c, d) in enumerate(STEPS))

HTML = f'''<title>Strobe, identité et site</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anybody:wdth,wght@50..150,100..900&family=Martian+Mono:wdth,wght@75..112.5,400..700&family=Schibsted+Grotesk:ital,wght@0,400..800;1,400&display=swap">
<style>{CSS}</style>
<header class="bar"><div class="wrap"><a class="lg" href="#identite" aria-label="Strobe, identité">{wm()}</a>
<nav class="sw" aria-label="Parties"><a href="#identite" data-v="identite">Brand book</a><a href="#site" data-v="site">Maquette du site</a></nav>
<button class="tg" type="button" id="themeBtn">Thème</button></div></header>
<main>
<!-- =================== BRAND BOOK =================== -->
<div class="view" id="v-identite">
<section class="night cover"><div class="wrap cvw">
<p class="eyebrow">Brand book v2 · condensé · 10 novembre 2026</p>
<div class="stage frozen" id="sigCover" data-rest="frozen">{stage('cv')}</div>
<div class="cvb"><p class="d3">Ça marque. <span class="x">Burned in.</span></p>
<div class="btns"><button class="btn" type="button" data-replay="#sigCover">Rejouer la signature</button><button class="btn ghostb" type="button" data-replay="#sigCover" data-sound>Avec le son</button></div></div>
</div></section>

<div class="wrap">
<section class="sec" id="idee"><header><p class="eyebrow">L’idée</p><h2 class="d1">Une marque a une seconde.</h2></header>
<div class="cols"><p class="lead">Un stroboscope, c’est une lumière qui fige le mouvement. Ce qui bouge devient net, l’espace d’un éclair, puis l’image reste sur la rétine. Strobe fait ça pour les marques : on conçoit l’image qui tient dans la seconde où on la voit, et qui reste après.</p>
<ul class="senses"><li><b>Photo.</b> En studio, le flash s’appelle un strobe.</li><li><b>Scène.</b> Le stroboscope est la lumière du direct.</li><li><b>Animation.</b> Des images fixes, montrées vite, deviennent un mouvement : c’est le principe même du motion.</li><li><b>Mémoire.</b> L’image rémanente, c’est le travail du brand design.</li></ul></div></section>

<section class="sec" id="logo"><header><p class="eyebrow">Logo</p><h2 class="d2">Le disque décalé.</h2><p class="small">Le même dessin sert de symbole, de O dans le logotype et de point de départ de l’animation.</p></header>
<div class="cols"><figure class="pane">{construct}<figcaption>Un disque coupé à l’horizontale ; la moitié haute glisse à gauche, la basse à droite, chacune de 17 % du diamètre. Deux images d’un même objet, figées par le flash, et le décalage dessine un S. Dans le logotype, le glissement passe à 12 % pour laisser respirer le R et le B.</figcaption></figure>
<div class="lv">
<div class="night lvi">{wm(F)}</div><div class="day lvi bd1">{wm(N)}</div>
<div class="night lvi sq">{sym(F)}</div><div class="day lvi sq bd1">{sym(N)}</div><div class="lvi sq xb">{sym(N)}</div>
<div class="rules"><h3 class="eyebrow">Règles</h3><ul><li><b>Zone de protection :</b> la hauteur d’une moitié de disque, tout autour.</li><li><b>Tailles minimales :</b> symbole 16 px ou 5 mm ; logotype 72 px ou 20 mm de large.</li><li><b>Interdits :</b> recaler les deux moitiés, les colorer différemment, tourner le symbole, l’entourer d’un cercle ou d’un carré arrondi.</li></ul></div>
</div></div></section>

<section class="sec" id="couleurs"><header><p class="eyebrow">Couleurs</p><h2 class="d2">Noir, blanc, un seul flash.</h2>
<p class="small">Avant : graphite, lin, cuivre et bleu, deux accents qui se disputaient la vedette. Après : un seul accent, et il a une raison d’exister. Pourquoi : un flash ne se partage pas.</p></header>
<div class="pal">{pal}</div>
<div class="prop" role="img" aria-label="Proportions : noir 55 %, blanc 35 %, xénon 7 %, câble 3 %"><i style="flex:55;background:#0B0C0E"></i><i style="flex:35;background:#F3F5F2"></i><i style="flex:7;background:#22E1FF"></i><i style="flex:3;background:#8A9196"></i></div>
<p class="small">Mode sombre par défaut à l’écran (la salle), mode clair pour les documents et le jour. Le xénon reste le même dans les deux ; en mode clair, il passe en aplat derrière du noir, jamais en texte.</p></section>

<section class="sec" id="typo"><header><p class="eyebrow">Typographie</p><h2 class="d2">Une fonte qui s’étire.</h2>
<p class="small">Avant : Big Shoulders et IBM Plex, la « tech premium » de 2020. Après : Anybody et Schibsted Grotesk. Pourquoi : Anybody va de 50 à 150 % de largeur sur un seul fichier, donc la typo peut bouger comme un objet sous le stroboscope ; Schibsted Grotesk est un texte de presse, net et chaleureux, peu vu dans les studios.</p></header>
<div class="tyw"><div class="tys"><p id="wdthSample" class="wsamp">Ça marque.</p>
<label class="rng" for="wdth"><span class="mono">Largeur <b id="wdthVal">100</b> %</span><input id="wdth" type="range" min="50" max="150" value="100"></label></div>
<div class="tyl"><div><p class="eyebrow">Titrage · Anybody 800 à 900</p><p class="tA">Chaque image frappe.</p></div>
<div><p class="eyebrow">Texte · Schibsted Grotesk 400 à 600</p><p class="tB">On conçoit l’image qui tient dans la seconde où on la voit, et qui reste après. Identité, motion, web : le même trait partout.</p></div>
<div><p class="eyebrow">Données · Martian Mono</p><p class="tC">TC 01:00:12:08 · 5600 K · −14 LUFS · 1/8000 s</p></div></div></div>
<p class="small">Règle cinétique : la largeur est réservée au mouvement (s’étirer, c’est aller vite). On n’anime jamais la couleur et la largeur en même temps.</p></section>

<section class="sec" id="motion"><header><p class="eyebrow">Motion</p><h2 class="d2">Le flash, en 900 ms.</h2><p class="small">Avant : un « allumage » sans séquence. Après : une signature codée, la même partout, de l’intro vidéo au bouton du site.</p></header>
<div class="tbl"><table><thead><tr><th>Phase</th><th>Temps</th><th>Courbe</th><th>Ce qui se passe</th></tr></thead><tbody>{mot}</tbody></table></div>
<ul class="mrules"><li>Un flash au maximum par séquence, jamais plus de trois par seconde (seuil WCAG 2.3.1), jamais de clignotement en boucle.</li><li>Mouvement réduit demandé : aucun flash, le logo apparaît calé.</li><li>Coupes franches plutôt que fondus. Les éléments entrent par bandes, jamais en rebond.</li></ul></section>

<section class="sec" id="son"><header><p class="eyebrow">Son</p><h2 class="d2">La signature sonore.</h2><p class="small">Le studio est né sur le terrain du son. Aucun studio de design ne signe au son : c’est la place à prendre.</p></header>
<div class="snd night"><div class="stage small-st" id="sigStage">{sym(F, 'sy sst')}</div>
<div class="sndr"><div class="btns"><button class="btn" type="button" data-play="full">Écouter · 1,5 s</button><button class="btn ghostb" type="button" data-play="short">Version courte · 0,4 s</button></div>
<div class="tl" aria-hidden="true"><span class="seg s1">Charge</span><span class="seg s2">Flash</span><span class="seg s3">Rémanence</span><i id="playhead"></i></div>
<p class="small">Prototype synthétisé dans la page (Web Audio), sans fichier.</p></div></div>
<div class="grid brief">
<article><h3 class="d3">1 · Charge</h3><p>0 à 0,6 s. Un sifflement qui monte de 1,4 à 5,2 kHz, très bas : le son du flash de studio qui se charge, reconnu par tous les photographes.</p></article>
<article><h3 class="d3">2 · Flash</h3><p>À 0,6 s. Un clac de bruit filtré autour de 2,6 kHz et un coup sourd de 140 à 42 Hz : la sono qu’on met sous tension.</p></article>
<article><h3 class="d3">3 · Rémanence</h3><p>0,6 à 1,5 s. Une quinte (la, mi, la) dont le filtre se ferme de 5 kHz à 500 Hz : l’image qui reste.</p></article>
<article><h3 class="d3">Usages</h3><p>Fin de chaque vidéo, ouverture d’événement, début de présentation, réseaux. Sur le site : coupé par défaut, jamais en lecture automatique. Version finale à produire et mixer par le studio : −14 LUFS, compatible mono.</p></article>
</div></section>

<section class="sec" id="ton"><header><p class="eyebrow">Images et ton</p><h2 class="d2">Net. Court. Vrai.</h2><p class="small">Gardé du v1 : la lumière de travail, le ton direct et technique sans jargon. Durci : règles plus précises et une liste « jamais ».</p></header>
<div class="grid tw">
<article><h3 class="d3">Images</h3><ul><li>Un flash, dur. Ombres nettes, le fond tombe au noir.</li><li>Le geste exact, figé net : la main sur le fader, le câble qu’on branche, l’écran qui s’allume.</li><li>Cadre serré, matières vraies : métal, câble, peau, papier.</li><li>Un accent xénon au maximum par image : une gélatine, un écran.</li><li>Les personnes en action, de dos ou de profil.</li></ul></article>
<article><h3 class="d3">Voix</h3><ul><li>Titres de deux à six mots. Un verbe par phrase.</li><li>« On » en français, « we » en anglais.</li><li>Des chiffres réels, ou aucun chiffre.</li><li>Ni point d’exclamation, ni superlatif.</li><li>Rien de tiède.</li></ul></article>
<article class="never"><h3 class="d3">Jamais</h3><ul><li>Banques d’images, poignées de main, sourires face caméra, drone sur la ville.</li><li>Wax, masques, cartes ou silhouettes du continent, globes, ampoules « idée ».</li><li>Flou de bougé décoratif, néons « good vibes », images générées présentées comme de vrais projets.</li><li>« Solutions », « innovant », « passion », « 360° », « élever », « créons ensemble ».</li></ul></article></div>
<div class="tbl"><table><thead><tr><th>Avant</th><th>Après</th></tr></thead><tbody>
<tr><td>Nous accompagnons les marques dans leur transformation digitale.</td><td><b>On rend votre marque visible en une seconde.</b></td></tr>
<tr><td>Une équipe passionnée à votre écoute.</td><td><b>Un brief, une réponse, une date.</b></td></tr>
<tr><td>Des solutions créatives sur-mesure.</td><td><b>Identité, motion, web. Le même trait partout.</b></td></tr></tbody></table></div></section>

<section class="sec" id="applications"><header><p class="eyebrow">Applications</p><h2 class="d2">Sur le terrain.</h2></header>
<div class="apps">
<figure><div class="night kak"><span class="kw">{wm(F)}</span><b class="kl">Ça<br>marque.</b><span class="ksym">{sym(X, 'sy')}</span></div><figcaption>Kakémono 80 × 200 cm, lisible à 20 m.</figcaption></figure>
<figure><div class="avs"><span class="av night">{sym(F)}</span><span class="av xb">{sym(N)}</span></div><figcaption>Avatars : noir par défaut, xénon pour les lancements.</figcaption></figure>
<figure><div class="night end"><span>{sym(F, 'sy')}</span><p class="mono">Burned in. · strobe.design</p></div><figcaption>Carte de fin vidéo 16:9, calée sur la signature sonore.</figcaption></figure>
<figure><div class="case"><span class="rv r1"></span><span class="rv r2"></span><span class="rv r3"></span><span class="rv r4"></span><p class="stn">STROBE</p><p class="stn s2">CH 1 · 2 · 3 · MASTER</p><p class="stn s3">FRAGILE · HAUT ↑</p></div><figcaption>Flight case, pochoir blanc : la marque voyage avec le matériel.</figcaption></figure>
</div></section>
</div></div>

<!-- =================== MAQUETTE DU SITE =================== -->
<div class="view site" id="v-site" data-lang="fr" lang="fr" hidden>
<div class="sbar night"><div class="wrap"><span class="slg">{wm(F)}</span>
<nav aria-label="Site"><a href="#s-poles">{t('Pôles', 'Practice')}</a><a href="#s-travaux">{t('Travaux', 'Work')}</a><a href="#s-methode">{t('Méthode', 'Process')}</a><a href="#s-contact">Contact</a></nav>
<button class="tg" type="button" id="langBtn">EN</button></div></div>

<section class="night hero" aria-label="Accueil"><div class="wrap hw">
<div class="stage hst" id="heroStage">{stage('hs')}</div>
<div class="hbot"><div class="manif d3">{t('Une marque a une seconde.<br>On en fait un flash.<br><span class="x">Celui qu’on voit encore les yeux fermés.</span>', 'A brand gets one second.<br>We make it a flash.<br><span class="x">The one you still see with your eyes shut.</span>')}</div>
<div class="hctl"><button class="btn fire" type="button" id="fireBtn">{t('Déclencher le flash', 'Fire the flash')}</button>
<button class="tg snd-b" type="button" id="soundBtn" aria-pressed="false"><span data-s="off">{t('Son coupé', 'Sound off')}</span><span data-s="on" hidden>{t('Son activé', 'Sound on')}</span></button>
<p class="mono hint">{t('ou touchez la scène', 'or tap the stage')} · 1/8000 s · 5600 K</p></div></div></div></section>

<section class="wrap s-thesis"><p class="kin" data-kin>{t('Une seconde.', 'One second.')}</p>
<p class="lead">{t('Sur un téléphone, dans une salle, sur un kakémono au bord de la route : une seconde. On conçoit chaque image pour cette seconde-là, et pour ce qui reste après.', 'On a phone, in a venue, on a banner by the road: one second. We design every image for that second, and for what stays after it.')}</p></section>

<section class="wrap s-poles" id="s-poles"><header class="sh"><p class="eyebrow">{t('Pôles', 'Practice')}</p><h2 class="d2">{t('Trois canaux.<br>Un bus master.', 'Three channels.<br>One master bus.')}</h2></header>
<ol class="console">{strips}</ol></section>

<section class="wrap s-work" id="s-travaux"><header class="sh"><p class="eyebrow">{t('Travaux', 'Work')}</p><h2 class="d2">{t('Planche contact.', 'Contact sheet.')}</h2>
<p class="small">{t('Emplacements d’exemple. Les vrais projets arrivent ici avec l’accord de publication des clients.', 'Example slots. Real projects go here once clients approve publication.')}</p></header>
<ol class="sheet">{frames}</ol></section>

<section class="wrap s-method" id="s-methode"><header class="sh"><p class="eyebrow">{t('Méthode', 'Process')}</p><h2 class="d2">{t('Quatre temps.', 'Four beats.')}</h2></header><ol class="steps">{steps}</ol></section>

<section class="night s-contact" id="s-contact"><div class="wrap cw">
<h2 class="mega">{t('On tourne ?', 'Ready to roll?')}</h2>
<form id="briefForm" class="form" novalidate>
<p class="lead">{t('Dites-nous ce que vous lancez, et pour quand.', 'Tell us what you’re launching, and when.')}</p>
<label for="f-name">{t('Nom', 'Name')}</label><input id="f-name" name="name" autocomplete="name" required value="">
<label for="f-mail">E-mail</label><input id="f-mail" name="email" type="email" autocomplete="email" required>
<label for="f-brief">{t('Le projet', 'The project')}</label><textarea id="f-brief" name="brief" rows="3" required></textarea>
<label for="f-when">{t('Échéance', 'Deadline')}</label><select id="f-when" name="when"><option data-fr="Moins d’un mois" data-en="Under a month">Moins d’un mois</option><option data-fr="Un à trois mois" data-en="One to three months">Un à trois mois</option><option data-fr="Plus tard" data-en="Later">Plus tard</option></select>
<button class="btn fire" type="submit">{t('Envoyer le brief', 'Send the brief')}</button>
<p id="formState" class="fstate" tabindex="-1" hidden>{t('Maquette : ce formulaire n’envoie rien. Sur le vrai site, le brief part au studio.', 'Mock-up: this form sends nothing. On the real site, the brief goes to the studio.')}</p>
</form></div>
<footer class="wrap foot"><div class="fwm">{wm(F)}</div>
<div class="fcols"><p>{t('Basés à Cotonou. Clients partout.', 'Based in Cotonou. Working everywhere.')}</p>
<p class="mono">strobe.design · {t('domaine à réserver', 'domain to register')}</p><p class="mono">@strobe.design · {t('compte à vérifier', 'handle to check')}</p>
<p class="mono">{t('Contenus d’exemple signalés · aucun client cité', 'Example content flagged · no clients named')}</p></div></footer></section>
</div>
</main>
<script>{JS}</script>'''
HTML = fr_typo(HTML)
open(os.path.join(HERE, '..', 'Volta_v2_identité_et_site.html'), 'w').write(HTML)
print('ok', len(HTML), HTML.count('—'))
