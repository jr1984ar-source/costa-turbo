import shutil,json,re
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v99.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
RM = json.load(open('realmap3.json'))
h = rep(h, "const APP_VER=98", "const APP_VER=99")
# ---- mapa grande (sin pasillo) ----
i0 = h.index("const RMAP={"); i1 = h.index("let RMD=null;", i0)
h = h[:i0] + "const RMAP={w:%d,h:%d,c:3,src:'%s'};const RCOR=%s;" % (RM['w'], RM['h'], RM['src'], json.dumps(RM['cor'], separators=(',', ':'))) + h[i1:]
# ---- la pantalla pasa a ser modo libre ----
h = rep(h, "{name:'SON MATÍAS – ILLETES',realMap:1,water:['#22b3d6','#0b6fb3'],obj:'race3',goal:'Termina entre los 3 primeros por la costa real: del JJ’S de Son Matías, por Punta Negra, Puerto Portals y Portals Nous, hasta la playa de Illetes.',len:10000,riv:5,",
 "{name:'SON MATÍAS · MODO LIBRE',realMap:1,playground:1,water:['#22b3d6','#0b6fb3'],obj:'free',goal:'Modo libre: navega por donde quieras. Rampas, olas, lanchas con esquí acuático, motos de otra gente y una recta larguísima para ir a fondo. Para salir, pulsa pausa.',len:10000,riv:0,")
h = rep(h, "{tag:'COSTA REAL · TOP 3'", "{tag:'MODO LIBRE'")
h = rep(h, "zone.rwall=Z.realMap?(y=>rmCor(y)):null;", "zone.rwall=Z.realMap&&!Z.playground?(y=>rmCor(y)):null;")
h = rep(h, " zone.objs=O.filter(o=>o.t==='check'||o.t==='finish'||", " if(Z.playground)pgBuild(zone,O,M,r);\n zone.objs=O.filter(o=>o.t==='check'||o.t==='finish'||")
# ---- generador del parque ----
h = rep(h, "const RTW=400,RSX=150,RSY=124;", r"""function pgBuild(zone,O,M,r){for(let k=O.length-1;k>=0;k--)if(O[k].t==='finish'||O[k].t==='check')O.splice(k,1);zone.finishY=-1e9;
 const top=RM_TOP+500,bot=RM_BOT-300,free=(x,y,m)=>x>m&&x<RMW-m&&!rmLand(x,y)&&!rmLand(x-m,y)&&!rmLand(x+m,y)&&!rmLand(x,y-m)&&!rmLand(x,y+m);
 const rightLand=y=>{for(let x=RMW-3;x>0;x-=9)if(rmLand(x,y))return x;return 0;};
 // recta larguísima mar adentro
 const y0=-900,y1=-10900;let mx=0;for(let y=y0;y>=y1;y-=120)mx=Math.max(mx,rightLand(y));const lx=Math.min(RMW-400,mx+650),lw=180;zone.lane={x:lx,w:lw,y0,y1,mid:(y0+y1)/2};
 for(let y=y0;y>=y1;y-=110){O.push({t:'lbuoy',x:lx-lw/2,y,c:'#ff7a1a'});O.push({t:'lbuoy',x:lx+lw/2,y,c:'#ffd21a'});}
 O.push({t:'lgate',x:lx,y:y0,w:lw,txt:'RECTA · ¡A FONDO!'});O.push({t:'lgate',x:lx,y:zone.lane.mid,w:lw,txt:'RADAR'});O.push({t:'lgate',x:lx,y:y1,w:lw,txt:'FIN DE LA RECTA'});
 const inLane=(x,y,m)=>Math.abs(x-lx)<lw/2+m&&y<y0+m&&y>y1-m;
 const rx=()=>150+r()*(RMW-300),ry=()=>top+r()*(bot-top);
 // olas en todas direcciones
 for(let n=0,t=0;n<90&&t<4000;t++){const x=rx(),y=ry();if(inLane(x,y,220)||!free(x,y,150))continue;O.push({t:'fwave',x,y,a:r()*Math.PI,L:150+r()*170,ph:r()*6});n++;}
 // rampas sueltas
 const SZ={s:{w:80,Lr:36,col:'#ffd21a'},m:{w:100,Lr:52,col:'#ff7a1a'},l:{w:124,Lr:72,col:'#e3202b'}};
 for(let n=0,t=0;n<55&&t<4000;t++){const x=rx(),y=ry(),sz=['s','m','l'][(r()*3)|0];if(inLane(x,y,120)||!free(x,y,90))continue;const o={t:'ramp',x,y,w:SZ[sz].w,Lr:SZ[sz].Lr,col:SZ[sz].col,sz,kick:1};if(rmFoot(o))continue;O.push(o);for(let i=0;i<4;i++)O.push({t:'coin',x,y:y-RAMP_D[sz]*(.2+.6*i/3),air:1});n++;}
 // monedas
 for(let n=0,t=0;n<45&&t<3000;t++){const x=rx(),y=ry();if(!free(x,y,60))continue;const sh=r();for(let i=0;i<7;i++)O.push({t:'coin',x:x+(sh<.5?Math.sin(i*.8)*30:0),y:y-i*28});n++;}
 // lanchas tirando de esquiadores
 for(let n=0,t=0;n<7&&t<600;t++){const cx=rx(),cy=ry(),A=350+r()*700,B=250+r()*500;let ok=true;for(let k=0;k<24&&ok;k++){const a=k/24*TAU;if(!free(cx+Math.cos(a)*A,cy+Math.sin(a)*B,90)||inLane(cx+Math.cos(a)*A,cy+Math.sin(a)*B,40))ok=false;}if(!ok)continue;
  const sp=150+r()*50,dir=r()<.5?1:-1,ang=r()*TAU;M.push({t:'skiboat',cx,cy,A,B,ang,w:dir*sp/((A+B)/2),x:cx+Math.cos(ang)*A,y:cy+Math.sin(ang)*B,h:0,trail:[],ph:r()*6,vx:0,vy:0,flash:0,sk:['#ff3f8e','#ffd21a','#33d6ff','#7be35a'][n%4]});n++;}
 // motos de agua de otra gente
 const ids=MOTOS.map(m=>m.id);for(let n=0,t=0;n<14&&t<800;t++){const x=rx(),y=ry();if(!free(x,y,100))continue;M.push({t:'npcjet',x,y,h:r()*TAU,th:null,v:120+r()*110,id:ids[(r()*ids.length)|0],tt:r()*3,trail:[],vx:0,vy:0,flash:0});n++;}}
function updatePG(dt){const Zn=G.zone,P=G.P;G.fuel=100;
 if(P.x<12)P.x=12;if(P.x>RMW-12)P.x=RMW-12;if(P.y<RM_TOP+300)P.y=RM_TOP+300;if(P.y>RM_BOT-10)P.y=RM_BOT-10;
 for(const o of Zn.movers){
  if(o.t==='skiboat'){o.ang+=o.w*dt;const nx=o.cx+Math.cos(o.ang)*o.A,ny=o.cy+Math.sin(o.ang)*o.B,dx=nx-o.x,dy=ny-o.y;if(dx||dy)o.h=Math.atan2(dx,-dy);o.x=nx;o.y=ny;
   o.tacc=(o.tacc||0)+Math.hypot(dx,dy);if(o.tacc>14){o.tacc=0;o.trail.unshift({x:o.x-Math.sin(o.h)*26,y:o.y+Math.cos(o.h)*26,h:o.h});if(o.trail.length>34)o.trail.pop();}
   const b=o.trail[Math.min(o.trail.length-1,6)];if(b){const sw=Math.sin(G.t*1.1+o.ph)*18;o.skx=b.x+Math.cos(b.h)*sw;o.sky=b.y+Math.sin(b.h)*sw;o.skh=b.h;}}
  else if(o.t==='npcjet'){o.tt-=dt;if(o.tt<=0){o.tt=1.5+Math.random()*3;o.th=o.h+(Math.random()-.5)*1.8;}const ax=o.x+Math.sin(o.h)*130,ay=o.y-Math.cos(o.h)*130;if(rmLand(ax,ay)||ax<80||ax>RMW-80||ay<RM_TOP+500||ay>RM_BOT-150)o.th=o.h+2;
   let d=(o.th==null?o.h:o.th)-o.h;while(d>Math.PI)d-=TAU;while(d<-Math.PI)d+=TAU;o.h+=clamp(d,-1.7*dt,1.7*dt);o.x+=Math.sin(o.h)*o.v*dt;o.y-=Math.cos(o.h)*o.v*dt;
   o.tacc=(o.tacc||0)+o.v*dt;if(o.tacc>10){o.tacc=0;o.trail.unshift({x:o.x-Math.sin(o.h)*24,y:o.y+Math.cos(o.h)*24,h:o.h});if(o.trail.length>16)o.trail.pop();}}}
 const L=Zn.lane;if(L&&P.prevY>L.mid&&P.y<=L.mid&&Math.abs(P.x-L.x)<L.w/2+20){const k=Math.round(Math.abs(P.v)*.31),best=store.get('ct_pg_vmax',0)|0;if(k>best)store.set('ct_pg_vmax',k);msg('RADAR: '+k+' KM/H',k>best?'¡NUEVO RÉCORD!':'Récord: '+best+' km/h','#ffe14d');}
 if(P.air>0||P.crash>0||P.inv>0&&false)return;P._wk=(P._wk||0)-dt;const spd=P.v;
 for(const o of Zn.movers)if(o.t==='skiboat'&&o.skx!=null&&P.crash<=0&&P.inv<=0&&Math.hypot(P.x-o.skx,P.y-o.sky)<13){crash(P,'¡ESQUIADOR!');return;}
 const O=Zn.objs;for(let i=findStart(O,P.y-260);i<O.length&&O[i].y<P.y+260;i++){const o=O[i];if(o.t!=='fwave')continue;const ca=Math.cos(o.a),sa=Math.sin(o.a),qx=P.x-o.x,qy=P.y-o.y,al=qx*ca+qy*sa,ac=-qx*sa+qy*ca,side=ac>0?1:-1;
  if(Math.abs(al)<o.L/2&&o._s!=null&&side!==o._s&&Math.abs(ac)<30&&spd>120&&P._wk<=0){const k=.55+.6*clamp((spd-120)/240,0,1);startJump(P);P.airT*=k;P.air=P.airT;P._wk=.45;const b=60+Math.round(spd/5);G.score+=b;pop(P.x,P.y-40,'¡OLA! +'+b,'#33d6ff');}
  o._s=Math.abs(al)<o.L/2+40?side:null;}
 if(P._wk<=0&&spd>140)for(const o of Zn.movers){if(o.t!=='skiboat'&&o.t!=='npcjet')continue;if(Math.abs(o.y-P.y)>520||Math.abs(o.x-P.x)>520)continue;const T=o.trail,f=o.t==='skiboat'?3.4:1.8;
  for(let k=3;k<T.length;k++){const p=T[k],off=k*f,px=Math.cos(p.h),py=Math.sin(p.h);for(const sg of[-1,1]){if(Math.hypot(P.x-(p.x+px*off*sg),P.y-(p.y+py*off*sg))<12){startJump(P);P.airT*=o.t==='skiboat'?.7:.5;P.air=P.airT;P._wk=.6;pop(P.x,P.y-40,'¡ESTELA!','#9fe8ff');G.score+=40;return;}}}}}
function drawPGMap(){const cvm=$('#cmap'),D=DPR||1,MW=124,MH=150,S=MW/2600;if(cvm._pg!==1){cvm.style.width=MW+'px';cvm.style.height=MH+'px';cvm.width=MW*D;cvm.height=MH*D;cvm._pg=1;}
 const P=G.P,R=G._pgm||(G._pgm={});if(!R.img||Math.hypot(P.x-R.cx,P.y-R.cy)>90){R.cx=P.x;R.cy=P.y;const w=Math.ceil(MW*1.4),hh=Math.ceil(MH*1.4),c=document.createElement('canvas');c.width=w;c.height=hh;const g=c.getContext('2d'),id=g.createImageData(w,hh);
  for(let y=0;y<hh;y++)for(let x=0;x<w;x++){const wx=R.cx+(x-w/2)/S,wy=R.cy+(y-hh/2)/S,v=rmV(wx,wy),k=(y*w+x)*4,land=v>0&&v<5;id.data[k]=land?(v===2?240:206):18;id.data[k+1]=land?(v===2?220:190):92;id.data[k+2]=land?(v===2?170:140):160;id.data[k+3]=wx<0||wx>RMW?120:235;}
  g.putImageData(id,0,0);R.img=c;}
 const g=cvm.getContext('2d');g.setTransform(1,0,0,1,0,0);g.clearRect(0,0,cvm.width,cvm.height);g.setTransform(D,0,0,D,0,0);
 g.save();g.beginPath();g.roundRect(0,0,MW,MH,12);g.clip();const ox=MW/2+(R.cx-P.x)*S-R.img.width/2,oy=MH*.62+(R.cy-P.y)*S-R.img.height/2;g.drawImage(R.img,ox,oy);
 const tx=x=>MW/2+(x-P.x)*S,ty=y=>MH*.62+(y-P.y)*S,L=G.zone.lane;if(L){g.strokeStyle='rgba(255,170,40,.9)';g.lineWidth=2;g.beginPath();g.moveTo(tx(L.x),ty(L.y0));g.lineTo(tx(L.x),ty(L.y1));g.stroke();}
 for(const o of G.zone.movers){const x=tx(o.x),y=ty(o.y);if(x<-4||x>MW+4||y<-4||y>MH+4)continue;g.fillStyle=o.t==='skiboat'?'#ffffff':'#ff4f8b';g.beginPath();g.arc(x,y,o.t==='skiboat'?2.6:2,0,TAU);g.fill();}
 g.translate(MW/2,MH*.62);g.rotate(P.h);g.fillStyle=playerSk().hull;g.strokeStyle='#fff';g.lineWidth=1.5;g.beginPath();g.moveTo(0,-7);g.lineTo(5,5);g.lineTo(-5,5);g.closePath();g.fill();g.stroke();g.restore();
 g.strokeStyle='rgba(255,255,255,.6)';g.lineWidth=1.5;g.beginPath();g.roundRect(.75,.75,MW-1.5,MH-1.5,12);g.stroke();g.fillStyle='rgba(255,255,255,.85)';g.font='800 10px "Saira Condensed",sans-serif';g.textAlign='center';g.fillText('N',MW/2,11);}
const RTW=400,RSX=150,RSY=124;""")
# ---- actualización, choques y daño ----
h = rep(h, "// movers\n for(const o of Zn.movers){", "if(Zn.Z.playground)updatePG(dt);\n // movers\n for(const o of Zn.movers){")
h = rep(h, "case 'turtle':return Math.hypot(o.x-x,o.y-y)<11+rad;", "case 'turtle':return Math.hypot(o.x-x,o.y-y)<11+rad;case 'skiboat':return Math.hypot(o.x-x,o.y-y)<18+rad;case 'npcjet':return Math.hypot(o.x-x,o.y-y)<12+rad;")
h = rep(h, "crash(c,{cata:'¡CATAMARÁN!',", "crash(c,{skiboat:'¡LANCHA!',npcjet:'¡CHOQUE!',cata:'¡CATAMARÁN!',")
h = rep(h, "if(c.isP)hurt(c,1e9);", "if(c.isP&&!Zn.Z.playground)hurt(c,1e9);")
h = rep(h, "if(c.isP)hurt(c,v0);", "if(c.isP&&!Zn.Z.playground)hurt(c,v0);")
# ---- HUD y minimapa ----
h = rep(h, "{const isC=!!G.zone.circ;$('#track').hidden=isC;$('#cmap').hidden=!isC;G._mm=null;if(isC)buildMiniMap();}",
 "{const isC=!!G.zone.circ,isPG=!!G.zone.Z.playground;$('#track').hidden=isC||isPG;$('#cmap').hidden=!(isC||isPG);G._mm=null;G._pgm=null;$('#cmap')._pg=0;if(isC)buildMiniMap();}")
h = rep(h, "if(Zn.circ)drawMiniMap();", "if(Zn.circ)drawMiniMap();else if(Z.playground)drawPGMap();")
h = rep(h, " // left panel\n if(Z.riv){", " // left panel\n if(Z.playground){setTxt('hlL','SALTOS');setTxt('hvL',String(G.jumps));}\n else if(Z.riv){")
# ---- dibujo: olas, carteles de la recta, lanchas con esquiador y motos ----
h = rep(h, " case 'pier':{", r""" case 'fwave':{const L=o.L,ph=G.t*2.2+o.ph;ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.a);ctx.fillStyle='rgba(8,60,110,.2)';ctx.beginPath();ctx.ellipse(0,9,L/2,11,0,0,TAU);ctx.fill();
  const g2=ctx.createLinearGradient(0,-14,0,8);g2.addColorStop(0,'rgba(200,245,255,0)');g2.addColorStop(.55,'rgba(170,235,250,.6)');g2.addColorStop(1,'rgba(255,255,255,.95)');ctx.fillStyle=g2;
  ctx.beginPath();ctx.moveTo(-L/2,5);for(let x=-L/2;x<=L/2;x+=8){const k=1-Math.abs(x)/(L/2);ctx.lineTo(x,-4-10*k-3*Math.sin(x*.05+ph)*k);}ctx.lineTo(L/2,5);ctx.closePath();ctx.fill();
  ctx.fillStyle='rgba(255,255,255,.95)';for(let x=-L/2+6;x<L/2;x+=8){const k=1-Math.abs(x)/(L/2);ctx.beginPath();ctx.arc(x,4+Math.sin(x*.3+ph*2)*1.4,1.4+k*2.4,0,TAU);ctx.fill();}ctx.restore();}return;
 case 'lgate':{const x0=o.x-o.w/2,x1=o.x+o.w/2;for(const x of[x0,x1]){ctx.fillStyle='rgba(0,20,50,.3)';ctx.beginPath();ctx.ellipse(x+3,o.y+4,7,5,0,0,TAU);ctx.fill();ctx.fillStyle='#ff7a1a';ctx.beginPath();ctx.arc(x,o.y,7,0,TAU);ctx.fill();}
  ctx.font='800 15px "Saira Condensed",sans-serif';const tw=ctx.measureText(o.txt).width+24;ctx.fillStyle='rgba(8,22,48,.88)';ctx.beginPath();ctx.roundRect(o.x-tw/2,o.y-30,tw,22,7);ctx.fill();ctx.fillStyle='#ffe14d';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(o.txt,o.x,o.y-18.5);
  ctx.strokeStyle='rgba(255,255,255,.7)';ctx.setLineDash([6,6]);ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(x0,o.y);ctx.lineTo(x1,o.y);ctx.stroke();ctx.setLineDash([]);}return;
 case 'skiboat':case 'npcjet':{const T=o.trail||[],f=o.t==='skiboat'?3.4:1.8;for(let k=1;k<T.length;k++){const p=T[k],a=(1-k/T.length)*(o.t==='skiboat'?.75:.55),off=k*f,px=Math.cos(p.h),py=Math.sin(p.h);ctx.fillStyle=`rgba(255,255,255,${a.toFixed(3)})`;for(const sg of[-1,1]){ctx.beginPath();ctx.arc(p.x+px*off*sg,p.y+py*off*sg,2+k*.08,0,TAU);ctx.fill();}if(k<8){ctx.beginPath();ctx.arc(p.x,p.y,3.2-k*.3,0,TAU);ctx.fill();}}
  if(o.t==='skiboat'){if(o.skx!=null){const sx2=o.x-Math.sin(o.h)*28,sy2=o.y+Math.cos(o.h)*28;ctx.strokeStyle='rgba(30,30,30,.7)';ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(sx2,sy2);ctx.lineTo(o.skx,o.sky);ctx.stroke();
    ctx.save();ctx.translate(o.skx,o.sky);ctx.rotate(o.skh||o.h);ctx.fillStyle='rgba(255,255,255,.7)';ctx.beginPath();ctx.ellipse(0,10,6,4,0,0,TAU);ctx.fill();ctx.fillStyle='#222';ctx.fillRect(-4,-7,2.4,15);ctx.fillRect(1.6,-7,2.4,15);ctx.fillStyle=o.sk;ctx.beginPath();ctx.ellipse(0,0,3.6,4.6,0,0,TAU);ctx.fill();ctx.fillStyle='#e8b48c';ctx.beginPath();ctx.arc(0,-4.5,2.4,0,TAU);ctx.fill();ctx.restore();}
   ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);ctx.fillStyle='rgba(0,20,50,.25)';ctx.beginPath();ctx.ellipse(4,6,10,26,0,0,TAU);ctx.fill();ctx.drawImage(SP.motor.c,-13,-29,26,58);ctx.restore();}
  else{const sp=SP.jet[o.id]||SP.jet[MOTOS[0].id];ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);ctx.drawImage(sp.c,-16,-34,32,68);ctx.restore();}}return;
 case 'pier':{""")
open(H, 'w').write(h); print('ok')
