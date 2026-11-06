p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)

# zona 20: ES VEDRÀ
rep("{name:'LA FINAL',","{name:'ES VEDRÀ',obj:'race2',goal:'Termina entre los 2 primeros alrededor del islote de Es Vedrà, al atardecer en Ibiza. Esquiva los catamaranes de fiesta que cruzan.',len:16000,riv:5,bar:null,theme:'tram',tod:'sunset',skill:.95,island:1,isleTheme:'cove',catas:1,finish:'ES VEDRÀ'},\n {name:'LA FINAL',")
rep("let best=Math.max(0,Math.min(19,","let best=Math.max(0,Math.min(20,")
rep("const APP_VER=31;","const APP_VER=32;")
# más largas y más difíciles según avanzas
rep("const len=Math.round(Z.len*(1+lap*.08))","const lenK=(1.25+zi*.025)*(1+lap*.08),len=Math.round(Z.len*lenK)")
rep("const zone={Z,zi,lap,len,","const zone={Z,zi,lap,len,lenK,")
rep("G.time=Z.obj==='time'||Z.obj==='slalom'||Z.obj==='jumps'?Math.round(Zn.len/3/(Z.pace||200))+9+(Z.giant?6:0):0;",
    "G.time=Z.obj==='time'||Z.obj==='slalom'||Z.obj==='jumps'?Math.round(Zn.len/3/((Z.pace||200)*(1+zi*.008)))+9+(Z.giant?6:0):0;")
rep("const add=Math.round(Zn.len/3/(Zn.Z.pace||200))+3;","const add=Math.round(Zn.len/3/((Zn.Z.pace||200)*(1+Zn.zi*.008)))+3;")
rep("c.skill=(Z.skill||.9)*(mm===SHARK?1.08:1)*(1+G.lap*.04)*(.97+i*.012);","c.skill=(Z.skill||.9)*(mm===SHARK?1.08:1)*(1+G.lap*.04)*(1+zi*.005)*(.97+i*.012);")
rep("  u+=110+r()*120;","  u+=(110+r()*120)*(1-zi*.012);")
rep("if(G.fuel>0){G.fuel=Math.max(0,G.fuel-(ctlP.thr||ctlP.drift?1.25:ctlP.rev?.5:.12)*(P.boostT>0?2.2:1)*dt);",
    "if(G.fuel>0){G.fuel=Math.max(0,G.fuel-(ctlP.thr||ctlP.drift?1.25:ctlP.rev?.5:.12)*(P.boostT>0?2.2:1)*dt/(Zn.lenK||1));")
s=s.replace("'ct_ghost_'+","'ct_ghost2_'+")
# catamaranes de fiesta
rep("if(Z.supers){for(let su=1200;","if(Z.catas){for(let su=1300;su<len-700;su+=1000+r()*500){const dir=r()<.5?1:-1;M.push({t:'cata',x:dir>0?-100-r()*150:WG+100+r()*150,y:-su,vx:dir*(38+r()*18),vy:0,flash:r()*3});resv.push([su-70,su+70]);}}\n if(Z.supers){for(let su=1200;")
rep("for(const o of Zn.movers)if(o.t==='super'){","for(const o of Zn.movers)if(o.t==='super'||o.t==='cata'){")
rep("case 'super':return","case 'cata':return Math.abs(o.x-x)<46+rad*.5&&Math.abs(o.y-y)<22+rad;case 'super':return")
rep("crash(c,{super:'¡SUPERYATE!',","crash(c,{cata:'¡CATAMARÁN!',super:'¡SUPERYATE!',")
rep(" case 'super':{",""" case 'cata':{const d=o.vx>0?1:-1;ctx.save();ctx.translate(o.x,o.y);ctx.rotate(d>0?Math.PI/2:-Math.PI/2);
  ctx.fillStyle='rgba(0,20,50,.28)';ctx.beginPath();ctx.ellipse(5,7,26,50,0,0,TAU);ctx.fill();for(let i=0;i<10;i++){ctx.globalAlpha=.5;ctx.drawImage(SP.dot.c,(i%2?14:-14)+Math.sin(i+t*5)*3-4,48+i*6-4,8,8);}ctx.globalAlpha=1;
  ctx.fillStyle='#f4f6f9';for(const hx of[-15,15]){ctx.beginPath();ctx.ellipse(hx,0,6,48,0,0,TAU);ctx.fill();}ctx.fillStyle='rgba(30,40,60,.75)';ctx.fillRect(-15,-26,30,34);ctx.strokeStyle='rgba(255,255,255,.35)';ctx.lineWidth=1;for(let k=-24;k<8;k+=4){ctx.beginPath();ctx.moveTo(-15,k);ctx.lineTo(15,k);ctx.stroke();}
  ctx.fillStyle='#e9edf2';ctx.beginPath();ctx.roundRect(-16,8,32,26,5);ctx.fill();ctx.fillStyle='#c9a77a';ctx.fillRect(-14,30,28,8);
  const cols=['#ff3f8e','#ffd21a','#33d6ff','#7be35a','#ff7a1a'];for(let i=0;i<9;i++){const px=-11+(i%3)*11+Math.sin(t*6+i)*1.5,py=-22+((i/3)|0)*10;ctx.fillStyle=cols[i%5];ctx.beginPath();ctx.arc(px,py+2,2.6,0,TAU);ctx.fill();ctx.fillStyle='#e8b48c';ctx.beginPath();ctx.arc(px,py-1.5,1.8,0,TAU);ctx.fill();}
  ctx.strokeStyle='#9aa6b5';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(0,-30);ctx.lineTo(0,10);ctx.stroke();ctx.restore();
  ctx.save();ctx.fillStyle='#ffffff';ctx.font='800 13px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';for(let k=0;k<3;k++){const ph=(t*1.2+k/3)%1;ctx.globalAlpha=1-ph;ctx.fillText(k%2?'♫':'♪',o.x+(k-1)*18,o.y-30-ph*30);}ctx.restore();}return;
 case 'super':{""")
# portada
rep(" {tag:'GANA A EL TIBURÓN',"," {tag:'CARRERA · TOP 2',sky:['#3b2d78','#ff8a5c'],sea:['#3f7cba','#0f2c66'],sun:[300,84,'#ffd27a'],land:'vedra'},\n {tag:'GANA A EL TIBURÓN',")
rep(" if(L==='storm'){cvRidge(g,q,-20,420,HZ,40,8,'#111a30');",""" if(L==='vedra'){cvMount(g,q,-10,140,HZ+2,26,'#5a4a46','rgba(30,20,18,.45)');g.fillStyle='#4a3b3a';g.beginPath();g.moveTo(190,HZ+2);g.lineTo(218,HZ-50);g.lineTo(236,HZ-82);g.lineTo(252,HZ-58);g.lineTo(262,HZ-40);g.lineTo(292,HZ+2);g.closePath();g.fill();g.fillStyle='rgba(255,150,90,.28)';g.beginPath();g.moveTo(236,HZ-82);g.lineTo(252,HZ-58);g.lineTo(262,HZ-40);g.lineTo(292,HZ+2);g.lineTo(246,HZ+2);g.closePath();g.fill();g.fillStyle='#3f3230';g.beginPath();g.moveTo(170,HZ+2);g.lineTo(184,HZ-14);g.lineTo(198,HZ+2);g.closePath();g.fill();}
 if(L==='storm'){cvRidge(g,q,-20,420,HZ,40,8,'#111a30');""")
rep(" else if(L==='formentor'){",""" else if(L==='vedra'){g.save();g.translate(110,HZ+30);g.fillStyle='#f4f6f9';g.fillRect(-36,0,72,5);g.fillRect(-36,6,72,4);g.fillStyle='rgba(30,40,60,.8)';g.fillRect(-26,-10,40,10);const cl=['#ff3f8e','#ffd21a','#33d6ff','#7be35a'];for(let i=0;i<6;i++){g.fillStyle=cl[i%4];g.fillRect(-24+i*7,-16,4,7);g.fillStyle='#e8b48c';g.beginPath();g.arc(-22+i*7,-18,2,0,TAU);g.fill();}g.fillStyle='#ffffff';g.font='800 12px "Saira Condensed",sans-serif';g.fillText('♪',8,-26);g.fillText('♫',22,-34);g.restore();cvRival(g,q,rv(0),190,150,.26,-.06);hero(290,172,.42,-.15,0);}
 else if(L==='formentor'){""")
open(p,'w').write(s);print('ok')
