import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v74.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:90]); return s.replace(a, b)
h = rep(h, "const APP_VER=73", "const APP_VER=74")
# moto 11: SUPER CHARGER (kit Riva Racing, negra con detalles rojos)
a = "side:{deck:'#d6c39a',hood:'#1d1f24',hull:'#c9b48a',trim:'#15171b',seatA:'#e3202b',seatB:'#3a3d45',seatC:'#1d1f24',stripe:'#1d1f24'},face:{skin:'#e2b088',hair:'#3a2a1a',style:'short',vest:'#1b1d22'}}"
h = rep(h, a, a + """,
 {id:'charger',name:'SUPER CHARGER',riva:1,colors:'Negra y roja · Kit Riva Racing',pilot:'Rayo Ferrer',bio:'Compresor a tope. La más rápida del taller.',ui:'#ff3b3b',st:{vel:5,ace:5,giro:4,turbo:5},
  sk:{hull:'#1c1e23',hullD:'#0b0c0f',acc:'#e3202b',seat:'#1c1e23',hood:'#16181d',rim:'#e3202b',vest:'#16181d',helmet:'#16181d',hs:'#e3202b',arm:'#16181d'},
  side:{deck:'#1c1e23',hood:'#16181d',hull:'#16181d',trim:'#0a0b0d',seatA:'#1c1e23',seatB:'#2a2d33',seatC:'#e3202b',stripe:'#e3202b'},face:{skin:'#e8b48c',hair:'#1a120c',style:'short',vest:'#16181d'}}""")
h = rep(h, "gris:[15000,0],dorada:[20000,0]};", "gris:[15000,0],dorada:[20000,0],charger:[25000,0]};")
h = rep(h, "dorada:'Kit Riva Racing: la joya del taller. La más cara.'", "dorada:'Kit Riva Racing: la joya del taller.',charger:'Kit Riva Racing: compresor a tope. La más rápida y la más cara.'")
h = rep(h, '"dorada": ["#b8903c", "#d6c39a", "#d6c39a", "#1d1f24", "#e3202b"]}', '"dorada": ["#b8903c", "#d6c39a", "#d6c39a", "#1d1f24", "#e3202b"], "charger": ["#16181d", "#16181d", "#16181d", "#e3202b", "#16181d"]}')
open(H, 'w').write(h); print('ok')
