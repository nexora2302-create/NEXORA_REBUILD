import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from marks3 import rhythmos_word, rhythmos_symbol, svg
from typo import fr_typo
INK, PAP, KY, KYL = '#121214', '#F2F3F5', '#2340D8', '#6E86FF'
CSS = open(os.path.join(HERE, 'base3.css')).read() + open(os.path.join(HERE, 'site3.css')).read()
JS = open(os.path.join(HERE, 'site3.js')).read()

def sym(fg='currentColor', acc='var(--x)', cls='sy', label='Symbole Rhythmos'): return svg(rhythmos_symbol(fg, acc), '0 0 100 100', cls, label)
def wm(fg='currentColor', cls='wm', label='Rhythmos'):
    i, w, h = rhythmos_word(fg); return svg(i, f'-30 0 {w+60:.0f} {h:.0f}', cls, label)
def lock(fg='currentColor', acc='var(--x)', cls='lock'):
    return f'<span class="{cls}">{sym(fg, acc, "sy")}{wm(fg)}</span>'
def live(word='RHYTHMOS', pat='LSSLSSLL', cls='lw'):
    return f'<span class="{cls}" aria-label="{word.capitalize()}">' + ''.join(f'<span aria-hidden="true" data-q="{q}" style="--i:{k}">{c}</span>' for k, (c, q) in enumerate(zip(word, pat))) + '</span>'
def t(fr, en, tag='span', cls=''):
    c = f' class="{cls}"' if cls else ''
    return f'<{tag}{c} lang="fr">{fr}</{tag}><{tag}{c} lang="en">{en}</{tag}>'

construct = f'''<svg class="cons" viewBox="-8 -4 116 108" role="img" aria-label="Construction du symbole Rhythmos">
<g stroke="var(--rule)" stroke-width=".3">{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="100"/>' for x in range(0, 101, 10))}{''.join(f'<line x1="0" y1="{y}" x2="100" y2="{y}"/>' for y in range(0, 101, 10))}</g>
<g opacity=".92">{rhythmos_symbol('var(--fg)', 'var(--x)')}</g>
<circle cx="50" cy="36" r="20" fill="none" stroke="var(--x)" stroke-width=".5" stroke-dasharray="1.4 1.2"/>
<line x1="50" y1="56" x2="84" y2="95" stroke="var(--x)" stroke-width=".4" stroke-dasharray="1 1"/>
<g class="cl"><text x="-6" y="-0.5">grille 100 · trait 14</text><text x="73" y="30">panse r 20</text><text x="60" y="104">jambe à 45°, détachée</text><text x="-6" y="104">Ρ grec</text></g></svg>'''

POLES = [
 ('motion', 'Motion design', 'Motion design', 'Chaque mouvement a une forme.', 'Every movement has a shape.', 'Logos animés, génériques, films de marque, contenus pour les réseaux, habillage d’écrans.', 'Animated logos, title sequences, brand films, social content, screen graphics.'),
 ('identite', 'Identité et communication visuelle', 'Identity and visual communication', 'Une forme qu’on reconnaît partout.', 'A shape you know anywhere.', 'Stratégie et nom, logo, systèmes graphiques, édition, affiches, signalétique.', 'Strategy and naming, logos, design systems, print, posters, signage.'),
 ('web', 'Sites web', 'Websites', 'Des pages qui ont du rythme.', 'Pages with a pulse.', 'Sites de marque, portfolios, pages de lancement, maintenance.', 'Brand sites, portfolios, launch pages, maintenance.'),
]
poles = ''.join(f'<li class="pole" id="s-{k}"><h3 class="pt">{t(a, b)}</h3><p class="pl it">{t(c, d)}</p><p class="ps">{t(e, f)}</p></li>' for k, a, b, c, d, e, f in POLES)

WORKS = [('L', 'Identité', 'Identity'), ('S', 'Motion', 'Motion'), ('S', 'Site web', 'Website'), ('L', 'Film de marque', 'Brand film'), ('S', 'Affiche', 'Poster'), ('S', 'Événement', 'Event')]
works = ''.join(f'<li class="wk wk-{q}"><div class="wimg" aria-hidden="true">{sym(PAP if k % 3 == 0 else INK, KYL if k % 3 == 0 else KY, "wsy", "")}</div><p class="wl">{t("Exemple · " + a, "Example · " + b)}</p></li>' for k, (q, a, b) in enumerate(WORKS))

STEPS = [('Écouter', 'Listen', 'Comprendre la marque, son public, ce qu’elle doit accomplir.', 'Understand the brand, its audience, what it has to achieve.'), ('Dessiner', 'Shape', 'Une direction claire, validée avec vous avant la production.', 'One clear direction, signed off before production.'), ('Animer', 'Move', 'Identité, mouvement, interface, avec des points d’étape réguliers.', 'Identity, motion, interface, with regular check-ins.'), ('Livrer', 'Deliver', 'Fichiers prêts, site en ligne, suivi après le lancement.', 'Files ready, site live, support after launch.')]
steps = ''.join(f'<li><span class="beat mono" aria-hidden="true">{"●" + "○" * k + "○" * (3 - k) if False else "".join("●" if j == k else "○" for j in range(4))}</span><h3 class="d3">{t(a, b)}</h3><p>{t(c, d)}</p></li>' for k, (a, b, c, d) in enumerate(STEPS))

MOT = [('Tempo', '100 battements par minute : un temps = 600 ms, une brève = 150 ms', '·', 'Tout mouvement tombe sur une subdivision du temps.'),
       ('1 · Le tracé', '0 → 600 ms', 'cubic-bezier(.65, 0, .35, 1)', 'Le Ρ se trace d’un seul geste.'),
       ('2 · Le pas', '600 → 900 ms', 'cubic-bezier(.2, .8, .2, 1)', 'La jambe se détache et fait un pas en avant.'),
       ('3 · Le mètre', '900 → 1 500 ms, une lettre toutes les 75 ms', 'cubic-bezier(.65, 0, .35, 1)', 'Les lettres du mot prennent leur largeur, longues et brèves.'),
       ('Règle', 'toujours', '·', 'Rien ne bouge autrement que par la forme (largeur), l’ordre (séquence) ou la position (quarts de tour). Aucun fondu, aucun rebond.')]
mot = ''.join(f'<tr><th scope="row">{a}</th><td class="n">{b}</td><td><code>{c}</code></td><td>{d}</td></tr>' for a, b, c, d in MOT)

HTML = f'''<title>Rhythmos, identité et site</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Mona+Sans:wdth,wght@75..125,400..900&family=Newsreader:ital,opsz,wght@0,6..72,400..600;1,6..72,400..500&family=JetBrains+Mono:wght@400..600&family=Noto+Serif:wght@500&display=swap">
<style>{CSS}</style>
<header class="bar"><div class="wrap"><a class="lg" href="#identite" aria-label="Rhythmos, brand book">{lock()}</a>
<nav class="sw" aria-label="Parties"><a href="#identite" data-v="identite">Brand book</a><a href="#site" data-v="site">Maquette du site</a></nav>
<button class="tg" type="button" id="themeBtn">Thème</button></div></header>
<main>
<div class="view" id="v-identite">
<section class="wrap cover"><p class="eyebrow">Brand book · 10 novembre 2026</p>
<div class="cvl" id="cvLogo">{sym('currentColor', 'var(--x)', 'sy cvs')}{live()}</div>
<p class="sig it">Avant de dire « rythme », <i>rhythmos</i> voulait dire « forme » : la forme que prend une chose pendant qu’elle bouge. Nous dessinons des marques qui bougent sans jamais perdre la leur.</p>
<div class="btns"><button class="btn" type="button" data-replay="#cvLogo">Rejouer la signature</button><button class="btn ghostb" type="button" data-replay="#cvLogo" data-with-sound>Avec le son</button></div></section>

<div class="wrap">
<section class="sec" id="histoire"><header><p class="eyebrow">L’histoire</p><h2 class="d1">La forme<br><span class="it hl">de ce qui bouge.</span></h2></header>
<div class="cols"><ol class="layers">
<li><span class="eyebrow">Le sens</span><p>En grec ancien, ῥυθμός (rhythmos) a d’abord voulu dire « forme ». Selon Aristote, Démocrite l’employait pour dire ce qui distingue la lettre A de la lettre N. Le linguiste Émile Benveniste a montré que c’était la forme d’une chose qui bouge, pas la cadence régulière des vagues.</p></li>
<li><span class="eyebrow">Le symbole</span><p>Notre R est un Ρ grec, le rhô, initiale du mot, qui fait un pas en avant. L’alphabet latin vient du grec : notre lettre est le grec qui se met en marche.</p></li>
<li><span class="eyebrow">La conviction</span><p>Une marque n’est jamais immobile : elle change d’écran, de format, de vitesse. Notre travail, c’est qu’elle garde sa forme.</p></li></ol>
<div class="mani"><div><p class="eyebrow">Manifeste · FR · 84 mots</p><p>Avant de dire « rythme », le mot grec <i>rhythmos</i> voulait dire « forme » : la forme que prend une chose pendant qu’elle bouge. Un geste, une écriture, un pas. Nous croyons qu’une marque est faite de la même matière. Elle passe d’un écran à une affiche, d’une seconde à une heure, d’une ville à une autre. Elle ne s’arrête jamais. Notre travail, c’est qu’elle garde sa forme. Motion, identité, web : trois manières de donner une forme juste à ce qui bouge.</p></div>
<div lang="en"><p class="eyebrow">Manifesto · EN · 80 words</p><p>Before it meant rhythm, the Greek word <i>rhythmos</i> meant form: the shape a thing takes while it moves. A gesture, a handwriting, a step. We believe brands are made of the same stuff. They move from a screen to a poster, from one second to an hour, from one city to another. They never stand still. Our job is to make sure they keep their shape. Motion, identity, web: three ways of giving the right form to things that move.</p></div></div></div></section>

<section class="sec" id="logo"><header><p class="eyebrow">Logo</p><h2 class="d2">Un rhô qui fait un pas.</h2></header>
<div class="cols"><figure class="pane">{construct}<figcaption>Le symbole : un Ρ grec tracé d’un seul geste, et une jambe détachée qui fait un pas. Le vide entre les deux vaut la moitié du trait : c’est lui qui révèle la double lecture.</figcaption></figure>
<div class="lvs">
<div class="lvi day wide">{lock(INK, KY)}</div><div class="lvi night wide">{lock(PAP, KYL)}</div>
<div class="lvi day">{sym(INK, KY)}</div><div class="lvi night">{sym(PAP, KYL)}</div><div class="lvi kb">{sym(PAP, PAP)}</div>
<div class="lvi day wide">{wm(INK)}</div>
<div class="rules"><p class="eyebrow">Le logotype</p><p class="small">Mona Sans 800. Les lettres longues sont en largeur 125, les brèves en 75, sur le mètre de la fin d’un vers d’Homère : ¯ ˘ ˘ | ¯ ˘ ˘ | ¯ ¯. Le nom est écrit en rythme.</p>
<p class="eyebrow">Règles</p><ul><li><b>Zone de protection :</b> deux épaisseurs de trait tout autour.</li><li><b>Tailles minimales :</b> symbole 16 px ou 5 mm ; logotype 80 px ou 22 mm de large.</li><li><b>Interdits :</b> recoller la jambe au rhô, égaliser les largeurs du logotype, donner à la jambe une autre couleur que le kyanos ou celle du rhô, faire tourner le symbole, l’entourer.</li></ul></div></div></div>
<div class="tests">
<figure><div class="tst day">{sym(INK, INK, 's16')}{sym(INK, INK, 's24')}{sym(INK, KY, 's32')}</div><figcaption>16, 24, 32 px</figcaption></figure>
<figure><div class="tst day blr">{sym(INK, INK)}</div><figcaption>Flou, sans le nom : un R qui avance</figcaption></figure>
<figure><div class="tst night">{sym(PAP, PAP)}</div><figcaption>Négatif monochrome</figcaption></figure>
<figure><div class="tst ph">{sym(PAP, PAP)}</div><figcaption>Sur image (fond simulé)</figcaption></figure></div></section>

<section class="sec" id="couleurs"><header><p class="eyebrow">Couleurs</p><h2 class="d2">Encre, plâtre, kyanos.</h2>
<p class="small">Une seule couleur possédée : le kyanos, le bleu égyptien, premier pigment fabriqué de l’histoire, que les Grecs ont posé sur leurs temples. Il sert à marquer, comme l’encre de couleur qui marquait les débuts de chapitre dans les manuscrits : jamais en grands aplats bleu et blanc.</p></header>
<div class="pal">
<div class="pc" style="background:{PAP};color:{INK}"><b>Plâtre</b><code>#F2F3F5</code><span class="pp">50 %</span><span>Fond principal. Un blanc froid, sans crème.</span><span class="ct">Encre dessus : 16,7:1</span></div>
<div class="pc" style="background:{INK};color:{PAP}"><b>Encre</b><code>#121214</code><span class="pp">35 %</span><span>Texte, mode sombre, vidéo.</span><span class="ct">Plâtre dessus : 16,7:1</span></div>
<div class="pc" style="background:{KY};color:{PAP}"><b>Kyanos</b><code>#2340D8</code><span class="pp">10 %</span><span>La jambe du R, les liens, les marques de rythme.</span><span class="ct">Sur plâtre : 6,7:1</span></div>
<div class="pc" style="background:{KYL};color:{INK}"><b>Kyanos clair</b><code>#6E86FF</code><span class="pp">sombre</span><span>Le kyanos du mode sombre.</span><span class="ct">Sur encre : 5,8:1</span></div>
<div class="pc" style="background:#5B6070;color:{PAP}"><b>Pierre</b><code>#5B6070</code><span class="pp">5 %</span><span>Texte secondaire. En sombre : #9AA0AE.</span><span class="ct">Sur plâtre : 5,6:1 · #9AA0AE sur encre : 7,1:1</span></div></div>
<div class="prop" role="img" aria-label="Proportions : plâtre 50 %, encre 35 %, kyanos 10 %, pierre 5 %"><i style="flex:50;background:{PAP}"></i><i style="flex:35;background:{INK}"></i><i style="flex:10;background:{KY}"></i><i style="flex:5;background:#5B6070"></i></div></section>

<section class="sec" id="typo"><header><p class="eyebrow">Typographie</p><h2 class="d2">Des longues et des brèves.</h2>
<p class="small">Mona Sans a un axe de largeur de 75 à 125 : on peut écrire en syllabes longues et brèves, comme un poète grec. Newsreader en italique porte les phrases longues. Pourquoi pas Anybody (Strobe) : son étirement extrême servait le flash ; ici, il faut une largeur mesurée, lisible en texte courant.</p></header>
<div class="spec"><div class="spo"><p id="meterOut" class="mo" aria-live="polite"></p>
<div class="spi"><label for="meterInput" class="eyebrow">Écrivez un mot</label><input id="meterInput" value="Cotonou" maxlength="18" autocomplete="off">
<label for="meterSel" class="eyebrow">Mètre</label><select id="meterSel"><option value="dactyle">Dactyle ¯ ˘ ˘</option><option value="trochee">Trochée ¯ ˘</option><option value="iambe">Iambe ˘ ¯</option><option value="anapeste">Anapeste ˘ ˘ ¯</option><option value="spondee">Spondée ¯ ¯</option></select></div></div>
<div class="tyl"><div><p class="eyebrow">Titrage · Mona Sans 800, largeur 75 à 125</p><p class="tA">Chaque mouvement a une forme.</p></div>
<div><p class="eyebrow">Phrase longue · Newsreader italique</p><p class="tS it">Nous dessinons des marques qui bougent sans jamais perdre leur forme.</p></div>
<div><p class="eyebrow">Texte · Mona Sans 400</p><p class="tB">Logos animés, génériques, systèmes graphiques et sites : le même dessin, à toutes les vitesses.</p></div>
<div><p class="eyebrow">Données · JetBrains Mono</p><p class="tC">100 BPM · 600 ms · ¯ ˘ ˘</p></div></div></div></section>

<section class="sec" id="motion"><header><p class="eyebrow">Motion</p><h2 class="d2">Forme, ordre, position.</h2><p class="small">Les trois différences de Démocrite deviennent les trois seules façons de bouger.</p></header>
<div class="tbl"><table><thead><tr><th>Phase</th><th>Temps</th><th>Courbe</th><th>Ce qui se passe</th></tr></thead><tbody>{mot}</tbody></table></div>
<div class="btns"><button class="btn" type="button" data-replay="#cvLogo" onclick="location.hash='identite'">Voir la séquence en haut de page</button></div></section>

<section class="sec" id="son"><header><p class="eyebrow">Son · bonus</p><h2 class="d2">Le dactyle.</h2><p class="small">Une signature de 1,7 s : une longue, deux brèves, une longue qui reste (la, mi, mi, la). Le rythme du mot, joué. Fin de vidéo, ouverture de présentation ; jamais en lecture automatique sur le site.</p></header>
<div class="snd"><button class="btn" type="button" data-sound-logo>Écouter · 1,7 s</button><p class="mono big">━ ◡ ◡ ━</p></div></section>

<section class="sec" id="images"><header><p class="eyebrow">Images et ton</p><h2 class="d2">Saisir la forme du geste.</h2></header>
<div class="grid tw">
<article><h3 class="d3">Images</h3><ul><li>Le geste en plusieurs états, comme une chronophotographie : la main qui trace, l’écran qui change, le pas.</li><li>Lumière de travail, nette, ombres franches. Gardé de la v2.</li><li>Les écrans et les supports en situation, à leur échelle réelle.</li><li>Un seul accent kyanos par image au maximum.</li></ul></article>
<article><h3 class="d3">Voix</h3><p><b>Précise.</b> <b>Calme.</b> <b>Vivante.</b></p><ul><li>« On a dessiné la forme. Maintenant, on la fait bouger. »</li><li>« Une marque qu’on reconnaît à toutes les vitesses, c’est une marque qui a un rythme. »</li><li>« On » en français, « we » en anglais. Pas de point d’exclamation, pas de superlatif.</li></ul></article>
<article class="never"><h3 class="d3">Jamais</h3><ul><li>Colonnes, temples, statues antiques, lauriers, frise grecque, bandes bleu et blanc, Santorin.</li><li>Wax, masques, cartes ou silhouettes du continent, globes, ampoules « idée ».</li><li>Ondes sonores décoratives, métronomes en clip-art, notes de musique.</li><li>Images générées présentées comme de vrais projets. « Solutions », « innovant », « passion », « 360° ».</li></ul></article></div>
<div class="tbl"><table><thead><tr><th>Avant</th><th>Après</th></tr></thead><tbody>
<tr><td>Nous créons des contenus dynamiques et impactants.</td><td><b>Chaque mouvement a une forme. On la dessine.</b></td></tr>
<tr><td>Une identité visuelle forte et cohérente.</td><td><b>Une forme qu’on reconnaît à toutes les vitesses.</b></td></tr>
<tr><td>Des sites modernes et responsives.</td><td><b>Des pages qui ont du rythme, sur tous les écrans.</b></td></tr></tbody></table></div></section>

<section class="sec" id="applications"><header><p class="eyebrow">Applications</p><h2 class="d2">Partout, la même forme.</h2></header>
<div class="apps">
<figure><div class="day kak"><span class="kl">{lock(INK, KY)}</span><p class="it ks">La forme<br>de ce qui bouge.</p><span class="ksy">{sym(INK, KY)}</span></div><figcaption>Kakémono 80 × 200 cm</figcaption></figure>
<figure><div class="avs"><span class="av night">{sym(PAP, KYL)}</span><span class="av kb">{sym(PAP, PAP)}</span><span class="av day bd">{sym(INK, KY)}</span></div><figcaption>Avatars</figcaption></figure>
<figure><div class="night end">{sym(PAP, KYL)}<p class="it" lang="en">In motion. In shape.</p><p class="mono">rhythmos.studio</p></div><figcaption>Carte de fin vidéo 16:9, calée sur le dactyle</figcaption></figure>
<figure><div class="day letter">{lock(INK, KY, 'lock sml')}<span class="lline"></span><span class="lline s"></span><span class="lline"></span><span class="lline s2"></span><p class="lfoot mono">Rhythmos · Cotonou, Bénin · rhythmos.studio</p></div><figcaption>En-tête de lettre A4</figcaption></figure>
<figure><div class="cards"><div class="bcard night">{sym(PAP, KYL)}</div><div class="bcard day bd"><b>Prénom Nom</b><span>Motion design</span><span class="mono">prenom@rhythmos.studio</span>{sym(INK, KY, 'sy bsy')}</div></div><figcaption>Carte de visite 85 × 55 mm (nom d’exemple)</figcaption></figure>
<figure><div class="day mail bd"><p>Prénom Nom<br><span class="small">Rhythmos · Motion, identité, web</span></p><p class="mono small">rhythmos.studio · Cotonou</p>{lock(INK, KY, 'lock xs')}</div><figcaption>Signature e-mail (nom d’exemple)</figcaption></figure>
</div></section>
</div></div>

<!-- =============== MAQUETTE =============== -->
<div class="view site" id="v-site" data-lang="fr" lang="fr" hidden>
<div class="sbar"><div class="wrap"><span class="slg">{lock()}</span>
<nav aria-label="Site"><a href="#s-motion">Motion</a><a href="#s-identite">{t('Identité', 'Identity')}</a><a href="#s-web">Web</a><a href="#s-av" class="sec2">{t('Audiovisuel', 'Audiovisual')}</a><a href="#s-contact">Contact</a></nav>
<button class="tg" type="button" id="langBtn">EN</button></div></div>

<section class="hero" id="heroStage" aria-label="Accueil"><div class="wrap hw">
<p class="eyebrow">{t('Studio de création · Cotonou', 'Creative studio · Cotonou')}</p>
<h1 class="hword" id="heroWord" aria-label="Rhythmos">{''.join(f'<span aria-hidden="true" data-q="{q}">{c}</span>' for c, q in zip('RHYTHMOS', 'LSSLSSLL'))}</h1>
<div class="hb"><p class="hsig it">{t('Avant de dire « rythme », <i>rhythmos</i> voulait dire « forme » : la forme que prend une chose pendant qu’elle bouge. Nous dessinons des marques qui bougent sans jamais perdre la leur.', 'Before it meant rhythm, <i>rhythmos</i> meant form: the shape a thing takes while it moves. We design brands that move without ever losing theirs.')}</p>
<div class="hctl"><button class="btn tap" type="button" id="tapBtn">{t('Battre la mesure', 'Tap the beat')}</button>
<div class="chips" role="group" aria-label="Mètre">{''.join(f'<button type="button" class="mchip" data-m="{m}" aria-pressed="{str(m == "dactyle").lower()}">{n}</button>' for m, n in [('dactyle', '━ ◡ ◡'), ('trochee', '━ ◡'), ('iambe', '◡ ━'), ('spondee', '━ ━')])}</div>
<p class="mono rd"><span id="meterSig">━ ◡ ◡</span> · <span id="bpm">100</span> BPM · {''.join(f'<span data-meter-name="{m}"{"" if m == "dactyle" else " hidden"}>{n}</span>' for m, n in [('dactyle', t('dactyle', 'dactyl')), ('trochee', t('trochée', 'trochee')), ('iambe', t('iambe', 'iamb')), ('anapeste', t('anapeste', 'anapest')), ('spondee', t('spondée', 'spondee'))])}</p>
<button class="tg" type="button" id="soundBtn" aria-pressed="false"><span data-s="off">{t('Son coupé', 'Sound off')}</span><span data-s="on" hidden>{t('Son activé', 'Sound on')}</span></button>
<p class="hint mono">{t('Touchez le mot, ou le bouton, en rythme.', 'Tap the word, or the button, in time.')}</p></div></div></div></section>

<section class="wrap s-sense"><p class="eyebrow">{t('Le nom', 'The name')}</p>
<ol class="sense"><li><b>ῥυθμός</b>{t('Le mot grec pour « forme » : la forme d’une chose qui bouge.', 'The Greek word for form: the shape of a thing in motion.')}</li>
<li>{sym('currentColor', 'var(--x)', 'sy ssy')}{t('Notre R est un rhô grec qui fait un pas en avant.', 'Our R is a Greek rho taking a step forward.')}</li>
<li><b class="it">{t('Garder la forme.', 'In motion. In shape.')}</b>{t('Une marque bouge tout le temps. Notre travail, c’est qu’elle reste elle-même.', 'Brands never stand still. Our job is to keep them themselves.')}</li></ol></section>

<section class="wrap s-poles"><header class="sh"><p class="eyebrow">{t('Ce que nous faisons', 'What we do')}</p><h2 class="d2">{t('Trois manières de donner une forme.', 'Three ways to give things shape.')}</h2></header>
<ol class="poles">{poles}</ol>
<div class="av-band" id="s-av"><p class="eyebrow">{t('Aussi, sur le terrain', 'Also, on the ground')}</p><p class="avt">{t('Son, projection, captation, location de matériel. La même équipe, le jour J : ce qu’on a dessiné, on sait aussi le faire tourner en salle.', 'Sound, projection, filming, equipment hire. The same team on the day: what we design, we can also run live in the room.')}</p></div></section>

<section class="wrap s-work"><header class="sh"><p class="eyebrow">{t('Travaux', 'Work')}</p><h2 class="d2">{t('Longue, brève, brève.', 'Long, short, short.')}</h2><p class="small">{t('La grille suit le dactyle. Emplacements d’exemple : les vrais projets arrivent avec l’accord des clients.', 'The grid follows the dactyl. Example slots: real projects go here once clients approve.')}</p></header><ol class="works">{works}</ol></section>

<section class="wrap s-method"><header class="sh"><p class="eyebrow">{t('Méthode', 'Process')}</p><h2 class="d2">{t('Une mesure à quatre temps.', 'Four beats to the bar.')}</h2></header><ol class="steps">{steps}</ol></section>

<section class="night s-contact" id="s-contact"><div class="wrap cw">
<h2 class="mega">{t('Donnons-lui<br><span class="it">sa forme.</span>', 'Let’s give it<br><span class="it">its shape.</span>')}</h2>
<form id="briefForm" class="form" novalidate>
<label for="f-name">{t('Nom', 'Name')}</label><input id="f-name" name="name" autocomplete="name" required>
<label for="f-mail">E-mail</label><input id="f-mail" name="email" type="email" autocomplete="email" required>
<label for="f-what">{t('Le projet', 'The project')}</label><select id="f-what" name="what"><option data-fr="Motion design" data-en="Motion design">Motion design</option><option data-fr="Identité" data-en="Identity">Identité</option><option data-fr="Site web" data-en="Website">Site web</option><option data-fr="Audiovisuel" data-en="Audiovisual">Audiovisuel</option></select>
<label for="f-brief">{t('Ce que vous lancez, et quand', 'What you’re launching, and when')}</label><textarea id="f-brief" name="brief" rows="3" required></textarea>
<button class="btn" type="submit">{t('Envoyer le brief', 'Send the brief')}</button>
<p id="formState" class="fstate" tabindex="-1" hidden>{t('Maquette : ce formulaire n’envoie rien. Sur le vrai site, le brief part au studio.', 'Mock-up: this form sends nothing. On the real site, the brief goes to the studio.')}</p></form></div>
<footer class="wrap foot"><div class="fwm">{wm(PAP)}</div><div class="fcols"><p>{t('Basés à Cotonou. Clients partout.', 'Based in Cotonou. Working everywhere.')}</p><p class="mono">rhythmos.studio · {t('domaine à réserver', 'domain to register')}</p><p class="mono">@rhythmos.studio · {t('compte à vérifier', 'handle to check')}</p><p class="mono">{t('Contenus d’exemple signalés · aucun client cité', 'Example content flagged · no clients named')}</p></div></footer></section>
</div></main>
<script>{JS}</script>'''
HTML = fr_typo(HTML)
open(os.path.join(HERE, '..', 'identité_et_site_rhythmos.html'), 'w').write(HTML)
print('ok', len(HTML), HTML.count('—'))
