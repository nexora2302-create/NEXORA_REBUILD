import re
from data import DIRS, CRIT
from entfinal import symbol_t, symbol, small, VB

def lum(h):
    h = h.lstrip('#'); r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + .055) / 1.055) ** 2.4
    return .2126 * f(r) + .7152 * f(g) + .0722 * f(b)
def on(h, dark='#111111', light='#F5F2EC'): return dark if lum(h) > .32 else light

# ---------- symboles partagés (<symbol> + <use>) ----------
defs = []
def to_symbol(svg, sid):
    inner = svg.split('>', 1)[1].rsplit('</svg>', 1)[0]
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
    return f'<symbol id="{sid}" viewBox="{vb}">{inner}</symbol>'
for d in DIRS:
    L = d['logo']
    defs.append(to_symbol(symbol_t(a=L['a'], b=L['b']), f's-{d["id"]}-d'))
    defs.append(to_symbol(symbol_t(a=L['la'], b=L['lb']), f's-{d["id"]}-l'))
    defs.append(to_symbol(small(a=L['a'][0], b=L['b'][0], bg=d['v']['bg'] if lum(d['v']['bg']) < .3 else d['v']['light']), f's-{d["id"]}-ico'))
SPRITE = '<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>' + ''.join(defs) + '</defs></svg>'
def use(did, kind='d', cls='sym', label=None):
    lab = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg class="{cls}" viewBox="{VB}" {lab}><use href="#s-{did}-{kind}"/></svg>'

def wordmark(d, kind='d', cls='wm'):
    return f'<span class="{cls}"><span>NE</span>{use(d["id"], kind, "wmx")}<span>ORA</span></span>'
def lockup(d, kind='d', cls='lk'):
    return f'<span class="{cls}">{use(d["id"], kind, "lksym")}<span class="lkw">NEXORA</span></span>'

def bars(scores):
    return ''.join(f'<div class="sc"><span>{c}</span><span class="scb" aria-label="{s} sur 5"><i style="width:{s*20}%"></i></span><b>{s}</b></div>' for c, s in zip(CRIT, scores))

def dir_view(d):
    v = d['v']; did = d['id']
    style = (f"--bg:{v['bg']};--fg:{v['fg']};--surf:{v['surf']};--acc:{v['acc']};--acc2:{v['acc2']};--mut:{v['mut']};--onacc:{v['onacc']};"
             f"--light:{v['light']};--lightfg:{v['lightfg']};--lightacc:{v['lightacc']};--line:{v['line']};"
             f"--fd:{d['fd']};--fdv:{d['fdv']};--fw:{d['fw']};--fls:{d['fls']};--fb:{d['fb']};--fa:{d['fa']}").replace('"', "'")
    pal_bar = ''.join(f'<i style="flex:{p};background:{h}" title="{n} {h}"></i>' for (n, h, r), p in zip(d['pal'], d['prop']))
    pal_list = ''.join(f'<li><span class="sw" style="background:{h}"></span><span><b>{n}</b><code>{h}</code><small>{r}</small></span></li>' for n, h, r in d['pal'])
    cards = ''
    for (w, t, x), m in zip([('Voir', 'Communication visuelle', 'Identité, direction artistique, supports.'), ('Bouger', 'Motion design', 'Logos animés, vidéos, contenus.'), ('Habiter', 'Création web', 'Sites vitrines, e-commerce, UI/UX.')], ('m1', 'm2', 'm3')):
        bg = v[m]; fg = on(bg, v['lightfg'] if lum(v['lightfg']) < .3 else '#111', v['fg'] if lum(v['fg']) > .3 else '#F5F2EC')
        cards += f'<article class="mcard" style="background:{bg};color:{fg}"><h4>{w}<span class="dot">.</span></h4><p class="ct">{t}</p><p>{x}</p></article>'
    apps_bg = v['bg']
    chips = ''.join(f'<li>{p}</li>' for p in d['perso'])
    plus = ''.join(f'<li>{x}</li>' for x in d['plus']); minus = ''.join(f'<li>{x}</li>' for x in d['minus'])
    return f'''
<section class="view dv" id="v-{did}" data-d="{did}" style="{style}" hidden aria-labelledby="t-{did}">
  <header class="dhead">
    <p class="dtag">{d['tag']} · territoire : {d['terr']}</p>
    <h2 id="t-{did}" class="dname">{d['n']}</h2>
    <p class="dline">{d['line']}</p>
    <ul class="chips">{chips}</ul>
  </header>

  <div class="blk"><h3 class="bh">Signature</h3>
  <div class="sig">
    <figure class="sg sg-main">{use(did, 'd', 'bigsym', 'Symbole NEXORA')}<figcaption>Symbole</figcaption></figure>
    <figure class="sg sg-light">{lockup(d, 'l')}<figcaption>Logo complet, fond clair</figcaption></figure>
    <figure class="sg sg-dark">{wordmark(d, 'd', 'wm wm-sig')}<figcaption>Mot signature</figcaption></figure>
    <figure class="sg sg-ico"><span class="ico">{use(did, 'ico', 'icosym')}</span><span class="ico ico-s">{use(did, 'ico', 'icosym')}</span><span class="ico ico-xs">{use(did, 'ico', 'icosym')}</span><figcaption>Icône, 32 et 16 px</figcaption></figure>
  </div></div>

  <div class="blk two"><div><h3 class="bh">Palette</h3><div class="pbar">{pal_bar}</div><ul class="plist">{pal_list}</ul></div>
  <div><h3 class="bh">Typographie</h3><div class="spec"><p class="spec-d">Nous faisons bouger les marques.</p><p class="spec-a">Aa Bb Ée 2026</p><p class="spec-b">Identité, motion design et sites web, pensés ensemble par un studio de Cotonou pour les marques du Bénin, d’Afrique et d’ailleurs.</p><p class="spec-f">{d['fonts']}</p></div>
  <h3 class="bh">Langage graphique</h3><p class="note">{d['lang']}</p></div></div>

  <div class="blk"><h3 class="bh">Le site NEXORA dans cette direction</h3>
  <div class="browser"><div class="bbar"><i></i><i></i><i></i><span>nexora.bj</span></div>
   <div class="site">
    <nav class="snav">{lockup(d, 'd', 'lk lk-nav')}<span class="slinks"><a>Studio</a><a>Expertises</a><a>Réalisations</a><a>Méthode</a></span><a class="btn btn-p">Démarrer un projet</a></nav>
    <div class="shero">
      {wordmark(d, 'd', 'wm wm-hero')}
      <div class="sh-row"><div><p class="sh-t">Nous faisons bouger <em>les marques.</em></p><div class="sh-btn"><a class="btn btn-p">Démarrer un projet</a><a class="btn btn-s">Voir les réalisations</a></div></div>
      <p class="sh-l">Studio créatif à Cotonou. Identité, motion design et sites web, pensés ensemble pour les marques du Bénin, d’Afrique et d’ailleurs.</p></div>
    </div>
    <div class="sstudio"><p class="ss-t">Né à Cotonou, pensé pour le monde.</p><p class="ss-l">Une idée d’abord, trois métiers, une seule équipe.</p></div>
    <div class="scards"><p class="sc-t">Trois métiers, un seul mouvement.</p><div class="cgrid">{cards}</div></div>
    <footer class="sfoot">{lockup(d, 'd', 'lk lk-foot')}<span>Studio créatif · Cotonou, Bénin</span><span>bonjour@nexora.bj</span></footer>
   </div></div></div>

  <div class="blk"><h3 class="bh">Applications</h3>
  <div class="apps">
    <figure class="app a-post"><div class="ap-in"><span class="ap-k">Expertises</span><p class="ap-t">Trois métiers, un seul mouvement.</p>{use(did, 'd', 'ap-sym')}<span class="ap-h">@nexora.studio</span></div><figcaption>Post Instagram, 1:1</figcaption></figure>
    <figure class="app a-story"><div class="ap-in">{use(did, 'd', 'st-sym')}<p class="ap-t">Du brief à l’image.</p><p class="ap-s">Écouter · Concevoir · Créer · Livrer</p><span class="btn btn-p">En savoir plus</span></div><figcaption>Story, 9:16</figcaption></figure>
    <div class="appcol">
      <figure class="app a-card"><div class="cards2"><div class="bc bc-r">{use(did, 'd', 'bc-sym')}</div><div class="bc bc-v"><b>Prénom Nom</b><span>Direction artistique</span><span class="bc-m">bonjour@nexora.bj · nexora.bj</span>{lockup(d, 'l', 'lk lk-bc')}</div></div><figcaption>Carte de visite, recto et verso</figcaption></figure>
      <figure class="app a-slide"><div class="ap-in"><span class="ap-k">Proposition créative · 2026</span><p class="ap-t">Votre marque, en mouvement.</p>{lockup(d, 'd', 'lk lk-slide')}</div><figcaption>Présentation commerciale, 16:9</figcaption></figure>
    </div>
    <figure class="app a-video"><div class="ap-in">{use(did, 'd', 'vid-sym')}<p class="vid-t">NEXORA présente</p><div class="lower"><b>Identité · Motion · Web</b><span>Studio créatif, Cotonou</span></div><span class="vid-rec">00:00:03:12</span></div><figcaption>Ouverture de vidéo et bandeau de titre, 16:9</figcaption></figure>
  </div></div>

  <div class="blk analysis">
    <div><h3 class="bh">Concept</h3><p>{d['concept']}</p><h3 class="bh">Positionnement</h3><p>{d['pos']}</p><h3 class="bh">Potentiel sur les supports</h3><p>{d['supports']}</p><h3 class="bh">Logo</h3><p>{d['logoevo']}</p></div>
    <div><h3 class="bh">Forces</h3><ul>{plus}</ul><h3 class="bh">Limites</h3><ul>{minus}</ul></div>
    <div><h3 class="bh">Évaluation</h3><div class="scores">{bars(d['scores'])}</div><p class="total">Total <b>{sum(d['scores'])}</b> / 40</p></div>
  </div>
</section>'''

# ---------- comparaison ----------
def compare():
    cols = ''
    for d in DIRS:
        v = d['v']
        strip = ''.join(f'<i style="flex:{p};background:{h}"></i>' for (n, h, r), p in zip(d['pal'], d['prop']))
        cols += (f'<article class="cmp" style="--bg:{v["bg"]};--fg:{v["fg"]};--acc:{v["acc"]};--onacc:{v["onacc"]};--fd:{d["fd"].replace(chr(34), chr(39))};--fdv:{d["fdv"]};--fw:{d["fw"]};--fls:{d["fls"]}">'
                 f'<a class="cmp-hero" href="#{d["id"]}">{wordmark(d, "d", "wm wm-cmp")}<span class="cmp-btn">Démarrer un projet</span></a>'
                 f'<div class="pbar">{strip}</div><h3>{d["n"]} <small>{d["tag"]}</small></h3><p>{d["terr"]}</p><p class="tot"><b>{sum(d["scores"])}</b> / 40</p></article>')
    head = ''.join(f'<th scope="col">{d["n"]}</th>' for d in DIRS)
    rows = ''
    for i, c in enumerate(CRIT):
        best = max(d['scores'][i] for d in DIRS)
        rows += f'<tr><th scope="row">{c}</th>' + ''.join(f'<td class="{"best" if d["scores"][i] == best else ""}"><span class="mini"><i style="width:{d["scores"][i]*20}%"></i></span>{d["scores"][i]}</td>' for d in DIRS) + '</tr>'
    rows += '<tr class="sum"><th scope="row">Total sur 40</th>' + ''.join(f'<td>{sum(d["scores"])}</td>' for d in DIRS) + '</tr>'
    return f'''<section class="view" id="v-comparer" hidden aria-labelledby="t-cmp"><h2 id="t-cmp" class="vh">Les quatre directions côte à côte</h2>
<div class="cmpgrid">{cols}</div>
<div class="tblw"><table><thead><tr><th scope="col">Critère</th>{head}</tr></thead><tbody>{rows}</tbody></table></div>
<p class="note">Notes de 1 à 5. En gras, la meilleure note de chaque ligne. Le coût de migration est noté à l’envers : 5 signifie que le changement est léger pour le site actuel.</p></section>'''

DIAG = '''<section class="view" id="v-diagnostic" aria-labelledby="t-diag">
<h2 id="t-diag" class="vh">NEXORA aujourd’hui</h2>
<div class="dg">
 <div><h3 class="bh">Ce que fait la marque</h3><p>Studio créatif basé à Cotonou : identité visuelle, motion design et audiovisuel, création web et production de contenus. Trois métiers pensés ensemble.</p>
 <h3 class="bh">À qui elle parle</h3><ul><li>Entreprises et marques qui veulent une image cohérente sur tous leurs supports</li><li>Institutions, avec des exigences de sérieux et de lisibilité</li><li>Créateurs et événements, qui vivent d’abord sur les réseaux sociaux</li></ul>
 <h3 class="bh">Son ambition</h3><p>Devenir un studio de référence au Bénin et en Afrique de l’Ouest, crédible à l’international, en français comme en anglais. Exister partout : vidéo, réseaux, présentations, événements, produits futurs.</p></div>
 <div><h3 class="bh">Audit de l’identité actuelle</h3>
 <p><b>Ce qui fonctionne.</b> L’exécution est aboutie : typographie très large, contraste fort, mouvement maîtrisé, logo Entrelacs et hero 3D parfaitement accordés. En vidéo et en motion, l’encre et la braise sont redoutablement efficaces.</p>
 <p><b>Ce qui pose question.</b> Le trio noir chaud, crème et orange vif est aujourd’hui l’un des codes les plus répandus chez les studios et agences créatives. La palette ne dit rien de Cotonou ni de la culture de la marque. Le orange saturé est la couleur de l’opérateur Orange, omniprésent en Afrique francophone, ce qui brouille la mémorisation sur des marchés que NEXORA vise. Enfin, le noir dominant pèse sur les supports imprimés et institutionnels.</p>
 <p><b>Conclusion d’audit.</b> Une bonne identité d’exécution, mais une identité de marque encore peu propriétaire. La question n’est pas « est-elle belle ? » mais « est-elle à nous seuls ? ».</p></div>
 <div><h3 class="bh">Ce que dit la recherche</h3><ul>
 <li>Les tendances 2026 se partagent entre un retour de la couleur franche et un retour au fait main, en réaction à la lassitude face aux visuels générés.</li>
 <li>Le bleu reste associé à la confiance et à la compétence ; l’orange à l’énergie et à la créativité. Leur association équilibre élan et fiabilité.</li>
 <li>La teinture à l’indigo est un savoir-faire documenté du nord du Bénin, actif jusqu’au XXe siècle.</li>
 <li>Le laiton coulé d’Abomey, œuvre de la guilde Hountondji, figure dans les collections des grands musées.</li>
 <li>Sur le marché béninois, le jaune est fortement associé à MTN ; dans les pays voisins, le orange à Orange.</li></ul>
 <h3 class="bh">Méthode</h3><p>Trois territoires réellement distincts, une référence (l’identité actuelle), et la même grille de huit critères pour les quatre. Le logo Entrelacs est conservé dans chaque direction ; seules ses couleurs changent.</p></div>
</div></section>'''

VERDICT = '''<section class="view" id="v-verdict" hidden aria-labelledby="t-ver"><h2 id="t-ver" class="vh">Verdict</h2>
<div class="ver">
 <div class="vq"><h3>Faut-il conserver la direction actuelle ?</h3><p>Pas telle quelle. Son exécution est excellente et doit être gardée : la typographie, le mouvement, le logo, le hero 3D. Mais sa palette est un code d’époque, partagé par trop de studios, et son orange appartient déjà, dans l’esprit du public ouest-africain, à un opérateur télécom. Elle porte bien un site ; elle porte mal une marque appelée à durer dix ans sur tous les supports.</p></div>
 <div class="vq"><h3>Les trois propositions apportent-elles une vraie valeur ?</h3><p>Oui, chacune sur un terrain précis. <b>Indigo</b> apporte du sens et de la crédibilité. <b>Marché</b> apporte une puissance sociale et un système modulaire. <b>Laiton</b> apporte un positionnement premium immédiat. Aucune n’est une simple variation de couleur : chacune déplace le positionnement.</p></div>
 <div class="vq vrec"><h3>Recommandation : Indigo</h3><p>C’est la seule direction qui coche à la fois la distinction, l’ancrage et la crédibilité, sans sacrifier ce qui fonctionne déjà. Elle garde la braise comme couleur d’action, Archivo pour l’interface et le logo Entrelacs : c’est une évolution maîtrisée, pas une rupture.</p></div>
 <div class="vq"><h3>Pourquoi stratégiquement et commercialement</h3><ul>
  <li><b>Propriété.</b> Une couleur d’origine béninoise, documentée, que presque aucun studio créatif n’occupe : NEXORA devient reconnaissable sans lire son nom.</li>
  <li><b>Marché.</b> Le bleu rassure les entreprises et les institutions, qui signent les budgets les plus importants ; la braise garde l’énergie qui attire les créateurs.</li>
  <li><b>Différenciation locale.</b> Elle sort du orange d’Orange et du jaune de MTN, les deux couleurs les plus présentes dans l’espace visuel de la région.</li>
  <li><b>International.</b> L’indigo raconte une histoire vraie, exportable, qui positionne NEXORA comme un studio africain contemporain et non comme une copie d’agence occidentale.</li>
  <li><b>Coût.</b> Le changement tient pour l’essentiel dans les couleurs du site, une police de titre et les fichiers du logo. Structure, animations et contenus restent.</li></ul></div>
 <div class="vq"><h3>Ce qu’il faut garder des autres</h3><p>De Marché : l’idée d’une couleur par métier pour les réseaux sociaux (en bleus et braise, pas en six couleurs). De Laiton : le traitement « objet » du logo pour le print et les coffrets. De Braise : l’exécution, intacte.</p></div>
</div></section>'''

tabs = [('diagnostic', 'Diagnostic')] + [(d['id'], d['n'] + (' (actuelle)' if d['id'] == 'braise' else '')) for d in DIRS] + [('comparer', 'Comparer'), ('verdict', 'Verdict')]
nav = ''.join(f'<a class="tab" href="#{k}" data-v="{k}">{n}</a>' for k, n in tabs)

CSS = open('atelier.css').read()
JS = '''(function(){var ids=%s;function show(){var h=(location.hash||'#diagnostic').slice(1);if(ids.indexOf(h)<0)h='diagnostic';ids.forEach(function(i){var el=document.getElementById('v-'+i);if(el)el.hidden=(i!==h);});document.querySelectorAll('.tab').forEach(function(t){var on=t.dataset.v===h;t.classList.toggle('on',on);if(on)t.setAttribute('aria-current','page');else t.removeAttribute('aria-current');});}window.addEventListener('hashchange',function(){show();window.scrollTo(0,0);});show();})();''' % repr([k for k, _ in tabs]).replace("'", '"')

html = f'''<title>Atelier de marque NEXORA</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Instrument+Serif:ital@0;1&family=Gloock&family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&family=Instrument+Sans:wght@400..700&family=Bodoni+Moda:ital,opsz,wght@0,6..96,400..900;1,6..96,400..900&family=Manrope:wght@400..800&display=swap">
<style>{CSS}</style>
{SPRITE}
<header class="top"><div class="topin"><p class="brand">NEXORA · atelier de marque</p><h1>Quatre directions pour une marque appelée à exister partout.</h1><p class="sub">Trois nouveaux territoires et l’identité actuelle, évalués avec la même exigence. Logo retenu : Entrelacs.</p></div>
<nav class="tabs" aria-label="Directions">{nav}</nav></header>
<main class="main">{DIAG}{''.join(dir_view(d) for d in DIRS)}{compare()}{VERDICT}</main>
<footer class="foot"><p>Sources de la recherche : Gosselain, « Documenter la teinture à l’indigo au Nord Bénin », Afrique Archéologie Arts, 2021 (doaj.org) · collections du Metropolitan Museum of Art, guilde Hountondji · presse télécoms sur la présence d’Orange et de MTN en Afrique de l’Ouest · rapports de tendances 2026. Maquettes de démonstration : aucun fichier du site NEXORA n’a été modifié.</p></footer>
<script>{JS}</script>
'''
open('../atelier-nexora.html', 'w').write(html)
print(len(html))
