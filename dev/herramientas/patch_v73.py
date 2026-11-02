import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v73.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:90]); return s.replace(a, b)
h = rep(h, "const APP_VER=72", "const APP_VER=73")
# la INFERNO pasa a ser RÁFAGA, blanca y roja
h = rep(h, "{id:'inferno',name:'INFERNO',colors:'Roja y negra',", "{id:'inferno',name:'RÁFAGA',colors:'Blanca y roja',")
h = rep(h, "sk:{hull:'#e3202b',hullD:'#8f0f17',acc:'#ffffff',seat:'#1d1f24',vest:'#16181d',helmet:'#e3202b',hs:'#ffffff',arm:'#16181d'},\n  side:{deck:'#de1a24',hood:'#e8262f',hull:'#cf1820',trim:'#1b1d22',seatA:'#d9161f',seatB:'#b0121a',seatC:'#1b1d22',stripe:'#1b1d22'}",
 "sk:{hull:'#f5f6f8',hullD:'#c3c9d2',acc:'#e3202b',seat:'#e3202b',hood:'#e3202b',rim:'#e3202b',vest:'#16181d',helmet:'#e3202b',hs:'#ffffff',arm:'#16181d'},\n  side:{deck:'#f2f3f5',hood:'#e3202b',hull:'#e3202b',trim:'#1b1d22',seatA:'#e3202b',seatB:'#e3202b',seatC:'#1b1d22',stripe:'#e3202b'}")
h = rep(h, '"inferno": ["#d81e28", "#e3202b", "#e3202b", "#16181d", "#16181d"]', '"inferno": ["#e3202b", "#f4f5f7", "#e3202b", "#e3202b", "#e3202b"]')
open(H, 'w').write(h); print('ok')
