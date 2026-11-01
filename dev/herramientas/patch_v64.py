import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v64.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a)
    assert c == n, (c, a[:90])
    return s.replace(a, b)
h = rep(h, "const APP_VER=63", "const APP_VER=64")
pil = open('pilot_svg.js').read()
pil = pil[:pil.index("if (typeof module")]
pil = rep(pil, "  g += `<g transform=\"translate(118 182) rotate(-6)\">", "  if (!V.plain) g += `<g transform=\"translate(118 182) rotate(-6)\">")
pil = rep(pil, "  if (V.name) g += `<rect", "  if (V.name && !V.plain) g += `<rect")
i0 = h.index("function pilotSVG(o, uid) {")
i1 = h.index("function gloveIcon(", i0)
h = h[:i0] + pil + h[i1:]
h = rep(h, " const S=q.suit.c?{c:q.suit.c,a:q.suit.a,pat:q.suit.pat}:{c:'#1d2027',a:'#3a3f4a'};",
        " const S=q.suit.c?{c:q.suit.c,a:q.suit.a,pat:q.suit.pat}:{},BARE=q.suit.c?null:{skin:av.skin,shorts:av.vest||'#1e5eff',shorts2:'#ffffff',lycra:'#1d2027'};")
h = rep(h, "pilotSVG({vest:V,suit:S,glove:q.glove.c||'#1d2027',gloveA:q.glove.a||null,noHelm:true},uid+'b')",
        "pilotSVG({vest:V,suit:S,bare:BARE,glove:q.glove.c||'#1d2027',gloveA:q.glove.a||null,noHelm:true},uid+'b')")
h = rep(h, "{id:'s0',n:'Sin neopreno',b:'De serie',p:0},", "{id:'s0',n:'Licra y bañador',b:'De serie',p:0},")
open(H, 'w').write(h)
print('ok')
