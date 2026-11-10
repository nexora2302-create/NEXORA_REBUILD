import math
def P(pts): return ' '.join(f'{x:.2f},{y:.2f}' for x, y in pts)

# VOLTA : une source et trois faisceaux (son, lumière, image). La silhouette forme un V.
def volta_symbol(fg, acc, src=None):
    """Trois faisceaux qui partent d'un même point : son, lumière, image. Ensemble, ils dessinent le V."""
    S = (50, 92); R = 88
    def wedge(a1, a2):
        a1, a2 = math.radians(a1), math.radians(a2)
        p = lambda a: (S[0] + R * math.sin(a), S[1] - R * math.cos(a))
        return [S, p(a1), p(a2)]
    return (f'<polygon points="{P(wedge(-31, -12.5))}" fill="{fg}"/><polygon points="{P(wedge(-7.2, 7.2))}" fill="{acc}"/>'
            f'<polygon points="{P(wedge(12.5, 31))}" fill="{fg}"/>')

# SILLAGE : une présence et son sillage, à l'angle exact de Kelvin (19,47°) que forme toute trace sur l'eau.
def sillage_symbol(fg, acc):
    cx, cy, r = 74, 50, 12
    k = math.tan(math.radians(19.47))
    def wake(sign):
        x0, x1 = 60, 6
        y0, y1 = cy + sign * 1.5, cy + sign * (1.5 + (x0 - x1) * k)
        t0, t1 = 5.0, 1.2
        dx, dy = x1 - x0, y1 - y0; L = math.hypot(dx, dy); nx, ny = -dy / L, dx / L
        return [(x0 + nx * t0 / 2, y0 + ny * t0 / 2), (x1 + nx * t1 / 2, y1 + ny * t1 / 2), (x1 - nx * t1 / 2, y1 - ny * t1 / 2), (x0 - nx * t0 / 2, y0 - ny * t0 / 2)]
    return (f'<polygon points="{P(wake(-1))}" fill="{fg}"/><polygon points="{P(wake(1))}" fill="{fg}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{acc}"/>')

# AVANT : un A penché vers l'avant dont la barre dépasse : toujours un temps d'avance.
def avant_symbol(fg, acc):
    return (f'<g transform="translate(16 0) skewX(-12)"><path d="M20 92 L50 20 L80 92" fill="none" stroke="{fg}" stroke-width="15" stroke-linejoin="miter" stroke-miterlimit="10"/></g>'
            f'<rect x="31" y="60" width="66" height="11" fill="{acc}"/>')

def svg(inner, vb='0 0 100 100', cls='', bg=None, label='Symbole'):
    b = f'<rect x="-20" y="-20" width="140" height="140" fill="{bg}"/>' if bg else ''
    return f'<svg class="{cls}" viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">{b}{inner}</svg>'
