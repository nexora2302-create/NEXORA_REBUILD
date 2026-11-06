import json
src = open('gen.py').read().replace("if __name__ == '__main__':", "if False:")
exec(src)

UID = [0]
def uid():
    UID[0] += 1
    return f'k{UID[0]}'

# ---------- symboles, viewBox serrés ----------
def sym(kind, fg, acc, cls='', title=None):
    t = f'<title>{title}</title>' if title else ''
    if kind == 'courbe':
        stems, c, T, W = courbe_parts()
        return (f'<svg class="{cls}" viewBox="0 0 {W} {H}" role="img" aria-label="{title or "Symbole Courbe"}">{t}'
                f'<path d="{stems}" fill="{fg}"/><path class="draw" pathLength="1" d="{c}" fill="none" stroke="{acc}" stroke-width="{T}"/></svg>')
    if kind == 'decalage':
        a, b = x_shift(shift=120)
        return (f'<svg class="{cls}" viewBox="-10 -130 900 828" role="img" aria-label="{title or "Symbole Décalage"}">{t}'
                f'<path d="{a}" fill="{fg}"/><path class="slide" d="{b}" fill="{acc}"/></svg>')
    if kind == 'entrelacs':
        L, pad = 980, 140; size = L + 2*pad; c = size/2
        b = blade(L, 210, 0.06); m = uid(); ang = 40
        g1 = f'translate({c} {c}) rotate({-ang})'; g2 = f'translate({c} {c}) rotate({180+ang})'
        return (f'<svg class="{cls}" viewBox="{c-450} {c-410} 900 820" role="img" aria-label="{title or "Symbole Entrelacs"}">{t}'
                f'<defs><mask id="{m}" maskUnits="userSpaceOnUse" x="0" y="0" width="{size}" height="{size}"><rect width="{size}" height="{size}" fill="#fff"/>'
                f'<path d="{b}" transform="{g1}" fill="#000" stroke="#000" stroke-width="68"/></mask></defs>'
                f'<g class="spin" style="transform-origin:{c}px {c}px"><g mask="url(#{m})"><path d="{b}" transform="{g2}" fill="{acc}"/></g><path d="{b}" transform="{g1}" fill="{fg}"/></g></svg>')

def word(kind, fg, acc, cls=''):
    v = {'courbe': 'courbe', 'decalage': 'decalage', 'entrelacs': 'entrelacs', 'plain': 'plain'}[kind]
    s, W = wordmark(fg, acc, v, None, pad=0)
    # ids de masque uniques
    if 'id="m' in s:
        import re
        for old in set(re.findall(r'id="(m\d+)"', s)):
            new = uid(); s = s.replace(f'id="{old}"', f'id="{new}"').replace(f'url(#{old})', f'url(#{new})')
    return s.replace('<svg ', f'<svg class="{cls}" role="img" aria-label="NEXORA" ', 1)

def current_nx(fg, acc, cls=''):
    N='M0 0h15l24 38V0h14v64H38L15 26v38H0z'; X='M59 0h16l11.5 20L98 0h16L94.5 31.5 115 64H99L86.5 43 74 64H58l20.5-32.5z'
    return f'<svg class="{cls}" viewBox="0 0 116 64" role="img" aria-label="Logo actuel NX"><path fill="{fg}" d="{N}"/><path fill="{acc}" d="{X}"/></svg>'

# ---------- schémas de construction ----------
def construction_courbe():
    stems, c, T, W = courbe_parts()
    x0, x1 = 232, W - 232; y0, y1 = T/2, H - T/2; dx = x1 - x0
    p1 = (x0 + .83*dx, y0); p2 = (x0 + .17*dx, y1)
    grid = ''.join(f'<line x1="{x}" y1="-60" x2="{x}" y2="{H+60}"/>' for x in range(0, W+1, 120)) + \
           ''.join(f'<line x1="-60" y1="{y}" x2="{W+60}" y2="{y}"/>' for y in range(0, H+1, 86))
    return f'''<svg class="diagram" viewBox="-120 -120 {W+240} {H+260}" role="img" aria-label="Construction du symbole Courbe">
<g stroke="var(--line)" stroke-width="2">{grid}</g>
<path d="{stems}" fill="var(--ghost)"/><path d="{c}" fill="none" stroke="var(--ghost-acc)" stroke-width="{T}"/>
<path d="{c}" fill="none" stroke="var(--ember)" stroke-width="5"/>
<g stroke="var(--fg)" stroke-width="4"><line x1="{x0}" y1="{y0}" x2="{p1[0]:.0f}" y2="{p1[1]:.0f}"/><line x1="{x1}" y1="{y1}" x2="{p2[0]:.0f}" y2="{p2[1]:.0f}"/></g>
<g fill="var(--fg)"><circle cx="{x0}" cy="{y0}" r="15"/><circle cx="{x1}" cy="{y1}" r="15"/></g>
<g fill="var(--bg)" stroke="var(--fg)" stroke-width="5"><circle cx="{p1[0]:.0f}" cy="{p1[1]:.0f}" r="17"/><circle cx="{p2[0]:.0f}" cy="{p2[1]:.0f}" r="17"/></g>
<g class="dlabel"><text x="{p1[0]+30:.0f}" y="{p1[1]-34:.0f}">0,83 ; 0</text><text x="{p2[0]-30:.0f}" y="{p2[1]+70:.0f}" text-anchor="end">0,17 ; 1</text>
<text x="116" y="{H+110}" text-anchor="middle">fût 232</text><text x="{W-116}" y="{H+110}" text-anchor="middle">fût 232</text><text x="{W/2}" y="-60" text-anchor="middle">bande 214</text></g></svg>'''

def construction_decalage():
    a, b = x_shift(shift=120)
    return f'''<svg class="diagram" viewBox="-160 -260 1340 1060" role="img" aria-label="Construction du symbole Décalage">
<g stroke="var(--line)" stroke-width="3"><line x1="-140" y1="0" x2="1020" y2="0"/><line x1="-140" y1="688" x2="1020" y2="688"/></g>
<path d="{a}" fill="var(--ghost)"/><path d="{b}" fill="none" stroke="var(--ember)" stroke-width="5" stroke-dasharray="14 12"/>
<path d="{a.replace('M0 0','M0 0')}" fill="none"/><g transform="translate(0 0)"><path d="M630 0H880L250 688H0Z" fill="none" stroke="var(--fg)" stroke-width="4"/></g>
<g stroke="var(--fg)" stroke-width="5" fill="none"><path d="M960 0V-120M940 -95l20 -25 20 25"/></g>
<g class="dlabel"><text x="-140" y="-30">hauteur de capitale</text><text x="-140" y="740">ligne de base</text><text x="990" y="-50">−120</text><text x="990" y="-10">soit 1/6</text></g></svg>'''

def construction_entrelacs():
    return f'''<svg class="diagram" viewBox="-560 -520 1120 1040" role="img" aria-label="Construction du symbole Entrelacs">
<g stroke="var(--line)" stroke-width="3" fill="none"><circle r="490"/><line x1="-540" y1="0" x2="540" y2="0"/><line x1="0" y1="-500" x2="0" y2="500"/></g>
<g transform="rotate(-40)"><path d="{blade(980,210,0.06)}" fill="var(--ghost)"/></g><g transform="rotate(220)"><path d="{blade(980,210,0.06)}" fill="none" stroke="var(--ember)" stroke-width="5"/></g>
<path d="M200 0A200 200 0 0 0 153 -128" fill="none" stroke="var(--fg)" stroke-width="5"/><path d="M200 0A200 200 0 0 1 153 128" fill="none" stroke="var(--fg)" stroke-width="5"/>
<g class="dlabel"><text x="230" y="-80">40°</text><text x="230" y="110">40°</text><text x="-520" y="-450">lame : 980 × 210</text><text x="-520" y="490">passage : 34</text></g></svg>'''

# ---------- briques de planche ----------
def tile(content, bg, cls='', label=''):
    lab = f'<span class="tlabel">{label}</span>' if label else ''
    return f'<figure class="tile {cls}" style="--tbg:{bg}">{content}{lab}</figure>'

def icon(kind, bg, fg, acc, shape='round'):
    return f'<span class="appicon {shape}" style="background:{bg}">{sym(kind, fg, acc, "isym")}</span>'

def favicons(kind):
    out = ''
    for px in (64, 32, 16):
        out += f'<span class="fav" style="--px:{px}px"><span class="favbox">{sym(kind, BONE, EMBER, "fsym")}</span><small>{px} px</small></span>'
    return out

def header_mock(kind, mode='word'):
    logo = word(kind, BONE, EMBER, 'hword') if mode == 'word' else sym(kind, BONE, EMBER, 'hsym')
    return f'''<div class="mock mock-head"><span class="mlogo">{logo}</span><span class="mnav"><i>Studio</i><i>Expertises</i><i>Réalisations</i><i>Méthode</i></span><span class="mcta">Démarrer un projet</span></div>'''

def footer_mock(kind):
    return f'''<div class="mock mock-foot"><span class="mlogo">{sym(kind, INK, DEEP, 'fsym2')}</span><span class="mfoot">Studio créatif · Cotonou, Bénin</span><span class="mfoot">© 2026</span></div>'''

def tab_mock(kind):
    return f'''<div class="tabmock"><span class="tab"><span class="tabicon">{sym(kind, BONE, EMBER, 'tsym')}</span><span>NEXORA, studio créatif</span><span class="x">×</span></span></div>'''

def direction(num, kind, name, idea, concept, logic, evolution, plus, minus, construction, motion_note, header_mode='word'):
    p = ''.join(f'<li>{x}</li>' for x in plus); m = ''.join(f'<li>{x}</li>' for x in minus)
    return f'''
<section class="dir" id="{kind}">
  <header class="dir-head">
    <p class="dir-num">Piste {num}</p>
    <h2>{name}</h2>
    <p class="dir-idea">{idea}</p>
  </header>

  <div class="hero-grid">
    {tile(sym(kind, BONE, EMBER, 'big', f'Symbole {name}'), INK, 'hero-sym motion')}
    {tile(word(kind, INK, DEEP, 'wd'), BONE, 'hero-word', 'Logotype, fond os')}
    {tile(word(kind, BONE, EMBER, 'wd'), INK, 'hero-word', 'Logotype, fond encre')}
  </div>

  <div class="two">
    <div class="text">
      <h3>Concept</h3><p>{concept}</p>
      <h3>Logique graphique</h3><p>{logic}</p>
      <h3>Mouvement</h3><p>{motion_note}</p>
    </div>
    <figure class="construct">{construction}<figcaption>Construction, unités de la fonte (hauteur de capitale 688)</figcaption></figure>
  </div>

  <h3 class="sub">Déclinaisons</h3>
  <div class="variants">
    {tile(sym(kind, BONE, EMBER, 'mid'), INK, '', 'Couleur, fond encre')}
    {tile(sym(kind, INK, DEEP, 'mid'), BONE, '', 'Couleur, fond os')}
    {tile(sym(kind, INK, INK, 'mid'), EMBER, '', 'Fond braise')}
    {tile(sym(kind, INK, INK, 'mid'), '#ffffff', '', 'Noir sur blanc')}
    {tile(sym(kind, '#ffffff', '#ffffff', 'mid'), '#000000', '', 'Blanc sur noir')}
  </div>

  <h3 class="sub">Petites tailles, icônes, contexte</h3>
  <div class="context">
    <div class="ctx-col">
      <div class="favs">{favicons(kind)}</div>
      {tab_mock(kind)}
      <div class="icons">{icon(kind, INK, BONE, EMBER)}{icon(kind, EMBER, INK, INK)}{icon(kind, BONE, INK, DEEP, 'circle')}<small>Icône d'application, avatar</small></div>
    </div>
    <div class="ctx-col">
      {header_mock(kind, header_mode)}
      {footer_mock(kind)}
    </div>
  </div>

  <div class="verdict">
    <div><h3>Forces</h3><ul>{p}</ul></div>
    <div><h3>Limites</h3><ul>{m}</ul></div>
    <div><h3>Évolution possible</h3><p>{evolution}</p></div>
  </div>
</section>'''

D1 = direction('1', 'courbe', 'Courbe',
  'Le N de NEXORA dessiné par la courbe d’animation du studio.',
  'Le N est fait de deux fûts et d’une bande. Cette bande n’est pas une diagonale droite : c’est la courbe d’accélération exacte qui anime tout le site, <em>ease-in-out</em>, le geste de base du motion design. Le symbole montre ce que fait NEXORA : prendre une forme fixe et la mettre en mouvement. Il ne s’explique pas par une icône, il se reconnaît par sa silhouette.',
  'Fûts verticaux de la largeur des fûts d’Archivo, bande de 214 unités guidée par une courbe de Bézier aux poignées 0,83 et 0,17. La bande part à plat du haut du premier fût, plonge, et arrive à plat au pied du second. En couleur, la bande est braise ; en monochrome, la lettre devient une seule silhouette, sans perte de lecture.',
  'La courbe devient un outil : elle sert de trait de soulignement, de forme de transition entre pages, de motif de chargement. Le symbole peut se dessiner, se tendre ou se relâcher selon le rythme d’une vidéo.',
  ['Concept propre au métier, invisible chez un concurrent', 'Reconnaissable sans lire le nom, même à 16 px', 'Fonctionne aussi bien en une couleur qu’en deux', 'Relie le logo au site : même courbe, même typo'],
  ['Les monogrammes en N existent ailleurs ; la courbe doit rester assez marquée pour s’en distinguer', 'L’idée de la courbe d’animation demande une phrase d’explication la première fois'],
  construction_courbe(),
  'À l’apparition, la bande se dessine d’un fût à l’autre en suivant sa propre courbe, en 0,9 s. Au survol du logo, elle se retend.')

D2 = direction('2', 'decalage', 'Décalage',
  'Un logotype dessiné où le X a bougé d’une image.',
  'Le mot NEXORA est composé serré, dans la typo du site, et une seule chose a changé : la branche montante du X a glissé vers le haut, comme une image clé décalée dans une animation. Le mot semble avoir été saisi en plein mouvement. Le X devient le symbole autonome.',
  'Deux branches parallélogrammes de 250 unités. La branche descendante tient sur la ligne de base ; la montante est relevée d’un sixième de la hauteur de capitale, ce qui la fait dépasser au-dessus du mot. Le décalage reste assez franc pour ne pas passer pour une erreur d’impression.',
  'Le décalage peut varier selon le support (plus fort sur une affiche, discret sur une facture) et devenir une règle de mise en page : un élément par composition qui sort de l’alignement.',
  ['Logotype très lisible, d’une seule pièce', 'Raconte le mouvement sans aucun ajout graphique', 'Simple à appliquer sur tous les supports'],
  ['Un X isolé évoque immédiatement d’autres marques, à commencer par le réseau X', 'En petit, le décalage peut se lire comme une coquille', 'Symbole moins propriétaire que les deux autres pistes'],
  construction_decalage(),
  'La branche braise glisse en place depuis l’alignement, puis rebondit légèrement : le mot « bouge » une fois, et se fige.')


import base64 as _b64
from entfinal import symbol as esym, symbol_t as esym_t, small as esmall, animated as eanim, display_word as edisplay, plain_word as eplain, blade as eblade, INK as _I, BONE as _B, EMBER as _E, RUST as _R, DEEP as _D
_poster = 'data:image/webp;base64,' + _b64.b64encode(open('/home/user/nexora_rebuild/NEXORA-REBUILD/02_NEXORA_WORKING/public/hero/x-sculpt-sm.webp','rb').read()).decode()

def ecss(svg, cls):
    return svg.replace('<svg class=""', f'<svg class="{cls}"', 1) if '<svg class=""' in svg else svg.replace('<svg ', f'<svg class="{cls}" ', 1)

def e_construction():
    sil, up, lo, mid = eblade()
    sil2 = eblade(k=-1.6)[0]
    return f"""<svg class="diagram" viewBox="-620 -380 1240 760" role="img" aria-label="Construction du symbole Entrelacs">
<g stroke="var(--line)" stroke-width="3" fill="none"><line x1="-600" y1="0" x2="600" y2="0"/><line x1="0" y1="-360" x2="0" y2="360"/></g>
<polygon points="{up}" fill="var(--ghost)"/><polygon points="{lo}" fill="var(--ghost-acc)"/>
<polyline points="{' '.join(f'{x:.0f},{y:.0f}' for x,y in mid)}" fill="none" stroke="var(--ember)" stroke-width="6"/>
<polygon points="{sil}" fill="none" stroke="var(--fg)" stroke-width="4"/>
<g class="dlabel"><text x="-590" y="-300">lame : 1000 × 240, pointes effilées</text><text x="-590" y="330">ligne de torsion : tanh, du bord haut au bord bas</text>
<text x="300" y="-150">face os</text><text x="-420" y="150">tranche braise</text></g></svg>"""

def stage3d(color, bg, fallback, zoom='1'):
    return f"""<figure class="tile stage" style="--tbg:{bg}"><div class="stage-fallback">{fallback}</div><canvas data-x3d data-color="{color}" data-zoom="{zoom}" aria-hidden="true"></canvas></figure>"""

PALETTES = [
  ('Os et braise, fond encre', esym(bg=_I), _I),
  ('Laque, fond os', esym(a=(_I, _E), b=('#4a4239', _D), bg=_B), _B),
  ('Braise, fond braise', esym(a=(_I, '#3a1206'), b=('#3a1206', _I), bg=_E), _E),
  ('Tranche, variante calme', esym(a=(_B, _E), b=('#3a3530', _E), bg=_I, kind='band'), _I),
  ('Noir sur blanc', esym(bg='#ffffff', mono=_I, gapcol='#ffffff'), '#ffffff'),
  ('Blanc sur noir', esym(bg='#000000', mono='#ffffff', gapcol='#000000'), '#000000'),
]
_pal = ''.join(f'<figure class="tile pal" style="--tbg:{bg}">{ecss(s, "mid")}<span class="tlabel">{n}</span></figure>' for n, s, bg in PALETTES)
_favs = ''.join(f'<span class="fav" style="--px:{px}px"><span class="favbox" style="background:none;outline:0">{ecss(esmall() if px <= 32 else esym(bg=_I), "fsymfull")}</span><small>{px} px</small></span>' for px in (64, 32, 16))

D3 = f"""
<section class="dir" id="entrelacs">
  <header class="dir-head">
    <p class="dir-num">Piste 3, approfondie</p>
    <h2>Entrelacs</h2>
    <p class="dir-idea">Le X du hero mis à plat : deux rubans qui se tordent et se croisent.</p>
  </header>

  <div class="hero-grid">
    {stage3d('0c0a09', '#0d0c0b', ecss(esym(bg=_I), 'big'))}
    <figure class="tile hero-word" style="--tbg:#ece5d8"><span class="lockup">{ecss(esym_t(a=(_I, _E), b=('#4a4239', _D)), 'lsym')}{ecss(eplain(_I), 'lword')}</span><span class="tlabel">Logo complet, fond os</span></figure>
    <figure class="tile hero-word" style="--tbg:#0d0c0b">{ecss(edisplay(_B, (_B, _E), (_E, _R)), 'wd')}<span class="tlabel">Mot signature, comme dans le hero</span></figure>
  </div>
  <p class="note">Le grand panneau est animé en 3D temps réel avec les mêmes rubans que la sculpture du site : dépliage à l’arrivée, respiration, tour complet toutes les 9 s, orientation vers le pointeur.</p>

  <h3 class="sub">Du volume au plat</h3>
  <div class="steps">
    <figure class="tile" style="--tbg:#0d0c0b"><img src="{_poster}" alt="Sculpture X du hero" class="poster"><span class="tlabel">La sculpture du hero</span></figure>
    <figure class="tile" style="--tbg:#0d0c0b">{ecss(esym(bg=_I), 'mid')}<span class="tlabel">Le symbole : face os, tranche braise</span></figure>
    <figure class="tile" style="--tbg:#0d0c0b">{ecss(esmall(), 'mid')}<span class="tlabel">Version réduite, 32 px et moins</span></figure>
  </div>

  <div class="two">
    <div class="text">
      <h3>Concept</h3><p>Le logo et la sculpture du hero deviennent un seul objet. Deux rubans se croisent en X : deux métiers qui se rencontrent, une marque et son studio, une idée et sa mise en forme. Chaque ruban se tord, on voit sa face os puis sa tranche braise, comme sur le site quand la lumière glisse sur la laque. Le logo n’est plus un dessin à côté du site : c’est l’image arrêtée de son animation.</p>
      <h3>Logique graphique</h3><p>Deux lames identiques de 1000 × 240 unités, inclinées à ±40°, pointes effilées. Une ligne de torsion en tangente hyperbolique traverse chaque lame d’un bord à l’autre et sépare la face os de la tranche braise. La lame arrière est plus sombre (braise et rouille) : la profondeur vient de la couleur, sans ombre ni dégradé. Un passage de 30 unités marque le dessus et le dessous. Sous 32 px, une version réduite garde les deux lames pleines et un passage élargi.</p>
      <h3>Mouvement</h3><p>Deux niveaux, la même chorégraphie. En 3D (hero, écrans d’accueil, vidéo) : dépliage, respiration, tour complet. En SVG léger (en-tête, chargement) : les rubans respirent en se tordant, puis le X fait un demi-tour avec la courbe d’accélération du site.</p>
    </div>
    <figure class="construct">{e_construction()}<figcaption>Construction d’une lame, unités de dessin</figcaption></figure>
  </div>

  <h3 class="sub">Agencements de couleurs</h3>
  <div class="palettes">{_pal}</div>

  <h3 class="sub">Animation</h3>
  <div class="anims">
    {stage3d('0c0a09', '#ece5d8', ecss(esym(a=(_I, _E), b=('#4a4239', _D), bg=_B), 'big'), '1.05')}
    <div class="anim-light">
      <figure class="tile" style="--tbg:#0d0c0b">{ecss(eanim(), 'mid')}<span class="tlabel">SVG léger, en boucle</span></figure>
      <div class="anim-sizes">{ecss(eanim(), 'a48')}{ecss(eanim(), 'a24')}<span>48 et 24 px : en-tête, menu, chargement</span></div>
    </div>
  </div>
  <p class="note">À gauche, la 3D sur fond os (laque d’encre, reflets os et braise). À droite, l’animation sans WebGL : quelques kilo-octets, utilisable dans l’en-tête et comme indicateur de chargement.</p>

  <h3 class="sub">Petites tailles, icônes, contexte</h3>
  <div class="context">
    <div class="ctx-col">
      <div class="favs">{_favs}</div>
      <div class="tabmock"><span class="tab"><span class="tabicon">{ecss(esmall(), 'tsym')}</span><span>NEXORA, studio créatif</span><span class="x">×</span></span></div>
      <div class="icons"><span class="appicon">{ecss(esym(bg=_I), 'fill')}</span><span class="appicon">{ecss(esym(a=(_I, '#3a1206'), b=('#3a1206', _I), bg=_E), 'fill')}</span><span class="appicon circle">{ecss(esym(a=(_I, _E), b=('#4a4239', _D), bg=_B), 'fill')}</span><small>Icône d’application, avatar</small></div>
    </div>
    <div class="ctx-col">
      <div class="mock mock-head"><span class="mlogo hl">{ecss(esym_t(), 'hsym')}{ecss(eplain(_B), 'hword')}</span><span class="mnav"><i>Studio</i><i>Expertises</i><i>Réalisations</i><i>Méthode</i></span><span class="mcta">Démarrer un projet</span></div>
      <div class="mock mock-foot"><span class="mlogo hl">{ecss(esym_t(a=(_I, _E), b=('#4a4239', _D)), 'fsym2')}{ecss(eplain(_I), 'hword')}</span><span class="mfoot">Studio créatif · Cotonou, Bénin</span><span class="mfoot">© 2026</span></div>
      <div class="changes"><h3>Ce qui change sur le site</h3><ul><li>Le logo de l’en-tête, du menu mobile et du pied de page.</li><li>Le favicon, l’icône Apple et l’image de partage.</li><li>Rien d’autre : la sculpture du hero est déjà ce logo en volume. Couleurs, typos, sections et animations restent identiques.</li></ul></div>
    </div>
  </div>

  <div class="verdict">
    <div><h3>Forces</h3><ul><li>Continuité totale avec le hero : le site n’a pas besoin d’être repensé</li><li>Un symbole abstrait et propriétaire, qui se reconnaît sans lire le nom</li><li>Deux niveaux d’animation cohérents, du WebGL au SVG léger</li><li>Plusieurs agencements de couleurs, tous dans la palette existante</li></ul></div>
    <div><h3>Limites</h3><ul><li>Dessin plus riche que les deux autres pistes : il faut la version réduite sous 32 px</li><li>Dans le mot NEXORA, le symbole se lit comme un X seulement en grand ; en petit, préférer le logo complet (symbole + nom)</li><li>À vérifier : l’antériorité des marques à deux lames croisées</li></ul></div>
    <div><h3>Évolution possible</h3><p>Le symbole devient le point d’entrée de toute la marque : intro de vidéos, transitions entre pages, chargement, objets imprimés en volume. La torsion peut porter une couleur différente par métier (identité, motion, web) sans changer la forme.</p></div>
  </div>
</section>"""
rows = [
 ('Intelligence du concept', 5, 3, 5),
 ('Mémorisation sans lire le nom', 5, 3, 4),
 ('Lisibilité à 16 px', 4, 4, 4),
 ('Noir et blanc', 5, 4, 4),
 ('Continuité avec le site actuel', 4, 3, 5),
 ('Durée de vie (5 ans et plus)', 5, 3, 5),
 ('Risque de confusion', 4, 2, 3),
]
def dots(n): return '<span class="dots" aria-label="'+str(n)+' sur 5">' + ''.join(f'<i class="{"on" if k < n else ""}"></i>' for k in range(5)) + '</span>'
table = ''.join(f'<tr><th scope="row">{r[0]}</th><td>{dots(r[1])}</td><td>{dots(r[2])}</td><td>{dots(r[3])}</td></tr>' for r in rows)
tot = [sum(r[i] for r in rows) for i in (1,2,3)]

X3D = open('x3d.js').read()
html = f'''<title>Logo NEXORA</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Instrument+Serif:ital@1&display=swap">
<style>
/* Planche de présentation sombre, dans l'univers NEXORA : encre, os, braise ; panneaux clairs pour tester chaque fond. */
:root {{
  --bg: #0d0c0b; --fg: #ece5d8; --muted: #a69f92; --card: #161412; --line: #2a2622; --ember: #ff4a1c;
  --ghost: #24201c; --ghost-acc: #3a1a10;
  --display: "Archivo", "Arial Black", system-ui, sans-serif; --serif: "Instrument Serif", Georgia, serif;
  color-scheme: dark;
}}
* {{ box-sizing: border-box }}
body {{ background: var(--bg); color: var(--fg); font: 400 16px/1.55 var(--display); padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 0 96px; -webkit-font-smoothing: antialiased }}
.wrap {{ max-width: 1240px; margin: 0 auto }}
h1, h2, h3 {{ text-wrap: balance; margin: 0 }}
p {{ margin: 0 }}
em {{ font-family: var(--serif); font-size: 1.12em }}
.intro {{ padding-block: 72px 40px; display: grid; gap: 28px }}
.intro h1 {{ font-size: clamp(2.6rem, 7vw, 6rem); font-weight: 900; font-stretch: 125%; line-height: .92; letter-spacing: -.04em }}
.intro h1 span {{ color: var(--ember) }}
.lead {{ font-size: clamp(1.1rem, 1.6vw, 1.3rem); max-width: 60ch; color: var(--fg) }}
.index {{ display: flex; flex-wrap: wrap; gap: 10px }}
.index a {{ color: var(--fg); text-decoration: none; border: 1px solid var(--line); border-radius: 999px; padding: 8px 16px; font-weight: 600 }}
.index a:hover, .index a:focus-visible {{ border-color: var(--ember); outline: none }}
.start {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.4fr); gap: 32px; align-items: center; background: var(--card); border-radius: 28px; padding: 32px }}
.start .tile {{ min-height: 220px }}
.start h2 {{ font-size: 1.6rem; font-weight: 800; font-stretch: 112% }}
.start ul {{ margin: 12px 0 0; padding-left: 1.1em; display: grid; gap: 6px }}
.dir {{ padding-top: 120px; display: grid; gap: 28px }}
.dir-head {{ display: grid; gap: 10px }}
.dir-num {{ color: var(--ember); font-weight: 700; letter-spacing: .04em }}
.dir h2 {{ font-size: clamp(3rem, 9vw, 7.5rem); font-weight: 900; font-stretch: 125%; line-height: .9; letter-spacing: -.045em }}
.dir-idea {{ font-family: var(--serif); font-style: italic; font-size: clamp(1.4rem, 2.6vw, 2.2rem); line-height: 1.15; max-width: 30ch }}
.hero-grid {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.25fr); grid-template-rows: auto auto; gap: 12px }}
.hero-sym {{ grid-row: span 2; min-height: 420px }}
.tile {{ margin: 0; position: relative; background: var(--tbg); box-shadow: inset 0 0 0 1px var(--line); border-radius: 22px; display: grid; place-items: center; padding: 40px; min-height: 200px; overflow: hidden }}
.tlabel {{ position: absolute; left: 16px; bottom: 12px; font-size: 12px; font-weight: 600; color: #8f887c; mix-blend-mode: difference }}
.big {{ width: min(62%, 320px); height: auto }}
.wd {{ width: 100%; height: auto; max-height: 110px }}
.mid {{ width: 56%; max-width: 120px; height: auto }}
.two {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 40px; align-items: start }}
.text {{ display: grid; gap: 10px; max-width: 62ch }}
.text h3, .sub, .verdict h3 {{ font-size: .95rem; font-weight: 700; color: var(--ember); letter-spacing: .02em }}
.text h3:not(:first-child) {{ margin-top: 14px }}
.construct {{ margin: 0; background: var(--card); border-radius: 22px; padding: 20px; display: grid; gap: 8px }}
.diagram {{ width: 100%; height: auto }}
.dlabel text {{ fill: var(--muted); font: 600 34px var(--display) }}
figcaption {{ font-size: 13px; color: var(--muted) }}
.sub {{ margin-top: 8px }}
.variants {{ display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 12px }}
.variants .tile {{ min-height: 170px; padding: 24px }}
.context {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.3fr); gap: 12px }}
.ctx-col {{ display: grid; gap: 12px; align-content: start }}
.favs {{ background: var(--card); border-radius: 22px; padding: 24px; display: flex; gap: 28px; align-items: end }}
.fav {{ display: grid; gap: 8px; justify-items: center; color: var(--muted); font-size: 12px }}
.favbox {{ width: var(--px); height: var(--px); background: #0d0c0b; border-radius: calc(var(--px) * .22); display: grid; place-items: center; outline: 1px solid var(--line) }}
.fsym {{ width: 74%; height: 74% }}
.tabmock {{ background: #1f1c19; border-radius: 16px; padding: 10px 10px 0 }}
.tab {{ display: inline-flex; align-items: center; gap: 10px; background: #2c2824; border-radius: 10px 10px 0 0; padding: 9px 14px; font-size: 13px; color: #ddd5c8 }}
.tabicon {{ width: 16px; height: 16px; display: grid; place-items: center }}
.tsym {{ width: 16px; height: 16px }}
.tab .x {{ color: #8a8378 }}
.icons {{ background: var(--card); border-radius: 22px; padding: 24px; display: flex; gap: 18px; align-items: center; flex-wrap: wrap }}
.icons small {{ color: var(--muted) }}
.appicon {{ width: 76px; height: 76px; display: grid; place-items: center; border-radius: 18px }}
.appicon.circle {{ border-radius: 50% }}
.isym {{ width: 60%; height: 60% }}
.mock {{ border-radius: 18px; display: flex; align-items: center; gap: 24px; padding: 0 22px; min-height: 72px }}
.mock-head {{ background: #0d0c0b; outline: 1px solid var(--line); color: #ece5d8 }}
.mlogo {{ display: flex; align-items: center }}
.hword {{ height: 15px; width: auto }}
.hsym {{ height: 22px; width: auto }}
.mnav {{ display: flex; gap: 20px; font-size: 13px; margin-left: auto }}
.mnav i {{ font-style: normal }}
.mcta {{ background: #ff4a1c; color: #0d0c0b; font-weight: 700; font-size: 13px; border-radius: 999px; padding: 8px 14px; white-space: nowrap }}
.mock-foot {{ background: #ece5d8; color: #0d0c0b; font-size: 13px; justify-content: space-between }}
.fsym2 {{ height: 26px; width: auto }}
.mfoot {{ color: #4f493f }}
.verdict {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 28px; background: var(--card); border-radius: 22px; padding: 28px }}
.verdict ul {{ margin: 10px 0 0; padding-left: 1.1em; display: grid; gap: 8px }}
.verdict p {{ margin-top: 10px }}
.compare {{ padding-top: 120px; display: grid; gap: 24px }}
.compare h2 {{ font-size: clamp(2.2rem, 5vw, 4rem); font-weight: 900; font-stretch: 125%; letter-spacing: -.04em; line-height: .95 }}
.tablewrap {{ overflow-x: auto; background: var(--card); border-radius: 22px; padding: 12px 20px }}
table {{ width: 100%; border-collapse: collapse; min-width: 560px; font-variant-numeric: tabular-nums }}
th, td {{ text-align: left; padding: 14px 10px; border-bottom: 1px solid var(--line) }}
thead th {{ font-weight: 800; font-stretch: 112% }}
tbody th {{ font-weight: 500 }}
tfoot td, tfoot th {{ border: 0; font-weight: 800 }}
.dots {{ display: inline-flex; gap: 5px }}
.dots i {{ width: 11px; height: 11px; border-radius: 50%; background: var(--line) }}
.dots i.on {{ background: var(--ember) }}
.reco {{ padding-top: 120px; display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 40px; align-items: center }}
.reco .tile {{ min-height: 420px }}
.reco h2 {{ font-size: clamp(2rem, 3.4vw, 3rem); font-weight: 900; font-stretch: 125%; letter-spacing: -.035em; line-height: .98; margin-bottom: 8px }}
.reco .text p + p {{ margin-top: 10px }}
.reco ol {{ margin: 14px 0 0; padding-left: 1.2em; display: grid; gap: 8px }}
.note {{ color: var(--muted); font-size: 14px }}
.stage {{ padding: 0; grid-row: span 2; min-height: 460px }}
.stage canvas {{ position: absolute; inset: 0; width: 100%; height: 100%; opacity: 0; transition: opacity 1s }}
.stage canvas.on {{ opacity: 1 }}
.stage canvas.on ~ * {{ display: none }}
.stage-fallback {{ position: absolute; inset: 0; display: grid; place-items: center }}
.stage canvas.on + .x {{ display: none }}
.lockup {{ display: flex; align-items: center; gap: 4%; width: 100% }}
.lsym {{ height: 120px; width: auto; flex: none }}
.lword {{ height: 62px; width: auto; min-width: 0; flex: 1 1 auto; max-width: 70% }}
.big-lockup .lsym {{ height: 150px }} .big-lockup .lword {{ height: 70px }}
.steps {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px }}
.steps .tile {{ min-height: 260px; padding: 28px }}
.poster {{ width: auto; height: 200px; max-width: 100% }}
.palettes {{ display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 12px }}
.palettes .tile {{ min-height: 180px; padding: 20px 20px 36px }}
.palettes .mid {{ width: 78%; max-width: 150px }}
.anims {{ display: grid; grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr); gap: 12px }}
.anims .stage {{ grid-row: auto; min-height: 420px }}
.anim-light {{ display: grid; gap: 12px }}
.anim-light .tile {{ min-height: 260px }}
.anim-light .mid {{ width: 50%; max-width: 200px }}
.anim-sizes {{ background: var(--card); border-radius: 22px; padding: 22px; display: flex; align-items: center; gap: 18px; color: var(--muted); font-size: 13px }}
.a48 {{ width: 48px; height: 48px; border-radius: 10px }} .a24 {{ width: 24px; height: 24px; border-radius: 5px }}
.fsymfull {{ width: 100%; height: 100%; border-radius: calc(var(--px) * .22) }}
.appicon .fill {{ width: 100%; height: 100%; border-radius: inherit }}
.appicon {{ overflow: hidden; padding: 0 }}
.hl {{ gap: 10px }} .hl .hsym {{ height: 26px }} .hl .fsym2 {{ height: 28px; width: auto }}
.changes {{ background: var(--card); border-radius: 22px; padding: 22px }}
.changes h3 {{ font-size: .95rem; color: var(--ember) }}
.changes ul {{ margin: 10px 0 0; padding-left: 1.1em; display: grid; gap: 6px }}
@media (prefers-reduced-motion: reduce) {{ .anim animate, .anim animateTransform {{ display: none }} }}
@media (max-width: 860px) {{ .steps, .anims {{ grid-template-columns: minmax(0, 1fr) }} .palettes {{ grid-template-columns: repeat(2, minmax(0, 1fr)) }} .lsym {{ height: 72px }} .lword {{ height: 36px }} }}
/* mouvement */
.motion .draw {{ stroke-dasharray: 1; animation: draw 4.2s cubic-bezier(.83,0,.17,1) infinite }}
@keyframes draw {{ 0% {{ stroke-dashoffset: 1 }} 35%, 100% {{ stroke-dashoffset: 0 }} }}
.motion .slide {{ animation: slide 3.6s cubic-bezier(.16,1,.3,1) infinite }}
@keyframes slide {{ 0%, 12% {{ transform: translateY(120px) }} 45%, 100% {{ transform: none }} }}
.motion .spin {{ animation: spin 5s cubic-bezier(.83,0,.17,1) infinite }}
@keyframes spin {{ 0%, 55% {{ transform: rotate(0) }} 85%, 100% {{ transform: rotate(90deg) }} }}
@media (prefers-reduced-motion: reduce) {{ .motion .draw, .motion .slide, .motion .spin {{ animation: none }} }}
@media (max-width: 860px) {{
  .start, .two, .reco, .context {{ grid-template-columns: minmax(0, 1fr) }}
  .hero-grid {{ grid-template-columns: minmax(0, 1fr) }}
  .hero-sym {{ grid-row: auto; min-height: 300px }}
  .variants {{ grid-template-columns: repeat(2, minmax(0, 1fr)) }}
  .verdict {{ grid-template-columns: minmax(0, 1fr) }}
  .mnav {{ display: none }}
}}
</style>
<div class="wrap">
  <header class="intro">
    <h1>Trois signatures pour <span>NEXORA</span></h1>
    <p class="lead">Exploration du logo, deuxième tour. La piste 3, Entrelacs, est approfondie pour se rapprocher de la sculpture du hero : nouveau dessin, agencements de couleurs, animation 3D et animation légère. Les pistes 1 et 2 restent présentées pour comparaison.</p>
    <nav class="index" aria-label="Pistes"><a href="#entrelacs">3. Entrelacs, approfondie</a><a href="#courbe">1. Courbe</a><a href="#decalage">2. Décalage</a><a href="#comparaison">Comparaison</a><a href="#recommandation">Recommandation</a></nav>
  </header>

  <section class="start" aria-labelledby="depart">
    {tile(current_nx(BONE, EMBER, 'big'), INK)}
    <div>
      <h2 id="depart">Point de départ&nbsp;: le monogramme NX actuel</h2>
      <ul>
        <li>Deux initiales posées côte à côte dans une typo existante : il nomme la marque mais ne raconte rien sur elle.</li>
        <li>Rien ne le distingue d’un autre « NX » ; il n’est pas reconnaissable sans le contexte du site.</li>
        <li>À garder pour la suite : l’accent braise, Archivo en largeur 125 et graisse 900, l’idée que la marque parle de mouvement.</li>
      </ul>
    </div>
  </section>

  {D3}
  {D1}
  {D2}

  <section class="compare" id="comparaison" aria-labelledby="cmp">
    <h2 id="cmp">Comparaison</h2>
    <div class="tablewrap"><table>
      <thead><tr><th scope="col">Critère</th><th scope="col">Courbe</th><th scope="col">Décalage</th><th scope="col">Entrelacs</th></tr></thead>
      <tbody>{table}</tbody>
      <tfoot><tr><th scope="row">Total sur 35</th><td>{tot[0]}</td><td>{tot[1]}</td><td>{tot[2]}</td></tr></tfoot>
    </table></div>
    <p class="note">Notes de 1 à 5. Pour « Risque de confusion », 5 signifie peu de risque.</p>
  </section>

  <section class="reco" id="recommandation" aria-labelledby="rec">
    <figure class="tile" style="--tbg:#0d0c0b"><span class="lockup big-lockup">{ecss(esym_t(), 'lsym')}{ecss(eplain(BONE), 'lword')}</span></figure>
    <div class="text">
      <h2 id="rec">Direction retenue&nbsp;: Entrelacs</h2>
      <p>Approfondie, la piste 3 répond le mieux à votre objectif : changer de logo sans refaire le site. La sculpture du hero devient le logo en volume, et le logo devient l’image arrêtée de la sculpture. Une seule forme, du favicon à la 3D.</p>
      <p>L’idée de la piste 1 reste précieuse : sa courbe est déjà celle des animations du site. Elle peut rester la signature du mouvement sans être le logo. La piste 2 est conservée pour mémoire.</p>
      <h3>Étapes suivantes, après votre validation</h3>
      <ol>
        <li>Choix de l’agencement de couleurs principal (proposé : os et braise sur encre, laque sur os).</li>
        <li>Finalisation du dessin : contours vectoriels, version réduite calée au pixel pour 16 et 32 px.</li>
        <li>Intégration : en-tête, menu, pied de page, favicon, icône Apple, image de partage, sans toucher au reste.</li>
        <li>Mise à jour du brand book et des fichiers de logo.</li>
      </ol>
    </div>
  </section>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>{X3D}</script>
'''
open('../logo-board.html', 'w').write(html)
print(len(html))
