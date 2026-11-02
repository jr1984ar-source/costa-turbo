import shutil,json
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v96.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
RM = json.load(open('realmap2.json'))
h = rep(h, "const APP_VER=95", "const APP_VER=96")
i0 = h.index("const RMAP="); i1 = h.index("const RING_R=72,")
code = r"""const RMAP={w:@W@,h:@H@,c:3,src:'@SRC@'};const RCOR=@COR@;let RMD=null;const RM_BOT=520,RM_TOP=RM_BOT-RMAP.h*3,RM_LEN=-(RM_TOP+300),RMW=RMAP.w*3;
{const im=new Image();im.onload=()=>{const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const g=c.getContext('2d');g.drawImage(im,0,0);const d=g.getImageData(0,0,im.width,im.height).data,a=new Uint8Array(im.width*im.height);for(let i=0;i<a.length;i++)a[i]=Math.round(d[i*4]/36);RMD=a;};im.src=RMAP.src;}
function rmV(x,y){if(!RMD)return x<40?1:0;let row=Math.floor((y-RM_TOP)/3);row=row<0?0:row>=RMAP.h?RMAP.h-1:row;const col=Math.floor(x/3);if(col>=RMAP.w)return 6;if(col<0){const v=RMD[row*RMAP.w];return v===0||v>=5?1:v;}return RMD[row*RMAP.w+col];}
const rmLand=(x,y)=>{const v=rmV(x,y);return v>0&&v<5;};
function rmCor(y){let r=Math.floor((y-RM_TOP)/12);r=r<0?0:r>=RCOR.length?RCOR.length-1:r;return RCOR[r];}
function rmShore(y){for(let x=0;x<RMW;x+=3)if(rmV(x,y)===0)return x;return RMW;}
function rmSpan(x,y){const runs=yy=>{const out=[];let a=-1;for(let c=-2;c<=RMAP.w+1;c++){const w=rmV(c*3+1,yy)===0;if(w&&a<0)a=c;if(!w&&a>=0){out.push([a*3,c*3]);a=-1;}}return out;};
 const pick=(rs,px)=>{let best=null,bd=1e9;for(const r of rs){if(r[1]-r[0]<45)continue;const d=px<r[0]?r[0]-px:px>r[1]?px-r[1]:0;if(d<bd||(d===bd&&best&&r[1]-r[0]>best[1]-best[0])){bd=d;best=r;}}return best;};
 let s=pick(runs(y-50),x);if(!s)s=pick(runs(y-130),x);if(!s)return[x-40,x+40];for(const dy of[130,230,330]){const s2=pick(runs(y-dy).filter(r=>r[1]>s[0]&&r[0]<s[1]),(s[0]+s[1])/2);if(!s2)break;const a=Math.max(s[0],s2[0]),b=Math.min(s[1],s2[1]);if(b-a>50)s=[a,b];else break;}
 let L=s[0]+26,R=s[1]-26;if(R-L>340)R=L+340;return L<R?[L,R]:[(s[0]+s[1])/2-2,(s[0]+s[1])/2+2];}
function rmUnstick(c,dt){if(c.isP||c.fin)return;const k=c._sk||(c._sk={y:c.y,t:0});k.t+=dt;if(k.t<1.6)return;if(Math.abs(c.y-k.y)<45){let best=null,bd=1e9;for(let x=4;x<RMW;x+=6){if(rmV(x,c.y)!==0||rmV(x,c.y-60)!==0)continue;const d=Math.abs(x-c.x);if(d<bd){bd=d;best=x;}}if(best!=null){c.x=best;c.h=c.va=0;c.v=Math.max(c.v,80);c.ai.tx=best;c.ai.re=.4;c._rlx=c.x;c._rly=c.y;}}c._sk={y:c.y,t:0};}
function realHit(c,dt){if(c.air>0){return;}const nx=c.x+Math.sin(c.h)*16,ny=c.y-Math.cos(c.h)*16;if(rmLand(c.x,c.y)||rmLand(nx,ny)){if(c._rlx!=null){c.x=c._rlx;c.y=c._rly;}c.v*=.35;c.boostT=0;c.h=c.va=c.h*.5;if(!c.isP)c.ai.re=0;if(c.isP&&!G.demo&&!(c._bumpT>0)){c._bumpT=.7;Snd.bump();buzz(40);G.shake=5;pop(c.x,c.y-36,'¡TIERRA!','#ff4757');}}else{c._rlx=c.x;c._rly=c.y;}if(c._bumpT>0)c._bumpT-=dt;}
function rmFoot(o){const P=[];const add=(dx,dy)=>P.push([o.x+dx,o.y+dy]);
 if(o.t==='ramp'){const w=(o.w||100)/2,D=o.mega?820:RAMP_D[o.sz||'m'];for(const dx of[-w,0,w])add(dx,0);for(let k=0;k<=6;k++)add(0,-D*k/6);for(const dx of[-20,20])add(dx,-D-20);}
 else if(o.t==='yacht'){for(const dx of[-26,0,26])for(const dy of[-76,0,76])add(dx,dy);}
 else if(o.t==='sail'||o.t==='motor'){for(const dx of[-12,12])for(const dy of[-34,0,34])add(dx,dy);}
 else{const r=(o.rad||8)+8;add(0,0);add(-r,0);add(r,0);add(0,-r);add(0,r);}
 return P.some(p=>rmV(p[0],p[1])!==0);}
const RTW=400;
function renderRealTile(i,j){const x0=j*RTW,x1=x0+RTW,y0=i*CH,CW=RTW,M=24;
 const c=document.createElement('canvas');c.width=Math.ceil(CW*K);c.height=Math.ceil(CH*K);const g=c.getContext('2d');
 const mw=Math.ceil((CW+2*M)/3)+2,mh=Math.ceil((CH+2*M)/3)+2,mx0=x0-M,my0=y0-M;
 const vals=new Uint8Array(mw*mh);for(let my=0;my<mh;my++)for(let mxx=0;mxx<mw;mxx++)vals[my*mw+mxx]=rmV(mx0+mxx*3+1.5,my0+my*3+1.5);
 const mask=(test)=>{const m=document.createElement('canvas');m.width=mw;m.height=mh;const mg=m.getContext('2d'),id=mg.createImageData(mw,mh);let any=false;for(let k=0;k<vals.length;k++){if(test(vals[k])){id.data[k*4+3]=255;id.data[k*4]=id.data[k*4+1]=id.data[k*4+2]=255;any=true;}}mg.putImageData(id,0,0);m._any=any;return m;};
 const put=(m,ctx)=>{ctx.imageSmoothingEnabled=true;ctx.drawImage(m,(mx0-x0)*K,(my0-y0)*K,mw*3*K,mh*3*K);};
 const landM=mask(v=>v>0&&v<5);
 const outM=mask(v=>v===6);if(outM._any){const t=document.createElement('canvas');t.width=c.width;t.height=c.height;const tg=t.getContext('2d');put(outM,tg);tg.globalCompositeOperation='source-in';tg.fillStyle='rgba(4,30,70,.22)';tg.fillRect(0,0,t.width,t.height);g.drawImage(t,0,0);}
 if(landM._any){
  g.save();g.shadowColor='rgba(140,240,226,.95)';g.shadowBlur=26*K;put(landM,g);put(landM,g);g.restore();
  g.save();g.shadowColor='rgba(255,255,255,.95)';g.shadowBlur=3*K;put(landM,g);g.restore();
  const layer=(test,fill)=>{const m=mask(test);if(!m._any)return;const t=document.createElement('canvas');t.width=c.width;t.height=c.height;const tg=t.getContext('2d');put(m,tg);tg.globalCompositeOperation='source-in';tg.fillStyle=fill;tg.fillRect(0,0,t.width,t.height);g.drawImage(t,0,0);};
  layer(v=>v>0&&v<5,'#c47a44');layer(v=>v===2,'#f1d9a6');layer(v=>v===3,'#7da35a');layer(v=>v===4,'#e9e4d8');}
 g.save();g.scale(K,K);g.translate(-x0,-y0);const q=rng(9000+i*7+j*131);const Zn=G.zone;
 if(landM._any)for(let k=0;k<360;k++){const x=x0+q()*CW,y=y0+q()*CH,v=rmV(x,y),e=rmLand(x-10,y)&&rmLand(x+10,y)&&rmLand(x,y-10)&&rmLand(x,y+10);
  if(v===1&&k%2){g.fillStyle=['#d98f57','#b9693a','#e7a46b','#a75d31'][k%4];g.globalAlpha=.8;g.beginPath();g.ellipse(x,y,4+q()*7,3+q()*4,q()*3,0,TAU);g.fill();g.globalAlpha=1;}
  else if(v===2&&k%3===0){g.fillStyle=q()>.5?'rgba(180,140,80,.35)':'rgba(255,255,255,.5)';g.fillRect(x,y,1.4,1.4);}
  else if(v===3&&e&&k%3===0)drawDeco(g,{t:'pine',x,y,r:8+q()*8,s:(q()*1e6)|0},Zn);
  else if(v===4&&e&&k%9===0)drawDeco(g,{t:'house',x,y,w:16+q()*16,h:14+q()*14,c:['#d9775a','#e9e4da','#c9a77a','#f2efe8','#d98a6a'][(q()*5)|0],s:(q()*1e6)|0},Zn);}
 for(let y=Math.ceil(y0/34)*34;y<y0+CH;y+=34){const xb=rmCor(y);if(xb<x0-10||xb>x1+10)continue;g.fillStyle='rgba(0,20,50,.3)';g.beginPath();g.ellipse(xb+2,y+3,5,3.5,0,0,TAU);g.fill();g.fillStyle=((y/34)|0)%2?'#ffffff':'#ff4d4d';g.beginPath();g.arc(xb,y,4.5,0,TAU);g.fill();}
 g.restore();return c;}
function drawRealMap(){const i0=Math.floor(camTop/CH),i1=Math.floor((camTop+VH)/CH),j0=Math.floor(camX/RTW),j1=Math.floor((camX+VW)/RTW);
 for(let i=i0;i<=i1;i++)for(let j=j0;j<=j1;j++){const key='t'+i+'_'+j;let c=chunks.get(key);if(!c){c=renderRealTile(i,j);chunks.set(key,c);if(chunks.size>18){for(const kk of chunks.keys()){const [a,b]=kk.slice(1).split('_').map(Number);if(a<i0-1||a>i1+1||b<j0-1||b>j1+1){chunks.delete(kk);if(chunks.size<=14)break;}}}}ctx.drawImage(c,j*RTW,i*CH,c.width/K,c.height/K);}}
"""
code = code.replace('@W@',str(RM['w'])).replace('@H@',str(RM['h'])).replace('@COR@',json.dumps(RM['cor'],separators=(',',':'))).replace('@SRC@',RM['src'])
h = h[:i0] + code + h[i1:]
# pasillo de carrera como pared derecha (sin dibujar costa a la derecha)
h = rep(h, "zone.rwall=null;if(Z.alt){", "zone.rwall=Z.realMap?(y=>rmCor(y)):null;if(Z.alt){")
h = rep(h, "if(Zn.rwall){const xr=(VW>WG?WG+(VW-WG)/2:WG)+40,", "if(Zn.rwall&&!Zn.realMap){const xr=(VW>WG?WG+(VW-WG)/2:WG)+40,")
h = rep(h, "const ex=(VW>WG?WG+(VW-WG)/2:WG)-11;", "const ex=Zn.realMap?1e9:(VW>WG?WG+(VW-WG)/2:WG)-11;")
h = rep(h, "case 'check':case 'finish':{const x0=G.zone.shore(o.y)+6,x1=WG+(VW>WG?(VW-WG)/2:0)-4,", "case 'check':case 'finish':{const x0=G.zone.shore(o.y)+6,x1=G.zone.realMap?G.zone.rwall(o.y)-4:WG+(VW>WG?(VW-WG)/2:0)-4,")
h = rep(h, "const L=Math.max(24,zone.shore(-u)+36),R=Math.min(WG-24,zone.rwall?zone.rwall(-u)-30:999);", "const L=Math.max(24,zone.shore(-u)+36),R=Math.min(Z.realMap?L+420:WG-24,zone.rwall?zone.rwall(-u)-30:999);")
# salida junto a la costa y cámara que sigue en horizontal
h = rep(h, "camTop=G.P.y-VH*.76;camX=-(VW-WG)/2;", "if(Zn.realMap){const sx=rmShore(0)+40;for(const c of[G.P,...G.rivals])c.x=sx+(c.x-WG*.3);G._camSnap=1;}camTop=G.P.y-VH*.76;camX=-(VW-WG)/2;")
h = rep(h, "const target=P.y-VH*.76;camTop+=(target-camTop)*Math.min(1,dt*8)", "const target=P.y-VH*.76;camTop+=(target-camTop)*Math.min(1,dt*8);if(Zn.realMap){const tx=clamp(P.x-VW/2,-40,RMW-VW+40);camX=G._camSnap?tx:camX+(tx-camX)*Math.min(1,dt*5);G._camSnap=0;}0")
h = rep(h, " if(Math.abs(target-camTop)>VH)camTop=target;\n camX=VW>WG?-(VW-WG)/2:0;}", " if(Math.abs(target-camTop)>VH)camTop=target;\n if(!Zn.realMap)camX=VW>WG?-(VW-WG)/2:0;}")
open(H, 'w').write(h); print('ok')
