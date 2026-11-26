import os
HERE=os.path.dirname(os.path.abspath(__file__))
FONTS='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;500;700&family=Mr+Dafoe&family=Mrs+Saint+Delafield&family=Bodoni+Moda:ital,opsz,wght@1,6..96,800&family=JetBrains+Mono:wght@400;500&display=swap">'
ENCRE,OS,BRAISE,CHARBON,PIERRE='#0D0C0B','#ECE5D8','#FF4A1C','#161412','#9A9386'
def T(color=BRAISE, h='.82em', extra=''):
    return (f'<svg class="bt" style="height:{h};{extra}" viewBox="0 0 100 106" aria-hidden="true">'
            f'<path fill="{color}" d="M2 26 C0 12 8 3 22 3 C46 2 74 1 100 0 C99 9 92 15 82 18 C62 22 40 24 18 30 C9 33 3 32 2 26 Z"/>'
            f'<path fill="{color}" d="M36 18 C44 15 58 14 66 15 C65 44 63 72 61 97 C60 101 58 103 54 103 L45 105 C42 105 40 103 40 99 C39 72 38 45 36 18 Z"/></svg>')
def logo(size, fg=OS, t=BRAISE):
    return f'<div class="w" style="font-size:{size}px;color:{fg}">NEX{T(t)}UDIO</div>'
CSS=f'''*{{box-sizing:border-box}}body{{margin:0;background:{ENCRE};color:{OS};font-family:Unbounded,sans-serif}}
.pg{{width:1920px;height:1080px;position:relative;overflow:hidden;padding:72px 88px;display:flex;flex-direction:column}}
.w{{font-weight:700;line-height:1;letter-spacing:-.035em;display:flex;align-items:baseline;white-space:nowrap}}
.bt{{display:inline-block;width:auto;margin:0 -.005em 0 -.025em;overflow:visible;flex:none}}
.m{{font-family:'JetBrains Mono',monospace;font-size:14px;letter-spacing:.1em;text-transform:uppercase;color:{PIERRE}}}
.hd{{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid rgba(236,229,216,.14);padding-bottom:18px}}
.ft{{position:absolute;left:88px;right:88px;bottom:56px;display:flex;justify-content:space-between}}
.lead{{font-family:Unbounded;font-weight:400;font-size:22px;line-height:1.5;letter-spacing:-.01em;color:#CFC8BB;max-width:880px}}
'''
def page(name, title, num, body, bg=ENCRE):
    html=f'<!doctype html><html lang="fr"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body><div class="pg" style="background:{bg}">'
    html+=f'<div class="hd"><span class="m">Nextudio · identité</span><span class="m">{title}</span><span class="m">{num}</span></div>{body}</div></body></html>'
    open(os.path.join(HERE,name+'.html'),'w').write(html)

# 01 logo principal
page('01-logo','Logo principal','01 / 06',f'''
<div style="flex:1;display:flex;align-items:center;justify-content:center">{logo(196)}</div>
<div class="ft"><span class="m">Unbounded 700 · T peint à la main · encre, os, braise</span><span class="m">Next + studio : un seul T</span></div>''')

# 02 construction
dim='rgba(236,229,216,.22)'
page('02-construction','L’idée','02 / 06',f'''
<div style="flex:1;display:flex;align-items:center;justify-content:center">
 <div style="display:inline-flex;flex-direction:column;gap:30px">
  <div style="align-self:flex-start;position:relative"><div class="w" style="font-size:120px;color:{dim}">NEX{T(BRAISE)}</div><span class="m" style="color:{OS};position:absolute;left:calc(100% + 32px);top:50%;transform:translateY(-50%);white-space:nowrap">next · demain, la suite</span></div>
  {logo(120)}
  <div style="align-self:flex-end;position:relative"><div class="w" style="font-size:120px;color:{dim}">S{T(BRAISE)}UDIO</div><span class="m" style="color:{OS};position:absolute;right:calc(100% + 32px);top:50%;transform:translateY(-50%);white-space:nowrap">studio · le savoir-faire</span></div>
 </div>
</div>
<div class="ft"><span class="lead" style="font-size:20px">Le T finit « next » et commence « studio ». C’est la seule lettre tracée à la main : la machine regarde devant, la main fait le travail.</span></div>''')

# 03 variantes du T
page('03-variantes','Le T : deux écritures','03 / 06',f'''
<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center;padding-top:40px">
 <div style="display:flex;flex-direction:column;gap:28px;align-items:center">
  <div style="width:100%;height:420px;background:{CHARBON};display:flex;align-items:center;justify-content:center">{logo(112)}</div>
  <span class="m" style="color:{OS}">A · T au pinceau · recommandé</span>
 </div>
 <div style="display:flex;flex-direction:column;gap:28px;align-items:center">
  <div style="width:100%;height:420px;background:{CHARBON};display:flex;align-items:center;justify-content:center"><div class="w" style="font-size:112px">NEX<span style="font-family:'Bodoni Moda';font-style:italic;font-weight:800;font-size:1.22em;color:{BRAISE};letter-spacing:0;line-height:.7;margin-left:-.02em">T</span>UDIO</div></div>
  <span class="m">B · T en Bodoni italique · plus éditorial</span>
 </div>
</div>
<div class="ft"><span class="m">A garde le geste de la main, comme le « Studio » de NEXORA Studio · B est plus chic, moins à nous</span></div>''')

# 04 monogramme et déclinaisons
def tile(bg, fg, label, size=240, r='0'):
    return f'''<div style="display:flex;flex-direction:column;gap:18px;align-items:center"><div style="width:{size}px;height:{size}px;border-radius:{r};background:{bg};display:flex;align-items:center;justify-content:center;font-size:{int(size*0.62)}px">{T(fg,'.82em','margin:0')}</div><span class="m">{label}</span></div>'''
page('04-declinaisons','Symbole et déclinaisons','04 / 06',f'''
<div style="display:flex;gap:56px;justify-content:center;align-items:flex-end;margin-top:72px">
 {tile(ENCRE,BRAISE,'Avatar',240,'50%').replace('background:#0D0C0B','background:#0D0C0B;box-shadow:inset 0 0 0 1px rgba(236,229,216,.18)')}
 {tile(BRAISE,ENCRE,'Icône d’application',240,'52px')}
 {tile(OS,BRAISE,'Sur fond clair',240,'0')}
 <div style="display:flex;flex-direction:column;gap:18px;align-items:center"><div style="display:flex;gap:28px;align-items:flex-end">
  <div style="width:64px;height:64px;border-radius:14px;background:{BRAISE};display:flex;align-items:center;justify-content:center;font-size:40px">{T(ENCRE,'.82em','margin:0')}</div>
  <div style="width:32px;height:32px;border-radius:7px;background:{BRAISE};display:flex;align-items:center;justify-content:center;font-size:20px">{T(ENCRE,'.82em','margin:0')}</div>
 </div><span class="m">Favicon 64 et 32</span></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-top:72px">
 <div style="background:{OS};height:250px;display:flex;align-items:center;justify-content:center">{logo(76, ENCRE, BRAISE)}</div>
 <div style="background:{BRAISE};height:250px;display:flex;align-items:center;justify-content:center">{logo(76, ENCRE, OS)}</div>
</div>''')

# 05 en situation
page('05-situation','En situation','05 / 06',f'''
<div style="display:flex;gap:48px;margin-top:44px">
 <div style="display:flex;flex-direction:column;gap:14px"><span class="m">Fin de vidéo, 16:9</span>
  <div style="width:1056px;height:594px;background:#0A0908;position:relative;display:flex;align-items:center;justify-content:center">{logo(118)}
   <div class="m" style="position:absolute;left:0;right:0;bottom:40px;text-align:center;letter-spacing:.24em">Motion design · Sites web · Cotonou</div></div></div>
 <div style="display:flex;flex-direction:column;gap:14px;flex:1"><span class="m">Sous-titre de montage</span>
  <div style="background:#0A0908;padding:22px 26px;border-left:4px solid {BRAISE};display:flex;flex-direction:column;gap:6px">
   <span style="font-weight:700;font-size:30px;letter-spacing:-.02em">LE NOUVEAU CODE</span>
   <span style="font-family:'Mr Dafoe';font-size:44px;line-height:1;color:{BRAISE}">de la route</span></div>
  <span class="m" style="margin-top:34px">Publication réseaux</span>
  <div style="width:300px;height:300px;background:{BRAISE};color:{ENCRE};padding:26px;display:flex;flex-direction:column;justify-content:space-between">
   <span style="font-weight:700;font-size:30px;line-height:1.05;letter-spacing:-.03em">NOUS FAISONS<br>BOUGER<br>LES MARQUES.</span>
   <div class="w" style="font-size:22px;color:{ENCRE}">NEX{T(OS)}UDIO</div></div>
 </div>
</div>
<div style="display:flex;flex-direction:column;gap:14px;margin-top:40px"><span class="m">En-tête du site</span>
 <div style="height:84px;background:#0A0908;display:flex;align-items:center;justify-content:space-between;padding:0 34px">
  {logo(28)}
  <div style="display:flex;gap:40px;font-weight:500;font-size:15px"><span>Studio</span><span>Expertises</span><span>Réalisations</span><span>Méthode</span></div>
  <span style="background:{BRAISE};color:{ENCRE};font-weight:500;font-size:15px;padding:14px 24px;border-radius:999px">Démarrer un projet</span></div>
</div>''')

# 06 NEXORA Studio affiné
def nx(size, script, sfam, ssize, mt, mr):
    return f'''<div style="display:inline-flex;flex-direction:column;align-items:flex-end"><div class="w" style="font-size:{size}px">NEXORA</div><div style="font-family:'{sfam}';font-size:{ssize}px;line-height:.8;color:{BRAISE};margin-top:{mt}px;margin-right:{mr}px">{script}</div></div>'''
page('06-nexora-studio','NEXORA Studio affiné','06 / 06',f'''
<div style="flex:1;display:flex;align-items:center;justify-content:center">{nx(150,'Studio','Mr Dafoe',150,-58,-8)}</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;margin-bottom:96px">
 <div style="background:{CHARBON};height:230px;display:flex;align-items:center;justify-content:center">{nx(70,'Studio','Mrs Saint Delafield',84,-12,-10)}</div>
 <div style="background:{OS};height:230px;display:flex;align-items:center;justify-content:center;color:{ENCRE}">{nx(70,'Studio','Mr Dafoe',70,-27,-4).replace('class="w" style="','class="w" style="color:#0D0C0B;')}</div>
</div>
<div class="ft"><span class="m">« Studio » redressé, posé à plat sur le bas du mot · en bas : variante plume (B), et version sur fond clair</span></div>''')
print('ok')
