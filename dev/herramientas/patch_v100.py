import shutil,json
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v100.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
RM = json.load(open('realmap4.json'))
h = rep(h, "const APP_VER=99", "const APP_VER=100")
i0 = h.index("const RMAP={"); i1 = h.index("let RMD=null;", i0)
h = h[:i0] + "const RMAP={w:%d,h:%d,c:3,src:'%s'};const RCOR=%s;const RSPOTS=%s;" % (RM['w'], RM['h'], RM['src'], json.dumps(RM['cor'], separators=(',', ':')), json.dumps(RM['spots'], separators=(',', ':'))) + h[i1:]
h = rep(h, "{name:'SON MATÍAS · MODO LIBRE',realMap:1,playground:1,water:['#22b3d6','#0b6fb3'],obj:'free',goal:'Modo libre: navega por donde quieras. Rampas, olas, lanchas con esquí acuático, motos de otra gente y una recta larguísima para ir a fondo. Para salir, pulsa pausa.',",
 "{name:'SON MATÍAS · MODO LIBRE',realMap:1,playground:1,water:['#22b3d6','#0b6fb3'],obj:'free',goal:'Modo libre: un lago enorme para explorar. Islas, calas escondidas, un faro, rampas, olas, lanchas con esquí y una recta larguísima. Busca los premios escondidos. Para salir, pulsa pausa.',")
# ---- tierra inventada (bosque = 7) ----
h = rep(h, "const rmLand=(x,y)=>{const v=rmV(x,y);return v>0&&v<5;};", "const rmLand=(x,y)=>{const v=rmV(x,y);return (v>0&&v<5)||v===7;};")
h = rep(h, "const landM=mask(v=>v>0&&v<5),outM=mask(v=>v===6);", "const landM=mask(v=>(v>0&&v<5)||v===7),outM=mask(v=>v===6);")
h = rep(h, "layer(landM,'#a9c47c');layer(mask(v=>v===2),'#f1d9a6');}", "layer(landM,'#a9c47c');layer(mask(v=>v===7),'#7c9f53');layer(mask(v=>v===2),'#f1d9a6');}")
h = rep(h, "if(!(v>0&&v<5)||v===2)continue;if(rmIn(x,y,14))continue;", "if(!((v>0&&v<5)||v===7)||v===2)continue;if(rmIn(x,y,14))continue;")
h = rep(h, "for(let y=y0-6;y<y1+6;y+=6)if(rmIn(sx,y,22))", "for(let y=y0-6;y<y1+6;y+=6)if(rmIn(sx,y,22)&&rmV(sx,y)!==7)")
h = rep(h, "for(let x=x0-6;x<x1+6;x+=6)if(rmIn(x,sy,22))", "for(let x=x0-6;x<x1+6;x+=6)if(rmIn(x,sy,22)&&rmV(x,sy)!==7)")
h = rep(h, "for(let kx=jx0;kx<=jx1;kx++){const sx=stX(kx);if(sx<x0-20||sx>x1+20)continue;for(let y=Math.floor(y0/14)*14;y<y1;y+=14)if(rmIn(sx,y,22))", "for(let kx=jx0;kx<=jx1;kx++){const sx=stX(kx);if(sx<x0-20||sx>x1+20)continue;for(let y=Math.floor(y0/14)*14;y<y1;y+=14)if(rmIn(sx,y,22)&&rmV(sx,y)!==7)")
h = rep(h, "for(let ky=jy0;ky<=jy1;ky++){const sy=stY(ky);if(sy<y0-20||sy>y1+20)continue;for(let x=Math.floor(x0/14)*14;x<x1;x+=14)if(rmIn(x,sy,22))", "for(let ky=jy0;ky<=jy1;ky++){const sy=stY(ky);if(sy<y0-20||sy>y1+20)continue;for(let x=Math.floor(x0/14)*14;x<x1;x+=14)if(rmIn(x,sy,22)&&rmV(x,sy)!==7)")
h = rep(h, "const forest=v===3&&r2<.5;\n    g.fillStyle=(a+b)%2?'#9cbd69':'#b2cd82';g.fillRect(lx+1.5,ly+1.5,lw-3,lh-3);g.strokeStyle='#6f9449';g.lineWidth=1.6;g.strokeRect(lx+1.5,ly+1.5,lw-3,lh-3);",
 "const forest=v===7||(v===3&&r2<.5);\n    if(!forest){g.fillStyle=(a+b)%2?'#9cbd69':'#b2cd82';g.fillRect(lx+1.5,ly+1.5,lw-3,lh-3);g.strokeStyle='#6f9449';g.lineWidth=1.6;g.strokeRect(lx+1.5,ly+1.5,lw-3,lh-3);}")
# pinos sueltos por el bosque
h = rep(h, "  // calles\n  const jx0=", "  for(let k=0;k<70;k++){const x=x0+q()*CW,y=y0+q()*CH;if(rmV(x,y)===7&&rmIn(x,y,10))drawDeco(g,{t:'pine',x,y,r:8+q()*9,s:(q()*1e6)|0},Zn);}\n  // calles\n  const jx0=")
h = rep(h, "land=v>0&&v<5;", "land=(v>0&&v<5)||v===7;")
# ---- premios escondidos, islita, faro ----
h = rep(h, "function updatePG(dt){", r"""const PG_GEAR=[['helm','h6'],['vest','v5'],['suit','s6'],['gog','g7'],['glove','gl4'],['helm','h5'],['vest','v4'],['suit','s5']];
function pgHidden(O){const S=RSPOTS;if(!S)return;
 (S.gear||[]).forEach((p,i)=>{const gi=PG_GEAR[i%PG_GEAR.length],it=gearItem(gi[0],gi[1]);if(gearStore.own.includes(it.id))return;O.push({t:'gearbox',x:p[0],y:p[1],cat:gi[0],id:it.id,name:(it.b&&it.b!=='De serie'?it.b+' ':'')+it.n,ph:i});});
 for(const p of S.heart||[])O.push({t:'heart',x:p[0],y:p[1]});
 for(const p of S.can||[])O.push({t:'can',x:p[0],y:p[1]});
 for(const p of S.coins||[])for(let i=0;i<8;i++){const a=i/8*TAU;O.push({t:'coin',x:p[0]+Math.cos(a)*34,y:p[1]+Math.sin(a)*34});}
 for(const p of S.palms||[])O.push({t:'bpalm',x:p[0],y:p[1]});
 (S.girls||[]).forEach((p,i)=>O.push({t:'bgirl',x:p[0],y:p[1],hair:['#f2cf63','#5a3218','#111111','#b5402a'][i%4],bik:['#ff3f8e','#22c4ff','#ffd21a','#7be35a'][i%4],ph:i*1.7}));
 if(S.faro)O.push({t:'faro',x:S.faro[0]+34,y:S.faro[1]});}
function updatePG(dt){""")
h = rep(h, " // monedas\n for(let n=0,t=0;n<45", " pgHidden(O);\n // monedas\n for(let n=0,t=0;n<45")
# saludos de las chicas de la islita
h = rep(h, " const L=Zn.lane;if(L&&P.prevY>L.mid", " if(!Zn._girls)Zn._girls=Zn.objs.filter(o=>o.t==='bgirl');for(const o of Zn._girls){const d=Math.hypot(P.x-o.x,P.y-o.y);if(d<170&&!o.said){o.said=1;o.wave=3;pop(o.x,o.y-26,['¡Holaaa!','¡Guapo!','¡Ven aquí!','¡Qué moto!'][(Math.random()*4)|0],'#ff8fc4');Snd.girls&&Snd.girls();}else if(d>420)o.said=0;if(o.wave>0)o.wave-=dt;}\n const L=Zn.lane;if(L&&P.prevY>L.mid")
# recoger piezas de equipo
h = rep(h, "if(o.t==='coin'){if(!o.got&&c.isP&&!G.demo&&Math.hypot(o.x-c.x,o.y-c.y)<17)",
 "if(o.t==='bgirl'||o.t==='bpalm'||o.t==='faro')continue;\n   if(o.t==='gearbox'){if(!o.got&&c.isP&&!G.demo&&Math.hypot(o.x-c.x,o.y-c.y)<26){o.got=1;if(!gearStore.own.includes(o.id)){gearStore.own.push(o.id);saveGear();}Snd.cash();buzz(80);G.shake=3;msg('¡PREMIO ESCONDIDO!',o.name+' · ya es tuyo en EQUIPO','#ffe14d');splash(o.x,o.y,30,160,'#ffe14d');}continue;}\n   if(o.t==='coin'){if(!o.got&&c.isP&&!G.demo&&Math.hypot(o.x-c.x,o.y-c.y)<17)")
# dibujo
h = rep(h, " case 'fwave':{", r""" case 'gearbox':{if(o.got)return;const p=1+Math.sin(G.t*4+o.ph)*.1,bob=Math.sin(G.t*2.5+o.ph)*3;ctx.save();ctx.translate(o.x,o.y+bob);
  const rg=ctx.createRadialGradient(0,0,4,0,0,40);rg.addColorStop(0,'rgba(255,225,80,.75)');rg.addColorStop(1,'rgba(255,225,80,0)');ctx.fillStyle=rg;ctx.beginPath();ctx.arc(0,0,40*p,0,TAU);ctx.fill();
  ctx.rotate(Math.sin(G.t*1.5+o.ph)*.15);ctx.fillStyle='rgba(0,20,50,.3)';ctx.fillRect(-11,-7,26,22);ctx.fillStyle='#f2b81e';ctx.fillRect(-13,-11,26,22);ctx.fillStyle='#ffd95a';ctx.fillRect(-13,-11,26,6);ctx.fillStyle='#e3202b';ctx.fillRect(-2.5,-11,5,22);ctx.fillRect(-13,-2.5,26,5);
  ctx.strokeStyle='#e3202b';ctx.lineWidth=2.4;ctx.beginPath();ctx.ellipse(-5,-14,5,3.5,-.5,0,TAU);ctx.ellipse(5,-14,5,3.5,.5,0,TAU);ctx.stroke();
  ctx.fillStyle='#ffffff';for(let k=0;k<4;k++){const a=G.t*2+k*1.57+o.ph;ctx.globalAlpha=.6+.4*Math.sin(G.t*6+k);ctx.beginPath();ctx.arc(Math.cos(a)*22,Math.sin(a)*22,2,0,TAU);ctx.fill();}ctx.restore();}return;
 case 'bgirl':drawGirl(ctx,o.x,o.y,o.hair,o.bik,(o.wave||0)>0||Math.sin(G.t*.7+o.ph)>.6,G.t*3+o.ph);return;
 case 'bpalm':drawDeco(ctx,{t:'palm',x:o.x,y:o.y,r:13,s:(o.x*7+o.y)|0},G.zone);return;
 case 'fwave':{""")
open(H, 'w').write(h); print('ok')
