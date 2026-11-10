"""Nom v3 : marques des trois propositions (contours de polices réelles + géométrie)."""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
HERE = os.path.dirname(os.path.abspath(__file__))
_F = {}
def font(n):
    if n not in _F:
        f = TTFont(os.path.join(HERE, 'fonts', n)); _F[n] = (f, f.getGlyphSet(), f.getBestCmap())
    return _F[n]
def glyph(n, ch, x=0, base=0, sx=1):
    f, gs, cm = font(n); g = gs[cm[ord(ch)]]; pen = SVGPathPen(gs)
    g.draw(TransformPen(pen, (sx, 0, 0, -1, x, base))); return pen.getCommands(), g.width
def bounds(n, ch):
    f, gs, cm = font(n); bp = BoundsPen(gs); gs[cm[ord(ch)]].draw(bp); return bp.bounds

# ---------- RHYTHMOS ----------
# Mot-symbole en mètre : large = syllabe longue, étroit = brève. ¯ ˘ ˘ | ¯ ˘ ˘ | ¯ ¯ (fin d'un hexamètre d'Homère)
METER = '-uu-uu--'
def rhythmos_word(fg='currentColor', meter=True, track=18):
    x = 0; parts = []; base = 729 + 40
    for ch, m in zip('RHYTHMOS', METER):
        fn = ('mona125.ttf' if m == '-' else 'mona75.ttf') if meter else 'mona100.ttf'
        p, w = glyph(fn, ch, x, base); parts.append(p); x += w + track
    W = x - track; H = 729 + 80
    return f'<path fill="{fg}" d="{"".join(parts)}"/>', W, H

def rhythmos_symbol(fg='currentColor', acc=None, gap=True, sw=14, cls=''):
    """Un R tracé d'un seul geste : le Ρ grec (rhô, initiale de ῥυθμός) et une jambe qui fait un pas."""
    acc = acc or fg
    rho = f'<path class="rho" pathLength="100" d="M28 92V16H50A20 20 0 0 1 50 56H28" fill="none" stroke="{fg}" stroke-width="{sw}" stroke-linejoin="miter"/>'
    leg = f'<path class="leg" d="M{57 if gap else 44} {71 if gap else 56}L78 92" fill="none" stroke="{acc}" stroke-width="{sw}"/>'
    return rho + leg

# ---------- ROSHEM ----------
def roshem_symbol(ink='currentColor', paper='#F3F3F0'):
    """Le sceau et son empreinte : à gauche le R gravé à l'envers, à droite le R imprimé. Pliez : ils coïncident."""
    (x0, y0, x1, y1) = bounds('young.ttf', 'R'); w = x1 - x0; h = y1 - y0
    s = 34 / h
    def R(cx, mirror, fill):
        sx = -s if mirror else s
        tx = cx + (w / 2 * s if mirror else -w / 2 * s) - x0 * sx
        p, _ = glyph('young.ttf', 'R')
        return f'<path fill="{fill}" transform="translate({tx:.2f} {67:.2f}) scale({sx:.4f} {s:.4f})" d="{p}"/>'
    return (f'<rect x="6" y="22" width="44" height="56" fill="{ink}"/>' + R(28, True, paper) +
            f'<rect x="50" y="22" width="44" height="56" fill="none" stroke="{ink}" stroke-width="2"/>' + R(72, False, ink))

def roshem_word(fg='currentColor', track=10):
    x = 0; parts = []; base = 750 + 40
    for ch in 'ROSHEM':
        p, w = glyph('young.ttf', ch, x, base); parts.append(p); x += w + track
    return f'<path fill="{fg}" d="{"".join(parts)}"/>', x - track, 750 + 80

# ---------- ÀMÌ ----------
def ami_word(fg='currentColor', acc=None):
    """àmì : les deux accents graves sont les « àmì ohùn », les signes qui décident du sens."""
    acc = acc or fg
    x = 0; base = 1060; parts = []; accs = []
    for ch in 'amı':
        p, w = glyph('notoami.ttf', ch, x, base); parts.append(p)
        if ch in 'aı':
            (x0, y0, x1, y1) = bounds('notoami.ttf', ch); cx = x + (x0 + x1) / 2 + (90 if ch == "a" else 20)
            top = base - y1 - 20
            accs.append(f'M{cx-150:.0f} {top-230:.0f}L{cx-20:.0f} {top-230:.0f}L{cx+110:.0f} {top:.0f}L{cx-20:.0f} {top:.0f}Z')
        x += w - 10
    return f'<path fill="{fg}" d="{"".join(parts)}"/><path class="acc" fill="{acc}" d="{"".join(accs)}"/>', x + 10, 1120

def ami_symbol(fg='currentColor', acc=None):
    acc = acc or fg
    return (f'<rect x="42" y="44" width="16" height="46" fill="{fg}"/>'
            f'<path class="acc" d="M28 10 L46 10 L62 34 L44 34 Z" fill="{acc}"/>')

def svg(inner, vb, cls='', label='', extra=''):
    return f'<svg class="{cls}" viewBox="{vb}" role="img" aria-label="{label}"{extra}>{inner}</svg>'
