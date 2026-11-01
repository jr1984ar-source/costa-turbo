p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
HOME='<button class="btn ghost sm hm" data-home style="flex:none"><svg class="hm-i" viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8 8 2.5 14 8M4 7v6.5h3V10h2v3.5h3V7" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/></svg>INICIO</button>'
for bid,title in [('aBack','TU PILOTO'),('gBack','ELIGE TU MOTO'),('pBack','PINTURA'),('fBack','CARRERA LIBRE')]:
    rep(f'<button class="btn ghost sm" id="{bid}" style="flex:none">‹ VOLVER</button><h2 class="h">{title}</h2><span style="width:70px"></span>',
        f'<button class="btn ghost sm" id="{bid}" style="flex:none">‹ ATRÁS</button><h2 class="h">{title}</h2>{HOME}')
rep('<button class="btn ghost sm" id="sBack" style="flex:none">‹ VOLVER</button><h2 class="h">TALLER</h2><div class="cash"><i class="coin"></i><span class="cashv">0</span></div></div>',
    '<button class="btn ghost sm" id="sBack" style="flex:none">‹ ATRÁS</button><h2 class="h">TALLER</h2>'+HOME+'</div>\n      <div class="cash"><i class="coin"></i><span class="cashv">0</span>&nbsp;PTA</div>')
hd=lambda i:f'<div class="head"><button class="btn ghost sm" id="{i}" style="flex:none">‹ ATRÁS</button><span class="sp"></span>{HOME}</div>\n      '
rep('<canvas id="mapCv" width="880" height="495"></canvas>',hd('mBk')+'<canvas id="mapCv" width="880" height="495"></canvas>')
rep('<button class="btn ghost" id="mBack" style="width:100%" hidden>‹ OTRA PANTALLA</button>','')
rep('<h2 class="h" id="rTitle"></h2>',hd('rBk')+'<h2 class="h" id="rTitle"></h2>')
rep('<h2 class="h">PAUSA</h2>',hd('psBk')+'<h2 class="h">PAUSA</h2>')
rep('<h2 class="h" id="oTitle">FIN DE LA PARTIDA</h2>',hd('oBk')+'<h2 class="h" id="oTitle">FIN DE LA PARTIDA</h2>')
rep('<h2 class="h">TOP 10</h2>',hd('rkBk')+'<h2 class="h">TOP 10</h2>')
# CSS
rep("/* usuario */",""".head .btn.sm{padding:8px 10px;font-size:13px}
.head h2.h{flex:1;min-width:0;text-align:center;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-size:clamp(20px,6vw,30px)}
.head .sp{flex:1}
.hm{display:inline-flex;align-items:center;gap:4px}.hm-i{width:14px;height:14px;flex:none}
/* usuario */""")
# JS
rep("$('#mBack').hidden=!G.free;}","}")
rep("on('#mBack',()=>{Snd.click();goFree();});","""on('#mBk',()=>{Snd.click();if(G.free)goFree();else goGarage();});
on('#rBk',()=>{Snd.click();const n=G._next;G._next=null;n&&n();});
on('#psBk',()=>resume());on('#oBk',()=>{Snd.click();goTitle();});on('#rkBk',()=>{Snd.click();goTitle();});
function midChamp(){return !!G._champOn&&!G.free&&(G.zi>0||G.lap>0)&&G.mode!=='over';}
function goHome(){if(midChamp()&&!confirm('¿Volver al inicio? Dejas el campeonato a medias.'))return;Snd.click();goTitle();}
document.addEventListener('click',e=>{const b=e.target.closest&&e.target.closest('[data-home]');if(!b)return;e.preventDefault();Snd.init();goHome();});""")
rep("on('#aBack',()=>{Snd.click();goTitle();","on('#aBack',()=>{goHome();")
rep("function goTitle(){Snd.engineStop();","function goTitle(){G._champOn=false;Snd.engineStop();")
rep("function newGame(){G.free=false;","function newGame(){G._champOn=true;G.free=false;")
rep("if(G.free)goFree();else newGame();});","if(G.free)goFree();else if(G._champOn){G.parts=partsOf(MOTOS[G.moto]);goMap();}else newGame();});")
rep("(G.free?'ELEGIR Y VER PANTALLAS':'ELEGIR ESTA MOTO')","(G.free?'ELEGIR Y VER PANTALLAS':G._champOn?'SEGUIR CON ESTA MOTO':'ELEGIR ESTA MOTO')")
open(p,'w').write(s);print('ok')
