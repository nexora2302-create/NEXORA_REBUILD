import os
from marks2 import svg, OS, BRAISE, ENCRE
HERE=os.path.dirname(os.path.abspath(__file__))
CHARBON,PIERRE='#161412','#9A9386'
FONTS=('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700&family=Sora:wght@400;700&'
       'family=Syne:wght@500;800&family=Michroma&family=Manrope:wght@400;500&family=JetBrains+Mono:wght@400;500&display=swap">')
CSS=f'''*{{box-sizing:border-box}}body{{margin:0;background:{ENCRE};color:{OS}}}
.pg{{width:1920px;height:1080px;overflow:hidden;padding:64px 88px;display:flex;flex-direction:column;gap:36px;position:relative}}
.m{{font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:{PIERRE}}}
.hd{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid rgba(236,229,216,.14);padding-bottom:18px}}
.w{{display:flex;align-items:baseline;white-space:nowrap;line-height:1}}
.mk{{flex:none;overflow:visible}}
.tile{{background:{CHARBON};display:flex;align-items:center;justify-content:center;position:relative}}
.cap{{position:absolute;left:20px;top:16px}}
.txt{{font-family:Manrope,sans-serif;font-size:19px;line-height:1.5;color:#CFC8BB}}
.txt b{{color:{OS};font-weight:500}}
'''
# ---------- logos ----------
def lk_balises(s, fg=OS, b=BRAISE):
    return (f'<div class="w" style="font-family:\'Space Grotesk\';font-weight:700;font-size:{s}px;letter-spacing:-.02em;color:{fg}">NE'
            f'{svg("chevrons",style="height:.7em;width:.66em;margin:0 .05em 0 .03em",a=fg,b=b)}TUDIO</div>')
def lk_cle(s, fg=OS, b=BRAISE):
    return (f'<div class="w" style="align-items:center;gap:.34em;font-size:{s}px">{svg("cle",style="height:.86em;width:.86em",a=fg,b=b)}'
            f'<span style="font-family:Sora;font-weight:700;letter-spacing:-.03em;color:{fg}">NEXTUDIO</span></div>')
def lk_tete(s, fg=OS, b=BRAISE):
    bar=lambda k: {'solid':f'background:{fg}','now':f'background:{b}','next':f'box-shadow:inset 0 0 0 .025em {fg}'}[k]
    col=lambda t,k,mark=False: (f'<span style="display:inline-flex;flex-direction:column;align-items:stretch">'
        f'<span>{t}</span><span style="height:.2em;display:flex;justify-content:center;align-items:flex-end">'
        + (f'<svg viewBox="0 0 26 20" style="height:.17em;width:.22em;overflow:visible"><path d="M0 0 H26 V11 L13 20 L0 11 Z" fill="{b}"/></svg>' if mark else '')
        + f'</span><span style="height:.11em;margin-top:.04em;{bar(k)}"></span></span>')
    return (f'<div class="w" style="font-family:Syne;font-weight:800;font-size:{s}px;letter-spacing:-.02em;color:{fg};align-items:flex-start">'
            f'{col("nex","solid")}{col("t","now",True)}{col("udio","next")}</div>')
def lk_amorce(s, fg=OS, b=BRAISE):
    return (f'<div class="w" style="align-items:center;gap:.42em;font-size:{s}px">{svg("amorce",style="height:1em;width:1em",a=fg,b=b)}'
            f'<span style="font-family:Michroma;letter-spacing:.14em;color:{fg};font-size:.62em">NEXTUDIO</span></div>')
P=[('balises','Balises','chevrons',lk_balises,"Space Grotesk 700","Space Grotesk 400",
    "Le X de NEXT est fait de deux pointes. <b>&gt; et &lt;</b> : les balises du code, donc le web. <b>&gt;</b> : la touche lecture et suivant, donc la vidéo. Nos deux métiers tiennent dans la lettre au cœur du nom.",
    "Le &gt; devient la flèche de toute la marque : boutons, listes, transitions d’une page à l’autre.", "La seule piste qui garde le X."),
   ('cle','Image clé','cle',lk_cle,"Sora 700","Sora 400",
    "En animation, tout part d’une <b>image clé</b> : le losange posé sur la ligne de temps. Le nôtre se coupe en deux et sa moitié droite, <b>le bouton lecture</b>, avance d’un cran. L’image d’après, c’est nous.",
    "Le losange devient puce, repère, motif ; il s’ouvre au centre pour passer d’un écran à l’autre.", "Le symbole des gens du métier."),
   ('tete','Tête de lecture','tete',lk_tete,"Syne 800","Syne 500",
    "La <b>tête de lecture</b> des logiciels de montage. À gauche, ce qui est joué ; à droite, ce qui vient. Elle se pose sur le <b>t</b>, là où « next » rejoint « studio ».",
    "La ligne de temps souligne tout : titres, menu, chargements. La tête avance quand on fait défiler la page.", "Le logo qui raconte le nom."),
   ('amorce','Lancement','amorce',lk_amorce,"Michroma","Manrope 400",
    "L’<b>amorce</b>, c’est le compte à rebours avant qu’une vidéo commence. L’anneau se remplit, le cadre est prêt, tout va partir. Au centre, <b>un +</b> : ce qu’on ajoute à une marque.",
    "L’anneau sert de chargement, de compteur, de transition ; le + marque les appels à l’action.", "Le plus futuriste, le plus « produit »."),
]
def page(name, title, num, body):
    html=(f'<!doctype html><html lang="fr"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body><div class="pg">'
          f'<div class="hd"><span class="m">Next Studio · logo</span><span class="m">{title}</span><span class="m">{num}</span></div>{body}</div></body></html>')
    open(os.path.join(HERE,name+'.html'),'w').write(html)
# ---------- 00 vue d’ensemble ----------
cols=''
for i,(k,nom,mk,lk,t1,t2,c,sy,tag) in enumerate(P):
    cols+=(f'<div style="display:flex;flex-direction:column;gap:26px">'
           f'<div class="tile" style="height:400px"><span class="m cap">0{i+1}</span>{svg(mk,style="width:190px;height:190px")}</div>'
           f'<div class="tile" style="height:150px;background:transparent;border:1px solid rgba(236,229,216,.12)">{lk(44 if k!="amorce" else 52)}</div>'
           f'<div style="display:flex;flex-direction:column;gap:8px"><span style="font-family:Sora;font-weight:700;font-size:26px;letter-spacing:-.02em">{nom}</span>'
           f'<span class="txt" style="font-size:17px">{tag}</span></div></div>')
page('00-vue-ensemble','Quatre propositions','00 / 04',f'<div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:32px;margin-top:20px">{cols}</div>'
     f'<div class="m" style="margin-top:auto">Couleurs gardées : encre #0D0C0B · os #ECE5D8 · braise #FF4A1C</div>')
# ---------- une planche par proposition ----------
for i,(k,nom,mk,lk,t1,t2,c,sy,tag) in enumerate(P):
    fam={'balises':"'Space Grotesk'",'cle':'Sora','tete':'Syne','amorce':'Michroma'}[k]
    fw={'balises':700,'cle':700,'tete':800,'amorce':400}[k]
    bodyfam={'balises':"'Space Grotesk'",'cle':'Sora','tete':'Syne','amorce':'Manrope'}[k]
    bodyw={'balises':400,'cle':400,'tete':500,'amorce':400}[k]
    big={'balises':150,'cle':132,'tete':140,'amorce':150}[k]
    small={'balises':26,'cle':24,'tete':26,'amorce':30}[k]
    card={'balises':58,'cle':52,'tete':56,'amorce':62}[k]
    chips=''.join(f'<div style="display:flex;flex-direction:column;gap:8px"><div style="width:92px;height:56px;background:{h};{"box-shadow:inset 0 0 0 1px rgba(236,229,216,.2)" if h==ENCRE else ""}"></div><span class="m" style="font-size:11px">{n} {h}</span></div>'
                  for n,h in (('encre',ENCRE),('os',OS),('braise',BRAISE)))
    body=f'''
<div style="display:grid;grid-template-columns:560px minmax(0,1fr);gap:48px;flex:1;min-height:0">
 <div style="display:flex;flex-direction:column;gap:28px">
  <div class="tile" style="height:560px"><span class="m cap">Symbole</span>{svg(mk,style="width:300px;height:300px")}</div>
  <div class="txt">{c}</div>
 </div>
 <div style="display:flex;flex-direction:column;gap:24px;min-width:0">
  <div class="tile" style="height:330px"><span class="m cap">Logo complet</span>{lk(big)}</div>
  <div style="display:flex;gap:40px;align-items:flex-end;justify-content:space-between">
   <div style="display:flex;flex-direction:column;gap:10px;min-width:0">
    <span class="m">Typographies</span>
    <span style="font-family:{fam};font-weight:{fw};font-size:40px;line-height:1.05;letter-spacing:{'.06em' if k=='amorce' else '-.02em'}">Nous faisons bouger les marques.</span>
    <span style="font-family:{bodyfam};font-weight:{bodyw};font-size:17px;color:#CFC8BB">{t1} pour les titres · {t2} pour le texte · JetBrains Mono pour les données</span>
   </div>
   <div style="display:flex;gap:14px;flex:none">{chips}</div>
  </div>
  <div class="txt" style="font-size:17px"><b>Système :</b> {sy}</div>
  <div style="display:flex;gap:24px;align-items:flex-end;margin-top:auto">
   <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Avatar</span>
    <div style="width:170px;height:170px;border-radius:50%;background:{ENCRE};box-shadow:inset 0 0 0 1px rgba(236,229,216,.16);display:flex;align-items:center;justify-content:center">{svg(mk,style="width:84px;height:84px")}</div></div>
   <div style="display:flex;flex-direction:column;gap:10px"><span class="m">Fin de vidéo</span>
    <div style="width:380px;height:214px;background:#0A0908;box-shadow:inset 0 0 0 1px rgba(236,229,216,.1);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px">{lk(card*0.55)}<span class="m" style="font-size:9px;letter-spacing:.22em">Motion design · Sites web · Cotonou</span></div></div>
   <div style="display:flex;flex-direction:column;gap:10px;flex:1;min-width:0"><span class="m">En-tête du site</span>
    <div style="height:72px;background:#0A0908;box-shadow:inset 0 0 0 1px rgba(236,229,216,.1);display:flex;align-items:center;justify-content:space-between;padding:0 22px;gap:16px">{lk(small*0.8)}
     <span style="font-family:{bodyfam};font-size:13px;color:#CFC8BB;white-space:nowrap">Réalisations · Méthode</span>
     <span style="background:{BRAISE};color:{ENCRE};font-family:{bodyfam};font-weight:500;font-size:13px;padding:9px 14px;border-radius:999px;white-space:nowrap">Démarrer un projet</span></div></div>
  </div>
 </div>
</div>'''
    page(f'0{i+1}-{k}',f'Proposition 0{i+1} · {nom}',f'0{i+1} / 04',body)
print('ok')
