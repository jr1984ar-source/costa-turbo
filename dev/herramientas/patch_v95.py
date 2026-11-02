import shutil,json
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v95.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
RM = json.load(open('realmap.json'))
h = rep(h, "const APP_VER=94", "const APP_VER=95")
# ---- pantalla nueva (solo Carrera libre) ----
h = rep(h, "theme:'port',tod:'golden',skill:.95,boss:1}\n];",
 "theme:'port',tod:'golden',skill:.95,boss:1},\n {name:'SON MATÍAS – ILLETES',realMap:1,water:['#22b3d6','#0b6fb3'],obj:'race3',goal:'Termina entre los 3 primeros por la costa real: del JJ’S de Son Matías, por Punta Negra, Puerto Portals y Portals Nous, hasta la playa de Illetes.',len:10000,riv:5,bar:null,theme:'cove',tod:'noon',skill:.9,finish:'ILLETES'}\n];")
h = rep(h, "land:'final'}\n];\n", "land:'final'},\n {tag:'COSTA REAL · TOP 3',sky:['#2a8de6','#cdeeff'],sea:['#78dcee','#0a5cae'],sun:[150,22,'#ffffff'],land:'portals'}\n];\n")
h = rep(h, "G.zi===ZONES.length-1?100:85", "ZONES[G.zi].boss?100:85")
# ---- datos del mapa y funciones ----
h = rep(h, "const RING_R=72,", """const RMAP={w:@W@,h:@H@,H:@HH@,src:'@SRC@'};let RMD=null;const RM_BOT=520,RM_TOP=RM_BOT-RMAP.H,RM_LEN=-(RM_TOP+320);
{const im=new Image();im.onload=()=>{const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const g=c.getContext('2d');g.drawImage(im,0,0);const d=g.getImageData(0,0,im.width,im.height).data,a=new Uint8Array(im.width*im.height);for(let i=0;i<a.length;i++)a[i]=Math.round(d[i*4]/40);RMD=a;};im.src=RMAP.src;}
function rmV(x,y){if(!RMD)return x<40?1:0;const row=Math.floor((y-RM_TOP)/2);if(row<0||row>=RMAP.h)return x<60?1:0;let col=Math.floor(x/2);if(col>=RMAP.w)return 0;if(col<0){const v=RMD[row*RMAP.w];return v===0||v===5?1:v;}return RMD[row*RMAP.w+col];}
const rmLand=(x,y)=>{const v=rmV(x,y);return v>0&&v<5;};
function rmShore(y){for(let x=0;x<WG;x+=2)if(!rmLand(x,y))return x;return WG;}
function rmSpan(x,y){const runs=yy=>{const out=[];let a=-1;for(let c=-6;c<=RMAP.w+2;c++){const w=rmV(c*2,yy)===0;if(w&&a<0)a=c;if(!w&&a>=0){out.push([a*2,c*2]);a=-1;}}if(a>=0)out.push([a*2,(RMAP.w+2)*2]);return out;};
 const pick=(rs,px)=>{let best=null,bd=1e9;for(const r of rs){if(r[1]-r[0]<44)continue;const d=px<r[0]?r[0]-px:px>r[1]?px-r[1]:0;if(d<bd||(d===bd&&best&&r[1]-r[0]>best[1]-best[0])){bd=d;best=r;}}return best;};
 let s=pick(runs(y-50),x);if(!s)s=pick(runs(y-130),x);if(!s)return[40,WG-40];for(const dy of[130,230,330]){const s2=pick(runs(y-dy).filter(r=>r[1]>s[0]&&r[0]<s[1]),(s[0]+s[1])/2);if(!s2)break;const a=Math.max(s[0],s2[0]),b=Math.min(s[1],s2[1]);if(b-a>50)s=[a,b];else break;}
 const L=s[0]+24,R=s[1]-24;return L<R?[L,R]:[(s[0]+s[1])/2-2,(s[0]+s[1])/2+2];}
function rmUnstick(c,dt){if(c.isP||c.fin)return;const k=c._sk||(c._sk={y:c.y,t:0});k.t+=dt;if(k.t<1.6)return;if(Math.abs(c.y-k.y)<45){let best=null,bd=1e9;for(let x=8;x<WG;x+=6){if(rmV(x,c.y)!==0||rmV(x,c.y-60)!==0)continue;const d=Math.abs(x-c.x);if(d<bd){bd=d;best=x;}}if(best!=null){c.x=best;c.h=c.va=0;c.v=Math.max(c.v,80);c.ai.tx=best;c.ai.re=.4;c._rlx=c.x;c._rly=c.y;}}c._sk={y:c.y,t:0};}
function realHit(c,dt){if(c.air>0){return;}const nx=c.x+Math.sin(c.h)*16,ny=c.y-Math.cos(c.h)*16;if(rmLand(c.x,c.y)||rmLand(nx,ny)){if(c._rlx!=null){c.x=c._rlx;c.y=c._rly;}c.v*=.35;c.boostT=0;c.h=c.va=c.h*.5;if(!c.isP)c.ai.re=0;if(c.isP&&!G.demo&&!(c._bumpT>0)){c._bumpT=.7;Snd.bump();buzz(40);G.shake=5;pop(c.x,c.y-36,'¡TIERRA!','#ff4757');}}else{c._rlx=c.x;c._rly=c.y;}if(c._bumpT>0)c._bumpT-=dt;}
function rmFoot(o){const P=[];const add=(dx,dy)=>P.push([o.x+dx,o.y+dy]);
 if(o.t==='ramp'){const w=(o.w||100)/2,D=o.mega?820:RAMP_D[o.sz||'m'];for(const dx of[-w,0,w])add(dx,0);for(let k=0;k<=6;k++)add(0,-D*k/6);for(const dx of[-20,20])add(dx,-D-20);}
 else if(o.t==='yacht'){for(const dx of[-26,0,26])for(const dy of[-76,0,76])add(dx,dy);}
 else if(o.t==='sail'||o.t==='motor'){for(const dx of[-12,12])for(const dy of[-34,0,34])add(dx,dy);}
 else{const r=(o.rad||8)+8;add(0,0);add(-r,0);add(r,0);add(0,-r);add(0,r);}
 return P.some(p=>rmLand(p[0],p[1]));}
function renderRealChunk(i){const x0=Math.floor(camX)-4,x1=Math.ceil(camX+VW)+4,y0=i*CH,CW=x1-x0;
 const c=document.createElement('canvas');c.width=Math.ceil(CW*K);c.height=Math.ceil(CH*K);c._x0=x0;const g=c.getContext('2d');
 const mw=Math.ceil(CW/2)+4,mh=CH/2+8,mx0=x0-4,my0=y0-8;
 const mk=()=>{const m=document.createElement('canvas');m.width=mw;m.height=mh;return m;};
 const vals=new Uint8Array(mw*mh);for(let my=0;my<mh;my++)for(let mxx=0;mxx<mw;mxx++)vals[my*mw+mxx]=rmV(mx0+mxx*2+1,my0+my*2+1);
 const mask=(test)=>{const m=mk(),mg=m.getContext('2d'),id=mg.createImageData(mw,mh);for(let k=0;k<vals.length;k++){const v=vals[k];if(test(v)){id.data[k*4+3]=255;id.data[k*4]=id.data[k*4+1]=id.data[k*4+2]=255;}}mg.putImageData(id,0,0);return m;};
 const landM=mask(v=>v>0&&v<5);
 const put=(m,ctx)=>{ctx.imageSmoothingEnabled=true;ctx.drawImage(m,(mx0-x0)*K,(my0-y0)*K,mw*2*K,mh*2*K);};
 g.save();g.shadowColor='rgba(140,240,226,.95)';g.shadowBlur=24*K;put(landM,g);put(landM,g);g.restore();
 g.save();g.shadowColor='rgba(255,255,255,.95)';g.shadowBlur=3*K;put(landM,g);g.restore();
 const layer=(test,fill)=>{const t=document.createElement('canvas');t.width=c.width;t.height=c.height;const tg=t.getContext('2d');put(mask(test),tg);tg.globalCompositeOperation='source-in';tg.fillStyle=fill;tg.fillRect(0,0,t.width,t.height);g.drawImage(t,0,0);};
 layer(v=>v>0&&v<5,'#c47a44');layer(v=>v===2,'#f1d9a6');layer(v=>v===3,'#7da35a');layer(v=>v===4,'#e9e4d8');
 g.save();g.scale(K,K);g.translate(-x0,-y0);const q=rng(9000+i*7);const Zn=G.zone;
 for(let k=0;k<520;k++){const x=x0+q()*CW,y=y0+q()*CH,v=rmV(x,y),e=rmLand(x-10,y)&&rmLand(x+10,y)&&rmLand(x,y-10)&&rmLand(x,y+10);
  if(v===1&&k%2){g.fillStyle=['#d98f57','#b9693a','#e7a46b','#a75d31'][k%4];g.globalAlpha=.8;g.beginPath();g.ellipse(x,y,4+q()*7,3+q()*4,q()*3,0,TAU);g.fill();g.globalAlpha=1;}
  else if(v===2&&k%3===0){g.fillStyle=q()>.5?'rgba(180,140,80,.35)':'rgba(255,255,255,.5)';g.fillRect(x,y,1.4,1.4);}
  else if(v===3&&e&&k%3===0)drawDeco(g,{t:'pine',x,y,r:8+q()*8,s:(q()*1e6)|0},Zn);
  else if(v===4&&e&&k%9===0)drawDeco(g,{t:'house',x,y,w:16+q()*16,h:14+q()*14,c:['#d9775a','#e9e4da','#c9a77a','#f2efe8','#d98a6a'][(q()*5)|0],s:(q()*1e6)|0},Zn);}
 g.restore();return c;}
function drawRealMap(){for(let i=Math.floor(camTop/CH);i<=Math.floor((camTop+VH)/CH);i++){const key='r'+i;let c=chunks.get(key);if(!c||c._x0!==Math.floor(camX)-4){c=renderRealChunk(i);chunks.set(key,c);if(chunks.size>8){const far=[...chunks.keys()].sort((a,b)=>Math.abs(+b.slice(1)-i)-Math.abs(+a.slice(1)-i))[0];chunks.delete(far);}}ctx.drawImage(c,c._x0,i*CH,c.width/K,c.height/K);}}
const RING_R=72,""".replace('@W@',str(RM['w'])).replace('@HH@',str(RM['H'])).replace('@H@',str(RM['h'])).replace('@SRC@',RM['src']))
# ---- generador de la pantalla ----
h = rep(h, "const lenK=(1.25+zi*.025)*(1+lap*.08),len=Math.round(Z.len*lenK),", "const lenK=(1.25+zi*.025)*(1+lap*.08),len=Z.realMap?RM_LEN:Math.round(Z.len*lenK),")
h = rep(h, " if(Z.theme==='open'){shoreU=u=>-(VW>WG?(VW-WG)/2:0);kindU=u=>'open';}\n", " if(Z.theme==='open'){shoreU=u=>-(VW>WG?(VW-WG)/2:0);kindU=u=>'open';}\n if(Z.realMap){shoreU=u=>rmShore(-u);kindU=u=>'cliff';}\n")
h = rep(h, "for(let uu=-400;uu<len+600;uu+=18+dr()*26){if(Z.theme==='open')break;", "for(let uu=-400;uu<len+600;uu+=18+dr()*26){if(Z.theme==='open'||Z.realMap)break;")
h = rep(h, "zone.swimX=y=>{if(Z.cuts&&", "zone.swimX=y=>{if(Z.realMap)return null;if(Z.cuts&&")
h = rep(h, "const wPat=Z.form?", "const wPat=Z.realMap?{coins:3.5,ramp:1.4,rocks:1,boat:1.2,yacht:.5}:Z.form?")
h = rep(h, " zone.objs=O.filter(o=>o.t==='check'||o.t==='finish'||", " if(Z.realMap){zone.realMap=true;for(let k=O.length-1;k>=0;k--){const o=O[k];if(o.t!=='finish'&&o.t!=='check'&&rmFoot(o))O.splice(k,1);}}\n zone.objs=O.filter(o=>o.t==='check'||o.t==='finish'||")
# ---- dibujo ----
h = rep(h, " else if(!Zn.circ){const[x0]=chunkRange();", " else if(Zn.realMap)drawRealMap();\n else if(!Zn.circ){const[x0]=chunkRange();")
# ---- choques con la tierra ----
h = rep(h, "if(!Zn.circ){const sx=Zn.shore(c.y)+11;if(c.x<sx){", "if(!Zn.circ){if(Zn.realMap)realHit(c,dt);const sx=Zn.realMap?-1e9:Zn.shore(c.y)+11;if(c.x<sx){")
# ---- IA: buscar el canal de agua de delante ----
h = rep(h, "const Zn=G.zone,L=Math.max((VW>WG?-(VW-WG)/2:0)+30,Zn.shore(c.y-120)+30),R=Math.min(WG-26,Zn.rwall?Zn.rwall(c.y-120)-30:999);c.ai.re-=dt;",
 "const Zn=G.zone;let L=Math.max((VW>WG?-(VW-WG)/2:0)+30,Zn.shore(c.y-120)+30),R=Math.min(WG-26,Zn.rwall?Zn.rwall(c.y-120)-30:999);if(Zn.realMap){const sp=rmSpan(c.x,c.y);L=sp[0];R=sp[1];if(c.ai.tx<L||c.ai.tx>R)c.ai.re=0;rmUnstick(c,dt);}c.ai.re-=dt;")
h = rep(h, "const dx=c.ai.tx-c.x,want=clamp(Math.atan2(dx,170),-.55,.55);", "const dx=c.ai.tx-c.x,want=clamp(Math.atan2(dx,Zn.realMap?110:170),Zn.realMap?-.8:-.55,Zn.realMap?.8:.55);")
open(H, 'w').write(h); print('ok')
