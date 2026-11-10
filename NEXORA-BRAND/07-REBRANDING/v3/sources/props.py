import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(1, os.path.join(HERE, '..', '..', 'v2', 'sources'))
from marks3 import rhythmos_word, rhythmos_symbol, roshem_symbol, roshem_word, ami_word, ami_symbol, svg
import importlib.util
sp = importlib.util.spec_from_file_location('m2', os.path.join(HERE, '..', '..', 'v2', 'sources', 'marks.py'))
m2 = importlib.util.module_from_spec(sp); sp.loader.exec_module(m2)
from typo import fr_typo

CSS = open(os.path.join(HERE, 'base3.css')).read() + open(os.path.join(HERE, 'props.css')).read()
INK, PAP = '#121214', '#F2F3F5'
KY, KYL, CIRE, JAUNE = '#2340D8', '#6E86FF', '#A3161C', '#FFD23F'

def S(inner, cls='sy', label='', vb='0 0 100 100'): return svg(inner, vb, cls, label)
def W(fn, *a, cls='wm', label=''):
    i, w, h = fn(*a); return svg(i, f'-40 0 {w+80:.0f} {h:.0f}', cls, label)

# ---------------- Étape 1 ----------------
STROBE = [
 ('Ce que le nom dit', 'Il nomme un outil (le stroboscope) et un effet. Il ne dit rien de ce que le studio croit. On peut l’illustrer, pas le défendre en rendez-vous.'),
 ('Le biais', 'Scène, lumière, événementiel : exactement le pôle qui passe au second plan. Avec le nouveau poids des pôles, Strobe raconte le mauvais métier.'),
 ('La perception', 'Boîte de nuit, rave, location d’éclairage. À Dubaï ou dans une institution, il faut l’expliquer avant qu’il ne serve.'),
 ('La santé', 'Le stroboscope est un déclencheur connu de crises chez les personnes photosensibles. Une marque qui porte ce nom doit passer son temps à ne pas clignoter.'),
 ('L’étymologie', 'Vérifiée : « stroboscope » est forgé vers 1832-1833 par Simon Stampfer, du grec στρόβος (strobos, « tourbillon, action de tournoyer ») et σκοπεῖν (skopein, « regarder »). Exploitable ? À moitié : « regarder le tourbillon » donne une belle image, pas une conviction. Et le grec reste caché derrière un mot anglais technique.'),
]
strobe = ''.join(f'<li><b>{a}.</b> {b}</li>' for a, b in STROBE)
N911 = [
 ('ok', 'Court, graphique, se retient tout de suite.'),
 ('ok', 'Une idée d’urgence : « on répond vite », « on sauve votre marque ».'),
 ('ko', 'Aux États-Unis et au Canada, 911 est le numéro d’urgence. Le studio sonnera comme un service de secours.'),
 ('ko', '« 9/11 » se lit « nine-eleven » en anglais : les attentats du 11 septembre 2001. Une partie du public anglophone fera le lien, et on ne peut pas l’empêcher.'),
 ('ko', 'Porsche 911 : un des modèles de voiture les plus connus au monde. Toute recherche « 911 studio » renvoie vers Porsche ou les secours.'),
 ('ko', 'Un nom en chiffres se prononce différemment selon la langue : « neuf cent onze », « neuf-un-un », « nine-one-one », « nine-eleven ». Le nom n’a pas de son stable.'),
 ('ko', 'Un nombre seul est difficile à déposer comme marque : il faut prouver qu’il distingue. Une agence « Studio 911 » existe déjà au Guatemala (fondée en 2008).'),
]
n911 = ''.join(f'<li class="{c}"><span class="tag t-{c}">{"Pour" if c == "ok" else "Contre"}</span> {t}</li>' for c, t in N911)

# ---------------- Étape 2 : 42 candidats ----------------
FIELDS = {
 'Forme et mise en forme': [('ῥυθμός', 'rhythmos', 'gr.', 'la forme d’une chose en mouvement', 'Retenu', 'x'), ('σχῆμα', 'schēma', 'gr.', 'figure', 'Saturé (« schéma »)', 'ko'), ('μορφή', 'morphē', 'gr.', 'forme', 'Saturé (« morph »)', 'ko'), ('εἶδος', 'eidos', 'gr.', 'forme, idée', 'Eidos, éditeur de jeux vidéo', 'ko'), ('צוּרָה', 'tsurah', 'héb.', 'forme', 'Juste mais plat ; moins riche que roshem', 'mid'), ('forma', 'forma', 'lat.', 'forme', 'Générique', 'ko')],
 'Mouvement et rythme': [('κίνησις', 'kinēsis', 'gr.', 'mouvement', 'Saturé (kinetic, kinesis)', 'ko'), ('ῥοή', 'rhoē', 'gr.', 'écoulement', 'Sonne faible, « roé »', 'ko'), ('תְּנוּעָה', 'tnuʿah', 'héb.', 'mouvement (aussi politique)', 'Imprononçable, lecture politique', 'ko'), ('motus', 'motus', 'lat.', 'mouvement', '« Motus et bouche cousue »', 'ko')],
 'Apparition, rendre visible': [('ἐνάργεια', 'enargeia', 'gr.', 'faire voir si vivement qu’on croit l’avoir sous les yeux', 'Finaliste écarté : 4 à 5 syllabes, confondu avec « énergie »', 'mid'), ('φαίνω', 'phainō', 'gr.', 'faire apparaître', 'Un verbe, sonne mal (« faïno »)', 'ko'), ('ὑποτύπωσις', 'hypotypōsis', 'gr.', 'tableau vivant (rhétorique)', 'Trop long', 'ko'), ('evidentia', 'evidentia', 'lat.', 'la même idée, en latin', '« Evidence » en anglais', 'ko'), ('ἔκφρασις', 'ekphrasis', 'gr.', 'décrire une œuvre au point de la faire voir', 'Courant dans le monde de l’art', 'ko')],
 'Image et trace': [('רֹשֶׁם', 'roshem', 'héb.', 'empreinte, impression', 'Retenu', 'x'), ('ἴχνος', 'ichnos', 'gr.', 'trace de pas', '« Ick » en anglais', 'ko'), ('vestigium', 'vestigium', 'lat.', 'trace', 'Trop long', 'ko'), ('imago', 'imago', 'lat.', 'image', 'Saturé (agences photo, édition)', 'ko'), ('àwòrán', 'aworan', 'yor.', 'image, dessin', 'Très utilisé au Nigeria (à vérifier)', 'mid')],
 'L’instant juste': [('καιρός', 'kairos', 'gr.', 'le moment opportun', 'Saturé, et usage théologique chrétien', 'ko'), ('רֶגַע', 'rega', 'héb.', 'instant', 'Rega, marque hi-fi britannique', 'ko'), ('ἀκμή', 'akmē', 'gr.', 'sommet', 'Acme', 'ko')],
 'Le fil qui relie': [('ἁρμονία', 'harmonia', 'gr.', 'ajustement de pièces', 'Saturé', 'ko'), ('רִקְמָה', 'rikmah', 'héb.', 'broderie, tissage', 'Beau, mais « tissu » biologique en hébreu moderne', 'mid'), ('textus', 'textus', 'lat.', 'tissu, puis texte', 'Trop proche de « texte »', 'ko'), ('σύμβολον', 'symbolon', 'gr.', 'jeton brisé dont les moitiés se reconnaissent', 'Le « Symbole » est aussi le Credo chrétien', 'ko')],
 'Le signe et la voix': [('σῆμα', 'sēma', 'gr.', 'signe', 'Sema : cérémonie soufie (religieux)', 'ko'), ('àmì', 'ami', 'yor.', 'signe, marque', 'Retenu', 'x'), ('אוֹת', 'ot', 'héb.', 'signe, lettre', '« OT » : Ancien Testament', 'ko'), ('signum', 'signum', 'lat.', 'signe', 'Générique', 'ko'), ('χαρακτήρ', 'charaktēr', 'gr.', 'empreinte frappée sur une monnaie', 'Devenu « caractère », générique', 'ko')],
 'L’artisan et le savoir-faire': [('τέχνη', 'technē', 'gr.', 'art, savoir-faire', 'Saturé', 'ko'), ('μῆτις', 'mētis', 'gr.', 'l’intelligence rusée des artisans', 'Nom d’une déesse ; « métis » en français', 'ko'), ('γνώμων', 'gnōmōn', 'gr.', 'équerre, aiguille du cadran solaire', 'Gnomon, école d’effets visuels à Hollywood', 'ko'), ('ποίησις', 'poiēsis', 'gr.', 'fabrication', 'Courant dans les agences', 'ko'), ('ọnà / ọ̀nà', 'ona', 'yor.', 'art, ornement / chemin (selon le ton)', 'Court, saturé, et nom d’un mouvement artistique des années 1980', 'mid'), ('ζωγράφος', 'zōgraphos', 'gr.', 'peintre, « qui écrit le vivant »', 'Trop long, trop étroit', 'ko')],
 'La lumière sans cliché': [('κύανος', 'kyanos', 'gr.', 'le bleu (pigment)', 'Devenu « cyan » ; gardé comme couleur de Rhythmos', 'mid'), ('στρόβος', 'strobos', 'gr.', 'tourbillon', 'Racine de Strobe, le plan B', 'mid'), ('נְהוֹרָא', 'nehora', 'aram.', 'lumière', 'Prénom courant et mot de prière', 'ko'), ('lumen', 'lumen', 'lat.', 'lumière', 'Saturé', 'ko'), ('φάος', 'phaos', 'gr.', 'lumière', 'Cliché de la lumière, sonne « faux »', 'ko'), ('γλυφή', 'glyphē', 'gr.', 'gravure', 'Saturé (« glyph »)', 'ko')],
}
nc = sum(len(v) for v in FIELDS.values())
field = ''.join(f'<div class="fld"><h3 class="eyebrow">{k}</h3><ul>' + ''.join(f'<li class="c-{c}"><span class="og">{o}</span><span class="tr">{t}</span><span class="lg">{l}</span><span class="gl">{g}</span><span class="vd">{v}</span></li>' for o, t, l, g, v, c in items) + '</ul></div>' for k, items in FIELDS.items())

# ---------------- Étape 3 : les trois planches ----------------
def fiche(rows): return '<dl class="fiche">' + ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in rows) + '</dl>'
def layers(l): return '<ol class="layers">' + ''.join(f'<li><span class="eyebrow">{a}</span><p>{b}</p></li>' for a, b in l) + '</ol>'
def swatches(sw): return '<div class="sws">' + ''.join(f'<div class="swc" style="background:{h};color:{c}"><b>{n}</b><code>{h}</code><span>{d}</span></div>' for n, h, c, d in sw) + '</div>'

def board(key, num, lang, name, script, acc, accDark, fich, lay, story, logo_dark, logo_light, word_light, sym16, blurred, anim, hidden, construct, long_fr, long_en, short_fr, short_en, dbl, sw, typo_html, tone, motion, risks, fonts_note):
    return f'''<section class="wrap board" id="{key}" style="--acc:{acc};--accd:{accDark}">
<header class="bh"><p class="eyebrow">Proposition {num} · {lang}</p><h2 class="bn">{name}</h2><p class="scr" lang="{ 'el' if key == 'rhythmos' else ('he' if key == 'roshem' else 'yo')}">{script}</p></header>
<div class="b2">
<div class="bcol"><h3 class="eyebrow">Le nom</h3>{fich}{layers(lay)}
<div class="story"><p class="eyebrow">L’histoire, en 20 secondes</p><p>{story}</p></div></div>
<div class="bcol"><h3 class="eyebrow">Le logo</h3>
<div class="lgrid"><div class="lt day">{logo_light}</div><div class="lt night">{logo_dark}</div><div class="lt wide day">{word_light}</div>
<div class="lt sm day"><span class="small">16 px</span>{sym16}</div><div class="lt sm day"><span class="small">Flou, sans le nom</span><span class="blr">{blurred}</span></div><div class="lt sm night"><span class="small">Monochrome négatif</span>{logo_dark.replace(acc, PAP).replace(accDark, PAP)}</div>
<div class="lt sm day an an-{key}" tabindex="0" aria-label="Animation : survolez ou touchez">{anim}<span class="small">Survolez : l’animation</span></div></div>
<div class="hidden"><p class="eyebrow">L’idée cachée</p><p>{hidden}</p><p class="small">{construct}</p></div></div></div>
<div class="b3"><div class="slog"><p class="eyebrow">Ligne maîtresse</p><p class="lfr it">{long_fr}</p><p class="len it" lang="en">{long_en}</p>
<p class="eyebrow">Version courte</p><p class="d2 sfr">{short_fr}</p><p class="d3 sen" lang="en">{short_en}</p><p class="small">{dbl}</p></div>
<div class="sys"><p class="eyebrow">Couleur signature</p>{swatches(sw)}<p class="eyebrow">Typographie</p>{typo_html}<p class="small">{fonts_note}</p>
<p class="eyebrow">Ton de voix</p><p>{tone}</p><p class="eyebrow">Règle de mouvement</p><p>{motion}</p></div></div>
<div class="risk"><p class="eyebrow">Risques et vérifications</p><ul>{''.join(f'<li>{r}</li>' for r in risks)}</ul></div></section>'''

# Rhythmos
rh_fich = fiche([('Écriture', 'ῥυθμός (forme ionienne, chez Démocrite : ῥυσμός)'), ('Translittération', 'rhythmos'), ('Prononciation', 'FR « RIT-moss » · EN « RITH-moss » · en grec, l’accent tombe sur la fin : « rhyth-MOS »'), ('Racine', 'Rattaché à ῥέω (rheō), « couler ». Benveniste a montré que le sens ancien n’est pas la régularité des vagues mais la forme de ce qui coule.'), ('Sens ancien', 'Forme, configuration, disposition. Chez Démocrite, ce qui distingue la lettre A de la lettre N.'), ('Sens moderne', 'En grec moderne, ρυθμός = rythme, cadence. Aucun glissement gênant.'), ('Charge culturelle', 'Aucune charge religieuse ni politique connue.'), ('Certitude', '<span class="tag t-ok">Sûr</span> (Aristote, Métaphysique A 4, 985b ; Benveniste, 1951)')])
rh_lay = [('1 · Littéral', 'Avant de dire « rythme », rhythmos voulait dire « forme » : la forme particulière que prend une chose pendant qu’elle bouge.'), ('2 · Le métier', 'Le motion design donne une forme au mouvement. L’identité donne une forme à une marque. Le web donne un rythme à une page. Le mot couvre les trois pôles, dans l’ordre de leur poids.'), ('3 · La conviction', 'Une marque n’est pas une forme figée : c’est une forme qui bouge sans se perdre. Elle change de support, de format, de vitesse, et on la reconnaît toujours.')]
rh_story = 'Un des plus anciens emplois du mot rhythmos parle de lettres. Selon Aristote, Démocrite expliquait : A diffère de N par sa forme, AN diffère de NA par l’ordre, Z diffère de N par la position. Le linguiste Émile Benveniste a montré qu’à l’origine, le rythme, c’était la forme d’une chose qui bouge. C’est exactement notre métier : dessiner des formes faites pour bouger.'
rh = board('rhythmos', 1, 'grec ancien', 'Rhythmos', 'ῥυθμός', KY, KYL, rh_fich, rh_lay, rh_story,
  S(rhythmos_symbol(PAP, KYL)), S(rhythmos_symbol(INK, KY)), W(rhythmos_word, INK), S(rhythmos_symbol(INK, INK), 's16'), S(rhythmos_symbol(INK, INK)),
  S(rhythmos_symbol(INK, KY), 'sy anim'),
  'Le R se lit deux fois. C’est un Ρ grec, le rhô, initiale de ῥυθμός, auquel on a ajouté une jambe détachée : un pas en avant. L’alphabet latin est né du grec ; notre R, c’est le rhô qui se met en marche. Deuxième lecture, dans le logotype : les lettres larges et étroites suivent le mètre d’un vers d’Homère (longue, brève, brève). Le nom est écrit en rythme.',
  'Construction : tracé de 14 unités sur une grille de 100, panse de rayon 20, jambe à 45°, séparée du rhô par un vide égal à la moitié du trait. Logotype : Mona Sans 800, lettres longues en largeur 125, brèves en largeur 75 (¯ ˘ ˘ | ¯ ˘ ˘ | ¯ ¯).',
  'Avant de dire « rythme », <i>rhythmos</i> voulait dire « forme » : la forme que prend une chose pendant qu’elle bouge. Nous dessinons des marques qui bougent sans jamais perdre la leur.',
  'Before it meant rhythm, <i>rhythmos</i> meant form: the shape a thing takes while it moves. We design brands that move without ever losing theirs.',
  'Garder la forme.', 'In motion. In shape.',
  'Double sens : « garder la forme », c’est être en forme et garder sa forme. En anglais, « in shape » veut dire « en forme » et « qui a sa forme ». Les deux phrases sont écrites dans leur langue, pas traduites.',
  [('Kyanos', KY, PAP, 'Le bleu égyptien, premier pigment fabriqué de l’histoire, que les Grecs appelaient kyanos. Texte sur plâtre : 6,7:1.'), ('Kyanos clair', KYL, INK, 'Pour le mode sombre. Sur encre : 5,8:1.'), ('Encre et plâtre', INK, PAP, 'Encre #121214 sur plâtre #F2F3F5 : 16,7:1.')],
  '<p class="tyA" style="font-family:\'Mona Sans\';font-weight:800;font-stretch:125%">Rhythmos <span style="font-stretch:75%">rythme</span></p><p class="tyB it">la forme de ce qui bouge</p>',
  'Précis, calme, vivant. « On a dessiné la forme ; maintenant, on la fait bouger. » « Une marque qui change de format et qu’on reconnaît encore, c’est une marque qui a un rythme. »',
  'Forme, ordre, position : rien d’autre ne bouge. Les éléments changent de largeur (forme), d’ordre d’entrée (ordre) ou tournent par quarts (position), toujours sur un tempo de 100 battements par minute. Aucun fondu.',
  ['rhythmos.com appartient à une société d’analyse énergétique pour flottes électriques (États-Unis) : conflit possible en classe 42. Recherche de marques obligatoire.', 'rhythmos.co est utilisé par un cabinet de conseil aux églises : le nom exact sur ce domaine a donc une lecture religieuse marginale aux États-Unis.', '« Rhythm » est un mot courant : il faut le logo et le mètre du logotype pour se distinguer, le mot seul ne suffit pas.', 'L’orthographe « rh…th » se tape mal. Les redirections de fautes (rythmos) sont à prévoir.', 'Le bleu et le blanc évoquent la Grèce des cartes postales : jamais de bandes bleu et blanc, jamais de motif grec.'],
  'Mona Sans (GitHub, sur Google Fonts) : sa largeur variable de 75 à 125 permet d’écrire en longues et en brèves. Newsreader en italique pour les phrases longues.')

# Roshem
ro_fich = fiche([('Écriture', 'רֹשֶׁם (hébreu) · racine ר-ש-ם (R-Sh-M)'), ('Translittération', 'roshem'), ('Prononciation', 'FR « RO-chèm » · EN « ROH-shem » · accent sur la première syllabe'), ('Racine', 'R-Sh-M : inscrire, noter. Le verbe לִרְשֹׁם (lirshom) veut dire noter, inscrire ; רִישּׁוּם (rishum) veut dire enregistrement, et aussi esquisse.'), ('Sens', 'Impression, empreinte : l’effet laissé sur quelqu’un, et la marque laissée par une pression.'), ('Parenté', 'L’arabe رسم (rasm) veut dire dessin. Parenté sémitique probable, à faire confirmer.'), ('Charge culturelle', 'Mot courant, sans usage religieux. La racine apparaît dans l’araméen du livre de Daniel (« écrit, inscrit »), sans valeur sacrée. Contient « shem » (nom), qu’un hébréophone n’entend pas isolément.'), ('Certitude', '<span class="tag t-ok">Sûr</span> pour l’hébreu (dictionnaire Pealim) · <span class="tag t-mid">À faire vérifier</span> pour la parenté avec l’arabe')])
ro_lay = [('1 · Littéral', 'L’empreinte : celle d’un sceau pressé dans l’argile, et celle qu’une rencontre laisse dans l’esprit.'), ('2 · Le métier', 'La même racine donne l’esquisse et l’enregistrement (rishum) : dessiner une marque, puis la déposer.'), ('3 · La conviction', 'On ne juge pas une marque à ce qu’elle montre, mais à ce qu’elle laisse quand on a détourné les yeux.')]
ro = board('roshem', 2, 'hébreu', 'Roshem', 'רֹשֶׁם', CIRE, '#FF6B6B', ro_fich, ro_lay,
  'En hébreu, roshem, c’est l’empreinte. Pendant des millénaires, au Proche-Orient, on signait en pressant un sceau gravé à l’envers dans l’argile : l’empreinte, elle, se lisait à l’endroit. Une marque marche pareil. Ce que nous gravons d’un côté, le public le lit de l’autre. Et ce qui compte, c’est ce qui reste.',
  S(roshem_symbol(PAP, INK)), S(roshem_symbol(INK, PAP)), W(roshem_word, INK), S(roshem_symbol(INK, PAP), 's16'), S(roshem_symbol(INK, PAP)),
  S(roshem_symbol(INK, PAP), 'sy anim'),
  'Le symbole est un sceau et son empreinte. À gauche, le R est gravé à l’envers dans le bloc ; à droite, il est imprimé à l’endroit. Pliez le symbole sur son axe : les deux R coïncident exactement. Animation : la moitié gauche se rabat sur la droite, comme on presse un sceau.',
  'Construction : deux carrés de 44 × 56, R de Young Serif à 34 unités, miroir parfait autour de l’axe central.',
  'En hébreu, <i>roshem</i>, c’est l’empreinte : celle du sceau dans l’argile, et celle qu’une rencontre laisse dans l’esprit. Nous dessinons ce qui reste quand on a détourné les yeux.',
  'In Hebrew, <i>roshem</i> is an impression: a seal pressed into clay, and what a meeting leaves in the mind. We design what stays once you’ve looked away.',
  'Ce qui reste.', 'What stays.',
  'Pas de jeu de mots : une phrase sèche qui porte la conviction. « What stays » est la tournure anglaise naturelle, pas une traduction.',
  [('Cire', CIRE, PAP, 'Le rouge de la cire à cacheter. Texte sur papier : 7,0:1.'), ('Papier', PAP, INK, 'Papier #F2F3F5 et encre #121214.')],
  '<p class="tyA" style="font-family:\'Young Serif\'">Roshem</p><p class="tyB" style="font-family:\'Hanken Grotesk\'">ce qui reste</p>',
  'Grave, net, sobre. « On grave une fois, on imprime partout. » « Votre marque se juge à ce qu’on en retient. »',
  'Presser, relever : les éléments arrivent par pression (léger écrasement, puis retour), et ce qui est à l’envers se retourne à l’endroit. Lent et lourd : 700 ms par geste.',
  ['Origine hébraïque : dans certains marchés du Golfe, une marque présentée comme hébraïque peut avoir une lecture politique. Parade honnête : présenter la racine sémitique commune (hébreu rōshem, arabe rasm), à condition de faire valider cette parenté.', 'Le R inversé ressemble à la lettre cyrillique Я.', 'Le mot n’a aucun écho en français ni en anglais : tout passe par l’histoire.', 'Faible pour le motion : l’empreinte est une image fixe.'],
  'Young Serif, un caractère à empattements gravé et lourd comme un sceau ; Hanken Grotesk pour le texte.')

# Àmì
am_fich = fiche([('Écriture', 'àmì (yoruba, langue parlée au Bénin et au Nigeria)'), ('Translittération', 'ami (les accents graves marquent deux tons bas)'), ('Prononciation', 'FR « a-mi » · EN « ah-mee », deux syllabes basses'), ('Sens', 'Signe, marque, repère. Les accents du yoruba s’appellent « àmì ohùn », les signes de la voix.'), ('Écho', 'En français, « ami ». Une double lecture chaleureuse pour les clients francophones.'), ('Charge culturelle', 'Aucune charge religieuse connue. Ni masque, ni motif, ni folklore : un mot de grammaire.'), ('Certitude', '<span class="tag t-ok">Sûr</span> pour « àmì ohùn » (Wiktionnaire) · <span class="tag t-mid">À faire valider</span> par un locuteur pour les tons de l’exemple ọkọ ; le fon et le goun ne sont pas couverts')])
am_lay = [('1 · Littéral', 'Le signe, la marque, ce qui permet de reconnaître.'), ('2 · Le métier', 'Une marque est un signe. Les accents du yoruba en sont la preuve : un petit trait change le sens du mot entier.'), ('3 · La conviction', 'Le détail décide de tout. Sans le bon signe, la même chose veut dire autre chose.')]
am = board('ami', 3, 'yoruba', 'Àmì', 'àmì', '#C99700', JAUNE, am_fich, am_lay,
  'En yoruba, les mêmes lettres o-k-o peuvent vouloir dire mari, houe, véhicule ou lance. Seuls les petits accents posés dessus décident du sens. Ces accents s’appellent « àmì » : les signes. Une marque, c’est ce signe-là. Et en français, àmì se lit « ami ».',
  S(ami_symbol(PAP, JAUNE)), S(ami_symbol(INK, '#C99700')), W(ami_word, INK, '#C99700'), S(ami_symbol(INK, INK), 's16'), S(ami_symbol(INK, INK)),
  S(ami_symbol(INK, '#C99700'), 'sy anim'),
  'Les deux accents graves du logotype sont le sujet du nom : des « àmì ohùn ». Le symbole est un ì : une barre et son accent. Animation : le mot apparaît sans ses accents, puis les accents tombent en dernier, et le mot prend son sens.',
  'Construction : Noto Serif Display 700 (choisi parce qu’il affiche correctement les tons yoruba), accents redessinés à 1,6 fois leur taille.',
  'En yoruba, les mêmes lettres peuvent dire « mari », « houe », « véhicule » ou « lance » : seul le petit signe posé dessus décide. Une marque, c’est ce signe.',
  'In Yoruba, the same letters can mean husband, hoe, vehicle or spear: only the small mark above them decides. A brand is that mark.',
  'Le signe qui décide.', 'The mark that decides.',
  'La version courte vaut en français comme en anglais ; le double sens est dans le nom lui-même (signe en yoruba, ami en français).',
  [('Surligneur', '#FFD23F', INK, 'Le jaune du marqueur : ce qui décide de ce qu’on lit. Sur encre : 13:1, jamais en texte sur blanc.'), ('Ocre foncé', '#C99700', INK, 'Pour les marques sur fond clair.')],
  '<p class="tyA" style="font-family:\'Noto Serif Display\';font-weight:700">àmì · ọkọ̀</p><p class="tyB" style="font-family:\'Noto Sans\'">le signe qui décide</p>',
  'Chaleureux, exact, malin. « Un détail, et tout change. » « On cherche le signe juste avant de chercher le joli. »',
  'Le sens arrive en dernier : un élément entre « nu », puis son signe (accent, couleur, détail) se pose et le fixe. Coup sec de 200 ms.',
  ['AMI Paris, marque de mode très connue (logo cœur et A) : confusion probable et recherche Google inutilisable.', 'Domaines : amistudio.com, studioami.com, ami.design et ami.studio sont pris.', 'Trois lettres : très difficile à protéger seul.', 'Le fon et le goun ne sont pas couverts : ma connaissance de ces langues est trop faible pour proposer un mot sans risque d’erreur.'],
  'Noto Serif Display et Noto Sans : une famille qui gère le point souscrit et les tons du yoruba sans bricolage.')

# ---------------- Étape 4 : comparatif ----------------
CR = ['Profondeur de sens', 'Distinctivité', 'Sonorité FR / EN', 'Polyvalence (motion 35 %, identité 35 %, web 20 %, audiovisuel 10 %)', 'Crédibilité internationale', 'Force du logo', 'Protégeabilité (35, 41, 42)', 'Domaine']
SC = {'Rhythmos': [5, 4, 4, 5, 5, 4, 3, 4], 'Roshem': [4, 5, 4, 3, 3, 4, 4, 4], 'Strobe': [2, 4, 4, 3, 3, 5, 3, 3], 'Àmì': [4, 2, 5, 3, 3, 3, 2, 1]}
WHY = {'Rhythmos': ['Trois couches solides et sourcées', 'Aucun studio de création à ce nom ; « Rhythm Studio » existe au Royaume-Uni', 'On entend « rythme » partout ; orthographe difficile', 'Motion d’abord, puis forme, puis rythme de page', 'Le grec ancien se lit « culture », sans folklore', 'Double lecture R / Ρ, logotype en mètre', 'Société homonyme en analyse énergétique (classe 42 ?)', 'rhythmos.studio libre (registre)'],
       'Roshem': ['Empreinte, esquisse, enregistrement', 'Aucun homonyme trouvé', 'Facile, mais opaque', 'Fort en identité, faible en motion', 'Lecture politique possible dans le Golfe', 'Sceau et empreinte, très clair', 'Mot rare, arbitraire', 'roshem.studio libre (registre)'],
       'Strobe': ['Un outil, pas une conviction', 'Aucun studio à ce nom', 'Mot anglais natif', 'Penche vers la scène', 'Boîte de nuit', 'Disque décalé, le plus abouti', 'Descriptif pour la photo et l’éclairage', 'strobe.design libre ; .com et .studio pris'],
       'Àmì': ['Belle idée, sens étroit', 'AMI Paris', 'Parfait (ami)', 'Neutre', 'Sympathique, peu premium', 'Correct', 'Trois lettres', 'Les replis crédibles sont pris']}
order = sorted(SC, key=lambda k: -sum(SC[k]))
def dots(v): return ''.join(f'<i class="{"on" if j < v else ""}"></i>' for j in range(5))
cmp_rows = ''.join(f'<tr><th scope="row">{c}</th>' + ''.join(f'<td><span class="dots" aria-label="{SC[n][k]} sur 5">{dots(SC[n][k])}</span><span class="why">{WHY[n][k]}</span></td>' for n in order) + '</tr>' for k, c in enumerate(CR))
cmp_rows += '<tr class="sum"><th scope="row">Total sur 40</th>' + ''.join(f'<td class="n">{sum(SC[n])}</td>' for n in order) + '</tr>'
cmp_head = ''.join(f'<th>{n}{" <span class=tag style=background:var(--x);color:var(--onx);border-color:var(--x)>Gagnant</span>" if j == 0 else ""}</th>' for j, n in enumerate(order))

DOM = [('rhythmos.studio', 'Libre', 'ok', 'RDAP du registre (Identity Digital) : 404'), ('rhythmos.design', 'Libre', 'ok', 'RDAP du registre .design : 404'), ('rhythmosstudio.com · wearerhythmos.com · rhythmos-studio.com', 'Libres', 'ok', 'RDAP Verisign : 404'), ('rhythmos.com', 'Pris', 'ko', 'Société d’analyse énergétique (site consulté)'), ('rhythmos.co', 'Pris', 'ko', 'Conseil aux églises (site consulté)'), ('studiorhythmos.com', 'Pris', 'ko', 'RDAP Verisign : 200, pas de site'), ('rhythmos.io', 'Pris', 'ko', 'DNS actif'), ('rhythmos.bj', 'Probablement libre', 'mid', 'Aucune délégation DNS ; pas de RDAP pour le .bj'),
       ('roshem.studio · roshem.design · roshemstudio.com', 'Libres', 'ok', 'RDAP : 404'), ('roshem.com', 'Pris', 'ko', 'RDAP : 200, pas de site'),
       ('amistudio.com · studioami.com · ami.design · ami.studio', 'Pris', 'ko', 'RDAP / DNS'), ('911studio.com', 'Pris', 'ko', 'RDAP : 200')]
dom = ''.join(f'<tr><th scope="row"><code>{a}</code></th><td><span class="tag t-{c}">{b}</span></td><td>{d}</td></tr>' for a, b, c, d in DOM)

RECEP = [('Rhythmos', 'Culture classique, compris (« rythme »)', 'Neutre, sonne savant', 'Clair (« rhythm »), terminaison grecque lue comme sérieuse', 'Neutre ; le rythme est une valeur forte dans la musique d’ici'),
         ('Roshem', 'Mot inconnu, neutre', 'Risque politique si présenté comme hébreu', 'Neutre', 'Neutre'),
         ('Àmì', '« Ami » : sympathique', 'Neutre', 'Lu comme un prénom', 'Compris par les locuteurs yoruba (Bénin, Nigeria)')]
recep = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>' for a, b, c, d, e in RECEP)

HTML = f'''<title>Propositions de nom v3</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Mona+Sans:wdth,wght@75..125,400..900&family=Newsreader:ital,opsz,wght@0,6..72,400..600;1,6..72,400..500&family=JetBrains+Mono:wght@400..600&family=Young+Serif&family=Hanken+Grotesk:wght@400..600&family=Noto+Serif+Display:wght@700&family=Noto+Sans:wght@400&family=Noto+Serif+Hebrew:wght@500&family=Noto+Serif:wght@500&display=swap">
<style>{CSS}</style>
<header class="bar"><div class="wrap"><a class="lg" href="#top">{W(rhythmos_word, 'currentColor', cls='wm', label='Rhythmos')}</a>
<nav aria-label="Parties"><a href="#verdicts">Verdicts</a><a href="#champ">Exploration</a><a href="#rhythmos">Rhythmos</a><a href="#roshem">Roshem</a><a href="#ami">Àmì</a><a href="#choix">Choix</a></nav>
<button class="tg" type="button" id="themeBtn">Thème</button></div></header>
<main id="top">
<section class="wrap hero"><p class="eyebrow">Nom v3 · 10 novembre 2026 · trois territoires de langue</p>
<h1 class="d1">La forme<br><span class="it hl">de ce qui bouge.</span></h1>
<p class="lead">J’ai cherché un nom qui ait trois couches : un sens littéral, un lien direct avec le métier, et une conviction. {nc} mots explorés en grec, hébreu, araméen, latin et yoruba. Trois planches. Un gagnant : <b>Rhythmos</b>, le mot grec qui voulait dire « forme » avant de vouloir dire « rythme ».</p>
<div class="trio">{S(rhythmos_symbol(INK, KY))}{S(roshem_symbol(INK, PAP))}{S(ami_symbol(INK, '#C99700'))}{S(m2.symbol(INK), 'sy pb')}</div>
<p class="small">De gauche à droite : Rhythmos, Roshem, Àmì, et Strobe (plan B).</p></section>

<section class="wrap sec" id="verdicts"><header><p class="eyebrow">Étape 1 · Deux verdicts courts</p><h2 class="d2">Strobe reste le plan B. 911 ne se sauve pas.</h2></header>
<div class="grid v2c"><article class="vc"><h3 class="d3">Strobe</h3><ul class="vl">{strobe}</ul><p class="small"><b>Verdict :</b> le meilleur logo des quatre, le sens le plus mince. Plan B à battre.</p></article>
<article class="vc"><h3 class="d3">« 911 Studio »</h3><ul class="vl n911">{n911}</ul><p class="small"><b>Verdict :</b> non. Aucune version en chiffres ne se sauve sans perdre un son stable d’une langue à l’autre. Si l’idée d’urgence plaît, elle vit mieux dans une phrase (« On répond vite ») ; si les chiffres plaisent, ils ont leur place dans la numérotation des projets (n° 001, 002…).</p></article></div></section>

<section class="wrap sec" id="champ"><header><p class="eyebrow">Étape 2 · Exploration</p><h2 class="d2">{nc} mots, neuf champs, trois retenus.</h2>
<p class="small">Filtres : 2 à 3 syllabes, lisible à vue en français et en anglais, aucun nom divin ni terme sacré, aucun mot saturé en branding. Les sens sont ceux des dictionnaires ; ce qui n’est pas sûr est marqué.</p></header>
<div class="fields">{field}</div>
<h3 class="eyebrow">Réception culturelle des trois retenus</h3>
<div class="tbl"><table><thead><tr><th>Nom</th><th>Europe</th><th>Golfe</th><th>Amérique du Nord</th><th>Afrique de l’Ouest</th></tr></thead><tbody>{recep}</tbody></table></div></section>

{rh}
{ro}
{am}

<section class="wrap sec" id="choix"><header><p class="eyebrow">Étape 4 · Le choix</p><h2 class="d1">Rhythmos gagne.</h2>
<p class="lead">Rhythmos est le seul nom dont les trois couches couvrent les pôles dans l’ordre de leur poids : le motion (la forme en mouvement), l’identité (la forme), le web (le rythme d’une page), puis l’audiovisuel (le rythme d’un montage, d’un son). Il bat Strobe là où Strobe était faible, le sens, et perd sur un seul point : la protection, à cause d’une société homonyme hors de notre métier.</p></header>
<div class="tbl"><table class="cmp"><thead><tr><th>Critère</th>{cmp_head}</tr></thead><tbody>{cmp_rows}</tbody></table></div>
<p class="small">Notes de direction artistique, à confronter à cinq prospects. Strobe garde la meilleure note de logo : c’est le dessin le plus abouti, mais il raconte le mauvais métier.</p>
<h3 class="eyebrow">Domaines : vérifié le 10 nov. 2026 entre 02 h 12 et 02 h 17 UTC</h3>
<div class="tbl"><table><thead><tr><th>Domaine</th><th>État</th><th>Méthode</th></tr></thead><tbody>{dom}</tbody></table></div>
<div class="grid strat">
<article><h3 class="d3">Forme du nom</h3><p><b>RHYTHMOS</b> dans le logotype, « Rhythmos » dans le texte. Les fautes de frappe « rythmos » et « ritmos » sont à rediriger.</p></article>
<article><h3 class="d3">Domaine principal</h3><p><b>rhythmos.studio</b>, vérifié libre auprès du registre. Redirections : rhythmos.design et rhythmosstudio.com (libres).</p></article>
<article><h3 class="d3">Comptes</h3><p><b>@rhythmos.studio</b> partout, le même texte que le domaine. Repli : @rhythmosstudio. Non vérifiés.</p></article>
<article><h3 class="d3">Dépôt</h3><p>Recherche d’antériorités (OAPI, WIPO, EUIPO, INPI, USPTO) en classes 35, 41 et 42, avec une attention particulière à la société américaine Rhythmos en classe 42. Puis OAPI, et extension par le système de Madrid.</p></article></div>
</section>
<p class="wrap small src">Sources : <a href="https://www.scielo.br/j/archai/a/mFCr9Q6jpDs9LmwHWN3st5B/?lang=en">Gomes, « On Democritean Rhysmos », Archai, 2019</a> · <a href="https://books.openedition.org/purh/724">Rythme, flux, forme (OpenEdition)</a> · <a href="https://www.pealim.com/dict/3845-roshem/">Pealim : roshem</a> · <a href="https://pealim.com/dict/6288-rishum">Pealim : rishum</a> · <a href="https://www.wiktionary.com/wiki/ami_ohun">Wiktionnaire : àmì ohùn</a> · <a href="https://archive.phonetics.ucla.edu/Language/YOR/yor_word-list_1972_01.html">UCLA, liste de mots yoruba</a> · <a href="https://www.etymonline.com/fr/word/strabismus">Etymonline</a> · <a href="https://biblioteca.galileo.edu/xmlui/bitstream/handle/123456789/826/2018035_Pellecer%20Marroqu%c3%adn%20Lev%c3%ad%20Otoniel_20072220.pdf?sequence=1">Studio 911, Guatemala</a> · <a href="https://creativebath.org/creative-directory/rhythm-studio-profile-page/">Rhythm Studio, Royaume-Uni</a></p>
</main>
<script>
(()=>{{const r=document.documentElement,b=document.getElementById('themeBtn');
const cur=()=>r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
const lab=()=>{{b.textContent=cur()==='dark'?'Thème clair':'Thème sombre'}};
try{{const t=localStorage.getItem('t3');if(t)r.dataset.theme=t}}catch(e){{}}lab();
b.addEventListener('click',()=>{{r.dataset.theme=cur()==='dark'?'light':'dark';lab();try{{localStorage.setItem('t3',r.dataset.theme)}}catch(e){{}}}});}})();
</script>'''
HTML = fr_typo(HTML)
open(os.path.join(HERE, '..', 'propositions_nom_v3.html'), 'w').write(HTML)
print('ok', len(HTML), HTML.count('¯'), nc)
