import math
from marks import volta_symbol, P
G, L, CU, ARC, CA = '#121417', '#F2EFE9', '#C8693A', '#3D7BFF', '#8B9199'
def sym(fg, acc, cls='s', label='Symbole Volta'):
    return f'<svg class="{cls}" viewBox="0 0 100 100" role="img" aria-label="{label}">{volta_symbol(fg, acc)}</svg>'
def symvar(cls='s'):  # couleurs par variables CSS (thème clair/sombre)
    return f'<svg class="{cls}" viewBox="0 0 100 100" aria-hidden="true">{volta_symbol("var(--fg)", "var(--cu)")}</svg>'
def lk(fg, acc, cls='lk'):
    return f'<span class="{cls}" style="color:{fg}">{sym(fg, acc, "lks")}<span class="wd">Volta</span></span>'
def lkv(cls='lk'):
    return f'<span class="{cls}">{symvar("lks")}<span class="wd">Volta</span></span>'

# Construction : trois triangles d'un même point S, angles ±7,2° (faisceau central) et 12,5° à 31° (latéraux).
S = (50, 92); R = 88
def ray(a): a = math.radians(a); return (S[0] + R * math.sin(a), S[1] - R * math.cos(a))
construct = f'''<svg class="cons" viewBox="-6 -6 112 112" role="img" aria-label="Construction du symbole">
<circle cx="50" cy="92" r="88" fill="none" stroke="var(--rule)" stroke-width=".4"/>
{''.join(f'<line x1="50" y1="92" x2="{ray(a)[0]:.1f}" y2="{ray(a)[1]:.1f}" stroke="var(--rule)" stroke-width=".4"/>' for a in (-31, -12.5, -7.2, 0, 7.2, 12.5, 31))}
<g opacity=".9">{volta_symbol("var(--ghost)", "var(--cu)")}</g>
<circle cx="50" cy="92" r="1.8" fill="var(--fg)"/>
<g class="cl"><text x="54" y="98">source unique</text><text x="2" y="10">31°</text><text x="31" y="2">12,5°</text><text x="44" y="0">±7,2°</text><text x="66" y="62">rayon 88</text></g></svg>'''

CSS = open('volta.css').read()
JS = open('volta.js').read()
html = f'''<title>Volta, identité de marque</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@500..900&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@500&display=swap">
<style>{CSS}</style>
<header class="bar"><a class="bl" href="#identite">{lkv('lk lk-bar')}</a>
<nav class="sw" aria-label="Parties"><a href="#identite" data-v="identite">Identité</a><a href="#site" data-v="site">Site</a></nav>
<button class="th" type="button" id="themeBtn" aria-label="Changer de thème">Clair / sombre</button></header>

<main>
<!-- ================= IDENTITÉ ================= -->
<section class="view" id="v-identite" aria-label="Identité de marque">
 <div class="cover">
  <div class="cv-sym">{symvar('cvs')}</div>
  <h1 class="cv-t">Volta</h1>
  <p class="cv-l">Identité de marque · version 1.0</p>
 </div>

 <section class="ch" aria-labelledby="h1"><p class="cn">01</p><h2 id="h1">L’histoire</h2>
  <div class="cols">
   <p class="big">Avant chaque événement, il y a un moment précis : celui où l’on met le courant. Les enceintes s’allument, le projecteur s’éclaire, la caméra se met en route. Volta est né de ce moment.</p>
   <div class="txt"><p>Le volt est l’unité qui fait fonctionner tout ce que nous touchons : le son, l’image, la lumière, les écrans, les serveurs. « Volta » est aussi un mot de mouvement. En italien et en portugais, il signifie « le tour, le virage » ; c’est enfin une danse de la Renaissance faite de sauts tournés. L’énergie et le mouvement, dans un seul mot de deux syllabes qui se prononce de la même façon à Cotonou, Paris, Londres ou Dubaï.</p>
   <p>Le symbole réunit trois faisceaux issus d’un même point. C’est la forme commune au cône d’une enceinte, au faisceau d’un projecteur et au champ d’une caméra. Trois métiers, une seule source. Ensemble, ils dessinent le V de Volta. Le faisceau central, cuivre comme le conducteur, est celui qui porte l’idée : le brand design, qui traverse tout ce que nous faisons.</p></div>
  </div>
  <div class="poles"><div><b>Communication visuelle et audiovisuel</b><span>Faisceau gauche</span></div><div><b>Brand design</b><span>Faisceau central, la signature</span></div><div><b>Motion design et web</b><span>Faisceau droit</span></div></div>
 </section>

 <section class="ch" aria-labelledby="h2"><p class="cn">02</p><h2 id="h2">Le logo</h2>
  <div class="cols">
   <figure class="pane">{construct}<figcaption>Construction : trois triangles issus d’une source unique, sur un cercle de rayon 88. Écarts de 5,3° entre les faisceaux.</figcaption></figure>
   <div class="txt"><h3>Versions</h3>
    <div class="lv">
     <div class="lvi dk">{lk(L, CU)}</div><div class="lvi lt">{lk(G, CU)}</div>
     <div class="lvi lt sq">{sym(G, G)}</div><div class="lvi dk sq">{sym(L, L)}</div><div class="lvi cu sq">{sym(G, L)}</div>
    </div>
    <h3>Zone de protection</h3><p>Autour du logo, un espace libre égal à la hauteur du faisceau central divisée par deux (0,5 V). Rien n’y entre : ni texte, ni bord de page, ni autre logo.</p>
    <div class="clear"><span class="cz">{lk(G, CU)}</span></div>
    <h3>Tailles minimales</h3><p>Logo horizontal : 24 px de haut à l’écran, 8 mm à l’impression. Symbole seul : 16 px, 5 mm. En dessous, le faisceau central disparaît.</p>
   </div>
  </div>
  <h3 class="h3s">Usages à éviter</h3>
  <div class="dont">
   <figure><div class="dn">{sym(G, ARC)}</div><figcaption>Changer la couleur du faisceau central</figcaption></figure>
   <figure><div class="dn"><span style="display:inline-block;transform:rotate(180deg)">{sym(G, CU)}</span></div><figcaption>Retourner ou faire pivoter le symbole</figcaption></figure>
   <figure><div class="dn"><span style="display:inline-block;transform:scaleX(1.5)">{sym(G, CU)}</span></div><figcaption>Déformer les proportions</figcaption></figure>
   <figure><div class="dn" style="background:{CU}">{sym(G, CU)}</div><figcaption>Poser le symbole cuivre sur fond cuivre</figcaption></figure>
  </div>
 </section>

 <section class="ch" aria-labelledby="h3"><p class="cn">03</p><h2 id="h3">Couleurs</h2>
  <div class="pal">
   <div class="pc" style="background:{G};color:{L}"><b>Graphite</b><code>#121417</code><span>60 %. Fond principal, scène, vidéo, écrans.</span></div>
   <div class="pc" style="background:{L};color:{G}"><b>Lin</b><code>#F2EFE9</code><span>25 %. Fond clair, documents, texte sur sombre.</span></div>
   <div class="pc" style="background:{CU};color:{G}"><b>Cuivre</b><code>#C8693A</code><span>8 %. Action, signature, faisceau central.</span></div>
   <div class="pc" style="background:{ARC};color:{L}"><b>Arc</b><code>#3D7BFF</code><span>4 %. Liens, données, interface web.</span></div>
   <div class="pc" style="background:{CA};color:{G}"><b>Câble</b><code>#8B9199</code><span>3 %. Texte secondaire, filets.</span></div>
  </div>
  <p class="note">Contrastes mesurés : lin sur graphite 16,1:1 ; graphite sur cuivre 4,9:1 (texte de bouton) ; câble sur graphite 5,8:1. Sur fond lin, cuivre et arc (3,3:1) ne portent jamais de texte courant : aplats, filets ou titres très gras uniquement ; câble (2,8:1) y est réservé aux éléments décoratifs.</p>
 </section>

 <section class="ch" aria-labelledby="h4"><p class="cn">04</p><h2 id="h4">Typographie</h2>
  <div class="cols">
   <div class="pane ty"><p class="t1">On met le courant.</p><p class="t2">Big Shoulders Display, 800, capitales, interlettrage +2 %. Titres, affiches, écrans.</p></div>
   <div class="pane ty"><p class="t3">Son, image, lumière et web, pensés ensemble pour que tout fonctionne le jour J.</p><p class="t2">IBM Plex Sans, 400 et 600. Texte, interface, documents. IBM Plex Mono pour les données techniques (fiches, minutages).</p></div>
  </div>
  <div class="scale"><span style="font-size:4.5rem">Titre 72</span><span style="font-size:2.5rem">Section 40</span><span style="font-size:1.5rem;font-family:var(--ft)">Intertitre 24</span><span style="font-size:1.06rem;font-family:var(--ft)">Texte 17</span><span style="font-size:.82rem;font-family:var(--fm)">TECHNIQUE 13</span></div>
 </section>

 <section class="ch" aria-labelledby="h5"><p class="cn">05</p><h2 id="h5">Direction artistique</h2>
  <div class="dag">
   <div><h3>Images</h3><p>La lumière de travail, pas la photo de banque : plateaux, régies, câbles, faisceaux dans la fumée, mains sur une console, écrans allumés dans le noir. Ombres profondes, une seule source chaude, grain conservé. Les gens sont montrés en action, jamais en pose.</p></div>
   <div><h3>Icônes</h3><p>Trait de 1,5 px, angles vifs, construits sur la même géométrie de faisceaux. Une seule couleur. Pas d’icônes en pastille ni d’emoji.</p>
    <div class="icons">
     <svg viewBox="0 0 24 24" aria-label="Son"><path d="M4 9h4l5-4v14l-5-4H4z M16 9a4 4 0 0 1 0 6 M18.5 6.5a8 8 0 0 1 0 11" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
     <svg viewBox="0 0 24 24" aria-label="Projection"><path d="M3 8h8v8H3z M11 10l10-5v14l-10-5" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
     <svg viewBox="0 0 24 24" aria-label="Caméra"><path d="M3 7h12v10H3z M15 11l6-3v8l-6-3" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
     <svg viewBox="0 0 24 24" aria-label="Motion"><path d="M3 17c4 0 5-10 9-10s5 10 9 10" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
     <svg viewBox="0 0 24 24" aria-label="Web"><path d="M3 5h18v14H3z M3 9h18" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>
    </div></div>
   <div><h3>Mise en page</h3><p>Grille de 12 colonnes, marges larges, beaucoup de noir. Un seul élément cuivre par composition. Les titres en capitales serrées tiennent le haut ; les infos techniques en Plex Mono, alignées comme une feuille de service.</p></div>
  </div>
 </section>

 <section class="ch" aria-labelledby="h6"><p class="cn">06</p><h2 id="h6">Mouvement</h2>
  <div class="cols">
   <div class="pane mo"><div class="ign" aria-hidden="true">{symvar('igs')}</div><button type="button" class="replay" id="replay">Rejouer l’allumage</button></div>
   <div class="txt"><h3>L’allumage</h3><p>Le geste signature de la marque. Les trois faisceaux sortent de la source l’un après l’autre (gauche, droite, puis central), comme un plateau qu’on met sous tension. 900 ms, courbe <code>cubic-bezier(0.2, 0.9, 0.1, 1)</code>, 90 ms d’écart. C’est l’ouverture de chaque vidéo et le chargement du site.</p>
   <h3>Principes</h3><ul><li><b>Tout part d’une source.</b> Les éléments apparaissent depuis un point, jamais depuis le bord de l’écran.</li><li><b>Démarrage franc, arrêt doux.</b> Comme une mise sous tension : rapide au départ, posé à l’arrivée.</li><li><b>Un seul mouvement à la fois.</b> Le reste attend.</li><li><b>Le cuivre arrive en dernier.</b> Il ponctue.</li></ul></div>
  </div>
 </section>

 <section class="ch" aria-labelledby="h7"><p class="cn">07</p><h2 id="h7">Ton de voix</h2>
  <div class="tone">
   <div><b>Direct</b><p>On dit ce qu’on fait. « Son, lumière et captation pour 800 personnes. »</p></div>
   <div><b>Technique sans jargon</b><p>« La salle sera sonorisée sans un seul larsen. » plutôt que « gestion du feedback acoustique ».</p></div>
   <div><b>Énergique</b><p>Des verbes d’action, des phrases courtes.</p></div>
   <div><b>Fiable</b><p>Pas de superlatifs : des délais, des chiffres, des engagements.</p></div>
  </div>
  <div class="dd"><div><h3>Oui</h3><p>« Votre événement, branché de la première à la dernière minute. »</p><p>« Un site qui charge vite et qui tient la charge. »</p></div><div><h3>Non</h3><p>« Nous sommes des passionnés qui créons des expériences uniques et inoubliables. »</p><p>« Solutions innovantes à 360° pour booster votre marque. »</p></div></div>
 </section>

 <section class="ch" aria-labelledby="h8"><p class="cn">08</p><h2 id="h8">Applications</h2>
  <div class="ap">
   <figure class="ap-bc"><div class="bcr">{sym(L, CU, 'bcs')}</div><div class="bcv"><span>{lk(G, CU, 'lk lk-sm')}</span><span><b>Prénom Nom</b><br>Direction de projet</span><span class="mono">+229 00 00 00 00<br>bonjour@volta.example</span></div><figcaption>Carte de visite, 85 × 55 mm, recto et verso</figcaption></figure>
   <figure class="ap-doc"><div class="doc"><div class="dh">{lk(G, CU, 'lk lk-sm')}<span class="mono">DEVIS N° 2026-014</span></div><p class="dt">Sonorisation et captation</p><p class="dl">Client · Lieu · Date</p><div class="dlines"><i></i><i></i><i style="width:70%"></i></div><div class="df mono">VOLTA · Cotonou, Bénin · volta.example</div></div><figcaption>En-tête de document, A4</figcaption></figure>
   <figure class="ap-ban"><div class="ban">{sym(L, CU, 'bans')}<p>Son · Lumière · Image</p><span>{lk(L, CU, 'lk lk-ban')}</span></div><figcaption>Kakémono événementiel, 85 × 200 cm</figcaption></figure>
   <figure class="ap-scr"><div class="scr"><span class="mono">ÉCRAN 1 · 1920 × 1080</span>{sym(L, CU, 'scrs')}<p>On démarre dans 5 minutes.</p></div><figcaption>Écran de projection d’attente</figcaption></figure>
   <figure class="ap-mail"><div class="mail"><p><b>Prénom Nom</b><br>Direction de projet</p><p class="mrow">{lk(G, CU, 'lk lk-mail')}<span>Son · Image · Motion · Web</span></p><p class="mono">+229 00 00 00 00 · volta.example</p></div><figcaption>Signature e-mail</figcaption></figure>
   <figure class="ap-post"><div class="post"><p class="pt">Branché.</p><p class="ps">Conférence annuelle · 800 personnes · son, projection, captation</p>{sym(L, CU, 'posts')}</div><figcaption>Post réseaux sociaux, 1:1</figcaption></figure>
   <figure class="ap-tee"><div class="tee"><svg viewBox="0 0 200 200" aria-hidden="true"><path d="M60 20 L35 30 L10 60 L32 78 L45 66 L45 185 L155 185 L155 66 L168 78 L190 60 L165 30 L140 20 C132 34 116 40 100 40 C84 40 68 34 60 20Z" fill="{G}"/></svg>{sym(L, CU, 'tees')}<span class="crew mono">CREW</span></div><figcaption>Tenue d’équipe : t-shirt graphite, symbole poitrine, « CREW » au dos</figcaption></figure>
  </div>
 </section>
</section>

<!-- ================= MAQUETTE ================= -->
<section class="view site" id="v-site" hidden aria-label="Maquette de la page d’accueil">
 <header class="sn"><a href="#site" class="sl" aria-label="Volta, accueil">{lkv('lk lk-nav')}</a><nav aria-label="Navigation du site"><a href="#poles">Pôles</a><a href="#signature">Signature</a><a href="#travaux">Réalisations</a><a href="#contact">Contact</a></nav><a href="#contact" class="b b-p">Parler du projet</a></header>
 <div class="hero">
  <div class="h-sym" aria-hidden="true">{symvar('hs')}</div>
  <p class="h-k mono">COTONOU · PARIS · DUBAÏ · EN LIGNE</p>
  <h1 class="h-t">On met<br>le courant.</h1>
  <div class="h-row"><p class="h-l">Son, image, motion et web, réunis dans un même studio. Pour que votre marque s’allume partout : sur scène, à l’écran et en ligne.</p>
  <div class="h-b"><a href="#contact" class="b b-p">Parler du projet</a><a href="#travaux" class="b b-s">Voir les réalisations</a></div></div>
 </div>
 <section id="poles" class="sp" aria-labelledby="sp-t"><h2 id="sp-t" class="s2">Trois pôles,<br>une seule source.</h2>
  <div class="pg">
   <article class="pl"><span class="pn mono">01 / SCÈNE</span><h3>Communication visuelle et audiovisuel</h3><p>Réseaux sociaux, supports, présence de marque. Et le jour J : sonorisation, projection, captation, location de matériel.</p><ul class="mono"><li>Sonorisation</li><li>Projection et écrans</li><li>Captation</li><li>Location</li></ul></article>
   <article class="pl"><span class="pn mono">02 / MOUVEMENT</span><h3>Motion design</h3><p>Logos animés, motion graphics, ouvertures d’événements, contenus vidéo pour les réseaux.</p><ul class="mono"><li>Logos animés</li><li>Motion graphics</li><li>Habillage d’écran</li><li>Vidéo sociale</li></ul></article>
   <article class="pl"><span class="pn mono">03 / RÉSEAU</span><h3>Sites web</h3><p>Sites vitrines et professionnels, rapides, bilingues, faciles à mettre à jour.</p><ul class="mono"><li>Sites vitrines</li><li>Sites professionnels</li><li>Maintenance</li><li>Hébergement</li></ul></article>
  </div>
 </section>
 <section id="signature" class="sig" aria-labelledby="sg-t">
  <div class="sg-sym" aria-hidden="true">{symvar('sgs')}</div>
  <div><h2 id="sg-t" class="s2">Le brand design,<br>au centre.</h2><p>Logo, couleurs, direction artistique : c’est le faisceau central. Il traverse les trois pôles, pour que votre marque ait la même voix sur une affiche, dans une vidéo, sur un écran de scène et sur votre site.</p></div>
 </section>
 <section id="travaux" class="sw2" aria-labelledby="tr-t"><div class="tw-h"><h2 id="tr-t" class="s2">Réalisations</h2><p>Emplacements prêts à recevoir vos projets.</p></div>
  <div class="wg">
   <article class="wk wk-a"><div class="ph"><span class="mono">IMAGE 16:9</span></div><h3>Titre du projet</h3><p class="mono">ÉVÉNEMENT · SON · PROJECTION</p></article>
   <article class="wk"><div class="ph"><span class="mono">IMAGE 4:5</span></div><h3>Titre du projet</h3><p class="mono">MOTION DESIGN</p></article>
   <article class="wk"><div class="ph"><span class="mono">IMAGE 4:5</span></div><h3>Titre du projet</h3><p class="mono">SITE WEB</p></article>
   <article class="wk wk-a"><div class="ph"><span class="mono">IMAGE 16:9</span></div><h3>Titre du projet</h3><p class="mono">IDENTITÉ · BRAND DESIGN</p></article>
  </div></section>
 <section id="contact" class="ct" aria-labelledby="ct-t"><h2 id="ct-t" class="s2">Votre projet,<br>sous tension.</h2>
  <form class="cf" id="cf" novalidate>
   <label for="cf-n">Nom</label><input id="cf-n" name="n" autocomplete="name" required>
   <label for="cf-e">E-mail</label><input id="cf-e" name="e" type="email" autocomplete="email" required>
   <label for="cf-p">Pôle</label><select id="cf-p" name="p"><option>Communication et audiovisuel</option><option>Motion design</option><option>Site web</option><option>Plusieurs pôles</option></select>
   <label for="cf-m">Le projet en deux phrases</label><textarea id="cf-m" name="m" rows="3"></textarea>
   <button class="b b-p" type="submit">Envoyer</button><p class="cf-s" id="cf-s" role="status"></p>
  </form></section>
 <footer class="sf">{lkv('lk lk-foot')}<p>Son · Image · Motion · Web<br>Cotonou, Bénin · clients partout</p><p class="mono">bonjour@volta.example<br>@volta</p><p class="sm">© 2026 Volta. Maquette : contenus et adresses d’exemple.</p></footer>
</section>
</main>
<script>{JS}</script>
'''
open('../volta-identite.html', 'w').write(html)
print(len(html))
