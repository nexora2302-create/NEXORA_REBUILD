"""Strobe : génération des marques (contours Anybody 900, O remplacé par le disque décalé)."""
import math
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import os
HERE = os.path.dirname(os.path.abspath(__file__))
CAP = 1350

def _glyphs(w):
    f = TTFont(os.path.join(HERE, f'any{w}.ttf')); return f, f.getGlyphSet(), f.getBestCmap()

def glyph_path(gs, cm, ch, x, base):
    pen = SVGPathPen(gs)
    gs[cm[ord(ch)]].draw(TransformPen(pen, (1, 0, 0, -1, x, base)))
    return pen.getCommands(), gs[cm[ord(ch)]].width

def half(cx, cy, r, top):
    # demi-disque : arc supérieur (top) ou inférieur, fermé par le diamètre
    s = 0 if top else 1
    return f'M{cx-r:.1f} {cy:.1f}A{r:.1f} {r:.1f} 0 0 {1 if top else 0} {cx+r:.1f} {cy:.1f}Z'

def disc_split(cx, cy, r, d):
    """Le disque décalé : un disque coupé à l'horizontale, moitié haute à gauche, moitié basse à droite."""
    return half(cx - d, cy, r, True) + half(cx + d, cy, r, False)

def symbol(fg='currentColor', d=0.17):
    """Symbole seul, repère 100 x 100. r = 34, décalage = d * diamètre."""
    r = 34; off = d * 2 * r
    return f'<path fill="{fg}" d="{disc_split(50, 50, r, off)}"/>'

# Approche optique (unités de police) ajustée à l'œil entre paires
KERN = {('S','T'): -40, ('T','R'): -20, ('R','O'): 150, ('O','B'): 150, ('B','E'): -10}

def wordmark(w=100, fg='currentColor', o='split', d=0.12, track=24, bands=None):
    """Retourne (inner_svg, width, height) ; repère : ligne de base y = CAP + pad."""
    f, gs, cm = _glyphs(w)
    pad = 60; base = CAP + pad
    x = 0; parts = []; prev = None
    for ch in 'STROBE':
        if prev: x += KERN.get((prev, ch), 0) + track
        if ch == 'O':
            adv = gs[cm[ord('O')]].width
            r = CAP * 0.512; lsb = (adv - 2 * r) / 2
            cx = x + adv / 2; cy = base - CAP / 2
            if o == 'split': parts.append(disc_split(cx, cy, r, d * 2 * r))
            elif o == 'solid': parts.append(f'M{cx-r:.1f} {cy:.1f}a{r:.1f} {r:.1f} 0 1 0 {2*r:.1f} 0a{r:.1f} {r:.1f} 0 1 0 {-2*r:.1f} 0Z')
            elif o == 'slit':
                g = r * 0.16; a = math.asin(g / r); dx = r * math.cos(a)
                parts.append(f'M{cx-dx:.1f} {cy-g:.1f}A{r:.1f} {r:.1f} 0 1 1 {cx+dx:.1f} {cy-g:.1f}Z M{cx-dx:.1f} {cy+g:.1f}A{r:.1f} {r:.1f} 0 1 0 {cx+dx:.1f} {cy+g:.1f}Z')
            else: parts.append(glyph_path(gs, cm, 'O', x, base)[0])
            x += adv
        else:
            p, adv = glyph_path(gs, cm, ch, x, base); parts.append(p); x += adv
        prev = ch
    W = x; H = CAP + 2 * pad
    # marge du disque décalé qui dépasse
    path = ''.join(parts)
    if not bands:
        return f'<path fill="{fg}" d="{path}"/>', W, H
    # version tranchée (logo dynamique) : bandes horizontales décalées
    n = len(bands); h = H / n; out = []
    for i, dx in enumerate(bands):
        out.append(f'<clipPath id="b{i}{w}"><rect x="-400" y="{i*h:.1f}" width="{W+800:.0f}" height="{h+.5:.1f}"/></clipPath>'
                   f'<g clip-path="url(#b{i}{w})"><path fill="{fg}" transform="translate({dx} 0)" d="{path}"/></g>')
    return ''.join(out), W, H

def svg(inner, W, H, cls='', label='Strobe', pad=0):
    return (f'<svg class="{cls}" viewBox="{-pad:.0f} 0 {W+2*pad:.0f} {H:.0f}" role="img" aria-label="{label}">{inner}</svg>')

def slit(fg='currentColor'):
    r=34; g=5; import math; a=math.asin(g/r); dx=r*math.cos(a); cx=cy=50
    return f'<path fill="{fg}" d="M{cx-dx:.2f} {cy-g}A{r} {r} 0 1 1 {cx+dx:.2f} {cy-g}Z M{cx-dx:.2f} {cy+g}A{r} {r} 0 1 0 {cx+dx:.2f} {cy+g}Z"/>'

def ring(fg='currentColor', acc=None):
    import math; out=[]
    for i in range(12):
        a=math.radians(i*30); c=acc if (acc and i==0) else fg
        out.append(f'<rect x="47" y="12" width="6" height="16" rx="3" fill="{c}" transform="rotate({i*30} 50 50)"/>')
    return ''.join(out)

def ghost_s(fg='currentColor', acc='#22E1FF'):
    f, gs, cm = _glyphs(100)
    p1,_=glyph_path(gs,cm,'S',0,0)
    t=lambda dx:f'translate({20+dx} 83) scale(.0445)'
    return (f'<path d="{p1}" transform="{t(9)}" fill="none" stroke="{acc}" stroke-width="60"/>'
            f'<path d="{p1}" transform="{t(0)}" fill="{fg}"/>')
