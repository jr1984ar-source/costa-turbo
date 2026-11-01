p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
# ---- textos que se puedan leer ----
rep("function pop(x,y,txt,col){G.pops.push({x,y,txt,col:col||'#fff',life:1.1});}",
    "function pop(x,y,txt,col){const P=G.P;let f=null;if(P&&Math.hypot(x-P.x,y-P.y)<140){const n=G.pops.filter(q=>q.f&&q.life>.45).length;f={dx:0,dy:Math.min(-34,y-P.y)-n*22};}G.pops.push({x,y,txt,col:col||'#fff',life:2.2,max:2.2,f});}")
rep("""ctx.font='800 16px "Saira Condensed",sans-serif';ctx.lineWidth=3;ctx.strokeStyle='rgba(0,20,50,.55)';
 for(const p of G.pops){const a=clamp(p.life*1.6,0,1);ctx.globalAlpha=a;const y=p.y-(1.1-p.life)*26;if(CIRC){ctx.save();ctx.translate(p.x,p.y);ctx.rotate(G.camA||0);ctx.translate(0,-(1.1-p.life)*26);ctx.strokeText(p.txt,0,0);ctx.fillStyle=p.col;ctx.fillText(p.txt,0,0);ctx.restore();}else{ctx.strokeText(p.txt,p.x,y);ctx.fillStyle=p.col;ctx.fillText(p.txt,p.x,y);}}ctx.globalAlpha=1;""",
    """ctx.font='800 20px "Saira Condensed",sans-serif';ctx.lineWidth=4;ctx.lineJoin='round';ctx.strokeStyle='rgba(0,20,50,.6)';
 for(const p of G.pops){const a=clamp(p.life/.5,0,1),rise=((p.max||1.1)-p.life)*12,P=G.P,fo=p.f&&P;ctx.globalAlpha=a;const px=fo?P.x+p.f.dx:p.x,py=fo?P.y:p.y,oy=(fo?p.f.dy:0)-rise;
  if(CIRC){ctx.save();ctx.translate(px,py);ctx.rotate(G.camA||0);ctx.translate(0,oy);ctx.strokeText(p.txt,0,0);ctx.fillStyle=p.col;ctx.fillText(p.txt,0,0);ctx.restore();}else{const hw2=ctx.measureText(p.txt).width/2+6,cx=MIR?px:clamp(px,camX+hw2,camX+VW-hw2);ctx.strokeText(p.txt,cx,py+oy);ctx.fillStyle=p.col;ctx.fillText(p.txt,cx,py+oy);}}ctx.globalAlpha=1;""")
rep("msgTO=setTimeout(()=>m.hidden=true,1600);}","msgTO=setTimeout(()=>m.hidden=true,2600);}")
rep("#msg.go{animation:pop 1.6s ease-out both}","#msg.go{animation:pop 2.6s ease-out both}")
# ---- rampas de tamaños y de medio lado ----
rep("case 'ramp':{if(o.kick){const w=o.w,Lr=o.mega?92:52;","case 'ramp':{if(o.kick){const w=o.w,Lr=o.mega?92:(o.Lr||52);")
rep("ctx.fillStyle='#ff7a1a';for(let k=-w-Lr;k<w;k+=24){","ctx.fillStyle=o.col||'#ff7a1a';for(let k=-w-Lr;k<w;k+=24){")
rep(" case 'cramp':{ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);drawObj({t:'ramp',x:0,y:0,w:o.w,kick:1});ctx.restore();}return;",
    " case 'cramp':{ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.h);drawObj({t:'ramp',x:0,y:0,w:o.w,kick:1,Lr:o.Lr,col:o.col});if(o.defl){const L2=o.Lr||52;ctx.fillStyle='rgba(255,255,255,.95)';ctx.strokeStyle='#13285e';ctx.lineWidth=2;ctx.beginPath();ctx.moveTo(0,L2*.14);ctx.lineTo(13,L2*.58);ctx.lineTo(5,L2*.58);ctx.lineTo(5,L2*.9);ctx.lineTo(-5,L2*.9);ctx.lineTo(-5,L2*.58);ctx.lineTo(-13,L2*.58);ctx.closePath();ctx.stroke();ctx.fill();}ctx.restore();}return;")
rep("&&Math.abs(lt)<o.w/2&&c.air<=0&&c.v>110&&c.crash<=0){startJump(c);if(c.isP&&!G.demo){const b=100+Math.round(c.v/4);G.score+=b;pop(c.x,c.y-40,'¡SALTO! +'+b,'#ffc93c');}}continue;}",
    "&&Math.abs(lt)<o.w/2&&c.air<=0&&c.v>110&&c.crash<=0){startJump(c);if(o.sz){const kf=o.sz==='s'?.7:o.sz==='l'?1.45:1;c.airT*=kf;c.air=c.airT;}if(o.defl){c.h=o.h;c.va=o.h;}if(c.isP&&!G.demo){const b=(o.sz==='s'?100:o.sz==='l'?400:o.sz==='m'?200:100)+Math.round(c.v/4);G.score+=b;pop(c.x,c.y-40,(o.defl?'¡SALTO DE LADO! +':o.sz==='l'?'¡GRAN SALTO! +':'¡SALTO! +')+b,o.sz==='l'?'#ff6b7d':'#ffc93c');}}continue;}")
rep("startJump(c);if(o.mega){c.airT*=1.8;c.air=c.airT;}if(c.isP&&!G.demo){const b=(o.mega?600:100)+Math.round(c.v/4);G.score+=b;pop(c.x,c.y-40,(o.mega?'¡MEGA SALTO! +':'¡SALTO! +')+b,o.mega?'#33d6ff':'#ffc93c');",
    "startJump(c);if(o.mega){c.airT*=1.8;c.air=c.airT;}else if(o.sz){const kf=o.sz==='s'?.7:o.sz==='l'?1.45:1;c.airT*=kf;c.air=c.airT;}if(c.isP&&!G.demo){const b=(o.mega?600:o.sz==='s'?100:o.sz==='l'?400:o.sz==='m'?200:100)+Math.round(c.v/4);G.score+=b;pop(c.x,c.y-40,(o.mega?'¡MEGA SALTO! +':o.sz==='l'?'¡GRAN SALTO! +':'¡SALTO! +')+b,o.mega?'#33d6ff':o.sz==='l'?'#ff6b7d':'#ffc93c');")
i=s.find("if(Z.ramps){u=len;");j=s.find("   if(r()<.14)add({t:'fuel',x:lerp(L+20,R-20,r()),y:-u2+70});u2+=130+r()*90;}",i);assert 0<i<j
s=s[:i]+"""if(Z.ramps){u=len;let u2=650,pat=0;const SZ={s:{w:80,Lr:36,col:'#ffd21a'},m:{w:100,Lr:52,col:'#ff7a1a'},l:{w:124,Lr:72,col:'#e3202b'}};
  const ramp=(x,uu,sz)=>add({t:'ramp',x,y:-uu,w:SZ[sz].w,Lr:SZ[sz].Lr,col:SZ[sz].col,sz,kick:1}),air=(x,uu,n,sp)=>{for(let i=0;i<(n||4);i++)add({t:'coin',x,y:-uu-64-i*(sp||28),air:1});};
  const side=(x,uu,dir,sz)=>{const h=dir*.5;add({t:'cramp',x,y:-uu,h,w:SZ[sz].w,Lr:SZ[sz].Lr,col:SZ[sz].col,sz,kick:1,defl:1});for(let i=0;i<4;i++){const d=84+i*36;add({t:'coin',x:x+Math.sin(h)*d,y:-uu-Math.cos(h)*d,air:1});}},szr=()=>['s','m','l'][(r()*3)|0];
  while(u2<len-800){const L=zone.shore(-u2)+40,R=WG-40,mid=(L+R)/2,k=pat++%7;
   if(k===0){const x=[L+66,mid,R-66][(r()*3)|0],sz=szr();ramp(x,u2,sz);air(x,u2,sz==='l'?6:4,sz==='l'?34:28);u2+=sz==='l'?520:430;}
   else if(k===1){for(let i=0;i<3;i++)ramp(i%2?R-66:L+66,u2+i*260,'s');u2+=880;}
   else if(k===2){const x=lerp(L+80,R-80,r());ramp(x,u2,'l');add({t:r()<.6?'sail':'motor',x,y:-u2-160,rot:0});air(x,u2+40,5,34);u2+=640;}
   else if(k===3){const left=r()<.5;side(left?L+72:R-72,u2,left?1:-1,'m');u2+=560;}
   else if(k===4){const sw=r()<.5;ramp(sw?R-74:L+70,u2,'s');ramp(sw?L+74:R-74,u2,'l');air(sw?L+74:R-74,u2,5,32);u2+=540;}
   else if(k===6){side(L+72,u2,1,'s');side(R-72,u2+430,-1,'m');u2+=920;}
"""+s[i+s[i:].find("   else{for(let i=0;i<3;i++)add({t:'rock'"):]
rep("goal:'Haz 10 saltos de rampa y llega antes de que se acabe el tiempo. Mar abierto, sin costa.'",
    "goal:'Haz 10 saltos de rampa y llega antes de que se acabe el tiempo. Mar abierto, sin costa. Rampas amarillas (pequeñas), naranjas y rojas (saltos enormes), y algunas de lado que te lanzan en diagonal.'")
rep("const APP_VER=49;","const APP_VER=50;")
open(p,'w').write(s);print('ok')
