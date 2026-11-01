p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
# hueco en cada ola
rep("zone.waves=[];if(Z.giant){for(const f of(Array.isArray(Z.giant)?Z.giant:[.2,.34,.48,.62,.85,.88,.91])){const cu=Math.round(len*f);zone.waves.push({y:-cu,act:0,side:1,done:0,sp:44+r()*16,ph:r()*6,fade:1});",
    "zone.waves=[];if(Z.giant){const rg=rng(seed+55);let lastG=null;for(const f of(Array.isArray(Z.giant)?Z.giant:[.2,.34,.48,.62,.85,.88,.91])){const cu=Math.round(len*f),gL=Math.max(20,zone.shore(-cu))+60,gR=(zone.rwall?zone.rwall(-cu):WG)-60;let gx=lerp(gL,gR,rg());for(let k=0;k<8&&lastG!=null&&Math.abs(gx-lastG)<70;k++)gx=lerp(gL,gR,rg());lastG=gx;zone.waves.push({y:-cu,act:0,side:1,done:0,sp:44+r()*16,ph:r()*6,fade:1,gx,gw:44});")
rep("if(o.act&&o.side>0&&side<0){o.done=1;giantHit(P);}","if(o.act&&o.side>0&&side<0){o.done=1;giantHit(P,o);}")
rep("function giantHit(c){if(c.air>0||c.z>.5)return;",
    "function giantHit(c,o){if(c.air>0||c.z>.5)return;\n if(o&&o.gw&&Math.abs(c.x-o.gx)<=o.gw/2-9){if(c.isP&&!G.demo){const b=300;G.score+=b;Snd.gate();pop(c.x,c.y-46,'¡POR EL HUECO! +'+b,'#7be35a');splash(c.x,c.y,14,120);}return;}")
# dibujo en dos trozos con el hueco
i=s.find("function drawGiant(o){");j=s.find("\nfunction ",i+10);assert 0<i<j
s=s[:i]+"""function drawGiant(o){const X0=G.zone.shore(o.y)-6,X1=WG+(VW>WG?(VW-WG)/2:0)+30,y=o.y,t=G.t+o.ph;ctx.save();ctx.globalAlpha=o.fade;
 const segs=o.gw?[[X0,o.gx-o.gw/2],[o.gx+o.gw/2,X1]]:[[X0,X1]];
 if(o.gw){const a=o.gx-o.gw/2,b=o.gx+o.gw/2;let g=ctx.createLinearGradient(0,y-60,0,y+40);g.addColorStop(0,'rgba(160,245,248,0)');g.addColorStop(.6,'rgba(160,245,248,.35)');g.addColorStop(1,'rgba(160,245,248,0)');ctx.fillStyle=g;ctx.fillRect(a,y-60,b-a,100);
  ctx.strokeStyle='rgba(255,255,255,.55)';ctx.lineWidth=1.4;for(let k=0;k<3;k++){const yy=y-26+k*16+((t*30)%16);ctx.beginPath();ctx.moveTo(a+8,yy);ctx.quadraticCurveTo(o.gx,yy-4,b-8,yy);ctx.stroke();}}
 for(const[x0,x1]of segs){if(x1-x0<4)continue;const wd=x1-x0;
  let g=ctx.createLinearGradient(0,y-100,0,y);g.addColorStop(0,'rgba(120,230,240,0)');g.addColorStop(1,'rgba(160,245,248,.6)');ctx.fillStyle=g;ctx.fillRect(x0,y-100,wd,100);
  g=ctx.createLinearGradient(0,y,0,y+78);g.addColorStop(0,'rgba(2,22,56,.8)');g.addColorStop(.45,'rgba(2,22,56,.35)');g.addColorStop(1,'rgba(2,22,56,0)');ctx.fillStyle=g;ctx.fillRect(x0,y,wd,78);
  ctx.strokeStyle='rgba(255,255,255,.2)';ctx.lineWidth=1.2;for(let x=x0;x<x1;x+=13){ctx.beginPath();ctx.moveTo(x,y+6);ctx.lineTo(x+5,y+30+Math.sin(x*.3+t*3)*5);ctx.stroke();}
  ctx.fillStyle='#ffffff';ctx.beginPath();ctx.moveTo(x0,y+7);for(let x=x0;x<=x1;x+=8)ctx.lineTo(x,y-7+Math.sin(x*.09+t*4)*3+Math.sin(x*.23-t*2)*2);ctx.lineTo(x1,y-7+Math.sin(x1*.09+t*4)*3);for(let x=x1;x>=x0;x-=8)ctx.lineTo(x,y+12+Math.sin(x*.13+t*3)*3);ctx.closePath();ctx.fill();
  const nf=Math.max(1,Math.round(wd/42));for(let i=0;i<nf;i++){const x=x0+(i+.5)*wd/nf+Math.sin(t+i)*Math.min(8,wd/8);ctx.fillStyle='rgba(255,255,255,.9)';ctx.beginPath();ctx.ellipse(x,y+16,Math.min(15,wd/3)+Math.sin(t*3+i)*3,7,0,0,TAU);ctx.fill();}
  const np=Math.round(46*wd/(X1-X0));for(let i=0;i<np;i++){const x=x0+((i*53.7+t*30)%wd),yy=y-6-((i*17+t*40)%26);ctx.fillStyle='rgba(255,255,255,.75)';ctx.beginPath();ctx.arc(x,yy,1.2+(i%3)*.7,0,TAU);ctx.fill();}
  if(o.gw){for(const ex of[x0,x1]){if(ex<=X0+1||ex>=X1-1)continue;ctx.fillStyle='#ffffff';ctx.beginPath();ctx.ellipse(ex,y+2,6+Math.sin(t*5+ex)*1.5,13,0,0,TAU);ctx.fill();for(let k=0;k<4;k++){ctx.fillStyle='rgba(255,255,255,.8)';ctx.beginPath();ctx.arc(ex+(ex===x0?1:-1)*(4+((t*20+k*7)%10)),y-8-k*4,1.4,0,TAU);ctx.fill();}}}}
 ctx.restore();}"""+s[j:]
rep("msg('¡OLA GIGANTE!','Rápido y recto o vuelcas (−⅔ ♥)','var(--cyan)')","msg('¡OLA GIGANTE!','Rápido y recto, o busca el hueco','var(--cyan)')")
rep("si vas lento o torcido, vuelcas y pierdes ⅔ de corazón.","si vas lento o torcido, vuelcas y pierdes ⅔ de corazón. Cada ola tiene un hueco muy estrecho por donde pasar sin saltar.")
rep("const APP_VER=45;","const APP_VER=46;")
open(p,'w').write(s);print('ok')
