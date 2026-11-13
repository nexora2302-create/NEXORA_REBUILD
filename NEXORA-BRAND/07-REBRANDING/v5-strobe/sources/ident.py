import os, sys, math, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from marks5 import symbol, favicon, wordmark, halves, svg, wm, sym, R, G, D
from typo import fr_typo
sp = importlib.util.spec_from_file_location('m1', os.path.join(HERE, '..', '..', 'v2', 'sources', 'marks.py'))
m1 = importlib.util.module_from_spec(sp); sp.loader.exec_module(m1)
CSS = open(os.path.join(HERE, 'base5.css')).read() + open(os.path.join(HERE, 'ident.css')).read()
N, P, A, AB = '#0F0F11', '#F1F1EE', '#FFAE42', '#7A4205'

# ---------- pistes ----------
def p_slit_only(fg):
    t, b = halves(); return f'<path fill="{fg}" d="{t}"/><path fill="{fg}" d="{b}"/>'
def p_ring(fg):
    out = f'<circle cx="50" cy="50" r="34" fill="{fg}"/>'
    for i in range(12):
        out += f'<rect x="48.3" y="17" width="3.4" height="11" rx="1" fill="var(--bg)" transform="rotate({i*30} 50 50)"/>'
    return out
def p_chrono(fg):
    return ''.join(f'<g opacity="{o}" transform="translate({dx} 0) scale(.62) translate(30 30)">{symbol(fg)}</g>' for dx, o in ((-26, .16), (-13, .4), (0, 1)))
def echo_wm(fg):
    i, w, h = wordmark(fg)
    return svg(''.join(f'<g opacity="{o}" transform="translate({dx} 0)">{i}</g>' for dx, o in ((-260, .14), (-130, .36), (0, 1))), f'-320 0 {w+380:.0f} {h}', 'wm', 'Strobe, écho')
PISTES = [
 ('1', 'Disque décalé (v1)', svg(m1.symbol('currentColor'), '0 0 100 100', 'sy', 'v1'), 'Un disque coupé, moitiés glissées. Lu comme un tilde à 16 px ; la famille des cercles coupés est très peuplée.', 'RETRAVAILLER', 'mid'),
 ('2', 'Disque à fente', sym(), 'Le même disque, ouvert par une fente de visée : on regarde à travers (skopein), et ce qu’on voit a bougé (strobos). Deux formes nettes, lisibles à 16 px.', 'RETENU', 'acc'),
 ('3', 'Disque stroboscopique', svg(p_ring('currentColor'), '0 0 100 100', 'sy', ''), 'Le disque de 1833 réduit à 12 fentes. Juste historiquement, mais il devient une roue dentée à 16 px.', 'JETER', 'ko'),
 ('4', 'Écho du logotype', echo_wm('currentColor'), 'Le mot et deux traces, comme une multi-exposition. Superbe en mouvement, illisible en petit : c’est un dispositif, pas un logo.', 'GARDER EN DISPOSITIF', 'ok'),
 ('5', 'Fente seule', svg(p_slit_only('currentColor'), '0 0 100 100', 'sy', ''), 'Le disque fendu sans décalage : immobile, il ne raconte plus le mouvement, et rappelle un bouton.', 'JETER', 'ko'),
 ('6', 'Chronophotographie', svg(p_chrono('currentColor'), '0 0 100 100', 'sy', ''), 'Trois positions du symbole. Très parlant, mais trois formes de trop pour un avatar ; réservé à l’animation.', 'GARDER EN ANIMATION', 'ok'),
]
pistes = ''.join(f'<article class="pi{" win" if c == "acc" else ""}"><div class="pv">{s}</div><div class="pt"><p class="eyebrow">Piste {k}</p><h3 class="d3">{t}</h3><p>{d}</p><span class="tag t-{c}">{v}</span></div></article>' for k, t, s, d, v, c in PISTES)

# ---------- audit ----------
AUD = [
 ('Symbole (disque décalé)', 'Oui', 'Ambigu (tilde)', 'Oui', 'Oui', 6, 'RETRAVAILLER', 'mid', 'Le principe tient (un objet, deux instants). Il lui manque le regard : la fente.'),
 ('Logotype (O = disque plein)', '·', 'Non', 'Oui', 'Oui', 5, 'RETRAVAILLER', 'mid', 'Un O plein se lit mal ; on lisait parfois « STR-BE ». Le O devient un anneau fendu.'),
 ('Palette (xénon sur noir)', '·', '·', '·', '·', 4, 'JETER', 'ko', 'Cyan électrique sur noir : le code couleur du « tech » et des visuels de club. Confirmé.'),
 ('Anybody 900, largeur 125', '·', '·', '·', '·', 6, 'RETRAVAILLER', 'mid', 'Trop affiche de soirée. Passe en 800, largeur 112,5 : la même voix, plus posée.'),
 ('Schibsted Grotesk (texte)', '·', '·', '·', '·', 8, 'GARDER', 'ok', 'Lisible, chaleureux, peu vu.'),
 ('Martian Mono (données)', '·', '·', '·', '·', 7, 'GARDER', 'ok', 'Devient la voix des numéros d’image (07/12), comme sur une planche de Muybridge.'),
 ('Direction artistique', '·', '·', '·', '·', 5, 'RETRAVAILLER', 'mid', '« Salle noire, flash » : penchait scène et soirée. Devient « l’instant net, l’écho, la planche ».'),
 ('Motion (le flash, 900 ms)', '·', '·', '·', '·', 6, 'RETRAVAILLER', 'mid', 'Un flash blanc, même unique, reste le geste du club. Remplacé par l’arrêt à 12 images par seconde.'),
 ('« Ça marque. / Burned in. »', '·', '·', '·', '·', 8, 'GARDER', 'ok', 'Toujours juste. Une ligne plus profonde est proposée en parallèle.'),
]
aud = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td><td class="n">{f}/10</td><td><span class="tag t-{h}">{g}</span></td><td>{i}</td></tr>' for a, b, c, d, e, f, g, h, i in AUD)
REFS = [('Buck', 'motion'), ('ManvsMachine', 'motion, 3D'), ('Studio Dumbar', 'identités en mouvement'), ('Porto Rocha', 'typographie cinétique'), ('DixonBaxi', 'identités pour l’écran'), ('Koto', 'systèmes de marque'), ('Moment Factory', 'expériences lumière et son'), ('United Visual Artists', 'installations lumière')]
refs = ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in REFS)

# ---------- histoire ----------
FACTS = [
 ('« Stroboscope » vient du grec strobos (tourbillon, action de tournoyer) et skopein (regarder).', 'Sûr'),
 ('Fin 1832 et début 1833, Joseph Plateau (Belgique) et Simon Stampfer (Autriche) conçoivent presque en même temps un disque à fentes qui, tournant devant un miroir, change des dessins fixes en mouvement. Plateau publie en janvier 1833.', 'Sûr'),
 ('Stampfer appelle ses disques « stroboscopische Scheiben », disques stroboscopiques ; brevet autrichien du 7 mai 1833.', 'Sûr'),
 ('Ces disques sont parmi les premiers appareils d’animation à large diffusion. Les appeler « la première animation » est plus fort que ce que disent les sources.', 'Sûr (nuance)'),
 ('1878 : Eadweard Muybridge photographie un cheval au galop avec une rangée d’appareils déclenchés par des fils.', 'Sûr'),
 ('Étienne-Jules Marey enregistre le mouvement sur une plaque derrière des disques à fentes tournants.', 'Sûr'),
 ('Le « fusil photographique » de Marey date de 1882.', 'Probable, à vérifier'),
 ('Vers 1931, au MIT, Harold Edgerton met au point un flash électronique répétitif ; il photographie des gouttes de lait dès 1932 ; « Milk Drop Coronet » date de 1957. Il n’a jamais revendiqué l’invention du stroboscope.', 'Sûr'),
]
facts = ''.join(f'<li><span class="tag t-{"ok" if c.startswith("Sûr") else "mid"}">{c}</span><p>{t}</p></li>' for t, c in FACTS)

# ---------- palettes ----------
SCALE_B = [('Argentique 900', '#1A1A1D'), ('800', '#26262A'), ('700', '#3E3D39'), ('500', '#64625C'), ('400', '#8E8B84'), ('300', '#B9B6AE'), ('100', '#E8E6E0')]
SCALE_A = [('Ardoise 900', '#16181B'), ('800', '#22262A'), ('700', '#353A40'), ('500', '#555B62'), ('400', '#7F868D'), ('300', '#AEB4B9'), ('100', '#E3E6E8')]
def scale(sc): return '<div class="scale">' + ''.join(f'<div style="background:{h};color:{"#F1F1EE" if i < 4 else "#0F0F11"}"><b>{n}</b><code>{h}</code></div>' for i, (n, h) in enumerate(sc)) + '</div>'
def pal(name, sub, rec, mains, sc, rows, photo):
    m = ''.join(f'<div class="pm" style="background:{h};color:{c}"><b>{n}</b><code>{h}</code><span class="pp">{r}</span><span>{d}</span><span class="ct">{ct}</span></div>' for n, h, c, r, d, ct in mains)
    return f'''<article class="palx{" rec" if rec else ""}"><header><p class="eyebrow">{sub}</p><h3 class="d2">{name}</h3>{"<span class='tag t-acc'>Recommandée</span>" if rec else ""}</header>
<div class="pms">{m}</div><p class="eyebrow">Famille de nuances</p>{scale(sc)}
<div class="tbl"><table><tbody>{rows}</tbody></table></div><p class="small">{photo}</p></article>'''
rowsB = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in [('Ratio', 'Chambre noire 60 · Argentique 30 · Ambre 10. En document clair : Plaque 60 · Argentique 30 · Ambre brûlé 10.'), ('Texte', 'Plaque sur chambre noire 16,9:1 · Ambre sur chambre noire 10,4:1 · Ambre brûlé #7A4205 sur plaque 7,1:1 · Argentique 400 sur chambre noire 5,6:1 · Argentique 500 sur plaque 5,4:1'), ('Jamais', 'Ambre en texte sur fond clair (1,6:1) ; ambre et violet ensemble ; dégradé d’ambre vers une autre teinte.'), ('Dégradés', 'Uniquement dans la famille argentique, du 900 au 700 : de la profondeur, jamais de la couleur.'), ('États', 'Survol : argentique 800 → 700. Actif : ambre. Désactivé : argentique 500.')])
rowsA = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in [('Ratio', 'Chambre noire 60 · Ardoise 30 · Xénon pâle 10'), ('Texte', 'Xénon pâle sur noir 13,3:1 · Xénon profond #1F6E7A sur clair 5,2:1'), ('Limite', 'Même désaturé, le cyan sur noir reste lu « tech ». C’est une évolution prudente, pas une identité.')])
palB = pal('Révélateur', 'Palette B · rupture assumée', True,
  [('Chambre noire', N, P, '60 %', 'Le fond profond : la chambre noire où l’image apparaît.', 'Plaque dessus : 16,9:1'),
   ('Ambre', A, N, '10 %', 'La lumière inactinique de la chambre noire, sous laquelle l’instant devient visible. La signature.', 'Sur chambre noire : 10,4:1')],
  SCALE_B, rowsB, 'Sur photo : logo en plaque #F1F1EE sur image sombre, en chambre noire sur image claire ; ambre seulement sur une zone calme et sombre. Sur vidéo : ambre pour les titres et les synthés, plaque pour les sous-titres ; valeurs à contrôler dans l’espace légal Rec. 709 avant diffusion télé.')
palA = pal('Xénon apaisé', 'Palette A · évolution', False,
  [('Chambre noire', N, P, '60 %', 'Inchangé.', ''), ('Xénon pâle', '#9AE3EE', N, '10 %', 'Le cyan v1, désaturé.', 'Sur noir : 13,3:1')], SCALE_A, rowsA, 'Fonctionne sur vidéo, mais s’effondre sur photo chaude et reste dans le territoire du « tech ».')

# ---------- variantes ----------
seal_text = 'STROBE · COTONOU · MOTION · BRAND · WEB · '
seal = f'''<svg class="sy seal" viewBox="0 0 100 100" role="img" aria-label="Sceau Strobe"><defs><path id="sc" d="M50 50m-38 0a38 38 0 1 1 76 0a38 38 0 1 1 -76 0"/></defs>
<text font-family="Martian Mono, monospace" font-size="6.3" letter-spacing="1.6" fill="currentColor"><textPath href="#sc">{seal_text}</textPath></text>
<g transform="translate(25 25) scale(.5)">{symbol('currentColor')}</g></svg>'''
def lock(fg='currentColor', acc='var(--acc)', cls='lock'): return f'<span class="{cls}">{sym(acc)}{wm(fg, acc)}</span>'
def pole(name, sec=False): return f'<span class="pole{" sec" if sec else ""}">{wm("currentColor", "var(--acc)")}<i></i><b>{name}</b></span>'
VAR = [
 ('Principal horizontal', f'<div class="vb dk wide">{lock(P, A)}</div>'),
 ('Compact, empilé', f'<div class="vb dk"><span class="stack">{sym(A)}{wm(P, A)}</span></div>'),
 ('Icône seule', f'<div class="vb dk">{sym(A)}</div>'),
 ('Logotype seul', f'<div class="vb lt bd wide">{wm(N, AB)}</div>'),
 ('Monochrome', f'<div class="vb lt bd">{lock(N, N)}</div>'),
 ('Négatif', f'<div class="vb dk">{lock(P, P)}</div>'),
 ('Une couleur (ambre)', f'<div class="vb dk">{lock(A, A)}</div>'),
 ('Sceau, filigrane', f'<div class="vb lt bd">{seal}</div>'),
 ('Favicon 12 et 16 px', f'<div class="vb lt bd fav">{svg(favicon(N), "0 0 100 100", "f12", "Favicon 12 px")}{svg(favicon(N), "0 0 100 100", "f16", "Favicon 16 px")}{svg(favicon(N), "0 0 100 100", "f32", "Favicon 32 px")}</div>'),
 ('Avatar', f'<div class="vb lt bd"><span class="av">{sym(A)}</span></div>'),
]
var = ''.join(f'<figure class="vf">{b}<figcaption>{t}</figcaption></figure>' for t, b in VAR)
poles = f'<div class="poles dk">{pole("Motion")}{pole("Brand")}{pole("Web")}{pole("Live", True)}</div>'

# construction
r, g, d = R, G, D
cons = f'''<svg class="cons" viewBox="-6 -6 112 112" role="img" aria-label="Construction du symbole">
<g stroke="var(--rule)" stroke-width=".3">{''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="100"/>' for x in range(0, 101, 10))}{''.join(f'<line x1="0" y1="{y}" x2="100" y2="{y}"/>' for y in range(0, 101, 10))}</g>
<circle cx="{50-d}" cy="50" r="{r}" fill="none" stroke="var(--mut)" stroke-width=".35" stroke-dasharray="1.2 1"/><circle cx="{50+d}" cy="50" r="{r}" fill="none" stroke="var(--mut)" stroke-width=".35" stroke-dasharray="1.2 1"/>
<g opacity=".95">{symbol('var(--fg)')}</g>
<rect x="0" y="{50-g/2}" width="100" height="{g}" fill="var(--acc)" opacity=".28"/>
<g class="cl"><text x="-5" y="-1.5">r 36,5 (36 + 0,5 de compensation)</text><text x="-5" y="104">fente 6,6 · décalage 5,6 par moitié</text><text x="72" y="48">fente</text></g></svg>'''
KERN = [('S · T', '−30'), ('T · R', '−40'), ('R · O', '+40'), ('O · B', '+40'), ('B · E', '−10'), ('Approche générale', '+20')]
kern = ''.join(f'<tr><th scope="row">{a}</th><td class="n">{b}</td></tr>' for a, b in KERN)

# ---------- applications ----------
APPS = f'''
<figure><div class="ap car dk"><span class="cn mono">01/05</span>{sym(A, 'sy cs')}<p class="ct2">On arrête le mouvement<br>pour le faire voir.</p><span class="cw">{wm(P, A)}</span></div><figcaption>Couverture de carrousel 4:5</figcaption></figure>
<figure><div class="ap title dk"><span class="tcn mono">SC 04 · 12 i/s</span><div class="echo">{''.join(f'<span style="opacity:{o};transform:translateX({x}%)">{wm(P, A)}</span>' for x, o in ((-6, .12), (-3, .35), (0, 1)))}</div><p class="mono tsub">Film de marque · exemple</p></div><figcaption>Carton-titre vidéo 16:9, avec l’écho</figcaption></figure>
<figure><div class="ap kak dk"><span class="kw">{wm(P, A)}</span><p class="kl">Ça<br>marque.</p><span class="kchrono">{''.join(f'<span style="opacity:{o}">{sym(A)}</span>' for o in (.15, .4, 1))}</span><p class="mono ku">strobe.design</p></div><figcaption>Kakémono d’événement 80 × 200</figcaption></figure>
<figure><div class="ap hero lt bd"><div class="hbar">{lock(N, AB)}<span class="mono">Motion · Brand · Web</span></div><p class="hh">L’arrêt,<br>puis la vie.</p><div class="hstrip">{''.join(f'<span><i class="mono">{k:02d}</i></span>' for k in range(1, 7))}</div></div><figcaption>Aperçu de hero de site (planche contact)</figcaption></figure>
<figure><div class="cards"><div class="bc dk">{sym(A)}</div><div class="bc lt bd"><b>Prénom Nom</b><span>Motion design</span><span class="mono">prenom@strobe.design</span><span class="bcl">{wm(N, AB)}</span></div></div><figcaption>Carte de visite 85 × 55 (nom d’exemple)</figcaption></figure>
<figure><div class="ap avs"><span class="av dk">{sym(A)}</span><span class="av lt bd">{sym(N)}</span><span class="av" style="background:{A}">{sym(N)}</span></div><figcaption>Avatars</figcaption></figure>'''

HTML = f'''<title>Strobe v2, identité</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anybody:wdth,wght@50..150,400..900&family=Schibsted+Grotesk:ital,wght@0,400..800;1,400&family=Martian+Mono:wdth,wght@75..112.5,400..700&display=swap">
<style>{CSS}</style>
<header class="bar"><div class="wrap"><a class="lg" href="#top" aria-label="Strobe">{lock()}</a>
<nav aria-label="Parties"><a href="#audit">Audit</a><a href="#histoire">Histoire</a><a href="#logo">Logo</a><a href="#variantes">Variantes</a><a href="#palette">Palette</a><a href="#typo">Typo</a><a href="#da">Direction</a></nav>
<button class="tg" type="button" id="themeBtn">Thème</button></div></header>
<main id="top">
<section class="wrap hero0"><p class="eyebrow">Strobe · identité v2 · 13 novembre 2026</p>
<div class="h0">{sym('var(--acc)', 'sy h0s')}<div><h1 class="d1">L’arrêt,<br>puis la vie.</h1>
<p class="lead">La v1 parlait de flash et de salle noire. La v2 parle de ce que Strobe a vraiment inventé : un disque à fentes qui arrête le mouvement pour le faire voir, puis l’enchaîne pour lui donner vie. Le disque gagne une fente, le xénon laisse place à l’ambre, le flash à l’image par image.</p></div></div></section>

<section class="wrap sec" id="audit"><header><p class="eyebrow">Étape 1 · Mini-audit de la v1</p><h2 class="d2">Ce qui tient, ce qui penchait.</h2></header>
<div class="tbl"><table><thead><tr><th>Élément</th><th>Flou</th><th>16 px</th><th>Mono</th><th>Négatif</th><th>Note</th><th>Verdict</th><th>Pourquoi</th></tr></thead><tbody>{aud}</tbody></table></div>
<div class="cols"><div class="hyp"><h3 class="d3">Les trois hypothèses</h3><ul>
<li><b>Le cyan xénon sur noir est trop vu en 2026 :</b> confirmé. C’est la palette par défaut du « tech », du jeu vidéo et des visuels de club. Elle ne dit pas « studio de création ».</li>
<li><b>Le disque décalé est-il assez distinctif ?</b> À moitié. Le principe (un objet, deux instants) est fort ; le dessin seul rejoint la famille très peuplée des cercles coupés. Avec une fente de visée, il devient spécifique : il raconte le disque de 1833. À confirmer par une recherche de marques figuratives (classification de Vienne, cercles).</li>
<li><b>L’identité penchait boîte de nuit et scène :</b> confirmé. Flash blanc, salle noire, xénon, « Pas de deuxième prise » : quatre signaux d’événement pour un studio dont le cœur est le motion.</li></ul></div>
<div class="hyp"><h3 class="d3">Face à 8 studios de référence</h3><ul class="refs">{refs}</ul><p class="small">La v1 se rangeait du côté de Moment Factory et d’UVA (lumière, événement). La v2 vise le côté de Buck, ManvsMachine et Studio Dumbar : le motion et le dessin d’abord. Comparaison de positionnement, pas de logo à logo.</p></div></div></section>

<section class="wrap sec" id="histoire"><header><p class="eyebrow">Étape 2 · Profondeur de sens</p><h2 class="d2">La machine qui a inventé l’animation.</h2></header>
<div class="cols"><ol class="facts">{facts}</ol>
<div class="story"><p class="eyebrow">L’histoire, en 5 lignes</p><p>Fin 1832, deux savants, l’un belge, l’autre autrichien, font tourner un disque percé de fentes devant un miroir : des dessins immobiles se mettent à bouger. Stampfer l’appelle « disque stroboscopique », de strobos, le tourbillon, et skopein, regarder. Un siècle plus tard, le flash stroboscopique d’Edgerton fige une goutte de lait en plein vol. Arrêter le mouvement pour le faire voir, puis l’enchaîner pour qu’il vive : c’est le principe de l’animation, et c’est notre métier. Strobe, c’est ce disque.</p>
<p class="eyebrow">Ligne gardée</p><p class="d3">Ça marque. <span class="acc" lang="en">Burned in.</span></p>
<p class="eyebrow">Ligne plus profonde, proposée en parallèle</p><p class="ln">En 1833, un disque à fentes tournait devant l’œil et des images fixes se mettaient à vivre. Nous faisons le même geste : arrêter l’instant pour qu’on le voie, puis l’enchaîner pour qu’il vive.</p>
<p class="ln" lang="en">In 1833, a slotted disc spun before the eye and still pictures came to life. We make the same move: stop the moment so it can be seen, then link it so it lives.</p>
<p class="eyebrow">Version courte</p><p class="d3">L’arrêt, puis la vie. <span class="acc" lang="en">Still. Then alive.</span></p>
<p class="small">« Still » veut dire à la fois « immobile » et « encore » : still, then alive. Le français garde la séquence en deux temps, comme le disque. Les deux lignes coexistent : « Ça marque » pour la signature, « L’arrêt, puis la vie » pour le récit et le site.</p></div></div></section>

<section class="wrap sec" id="logo"><header><p class="eyebrow">Étape 3 · Logo</p><h2 class="d2">Six pistes, un disque à fente.</h2><p class="small">Interdits respectés : ni éclair, ni onde, ni objectif, ni play, ni triangle, ni globe, ni étincelle, ni néon.</p></header>
<div class="pis">{pistes}</div>
<div class="cols"><figure class="pane">{cons}<figcaption>Le disque est surcompensé de 0,5 pour que la fente ne l’amincisse pas à l’œil. La fente fait 9 % du diamètre : sous ce seuil, elle se ferme à 24 px. Chaque moitié glisse de 5,6 : assez pour lire le mouvement, pas assez pour casser le disque.</figcaption></figure>
<div class="dec"><h3 class="d3">Les décisions</h3><ul>
<li><b>Le disque à fente remplace le disque décalé.</b> Avant : un disque coupé. Après : un disque ouvert par une fente de visée. Pourquoi : il gagne le regard (skopein), se lit mieux en petit, et ne ressemble plus à un cercle coupé générique.</li>
<li><b>Il vit seul, et le O devient son anneau.</b> Avant : le O était un disque plein, qui cassait la lecture. Après : un anneau fendu, de même épaisseur que les lettres. Le mot se lit STROBE, et le symbole vit seul en icône.</li>
<li><b>L’écho et la chronophotographie deviennent des dispositifs</b>, pas des logos : réservés au mouvement et aux grands formats.</li></ul>
<div class="tbl"><table><thead><tr><th>Crénage fait main (unités, capitale = 1 350)</th><th>Valeur</th></tr></thead><tbody>{kern}</tbody></table></div></div></div></section>

<section class="wrap sec" id="variantes"><header><p class="eyebrow">Étape 3 · Système de variantes</p><h2 class="d2">Un disque, dix usages.</h2></header>
<div class="vars">{var}</div>
<p class="eyebrow">Lockups par pôle</p>{poles}
<div class="grid rules3"><article><h3 class="d3">Zone de protection</h3><p>Quatre hauteurs de fente autour du symbole et du logo. Rien n’y entre.</p></article><article><h3 class="d3">Tailles minimales</h3><p>Symbole : 16 px (12 px avec la version favicon, fente agrandie). Logo horizontal : 96 px ou 25 mm de large.</p></article><article><h3 class="d3">Trois interdits</h3><p>Refermer la fente. Décaler les moitiés dans l’autre sens ou les colorer différemment. Ajouter une lueur, un néon ou un reflet.</p></article></div></section>

<section class="wrap sec" id="palette"><header><p class="eyebrow">Étape 4 · Palette</p><h2 class="d2">Chambre noire, ambre, argentique.</h2>
<p class="small">Avant : noir, blanc flash et xénon cyan. Après : deux couleurs principales (chambre noire et ambre) et une famille de nuances (argentique). Pourquoi : l’ambre est la lumière de la chambre noire, celle sous laquelle l’instant arrêté apparaît sur le papier. Il dit « révélation », pas « soirée ».</p></header>
<div class="pals">{palB}{palA}</div></section>

<section class="wrap sec" id="typo"><header><p class="eyebrow">Étape 5 · Typographie</p><h2 class="d2">Une voix, trois registres.</h2>
<p class="small">Avant : Anybody 900 en largeur 125. Après : Anybody 800 en largeur 112,5 pour le titrage, Schibsted Grotesk pour le texte, Martian Mono pour les numéros d’image. Pourquoi : la même famille, moins affiche de soirée, plus studio.</p></header>
<div class="spec">
<div class="sp"><p class="eyebrow">Titrage · Anybody 800, largeur 112,5 · repli Arial Black</p><p class="s1">Ça marque. Burned in.</p><p class="s2">L’arrêt, puis la vie. Still. Then alive.</p><p class="s3">Été 1833, à l’œuvre : déjà vu ? Ça déçoit rarement.</p></div>
<div class="sp"><p class="eyebrow">Texte · Schibsted Grotesk 400 à 600 · repli Helvetica Neue, Arial</p><p class="s4">Nous concevons des identités, des logos animés et des sites. Chaque projet commence par un arrêt sur image : comprendre ce qui doit être vu, puis le mettre en mouvement. Basés à Cotonou, clients partout.</p></div>
<div class="sp"><p class="eyebrow">Données · Martian Mono · repli ui-monospace, Menlo</p><p class="s5">IMG 07/12 · 12 i/s · 1/1000 s · 24 fps · TC 00:00:02:06</p></div></div>
<div class="cols"><div class="tbl"><table><thead><tr><th>Niveau</th><th>Taille / interligne</th><th>Usage</th></tr></thead><tbody>
<tr><th scope="row">Affiche</th><td class="n">144 / 0,88</td><td>Kakémono, carte de fin</td></tr><tr><th scope="row">Titre 1</th><td class="n">72 / 0,92</td><td>Hero</td></tr><tr><th scope="row">Titre 2</th><td class="n">40 / 1,0</td><td>Sections</td></tr><tr><th scope="row">Titre 3</th><td class="n">24 / 1,15</td><td>Cartes</td></tr><tr><th scope="row">Texte</th><td class="n">17 / 1,55</td><td>Courant</td></tr><tr><th scope="row">Légende</th><td class="n">13 / 1,4</td><td>Notes</td></tr><tr><th scope="row">Données</th><td class="n">11 à 12</td><td>Numéros, codes temps</td></tr></tbody></table></div>
<div class="kin"><h3 class="d3">Typographie cinétique</h3><ul><li>Les lettres apparaissent une par image, à 12 images par seconde : le rythme du disque.</li><li>La largeur passe de 100 à 112,5 au moment de l’arrêt, jamais pendant le mouvement.</li><li>Écho : deux traces au plus derrière un mot, à 35 % et 12 %, dans le sens du mouvement.</li><li>Jamais de rebond, jamais de lettre qui tourne sur elle-même, jamais de fondu enchaîné sur du texte.</li></ul></div></div></section>

<section class="wrap sec" id="da"><header><p class="eyebrow">Étape 7 · Direction artistique</p><h2 class="d2">L’instant net, l’écho, la planche.</h2></header>
<div class="grid prin">
<article><span class="mono">01/05</span><h3 class="d3">L’instant net</h3><p>Chaque image montre un instant arrêté, net, au moment exact du geste. Lumière dure, latérale, ombres franches.</p></article>
<article><span class="mono">02/05</span><h3 class="d3">L’écho, dosé</h3><p>Le dispositif signature : un sujet et ses traces (trois positions au plus, à 100, 35 et 12 %), toujours dans le sens du mouvement. Une fois par composition, jamais sur du texte courant.</p></article>
<article><span class="mono">03/05</span><h3 class="d3">La chambre noire</h3><p>Fonds profonds, sujets éclairés. L’ambre comme lumière de révélation, posée sur une seule zone. Grain argentique fin, 2 à 4 %.</p></article>
<article><span class="mono">04/05</span><h3 class="d3">La planche</h3><p>Grille de 12 colonnes, cases numérotées en Martian Mono, comme une planche contact. Le hasard est dans l’image, jamais dans la grille.</p></article>
<article><span class="mono">05/05</span><h3 class="d3">Le rythme 12 / 24</h3><p>12 images par seconde pour les moments de marque (saccadé, assumé), fluide pour l’interface et la lecture.</p></article></div>
<div class="cols"><div class="kin"><h3 class="d3">Par type d’image</h3><ul><li><b>Photo :</b> sujets en mouvement saisis net sur fond sombre ; séquences de 3 à 6 images en planche.</li><li><b>Vidéo :</b> prises nettes, vitesse d’obturation élevée ; passages à 12 i/s pour les signatures.</li><li><b>3D :</b> matières mates, une seule source de lumière, trajectoires visibles.</li><li><b>Illustration :</b> image par image, trait unique, couleurs de la palette.</li></ul>
<p class="small">Références d’inspiration : les disques de Plateau et Stampfer, les planches de Muybridge, les chronophotographies de Marey, les photos d’Edgerton. On s’en inspire ; on ne reproduit aucune image.</p></div>
<div class="kin never"><h3 class="d3">Jamais</h3><ul><li>Stroboscope de club, lasers, fumée, ambiance rave.</li><li>Glitch gratuit, lignes de balayage RGB, néon cyberpunk.</li><li>Dégradé violet-bleu, effets de lueur.</li><li>Banques d’images, poignées de main, sourires face caméra.</li><li>Folklore : wax, masques, cartes ou silhouettes du continent.</li><li>Clignotement : jamais plus de trois flashs par seconde.</li></ul></div></div>
<p class="eyebrow">Applications</p><div class="apps">{APPS}</div></section>
<p class="wrap small src">Sources : <a href="https://en.wikipedia.org/wiki/Phenakistoscope">Phénakistiscope (Wikipédia)</a> · <a href="https://publicdomainreview.org/collection/phenakistoscopes-1833">Public Domain Review, 1833</a> · <a href="https://www.etymonline.com/fr/word/strabismus">Etymonline</a> · <a href="https://lemelson.mit.edu/resources/harold-edgerton">MIT Lemelson : Harold Edgerton</a> · <a href="https://inventionandtech.com/node/85939">The Man Who Stopped Time</a> · <a href="https://flashbak.com/?p=45177">Edgerton, strobe photography</a></p>
</main>
<script>
(()=>{{const r=document.documentElement,b=document.getElementById('themeBtn');
const cur=()=>r.dataset.theme||(matchMedia('(prefers-color-scheme: light)').matches?'light':'dark');
const lab=()=>{{b.textContent=cur()==='dark'?'Thème clair':'Thème sombre'}};
try{{const t=localStorage.getItem('s5');if(t)r.dataset.theme=t}}catch(e){{}}lab();
b.addEventListener('click',()=>{{r.dataset.theme=cur()==='dark'?'light':'dark';lab();try{{localStorage.setItem('s5',r.dataset.theme)}}catch(e){{}}}});}})();
</script>'''
HTML = fr_typo(HTML)
open(os.path.join(HERE, '..', 'Strobe_v2_identité.html'), 'w').write(HTML)
print('ok', len(HTML), HTML.count('—'))
