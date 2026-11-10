import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from marks import wordmark, svg, symbol, slit, ring, ghost_s
from marks import _glyphs  # noqa
import importlib.util
spec = importlib.util.spec_from_file_location('vm', os.path.join(os.path.dirname(__file__), '..', '..', 'sources', 'rebrand', 'marks.py'))
vm = importlib.util.module_from_spec(spec); spec.loader.exec_module(vm)

X = '#22E1FF'; N = '#0B0C0E'; F = '#F3F5F2'
CSS = open(os.path.join(os.path.dirname(__file__), 'common.css')).read() + open(os.path.join(os.path.dirname(__file__), 'audit.css')).read()

def wm(fg='currentColor', cls='wm', o='split', bands=None, label='Strobe'):
    i, W, H = wordmark(100, fg, o, bands=bands); return svg(i, W, H, cls, label, pad=110)
def sym(inner, cls='sy', label='Symbole'):
    return f'<svg class="{cls}" viewBox="0 0 100 100" role="img" aria-label="{label}">{inner}</svg>'
def volta(fg, acc, cls='sy'):
    return f'<svg class="{cls}" viewBox="0 0 100 100" role="img" aria-label="Symbole Volta v1">{vm.volta_symbol(fg, acc)}</svg>'

# ---------- 1. Red team ----------
RED = [
 ('Directeur de création, Paris ou Londres', 'Propre et sans idée. Trois triangles en V, j’en ai vu dix cette année. Big Shoulders et Plex, c’est la « tech premium » de 2020. La maquette est un gabarit bien rangé : rien ne bouge, rien ne se raconte. Et il y a déjà des studios Volta à Porto, Berne, Utrecht, Anvers et Toronto.', 'Le nom, le symbole, la maquette.'),
 ('Juriste en propriété intellectuelle', 'VOLTA est arbitraire pour du design, donc protégeable en théorie. En pratique, les antériorités sont nombreuses : des studios de design homonymes en Europe et au Canada, dont un studio de motion à Berne fondé en 2023. Risque d’opposition élevé en classes 35, 41 et 42 dès qu’on vise l’Europe. Seul le logo complet resterait défendable, et ce logo est générique.', 'Le dépôt international du nom.'),
 ('Client à Dubaï qui reçoit la plaquette', 'Volta, je pense bornes de recharge. « Cotonou, Paris, Londres ou Dubaï » : vous avez un bureau ici ? Non ? Alors pourquoi l’écrire. « We switch brands on » sonne traduit. C’est propre, mais je ne retiens rien.', 'La crédibilité : une seule fausse ligne suffit.'),
 ('22 ans, Instagram et TikTok', 'Rien à filmer. Pas de son, pas de mouvement signature, pas de moment que j’ai envie de mettre en story. « Branché », c’est ce que dit mon oncle.', 'Le slogan, le motion, l’absence de son.'),
]
red = ''.join(f'<article class="rt"><p class="eyebrow">{who}</p><p>{say}</p><p class="small"><b>Ce qu’il tuerait :</b> {kill}</p></article>' for who, say, kill in RED)

PM = [
 ('Confusion', 'Les recherches « Volta studio » renvoient vers Berne, Porto ou Toronto. Les prospects atterrissent chez un concurrent homonyme.'),
 ('Opposition', 'Au premier dépôt visant l’Europe, une opposition arrive. Renommage forcé après deux ans d’investissement, supports à refaire.'),
 ('Invisibilité', 'Le symbole ne se reconnaît ni sur un kakémono à vingt mètres ni en avatar de 40 px : le faisceau central disparaît sous 16 px, ce que le brand book v1 écrivait lui-même.'),
 ('Tiédeur', 'Personne ne reprend les slogans. Les réseaux montrent des projets propres sans signature : le studio ressemble à tous les autres.'),
 ('Crédibilité', 'Un prospect vérifie « Paris, Londres, Dubaï », ne trouve aucune adresse et doute de tout le reste.'),
 ('Lecture régionale', 'Dans la sous-région, Volta évoque d’abord le lac et le fleuve du Ghana, et la Haute-Volta, nom colonial du Burkina Faso jusqu’en 1984. Une lecture géographique et coloniale pour une marque qui voulait éviter les références locales.'),
]
pm = ''.join(f'<li><b>{t}.</b> {d}</li>' for t, d in PM)

BENCH = [
 ('Koto', 'Londres', 'Branding', 'Des systèmes très souples, un ton joueur et sûr de lui.', 'Le registre « mascotte ».'),
 ('DixonBaxi', 'Londres', 'Branding, motion', 'Des identités conçues pour l’écran et le mouvement dès le premier jour.', 'L’échelle des budgets.'),
 ('ManvsMachine', 'Londres', 'Motion, 3D', 'Une image forte par idée, une exécution sans bavure.', 'La 3D hyperréaliste comme style par défaut.'),
 ('Buck', 'Los Angeles', 'Motion design', 'Une culture d’atelier : l’artisanat se voit dans chaque image.', 'La multiplication des styles.'),
 ('Studio Dumbar', 'Rotterdam', 'Branding, motion', 'Des identités pilotées par des règles de mouvement, pas par un logo figé.', 'La rigueur institutionnelle néerlandaise telle quelle.'),
 ('Porto Rocha', 'New York', 'Branding', 'La typographie cinétique comme cœur de l’identité.', 'Les effets typographiques gratuits.'),
 ('Moment Factory', 'Montréal', 'Expériences immersives', 'Lumière, son, vidéo et espace pensés comme un seul médium.', 'Le spectaculaire permanent.'),
 ('United Visual Artists', 'Londres', 'Installations lumière', 'La lumière comme matière, et le temps comme outil de composition.', 'Le registre galerie d’art.'),
]
bench = ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>' for a, b, c, d, e in BENCH)
PRINC = [
 ('Le mouvement d’abord', 'Le logo fixe est une image arrêtée du logo animé, pas l’inverse.'),
 ('Une idée, des règles', 'Une marque moderne est un comportement codé (comment elle entre, coupe, s’arrête), plus qu’un dessin.'),
 ('La typo comme instrument', 'Des fontes variables qui s’étirent et réagissent, au lieu d’un titrage décoratif.'),
 ('Le son est designé', 'Une signature de deux secondes pèse autant qu’un symbole sur les écrans et en événement.'),
 ('Une couleur, massivement', 'Une couleur possédée, utilisée en grand, plutôt que trois accents timides.'),
 ('Parler court', 'Peu de mots, des verbes, aucune explication de ce qu’on vient de montrer.'),
]
princ = ''.join(f'<li><b>{a}.</b> {b}</li>' for a, b in PRINC)

HYP = [
 ('Logo : géométrie générique', 'Confirmée', 'ko', 'Test du flou ci-dessous : flouté et sans nom, le V se confond avec n’importe quel logo de start-up énergie.'),
 ('Slogans : littéraux, anglais non natif, « Branché » daté', 'Confirmée', 'ko', 'Les trois décrivent au lieu de frapper. « We switch brands on » est une traduction, aucun rédacteur anglophone ne l’écrirait.'),
 ('Typo et palette : premium tech 2020, deux accents sans raison', 'Confirmée', 'ko', 'Cuivre et bleu se disputaient le rôle d’accent. Big Shoulders est une bonne fonte, mais attendue.'),
 ('Maquette : structure de template, villes trompeuses', 'Confirmée', 'ko', 'Hero, trois cartes, bloc, grille, formulaire. Et « Cotonou, Paris, Londres ou Dubaï » laisse croire à des implantations qui n’existent pas.'),
 ('Nom : saturé, domaines faibles, Haute-Volta', 'Confirmée, et pire', 'ko', 'Au moins six studios de design s’appellent déjà Volta (sources en bas de page). volta.design est pris aussi.'),
 ('Notes complaisantes', 'Confirmée', 'ko', 'Volta avait 5/5 en crédibilité internationale sans aucun test. Seule la note de protection (2/5) était honnête, et le total l’a noyée.'),
 ('Ajout : je n’avais pas cherché les homonymes', 'Faute du v1', 'ko', 'C’est la plus grave : une recherche de cinq minutes suffisait à écarter Volta.'),
 ('Ajout : un studio fondé sur le son, sans son', 'Faute du v1', 'ko', 'L’identité v1 était muette. C’était pourtant le seul terrain qu’aucun concurrent n’occupe.'),
 ('Ajout : l’idée d’« allumage » était juste', 'Démolie en partie', 'ok', 'Le moment où tout s’allume reste la bonne intuition. Elle était mal exploitée (un V statique), pas fausse.'),
]
hyp = ''.join(f'<tr><th scope="row">{a}</th><td><span class="tag t-{c}">{b}</span></td><td>{d}</td></tr>' for a, b, c, d in HYP)

SC = [
 ('Nom', 4, 'JETER', 'ko', 7, 'Volta → Strobe. Aucun studio homonyme trouvé, domaine .design vérifié libre.'),
 ('Logo', 3, 'JETER', 'ko', 8, 'Trois triangles → disque décalé : un mouvement figé par le flash, lisible à 16 px.'),
 ('Palette', 5, 'RETRAVAILLER', 'mid', 7, 'Deux accents → un seul (xénon), noir salle et blanc flash.'),
 ('Typographie', 5, 'RETRAVAILLER', 'mid', 8, 'Big Shoulders + Plex → Anybody (largeur variable, cinétique) + Schibsted Grotesk.'),
 ('Slogans', 3, 'JETER', 'ko', 8, '« On met le courant » → « Ça marque. / Burned in. »'),
 ('Ton de voix', 6, 'GARDER', 'ok', 8, 'Gardé (direct, technique, fiable), durci : phrases plus courtes, liste « jamais ».'),
 ('Direction artistique', 6, 'GARDER', 'ok', 7, 'Lumière de travail gardée, précisée : un flash, ombres nettes, geste figé.'),
 ('Motion', 4, 'RETRAVAILLER', 'mid', 8, 'L’allumage devient une séquence codée de 900 ms : dérive, flash, rémanence.'),
 ('Son', 0, 'NOUVEAU', 'mid', 7, 'Signature de 1,5 s : charge du flash, déclenchement, rémanence. Jouable dans le fichier 2.'),
 ('Applications', 5, 'RETRAVAILLER', 'mid', 7, 'Kakémono, avatar, carte de fin vidéo, flight case.'),
 ('Maquette du site', 4, 'JETER', 'ko', 8, 'Gabarit → hero à déclencher, console de mixage, planche contact. Bilingue.'),
]
def bar(v, cls): return f'<span class="mtr {cls}" aria-hidden="true"><i style="width:{v*10}%"></i></span>'
sc = ''.join(f'<tr><th scope="row">{a}</th><td class="n">{b if b else "·"}/10 {bar(b,"m1")}</td><td><span class="tag t-{c}">{v}</span></td><td class="n">{d}/10 {bar(d,"m2")}</td><td>{e}</td></tr>' for a, b, v, c, d, e in SC)

# ---------- 2. Nom ----------
CRIT = ['Distinctivité', 'Sens', 'Sonorité FR / EN', 'Protégeabilité (35, 41, 42)', 'Polyvalence sur les 3 pôles', 'Domaine et comptes obtenables']
NS = {
 'Volta': ([1, 3, 5, 1, 3, 1], ['Au moins six studios de design homonymes, plus Volta Charging, Volta Trucks, l’album de Björk.', 'Le volt, l’allumage. Juste, mais générique.', 'Se dit partout sans effort.', 'Antériorités directes en design en Europe et au Canada.', 'Neutre : ne dit rien de l’image ni du mouvement.', '.com, .studio, .design et les replis crédibles sont pris.']),
 'Strobe': ([4, 5, 4, 3, 4, 3], ['Aucun studio de création à ce nom trouvé (recherche web, 10 nov. 2026).', 'Le flash qui fige le mouvement : la photo, la scène, le principe même de l’animation, et l’image qui reste sur la rétine.', 'Mot anglais natif ; en français, « stroboscope », « strobo » sont connus.', 'Arbitraire pour le branding, le web et le motion. Descriptif pour la location d’éclairage et la photo : on ne pourra pas le défendre sur ces seuls services.', 'Photo et image (le strobe est le flash de studio), événementiel, motion. Le web est le lien le plus faible.', 'strobe.design libre (registre). .com et .studio pris.']),
 'Raccord': ([4, 4, 2, 4, 4, 3], ['Aucune agence à ce nom trouvée.', '« Être raccord » : la continuité d’un plan à l’autre, donc la cohérence de la marque partout. Aussi le raccordement électrique et le raccord de montage.', 'Riche en français, vide en anglais (on y entend « record »).', 'Arbitraire pour tous les services visés.', 'Très bon pour le brand design transversal et la vidéo.', 'raccord.design et studioraccord.com libres.']),
}
def dots(v): return ''.join(f'<i class="{"on" if k < v else ""}"></i>' for k in range(5))
nrows = ''.join(f'<tr><th scope="row">{c}</th>' + ''.join(f'<td><span class="dots" aria-label="{NS[n][0][k]} sur 5">{dots(NS[n][0][k])}</span><span class="why">{NS[n][1][k]}</span></td>' for n in NS) + '</tr>' for k, c in enumerate(CRIT))
nrows += '<tr class="sum"><th scope="row">Total sur 30</th>' + ''.join(f'<td class="n">{sum(NS[n][0])}</td>' for n in NS) + '</tr>'

DOM = [
 ('volta.com', 'Pris', 'ko', 'RDAP Verisign'), ('volta.studio', 'Pris', 'ko', 'RDAP Identity Digital (9 nov.)'), ('voltastudio.com / studiovolta.com / wearevolta.com', 'Pris', 'ko', 'RDAP Verisign'), ('volta.design', 'Pris', 'ko', 'RDAP registre .design'),
 ('strobe.com / strobestudio.com / studiostrobe.com / wearestrobe.com', 'Pris', 'ko', 'RDAP Verisign'), ('strobe.studio', 'Pris', 'ko', 'DNS : serveurs de noms actifs (RDAP refusé)'), ('strobe.co / strobe.agency / strobe.works / strobe.tv', 'Pris', 'ko', 'DNS : serveurs de noms actifs'),
 ('strobe.design', 'Libre', 'ok', 'RDAP du registre .design : introuvable (404)'), ('thisisstrobe.com', 'Libre', 'ok', 'RDAP Verisign : 404'), ('strobe-studio.com', 'Libre', 'ok', 'RDAP Verisign : 404'), ('strobe.bj', 'Probablement libre', 'mid', 'DNS : aucune délégation. Pas de RDAP pour le .bj : à vérifier auprès d’un bureau d’enregistrement'),
 ('raccord.com / raccord.studio', 'Pris', 'ko', 'RDAP Verisign / DNS'), ('raccord.design / studioraccord.com', 'Libre', 'ok', 'RDAP : 404'),
]
dom = ''.join(f'<tr><th scope="row"><code>{a}</code></th><td><span class="tag t-{c}">{b}</span></td><td>{d}</td></tr>' for a, b, c, d in DOM)

# ---------- 3. Slogans ----------
REG = {
 'Ordre, impératif': [('Allumez.', 'FR', 'Éliminé', 'Sans objet : on dirait une pub de fournisseur d’électricité.'), ('Hit the lights.', 'EN', 'Éliminé', 'Ambigu en anglais : veut dire allumer ou éteindre.'), ('Montez le son.', 'FR', 'Éliminé', 'Cliché de radio.'), ('Turn it up.', 'EN', 'Éliminé', 'Déjà partout, chansons et pubs.'), ('Don’t blink.', 'EN', 'Éliminé', 'Réplique culte de Doctor Who, titre de roman.')],
 'Défi, provocation': [('Invisible, c’est un choix.', 'FR', 'Gardé', 'Pour les posts et le manifeste, pas comme signature.'), ('Nobody remembers beige.', 'EN', 'Éliminé', 'Attaque une couleur, pas une idée. Vieillit vite.'), ('Rien de tiède.', 'FR', 'Gardé', 'Devient une règle du ton de voix.'), ('Quiet is a choice.', 'EN', 'Éliminé', 'Ambigu : le calme peut être une qualité.'), ('Clignez, c’est perdu.', 'FR', 'Éliminé', 'Négatif, parle de perte.')],
 'Double sens (courant, son, lumière)': [('Sous tension.', 'FR', 'Finaliste', ''), ('Charged.', 'EN', 'Finaliste', ''), ('Ça claque.', 'FR', 'Éliminé', 'Argot de France, mal compris ailleurs ; « claquer » veut aussi dire mourir ou dépenser.'), ('Live wire.', 'EN', 'Éliminé', 'Nom d’une marque de motos électriques (LiveWire).'), ('Plein feu.', 'FR', 'Éliminé', 'Français de théâtre, aucune prise en anglais.')],
 'Promesse de résultat': [('Ça marque.', 'FR', 'Finaliste', ''), ('Burned in.', 'EN', 'Finaliste', ''), ('Vite chargé, dur à oublier.', 'FR', 'Pôle web', ''), ('Loads fast. Lands hard.', 'EN', 'Pôle web', ''), ('Seen. Remembered.', 'EN', 'Éliminé', 'Plat : décrit au lieu de frapper.')],
 'Manifeste ultra-court': [('Une seconde suffit.', 'FR', 'Hero', 'Repris dans le manifeste du hero.'), ('One flash. One brand.', 'EN', 'Éliminé', 'Symétrie facile, déjà entendue.'), ('Chaque image frappe.', 'FR', 'Pôle motion', ''), ('Every frame hits.', 'EN', 'Pôle motion', ''), ('Net. Fort. Vivant.', 'FR', 'Éliminé', 'Trois adjectifs : slogan de salle de sport.')],
 'Attitude': [('Pas de deuxième prise.', 'FR', 'Finaliste', ''), ('No second takes.', 'EN', 'Finaliste', ''), ('On tourne ?', 'FR', 'CTA', ''), ('Ready to roll?', 'EN', 'CTA', ''), ('Prêts pour le direct.', 'FR', 'Éliminé', 'Plat, sonne chaîne d’info.')],
}
def stcls(s): return 'x' if s == 'Finaliste' else ('ko' if s == 'Éliminé' else 'ok')
n = 0; slog = ''
for r, lines in REG.items():
    items = ''
    for l, lang, st, why in lines:
        n += 1
        items += f'<li><span class="num">{n:02d}</span><span class="ln" lang="{lang.lower()}">{l}</span><span class="lg">{lang}</span><span class="tag t-{stcls(st)}">{st}</span><span class="why">{why}</span></li>'
    slog += f'<div class="reg"><h3 class="eyebrow">{r}</h3><ol>{items}</ol></div>'

TESTS = ['2 à 5 mots', 'Verbe fort ou image nette', 'Se dit devant 800 personnes', 'Tient sur un kakémono', 'Ferme un générique', 'Tient dans une bio Instagram', 'Pas trouvé chez une marque connue¹']
FIN = [
 ('Ça marque.', 'Burned in.', True, 'En français, « ça marque » veut dire « ça laisse une trace », et « marque », c’est le métier. En anglais, « burned in », c’est l’image qui reste sur la rétine après un flash, et sur un écran resté trop longtemps allumé. Même idée, deux langues, aucune traduction.', [1, 1, 1, 1, 1, 1, 1], 'Recommandée comme ligne maîtresse : elle dit le résultat, pas le procédé.'),
 ('Sous tension.', 'Charged.', False, '« Sous tension » : alimenté, et en suspense. « Charged » : chargé en électricité, et chargé d’émotion.', [1, 0, 1, 1, 1, 1, 1], 'Décrit un état, pas un résultat. Pas de verbe d’action. À garder pour une campagne ou un événement.'),
 ('Pas de deuxième prise.', 'No second takes.', False, '« Prise » : la prise de vue et la prise électrique. « Take » : la prise et l’avis (« a take »). C’est la culture du direct : le soir de l’événement, on ne refait pas.', [1, 1, 1, 1, 1, 1, 1], 'La plus dure, mais un client peut y lire « pas de retouches ». Réservée au pôle audiovisuel et au direct.'),
]
fin = ''
for fr, en, rec, why, t, verdict in FIN:
    ticks = ''.join(f'<li class="{"y" if v else "n"}">{"Oui" if v else "Non"} · {TESTS[k]}</li>' for k, v in enumerate(t))
    fin += f'<article class="fin{" rec" if rec else ""}"><div class="fl"><p class="d2" lang="fr">{fr}</p><p class="d2 en" lang="en">{en}</p></div><div class="fx"><p>{why}</p><ul class="ticks">{ticks}</ul><p class="small"><b>Verdict :</b> {verdict}</p></div>{"<span class=\"tag t-x recb\">Recommandée</span>" if rec else ""}</article>'

SYS = [
 ('Ligne maîtresse', 'Ça marque.', 'Burned in.', 'Signature, fin de vidéo, kakémono, bio.'),
 ('Communication visuelle et audiovisuel', 'Pas de deuxième prise.', 'No second takes.', 'Le terrain, le direct, l’événement.'),
 ('Motion design', 'Chaque image frappe.', 'Every frame hits.', 'Vingt-cinq images par seconde, aucune de trop.'),
 ('Sites web', 'Vite chargé, dur à oublier.', 'Loads fast. Lands hard.', '« Chargé » renvoie aussi au flash qu’on charge.'),
 ('Brand design (fil transversal)', 'Ça marque.', 'Burned in.', 'Le fil transversal porte la ligne maîtresse : c’est lui qui fait que tout se ressemble.'),
]
sysr = ''.join(f'<tr><th scope="row">{a}</th><td lang="fr"><b>{b}</b></td><td lang="en"><b>{c}</b></td><td>{d}</td></tr>' for a, b, c, d in SYS)

# ---------- 4. Logos ----------
def tile(inner_dark, inner_light, tiny, name, idea, verdict, vcls, wide=False):
    return f'''<article class="lp{' wide' if wide else ''}"><div class="lpv"><div class="night lpd">{inner_dark}</div><div class="day lpl">{inner_light}</div></div>
<div class="lpt"><h3 class="d3">{name}</h3><p>{idea}</p><p class="px16"><span class="small">16 px :</span> {tiny}</p><p><span class="tag t-{vcls}">{verdict}</span></p></div></article>'''

PISTES = [
 (sym(symbol(F)), sym(symbol(N)), sym(symbol('currentColor'), 'tiny'), '1 · Disque décalé (symbole)', 'Un disque coupé à l’horizontale dont les deux moitiés sont décalées : deux images successives d’un même objet, figées par le flash. Le décalage dessine un S. Concept : le mouvement arrêté net.', 'Retenu', 'x'),
 (sym(slit(F)), sym(slit(N)), sym(slit('currentColor'), 'tiny'), '2 · La fente (symbole)', 'Un disque traversé par une fente de lumière : l’obturateur à l’instant où il s’ouvre. Très lisible, mais on y lit aussi une fente de boîte aux lettres ou un bouton.', 'Écarté : trop proche d’une icône', 'ko'),
 (wm(F, 'wm', 'solid'), wm(N, 'wm', 'solid'), '<span class="small">illisible, la marque est le mot</span>', '3 · STR●BE (logotype, lettre-signature)', 'Le O devient un disque plein : le flash. Immédiat, mais le point plein dans un mot est un procédé vu partout.', 'Écarté : déjà vu', 'ko', True),
 (sym(ghost_s(F, X)), sym(ghost_s(N, X)), sym(ghost_s('currentColor', X), 'tiny'), '4 · Rémanence (monogramme)', 'Le S plein et son image rémanente décalée en xénon. Fort à l’écran, mais il dépend de la couleur : en une couleur, il perd son sens.', 'Écarté : ne tient pas en monochrome', 'ko'),
 (sym(ring(F, X)), sym(ring(N, X)), sym(ring('currentColor'), 'tiny'), '5 · Anneau stroboscopique (symbole)', 'Les repères stroboscopiques des platines : quand la vitesse est juste, ils paraissent immobiles. Belle idée de son et de lumière, mais l’anneau devient une roue crantée en petit.', 'Écarté : illisible à 16 px', 'ko'),
 (wm(F, 'wm', 'split', [-140, 140, 0]), wm(N, 'wm', 'split', [-140, 140, 0]), '<span class="small">version animée uniquement</span>', '6 · Logo tranché (dynamique, pour le motion)', 'Le mot coupé en trois bandes qui glissent comme un objet en mouvement, puis se calent au moment du flash. Conçu pour l’animation ; l’image fixe est son état de départ.', 'Retenu comme version animée', 'x', True),
]
pistes = ''.join(tile(*p) for p in PISTES)

blur = ''.join(f'<figure><div class="bl">{s}</div><figcaption>{c}</figcaption></figure>' for s, c in [
 (volta(N, N), 'Volta v1, flouté : un V comme cent autres'), (sym(symbol(N)), 'Strobe, flouté : la silhouette reste unique')])

HTML = f'''<title>Audit Volta v2</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anybody:wdth,wght@50..150,100..900&family=Martian+Mono:wdth,wght@75..112.5,400..700&family=Schibsted+Grotesk:ital,wght@0,400..800;1,400&display=swap">
<style>{CSS}</style>
<header class="bar"><div class="wrap"><a class="lg" href="#top" aria-label="Haut de page">{wm()}</a>
<nav aria-label="Parties"><a href="#audit">Audit</a><a href="#notes">Notes</a><a href="#nom">Nom</a><a href="#slogans">Slogans</a><a href="#logo">Logo</a><a href="#bilan">Bilan</a></nav>
<button class="tg" type="button" id="themeBtn">Thème</button></div></header>
<main id="top">
<section class="wrap hero"><p class="eyebrow">Audit v2 du rebranding · 10 novembre 2026</p>
<h1 class="d1">Volta perd.<br><span class="xh">Strobe</span> gagne.</h1>
<p class="lead">J’ai traité le v1 comme un brouillon à attaquer. Le nom ne survit pas à une recherche de cinq minutes, le symbole ne survit pas au flou, les slogans ne survivent pas à la voix haute. L’intuition de départ, le moment où tout s’allume, survit. Elle devient un flash.</p>
<div class="hv night">{wm(F, 'wm hwm')}<p class="mono hvl">Ça marque. · Burned in.</p></div></section>

<section class="wrap sec" id="audit"><header><p class="eyebrow">Étape 1 · Red team</p><h2 class="d2">Quatre lecteurs, quatre exécutions.</h2><p class="small">Critiques simulées, écrites pour attaquer le v1.</p></header>
<div class="grid rts">{red}</div></section>

<section class="wrap sec"><header><p class="eyebrow">Étape 1 · Pré-mortem</p><h2 class="d2">Novembre 2028. La marque a échoué.</h2><p class="lead">Pourquoi, dans l’ordre de probabilité :</p></header><ol class="pm">{pm}</ol></section>

<section class="wrap sec"><header><p class="eyebrow">Étape 1 · Benchmark</p><h2 class="d2">Ce que font les meilleurs en 2026.</h2><p class="small">Huit studios de référence en création, motion, audiovisuel et lumière. On en tire des principes, on ne copie aucune forme.</p></header>
<div class="tbl"><table><thead><tr><th>Studio</th><th>Ville</th><th>Métier</th><th>Ce qu’on en retient</th><th>Ce qu’on ne prend pas</th></tr></thead><tbody>{bench}</tbody></table></div>
<ol class="princ">{princ}</ol></section>

<section class="wrap sec"><header><p class="eyebrow">Étape 1 · Hypothèses</p><h2 class="d2">Vos six hypothèses, et trois des miennes.</h2></header>
<div class="tbl"><table><thead><tr><th>Hypothèse</th><th>Verdict</th><th>Preuve</th></tr></thead><tbody>{hyp}</tbody></table></div>
<div class="blur">{blur}</div></section>

<section class="wrap sec" id="notes"><header><p class="eyebrow">Étape 1 · Notes</p><h2 class="d2">Avant, après.</h2><p class="small">Les notes v2 sont les miennes, donc à confronter à cinq prospects avant d’y croire. Je les ai volontairement plafonnées à 8.</p></header>
<div class="tbl"><table class="sc"><thead><tr><th>Élément</th><th>v1</th><th>Verdict</th><th>v2</th><th>Ce qui change</th></tr></thead><tbody>{sc}</tbody></table></div></section>

<section class="wrap sec" id="nom"><header><p class="eyebrow">Étape 2 · Verdict sur le nom</p><h2 class="d1">Je change pour Strobe.</h2>
<p class="lead">Vingt-quatre noms testés en interne contre Volta. Deux le battent vraiment ; Strobe est le seul qui gagne aussi à l’international. Écartés notables : Takt (agence de Vancouver qui porte ce nom depuis 2025) et Gobo (Studio Gobo, studio de jeux vidéo de Brighton, plus de cent personnes).</p></header>
<div class="tbl"><table class="nm"><thead><tr><th>Critère</th><th>Volta</th><th>Strobe <span class="tag t-x">Choisi</span></th><th>Raccord</th></tr></thead><tbody>{nrows}</tbody></table></div>
<div class="grid strat">
<article><h3 class="d3">Forme du nom</h3><p><b>STROBE</b> en capitales dans le logo, « Strobe » dans le texte. Mention complète quand le contexte l’exige : « Strobe, studio de création ». Pas de « Maison », pas de « The », pas de « Studio » collé au nom.</p></article>
<article><h3 class="d3">Domaine principal</h3><p><b>strobe.design</b>, vérifié libre auprès du registre aujourd’hui. Crédible dans le métier, court, sans tiret. Redirections : <code>thisisstrobe.com</code> (libre) et <code>strobe.bj</code> s’il est libre. Le tarif peut être « premium » chez certains bureaux d’enregistrement : à réserver vite.</p></article>
<article><h3 class="d3">Comptes</h3><p><b>@strobe.design</b> partout : Instagram, TikTok, Behance, Threads, et une page LinkedIn « Strobe ». Le compte reprend le domaine, c’est la même adresse partout. Repli : <code>@strobedesign</code>. Non vérifié : à tester à la main sur chaque réseau.</p></article>
<article><h3 class="d3">Dépôt</h3><p>Avant tout dépôt : recherche d’antériorités dans les bases OAPI, WIPO Global Brand Database, EUIPO, INPI et USPTO. Puis dépôt OAPI (le Bénin en est membre, un dépôt couvre ses dix-sept États) en classes 35, 41 et 42, marque verbale STROBE et marque semi-figurative (logo). Extension par le système de Madrid vers l’UE, le Royaume-Uni, les Émirats et les États-Unis. Le mot sera faible pour la photo et la location d’éclairage : le logo protège ces services. À valider avec un conseil en propriété industrielle.</p></article>
</div>
<h3 class="eyebrow">Domaines : ce qui est vérifié aujourd’hui (10 nov. 2026, 01 h 33 UTC)</h3>
<div class="tbl"><table><thead><tr><th>Domaine</th><th>État</th><th>Méthode</th></tr></thead><tbody>{dom}</tbody></table></div>
<div class="todo"><h3 class="d3">À vérifier vous-même</h3><ul><li><b>.bj :</b> disponibilité de <code>strobe.bj</code> auprès d’un bureau d’enregistrement agréé (pas de RDAP pour le .bj).</li><li><b>Comptes :</b> @strobe.design et @strobedesign sur Instagram, TikTok, Behance, X, YouTube, LinkedIn.</li><li><b>Marques :</b> OAPI, WIPO, EUIPO, INPI, USPTO en classes 35, 41, 42. Attention aux marques STROBE en classes 9 et 11 (éclairage), qui peuvent gêner les services de location.</li><li><b>Sens :</b> en fon, yoruba, espagnol, portugais et arabe. En espagnol et portugais, « estrobo » est un terme de marine (une estrope), sans connotation gênante à ma connaissance.</li></ul></div>
</section>

<section class="wrap sec" id="slogans"><header><p class="eyebrow">Étape 3 · Slogans</p><h2 class="d2">Trente lignes brutes. Trois finalistes.</h2><p class="small">Chaque ligne est écrite dans sa langue, pas traduite. Six registres, cinq lignes chacun.</p></header>
<div class="regs">{slog}</div>
<div class="fins">{fin}</div>
<p class="small">¹ Recherche web du 10 nov. 2026 sur « Ça marque », « Burned in » et « No second takes » : aucune marque ni campagne connue trouvée. Une recherche INPI et EUIPO reste nécessaire avant dépôt.</p>
<header><h2 class="d2">Le système.</h2></header>
<div class="tbl"><table><thead><tr><th>Usage</th><th>Français</th><th>English</th><th>Pourquoi</th></tr></thead><tbody>{sysr}</tbody></table></div>
<div class="grid man">
<article class="night mf"><p class="eyebrow">Manifeste du hero · FR</p><p class="d3">Une marque a une seconde.<br>On en fait un flash.<br>Celui qu’on voit encore les yeux fermés.</p></article>
<article class="night mf"><p class="eyebrow">Hero manifesto · EN</p><p class="d3" lang="en">A brand gets one second.<br>We make it a flash.<br>The one you still see with your eyes shut.</p></article>
<article class="mf cta"><p class="eyebrow">CTA, avant → après</p><p><s>Parler du projet</s></p><p class="d2">On tourne ?</p><p class="d3" lang="en">Ready to roll?</p><p class="small">Sur le plateau, « On tourne ! » lance la prise. En question, c’est une invitation à s’engager. Le bouton du formulaire, lui, dit l’action : « Envoyer le brief / Send the brief ».</p></article>
</div></section>

<section class="wrap sec" id="logo"><header><p class="eyebrow">Étape 4 · Logo v2</p><h2 class="d2">Six pistes, une idée retenue.</h2><p class="small">Interdits respectés : ni éclair, ni onde, ni objectif, ni bouton lecture, ni triangle, ni globe, ni étincelle. Chaque piste est montrée sur noir, sur blanc et à 16 px.</p></header>
<div class="lps">{pistes}</div>
<div class="ret night"><div class="retl"><p class="eyebrow">Retenu</p><h3 class="d2">Le disque décalé, devenu le O de STROBE.</h3>
<p>Un seul dessin fait tout : le symbole seul pour l’avatar et le favicon, le O du logotype, et le point de départ de l’animation (les moitiés glissent, le flash les fige). Il se lit à 16 px, en une couleur, en négatif, et sur une photo. Construction : disque de rayon 34 dans un carré de 100, chaque moitié glisse de 17 % du diamètre ; dans le logotype, le glissement passe à 12 % pour ne pas heurter le R et le B.</p></div>
<div class="retv">{sym(symbol(F), 'sy big')}</div></div>
<div class="ba"><figure><div class="day bav">{volta(N, '#C8693A', 'sy')}<span class="vw">VOLTA</span></div><figcaption><b>Avant.</b> Trois triangles issus d’un point. Générique, illisible sous 16 px, muet en animation.</figcaption></figure>
<figure><div class="day bav">{wm(N, 'wm')}</div><figcaption><b>Après.</b> Un mot dessiné sur Anybody 900, approches retouchées autour du disque, un O qui porte toute l’idée.</figcaption></figure></div>
<div class="tests">
<figure><div class="tst night">{sym(symbol(F), 'sy')}</div><figcaption>Négatif</figcaption></figure>
<figure><div class="tst day">{sym(symbol(N), 'sy')}</div><figcaption>Monochrome</figcaption></figure>
<figure><div class="tst xb">{sym(symbol(N), 'sy')}</div><figcaption>Sur xénon</figcaption></figure>
<figure><div class="tst ph">{sym(symbol(F), 'sy')}</div><figcaption>Sur image (fond simulé)</figcaption></figure>
<figure><div class="tst day row16">{sym(symbol(N), 's16')}{sym(symbol(N), 's24')}{sym(symbol(N), 's32')}</div><figcaption>16, 24, 32 px</figcaption></figure>
<figure><div class="tst night kk"><span>{wm(F, 'wm')}</span><b>Ça marque.</b><i>Burned in.</i></div><figcaption>Kakémono 80 × 200</figcaption></figure>
</div></section>

<section class="wrap sec" id="bilan"><header><p class="eyebrow">Bilan</p><h2 class="d2">Je garde. Je change. Je jette.</h2></header>
<div class="grid gcj">
<article><h3 class="d3 t-ok">Je garde</h3><ul><li>L’intuition fondatrice : le moment où tout s’allume, devenu le flash.</li><li>Le ton : direct, technique sans jargon, fiable.</li><li>La lumière de travail comme direction photo.</li><li>Le bilingue écrit nativement, les thèmes clair et sombre.</li><li>« Basés à Cotonou, clients partout. »</li><li>Aucune section « à propos », aucun nom d’associé.</li></ul></article>
<article><h3 class="d3 t-mid">Je change</h3><ul><li>Le nom : Volta → Strobe.</li><li>La palette : deux accents → un seul, le xénon.</li><li>La typo : Big Shoulders + Plex → Anybody + Schibsted Grotesk.</li><li>Le motion : un principe vague → une séquence de 900 ms codée.</li><li>Le site : un gabarit → un hero à déclencher, une console, une planche contact.</li><li>Ajout : une signature sonore.</li></ul></article>
<article><h3 class="d3 t-ko">Je jette</h3><ul><li>Les trois triangles.</li><li>Cuivre + bleu.</li><li>« On met le courant. », « We switch brands on. », « Branché. »</li><li>La liste de villes du hero.</li><li>La grille de trois cartes identiques.</li><li>Les notes 5/5 que je m’étais attribuées.</li></ul></article>
</div>
<div class="bet night"><p class="eyebrow">Si je pariais mon agence sur une seule version</p><p class="lead">Strobe, avec le disque décalé et « Ça marque. / Burned in. ». C’est la seule version où le nom, le symbole, le slogan, le mouvement et le son racontent la même chose : un flash qui fige l’instant juste et qui reste sur la rétine. Et c’est la seule dont j’ai vérifié qu’aucun studio ne la porte déjà et que le domaine est libre.</p></div>
<div class="risks"><h3 class="d3">Les trois risques qui restent</h3><ol><li><b>Juridique :</b> une marque STROBE déposée en classe 35, 41 ou 42 que ma recherche web n’a pas trouvée. Seule une recherche en base (OAPI, WIPO, EUIPO) le dira.</li><li><b>Perception :</b> à Dubaï ou dans une institution, « strobe » peut évoquer la boîte de nuit ou la location d’éclairage. L’identité doit rester sévère et éditoriale pour tenir la ligne premium.</li><li><b>Santé :</b> le stroboscope déclenche des crises chez les personnes photosensibles. La marque ne clignote jamais : un flash par séquence, jamais plus de trois par seconde, rien sans mouvement réduit.</li></ol></div>
<p class="small src">Sources de la recherche d’homonymes (10 nov. 2026) : <a href="https://www.behance.net/voltastudio/info">Volta, Porto (Behance)</a> · <a href="https://www.markt-kom.com/en/markom/business/isabelle-lindner-und-selina-muth-gruenden-volta-studio">Volta Studio, Berne</a> · <a href="https://www.sortlist.co.uk/agency/volta-communicatie-in-vorm">Volta, Anvers</a> · <a href="https://www.designrush.com/agency/profile/volta-creative">Volta Creative, Sheffield</a> · <a href="https://www.keywordsstudios.com/en/about-us/global-offer/locations-studios/volta/">Volta, Québec (Keywords Studios)</a> · <a href="https://www.businesswire.com/news/home/20250303726583/en">Takt, Vancouver</a> · <a href="https://www.keywordsstudios.com/en/about-us/global-offer/locations-studios/studio-gobo">Studio Gobo, Brighton</a>.</p>
</section></main>
<script>
(()=>{{const r=document.documentElement,b=document.getElementById('themeBtn');
const cur=()=>r.dataset.theme||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light');
const lab=()=>{{b.textContent=cur()==='dark'?'Thème clair':'Thème sombre'}};lab();
b.addEventListener('click',()=>{{r.dataset.theme=cur()==='dark'?'light':'dark';lab();try{{localStorage.setItem('t',r.dataset.theme)}}catch(e){{}}}});
try{{const t=localStorage.getItem('t');if(t){{r.dataset.theme=t;lab()}}}}catch(e){{}}}})();
</script>'''
from typo import fr_typo
HTML = fr_typo(HTML)
out = os.path.join(os.path.dirname(__file__), '..', 'Volta_v2_audit.html')
open(out, 'w').write(HTML)
print('ok', len(HTML), HTML.count('—'))
