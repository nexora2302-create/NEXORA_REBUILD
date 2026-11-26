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
# ---------- traitements de NEXT ----------
def next_entrelacs(fg=OS,b=BRAISE,bg=ENCRE): return f'NE{xsvg(x_entrelacs,a=fg,b=b,bg=bg)}T'
def next_fleche(fg=OS,b=BRAISE,bg=ENCRE): return f'NE{xsvg(x_fleche,a=fg,b=b,bg=bg)}T'
def next_glitch(fg=OS,b=BRAISE,bg=ENCRE,word='NEXT'):
    bands=[(0,50.5,-.035,fg),(53.5,100,.035,fg),(50.5,53.5,.11,b)]
    lay=''.join(f'<span aria-hidden="true" style="position:absolute;left:0;top:0;color:{c};clip-path:inset({t}% -30% {100-btm}% -30%);transform:translateX({dx}em)">{word}</span>' for t,btm,dx,c in bands)
    return f'<span style="position:relative;display:inline-block"><span style="visibility:hidden">{word}</span>{lay}</span>'
def next_echo(fg=OS,b=BRAISE,bg=ENCRE,word='NEXT'):
    return (f'<span style="position:relative;display:inline-block"><span aria-hidden="true" style="position:absolute;left:.13em;top:0;color:transparent;-webkit-text-stroke:.03em {b}">{word}</span>'
            f'<span style="position:relative;color:{fg}">{word}</span></span>')
def next_curseur(fg=OS,b=BRAISE,bg=ENCRE):
    return f'NEXT<span style="display:inline-block;width:.4em;height:.75em;background:{b};margin-left:.08em"></span>'
T={'entrelacs':next_entrelacs,'glitch':next_glitch,'echo':next_echo,'fleche':next_fleche,'curseur':next_curseur}
def lockup(k,s,fg=OS,b=BRAISE,bg=ENCRE):
    studio=''.join(f'<span>{c}</span>' for c in 'STUDIO')
    return (f'<div style="display:inline-flex;flex-direction:column;gap:{s*0.17:.0f}px;font-family:Unbounded">'
            f'<div style="display:flex;align-items:baseline;font-weight:700;font-size:{s}px;line-height:.78;letter-spacing:0;color:{fg};white-space:nowrap">{T[k](fg=fg,b=b,bg=bg)}</div>'
            f'<div style="display:flex;justify-content:space-between;font-weight:400;font-size:{s*0.43:.1f}px;line-height:1;color:{fg};padding-right:{s*0.01:.0f}px">{studio}</div></div>')
def line(k,s,fg=OS,b=BRAISE,bg=ENCRE):
    return (f'<div style="display:flex;align-items:baseline;gap:.34em;font-family:Unbounded;font-size:{s}px;line-height:1;color:{fg};white-space:nowrap">'
            f'<span style="display:flex;align-items:baseline;font-weight:700">{T[k](fg=fg,b=b,bg=bg)}</span><span style="font-weight:400;letter-spacing:.18em">STUDIO</span></div>')
def symbol(k,s,fg=OS,b=BRAISE,bg=ENCRE):
    if k=='entrelacs': return xsvg(x_entrelacs,h=f'{s}px',a=fg,b=b,bg=bg)
    if k=='fleche': return xsvg(x_fleche,h=f'{s}px',a=fg,b=b,bg=bg)
    sz=s/0.75
    inner={'glitch':next_glitch(fg,b,bg,'N'),'echo':next_echo(fg,b,bg,'N'),
           'curseur':f'N<span style="display:inline-block;width:.4em;height:.75em;background:{b};margin-left:.08em"></span>'}[k]
    return f'<div style="display:flex;align-items:baseline;font-family:Unbounded;font-weight:700;font-size:{sz:.0f}px;line-height:.75;color:{fg}">{inner}</div>'
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;700&family=Manrope:wght@400;500&family=JetBrains+Mono:wght@400&family=Tektur:wdth,wght@75..100,400..900&family=Krona+One&family=Syncopate:wght@700&family=Lexend+Zetta:wght@700&display=swap">'
CSS=f'''*{{box-sizing:border-box}}body{{margin:0;background:{ENCRE};color:{OS}}}
.pg{{width:1920px;height:1080px;overflow:hidden;padding:60px 88px;display:flex;flex-direction:column;gap:30px}}
.m{{font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:{PIERRE}}}
.hd{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid rgba(236,229,216,.14);padding-bottom:18px}}
.tile{{background:{CHARBON};display:flex;align-items:center;justify-content:center;position:relative}}
.cap{{position:absolute;left:18px;top:14px}}
.txt{{font-family:Manrope,sans-serif;font-size:19px;line-height:1.5;color:#CFC8BB}}.txt b{{color:{OS};font-weight:500}}'''
def page(name,title,num,body):
    open(os.path.join(HERE,name+'.html'),'w').write(f'<!doctype html><html lang="fr"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body><div class="pg"><div class="hd"><span class="m">Next Studio · logo</span><span class="m">{title}</span><span class="m">{num}</span></div>{body}</div></body></html>')
P=[('entrelacs','Entrelacs',"Ton X : deux rubans qui se croisent et se pincent au centre, l’orange passe devant. C’est le X en 3D du site, à plat.","En mouvement : le X fait un tour sur lui-même, les rubans se tordent, puis il se repose."),
   ('glitch','Glitch',"NEXT se décale par tranches, comme une image qui arrive d’ailleurs : demain qui force l’entrée. STUDIO reste net, posé.","En mouvement : NEXT glitche une fraction de seconde, puis se recale net. Toutes les vidéos peuvent s’ouvrir comme ça."),
   ('echo','L’image d’après',"Derrière NEXT, son double orange est déjà dessiné un cran plus loin : la prochaine image, celle qu’on prépare.","En mouvement : le mot glisse dans son double, le double repart en avant. Une boucle infinie."),
   ('fleche','Flèche',"Le X garde ses deux branches, mais celle qui monte vers la droite devient une flèche orange : NEXT pointe vers demain.","En mouvement : la flèche part, sort du cadre et revient. Elle sert aussi de bouton « suivant » sur le site."),
   ('curseur','Curseur',"Après NEXT, un curseur orange : la suite est en train de s’écrire. Un geste du web, un rythme de vidéo.","En mouvement : le curseur clignote, puis tape le mot qu’on veut : NEXT VIDÉO, NEXT SITE, NEXT MARQUE.")]
for i,(k,nom,c,mv) in enumerate(P):
    body=f'''
<div class="tile" style="height:470px;background:{ENCRE};box-shadow:inset 0 0 0 1px rgba(236,229,216,.1)"><span class="m cap">Logo</span>{lockup(k,200)}</div>
<div style="display:grid;grid-template-columns:300px 300px 1fr 1fr;gap:26px;align-items:end">
 <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Symbole</span><div class="tile" style="height:300px">{symbol(k,130,bg=CHARBON)}</div></div>
 <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Avatar</span><div style="height:300px;display:flex;align-items:center;justify-content:center"><div style="width:250px;height:250px;border-radius:50%;background:{BRAISE};display:flex;align-items:center;justify-content:center">{symbol(k,96,fg=ENCRE,b=OS,bg=BRAISE)}</div></div></div>
 <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Fin de vidéo</span><div class="tile" style="height:300px;background:#0A0908;flex-direction:column;gap:30px">{lockup(k,92)}<span class="m" style="font-size:10px;letter-spacing:.24em">Motion design · Sites web · Cotonou</span></div></div>
 <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Sur fond clair, en ligne</span><div class="tile" style="height:300px;background:{OS};flex-direction:column;gap:34px">{line(k,34,fg=ENCRE,b=BRAISE,bg=OS)}<div style="display:flex;gap:18px;font-family:Manrope;font-size:14px;color:{ENCRE}"><span>Réalisations</span><span>Méthode</span><span style="background:{BRAISE};padding:8px 14px;border-radius:999px;font-weight:500">Démarrer un projet</span></div></div></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:48px"><div class="txt">{c}</div><div class="txt"><b>Mouvement</b> · {mv.split(" : ",1)[1]}</div></div>'''
    page(f'0{i+1}-{k}',f'0{i+1} · {nom}',f'0{i+1} / 06',body)
# ---------- typographies ----------
rows=[("Unbounded 700","'Unbounded'",700,"normal","Celle du logo au T peint. Ronde, large, solide. Recommandée."),
      ("Tektur 800","'Tektur'",800,"normal","Coupes droites, futuriste sans tomber dans la science-fiction."),
      ("Krona One","'Krona One'",400,"normal","Très large, calme, très « marque de tech »."),
      ("Syncopate 700","'Syncopate'",700,"normal","Capitales étirées, effet générique de film."),
      ("Lexend Zetta 700","'Lexend Zetta'",700,"normal","Ultra large et lisible, plus sage.")]
rw=''.join(f'''<div style="display:grid;grid-template-columns:240px 1fr 420px;gap:30px;align-items:center;border-top:1px solid rgba(236,229,216,.12);padding:20px 0">
 <span class="m" style="color:{OS}">{n}</span>
 <div style="display:flex;align-items:baseline;gap:.3em;font-family:{fam};font-weight:{w};font-size:64px;line-height:1;white-space:nowrap">NEXT<span style="font-size:.32em;letter-spacing:.3em;font-weight:{w if fam!="'Unbounded'" else 400}">STUDIO</span></div>
 <span class="txt" style="font-size:16px">{d}</span></div>''' for n,fam,w,_,d in rows)
page('06-typographies','06 · Autres typographies','06 / 06',f'<div style="display:flex;flex-direction:column;margin-top:10px">{rw}</div><div class="txt" style="font-size:16px;margin-top:auto">Toutes gratuites (Google Fonts), utilisables sur le site, dans les vidéos et sur les documents.</div>')
print('ok')
