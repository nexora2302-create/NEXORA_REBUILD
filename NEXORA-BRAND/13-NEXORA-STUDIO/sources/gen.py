"""Logo NEXORA Studio en tracés vectoriels (Unbounded 700 + Mr Dafoe), favicon N + s."""
import json, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
HERE=os.path.dirname(os.path.abspath(__file__))
M=json.load(open(os.path.join(HERE,'metrics.json')))
U=TTFont(os.path.join(HERE,'font/Unbounded.woff2')); Dd=TTFont(os.path.join(HERE,'font/MrDafoe.woff2'))
def gpath(font, ch, x, y, s=1.0):
    gs=font.getGlyphSet(); name=font.getBestCmap()[ord(ch)]
    pen=SVGPathPen(gs, ntos=lambda v: f'{v:.1f}'.rstrip('0').rstrip('.'))
    gs[name].draw(TransformPen(pen,(s,0,0,-s,x,y)))
    return pen.getCommands()
def asc_desc(font): return font['hhea'].ascent, -font['hhea'].descent
uA,uD=asc_desc(U); dA,dD=asc_desc(Dd)
LS=-35
def E_custom(x,y):
    # E redessiné, sans le fût pincé de l'Unbounded : fût 220, bras 180 (unités de 1000 par em)
    pts=[(0,0),(710,0),(710,180),(220,180),(220,285),(650,285),(650,465),(220,465),(220,570),(710,570),(710,750),(0,750)]
    return 'M'+' L'.join(f'{x+px:.0f} {y-750+py:.0f}' for px,py in pts)+' Z'
def nexora_paths(base_y=0):
    out=[]
    for i,ch in enumerate('NEXORA'):
        x=M['U'][i]+LS*i
        out.append(E_custom(x+40,base_y) if ch=='E' else gpath(U,ch,x,base_y))
    return ' '.join(out)
# --- logotype : mêmes réglages que la planche validée (NEXORA 1 em, Studio 1 em, posé à plat, recouvre le bas du mot)
base_U=(1000-(uA+uD))/2+uA
right_U=M['U'][6]+LS*6
studio_left=right_U+53-M['D'][6]
top_D=1000-387; base_D=top_D+(800-(dA+dD))/2+dA
studio=' '.join(gpath(Dd,ch,studio_left+M['D'][i],base_D) for i,ch in enumerate('Studio'))
word=nexora_paths(base_U)
# boîte : du haut des capitales au bas de l'écriture
x0=-10; y0=base_U-760; x1=max(right_U, studio_left+M['Dbox'][1])+20; y1=base_D+M['Dbox'][3]+40
vb=f'{x0:.0f} {y0:.0f} {x1-x0:.0f} {y1-y0:.0f}'
# --- favicon : N de l'Unbounded + le S manuscrit de « Studio », qui traverse le N
# N : boîte 0..750 de haut ; S (Mr Dafoe) : bornes mesurées, mis à l'échelle pour couvrir le bas droit du N
NB=(70,0,902,750)
fsN=0.74; Nx=1000/2-((NB[0]+NB[2])/2)*fsN-70; Nb=500+375*fsN
N=gpath(U,'N',Nx,Nb,fsN)
SB=(-191,-63,806,633)
ssS=0.66; Sx=625-((SB[0]+SB[2])/2)*ssS; Sb=650+((SB[1]+SB[3])/2)*ssS
s_=gpath(Dd,'S',Sx,Sb,ssS)
json.dump({'viewBox':vb,'word':word,'studio':studio,'fav':{'N':N,'s':s_}},open(os.path.join(HERE,'logo.json'),'w'))
def svg_logo(fg,acc,bg=None):
    rect=f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{x1-x0:.0f}" height="{y1-y0:.0f}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{rect}<path fill="{fg}" d="{word}"/><path fill="{acc}" d="{studio}"/></svg>'
def svg_fav(bg='#0D0C0B',fg='#ECE5D8',acc='#FF4A1C',r=220):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><rect width="1000" height="1000" rx="{r}" fill="{bg}"/>'
            f'<path fill="{fg}" d="{N}"/><path fill="{acc}" d="{s_}" stroke="{bg}" stroke-width="34" paint-order="stroke"/></svg>')
os.makedirs(os.path.join(HERE,'out'),exist_ok=True)
open(os.path.join(HERE,'out/nexora-studio-sombre.svg'),'w').write(svg_logo('#ECE5D8','#FF4A1C'))
open(os.path.join(HERE,'out/nexora-studio-clair.svg'),'w').write(svg_logo('#0D0C0B','#FF4A1C'))
open(os.path.join(HERE,'out/nexora-studio-braise.svg'),'w').write(svg_logo('#0D0C0B','#ECE5D8'))
open(os.path.join(HERE,'out/icon.svg'),'w').write(svg_fav())
html=('<!doctype html><html><body style="margin:0;background:#161412;display:flex;flex-wrap:wrap;gap:40px;padding:40px;align-items:center">'
      f'<div style="background:#0D0C0B;padding:60px">{svg_logo("#ECE5D8","#FF4A1C").replace("<svg ","<svg style=\"width:900px\" ")}</div>'
      f'<div style="background:#ECE5D8;padding:40px">{svg_logo("#0D0C0B","#FF4A1C").replace("<svg ","<svg style=\"width:420px\" ")}</div>'
      + ''.join(f'<div>{svg_fav().replace("<svg ",f"<svg style=\"width:{w}px\" ")}</div>' for w in (260,64,32,16))
      + f'<div style="background:#0D0C0B;padding:16px 24px">{svg_logo("#ECE5D8","#FF4A1C").replace("<svg ","<svg style=\"height:26px\" ")}</div>'
      + '</body></html>')
open(os.path.join(HERE,'preview.html'),'w').write(html)
print('viewBox',vb)
