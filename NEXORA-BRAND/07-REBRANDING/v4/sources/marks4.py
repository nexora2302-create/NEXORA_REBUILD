"""Keraia : l'iota et son trait (κεραία). Le point du i devient une petite corne, inclinée comme pour verser."""
import os, math
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
HERE = os.path.dirname(os.path.abspath(__file__))
_F = {}
def font(n):
    if n not in _F:
        f = TTFont(os.path.join(HERE, 'fonts', n)); _F[n] = (f, f.getGlyphSet(), f.getBestCmap(), f['head'].unitsPerEm, f['OS/2'].sxHeight)
    return _F[n]

def horn_path(cx, cy, s=1.0, rot=0.0, W=0.62, P0=(-0.70, -0.80), P1=(-0.55, 0.30), P2=(0.45, 0.28)):
    """Corne effilée : axe en arc (quadratique), largeur de 0 (pointe) à 1 (embouchure). Repère local, puis échelle s et rotation."""
    def q(t):
        x = (1-t)**2*P0[0] + 2*(1-t)*t*P1[0] + t*t*P2[0]; y = (1-t)**2*P0[1] + 2*(1-t)*t*P1[1] + t*t*P2[1]
        dx = 2*(1-t)*(P1[0]-P0[0]) + 2*t*(P2[0]-P1[0]); dy = 2*(1-t)*(P1[1]-P0[1]) + 2*t*(P2[1]-P1[1])
        n = math.hypot(dx, dy); return x, y, -dy/n, dx/n
    N = 40; L = []; R = []
    for i in range(N + 1):
        t = i / N; x, y, nx, ny = q(t); w = W * (t ** 0.7) / 2
        L.append((x + nx*w, y + ny*w)); R.append((x - nx*w, y - ny*w))
    pts = L + R[::-1]
    c, sn = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    tr = lambda p: (cx + s*(p[0]*c - p[1]*sn), cy + s*(p[0]*sn + p[1]*c))
    return 'M' + 'L'.join(f'{tr(p)[0]:.2f} {tr(p)[1]:.2f}' for p in pts) + 'Z'

def symbol(fg='currentColor', acc=None, cls='', drop=False):
    """Repère 100 x 100. Tige (iota) + corne (keraia)."""
    acc = acc or fg
    stem = f'<rect class="stem" x="42" y="46" width="16" height="46" fill="{fg}"/>'
    horn = f'<path class="horn" fill="{acc}" d="{horn_path(44, 22, 26)}"/>'
    d = f'<circle class="drop" cx="55" cy="39" r="2.6" fill="{acc}"/>' if drop else ''
    return stem + horn + d

def glyph(n, ch, x, base, scale):
    f, gs, cm, upm, xh = font(n); g = gs[cm[ord(ch)]]; pen = SVGPathPen(gs)
    g.draw(TransformPen(pen, (scale, 0, 0, -scale, x, base))); return pen.getCommands(), g.width * scale

def bounds(n, ch):
    f, gs, cm, upm, xh = font(n); bp = BoundsPen(gs); gs[cm[ord(ch)]].draw(bp); return bp.bounds

def wordmark(n='gloock.ttf', fg='currentColor', acc=None, track=0.02, kern=None):
    """keraia en minuscules ; le i est un ı (sans point) surmonté de la corne."""
    acc = acc or fg
    f, gs, cm, upm, xh = font(n); s = 100 / xh   # hauteur d'x = 100
    base = 190; x = 0; parts = []; hornd = ''
    kern = kern or {}
    for k, ch in enumerate('keraıa'):
        if k: x += kern.get('keraıa'[k-1:k+1], 0) + track * 100
        p, w = glyph(n, ch, x, base, s); parts.append(p)
        if ch == 'ı':
            (x0, y0, x1, y1) = bounds(n, 'ı'); cx = x + (x0 + x1) / 2 * s
            stemw = (x1 - x0) * s
            hornd = horn_path(cx - 2, base - 100 - 46, 50)
        x += w
    return f'<path fill="{fg}" d="{"".join(parts)}"/><path class="horn" fill="{acc}" d="{hornd}"/>', x, 230

def svg(inner, vb, cls='', label='', extra=''):
    return f'<svg class="{cls}" viewBox="{vb}" role="img" aria-label="{label}"{extra}>{inner}</svg>'
