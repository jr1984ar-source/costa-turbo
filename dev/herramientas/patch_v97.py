import shutil
H = 'costa-turbo.html'
shutil.copy(H, 'costa-turbo.pre-v97.html')
h = open(H).read()
def rep(s, a, b, n=1):
    c = s.count(a); assert c == n, (c, a[:100]); return s.replace(a, b)
h = rep(h, "const APP_VER=96", "const APP_VER=97")
# ---- choques: no tocar el rumbo (así se puede girar y salir); si te quedas dentro, te saca al agua ----
i0 = h.index("function rmUnstick(c,dt){"); i1 = h.index("function rmFoot(o){")
h = h[:i0] + r"""function rmNearWater(x,y,ty){let best=null,bd=1e9;for(let r=6;r<=150;r+=6){for(let k=0;k<16;k++){const a=k/16*TAU,px=x+Math.cos(a)*r,py=y+Math.sin(a)*r;if(rmV(px,py)===0&&rmV(px,py-30)===0){const d=Math.hypot(px-(ty!=null?ty:x),py-y)*.3+r;if(d<bd){bd=d;best=[px,py];}}}if(best)return best;}return null;}
function rmUnstick(c,dt){if(c.isP||c.fin)return;const k=c._sk||(c._sk={y:c.y,t:0});k.t+=dt;if(k.t<1.4)return;if(Math.abs(c.y-k.y)<45){const sp=rmSpan(c.x,c.y),tx=(sp[0]+sp[1])/2;let best=null,bd=1e9;for(let x=4;x<RMW;x+=6){if(rmV(x,c.y)!==0||rmV(x,c.y-50)!==0||rmV(x,c.y-110)!==0)continue;const d=Math.abs(x-tx)*.5+Math.abs(x-c.x);if(d<bd){bd=d;best=x;}}if(best!=null){c.x=best;c.h=c.va=0;c.v=Math.max(c.v,90);c.ai.tx=best;c.ai.re=.5;c._rlx=c.x;c._rly=c.y;}}c._sk={y:c.y,t:0};}
function rmNormal(x,y){let nx=0,ny=0;for(let k=0;k<16;k++){const a=k/16*TAU,dx=Math.cos(a),dy=Math.sin(a);if(rmLand(x+dx*16,y+dy*16)){nx-=dx;ny-=dy;}}const l=Math.hypot(nx,ny);return l?[nx/l,ny/l]:[0,1];}
function realHit(c,dt){if(c._bumpT>0)c._bumpT-=dt;if(c.air>0)return;const nose=()=>[c.x+Math.sin(c.h)*16,c.y-Math.cos(c.h)*16];let hp=nose();const onC=rmLand(c.x,c.y),onN=c.v>0&&rmLand(hp[0],hp[1]);
 if(!onC&&!onN){c._rlx=c.x;c._rly=c.y;return;}
 const n=onC?rmNormal(c.x,c.y):rmNormal(hp[0],hp[1]);
 let fx=Math.sin(c.h),fy=-Math.cos(c.h);const d=fx*n[0]+fy*n[1];
 if(d<0&&c.v>0){fx-=n[0]*d*1.35;fy-=n[1]*d*1.35;c.h=c.va=Math.atan2(fx,-fy);}
 for(let s=0;s<16;s++){hp=nose();if(!rmLand(c.x,c.y)&&!(c.v>0&&rmLand(hp[0],hp[1])))break;c.x+=n[0]*3;c.y+=n[1]*3;}
 if(rmLand(c.x,c.y)){const w=rmNearWater(c.x,c.y);if(w){c.x=w[0];c.y=w[1];}}
 const hard=d<-.55;c.v*=hard?.55:.9;if(hard)c.boostT=0;if(!c.isP&&hard)c.ai.re=0;
 if(c.isP&&!G.demo&&hard&&!(c._bumpT>0)){c._bumpT=.7;Snd.bump();buzz(40);G.shake=5;pop(c.x,c.y-36,'¡TIERRA!','#ff4757');}}
""" + h[i1:]
# ---- dibujo de la tierra: calles, chalets con tejado, piscinas, jardines y pisos ----
i0 = h.index("const RTW=400;\nfunction renderRealTile(i,j){"); i1 = h.index("function drawRealMap(){")
h = h[:i0] + r"""const RTW=400,RSX=150,RSY=124;
const rmIn=(x,y,d)=>rmLand(x,y)&&rmLand(x-d,y)&&rmLand(x+d,y)&&rmLand(x,y-d)&&rmLand(x,y+d)&&rmV(x,y)!==2;
const stX=k=>k*RSX+hash2(k,7,5)*36,stY=k=>k*RSY+hash2(k,3,9)*28;
function renderRealTile(i,j){const x0=j*RTW,x1=x0+RTW,y0=i*CH,y1=y0+CH,CW=RTW,M=24;
 const c=document.createElement('canvas');c.width=Math.ceil(CW*K);c.height=Math.ceil(CH*K);const g=c.getContext('2d');
 const mw=Math.ceil((CW+2*M)/3)+2,mh=Math.ceil((CH+2*M)/3)+2,mx0=x0-M,my0=y0-M;
 const vals=new Uint8Array(mw*mh);for(let my=0;my<mh;my++)for(let mxx=0;mxx<mw;mxx++)vals[my*mw+mxx]=rmV(mx0+mxx*3+1.5,my0+my*3+1.5);
 const mask=(test)=>{const m=document.createElement('canvas');m.width=mw;m.height=mh;const mg=m.getContext('2d'),id=mg.createImageData(mw,mh);let any=false;for(let k=0;k<vals.length;k++){if(test(vals[k])){id.data[k*4+3]=255;id.data[k*4]=id.data[k*4+1]=id.data[k*4+2]=255;any=true;}}mg.putImageData(id,0,0);m._any=any;return m;};
 const put=(m,ctx)=>{ctx.imageSmoothingEnabled=true;ctx.drawImage(m,(mx0-x0)*K,(my0-y0)*K,mw*3*K,mh*3*K);};
 const layer=(m,fill)=>{if(!m._any)return;const t=document.createElement('canvas');t.width=c.width;t.height=c.height;const tg=t.getContext('2d');put(m,tg);tg.globalCompositeOperation='source-in';tg.fillStyle=fill;tg.fillRect(0,0,t.width,t.height);g.drawImage(t,0,0);};
 const landM=mask(v=>v>0&&v<5),outM=mask(v=>v===6);
 layer(outM,'rgba(4,30,70,.22)');
 if(landM._any){
  g.save();g.shadowColor='rgba(140,240,226,.95)';g.shadowBlur=26*K;put(landM,g);put(landM,g);g.restore();
  g.save();g.shadowColor='rgba(255,255,255,.95)';g.shadowBlur=3*K;put(landM,g);g.restore();
  layer(landM,'#a9c47c');layer(mask(v=>v===2),'#f1d9a6');}
 g.save();g.scale(K,K);g.translate(-x0,-y0);const q=rng(9000+i*7+j*131),Zn=G.zone;
 if(landM._any){
  // césped con matices y orilla de roca
  for(let k=0;k<260;k++){const x=x0+q()*CW,y=y0+q()*CH;if(!rmLand(x,y)||rmV(x,y)===2)continue;g.fillStyle=k%2?'rgba(120,160,80,.35)':'rgba(190,210,140,.35)';g.beginPath();g.arc(x,y,3+q()*5,0,TAU);g.fill();}
  for(let k=0;k<900;k++){const x=x0+q()*CW,y=y0+q()*CH,v=rmV(x,y);if(!(v>0&&v<5)||v===2)continue;if(rmIn(x,y,14))continue;g.fillStyle=['#bfa98c','#a28d75','#cdbfa6','#8f7c66'][k%4];g.beginPath();g.ellipse(x,y,3+q()*5,2+q()*3.5,q()*3,0,TAU);g.fill();}
  // calles
  const jx0=Math.floor((x0-M)/RSX)-1,jx1=Math.ceil((x1+M)/RSX)+1,jy0=Math.floor((y0-M)/RSY)-1,jy1=Math.ceil((y1+M)/RSY)+1;
  g.fillStyle='#8e9196';
  for(let kx=jx0;kx<=jx1;kx++){const sx=stX(kx);if(sx<x0-20||sx>x1+20)continue;for(let y=y0-6;y<y1+6;y+=6)if(rmIn(sx,y,22))g.fillRect(sx-6,y,12,6.6);}
  for(let ky=jy0;ky<=jy1;ky++){const sy=stY(ky);if(sy<y0-20||sy>y1+20)continue;for(let x=x0-6;x<x1+6;x+=6)if(rmIn(x,sy,22))g.fillRect(x,sy-6,6.6,12);}
  g.fillStyle='rgba(255,255,255,.7)';
  for(let kx=jx0;kx<=jx1;kx++){const sx=stX(kx);if(sx<x0-20||sx>x1+20)continue;for(let y=Math.floor(y0/14)*14;y<y1;y+=14)if(rmIn(sx,y,22))g.fillRect(sx-.6,y,1.2,6);}
  for(let ky=jy0;ky<=jy1;ky++){const sy=stY(ky);if(sy<y0-20||sy>y1+20)continue;for(let x=Math.floor(x0/14)*14;x<x1;x+=14)if(rmIn(x,sy,22))g.fillRect(x,sy-.6,6,1.2);}
  // parcelas: chalets con tejado, piscinas, jardines, pisos y árboles
  for(let kx=jx0;kx<jx1;kx++)for(let ky=jy0;ky<jy1;ky++){const bx0=stX(kx)+9,bx1=stX(kx+1)-9,by0=stY(ky)+9,by1=stY(ky+1)-9;if(bx1<x0-60||bx0>x1+60||by1<y0-60||by0>y1+60)continue;
   const nx=2,ny=2,lw=(bx1-bx0)/nx,lh=(by1-by0)/ny;
   for(let a=0;a<nx;a++)for(let b=0;b<ny;b++){const lx=bx0+a*lw,ly=by0+b*lh,cx=lx+lw/2,cy=ly+lh/2,r=hash2(kx*7+a,ky*5+b,77),r2=hash2(kx+a*3,ky+b*11,31),v=rmV(cx,cy);
    if(!rmIn(cx,cy,Math.min(lw,lh)/2-2)||!rmLand(lx+2,ly+2)||!rmLand(lx+lw-2,ly+2)||!rmLand(lx+2,ly+lh-2)||!rmLand(lx+lw-2,ly+lh-2))continue;
    const forest=v===3&&r2<.5;
    g.fillStyle=(a+b)%2?'#9cbd69':'#b2cd82';g.fillRect(lx+1.5,ly+1.5,lw-3,lh-3);g.strokeStyle='#6f9449';g.lineWidth=1.6;g.strokeRect(lx+1.5,ly+1.5,lw-3,lh-3);
    if(forest){for(let t=0;t<4;t++)drawDeco(g,{t:'pine',x:lx+8+hash2(kx+t,ky+a,b+5)*(lw-16),y:ly+8+hash2(ky+t,kx+b,a+9)*(lh-16),r:7+hash2(t,kx,ky)*6,s:(r*1e6+t)|0},Zn);continue;}
    const flat=r>.72,big=r>.9&&(v===4||v===1);
    const hw=big?lw*.8:lw*(.42+r2*.18),hh=big?lh*.7:lh*(.4+r*.15),hx=lx+(big?lw*.1:(r2<.5?lw*.12:lw-hw-lw*.12)),hy=ly+(big?lh*.15:lh*.14);
    g.fillStyle='rgba(0,0,0,.22)';g.fillRect(hx+4,hy+5,hw,hh);
    if(big){g.fillStyle='#e2ddd2';g.fillRect(hx,hy,hw,hh);g.strokeStyle='#b9b2a4';g.lineWidth=1.2;g.strokeRect(hx,hy,hw,hh);for(let t=1;t<4;t++){g.beginPath();g.moveTo(hx+hw*t/4,hy);g.lineTo(hx+hw*t/4,hy+hh);g.stroke();}g.fillStyle='#a8a296';g.fillRect(hx+4,hy+4,5,4);g.fillRect(hx+hw-10,hy+hh-9,6,5);}
    else if(flat){g.fillStyle='#f1eee7';g.fillRect(hx,hy,hw,hh);g.strokeStyle='#c9c3b6';g.lineWidth=1.2;g.strokeRect(hx+1,hy+1,hw-2,hh-2);g.fillStyle='#b7b0a2';g.fillRect(hx+hw*.6,hy+hh*.2,4,4);}
    else{const tc=['#c8643c','#d2703f','#b95a35','#c96a44'][(r2*4)|0];g.fillStyle=tc;g.fillRect(hx,hy,hw,hh);g.fillStyle='rgba(255,220,190,.22)';g.fillRect(hx,hy,hw,hh/2);g.fillStyle='rgba(60,20,10,.2)';g.fillRect(hx,hy+hh/2,hw,hh/2);g.strokeStyle='#8e3f22';g.lineWidth=1.3;g.beginPath();g.moveTo(hx+2,hy+hh/2);g.lineTo(hx+hw-2,hy+hh/2);g.stroke();
     g.strokeStyle='rgba(120,50,25,.35)';g.lineWidth=.6;for(let t=hx+3;t<hx+hw;t+=3){g.beginPath();g.moveTo(t,hy);g.lineTo(t,hy+hh);g.stroke();}}
    if(!big&&r2>.25){const pw=Math.min(lw*.4,22),ph=Math.min(lh*.26,11),px=r2<.5?lx+lw-pw-6:lx+6,py=ly+lh-ph-7;if(rmIn(px+pw/2,py+ph/2,8)){g.fillStyle='#f4f1ea';g.fillRect(px-2,py-2,pw+4,ph+4);g.fillStyle='#3cc6e6';g.fillRect(px,py,pw,ph);g.fillStyle='rgba(255,255,255,.55)';g.fillRect(px+2,py+2,pw*.4,1.4);}}
    if(r>.35)drawDeco(g,{t:'pine',x:r2<.5?lx+lw-9:lx+9,y:ly+9,r:6+r*4,s:(r*1e6)|0},Zn);}}
 }
 for(let y=Math.ceil(y0/34)*34;y<y1;y+=34){const xb=rmCor(y);if(xb<x0-10||xb>x1+10)continue;g.fillStyle='rgba(0,20,50,.3)';g.beginPath();g.ellipse(xb+2,y+3,5,3.5,0,0,TAU);g.fill();g.fillStyle=((y/34)|0)%2?'#ffffff':'#ff4d4d';g.beginPath();g.arc(xb,y,4.5,0,TAU);g.fill();}
 g.restore();return c;}
""" + h[i1:]
open(H, 'w').write(h); print('ok')
