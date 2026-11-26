import os, math
HERE=os.path.dirname(os.path.abspath(__file__))
ENCRE,OS,BRAISE,CHARBON,PIERRE='#0D0C0B','#ECE5D8','#FF4A1C','#161412','#9A9386'
def f(v): return f'{v:.2f}'.rstrip('0').rstrip('.')
# ---------- le X, aux proportions de l'Unbounded 700 (hauteur 0,75 em = 100 unités ; chasse 121 unités) ----------
def bar(xt,xb,hmax,hmin,n=40):
    L,R=[],[]
    for i in range(n+1):
        t=i/n; y=100*t; x=xt+(xb-xt)*t; h=hmin+(hmax-hmin)*(2*t-1)**2
        L.append((x-h,y)); R.append((x+h,y))
    return 'M'+' L'.join(f'{f(a)} {f(b)}' for a,b in L+R[::-1])+' Z'
def x_entrelacs(a=OS,b=BRAISE,bg=ENCRE):
    return (f'<path d="{bar(18,103,18,6.5)}" fill="{a}"/>'
            f'<path d="{bar(103,18,18,6.5)}" fill="{b}" stroke="{bg}" stroke-width="6" paint-order="stroke"/>')
def x_fleche(a=OS,b=BRAISE,bg=ENCRE):
    # barre 1 pleine ; barre 2 : moitié basse os, moitié haute braise terminée en flèche qui dépasse vers le haut à droite
    h=15.5
    p1=bar(18,103,h,h,2)
    lo=f'M{f(60.5-h)} 50 L{f(18-h)} 100 L{f(18+h)} 100 L{f(60.5+h)} 50 Z'
    dx,dy=103-18,-100; L=math.hypot(dx,dy); ux,uy=dx/L,dy/L; nx,ny=-uy,ux
    # tige haute de y=50 à y=8, puis pointe
    def pt(t): return (60.5+ (103-60.5)*t, 50-50*t)
    sx,sy=pt(0.74); tipx,tipy=sx+ux*46, sy+uy*46
    w=h*1.0; W=h*2.9
    up=(f'M{f(60.5-h)} 50 L{f(sx-h)} {f(sy)} L{f(sx-W*0.98)} {f(sy+1)} L{f(tipx)} {f(tipy)} L{f(sx+W*0.98)} {f(sy-1)}'
        f' L{f(sx+h)} {f(sy)} L{f(60.5+h)} 50 Z')
    return (f'<path d="{p1}" fill="{a}"/><path d="{lo}" fill="{a}"/>'
            f'<path d="{up}" fill="{b}" stroke="{bg}" stroke-width="5" paint-order="stroke"/>')
def xsvg(fn, h='.75em', **kw):
    return f'<svg viewBox="0 0 121 100" style="height:{h};width:auto;flex:none;overflow:visible;margin:0 .005em" aria-hidden="true">{fn(**kw)}</svg>'
