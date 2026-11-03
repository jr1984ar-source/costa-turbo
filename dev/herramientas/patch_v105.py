import json
p='costa-turbo.html';s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
RM=json.load(open('/tmp/claude-0/-home-user/e02bf71e-076d-586d-89ee-84e1312586e6/scratchpad/costa_real/realmap5.json'))
i0=s.index("const RMAP={");i1=s.index("let RMD=null;",i0)
s=s[:i0]+"const RMAP={w:%d,h:%d,c:3,src:'%s'};const RCOR=%s;const RSPOTS=%s;const RZONE=%s;"%(RM['w'],RM['h'],RM['src'],json.dumps(RM['cor'],separators=(',',':')),json.dumps(RM['spots'],separators=(',',':')),json.dumps(RM['zones'],separators=(',',':')))+s[i1:]
# zonas del lago: 1 agua profunda, 2 tropical, 3 pueblo
rep("a[i]=Math.round(d[i*4]/25);RMD=a;};im.src=RMAP.src;}",
"""a[i]=Math.round(d[i*4]/25);RMD=a;};im.src=RMAP.src;}
let RZD=null;{const im=new Image();im.onload=()=>{const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const g=c.getContext('2d');g.drawImage(im,0,0);RZD=g.getImageData(0,0,im.width,im.height).data;};im.src=RZONE.src;}
function rzF(x,y,k){if(!RZD)return 0;const S=RZONE.s*3,fx=x/S-.5,fy=(y-RM_TOP)/S-.5,ix=Math.floor(fx),iy=Math.floor(fy),tx=fx-ix,ty=fy-iy,W=RZONE.w,Hh=RZONE.h,ch=k-1;const at=(c,r)=>{c=c<0?0:c>=W?W-1:c;r=r<0?0:r>=Hh?Hh-1:r;return RZD[(r*W+c)*4+ch]/255;};return at(ix,iy)*(1-tx)*(1-ty)+at(ix+1,iy)*tx*(1-ty)+at(ix,iy+1)*(1-tx)*ty+at(ix+1,iy+1)*tx*ty;}""")
# agua de cada zona (debajo de la tierra) y bancos de arena
rep("layer(outM,'rgba(4,30,70,.22)');","""layer(outM,'rgba(4,30,70,.22)');
 if(RZD){const maskA=(fn)=>{const m=document.createElement('canvas');m.width=mw;m.height=mh;const mg=m.getContext('2d'),id=mg.createImageData(mw,mh);let any=false;for(let my=0;my<mh;my++)for(let mxx=0;mxx<mw;mxx++){const k=my*mw+mxx;if(vals[k]!==0&&vals[k]!==10)continue;const a=fn(mx0+mxx*3+1.5,my0+my*3+1.5);if(a>0.01){id.data[k*4+3]=Math.round(a*255);id.data[k*4]=id.data[k*4+1]=id.data[k*4+2]=255;any=true;}}mg.putImageData(id,0,0);m._any=any;return m;};
  const cx=(x0+x1)/2,cy=(y0+y1)/2;if(rzF(cx,cy,1)+rzF(x0,y0,1)+rzF(x1,y1,1)+rzF(x0,y1,1)+rzF(x1,y0,1)>0)layer(maskA((x,y)=>rzF(x,y,1)),'rgba(4,26,80,.45)');
  if(rzF(cx,cy,2)+rzF(x0,y0,2)+rzF(x1,y1,2)+rzF(x0,y1,2)+rzF(x1,y0,2)>0){layer(maskA((x,y)=>rzF(x,y,2)),'rgba(72,226,214,.62)');
   g.save();g.scale(K,K);g.translate(-x0,-y0);const qq=rng(777+i*13+j*71);for(let k=0;k<90;k++){const x=x0+qq()*CW,y=y0+qq()*CH;if(rmV(x,y)!==0||rzF(x,y,2)<.6)continue;g.fillStyle=qq()<.5?'rgba(255,250,220,.18)':'rgba(255,255,255,.12)';g.beginPath();g.ellipse(x,y,6+qq()*16,3+qq()*6,qq()*3,0,TAU);g.fill();}
   for(const b of RSPOTS.sb||[]){if(b[0]+b[2]<x0-20||b[0]-b[2]>x1+20||b[1]+b[2]<y0-20||b[1]-b[2]>y1+20)continue;g.save();g.translate(b[0],b[1]);g.rotate(b[4]);g.scale(1,b[3]/b[2]);const rg=g.createRadialGradient(0,0,4,0,0,b[2]);rg.addColorStop(0,'rgba(250,236,190,.85)');rg.addColorStop(.7,'rgba(240,226,180,.55)');rg.addColorStop(1,'rgba(240,226,180,0)');g.fillStyle=rg;g.beginPath();g.arc(0,0,b[2],0,TAU);g.fill();g.restore();}
   g.restore();}}""")
# pueblo: más pisos y fachadas de colores
rep("const flat=r>.72,big=r>.9&&(v===4||v===1);","const town=rzF(cx,cy,3)>.5,flat=town?r>.4:r>.72,big=town?r>.62:r>.9&&(v===4||v===1);")
rep("else if(flat){g.fillStyle='#f1eee7';","else if(flat){g.fillStyle=town?['#f1eee7','#f4d9b0','#ecc9c1','#d9e4ea','#f7e7a8'][(r2*5)|0]:'#f1eee7';")
# minimapa con los colores de cada zona de agua
rep("id.data[k]=land?(v===2?240:v>=8?222:206):18;id.data[k+1]=land?(v===2?220:v>=8?218:190):92;id.data[k+2]=land?(v===2?170:v>=8?212:140):160;",
    "const zd=land?0:rzF(wx,wy,1),zt=land?0:rzF(wx,wy,2);id.data[k]=land?(v===2?240:v>=8?222:206):Math.round(18-8*zd+40*zt);id.data[k+1]=land?(v===2?220:v>=8?218:190):Math.round(92-40*zd+105*zt);id.data[k+2]=land?(v===2?170:v>=8?212:140):Math.round(160-30*zd+45*zt);")
# animales y cosas de cada zona
rep(" // olas en todas direcciones",""" // animales del lago
 const zoneIs=(x,y,k)=>rzF(x,y,k)>.6;
 for(let n=0,t=0;n<4&&t<3000;t++){const x=rx(),y=ry();if(!free(x,y,220)||inLane(x,y,100))continue;const sz=3+(n%2);M.push({t:'pgpod',x,y,h:r()*TAU,sp:80+r()*20,n:sz,ph:r()*6,fol:0,cd:0,vx:0,vy:0,flash:0});n++;}
 for(let n=0,t=0;n<6&&t<3000;t++){const x=rx(),y=ry();if(!free(x,y,140)||inLane(x,y,60)||zoneIs(x,y,2))continue;for(let k=0;k<4;k++)O.push({t:'jelly',x:x+(r()-.5)*120,y:y+(r()-.5)*120,ph:r()*6,hit:0});n++;}
 for(let n=0,t=0;n<14&&t<3000;t++){const x=rx(),y=ry();if(!free(x,y,70)||inLane(x,y,40))continue;O.push({t:'turtle',x,y,rot:r()*TAU,ph:r()*6});n++;}
 for(let n=0,t=0;n<9&&t<4000;t++){const x=rx(),y=ry();if(!zoneIs(x,y,2)||!free(x,y,60))continue;M.push({t:'pgray',x,y,h:r()*TAU,fl:r()*6,vx:0,vy:0,flash:0});n++;}
 if(RSPOTS&&RSPOTS.pigb){const[px,py,pr]=RSPOTS.pigb;for(let k=0;k<6;k++){const a=k/6*TAU+.3,x=px+Math.cos(a)*(pr+26),y=py+Math.sin(a)*(pr+22);if(!rmLand(x,y))O.push({t:'pig',x,y,ph:k*1.3});}O.push({t:'pglabel',x:px,y:py-pr-40,txt:'PIG BEACH',sub:'CERDOS NADADORES'});}
 for(const c of (RSPOTS&&RSPOTS.cays)||[]){O.push({t:'bpalm',x:c[0]-c[2]*.3,y:c[1]-c[2]*.15});O.push({t:'bpalm',x:c[0]+c[2]*.25,y:c[1]+c[2]*.2});}
 // olas grandes en el agua profunda
 for(let n=0,t=0;n<40&&t<4000;t++){const x=rx(),y=ry();if(!zoneIs(x,y,1)||inLane(x,y,220)||!free(x,y,150))continue;O.push({t:'fwave',x,y,a:r()*Math.PI,L:200+r()*170,ph:r()*6});n++;}
 // olas en todas direcciones""")
# movimiento de delfines y rayas; premio si sigues a los delfines; bancos de arena que frenan
rep("  else if(o.t==='npcjet'){","""  else if(o.t==='pgpod'||o.t==='pgray'){const sp=o.t==='pgpod'?o.sp:26,ah=o.t==='pgpod'?260:120;o.wt=(o.wt||0)-dt;if(o.wt<=0){o.wt=2+Math.random()*3;o.th=o.h+(Math.random()-.5)*1.6;}
   const ax=o.x+Math.sin(o.h)*ah,ay=o.y-Math.cos(o.h)*ah;if(rmLand(ax,ay)||ax<120||ax>RMW-120||ay<RM_TOP+500||ay>RM_BOT-200){const l=rmLand(o.x+Math.sin(o.h-.8)*ah,o.y-Math.cos(o.h-.8)*ah);o.th=o.h+(l?1.2:-1.2);}
   if(o.th!=null){let dh=o.th-o.h;while(dh>Math.PI)dh-=TAU;while(dh<-Math.PI)dh+=TAU;o.h+=clamp(dh,-1.2*dt,1.2*dt);}
   const nx=o.x+Math.sin(o.h)*sp*dt,ny=o.y-Math.cos(o.h)*sp*dt;if(!rmLand(nx,ny)){o.x=nx;o.y=ny;}else o.th=o.h+Math.PI;o.fl=(o.fl||0)+dt;
   if(o.t==='pgpod'&&!G.demo){if(o.cd>0)o.cd-=dt;const d=Math.hypot(P.x-o.x,P.y-o.y);
    if(o.cd<=0&&d<190&&P.v>50){if(o.fol===0)pop(P.x,P.y-50,'¡SÍGUELOS!','#33d6ff');o.fol+=dt;if(o.fol>=6){o.fol=0;o.cd=90;G.money+=300;G.score+=300;if(G.turbo<5){G.turbo++;turboUI();}Snd.cash();Snd.pickup();msg('¡AMIGO DE LOS DELFINES!','+300 PESETAS · +1 TURBO','var(--cyan)');}}
    else if(d>320)o.fol=0;}}
  else if(o.t==='npcjet'){""")
rep(" if(!G.demo)for(const o of Zn.big){if(o.t!=='pgbar'&&o.t!=='pggas')continue;",""" if(!G.demo&&P.z<.5){let inb=false;for(const b of RSPOTS.sb||[]){const dx=P.x-b[0],dy=P.y-b[1],c=Math.cos(b[4]),sn=Math.sin(b[4]),lx=dx*c+dy*sn,ly=-dx*sn+dy*c;if((lx/b[2])**2+(ly/b[3])**2<.8){inb=true;break;}}
  if(inb){if(P.v>P.st.maxV*.4)P.v*=1-1.8*dt;if(!G._sbk){G._sbk=1;pop(P.x,P.y-40,'¡BANCO DE ARENA!','#f4d27a');}}else G._sbk=0;}
 if(!G.demo)for(const o of Zn.big){if(o.t!=='pgbar'&&o.t!=='pggas')continue;""")
rep("case 'pgbar':{","""case 'pgpod':{for(let k=0;k<o.n;k++){const ox=(k%2?1:-1)*(k?18+k*6:0),oy=k*34,ca=Math.cos(o.h),sa=Math.sin(o.h),x=o.x+ox*ca-oy*sa,y=o.y+ox*sa+oy*ca;const pr=o._d||(o._d={t:'dolphin'});pr.x=0;pr.y=0;pr.flash=o.fl+k*.37+o.ph;ctx.save();ctx.translate(x,y);ctx.rotate(o.h);drawObj(pr);ctx.restore();}}return;
 case 'pgray':{const pr=o._d||(o._d={t:'ray'});pr.x=0;pr.y=0;pr.vx=1;pr.flash=o.fl;ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h-Math.PI/2);drawObj(pr);ctx.restore();}return;
 case 'pglabel':{ctx.save();ctx.translate(o.x,o.y);ctx.rotate(G.camA||0);label(0,0,o.txt,o.sub||'');ctx.restore();}return;
 case 'pgbar':{""")
rep("if(o.t==='bgirl'||o.t==='bpalm'||o.t==='faro'||o.t==='pgbar'||o.t==='pggas')continue;","if(o.t==='bgirl'||o.t==='bpalm'||o.t==='faro'||o.t==='pgbar'||o.t==='pggas'||o.t==='pglabel'||o.t==='turtle'||o.t==='pig')continue;")
rep("const APP_VER=104;","const APP_VER=105;")
open(p,'w').write(s);print('ok',len(s))
