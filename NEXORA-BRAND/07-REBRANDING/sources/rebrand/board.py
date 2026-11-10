from marks import *
B = [
 dict(id='volta', n='Volta', fd="'Big Shoulders Display', 'Arial Narrow', sans-serif", fdw=800, fdls='.02em', fdcase='uppercase', fb="'IBM Plex Sans', system-ui, sans-serif",
  terr='Énergie · le terrain', var='Volta · Volta Studio · déclinaisons : Volta Live (événementiel), Volta Motion, Volta Web',
  sens='Le volt est l’unité qui fait tout fonctionner sur un plateau : sono, projecteurs, caméras, écrans, serveurs. « Volta » signifie aussi « le tour, le virage » en italien et en portugais, et c’est une danse de la Renaissance faite de sauts tournés : l’énergie et le mouvement dans un seul mot. Le symbole réunit trois faisceaux issus d’un même point, la forme commune au cône d’une enceinte, au faisceau d’un projecteur et au champ d’une caméra : vos trois métiers de terrain, une seule source.',
  tag=('On met le courant.', 'We switch brands on.'),
  logo=lambda fg, acc: volta_symbol(fg, acc),
  pal=[('Graphite', '#121417', 'Fond principal, scène, vidéo'), ('Lin', '#F2EFE9', 'Fond clair, texte sur sombre'), ('Cuivre', '#C8693A', 'Accent, action : le conducteur'), ('Arc', '#3D7BFF', 'Lumière froide de l’arc : web, liens'), ('Câble', '#8B9199', 'Texte secondaire, détails')],
  palwhy='Graphite et lin pour la sobriété d’un gros studio ; cuivre (le métal qui conduit le courant) et bleu d’arc (la lumière d’un arc électrique) pour l’énergie, sans tomber dans le néon.',
  fonts=('Big Shoulders Display', 'IBM Plex Sans', 'Display condensé d’affiche et de signalétique de scène, en capitales ; texte technique et lisible, culture d’ingénieur.'),
  tone=['Direct', 'Technique sans jargon', 'Énergique', 'Fiable'], ex=['Votre événement, branché de la première à la dernière minute.', 'Un site qui charge vite et qui tient la charge.'],
  dark='#121417', light='#F2EFE9', fg_on_dark='#F2EFE9', fg_on_light='#121417', acc='#C8693A',
  risks=['Mot très utilisé dans le monde (bornes de recharge, véhicules, un album de Björk) : la protection se fera par l’ensemble nom + logo, pas par le mot seul.', 'Haute-Volta est l’ancien nom colonial du Burkina Faso : à tester en Afrique de l’Ouest, même si le fleuve et le lac Volta restent les références actuelles.', '.com exact pris ; thevoltastudio.com et maisonvolta.com étaient libres au moment du test.']),
 dict(id='sillage', n='Sillage', fd="'Cormorant Garamond', Garamond, serif", fdw=500, fdls='.22em', fdcase='uppercase', fb="'Jost', system-ui, sans-serif",
  terr='Présence · héritière de « Aura »', var='Sillage · Studio Sillage · signature : « par Sillage »',
  sens='Le sillage, c’est la trace laissée par un bateau, et dans le vocabulaire du parfum, la présence qui reste après qu’une personne est passée : exactement l’« aura » de Nexora, en plus mûr. Pour un studio, c’est la promesse : ce qu’on fait pour vous continue d’agir après nous (une image, un son, une marque). Le symbole dessine une présence et son sillage à l’angle de Kelvin, 19,47°, l’angle que forme toute trace sur l’eau, quelle que soit la vitesse.',
  tag=('Laissez une trace.', 'Leave a trace.'),
  logo=lambda fg, acc: sillage_symbol(fg, acc),
  pal=[('Nuit', '#0F1214', 'Fond principal, vidéo'), ('Porcelaine', '#F2F0EB', 'Fond clair, texte'), ('Bleu sillage', '#2F4A5C', 'Couleur de marque, aplats'), ('Écume', '#D7E0E3', 'Surfaces claires, filets'), ('Laiton', '#B39257', 'Accent rare : la présence')],
  palwhy='Une palette d’eau profonde et de lumière tamisée : calme, coûteuse, très lisible. Le laiton est réservé au point de présence, comme une signature.',
  fonts=('Cormorant Garamond', 'Jost', 'Garalde élégante en capitales espacées pour la signature ; géométrique sobre pour lire. Registre maison de création, hôtellerie, culture.'),
  tone=['Calme', 'Précis', 'Élégant', 'Peu de mots'], ex=['On travaille pour ce qui reste.', 'Votre marque mérite qu’on s’en souvienne.'],
  dark='#0F1214', light='#F2F0EB', fg_on_dark='#F2F0EB', fg_on_light='#0F1214', acc='#B39257',
  risks=['Prononciation anglaise incertaine hors du monde du luxe (« sil-lidge ») : à tester à Londres et New York.', 'Registre parfum et luxe : moins naturel pour la location de son et l’événementiel de terrain.', 'Le symbole peut se lire « > ● » en très petit : version réduite à prévoir.']),
 dict(id='avant', n='Avant', fd="'Anton', Impact, sans-serif", fdw=400, fdls='.01em', fdcase='uppercase', fb="'Figtree', system-ui, sans-serif",
  terr='Élan · héritière de « Next »', var='Avant · Avant Studio · Avant-première (format événement)',
  sens='« Avant » garde l’esprit de « Next » (être en avance) et parle aux deux langues : avant-garde, avant-première. L’avant-première réunit vos trois métiers en un seul moment : une projection, un son, une captation, une campagne qui la prépare. Le symbole : un A penché vers l’avant dont la barre dépasse, comme une ligne de temps qui a déjà un pas d’avance.',
  tag=('Voir avant.', 'See it first.'),
  logo=lambda fg, acc: avant_symbol(fg, acc),
  pal=[('Écran', '#FAF8F4', 'Fond principal'), ('Encre', '#141416', 'Texte, fonds sombres'), ('Rouge première', '#E0322B', 'Accent, action : le tapis rouge'), ('Velours', '#4A1424', 'Fond de salle, profondeur'), ('Gris salle', '#9A9590', 'Texte secondaire')],
  palwhy='Le vocabulaire de la salle de cinéma un soir de première : écran blanc, velours, tapis rouge. Lumineuse, festive, très lisible.',
  fonts=('Anton', 'Figtree', 'Capitales condensées d’affiche de film ; texte amical et moderne.'),
  tone=['Enthousiaste', 'Confiant', 'Rythmé', 'Accessible'], ex=['Votre lancement mérite une avant-première.', 'On imagine la suite avant tout le monde.'],
  dark='#141416', light='#FAF8F4', fg_on_dark='#FAF8F4', fg_on_light='#141416', acc='#E0322B',
  risks=['Adjectif courant : quasi impossible à protéger seul, nombreux homonymes (finance, mode, technologie).', '« One step ahead » / « un temps d’avance » sont des promesses banales : le concept doit tout porter.', 'Rouge vif proche de nombreuses marques grand public.']),
]
SC = ['Mémorisation', 'Polyvalence sur les 3 pôles', 'Crédibilité internationale', 'Originalité', 'Facilité à protéger', 'Potentiel d’évolution']
SCORES = {'volta': [5, 5, 5, 3, 2, 5], 'sillage': [4, 4, 4, 5, 3, 4], 'avant': [4, 3, 4, 2, 1, 4]}

def sym(b, fg, acc, cls='', bg=None): return svg(b['logo'](fg, acc), cls=cls, bg=bg, label=f'Symbole {b["n"]}')
def word(b, color, cls='w'):
    return f'<span class="{cls}" style="font-family:{b["fd"]};font-weight:{b["fdw"]};letter-spacing:{b["fdls"]};text-transform:{b["fdcase"]};color:{color}">{b["n"]}</span>'
def lockup(b, fg, acc, cls='lk'):
    return f'<span class="{cls}">{sym(b, fg, acc, "lks")}{word(b, fg)}</span>'

def proposal(i, b):
    d, l, fd, fl, acc = b['dark'], b['light'], b['fg_on_dark'], b['fg_on_light'], b['acc']
    sw = ''.join(f'<li><i style="background:{h}"></i><b>{n}</b><code>{h}</code><small>{r}</small></li>' for n, h, r in b['pal'])
    tone = ''.join(f'<li>{t}</li>' for t in b['tone']); ex = ''.join(f'<p class="q">« {e} »</p>' for e in b['ex'])
    risks = ''.join(f'<li>{r}</li>' for r in b['risks'])
    return f'''
<section class="prop" id="{b['id']}" aria-labelledby="h-{b['id']}" style="--d:{d};--l:{l};--fd:{fd};--fl:{fl};--acc:{acc}">
 <header class="phead" style="background:{d};color:{fd}">
  <div class="phl"><p class="pn">Proposition {i} · {b['terr']}</p>
  <h2 id="h-{b['id']}" class="pname">{lockup(b, fd, acc, 'lk lk-hero')}</h2>
  <p class="ptag" style="font-family:{b['fb']}">{b['tag'][0]} <span>{b['tag'][1]}</span></p></div>
 </header>
 <div class="pgrid">
  <div class="card c-name"><h3>Nom et sens</h3><p>{b['sens']}</p><p class="var">{b['var']}</p></div>
  <div class="card c-logo"><h3>Logo</h3>
   <div class="logos">
    <figure style="background:{d}">{lockup(b, fd, acc)}<figcaption>Horizontal, fond sombre</figcaption></figure>
    <figure style="background:{l}">{lockup(b, fl, acc)}<figcaption>Horizontal, fond clair</figcaption></figure>
    <figure style="background:{d}" class="sq">{sym(b, fd, acc, 'big')}<figcaption>Icône seule</figcaption></figure>
    <figure style="background:#ffffff" class="sq">{sym(b, '#000000', '#000000', 'big')}<figcaption>Monochrome noir</figcaption></figure>
    <figure style="background:#000000" class="sq">{sym(b, '#ffffff', '#ffffff', 'big')}<figcaption>Monochrome blanc</figcaption></figure>
    <figure style="background:#ffffff" class="sq small"><span class="fv" style="background:{d}">{sym(b, fd, acc)}</span><span class="fv f32" style="background:{d}">{sym(b, fd, acc)}</span><span class="fv f16" style="background:{d}">{sym(b, fd, acc)}</span><span class="av" style="background:{acc}">{sym(b, d, d)}</span><figcaption>Favicon 48, 32, 16 px · avatar</figcaption></figure>
   </div></div>
  <div class="card c-pal"><h3>Palette</h3><ul class="sw">{sw}</ul><p class="why">{b['palwhy']}</p></div>
  <div class="card c-type"><h3>Typographie</h3><div class="spec" style="background:{d};color:{fd}"><p style="font-family:{b['fd']};font-weight:{b['fdw']};text-transform:{b['fdcase']};letter-spacing:{b['fdls']}" class="sd">{b['tag'][0]}</p><p style="font-family:{b['fb']}" class="sb">Communication visuelle, audiovisuel, motion design et sites web.</p></div><p class="why"><b>{b['fonts'][0]}</b> (principale) et <b>{b['fonts'][1]}</b> (secondaire), Google Fonts. {b['fonts'][2]}</p></div>
  <div class="card c-tone"><h3>Ton de voix</h3><ul class="chips">{tone}</ul>{ex}</div>
  <div class="card c-app"><h3>Applications</h3><div class="apps">
    <div class="bc" style="background:{d}">{sym(b, fd, acc, 'bcs')}</div>
    <div class="bc bcv" style="background:{l};color:{fl}">{lockup(b, fl, acc, 'lk lk-bc')}<span style="font-family:{b['fb']}">Prénom Nom<br><small>Direction de projet</small></span><span class="bcm" style="font-family:{b['fb']}">bonjour@{b['id']}.studio</span></div>
    <div class="ig"><div class="igav" style="background:{d}">{sym(b, fd, acc)}</div><div><b>{b['id']}.studio</b><small>{b['tag'][0]}</small></div></div>
  </div></div>
  <div class="card c-risk"><h3>Risques et points d’attention</h3><ul>{risks}</ul></div>
 </div>
</section>'''

rows = ''.join(f'<tr><th scope="row">{c}</th>' + ''.join(f'<td><span class="bar"><i style="width:{SCORES[b["id"]][k]*20}%"></i></span>{SCORES[b["id"]][k]}</td>' for b in B) + '</tr>' for k, c in enumerate(SC))
rows += '<tr class="sum"><th scope="row">Total sur 30</th>' + ''.join(f'<td>{sum(SCORES[b["id"]])}</td>' for b in B) + '</tr>'

CSS = open('board.css').read()
html = f'''<title>Rebranding Nexora</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@600..900&family=IBM+Plex+Sans:wght@400;500;600&family=Cormorant+Garamond:wght@400;500;600&family=Jost:wght@400;500&family=Anton&family=Figtree:wght@400;600&family=Instrument+Sans:wght@400..700&display=swap">
<style>{CSS}</style>
<div class="wrap">
<header class="top"><p class="k">Rebranding · étape 1 sur 2</p><h1>Trois noms, trois territoires.</h1><p class="lead">Diagnostic, trois propositions avec leur identité minimale, comparaison, recommandation et vérifications à faire avant de valider.</p>
<nav class="toc" aria-label="Sommaire"><a href="#diag">Diagnostic</a><a href="#volta">Volta</a><a href="#sillage">Sillage</a><a href="#avant">Avant</a><a href="#comparatif">Comparatif</a><a href="#verifs">Vérifications</a></nav></header>

<section id="diag" class="sec" aria-labelledby="h-diag"><h2 id="h-diag" class="sh">Diagnostic</h2>
<div class="dg">
 <div class="card"><h3>Ce que la marque doit exprimer</h3><ul><li>Une maîtrise technique de terrain : le son, l’image et la lumière qui marchent le jour J.</li><li>Une création au même niveau que la technique : motion, image, web.</li><li>Une seule maison pour trois pôles, le brand design comme fil commun.</li><li>L’ambition d’un grand studio, crédible à Paris comme à Dubaï, avec une origine assumée sans folklore.</li></ul></div>
 <div class="card"><h3>Pièges à éviter</h3><ul><li>Un nom descriptif (Média, Audio, Web) qui enferme un pôle.</li><li>Un nom inventé qui ne veut rien dire et qu’il faut épeler au téléphone.</li><li>Les clichés de secteur (Pixel, Vision, Creative, Lab) et les symboles attendus (éclair, objectif, onde Wi-Fi).</li><li>Un nom trop local ou religieux pour un public international et grand public.</li></ul></div>
 <div class="card verdict"><h3>« Next Studio » : verdict</h3><p><b>À écarter.</b> Il est clair et prononçable partout, mais il n’appartient à personne : des centaines de studios portent ce nom, « Next » est déjà une grande enseigne britannique et un framework web très connu (Next.js), et le mot est descriptif, donc fragile en dépôt de marque. Le référencement serait quasi impossible. nextstudio.com et next.studio sont déjà enregistrés. On garde l’esprit (avoir un temps d’avance), pas le mot.</p></div>
</div></section>

{''.join(proposal(i + 1, b) for i, b in enumerate(B))}

<section id="comparatif" class="sec" aria-labelledby="h-cmp"><h2 id="h-cmp" class="sh">Comparatif et classement</h2>
<div class="tw"><table><thead><tr><th scope="col">Critère (sur 5)</th>{''.join(f'<th scope="col">{b["n"]}</th>' for b in B)}</tr></thead><tbody>{rows}</tbody></table></div>
<ol class="rank">
 <li><b>Volta.</b> Le seul nom qui porte à la fois le terrain (son, lumière, image, événements) et la création (le tour, le mouvement), sans exclure un pôle. Court, international, déclinable en sous-marques (Volta Live, Volta Motion, Volta Web). Point faible : la protection, à sécuriser par le logo et un nom complet.</li>
 <li><b>Sillage.</b> Le plus original et le plus élégant, avec le meilleur lien à « Aura ». Mais il tire le studio vers le luxe calme, moins naturel pour la sonorisation et la location de matériel, et sa prononciation anglaise reste un pari.</li>
 <li><b>Avant.</b> Le plus fidèle à « Next », facile partout, mais trop générique pour être protégé et distingué durablement.</li>
</ol></section>

<section id="verifs" class="sec" aria-labelledby="h-ver"><h2 id="h-ver" class="sh">Vérifications avant validation</h2>
<div class="dg">
 <div class="card"><h3>Vérifié par moi (registre RDAP, aujourd’hui)</h3><ul class="chk">
  <li><b>Déjà enregistrés</b> : nextstudio.com, next.studio, volta.com, voltastudio.com, volta-studio.com, studiovolta.com, voltastudios.com, volta.studio, sillage.com, sillagestudio.com, studiosillage.com, sillage.studio, avant.com, avantstudio.com, studioavant.com, avant.studio.</li>
  <li><b>Non enregistrés au moment du test</b> : thevoltastudio.com, maisonvolta.com, maisonvolta.studio. Un domaine peut être pris à tout moment : réservez dès la décision.</li>
  <li>Je ne peux pas vérifier les .bj, les comptes de réseaux sociaux, ni les bases de marques.</li></ul></div>
 <div class="card"><h3>À vérifier de votre côté</h3><ul class="chk">
  <li><b>Domaines .bj</b> : auprès d’un bureau d’enregistrement agréé au Bénin.</li>
  <li><b>Comptes</b> : Instagram, TikTok, LinkedIn, YouTube, X, Facebook, Behance (formats @nom.studio, @nomstudio).</li>
  <li><b>Antériorité de marque</b> : OAPI (zone Bénin et Afrique francophone), puis WIPO Global Brand Database, EUIPO, INPI et USPTO pour l’international. Classes à viser : 35 (publicité, communication), 41 (événementiel, production audiovisuelle), 42 (design, création de sites).</li>
  <li><b>Dépôt</b> : OAPI d’abord, puis extension internationale par le système de Madrid si l’activité le justifie.</li>
  <li><b>Sens et prononciation</b> : tester en français, anglais, espagnol, portugais et arabe, et auprès de locuteurs fon et yoruba pour écarter un sens gênant.</li></ul></div>
</div></section>
<p class="foot">Adresses e-mail et comptes affichés : exemples de mise en page, non réservés. Hypothèses : les noms et rôles des associés ne figurent volontairement dans aucun livrable. Les notes sont un jugement de direction artistique, à confronter à quelques clients et prospects.</p>
</div>'''
open('../rebrand-board.html', 'w').write(html)
print(len(html))
