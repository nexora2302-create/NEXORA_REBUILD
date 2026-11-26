import os
from lib4 import x_entrelacs, xsvg, ENCRE, OS, BRAISE, CHARBON, PIERRE
HERE=os.path.dirname(os.path.abspath(__file__))
def Esvg(fg):
    # E redessiné : fût et trois bras pleins, sans l'encoche de l'Unbounded (unités = 1/100 em)
    return (f'<svg viewBox="0 0 71 75" style="height:.75em;width:.71em;flex:none;margin:0 .045em 0 .04em;overflow:visible" aria-hidden="true">'
            f'<path fill="{fg}" d="M0 0 H71 V18 H22 V28.5 H65 V46.5 H22 V57 H71 V75 H0 Z"/></svg>')
def NEXT(fg=OS,b=BRAISE,bg=ENCRE,xa=None):
    return f'N{Esvg(fg)}{xsvg(x_entrelacs,a=xa or fg,b=b,bg=bg)}T'
def row(s,fg=OS,b=BRAISE,bg=ENCRE,inner=None):
    return f'<div style="display:flex;align-items:baseline;font-family:Unbounded;font-weight:700;font-size:{s}px;line-height:.75;color:{fg};white-space:nowrap">{inner or NEXT(fg,b,bg)}</div>'
# 1 · Signature : « Studio » écrit à la main, posé à plat sur le bas du mot
def L_signature(s,fg=OS,b=BRAISE,bg=ENCRE):
    return (f'<div style="display:inline-flex;flex-direction:column;align-items:flex-end">{row(s,fg,b,bg)}'
            f'<div style="font-family:\'Mr Dafoe\';font-size:{s*0.92:.0f}px;line-height:.8;color:{b};margin-top:{-s*0.17:.0f}px;margin-right:{-s*0.16:.0f}px">Studio</div></div>')
# 2 · Exposant : NEXT porte tout, « studio » se pose en haut à droite, comme une précision
def L_exposant(s,fg=OS,b=BRAISE,bg=ENCRE):
    return (f'<div style="display:inline-flex;align-items:flex-start;gap:{s*0.07:.0f}px">{row(s,fg,b,bg)}'
            f'<div style="font-family:Unbounded;font-weight:500;font-size:{s*0.19:.0f}px;line-height:1;letter-spacing:.02em;color:{fg};margin-top:{-s*0.005:.0f}px">studio<span style="color:{b}">.</span></div></div>')
# 3 · Bloc : NE sur XT, un carré ; STUDIO dessous, à la largeur du carré
def block(s,fg=OS,b=BRAISE,bg=ENCRE):
    return (f'<div style="display:inline-flex;flex-direction:column;gap:{s*0.13:.0f}px;font-family:Unbounded;font-weight:700;font-size:{s}px;line-height:.75;color:{fg}">'
            f'<div style="display:flex;align-items:baseline;justify-content:space-between">N{Esvg(fg)}</div>'
            f'<div style="display:flex;align-items:baseline;justify-content:space-between">{xsvg(x_entrelacs,a=fg,b=b,bg=bg)}<span style="margin-left:{s*0.03:.0f}px">T</span></div></div>')
def L_bloc(s,fg=OS,b=BRAISE,bg=ENCRE):
    st=''.join(f'<span>{c}</span>' for c in 'STUDIO')
    return (f'<div style="display:inline-flex;flex-direction:column;gap:{s*0.2:.0f}px">{block(s,fg,b,bg)}'
            f'<div style="display:flex;justify-content:space-between;font-family:Unbounded;font-weight:500;font-size:{s*0.24:.0f}px;line-height:1;color:{fg}">{st}</div></div>')
# 4 · Étiquette : STUDIO dans une étiquette orange collée au T
def L_etiquette(s,fg=OS,b=BRAISE,bg=ENCRE):
    return (f'<div style="display:inline-flex;align-items:flex-end;gap:{s*0.08:.0f}px">{row(s,fg,b,bg)}'
            f'<div style="font-family:Unbounded;font-weight:600;font-size:{s*0.17:.0f}px;line-height:1;letter-spacing:.06em;color:{bg if bg!=b else ENCRE};background:{b};padding:{s*0.06:.0f}px {s*0.09:.0f}px;border-radius:{s*0.06:.0f}px;margin-bottom:{-s*0.0:.0f}px">STUDIO</div></div>')
L=[('signature','Signature',L_signature,"« Studio » écrit à la main, à plat, posé sur le bas du mot. Le même geste que NEXORA Studio : les deux noms restent de la même famille."),
   ('exposant','Exposant',L_exposant,"NEXT porte tout. « studio. » se pose en petit, en haut à droite, comme une précision. Le plus sobre, le plus « grande agence »."),
   ('bloc','Bloc',L_bloc,"NE sur XT : le mot plié en carré, le X au centre. STUDIO dessous à la même largeur. Le carré sert seul d’avatar et d’icône."),
   ('etiquette','Étiquette',L_etiquette,"STUDIO dans une étiquette orange collée au T, comme une pastille sur une vidéo ou un bouton sur un site.")]
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;500;600;700&family=Mr+Dafoe&family=Manrope:wght@400;500&family=JetBrains+Mono:wght@400&display=swap">'
CSS=f'''*{{box-sizing:border-box}}body{{margin:0;background:{ENCRE};color:{OS}}}
.pg{{width:1920px;height:1080px;overflow:hidden;padding:60px 88px;display:flex;flex-direction:column;gap:28px}}
.m{{font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:{PIERRE}}}
.hd{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid rgba(236,229,216,.14);padding-bottom:18px}}
.tile{{background:{CHARBON};display:flex;align-items:center;justify-content:center;position:relative}}
.cap{{position:absolute;left:18px;top:14px}}
.txt{{font-family:Manrope,sans-serif;font-size:18px;line-height:1.5;color:#CFC8BB}}.txt b{{color:{OS};font-weight:500}}'''
def page(name,title,num,body):
    open(os.path.join(HERE,name+'.html'),'w').write(f'<!doctype html><html lang="fr"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body><div class="pg"><div class="hd"><span class="m">Next Studio · logo</span><span class="m">{title}</span><span class="m">{num}</span></div>{body}</div></body></html>')
# 00 : les quatre façons de poser STUDIO, et le symbole commun
cells=''.join(f'''<div style="display:flex;flex-direction:column;gap:14px"><div class="tile" style="height:330px"><span class="m cap">0{i+1} · {n}</span>{fn(118 if k!="bloc" else 112, bg=CHARBON)}</div><div class="txt" style="font-size:16px">{d}</div></div>''' for i,(k,n,fn,d) in enumerate(L))
page('00-studio','Où poser « studio »','00 / 03',f'''<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px 40px">{cells}</div>''')
# 01 : le symbole commun, NE sur XT
def av(bgc,fg,b,bgx,s=78,r='50%'):
    return f'<div style="width:240px;height:240px;border-radius:{r};background:{bgc};display:flex;align-items:center;justify-content:center">{block(s,fg,b,bgx)}</div>'
page('01-symbole','Le symbole : NE sur XT','01 / 03',f'''
<div style="display:grid;grid-template-columns:620px 1fr;gap:48px;flex:1">
 <div class="tile" style="background:{ENCRE};box-shadow:inset 0 0 0 1px rgba(236,229,216,.1)"><span class="m cap">Symbole</span>{block(190)}</div>
 <div style="display:flex;flex-direction:column;gap:30px">
  <div class="txt" style="font-size:20px">Le symbole n’est pas une lettre isolée : c’est <b>le mot plié en carré</b>. NE sur XT, le X entrelacé au centre. Il se lit, il tient dans un rond comme dans un carré, et il reste NEXT même tout petit.</div>
  <div style="display:flex;gap:28px;align-items:flex-end">
   <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Avatar</span>{av(BRAISE,ENCRE,OS,BRAISE)}</div>
   <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Avatar sombre</span>{av(ENCRE,OS,BRAISE,ENCRE).replace("background:#0D0C0B","background:#0D0C0B;box-shadow:inset 0 0 0 1px rgba(236,229,216,.16)")}</div>
   <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Icône</span>{av(OS,ENCRE,BRAISE,OS,r="54px")}</div>
   <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Favicon 64 · 32</span><div style="display:flex;gap:20px;align-items:flex-end">
    <div style="width:64px;height:64px;border-radius:14px;background:{BRAISE};display:flex;align-items:center;justify-content:center">{block(21,ENCRE,OS,BRAISE)}</div>
    <div style="width:32px;height:32px;border-radius:7px;background:{BRAISE};display:flex;align-items:center;justify-content:center">{block(10.5,ENCRE,OS,BRAISE)}</div></div></div>
  </div>
 </div>
</div>''')
# 02 : la recommandée en situation (signature)
page('02-situation','Signature, en situation','02 / 03',f'''
<div class="tile" style="height:440px;background:{ENCRE};box-shadow:inset 0 0 0 1px rgba(236,229,216,.1)"><span class="m cap">Logo</span>{L_signature(190)}</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:26px">
 <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Fin de vidéo</span><div class="tile" style="height:330px;background:#0A0908;flex-direction:column;gap:34px">{L_signature(86)}<span class="m" style="font-size:10px;letter-spacing:.24em">Motion design · Sites web · Cotonou</span></div></div>
 <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Sur fond clair</span><div class="tile" style="height:330px;background:{OS}">{L_signature(86,fg=ENCRE,b=BRAISE,bg=OS)}</div></div>
 <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Sur braise</span><div class="tile" style="height:330px;background:{BRAISE}">{L_signature(86,fg=ENCRE,b=OS,bg=BRAISE)}</div></div>
</div>''')
print('ok')
