"""Strobe v2 : le disque à fente. Un disque, une fente de visée (skopein), deux moitiés décalées (strobos)."""
import os, math
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
HERE = os.path.dirname(os.path.abspath(__file__))
F = TTFont(os.path.join(HERE, 'fonts', 'a112w8.ttf')); GS = F.getGlyphSet(); CM = F.getBestCmap(); CAP = 1350

# Géométrie du symbole, repère 100 x 100
R, G, D = 36.5, 6.6, 5.6       # rayon (surcompensé de 0,5 pour la fente), hauteur de fente, décalage de chaque moitié
def halves(cx=50, cy=50, r=R, g=G, ring=0):
    """Renvoie (haut, bas) : segments de disque au-dessus et au-dessous de la fente. ring>0 : anneau (épaisseur ring)."""
    h = g / 2; out = []
    for top in (True, False):
        y = cy - h if top else cy + h
        dx = math.sqrt(r * r - h * h)
        sweep = 1 if top else 0
        p = f'M{cx-dx:.3f} {y:.3f}A{r} {r} 0 1 {sweep} {cx+dx:.3f} {y:.3f}'
        if ring:
            ri = r - ring; dxi = math.sqrt(ri * ri - h * h)
            p += f'L{cx+dxi:.3f} {y:.3f}A{ri} {ri} 0 1 {1-sweep} {cx-dxi:.3f} {y:.3f}'
        out.append(p + 'Z')
    return out

def symbol(fg='currentColor', d=D, cls='', g=G, r=R):
    t, b = halves(g=g, r=r)
    return (f'<path class="h-top" fill="{fg}" transform="translate({-d} 0)" d="{t}"/>'
            f'<path class="h-bot" fill="{fg}" transform="translate({d} 0)" d="{b}"/>')

def favicon(fg='currentColor'):
    """Version 12 à 16 px : fente et décalage agrandis pour survivre à la réduction."""
    return symbol(fg, d=8, g=12, r=40)

# Logotype : Anybody 800, largeur 112,5 ; le O est l'anneau à fente, approches retouchées à la main
KERN = {'ST': -30, 'TR': -40, 'RO': 40, 'OB': 40, 'BE': -10}
def wordmark(fg='currentColor', acc=None, track=20):
    acc = acc or fg
    base = CAP + 60; x = 0; parts = []; ring = ''
    prev = ''
    for ch in 'STROBE':
        if prev: x += KERN.get(prev + ch, 0) + track
        if ch == 'O':
            r = CAP * 0.515; stroke = 300; adv = 2 * r + 120
            cx = x + adv / 2; cy = base - CAP / 2
            sc = r / R
            t, b = halves(cx, cy, r, G * sc, ring=stroke)
            dd = D * sc * 0.8
            ring = (f'<path class="o-top" fill="{acc}" transform="translate({-dd:.1f} 0)" d="{t}"/>'
                    f'<path class="o-bot" fill="{acc}" transform="translate({dd:.1f} 0)" d="{b}"/>')
            x += adv
        else:
            pen = SVGPathPen(GS); g = GS[CM[ord(ch)]]
            g.draw(TransformPen(pen, (1, 0, 0, -1, x, base))); parts.append(f'<path class="l-{ch}" fill="{fg}" d="{pen.getCommands()}"/>')
            x += g.width
        prev = ch
    return ''.join(parts) + ring, x, CAP + 120

def svg(inner, vb, cls='', label='', extra=''):
    return f'<svg class="{cls}" viewBox="{vb}" role="img" aria-label="{label}"{extra}>{inner}</svg>'

def wm(fg='currentColor', acc=None, cls='wm', label='Strobe'):
    i, w, h = wordmark(fg, acc); return svg(i, f'-60 0 {w+120:.0f} {h}', cls, label)
def sym(fg='currentColor', cls='sy', label='Symbole Strobe', **k):
    return svg(symbol(fg, **k), '0 0 100 100', cls, label)
