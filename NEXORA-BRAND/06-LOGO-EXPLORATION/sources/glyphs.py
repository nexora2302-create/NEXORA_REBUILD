import sys, json
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
src=sys.argv[1]; out={}
for wght in (900, 800, 700):
    f=TTFont(src); inst=instantiateVariableFont(f,{'wdth':125,'wght':wght})
    gs=inst.getGlyphSet(); cmap=inst.getBestCmap(); cap=inst['OS/2'].sCapHeight
    d={}
    for ch in 'NEXORA':
        g=cmap[ord(ch)]; pen=SVGPathPen(gs); tp=TransformPen(pen,(1,0,0,-1,0,cap)); gs[g].draw(tp)
        bp=BoundsPen(gs); gs[g].draw(bp)
        d[ch]={'d':pen.getCommands(),'adv':gs[g].width,'bounds':bp.bounds}
    out[wght]={'cap':cap,'g':d}
json.dump(out,open(sys.argv[2],'w'))
print({w:{c:(v['g'][c]['adv'],[round(b) for b in v['g'][c]['bounds']]) for c in 'NEXORA'} for w,v in out.items()})
