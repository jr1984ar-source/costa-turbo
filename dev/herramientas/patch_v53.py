p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
i=s.find("if(Z.ramps){u=len;");j=s.find("  const mu=len-560;",i);assert 0<i<j
s=s[:i]+"""if(Z.ramps){u=len;let u2=650,pat=0;const SZ={s:{w:80,Lr:36,col:'#ffd21a'},m:{w:100,Lr:52,col:'#ff7a1a'},l:{w:124,Lr:72,col:'#e3202b'}},RD=RAMP_D;
  const gap=sz=>Math.round(RD[sz]*1.3+140);
  const ramp=(x,uu,sz)=>add({t:'ramp',x,y:-uu,w:SZ[sz].w,Lr:SZ[sz].Lr,col:SZ[sz].col,sz,kick:1}),air=(x,uu,sz)=>{const n=sz==='l'?6:sz==='m'?5:4;for(let i=0;i<n;i++)add({t:'coin',x,y:-uu-RD[sz]*(.2+.6*i/(n-1)),air:1});},szr=()=>['s','m','l'][(r()*3)|0];
  while(u2<len-900){const L=zone.shore(-u2)+40,R=WG-40,mid=(L+R)/2,k=pat++%7;
   if(k===0){const x=[L+66,mid,R-66][(r()*3)|0],sz=szr();ramp(x,u2,sz);air(x,u2,sz);u2+=gap(sz);}
   else if(k===1){let uu=u2;for(let i=0;i<3;i++){const x=i%2?R-66:L+66;ramp(x,uu,'s');air(x,uu,'s');uu+=gap('s');}u2=uu;}
   else if(k===2){const x=lerp(L+80,R-80,r());ramp(x,u2,'l');add({t:r()<.6?'sail':'motor',x,y:-u2-170,rot:0});air(x,u2,'l');u2+=gap('l');}
   else if(k===3){const x=lerp(L+70,R-70,r());ramp(x,u2,'m');air(x,u2,'m');const u3=u2+gap('m');ramp(x,u3,'s');air(x,u3,'s');u2=u3+gap('s');}
   else if(k===4){const sw=r()<.5,xs=sw?R-74:L+70,xl=sw?L+74:R-74;ramp(xs,u2,'s');ramp(xl,u2,'l');air(xl,u2,'l');air(xs,u2,'s');u2+=gap('l');}
   else if(k===6){ramp(L+70,u2,'m');air(L+70,u2,'m');const u3=u2+gap('m');ramp(R-70,u3,'m');air(R-70,u3,'m');const u4=u3+gap('m');ramp(mid,u4,'l');air(mid,u4,'l');u2=u4+gap('l');}
   else{for(let i=0;i<3;i++)add({t:'rock',x:lerp(L+20,R-20,r()),y:-u2-(r()-.5)*60,rad:10+r()*7,v:(r()*3)|0});const x=lerp(L+60,R-60,r());for(let i=0;i<6;i++)add({t:'coin',x:clamp(x+Math.sin(i*.8)*30,L,R),y:-u2-90-i*28});u2+=400;}
   if(r()<.14)add({t:'fuel',x:lerp(L+20,R-20,r()),y:-u2+70});u2+=60+r()*80;}
"""+s[j:]
# limpiar la zona de caída de todas las rampas (todas las pantallas)
rep(" // remove objects colliding with checks/finish band",""" {const OB={rock:1,sail:1,motor:1,kayak:1,yacht:1,patrol:1,turtle:1,pig:1,surfer:1,croc:1,coral:1,float:1};
  for(const rp of O.filter(o=>o.t==='ramp')){const d=rp.mega?820:RAMP_D[rp.sz||'m'],u0=-rp.y,ww=(rp.w||100)/2+70;for(let i=O.length-1;i>=0;i--){const o=O[i];if(!OB[o.t])continue;const du=-o.y-u0;if(du>d*.5&&du<d*1.45&&Math.abs(o.x-rp.x)<ww+(o.t==='yacht'?40:0))O.splice(i,1);}}}
 // remove objects colliding with checks/finish band""")
rep("function startJump(c){","const RAMP_D={s:330,m:470,l:690};\nfunction startJump(c){")
rep("const APP_VER=52;","const APP_VER=53;")
open(p,'w').write(s);print('ok')
