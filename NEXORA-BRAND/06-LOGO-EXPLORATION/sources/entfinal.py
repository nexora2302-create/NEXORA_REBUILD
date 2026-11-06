import math, json
INK, BONE, EMBER, DEEP, CHAR, RUST = '#0d0c0b', '#ece5d8', '#ff4a1c', '#b02f0b', '#161412', '#7a2410'
G = json.load(open('glyphs.json'))['900']['g']; H = 688
def P(path): return ' '.join(f'{x:.1f},{y:.1f}' for x, y in path)
SIZE = 1200; C = SIZE / 2; ANG = 40
VB = f'{C-505} {C-495} 1010 990'

def blade(k=1.6, w=240, bend=55, taper=0.72, n=120, kind='flip', L=1000):
    hl = L / 2; top = []; mid = []; bot = []
    for i in range(n + 1):
        t = -1 + 2 * i / n
        x = t * hl; y = -bend * (1 - t * t)
        hw = w / 2 * max(0.0, 1 - t * t) ** taper
        if kind == 'flip':
            s = (math.tanh(t * k) / math.tanh(abs(k)) if abs(k) > 1e-3 else t) * hw * 0.92 * (1 if k >= 0 else -1) * (1 if k >= 0 else -1)
            s = math.tanh(t * k) / math.tanh(max(abs(k), 1e-3)) * hw * 0.92
        else:
            s = hw * 0.36 + hw * 0.18 * math.sin(math.pi * t)
        top.append((x, y - hw)); mid.append((x, y + s)); bot.append((x, y + hw))
    return P(top + bot[::-1]), P(top + mid[::-1]), P(mid + bot[::-1]), mid

_n = [0]
def symbol(a=(BONE, EMBER), b=(EMBER, RUST), bg=None, gap=30, mono=None, gapcol=None, kind='flip', cls='', label='Symbole NEXORA', **kw):
    sil, up, lo, mid = blade(kind=kind, **kw)
    out = f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="{VB}" role="img" aria-label="{label}">'
    if bg: out += f'<rect x="0" y="0" width="{SIZE}" height="{SIZE}" fill="{bg}"/>'
    def lame(rot, faces):
        if not mono and faces[0] == faces[1]:
            return f'<g transform="translate({C} {C}) rotate({rot})"><polygon points="{sil}" fill="{faces[0]}"/></g>'
        if mono:
            f = f'<polyline points="{P(mid)}" fill="none" stroke="{gapcol}" stroke-width="{gap*0.7:.0f}" stroke-linecap="round"/>' if gapcol else ''
            return f'<g transform="translate({C} {C}) rotate({rot})"><polygon points="{sil}" fill="{mono}"/>{f}</g>'
        return f'<g transform="translate({C} {C}) rotate({rot})"><polygon points="{up}" fill="{faces[0]}"/><polygon points="{lo}" fill="{faces[1]}"/></g>'
    out += lame(180 + ANG, b)
    gc = gapcol or bg
    if gc:
        out += f'<g transform="translate({C} {C}) rotate({-ANG})"><polygon points="{sil}" fill="{gc}" stroke="{gc}" stroke-width="{gap*2}" stroke-linejoin="round"/></g>'
    else:  # fond transparent : le passage est découpé par un masque
        pass
    out += lame(-ANG, a)
    return out + '</svg>'

def symbol_t(a=(BONE, EMBER), b=(EMBER, RUST), gap=30, cls='', **kw):
    """Fond transparent : la lame arrière est découpée par un masque autour de la lame avant."""
    _n[0] += 1; m = f'mx{_n[0]}'
    sil, up, lo, mid = blade(**kw)
    tr1 = f'translate({C} {C}) rotate({-ANG})'; tr2 = f'translate({C} {C}) rotate({180+ANG})'
    return (f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="{VB}" role="img" aria-label="Symbole NEXORA">'
            f'<defs><mask id="{m}" maskUnits="userSpaceOnUse" x="0" y="0" width="{SIZE}" height="{SIZE}"><rect width="{SIZE}" height="{SIZE}" fill="#fff"/>'
            f'<polygon transform="{tr1}" points="{sil}" fill="#000" stroke="#000" stroke-width="{gap*2}" stroke-linejoin="round"/></mask></defs>'
            f'<g mask="url(#{m})"><g transform="{tr2}"><polygon points="{up}" fill="{b[0]}"/><polygon points="{lo}" fill="{b[1]}"/></g></g>'
            f'<g transform="{tr1}"><polygon points="{up}" fill="{a[0]}"/><polygon points="{lo}" fill="{a[1]}"/></g></svg>')

def small(a=BONE, b=EMBER, bg=INK, cls=''):
    """Version réduite (≤ 32 px) : lames pleines, plus larges, passage élargi."""
    return symbol(a=(a, a), b=(b, b), bg=bg, gap=46, w=300, bend=40, cls=cls, label='Symbole NEXORA, version réduite')

def animated(a=(BONE, EMBER), b=(EMBER, RUST), bg=INK, cls='', dur=7.0):
    """Animation légère (SVG natif) : les rubans respirent (torsion), puis l'X fait un demi-tour, comme la sculpture du hero."""
    ks = [1.6, 2.5, 1.6, -1.6, -2.5, -1.6, 1.6]
    kt = '0;0.22;0.44;0.62;0.78;0.9;1'
    def frames(part):
        return ';'.join(blade(k=k)[part] for k in ks)
    sil = blade()[0]
    spl = ';'.join(['0.45 0 0.55 1'] * 6)
    def lame(rot, faces, front):
        g = (f'<g transform="translate({C} {C}) rotate({rot})">'
             f'<polygon fill="{faces[0]}"><animate attributeName="points" dur="{dur}s" repeatCount="indefinite" values="{frames(1)}" keyTimes="{kt}" calcMode="spline" keySplines="{spl}"/></polygon>'
             f'<polygon fill="{faces[1]}"><animate attributeName="points" dur="{dur}s" repeatCount="indefinite" values="{frames(2)}" keyTimes="{kt}" calcMode="spline" keySplines="{spl}"/></polygon></g>')
        return g
    gapg = f'<g transform="translate({C} {C}) rotate({-ANG})"><polygon points="{sil}" fill="{bg}" stroke="{bg}" stroke-width="60" stroke-linejoin="round"/></g>'
    spin = (f'<animateTransform attributeName="transform" type="rotate" dur="{dur}s" repeatCount="indefinite" '
            f'values="0 {C} {C};0 {C} {C};180 {C} {C};180 {C} {C}" keyTimes="0;0.5;0.68;1" calcMode="spline" keySplines="0 0 1 1;0.83 0 0.17 1;0 0 1 1"/>')
    return (f'<svg class="{cls} anim" xmlns="http://www.w3.org/2000/svg" viewBox="{VB}" role="img" aria-label="Symbole NEXORA animé">'
            f'<rect x="0" y="0" width="{SIZE}" height="{SIZE}" fill="{bg}"/><g>{spin}{lame(180+ANG, b, False)}{gapg}{lame(-ANG, a, True)}</g></svg>')

def display_word(fg, a, b, bg=None, cls=''):
    """NE[X]ORA : le symbole prend la place du X, comme dans le hero."""
    gap = 64; x = 0; parts = []
    sym_h = H * 2.0; sym_w = sym_h * 1010 / 990
    for ch in 'NEXORA':
        if ch == 'X':
            x += gap - 230
            inner = symbol_t(a=a, b=b).split('>', 1)[1].rsplit('</svg>', 1)[0]
            sc = sym_h / 990
            parts.append(f'<g transform="translate({x:.0f} {H/2 - sym_h/2:.0f}) scale({sc:.4f}) translate({-(C-505)} {-(C-495)})">{inner}</g>')
            x += sym_w - 250
            continue
        gl = G[ch]; l, r = gl['bounds'][0], gl['bounds'][2]
        if parts: x += gap + {'R': 6, 'A': -46}.get(ch, 0)
        parts.append(f'<path transform="translate({x - l:.0f} 0)" d="{gl["d"]}" fill="{fg}"/>')
        x += r - l
    top = H/2 - sym_h/2
    rr = f'<rect x="-80" y="{top-60:.0f}" width="{x+160:.0f}" height="{sym_h+120:.0f}" fill="{bg}"/>' if bg else ''
    return f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="-80 {top-60:.0f} {x+160:.0f} {sym_h+120:.0f}" role="img" aria-label="NEXORA">{rr}{"".join(parts)}</svg>'

def plain_word(fg, cls=''):
    gap = 64; x = 0; parts = []; prev = None
    ADJ = {('E', 'X'): -34, ('X', 'O'): -40, ('R', 'A'): -46, ('O', 'R'): 6}
    for ch in 'NEXORA':
        gl = G[ch]; l, r = gl['bounds'][0], gl['bounds'][2]
        if prev: x += gap + ADJ.get((prev, ch), 0)
        parts.append(f'<path transform="translate({x - l:.0f} 0)" d="{gl["d"]}" fill="{fg}"/>'); x += r - l; prev = ch
    return f'<svg class="{cls}" xmlns="http://www.w3.org/2000/svg" viewBox="0 -2 {x:.0f} 692" role="img" aria-label="NEXORA">{"".join(parts)}</svg>'

if __name__ == '__main__':
    import base64
    items = [symbol(bg=INK), small(), animated(), display_word(BONE, (BONE, EMBER), (EMBER, RUST), INK), symbol_t(), plain_word(INK)]
    html = '<html><meta charset="utf-8"><body style="margin:0;background:#888;padding:16px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px">'
    for s in items: html += f'<div style="height:260px;display:flex;align-items:center;justify-content:center;background:#ece5d8">{s.replace("<svg ", "<svg style=\'max-width:100%;max-height:100%\' ",1)}</div>'
    open('explore6.html', 'w').write(html + '</body></html>')
