"""Brand Book NEXORA Studio v2.0 (26 nov. 2026). Génère brandbook.html ; pdf.js en fait le PDF 16:9.
Faits repris du brand book v1 (relevés sur le site) et des décisions du 26 nov. 2026. Rien d'inventé."""
import os, sys, json, math
HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, '..', '..')
sys.path.insert(0, os.path.join(B, '07-REBRANDING', 'v4', 'sources'))
from typo import fr_typo
L = json.load(open(os.path.join(B, '13-NEXORA-STUDIO', 'sources', 'logo.json')))
VB = L['viewBox']; X0, Y0, W, H = map(float, VB.split())
BASE, CAPTOP = Y0 + 760, Y0 + 10          # ligne de base et haut des capitales de NEXORA (unités du tracé)
ENCRE, OS, BRAISE, BRAISE_P = '#0D0C0B', '#ECE5D8', '#FF4A1C', '#B02F0B'
NPAGES = 25
IMG = 'img'

def logo(cls='', style='', word='currentColor', studio=None, extra=''):
    st = f' fill="{studio}"' if studio else ' class="st"'
    return (f'<svg class="lg {cls}" style="{style}" viewBox="{VB}" role="img" aria-label="NEXORA Studio" overflow="visible">'
            f'<path fill="{word}" d="{L["word"]}"/><path{st} d="{L["studio"]}"/>{extra}</svg>')
def symbol(size, bg=ENCRE, n=OS, s=BRAISE, r=220, style=''):
    rect = f'<rect width="1000" height="1000" rx="{r}" fill="{bg}"/>' if bg else ''
    return (f'<svg style="width:{size}px;height:{size}px;display:block;{style}" viewBox="0 0 1000 1000" aria-hidden="true">{rect}'
            f'<path fill="{n}" d="{L["fav"]["N"]}"/><path fill="{s}" d="{L["fav"]["s"]}" stroke="{bg or ENCRE}" stroke-width="34" paint-order="stroke"/></svg>')
def E_custom(fill, h):
    return f'<svg viewBox="0 0 710 750" style="height:{h}px;width:auto;display:block" aria-hidden="true"><path fill="{fill}" d="M0 0H710V180H220V285H650V465H220V570H710V750H0Z"/></svg>'

def head(n, label):
    return f'<header class="ph"><span class="sm">{logo("small")}</span><span class="mono">{label}</span><span class="mono pn">{n:02d} / {NPAGES}</span></header>'
def page(n, theme, label, body, cls=''):
    return f'<section class="pg {theme} {cls}">{head(n, label)}{body}</section>'
def ttl(t, sub=''):
    return f'<div class="tt"><h2>{t}</h2>{f"<p class=lead>{sub}</p>" if sub else ""}</div>'

P = []
# 01 couverture
P.append(f'''<section class="pg dark cover">
<header class="ph"><span class="mono">Brand Book</span><span class="mono">Version 2.0 · novembre 2026</span><span class="mono">Cotonou, Bénin</span></header>
<div class="cv">{logo('huge')}</div>
<p class="cv-lead"><span class="hand">Nous faisons bouger les marques.</span></p>
<p class="mono cv-foot">Identité, logo, couleurs, typographies, mouvement et applications</p>
</section>''')
# 02 sommaire
toc = [('La marque', '03'), ('Le nom', '07'), ('Le logo', '08'), ('Le symbole', '13'), ('Usages interdits', '14'), ('Les couleurs', '15'),
       ('Les typographies', '18'), ('Le geste manuscrit', '20'), ('Image et mouvement', '21'), ('Applications', '22'), ('Fichiers livrés', '25')]
P.append(page(2, 'light', 'Sommaire', f'''{ttl('Sommaire')}
<ol class="toc">{''.join(f'<li><span class="mono">{p}</span><b>{t}</b></li>' for t, p in toc)}</ol>'''))
# 03 ce qui change
P.append(page(3, 'dark', 'Version 2.0', f'''{ttl('Ce qui change, <em class="hand">ce qui reste.</em>')}
<div class="two">
<div><h3 class="mono acc">Change</h3><ul class="lst">
<li><b>Le nom</b><span>NEXORA devient NEXORA Studio.</span></li>
<li><b>Le logo</b><span>Le monogramme NX est remplacé par le mot NEXORA et « Studio » écrit à la main.</span></li>
<li><b>Les typographies</b><span>Unbounded pour les titres, Mr Dafoe pour le geste manuscrit. Archivo reste pour le texte, JetBrains Mono pour les données.</span></li>
<li><b>Le symbole</b><span>Un N traversé par le S de « Studio », pour le favicon, les avatars et les petites tailles.</span></li></ul></div>
<div><h3 class="mono">Reste</h3><ul class="lst">
<li><b>Les couleurs</b><span>Encre, os, braise, et toutes leurs déclinaisons.</span></li>
<li><b>Le ton</b><span>Court, actif, au vouvoiement, en français d’abord.</span></li>
<li><b>La sculpture 3D du X</b><span>Elle reste l’image d’ouverture du site.</span></li>
<li><b>La règle d’or</b><span>La braise ne se pose jamais sur l’os.</span></li></ul></div>
</div>'''))
# 04 mission
P.append(page(4, 'light', 'La marque', f'''{ttl('Mission et positionnement')}
<div class="two">
<div><p class="big-q">Transformer les idées en identités fortes, contenus visuels et expériences digitales pertinentes.</p></div>
<div class="txt"><p><b>Qui.</b> Un studio créatif et digital qui accompagne entreprises, marques, entrepreneurs, institutions et créateurs.</p>
<p><b>Où.</b> Basé à Cotonou, au Bénin. Des clients au Bénin, en Afrique et à l’international, en français comme en anglais.</p>
<p><b>Quoi.</b> Communication visuelle, motion design, création de sites web : séparément ou ensemble.</p>
<p><b>Positionnement.</b> Un studio contemporain, exigeant, polyvalent et professionnel, qui refuse de ressembler à une agence générique.</p></div>
</div>'''))
# 05 personnalité
traits = [('En mouvement', 'La marque se pense comme une image qui bouge. Tout ce qu’elle produit a un rythme.'),
          ('Éditoriale', 'Typographie affirmée, hiérarchie nette, compositions audacieuses mais lisibles.'),
          ('Cinématographique', 'Fond d’encre, lumière braise, contrastes maîtrisés, sens du cadrage.'),
          ('Ancrée et ouverte', 'Née à Cotonou, pensée pour le monde. Fière d’où elle vient, sans folklore.')]
P.append(page(5, 'dark', 'La marque', f'''{ttl('Personnalité')}
<div class="grid4">{''.join(f'<div class="card"><span class="mono acc">0{i+1}</span><b>{t}</b><span>{d}</span></div>' for i, (t, d) in enumerate(traits))}</div>
<div class="mat"><span class="mono">Quatre matières</span><b>L’encre</b> le fond, noir chaud · <b>L’os</b> la lumière du papier · <b>La braise</b> l’énergie · <b>Le geste</b> la main qui signe</div>'''))
# 06 ton de voix
sig = ['Studio créatif en mouvement.', 'Nous faisons bouger les marques.', 'Né à Cotonou, pensé pour le monde.', 'Trois métiers, un seul mouvement.', 'Du brief à l’image.', 'Un projet ? Mettons-le en mouvement.']
rules = [('Court et actif', 'Des verbes plutôt que des adjectifs : « Démarrer un projet ».'), ('Vouvoiement', 'On s’adresse au lecteur avec « vous ».'),
         ('Français d’abord', 'Anglais disponible. Espace fine avant ? ! : ;'), ('Pas de tiret cadratin', 'Virgules, deux-points ou points.'),
         ('Rien d’invérifiable', 'Pas de chiffres, délais ou références non confirmés.'), ('« Vidéo », pas « film »', 'On parle de vidéos de marque, de présentation, de lancement.')]
P.append(page(6, 'light', 'La marque', f'''{ttl('Ton de voix')}
<div class="two"><div><h3 class="mono acc-p">Signatures du site</h3><ul class="sig">{''.join(f'<li>{x}</li>' for x in sig)}</ul></div>
<div><h3 class="mono acc-p">Règles d’écriture</h3><ul class="lst dk">{''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in rules)}</ul></div></div>'''))
# 07 le nom
P.append(page(7, 'dark', 'Le nom', f'''{ttl('NEXORA Studio : un mot fort, <em class="hand">un geste.</em>')}
<div class="two">
<div class="txt"><p>Le nom fonctionne comme un titre de montage : <b>un mot fort, puis une écriture à la main</b>. NEXORA pose la marque, nette et solide. « Studio » ajoute la main de ceux qui fabriquent.</p>
<p>On écrit toujours <b>NEXORA Studio</b> : NEXORA en capitales, Studio avec une seule capitale. Dans une phrase, on ne dit pas « le studio NEXORA Studio » : on dit « NEXORA Studio » ou « le studio ».</p></div>
<div class="nm"><div class="ok"><span class="mono acc">Oui</span><b>NEXORA Studio</b></div><div class="no"><span class="mono">Non</span><b>Nexora studio · NEXORA STUDIO · Nexora-Studio · NXS</b></div></div>
</div>'''))
# 08 logo principal
P.append(page(8, 'dark', 'Le logo', f'''<div class="hero-logo">{logo('xl')}</div>
<p class="mono cap-b">Logo principal · NEXORA en os, « Studio » en braise, sur encre</p>''', 'center'))
# 09 construction
cap_h = BASE - CAPTOP
guides = (f'<g stroke="{BRAISE}" stroke-width="6" stroke-dasharray="30 22" fill="none" opacity=".9">'
          f'<line x1="{X0-200}" y1="{CAPTOP}" x2="{X0+W+200}" y2="{CAPTOP}"/><line x1="{X0-200}" y1="{BASE}" x2="{X0+W+200}" y2="{BASE}"/></g>')
notes = [('Haut des capitales', 'NEXORA en Unbounded, graisse 700, approche −35 unités'), ('Ligne de base', '« Studio » recouvre le bas du mot sur environ un tiers de la hauteur des capitales'),
         ('« Studio »', 'Mr Dafoe, même corps que NEXORA, posé à plat, aligné à droite, dépasse légèrement le A'), ('Le E', 'Redessiné avec un fût droit, de la même épaisseur que les autres lettres (voir page suivante)')]
P.append(page(9, 'dark', 'Le logo', f'''{ttl('Construction')}
<div class="cons">{logo('lg2', extra=guides)}</div>
<div class="grid4 sm">{''.join(f'<div class="card"><b>{a}</b><span>{b}</span></div>' for a, b in notes)}</div>
<p class="mono foot">Tracés vectoriels : 13-NEXORA-STUDIO/sources/gen.py. Le logo ne se recompose jamais à la main avec les polices.</p>'''))
# 10 le E
P.append(page(10, 'light', 'Le logo', f'''{ttl('Le E redessiné', 'Le E de l’Unbounded a un fût pincé en son milieu. Dans le logo et le grand mot du site, il est remplacé par un E droit, de la même épaisseur que les autres lettres.')}
<div class="ecmp"><div><span class="ue">E</span><span class="mono">Unbounded d’origine · fût pincé</span></div>
<div>{E_custom(ENCRE, 300)}<span class="mono acc-p">NEXORA Studio · fût droit</span></div></div>
<p class="mono foot">Dans les titres courants, le E de l’Unbounded reste tel quel : trop petit pour gêner.</p>'''))
# 11 protection
pad = cap_h * 0.5
box = f'<rect x="{X0-pad}" y="{Y0-pad}" width="{W+2*pad}" height="{H+2*pad}" fill="none" stroke="{BRAISE}" stroke-width="7" stroke-dasharray="26 20"/>'
P.append(page(11, 'dark', 'Le logo', f'''{ttl('Zone de protection et tailles minimales')}
<div class="two">
<div class="prot">{logo('lg3', extra=box)}</div>
<div class="txt"><p><b>Zone libre.</b> Une marge égale à la moitié de la hauteur des capitales de NEXORA, sur tout le pourtour. Rien n’y entre : texte, image ou bord de page.</p>
<p><b>Taille minimale.</b> 120 px de large à l’écran (le site l’affiche autour de 140 px), 30 mm à l’impression.</p>
<p><b>En dessous</b>, on utilise le symbole N + S.</p>
<div class="minis">{logo('m1')}<span class="mono">140 px</span>{logo('m2')}<span class="mono">120 px</span></div></div>
</div>'''))
# 12 versions
vers = [('Sur encre', ENCRE, OS, BRAISE, 'Version principale.'), ('Sur os', OS, ENCRE, BRAISE_P, '« Studio » passe en braise profonde.'),
        ('Sur braise', BRAISE, ENCRE, ENCRE, 'Tout en encre.'), ('Sur braise, grand format', BRAISE, ENCRE, OS, 'Studio en os, seulement en très grand (couverture, fin de document).'),
        ('Monochrome encre', '#FFFFFF', ENCRE, ENCRE, 'Impression une couleur, tampon, gravure.'), ('Monochrome os', '#161412', OS, OS, 'Sur photo sombre ou fond charbon.')]
P.append(page(12, 'light', 'Le logo', f'''{ttl('Versions')}
<div class="vers">{''.join(f'<div><div class="vt" style="background:{bg}">{logo("v", word=w, studio=s)}</div><b>{n}</b><span>{d}</span></div>' for n, bg, w, s, d in vers)}</div>'''))
# 13 symbole
P.append(page(13, 'dark', 'Le symbole', f'''{ttl('Le symbole N + S')}
<div class="symrow">
<div class="symbig">{symbol(420)}</div>
<div class="txt"><p>Le N de NEXORA, traversé par le S manuscrit de « Studio ». Un contour de la couleur du fond détache le S du N.</p>
<p><b>Usages :</b> favicon, avatar des réseaux, icône d’application, filigrane de vidéo, tout espace trop petit pour le logo complet.</p>
<div class="syms"><div style="border-radius:50%;overflow:hidden;width:180px;height:180px">{symbol(180, r=0)}</div>{symbol(180, OS, ENCRE, BRAISE_P)}
<div class="favs">{symbol(64)}{symbol(32, r=7)}{symbol(16, r=4)}</div></div>
<p class="mono foot2">Avatar rond · icône sur os · favicon 64, 32, 16</p></div></div>'''))
# 14 interdits
def tile_bad(inner, label, bg=ENCRE):
    return f'<div><div class="vt bad" style="background:{bg}">{inner}<i class="xx" aria-hidden="true"></i></div><span>{label}</span></div>'
rot = logo('v', extra='').replace(f'<path class="st" d="{L["studio"]}"/>', f'<path class="st" d="{L["studio"]}" transform="rotate(-9 3600 1150)"/>')
bad = [tile_bad(rot, 'Pencher « Studio »'),
       tile_bad('<div class="fake">NEXORA <span class="hand">Studio</span></div>', 'Recomposer le logo avec les polices'),
       tile_bad(logo('v', word=ENCRE, studio=BRAISE), 'Braise sur os', OS),
       tile_bad(logo('v', style='transform:scaleX(1.35)'), 'Déformer'),
       tile_bad(logo('v', style='filter:drop-shadow(0 12px 10px rgba(255,74,28,.8))'), 'Ajouter un effet'),
       tile_bad(f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px"><span class="hand" style="font-size:46px;color:{BRAISE}">Studio</span><span style="font-family:Unbounded;font-weight:700;font-size:40px;color:{OS}">NEXORA</span></div>', 'Déplacer « Studio »')]
P.append(page(14, 'light', 'Usages interdits', f'''{ttl('Usages interdits')}<div class="vers">{''.join(bad)}</div>'''))
# 15-17 couleurs
def cmyk(hx):
    r, g, b = (int(hx[i:i+2], 16) / 255 for i in (1, 3, 5)); k = 1 - max(r, g, b)
    if k >= 1: return '0 · 0 · 0 · 100'
    return ' · '.join(str(round(v * 100)) for v in ((1-r-k)/(1-k), (1-g-k)/(1-k), (1-b-k)/(1-k), k))
def rgb(hx): return ', '.join(str(int(hx[i:i+2], 16)) for i in (1, 3, 5))
main = [('Encre', ENCRE, 'Fond principal ; texte sur fond clair et sur braise', OS), ('Os', OS, 'Texte sur fond sombre ; fond des sections claires', ENCRE), ('Braise', BRAISE, 'Accent : action principale, « Studio », contact', ENCRE)]
P.append(page(15, 'dark', 'Les couleurs', f'''{ttl('Palette principale')}
<div class="sw3">{''.join(f'<div class="sw" style="background:{h};color:{t}"><b>{n}</b><span class="mono">{h}</span><span class="mono">RVB {rgb(h)}</span><span class="mono">CMJN {cmyk(h)}</span><em>{r}</em></div>' for n, h, r, t in main)}</div>
<p class="mono foot">CMJN calculé à titre indicatif : à valider avec l’imprimeur sur épreuve. Proportions : encre 62 %, os 24 %, braise 10 %, le reste 4 %.</p>'''))
sec = [('Braise profonde', '#B02F0B', 'Accent sur fond os ; « Studio » sur os'), ('Rouille', '#7A2410', 'Illustration, lueur'), ('Braise sombre', '#5C1A09', 'Lueur du hero, profondeur'), ('Braise nuit', '#3A1206', 'Texte secondaire sur braise'),
       ('Charbon', '#161412', 'Surfaces sur encre'), ('Cendre', '#3A3631', 'Éléments inactifs'), ('Pierre', '#9A9386', 'Texte secondaire sur encre'), ('Terre', '#4F493F', 'Texte secondaire sur os'), ('Sable', '#E2DACB', 'Surfaces sur os')]
P.append(page(16, 'light', 'Les couleurs', f'''{ttl('Déclinaisons et neutres')}
<div class="sw9">{''.join(f'<div><div class="chip" style="background:{h}"></div><b>{n}</b><span class="mono">{h}</span><span>{r}</span></div>' for n, h, r in sec)}</div>'''))
con = [('Os', 'Encre', '15,6:1', True), ('Braise', 'Encre', '5,81:1', True), ('Pierre', 'Encre', '6,41:1', True), ('Encre', 'Os', '15,6:1', True), ('Braise profonde', 'Os', '5,15:1', True),
       ('Terre', 'Os', '7,11:1', True), ('Encre', 'Braise', '5,81:1', True), ('Braise', 'Os', '2,68:1', False), ('Os', 'Braise', '2,68:1', False)]
P.append(page(17, 'dark', 'Les couleurs', f'''{ttl('Contrastes et règle d’or', 'La braise ne se pose jamais sur l’os, ni l’os sur la braise, pour un texte. Sur fond os, l’accent devient la braise profonde. Sur fond braise, tout passe en encre.')}
<table class="ct"><thead><tr><th>Texte</th><th>Fond</th><th>Rapport</th><th>Lisible (WCAG AA)</th></tr></thead><tbody>
{''.join(f'<tr class="{"" if ok else "ko"}"><td>{a}</td><td>{b}</td><td>{r}</td><td>{"Oui" if ok else "Non"}</td></tr>' for a, b, r, ok in con)}</tbody></table>'''))
# 18-19 typographies
fam = [('Unbounded', "'Unbounded'", 700, 'Titres, grand mot, chiffres de prix', 'Aa Bb 0123', 'Graisses 600 et 700. Jamais en 900.'),
       ('Mr Dafoe', "'Mr Dafoe'", 400, 'Le geste manuscrit : « Studio » et un mot d’accent', 'les marques.', 'Une seule graisse. Jamais en capitales, jamais en italique ajouté.'),
       ('Archivo', "'Archivo'", 400, 'Texte courant, boutons, formulaires', 'Texte courant', 'Largeur normale. Graisses 400 à 600.'),
       ('JetBrains Mono', "'JetBrains Mono'", 500, 'Données, repères, légendes en capitales', 'MOTION · 2026', 'Corps 12 à 14 px, espacé de 8 %.')]
P.append(page(18, 'light', 'Les typographies', f'''{ttl('Quatre familles, quatre rôles')}
<div class="fams">{''.join(f'<div><span class="spec" style="font-family:{f};font-weight:{w}">{s}</span><b>{n}</b><span>{r}</span><span class="mono">{x}</span></div>' for n, f, w, r, s, x in fam)}</div>
<p class="mono foot">Toutes gratuites sur Google Fonts, licence SIL Open Font : site, vidéos, documents et impression.</p>'''))
scale = [('Grand mot', 'Unbounded 700', 'largeur de l’écran', "font-family:Unbounded;font-weight:700;font-size:96px;letter-spacing:-.01em;line-height:.9", 'NEXORA'),
         ('Titre de section', 'Unbounded 700 · 38 à 96 px', 'interligne 0,96 · approche −2,5 %', "font-family:Unbounded;font-weight:700;font-size:64px;letter-spacing:-.025em;line-height:.96", 'Du brief à l’image.'),
         ('Titre de carte', 'Unbounded 700 · 32 à 58 px', 'interligne 0,98 · approche −2 %', "font-family:Unbounded;font-weight:700;font-size:44px;letter-spacing:-.02em", 'Mara Academy'),
         ('Accroche', 'Unbounded 600 · 27 à 45 px', 'interligne 1,06', "font-family:Unbounded;font-weight:600;font-size:34px;letter-spacing:-.025em", 'Nous faisons bouger'),
         ('Geste', 'Mr Dafoe · 34 à 40 px', '1,2 fois le texte voisin', f"font-family:'Mr Dafoe';font-size:46px;color:{BRAISE_P}", 'les marques.'),
         ('Texte', 'Archivo 400 · 16 à 18 px', 'interligne 1,6', "font-family:Archivo;font-size:18px", 'Un premier échange pour comprendre votre marque, votre public et ce que le projet doit accomplir.'),
         ('Donnée', 'JetBrains Mono 500 · 12 à 14 px', 'capitales, espacé de 8 %', "font-family:'JetBrains Mono';font-weight:500;font-size:14px;letter-spacing:.08em;text-transform:uppercase", 'Étape 1 sur 4')]
P.append(page(19, 'light', 'Les typographies', f'''{ttl('Échelle')}
<div class="scale">{''.join(f'<div><span class="mono">{n}</span><span class="sp" style="{st}">{ex}</span><span class="sz">{a}<br>{b}</span></div>' for n, a, b, st, ex in scale)}</div>'''))
# 20 geste manuscrit
gr = [('Un à quatre mots', 'Jamais une phrase entière à lire, jamais un paragraphe, un prix ou une adresse.'), ('Une fois par composition', 'Un seul geste par page, par écran ou par visuel.'),
      ('En couleur d’accent', 'Braise sur encre, braise profonde sur os, encre sur braise.'), ('Plus grand que le texte voisin', 'Environ 1,2 fois le titre qu’il accompagne : son œil est plus petit.'),
      ('À plat', 'Pas de rotation : « Studio » ne penche jamais.'), ('Jamais en capitales', 'Mr Dafoe ne s’écrit qu’en minuscules, avec une capitale initiale au plus.')]
P.append(page(20, 'dark', 'Le geste manuscrit', f'''{ttl('Le geste manuscrit')}
<div class="two"><div class="ex"><span class="ux">Nous faisons bouger</span><span class="hand gx">les marques.</span>
<span class="ux" style="margin-top:46px">Un projet ?</span><span class="hand gx">Mettons-le en mouvement.</span></div>
<ul class="lst">{''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in gr)}</ul></div>'''))
# 21 image et mouvement
mv = [('« Studio » s’écrit', 'Après l’arrivée des lettres, « Studio » se dévoile de gauche à droite en 1,3 s.'), ('Les images s’ouvrent', 'Elles apparaissent en rideau, de bas en haut, en 1,2 s.'),
      ('Les vidéos jouent à l’écran', 'Extraits muets en boucle, lancés seulement quand ils sont visibles.'), ('Le mouvement réduit est respecté', 'Si le visiteur l’a demandé, tout s’affiche sans animation.')]
P.append(page(21, 'dark', 'Image et mouvement', f'''{ttl('Image et mouvement')}
<div class="two"><figure class="shot"><img src="{IMG}/site-accueil.jpg" alt=""><figcaption class="mono">La sculpture 3D du X, image d’ouverture du site</figcaption></figure>
<ul class="lst">{''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in mv)}</ul></div>'''))
# 22-24 applications
P.append(page(22, 'dark', 'Applications', f'''{ttl('Le site')}
<div class="apps"><figure class="shot big"><img src="{IMG}/site-accueil.jpg" alt=""></figure>
<figure class="shot mob"><img src="{IMG}/site-mobile.jpg" alt=""></figure>
<figure class="shot"><img src="{IMG}/site-realisations.jpg" alt=""></figure><figure class="shot"><img src="{IMG}/site-studio.jpg" alt=""></figure></div>'''))
P.append(page(23, 'light', 'Applications', f'''{ttl('Les documents')}
<div class="docs">{''.join(f'<figure class="shot"><img src="{IMG}/catalogue-{p}.jpg" alt=""></figure>' for p in ('p01', 'p04', 'p12', 'p15'))}</div>
<p class="mono foot">Catalogue NEXORA Studio 2026 : couverture, page de projet, tarifs, contact.</p>'''))
P.append(page(24, 'dark', 'Applications', f'''{ttl('Réseaux et vidéo')}
<div class="soc">
<div><div class="endc">{logo('ec')}<span class="mono">Motion design · Sites web · Cotonou</span></div><span class="mono">Fin de vidéo, 16:9</span></div>
<div class="wide"><figure class="shot"><img src="{IMG}/partage.jpg" alt=""></figure><span class="mono">Image de partage du lien (WhatsApp, réseaux)</span></div>
<div><div style="width:240px;height:240px;border-radius:50%;overflow:hidden">{symbol(240, r=0)}</div><span class="mono">Avatar</span></div>
<div><div class="lt"><b>LE NOUVEAU CODE</b><span class="hand">de la route</span></div><span class="mono">Sous-titre de montage</span></div>
</div>'''))
# 25 fichiers
files = [('01-BRAND-BOOK', 'Ce document en PDF et en Markdown ; la version 1 est archivée.'), ('02-LOGO-BRAND-ASSETS/svg et png', '8 versions du logo et 4 du symbole N + S, en vectoriel et en PNG 2048 px.'),
         ('02-LOGO-BRAND-ASSETS/favicon', 'favicon.ico, favicon.svg, PNG 16, 32, 48, 180 (Apple), 192 et 512.'), ('03-COLOR-PALETTE-TYPOGRAPHY', 'Planches couleurs, typographies et logo en PNG.'),
         ('05-DESIGN-TOKENS-SOURCE-FILES', 'Couleurs et typographies en CSS et JSON, composant du logo pour le site.'), ('13-NEXORA-STUDIO/sources', 'Le générateur des tracés du logo et ses mesures.')]
P.append(page(25, 'light', 'Fichiers livrés', f'''{ttl('Fichiers livrés')}
<ul class="files">{''.join(f'<li><span class="mono">{a}</span><span>{b}</span></li>' for a, b in files)}</ul>
<div class="endmark">{logo('lg4')}</div>'''))

HTML = (f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>NEXORA Studio, Brand Book v2.0</title>'
        f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600&family=Unbounded:wght@400;600;700&family=Mr+Dafoe&family=JetBrains+Mono:wght@400;500&display=swap">'
        f'<link rel="stylesheet" href="bb.css"></head><body>{"".join(P)}</body></html>')
assert len(P) == NPAGES, len(P)
open(os.path.join(HERE, 'brandbook.html'), 'w').write(fr_typo(HTML))
print('ok', len(P))
