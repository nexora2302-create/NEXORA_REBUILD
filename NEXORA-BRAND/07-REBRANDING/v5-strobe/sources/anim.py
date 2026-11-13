import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from marks5 import halves, GS, CM, CAP, KERN, R, G, D, wm, sym
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from typo import fr_typo
CSS = open(os.path.join(HERE, 'base5.css')).read() + open(os.path.join(HERE, 'anim.css')).read()
JS = open(os.path.join(HERE, 'anim.js')).read()
TOP, BOT = halves()

def letters():
    base = CAP + 60; x = 0; out = []; prev = ''
    for ch in 'STROBE':
        if prev: x += KERN.get(prev + ch, 0) + 20
        if ch == 'O':
            r = CAP * 0.515; adv = 2 * r + 120; cx = x + adv / 2; cy = base - CAP / 2; sc = r / R
            t, b = halves(cx, cy, r, G * sc, ring=300)
            out.append(f'<g class="L"></g><path class="ot" fill="var(--gacc)" d="{t}"/><path class="ob" fill="var(--gacc)" d="{b}"/>'); x += adv
        else:
            pen = SVGPathPen(GS); g = GS[CM[ord(ch)]]; g.draw(TransformPen(pen, (1, 0, 0, -1, x, base)))
            out.append(f'<g class="L"><path fill="var(--ink)" d="{pen.getCommands()}"/></g>'); x += g.width
        prev = ch
    return out, x
LET, WW = letters()
def wmk(x, y, cap, cls='wmk'):
    s = cap / CAP
    return f'<g class="{cls}" transform="translate({x:.1f} {y - 60*s:.1f}) scale({s:.5f})">{"".join(LET)}</g>'
def wecho(x, y, cap, dx, o):
    s = cap / CAP; full = ''.join(LET).replace('<g class="L">', '<g>').replace('class="ot"', '').replace('class="ob"', '').replace('var(--gacc)', 'var(--ink)')
    return f'<g class="wecho" opacity="{o}" transform="translate({x+dx:.1f} {y - 60*s:.1f}) scale({s:.5f})">{full}</g>'
def symg(x, y, s, cls='sym'):
    inner = f'<path class="ht" fill="var(--gacc)" transform="translate({-D} 0)" d="{TOP}"/><path class="hb" fill="var(--gacc)" transform="translate({D} 0)" d="{BOT}"/>' if cls == 'sym' else f'<path fill="var(--gacc)" transform="translate({-D} 0)" d="{TOP}"/><path fill="var(--gacc)" transform="translate({D} 0)" d="{BOT}"/>'
    return f'<g class="{cls}" transform="translate({x} {y}) scale({s})">{inner}</g>'
RING = '<g class="ring" visibility="hidden"><circle cx="50" cy="50" r="58" fill="none" stroke="var(--ink)" stroke-width="5" stroke-dasharray="24.4 6" opacity=".55"/></g>'
def stage(inner, sid): return f'<svg id="{sid}" viewBox="0 0 640 360" role="img" aria-label="Logo animé"><rect width="640" height="360" fill="var(--stage)"/>{inner}</svg>'

# lockup : symbole 70 px à gauche, mot à capitale 52 px
LOCK = symg(82, 145, .7) + wecho(170, 154, 52, -24, 0) + wecho(170, 154, 52, -12, 0) + wmk(170, 154, 52)
SCENES = {
 'reveal': stage(RING + symg(250, 110, 1.4) + wecho(170, 154, 52, -24, 0) + wecho(170, 154, 52, -12, 0) + wmk(170, 154, 52), 'st-reveal'),
 'loop': stage(LOCK, 'st-loop'),
 'wipe': stage('''<g class="scB"><rect width="640" height="360" fill="var(--gacc)"/><text x="320" y="192" text-anchor="middle" font-family="Anybody" font-weight="800" font-size="40" fill="var(--stage)">Séquence B</text></g>
<defs><clipPath id="cA"><rect width="640" height="180"/></clipPath><clipPath id="cB"><rect y="180" width="640" height="180"/></clipPath></defs>
<g class="pa"><g clip-path="url(#cA)"><rect width="640" height="360" fill="var(--stage)"/><text x="320" y="192" text-anchor="middle" font-family="Anybody" font-weight="800" font-size="40" fill="var(--ink)">Séquence A</text></g></g>
<g class="pb"><g clip-path="url(#cB)"><rect width="640" height="360" fill="var(--stage)"/><text x="320" y="192" text-anchor="middle" font-family="Anybody" font-weight="800" font-size="40" fill="var(--ink)">Séquence A</text></g></g>
<rect class="slit" x="0" y="180" width="640" height="0" fill="var(--gacc)"/>''', 'st-wipe'),
 'end': stage(symg(285, 46, .7, 'esym') + symg(285, 46, .7, 'esym') + symg(285, 46, .7) +
   f'<defs><clipPath id="cW"><rect class="clipr" x="0" y="138" width="640" height="80"/></clipPath></defs><g clip-path="url(#cW)">{wmk(320 - WW * 40 / CAP / 2, 158, 40)}</g>'
   '<text class="slogan" x="320" y="262" text-anchor="middle" font-family="Anybody" font-weight="800" font-size="30" fill="var(--ink)">' + ''.join(f'<tspan>{c}</tspan>' for c in 'Ça marque.') + '</text>'
   '<text class="url" x="320" y="300" text-anchor="middle" font-family="Martian Mono" font-size="13" fill="var(--gacct)" letter-spacing="1">strobe.design</text>', 'st-end'),
 'avatar': stage('<circle cx="320" cy="180" r="92" fill="var(--avbg)"/>' + symg(265, 125, 1.1), 'st-avatar'),
 'loader': stage(symg(270, 130, 1) + '<text x="320" y="292" text-anchor="middle" font-family="Martian Mono" font-size="12" fill="var(--mutc)" letter-spacing="2">CHARGEMENT</text>', 'st-loader'),
}

FICHES = {
 'reveal': ('Révélation d’ouverture', '2,2 s', '12 i/s, puis fluide (dernière phase)', 'cubic-bezier(.16, 1, .3, 1) pour l’extinction des échos ; le reste en images tenues', 'Anneau à 12 fentes · moitié haute · moitié basse · lettres S, T, R, B, E · anneau du O (2 moitiés) · 2 échos du mot',
   [('0,00 → 0,90 s', 'L’anneau à fentes tourne de 30° par image ; derrière, les moitiés du disque parcourent 8 positions (−1, −0,5, 0, 0,5, 1…) : un mouvement vu à travers les fentes.'), ('0,90 s', 'Coupe : l’anneau disparaît, les moitiés s’arrêtent net à ± 5,6. C’est l’instant. Le clac de la signature sonore tombe ici.'), ('0,90 → 1,25 s', 'Le symbole glisse en 4 images vers sa place de logo, en se réduisant de moitié.'), ('1,00 → 1,50 s', 'Les lettres apparaissent une par image : S, T, R, O, B, E.'), ('1,50 → 2,20 s', 'Deux échos du mot (35 % et 12 %, décalés de 24 et 12 px) s’éteignent, fluide.')], 'After Effects : effet « Posterize Time » à 12 i/s sur les calques de la phase saccadée ; images clés tenues (« hold »). Lottie : images clés tenues, export à 24 i/s.'),
 'loop': ('Boucle discrète', '2,4 s, en boucle', '12 i/s', 'sinusoïde quantifiée à 12 i/s', 'Moitié haute · moitié basse · anneau du O',
   [('0 → 2,4 s', 'Les moitiés du symbole et du O s’écartent et se rapprochent de ± 1,6 autour de leur position de repos.'), ('Survol', 'La boucle se lance au survol de l’en-tête, et s’arrête hors de l’écran.')], 'Un seul calque de contrôle (expression sinus) relié aux deux moitiés ; « Posterize Time » 12. Lottie : 29 images clés tenues.'),
 'wipe': ('Transition entre séquences', '0,6 s', 'Fluide', 'cubic-bezier(.16, 1, .3, 1) pour la fente ; cubic-bezier(.7, 0, .2, 1) pour le glissement', 'Séquence A (moitié haute, moitié basse) · fente ambre · séquence B',
   [('0,00 → 0,15 s', 'Une fente ambre de 14 px s’ouvre au milieu de l’image.'), ('0,12 → 0,60 s', 'La moitié haute de la séquence A glisse à gauche, la moitié basse à droite : le symbole appliqué à l’image entière. La fente se referme en même temps.')], 'Deux précompositions masquées par moitié, déplacées en X ; la fente est un solide de 14 px. Aucune image blanche, aucun flash.'),
 'end': ('Carte de fin', '4 s (dont 1,2 s tenue)', '12 i/s, sortie du mot fluide', 'cubic-bezier(.16, 1, .3, 1) pour la sortie du mot', 'Échos du symbole ×2 · symbole · mot (masque de fente) · slogan (lettre par lettre) · adresse',
   [('0,00 → 0,75 s', 'Trois positions du symbole (12 %, 35 %, 100 %) convergent image par image : une chronophotographie qui se referme.'), ('0,75 → 1,50 s', 'Le mot sort de la fente : un masque s’ouvre verticalement depuis la ligne médiane.'), ('1,50 → 2,30 s', '« Ça marque. » s’écrit une lettre par image.'), ('2,40 s', 'L’adresse apparaît. Tenue jusqu’à 4 s.')], 'Masque de calque animé en hauteur ; texte animé par « Range Selector » en mode image par image. Pour la version anglaise, « Burned in. ».'),
 'avatar': ('Micro-animation d’avatar', '0,8 s', '3 images à 12 i/s, puis fluide', 'cubic-bezier(.16, 1, .3, 1) pour le retour', 'Moitié haute · moitié basse',
   [('0,00 → 0,25 s', 'Les moitiés traversent l’instant en trois images : décalées, alignées, décalées dans l’autre sens.'), ('0,25 → 0,80 s', 'Retour fluide à la position de repos.')], 'Pour avatars animés et favicon au survol. Lottie très léger : deux calques, six images clés.'),
 'loader': ('Chargement', '1 s par tour, en boucle', '12 i/s', 'rotation tenue, 30° par image', 'Symbole complet',
   [('Chaque image', 'Le symbole tourne de 30° : 12 images par tour, comme un disque de 1833 vu à travers ses fentes.')], 'Une rotation de 360° en 12 images tenues. Jamais plus vite : au-delà, l’œil y voit un clignotement.'),
}
ORDER = ['reveal', 'loop', 'wipe', 'end', 'avatar', 'loader']
cards = ''
for k, key in enumerate(ORDER):
    name, dur, fps, ease, layers, seq, export = FICHES[key]
    seqr = ''.join(f'<tr><td class="n">{a}</td><td>{b}</td></tr>' for a, b in seq)
    sound = '<button class="btn ghost withsound" type="button">Avec le son</button>' if key == 'reveal' else ''
    cards += f'''<section class="wrap anim sec" id="a-{key}" data-anim="{key}" data-frames="8">
<header><p class="eyebrow">Logo animé {k+1} sur 6</p><h2 class="d2">{name}</h2></header>
<div class="ag"><div class="stage">{SCENES[key]}</div>
<div class="side"><dl class="spec"><dt>Durée</dt><dd>{dur}</dd><dt>Cadence</dt><dd>{fps}</dd><dt>Courbes</dt><dd><code>{ease}</code></dd><dt>Calques</dt><dd>{layers}</dd></dl>
<div class="ctrl"><button class="btn replay" type="button">Rejouer</button>{sound}<span class="clock mono" aria-live="off">0,00 s</span></div></div></div>
<p class="eyebrow">Frise d’images clés</p><div class="strip"></div>
<div class="tbl"><table><thead><tr><th>Temps</th><th>Séquence</th></tr></thead><tbody>{seqr}</tbody></table></div><p class="small"><b>Export :</b> {export}</p></section>'''

HTML = f'''<title>Strobe v2, logos animés</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anybody:wdth,wght@50..150,400..900&family=Schibsted+Grotesk:wght@400..700&family=Martian+Mono:wdth,wght@75..112.5,400..700&display=swap">
<style>{CSS}</style>
<header class="bar"><div class="wrap"><a class="lg" href="#top" aria-label="Strobe"><span class="lock">{sym('var(--acc)')}{wm('currentColor', 'var(--acc)')}</span></a>
<nav aria-label="Animations">{''.join(f'<a href="#a-{k}">{FICHES[k][0].split(" ")[0]}</a>' for k in ORDER)}</nav>
<button class="tg" type="button" id="themeBtn">Thème</button></div></header>
<main id="top">
<section class="wrap hero0"><p class="eyebrow">Strobe · logos animés · 13 novembre 2026</p><h1 class="d1">Arrêter,<br>puis enchaîner.</h1>
<div class="cols"><p class="lead">Un principe moteur : le mouvement de Strobe obéit au disque de 1833. Il avance par images tenues (12 par seconde), s’arrête net sur l’instant, puis s’enchaîne. Le fluide est réservé à ce qui suit l’arrêt : un écho qui s’éteint, un mot qui sort de la fente.</p>
<div class="cmp"><div><p class="eyebrow">12 images par seconde : la marque</p><div class="lane"><span class="dot s12">{sym('var(--acc)')}</span></div></div><div><p class="eyebrow">Fluide : l’interface</p><div class="lane"><span class="dot sfl">{sym('var(--acc)')}</span></div></div></div></div>
<ul class="rules"><li>Aucun flash, aucune image blanche : rien ne clignote, jamais plus de trois changements de luminosité forts par seconde.</li><li>Mouvement réduit demandé : chaque logo s’affiche dans son état final, immobile, et la lecture est désactivée.</li><li>Chaque animation se rejoue, fonctionne en clair et en sombre, et sa frise montre 8 images clés tirées de la même fonction de rendu.</li><li>Le son de la v1 est recalé sur la révélation : le clac tombe à 0,90 s, au moment où le disque s’arrête.</li></ul></section>
{cards}
</main>
<script>{JS}</script>'''
HTML = fr_typo(HTML)
open(os.path.join(HERE, '..', 'Strobe_v2_logos_animés.html'), 'w').write(HTML)
print('ok', len(HTML), HTML.count('—'), WW)
