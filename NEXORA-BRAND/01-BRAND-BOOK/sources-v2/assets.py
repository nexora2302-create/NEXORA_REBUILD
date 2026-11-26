"""Fichiers du logo NEXORA Studio (SVG) à partir des tracés de 13-NEXORA-STUDIO/sources/logo.json."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.join(HERE, '..', '..')
L = json.load(open(os.path.join(B, '13-NEXORA-STUDIO', 'sources', 'logo.json')))
ENCRE, OS, BRAISE, BRAISE_P = '#0D0C0B', '#ECE5D8', '#FF4A1C', '#B02F0B'
VB = L['viewBox']; x0, y0, w, h = map(float, VB.split())
def logo(word, studio, bg=None, pad=0.0):
    p = pad * h
    vb = f'{x0-p:.0f} {y0-p:.0f} {w+2*p:.0f} {h+2*p:.0f}'
    rect = f'<rect x="{x0-p:.0f}" y="{y0-p:.0f}" width="{w+2*p:.0f}" height="{h+2*p:.0f}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{rect}<path fill="{word}" d="{L["word"]}"/><path fill="{studio}" d="{L["studio"]}"/></svg>'
def symbol(bg, n, s, r=220, stroke=None):
    st = stroke or bg
    rect = f'<rect width="1000" height="1000" rx="{r}" fill="{bg}"/>' if bg else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000">{rect}<path fill="{n}" d="{L["fav"]["N"]}"/>'
            f'<path fill="{s}" d="{L["fav"]["s"]}" stroke="{st}" stroke-width="34" paint-order="stroke"/></svg>')
FILES = {
 # logo complet
 'nexora-studio-sur-encre.svg': logo(OS, BRAISE, ENCRE, .35),
 'nexora-studio-sur-os.svg': logo(ENCRE, BRAISE_P, OS, .35),
 'nexora-studio-sur-braise.svg': logo(ENCRE, ENCRE, BRAISE, .35),
 'nexora-studio-sur-braise-grand-format.svg': logo(ENCRE, OS, BRAISE, .35),
 'nexora-studio-transparent-pour-fond-sombre.svg': logo(OS, BRAISE),
 'nexora-studio-transparent-pour-fond-clair.svg': logo(ENCRE, BRAISE_P),
 'nexora-studio-monochrome-encre.svg': logo(ENCRE, ENCRE),
 'nexora-studio-monochrome-os.svg': logo(OS, OS),
 # symbole N + S
 'symbole-ns-encre.svg': symbol(ENCRE, OS, BRAISE),
 'symbole-ns-os.svg': symbol(OS, ENCRE, BRAISE_P),
 'symbole-ns-carre-encre.svg': symbol(ENCRE, OS, BRAISE, r=0),
 'symbole-ns-monochrome-encre.svg': symbol(None, ENCRE, ENCRE, stroke='#FFFFFF00'),
}
out = os.path.join(B, '02-LOGO-BRAND-ASSETS', 'svg')
for n, s in FILES.items(): open(os.path.join(out, n), 'w').write(s)
open(os.path.join(B, '02-LOGO-BRAND-ASSETS', 'favicon', 'favicon.svg'), 'w').write(symbol(ENCRE, OS, BRAISE))
json.dump(list(FILES), open(os.path.join(HERE, 'assets-list.json'), 'w'))
print(len(FILES), 'fichiers SVG')
