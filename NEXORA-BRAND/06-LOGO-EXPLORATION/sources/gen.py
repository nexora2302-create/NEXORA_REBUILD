import json, math
G = json.load(open('glyphs.json'))
INK, BONE, EMBER, DEEP, CHAR, SAND = '#0d0c0b', '#ece5d8', '#ff4a1c', '#b02f0b', '#161412', '#e2dacb'
H = 688  # hauteur de capitale (unités de fonte, haut à y=0, ligne de base à y=688)

def f(v): return f'{v:.1f}'.rstrip('0').rstrip('.')

# ---------- A. COURBE : le N dessiné par une courbe d'accélération ----------
def courbe_parts(W=960, S=232, T=214, e=(0.83, 0.17), gap=0):
    """Deux fûts + une bande en S (courbe d'animation ease-in-out). gap>0 : les trois traits se séparent."""
    x0, x1 = S + gap - (4 if not gap else 0), W - S - gap + (4 if not gap else 0)  # léger chevauchement : pas de liseré
    y0, y1 = T / 2, H - T / 2
    dx = x1 - x0
    c = f'M{f(x0)} {f(y0)}C{f(x0 + e[0]*dx)} {f(y0)} {f(x0 + e[1]*dx)} {f(y1)} {f(x1)} {f(y1)}'
    stems = f'M0 0H{S}V{H}H0Z M{W-S} 0H{W}V{H}H{W-S}Z'
    return stems, c, T, W

def courbe_svg(fg=BONE, acc=EMBER, bg=None, pad=120, **k):
    stems, c, T, W = courbe_parts(**k)
    w, h = W + 2*pad, H + 2*pad
    r = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{r}<g transform="translate({pad} {pad})">'
            f'<path d="{stems}" fill="{fg}"/><path d="{c}" fill="none" stroke="{acc}" stroke-width="{T}"/></g></svg>')

# ---------- B. DÉCALAGE : un X dont une branche a glissé d'une image ----------
def x_shift(W=880, t=250, shift=150, mode='v'):
    """X en deux branches. mode v : la branche montante est décalée vers le haut ; h : coupée et décalée à droite."""
    a = f'M0 0H{t}L{W} {H}H{W-t}Z'           # branche descendante \
    if mode == 'v':
        b = f'M{W-t} {-shift}H{W}L{t} {H-shift}H0Z'  # branche montante / décalée vers le haut
    else:
        b = f'M{W-t+shift} 0H{W+shift}L{W/2+t/2+shift} {H/2}H{W/2-t/2+shift}Z M{W/2-t/2} {H/2}H{W/2+t/2}L{t} {H}H0Z'
    return a, b

def xshift_svg(fg=BONE, acc=EMBER, bg=None, pad=160, **k):
    a, b = x_shift(**k)
    W = k.get('W', 880) + (k.get('shift',150) if k.get('mode')=='h' else 0)
    w, h = W + 2*pad, H + 2*pad
    r = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}">{r}<g transform="translate({pad} {pad})">'
            f'<path d="{a}" fill="{fg}"/><path d="{b}" fill="{acc}"/></g></svg>')

# ---------- C. ENTRELACS : deux lames qui se croisent et tournent ----------
def blade(L=980, wmax=170, bend=0.18):
    """Croissant effilé centré à l'origine, horizontal, courbé vers le haut."""
    hl = L/2; sag_out = wmax*0.5 + bend*hl; sag_in = -wmax*0.5 + bend*hl
    def arc_r(s):  # rayon pour une flèche s sur une corde L
        return (hl*hl + s*s) / (2*abs(s)) if abs(s) > 1e-6 else 1e9
    ro, ri = arc_r(sag_out), arc_r(sag_in)
    so = 1 if sag_out > 0 else 0
    si = 1 if sag_in > 0 else 0
    return (f'M{-hl} 0A{f(ro)} {f(ro)} 0 0 {so} {hl} 0'
            f'A{f(ri)} {f(ri)} 0 0 {1-si} {-hl} 0Z')

_uid=[0]
def entrelacs_svg(fg=BONE, acc=EMBER, bg=None, gapcol=None, ang=38, L=980, wmax=170, bend=0.16, gap=34, pad=140):
    _uid[0]+=1; mid=f'm{_uid[0]}'
    size = L + 2*pad
    c = size/2
    b = blade(L, wmax, bend)
    g1 = f'translate({c} {c}) rotate({-ang})'
    g2 = f'translate({c} {c}) rotate({180-ang+2*ang})'
    r = f'<rect width="{size}" height="{size}" fill="{bg}"/>' if bg else ''
    # la lame 2 passe sous la lame 1 : on la masque autour de la lame 1 (espace = gap)
    m = (f'<mask id="{mid}" maskUnits="userSpaceOnUse"><rect width="{size}" height="{size}" fill="#fff"/>'
         f'<path d="{b}" transform="{g1}" fill="#000" stroke="#000" stroke-width="{gap*2}"/></mask>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}"><defs>{m}</defs>{r}'
            f'<g mask="url(#{mid})"><path d="{b}" transform="{g2}" fill="{acc}"/></g><path d="{b}" transform="{g1}" fill="{fg}"/></svg>')

if __name__ == '__main__':
    out = {}
    out['courbe-a'] = courbe_svg(bg=INK, e=(0.68, 0.32))
    out['courbe-b'] = courbe_svg(bg=INK, e=(0.68, 0.32), T=190, S=240)
    out['courbe-mono'] = courbe_svg(fg=INK, acc=INK, bg=BONE, e=(0.68, 0.32))
    out['courbe-os'] = courbe_svg(fg=INK, acc=DEEP, bg=BONE, e=(0.68, 0.32))
    out['x-v'] = xshift_svg(bg=INK, mode='v', shift=120)
    out['x-v2'] = xshift_svg(bg=INK, mode='v', shift=170, t=230)
    for i,(ang,bend,wm) in enumerate([(40,0.0,200),(40,0.06,210),(46,0.03,230)]):
        out[f'ent-{i}'] = entrelacs_svg(bg=INK, ang=ang, bend=bend, wmax=wm)
    out['ent-mono'] = entrelacs_svg(fg=INK, acc=INK, bg=BONE, ang=40, bend=0.06, wmax=210)
    html = '<html><body style="margin:0;background:#333;display:flex;flex-wrap:wrap;gap:16px;padding:16px;font:12px sans-serif;color:#fff">'
    for k, v in out.items():
        big=v.replace("<svg ", "<svg style='width:100%;height:100%' ")
        import base64; u='data:image/svg+xml;base64,'+base64.b64encode(v.encode()).decode()
        html += f'<div><div style="width:300px;height:300px;display:flex">{big}</div><div style="display:flex;gap:8px;align-items:end;margin-top:6px"><img style="width:32px;height:32px" src="{u}"><img style="width:16px;height:16px" src="{u}">{k}</div></div>'
    open('explore1.html', 'w').write(html + '</body></html>')

# ---------- Logotypes ----------
GL = G['900']['g']
# espacement optique entre lettres (unités de fonte, entre boîtes englobantes)
GAP = 64
ADJ = {('E', 'X'): -34, ('X', 'O'): -40, ('O', 'R'): 6, ('R', 'A'): -46, ('N', 'E'): 0}

def custom_N(fg, acc, e=(0.83, 0.17)):
    stems, c, T, W = courbe_parts(e=e)
    return f'<path d="{stems}" fill="{fg}"/><path d="{c}" fill="none" stroke="{acc}" stroke-width="{T}"/>', W

def custom_X_shift(fg, acc, shift=120):
    a, b = x_shift(shift=shift)
    return f'<path d="{a}" fill="{fg}"/><path d="{b}" fill="{acc}"/>', 880

def custom_X_ent(fg, acc, k=1.38):
    # lames calées sur la hauteur de capitale (débord de 8 % en haut et en bas)
    L = 980; size = L + 280; sc = H * 1.16 / (size * 0.78) * k
    inner = entrelacs_svg(fg=fg, acc=acc, ang=40, bend=0.06, wmax=210)
    inner = inner.split('>', 1)[1].rsplit('</svg>', 1)[0]
    w = size * sc
    return f'<g transform="translate({f(-size*sc*0.11)} {f(H/2 - size*sc/2)}) scale({f(sc)})">{inner}</g>', w * 0.78

def wordmark(fg, acc, variant='plain', bg=None, pad=140):
    items = []; x = 0; prev = None
    for ch in 'NEXORA':
        if variant == 'courbe' and ch == 'N':
            body, w = custom_N(fg, acc); l, r = 0, w
        elif variant == 'decalage' and ch == 'X':
            body, w = custom_X_shift(fg, acc); l, r = 0, w
        elif variant == 'entrelacs' and ch == 'X':
            body, w = custom_X_ent(fg, acc); l, r = 0, w
        else:
            gl = GL[ch]; l, r = gl['bounds'][0], gl['bounds'][2]
            body = f'<path d="{gl["d"]}" fill="{fg}"/>'
        if prev is not None:
            x += GAP + ADJ.get((prev, ch), 0)
            if variant == 'entrelacs' and ch in 'XO' and prev in 'EX':
                x += -10 if ch == 'X' else -150
        items.append(f'<g transform="translate({f(x - l)} 0)">{body}</g>')
        x += r - l; prev = ch
    W = x
    top = pad + (170 if variant == 'decalage' else 0)
    w, h = W + 2*pad, H + 2*pad + (170 if variant == 'decalage' else 0)
    rr = f'<rect width="{f(w)}" height="{h}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(w)} {h}">{rr}<g transform="translate({pad} {top})">' + ''.join(items) + '</g></svg>'), W
