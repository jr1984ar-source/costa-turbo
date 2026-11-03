import json
p='costa-turbo.html';s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
# ---------- mapa: puerto de Portals (espigón 8, pantalanes 9, amarres 10) y gasolineras ----------
RM=json.load(open('/tmp/claude-0/-home-user/e02bf71e-076d-586d-89ee-84e1312586e6/scratchpad/costa_real/realmap5.json'))
i0=s.index("const RMAP={");i1=s.index("let RMD=null;",i0)
s=s[:i0]+"const RMAP={w:%d,h:%d,c:3,src:'%s'};const RCOR=%s;const RSPOTS=%s;"%(RM['w'],RM['h'],RM['src'],json.dumps(RM['cor'],separators=(',',':')),json.dumps(RM['spots'],separators=(',',':')))+s[i1:]
rep("a[i]=Math.round(d[i*4]/36);","a[i]=Math.round(d[i*4]/25);")
rep("const rmLand=(x,y)=>{const v=rmV(x,y);return (v>0&&v<5)||v===7;};",
    "const rmLand=(x,y)=>{const v=rmV(x,y);return (v>0&&v<5)||v>=7;};\nconst rmB=(x,y)=>{const v=rmV(x,y);return (v>0&&v<5)||v===7;};")
rep("const rmIn=(x,y,d)=>rmLand(x,y)&&rmLand(x-d,y)&&rmLand(x+d,y)&&rmLand(x,y-d)&&rmLand(x,y+d)&&rmV(x,y)!==2;",
    "const rmIn=(x,y,d)=>rmB(x,y)&&rmB(x-d,y)&&rmB(x+d,y)&&rmB(x,y-d)&&rmB(x,y+d)&&rmV(x,y)!==2;")
rep("const landM=mask(v=>(v>0&&v<5)||v===7),outM=mask(v=>v===6);","const landM=mask(v=>(v>0&&v<5)||v===7||v===8||v===9),outM=mask(v=>v===6);")
rep("layer(mask(v=>v===2),'#f1d9a6');}","layer(mask(v=>v===2),'#f1d9a6');layer(mask(v=>v===8),'#cbc5b9');layer(mask(v=>v===9),'#c9a77a');}")
rep("if(!rmLand(x,y)||rmV(x,y)===2)continue;g.fillStyle=k%2?","if(!rmB(x,y)||rmV(x,y)===2)continue;g.fillStyle=k%2?")
rep("!rmLand(lx+2,ly+2)||!rmLand(lx+lw-2,ly+2)||!rmLand(lx+2,ly+lh-2)||!rmLand(lx+lw-2,ly+lh-2)","!rmB(lx+2,ly+2)||!rmB(lx+lw-2,ly+2)||!rmB(lx+2,ly+lh-2)||!rmB(lx+lw-2,ly+lh-2)")
rep(" for(let y=Math.ceil(y0/34)*34;y<y1;y+=34){const xb=rmCor(y);",""" // puerto: escollera en el espigón, tablones en los pantalanes y barcos amarrados
 {const edge=(x,y,v,d)=>rmV(x-d,y)!==v||rmV(x+d,y)!==v||rmV(x,y-d)!==v||rmV(x,y+d)!==v;
  for(let k=0;k<900;k++){const x=x0+q()*CW,y=y0+q()*CH;if(rmV(x,y)!==8||!edge(x,y,8,8))continue;g.fillStyle=['#9b968d','#b7b2a8','#85807a','#aaa59b'][k%4];g.beginPath();g.ellipse(x,y,3+q()*3.5,2.2+q()*2.5,q()*3,0,TAU);g.fill();}
  g.strokeStyle='rgba(90,60,30,.35)';g.lineWidth=.8;for(let x=Math.floor(x0/5)*5;x<x1;x+=5)for(let y=Math.floor(y0/3)*3;y<y1;y+=3)if(rmV(x,y)===9&&rmV(x,y+3)===9){g.beginPath();g.moveTo(x,y);g.lineTo(x,y+3);g.stroke();}
  for(let y=Math.floor(y0/36)*36;y<y1;y+=36)for(let x=Math.floor(x0/36)*36;x<x1;x+=36)if(rmV(x,y)===8&&!edge(x,y,8,7)){g.fillStyle='#4f4c47';g.beginPath();g.arc(x,y,2.2,0,TAU);g.fill();g.fillStyle='rgba(255,240,180,.8)';g.beginPath();g.arc(x,y,1,0,TAU);g.fill();}
  const S=15;for(let y=Math.floor((y0-60)/S)*S;y<y1+60;y+=S)for(let x=Math.floor((x0-60)/S)*S;x<x1+60;x+=S){if(rmV(x,y)!==10)continue;let b=null;
   for(const a of [0,2,4,6,1,3,5,7]){const ca=Math.cos(a*Math.PI/4),sa=Math.sin(a*Math.PI/4);for(let d=1.5;d<16.6;d+=1.5){const v=rmV(x+ca*d,y+sa*d);if(v===8||v===9){if(!b||d<b.d)b={d,ca,sa};break;}if(v!==10)break;}}
   if(!b||(b.d>3&&rmV(x+b.ca*S,y+b.sa*S)===10))continue;const h=hash2(Math.round(x),Math.round(y),71),h2=hash2(Math.round(y),Math.round(x),13),L=36+h*14,Wd=11+h2*4,sail=h2>.78;
   g.save();g.translate(x+b.ca*(b.d-1),y+b.sa*(b.d-1));g.rotate(Math.atan2(-b.sa,-b.ca));
   const hull=(o)=>{g.beginPath();g.moveTo(o,-Wd/2);g.lineTo(L*.62,-Wd/2);g.quadraticCurveTo(L,-Wd*.32,L,0);g.quadraticCurveTo(L,Wd*.32,L*.62,Wd/2);g.lineTo(o,Wd/2);g.closePath();};
   g.save();g.translate(2,3);g.fillStyle='rgba(0,30,60,.25)';hull(0);g.fill();g.restore();
   g.fillStyle='#f7f8fa';hull(0);g.fill();g.strokeStyle='#bcc6d1';g.lineWidth=.9;g.stroke();
   g.fillStyle=h<.4?'#d8c29a':'#e8ecf0';g.save();g.scale(.86,.78);hull(3);g.fill();g.restore();
   if(sail){g.strokeStyle='#8f969e';g.lineWidth=1.2;g.beginPath();g.moveTo(L*.2,0);g.lineTo(L*.62,0);g.stroke();g.fillStyle='#3b4250';g.beginPath();g.arc(L*.62,0,1.8,0,TAU);g.fill();g.fillStyle=['#1f4fa8','#c03a2b','#2f8f6f'][(h*3)|0];g.fillRect(L*.24,-1.6,L*.34,3.2);}
   else{const cc=['#1d3557','#2a9d8f','#e9e4d6','#264653','#8d99ae'][(h2*5)|0];g.fillStyle=cc;g.beginPath();g.roundRect(L*.22,-Wd*.3,L*.36,Wd*.6,3);g.fill();g.fillStyle='rgba(20,30,45,.75)';g.fillRect(L*.5,-Wd*.24,L*.06,Wd*.48);}
   g.restore();}}
 for(let y=Math.ceil(y0/34)*34;y<y1;y+=34){const xb=rmCor(y);""")
rep("land=(v>0&&v<5)||v===7;id.data[k]=land?(v===2?240:206):18;id.data[k+1]=land?(v===2?220:190):92;id.data[k+2]=land?(v===2?170:140):160;",
    "land=(v>0&&v<5)||v===7||v===8||v===9;id.data[k]=land?(v===2?240:v>=8?222:206):18;id.data[k+1]=land?(v===2?220:v>=8?218:190):92;id.data[k+2]=land?(v===2?170:v>=8?212:140):160;")
# ---------- gasolina en el lago: se gasta 3 veces más despacio ----------
rep("function updatePG(dt){const Zn=G.zone,P=G.P;G.fuel=100;","function updatePG(dt){const Zn=G.zone,P=G.P;")
rep("dt/(Zn.lenK||1));if(G.fuel<=0)msg('¡SIN GASOLINA!','Busca un bar para llenar','var(--red)');",
    "dt/(Zn.lenK||1)/(Zn.Z.playground?3:1));if(G.fuel<=0)msg('¡SIN GASOLINA!',Zn.Z.playground?'Busca una garrafa o una gasolinera':'Busca un bar para llenar','var(--red)');")
# garrafas sueltas, gasolineras y paradas de los bares
rep(" if(S.jj)O.push({t:'pgbar',k:'jj',x:S.jj[0],y:S.jj[1],rot:0,ry:220});}",
""" if(S.jj)O.push({t:'pgbar',k:'jj',x:S.jj[0],y:S.jj[1],rot:0,ry:220});
 for(const o of O)if(o.t==='pgbar'){const ca=Math.cos(o.rot),sa=Math.sin(o.rot),lx=o.k==='jj'?125:100,ly=o.k==='jj'?80:0;o.bx=o.x+lx*ca-ly*sa;o.by=o.y+lx*sa+ly*ca;}
 for(const g of S.gas||[])O.push({t:'pggas',x:g[0],y:g[1],ex:g[2],ey:g[3],ry:160});}""")
rep(" pgHidden(O);"," pgHidden(O);\n // garrafas de gasolina sueltas\n for(let n=0,t=0;n<14&&t<3000;t++){const x=rx(),y=ry();if(inLane(x,y,80)||!free(x,y,70))continue;if(O.some(o=>o.t==='fuel'&&Math.hypot(o.x-x,o.y-y)<1200))continue;O.push({t:'fuel',x,y});n++;}")
rep("zone.big=zone.objs.filter(o=>o.t==='island'||o.t==='pass'||o.t==='nozone'||o.t==='pgbar');","zone.big=zone.objs.filter(o=>o.t==='island'||o.t==='pass'||o.t==='nozone'||o.t==='pgbar'||o.t==='pggas');")
rep("if(o.t!=='island'&&o.t!=='pass'&&o.t!=='nozone'&&o.t!=='pgbar')drawObj(o);","if(o.t!=='island'&&o.t!=='pass'&&o.t!=='nozone'&&o.t!=='pgbar'&&o.t!=='pggas')drawObj(o);")
rep("if(o.t==='bgirl'||o.t==='bpalm'||o.t==='faro'||o.t==='pgbar')continue;","if(o.t==='bgirl'||o.t==='bpalm'||o.t==='faro'||o.t==='pgbar'||o.t==='pggas')continue;")
# paradas: bares, gasolineras y Piri-Piri fondeado (se frena con ATRÁS dentro del círculo)
rep(" if(P.x<12)P.x=12;if(P.x>RMW-12)P.x=RMW-12;",""" if(P.x<12)P.x=12;if(P.x>RMW-12)P.x=RMW-12;
 if(!G.demo)for(const o of Zn.big){if(o.t!=='pgbar'&&o.t!=='pggas')continue;const cx=o.t==='pgbar'?o.bx:o.x,cy=o.t==='pgbar'?o.by:o.y,d=Math.hypot(P.x-cx,P.y-cy);
  if(o.cool){if(d>RING_R+40)o.cool=0;continue;}
  if(d<RING_R&&P.v<P.st.maxV*.55){o.cool=1;
   if(o.t==='pgbar'){Zn.bar=o.k;Zn.ring={x:cx,y:cy};openBar();return;}
   if(G.fuel>=99)msg('DEPÓSITO LLENO','Ya tienes la gasolina al 100 %','var(--lime)');else if(G.money<300)msg('TE FALTAN PESETAS','Llenar el depósito cuesta 300','var(--red)');
   else{G.money-=300;saveWallet();G.fuel=100;Snd.cash();buzz(40);msg('¡DEPÓSITO LLENO!','−300 PESETAS','var(--lime)');}continue;}
  if(d<230&&!o.hint){o.hint=1;msg(o.t==='pggas'?'GASOLINERA':o.k==='jj'?"BAR JJ'S":'BAR ROXY','Frena con ATRÁS dentro del círculo','var(--gold)');}}""")
# el Piri-Piri navega un rato y fondea otro rato; fondeado, frenas a su lado y te da vida y turbos
rep("""else if(o.t==='piripg'){const n=o.path.length,tg=o.path[(o.i+1)%n],dx=tg[0]-o.x,dy=tg[1]-o.y,d=Math.hypot(dx,dy),sp=72*dt;
   if(d<sp+3)o.i=(o.i+1)%n;else{o.x+=dx/d*sp;o.y+=dy/d*sp;""","""else if(o.t==='piripg'){const n=o.path.length,tg=o.path[(o.i+1)%n],dx=tg[0]-o.x,dy=tg[1]-o.y,d=Math.hypot(dx,dy),sp=o.anch>0?0:72*dt;
   if(o.anch>0){o.anch-=dt;if(o.anch<=0){o.sail=40;}}else{o.sail=(o.sail==null?18:o.sail)-dt;if(o.sail<=0){o.anch=28;o.gift=0;const sd=rmLand(o.x+Math.cos(o.h)*60,o.y+Math.sin(o.h)*60)?-1:1;o.side=sd;}}
   if(sp>0){if(d<sp+3)o.i=(o.i+1)%n;else{o.x+=dx/d*sp;o.y+=dy/d*sp;""")
rep("""o.h+=dh*Math.min(1,1.8*dt);}
   o.rx=o.x+Math.cos(o.h)*50;o.ry=o.y+Math.sin(o.h)*50;o.tacc=(o.tacc||0)+sp;""","""o.h+=dh*Math.min(1,1.8*dt);}}
   const sd=o.side||1;o.rx=o.x+Math.cos(o.h)*62*sd;o.ry=o.y+Math.sin(o.h)*62*sd;o.tacc=(o.tacc||0)+sp;""")
rep("""   if(o.gift){o.gt-=dt;if(o.gt<=0)o.gift=0;}
   if(!G.demo){""","""   if(!G.demo){""")
rep("""    if(!o.gift&&Math.hypot(P.x-o.rx,P.y-o.ry)<40){o.gift=1;o.gt=45;setHp(hpTot()+3);""","""    const dr=Math.hypot(P.x-o.rx,P.y-o.ry);if(o.anch>0&&!o.gift&&dr<260&&!o.hint){o.hint=1;msg('PIRI-PIRI','Frena a su lado: vida y turbos','var(--gold)');}if(o.anch<=0)o.hint=0;
    if(o.anch>0&&!o.gift&&dr<46&&P.v<P.st.maxV*.55){o.gift=1;setHp(hpTot()+3);""")
rep("""  if(!o.gift){const p=1+Math.sin(G.t*5)*.08,rg=ctx.createRadialGradient(o.rx,o.ry,4,o.rx,o.ry,30);""","""  if(o.anch>0&&!o.gift){const p=1+Math.sin(G.t*5)*.08,rg=ctx.createRadialGradient(o.rx,o.ry,4,o.rx,o.ry,30);""")
rep("ctx.arc(o.rx,o.ry,30,0,TAU);ctx.fill();ctx.setLineDash([5,4]);ctx.lineDashOffset=-G.t*20;ctx.strokeStyle='#ffe28a';ctx.lineWidth=2.2;ctx.beginPath();ctx.arc(o.rx,o.ry,20*p,0,TAU);",
    "ctx.arc(o.rx,o.ry,48,0,TAU);ctx.fill();ctx.setLineDash([6,5]);ctx.lineDashOffset=-G.t*20;ctx.strokeStyle='#ffe28a';ctx.lineWidth=2.6;ctx.beginPath();ctx.arc(o.rx,o.ry,40*p,0,TAU);")
rep("label(0,-104,'PIRI-PIRI',o.gift?'¡GRACIAS!':'VIDA · TURBOS')","label(0,-104,'PIRI-PIRI',o.anch>0?(o.gift?'¡GRACIAS!':'FONDEADO · VIDA · TURBOS'):'NAVEGANDO')")
# dibujo: círculos de parada de los bares y gasolineras
RINGF="""const pgRing=(x,y,txt)=>{const p=1+Math.sin(G.t*5)*.08,R2=RING_R,rg=ctx.createRadialGradient(x,y,8,x,y,R2*1.15);rg.addColorStop(0,'rgba(255,201,60,.32)');rg.addColorStop(1,'rgba(255,201,60,0)');ctx.fillStyle=rg;ctx.beginPath();ctx.arc(x,y,R2*1.15,0,TAU);ctx.fill();ctx.setLineDash([9,7]);ctx.lineDashOffset=-G.t*24;ctx.strokeStyle='#ffe28a';ctx.lineWidth=3.2;ctx.beginPath();ctx.arc(x,y,R2*.78*p,0,TAU);ctx.stroke();ctx.setLineDash([]);ctx.save();ctx.translate(x,y);ctx.rotate(G.camA||0);ctx.fillStyle='#ffe28a';ctx.font='800 '+(txt.length>4?17:26)+'px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(txt,0,1);ctx.restore();};
"""
rep("function label(x,y,t,s){",RINGF+"function label(x,y,t,s){")
rep("""ctx.rotate(G.camA||0);label(0,0,o.k==='jj'?"BAR JJ'S":'BAR ROXY',o.k==='jj'?"JJ'S SPORTS LOUNGE":'LA CALA');ctx.restore();}return;""",
    """ctx.rotate(G.camA||0);label(0,0,o.k==='jj'?"BAR JJ'S":'BAR ROXY',o.k==='jj'?'VIDAS · GASOLINA':'PIEZAS · GASOLINA');ctx.restore();pgRing(o.bx,o.by,'BAR');}return;
 case 'pggas':{const dx=o.x-o.ex,dy=o.y-o.ey,a=Math.atan2(dy,dx);ctx.save();ctx.translate(o.ex,o.ey);ctx.rotate(a);
  ctx.fillStyle='rgba(0,30,60,.22)';ctx.fillRect(2,-13,46,30);ctx.fillStyle='#c9a77a';ctx.fillRect(-2,-15,46,30);ctx.strokeStyle='rgba(90,60,30,.4)';ctx.lineWidth=.8;for(let x=2;x<44;x+=5){ctx.beginPath();ctx.moveTo(x,-15);ctx.lineTo(x,15);ctx.stroke();}
  for(const yy of[-8,8]){ctx.fillStyle='#2b2f38';ctx.fillRect(14,yy-4,10,8);ctx.fillStyle='#e3202b';ctx.fillRect(15,yy-3,8,4);ctx.fillStyle='#ffd21a';ctx.fillRect(15,yy+1,8,2);}
  ctx.fillStyle='#ffffff';ctx.fillRect(30,-6,10,12);ctx.fillStyle='#2b9a3e';ctx.fillRect(31,-5,8,10);ctx.restore();
  ctx.save();ctx.translate(o.ex+Math.cos(a)*20,o.ey+Math.sin(a)*20-0);ctx.rotate(G.camA||0);label(0,-46,'GASOLINERA','LLENAR · 300 PESETAS');ctx.restore();pgRing(o.x,o.y,'GASOLINA');}return;""")
# minimapa: gasolineras
rep("for(const o of G.zone.big||[]){if(o.t!=='pgbar')continue;const x=tx(o.x),y=ty(o.y);if(x<-6||x>MW+6||y<-6||y>MH+6)continue;g.fillStyle=o.k==='jj'?'#e3202b':'#a0632f';",
    "for(const o of G.zone.big||[]){if(o.t!=='pgbar'&&o.t!=='pggas')continue;const x=tx(o.x),y=ty(o.y);if(x<-6||x>MW+6||y<-6||y>MH+6)continue;g.fillStyle=o.t==='pggas'?'#2bbf4a':o.k==='jj'?'#e3202b':'#a0632f';")
rep("const APP_VER=103;","const APP_VER=104;")
open(p,'w').write(s);print('ok',len(s))
