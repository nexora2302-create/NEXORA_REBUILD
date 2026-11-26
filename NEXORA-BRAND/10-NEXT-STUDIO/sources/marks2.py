"""Symboles NEXTUDIO, repère 100 x 100."""
ENCRE,OS,BRAISE='#0D0C0B','#ECE5D8','#FF4A1C'
_n=[0]
def _u(s):
    _n[0]+=1; k=_n[0]
    for i in ('cb','cl'): s=s.replace(f'id="{i}"',f'id="{i}{k}"').replace(f'url(#{i})',f'url(#{i}{k})')
    return s
# 1 · Chevrons (avec X) : > et <, pointe contre pointe
def chevrons(a=OS,b=BRAISE,bg=ENCRE):
    return _u(f'<defs><clipPath id="cb"><rect x="-30" y="0" width="160" height="100"/></clipPath></defs><g clip-path="url(#cb)">'
      f'<polyline points="-4,-14 36,50 -4,114" fill="none" stroke="{a}" stroke-width="18" stroke-miterlimit="10"/>'
      f'<polyline points="104,-14 64,50 104,114" fill="none" stroke="{b}" stroke-width="18" stroke-miterlimit="10"/></g>')
# 2 · Image clé : le losange des images clés, coupé ; la moitié droite (lecture) avance
def cle(a=OS,b=BRAISE,bg=ENCRE):
    return (f'<polygon points="43,2 -5,50 43,98" fill="{a}"/>'
            f'<polygon points="57,2 105,50 57,98" fill="{b}"/>')
# 3 · Tête de lecture : la ligne de temps et la tête de lecture qui la traverse
def tete(a=OS,b=BRAISE,bg=ENCRE):
    # ligne de temps : jouée (pleine) à gauche, à venir (contour) à droite ; la tête de lecture posée sur l'instant présent
    return (f'<rect x="0" y="66" width="58" height="20" fill="{a}"/>'
            f'<rect x="59.5" y="67.5" width="39" height="17" fill="none" stroke="{a}" stroke-width="3"/>'
            f'<path d="M45 10 H71 V30 L58 43 L45 30 Z" fill="{b}"/>'
            f'<rect x="55" y="40" width="6" height="50" fill="{b}"/>')
import math
def amorce(a=OS,b=BRAISE,bg=ENCRE):
    # amorce de lancement dans son cadre d'image : l'arc tourne (le décompte), le réticule vise l'image qui arrive
    r=31; ang=275; a0=-90; a1=a0+ang
    x0,y0=50+r*math.cos(math.radians(a0)),50+r*math.sin(math.radians(a0))
    x1,y1=50+r*math.cos(math.radians(a1)),50+r*math.sin(math.radians(a1))
    return (f'<rect x="3" y="3" width="94" height="94" rx="16" fill="none" stroke="{a}" stroke-width="6"/>'
            f'<circle cx="50" cy="50" r="{r}" fill="none" stroke="{a}" stroke-opacity=".28" stroke-width="10"/>'
            f'<path d="M{x0:.2f} {y0:.2f} A{r} {r} 0 1 1 {x1:.2f} {y1:.2f}" fill="none" stroke="{b}" stroke-width="10"/>'
            f'<rect x="48.75" y="30" width="2.5" height="40" fill="{a}"/><rect x="30" y="48.75" width="40" height="2.5" fill="{a}"/>')
MARKS={'chevrons':chevrons,'cle':cle,'tete':tete,'amorce':amorce}
def svg(name,style='',**kw):
    return f'<svg class="mk" style="{style}" viewBox="0 0 100 100" aria-hidden="true" overflow="visible">{MARKS[name](**kw)}</svg>'
