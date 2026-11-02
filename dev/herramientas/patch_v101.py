import json,base64
p='costa-turbo.html';s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
# 1) mapa nuevo: lado derecho con la costa real girada, calas, laguna, bares y ruta del Piri-Piri
RM=json.load(open('/tmp/claude-0/-home-user/e02bf71e-076d-586d-89ee-84e1312586e6/scratchpad/costa_real/realmap5.json'))
i0=s.index("const RMAP={");i1=s.index("let RMD=null;",i0)
s=s[:i0]+"const RMAP={w:%d,h:%d,c:3,src:'%s'};const RCOR=%s;const RSPOTS=%s;"%(RM['w'],RM['h'],RM['src'],json.dumps(RM['cor'],separators=(',',':')),json.dumps(RM['spots'],separators=(',',':')))+s[i1:]
# 2) la recta larga va en la franja de agua libre más ancha (antes caía dentro de la tierra)
rep(""" const rightLand=y=>{for(let x=RMW-3;x>0;x-=9)if(rmLand(x,y))return x;return 0;};
 // recta larguísima mar adentro
 const y0=-900,y1=-10900;let mx=0;for(let y=y0;y>=y1;y-=120)mx=Math.max(mx,rightLand(y));const lx=Math.min(RMW-400,mx+650),lw=180;zone.lane={x:lx,w:lw,y0,y1,mid:(y0+y1)/2};""",
""" // recta larguísima mar adentro: en la franja de agua libre más ancha
 const y0=-900,y1=-10900,lw=180;let lx=0,bs=-1;
 for(let x=600;x<RMW-600;x+=30){let ok=true;for(let y=y0;y>=y1&&ok;y-=60)for(const dx of[-lw/2-110,-lw/2,0,lw/2,lw/2+110])if(rmLand(x+dx,y)){ok=false;break;}if(!ok)continue;
  let m=0;for(let k=1;k<14;k++){let f=true;for(let y=y0;y>=y1&&f;y-=150)if(rmLand(x-lw/2-110-k*40,y)||rmLand(x+lw/2+110+k*40,y))f=false;if(!f)break;m=k;}if(m>bs){bs=m;lx=x;}}
 if(!lx)lx=RMW/2;zone.lane={x:lx,w:lw,y0,y1,mid:(y0+y1)/2};""")
# 3) casco dorado escondido + bares Roxy y JJ
rep("if(S.faro)O.push({t:'faro',x:S.faro[0]+34,y:S.faro[1]});}",
"""if(S.faro)O.push({t:'faro',x:S.faro[0]+34,y:S.faro[1]});
 if(S.gold&&!gearStore.own.includes('h7'))O.push({t:'gearbox',x:S.gold[0],y:S.gold[1],cat:'helm',id:'h7',name:'Casco Dorado',ph:9,gold:1});
 if(S.roxy)O.push({t:'pgbar',k:'roxy',x:S.roxy[0],y:S.roxy[1],rot:Math.PI/2,ry:220});
 if(S.jj)O.push({t:'pgbar',k:'jj',x:S.jj[0],y:S.jj[1],rot:0,ry:220});}""")
rep("msg('¡PREMIO ESCONDIDO!',o.name+' · ya es tuyo en EQUIPO','#ffe14d');",
    "if(o.gold)msg('¡CASCO DORADO!','El premio más escondido · ya es tuyo en EQUIPO','#ffe14d');else msg('¡PREMIO ESCONDIDO!',o.name+' · ya es tuyo en EQUIPO','#ffe14d');")
rep("if(o.t==='bgirl'||o.t==='bpalm'||o.t==='faro')continue;","if(o.t==='bgirl'||o.t==='bpalm'||o.t==='faro'||o.t==='pgbar')continue;")
rep("zone.big=zone.objs.filter(o=>o.t==='island'||o.t==='pass'||o.t==='nozone');","zone.big=zone.objs.filter(o=>o.t==='island'||o.t==='pass'||o.t==='nozone'||o.t==='pgbar');")
rep("if(o.t!=='island'&&o.t!=='pass'&&o.t!=='nozone')drawObj(o);","if(o.t!=='island'&&o.t!=='pass'&&o.t!=='nozone'&&o.t!=='pgbar')drawObj(o);")
# 4) Piri-Piri navegando alrededor de la isla grande del norte
rep("n++;}}\nconst PG_GEAR=","""n++;}
 if(RSPOTS&&RSPOTS.piri){const Pp=RSPOTS.piri;M.push({t:'piripg',path:Pp,i:0,x:Pp[0][0],y:Pp[0][1],h:Math.atan2(Pp[1][0]-Pp[0][0],-(Pp[1][1]-Pp[0][1])),gift:0,gt:0,rx:Pp[0][0],ry:Pp[0][1],vx:0,vy:0,flash:0,trail:[]});}}
const PG_GEAR=""")
rep("else if(o.t==='npcjet'){","""else if(o.t==='piripg'){const n=o.path.length,tg=o.path[(o.i+1)%n],dx=tg[0]-o.x,dy=tg[1]-o.y,d=Math.hypot(dx,dy),sp=72*dt;
   if(d<sp+3)o.i=(o.i+1)%n;else{o.x+=dx/d*sp;o.y+=dy/d*sp;let dh=Math.atan2(dx,-dy)-o.h;while(dh>Math.PI)dh-=TAU;while(dh<-Math.PI)dh+=TAU;o.h+=dh*Math.min(1,1.8*dt);}
   o.rx=o.x+Math.cos(o.h)*50;o.ry=o.y+Math.sin(o.h)*50;o.tacc=(o.tacc||0)+sp;if(o.tacc>12){o.tacc=0;o.trail.unshift({x:o.x-Math.sin(o.h)*36,y:o.y+Math.cos(o.h)*36});if(o.trail.length>26)o.trail.pop();}
   if(o.gift){o.gt-=dt;if(o.gt<=0)o.gift=0;}
   if(!G.demo){const dp=Math.hypot(P.x-o.x,P.y-o.y);if(dp<30&&P.z<.5){const k=30/(dp||1);P.x=o.x+(P.x-o.x)*k;P.y=o.y+(P.y-o.y)*k;P.v*=1-3*dt;}
    if(!o.gift&&Math.hypot(P.x-o.rx,P.y-o.ry)<40){o.gift=1;o.gt=45;setHp(hpTot()+3);G.turbo=Math.min(5,G.turbo+2);turboUI();Snd.cash();Snd.pickup();msg('¡PIRI-PIRI!','+1 CORAZÓN · +2 TURBOS','var(--gold)');}}}
  else if(o.t==='npcjet'){""")
rep("g.fillStyle=o.t==='skiboat'?'#ffffff':'#ff4f8b';g.beginPath();g.arc(x,y,o.t==='skiboat'?2.6:2,0,TAU);",
    "g.fillStyle=o.t==='piripg'?'#ffd21a':o.t==='skiboat'?'#ffffff':'#ff4f8b';g.beginPath();g.arc(x,y,o.t==='piripg'?3.4:o.t==='skiboat'?2.6:2,0,TAU);")
# 5) dibujo: bares, Piri-Piri y caja dorada
rep("case 'bgirl':","""case 'pgbar':{const ca=Math.cos(o.rot),sa=Math.sin(o.rot);ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.rot);if(o.k==='roxy')drawRoxyTop(ctx,{barY:0,shore:()=>0});else drawJJMini(ctx);ctx.restore();
  const lx=o.k==='jj'?-94:-62,ly=o.k==='jj'?-96:0;ctx.save();ctx.translate(o.x+lx*ca-ly*sa,o.y+lx*sa+ly*ca);ctx.rotate(G.camA||0);label(0,0,o.k==='jj'?"BAR JJ'S":'BAR ROXY',o.k==='jj'?"JJ'S SPORTS LOUNGE":'LA CALA');ctx.restore();}return;
 case 'piripg':{for(let k=0;k<o.trail.length;k++){const q=o.trail[k],a=1-k/o.trail.length;ctx.fillStyle=`rgba(255,255,255,${(a*.55).toFixed(3)})`;ctx.beginPath();ctx.arc(q.x,q.y,4+k*.6,0,TAU);ctx.fill();}
  ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);ctx.drawImage(SP.piri.c,-30,-40,60,80);ctx.restore();
  if(!o.gift){const p=1+Math.sin(G.t*5)*.08,rg=ctx.createRadialGradient(o.rx,o.ry,4,o.rx,o.ry,30);rg.addColorStop(0,'rgba(255,201,60,.4)');rg.addColorStop(1,'rgba(255,201,60,0)');ctx.fillStyle=rg;ctx.beginPath();ctx.arc(o.rx,o.ry,30,0,TAU);ctx.fill();ctx.setLineDash([5,4]);ctx.lineDashOffset=-G.t*20;ctx.strokeStyle='#ffe28a';ctx.lineWidth=2.2;ctx.beginPath();ctx.arc(o.rx,o.ry,20*p,0,TAU);ctx.stroke();ctx.setLineDash([]);ctx.save();ctx.translate(o.rx,o.ry);ctx.rotate(G.camA||0);ctx.fillStyle='#ff4757';ctx.font='800 15px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('♥',0,1);ctx.restore();}
  ctx.save();ctx.translate(o.x,o.y);ctx.rotate(G.camA||0);label(0,-104,'PIRI-PIRI',o.gift?'¡GRACIAS!':'VIDA · TURBOS');ctx.restore();}return;
 case 'bgirl':""")
rep("case 'gearbox':{if(o.got)return;const p=1+Math.sin(G.t*4+o.ph)*.1,bob=Math.sin(G.t*2.5+o.ph)*3;ctx.save();ctx.translate(o.x,o.y+bob);",
    "case 'gearbox':{if(o.got)return;const p=1+Math.sin(G.t*4+o.ph)*.1,bob=Math.sin(G.t*2.5+o.ph)*3,GO=!!o.gold;ctx.save();ctx.translate(o.x,o.y+bob);if(GO)ctx.scale(1.45,1.45);")
rep("ctx.fillStyle='#f2b81e';ctx.fillRect(-13,-11,26,22);ctx.fillStyle='#ffd95a';ctx.fillRect(-13,-11,26,6);ctx.fillStyle='#e3202b';ctx.fillRect(-2.5,-11,5,22);ctx.fillRect(-13,-2.5,26,5);\n  ctx.strokeStyle='#e3202b';",
    "ctx.fillStyle=GO?'#c9961a':'#f2b81e';ctx.fillRect(-13,-11,26,22);ctx.fillStyle=GO?'#fff1a8':'#ffd95a';ctx.fillRect(-13,-11,26,6);ctx.fillStyle=GO?'#7a1fd1':'#e3202b';ctx.fillRect(-2.5,-11,5,22);ctx.fillRect(-13,-2.5,26,5);\n  ctx.strokeStyle=GO?'#7a1fd1':'#e3202b';")
# 6) casco dorado en EQUIPO (no se vende: solo escondido en el lago)
gold=base64.b64encode(open('dorado/dorado.webp','rb').read()).decode()
rep("{id:'h6',n:'Supertech Flúor',b:'Alpinestars',p:16000,c:'#ff6a1a',c2:'#ff3f8e',st:'mx',pat:'flame',paint:'fluor'}]",
    "{id:'h6',n:'Supertech Flúor',b:'Alpinestars',p:16000,c:'#ff6a1a',c2:'#ff3f8e',st:'mx',pat:'flame',paint:'fluor'},\n  {id:'h7',n:'Casco Dorado',b:'Exclusivo',p:0,c:'#e8b923',c2:'#fff1a8',st:'mx',pat:'twin',paint:'dorado',hid:1}]")
i=s.index("const HELM_IMG=");j=s.index("};",i);s=s[:j]+',"dorado":"data:image/webp;base64,'+gold+'"'+s[j:]
rep("inf.querySelector('.nm').textContent=(it.b==='De serie'||it.b==='Neopreno'?'':it.b+' ')+it.n;inf.querySelector('.ef').textContent=gearDesc(gearCat,it)+(tryOn&&!own?' · probándolo':'');",
    "inf.querySelector('.nm').textContent=(it.b==='De serie'||it.b==='Neopreno'||it.b==='Exclusivo'?'':it.b+' ')+it.n;inf.querySelector('.ef').textContent=(it.hid&&!own?'Escondido en el lago de Son Matías':gearDesc(gearCat,it))+(tryOn&&!own?' · probándolo':'');")
rep("else{b.innerHTML='<i class=\"coin\"></i>'+pts(it.p);b.disabled=G.money<it.p;}","else if(it.hid){b.textContent='ESCONDIDO';b.disabled=true;}else{b.innerHTML='<i class=\"coin\"></i>'+pts(it.p);b.disabled=G.money<it.p;}")
rep("b.addEventListener('click',e=>{e.stopPropagation();if(on)return;","b.addEventListener('click',e=>{e.stopPropagation();if(on||(it.hid&&!own))return;")
# 7) bar JJ en pequeño (solo el edificio, con pantalán y motos)
i=s.index("function drawJJTop");j=s.index(" const sx=spx,L=sx-114;",i);k=s.index("\nfunction ",j)
body=s[j:k].replace(" const sx=spx,L=sx-114;\n g.save();g.translate(L,py-178);"," g.save();g.translate(-114,-68);").replace("const MJ=!!Zn.Z.mirror;","const MJ=false;")
assert body.endswith(" g.restore();}"),body[-30:]
mini="""function drawJJMini(g){
 g.fillStyle='rgba(0,0,0,.18)';g.fillRect(-10,-4,92,14);g.fillStyle='#9a6a3c';g.fillRect(-14,-8,90,14);g.strokeStyle='#6e4826';g.lineWidth=1;for(let x=-10;x<76;x+=6){g.beginPath();g.moveTo(x,-8);g.lineTo(x,6);g.stroke();}
 [20,44,68].forEach((x,k)=>{const sp=SP.jet[MOTOS[k%MOTOS.length].id];if(!sp)return;g.save();g.translate(x,18);g.rotate(Math.PI/2);g.drawImage(sp.c,-9,-19,18,38);g.restore();});
"""+body+"\n"
s=s[:k+1]+mini+s[k+1:]
rep("const APP_VER=100;","const APP_VER=101;")
open(p,'w').write(s);print('ok',len(s))
