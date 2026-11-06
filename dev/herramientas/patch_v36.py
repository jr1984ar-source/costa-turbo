p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)

rep("{name:'GRAN CARRERA',","{name:'GRAN CARRERA',alt:1,")
rep("{name:'TORMENTA',","{name:'TORMENTA',alt:1,")
rep(" if(Z.theme==='open'){shoreU=u=>-(VW>WG?(VW-WG)/2:0);kindU=u=>'open';}",""" if(Z.theme==='open'){shoreU=u=>-(VW>WG?(VW-WG)/2:0);kindU=u=>'open';}
 let altPres=null,altBase=null;if(Z.alt){const base=shoreU,n=5,sl=len/n;altBase=base;
  altPres=(u,want)=>{u=Math.max(0,u);const k=Math.min(n-1,Math.floor(u/sl));if((k%2)!==want)return 0;const din=k===0?1e9:u-k*sl,dout=k===n-1?1e9:(k+1)*sl-u;return Math.min(sm(0,420,din),sm(0,420,dout));};
  shoreU=u=>lerp(-90,base(u),altPres(u,0));}""")
rep("zone.rwall=null;if(Z.canyon){","zone.rwall=null;if(Z.alt){zone.rwall=y=>{const u=-y;return lerp((VW>WG?WG+(VW-WG)/2:WG)+600,(VW>WG?WG+(VW-WG)/2:WG)-altBase(u)*.92,altPres(u,1));};}\n if(Z.canyon){")
rep("if(Z.piri){let pu=Math.round(len*.3);while(isRes(pu)||Math.abs(pu-barU)<400)pu+=300;const L=zone.shore(-pu),x=lerp(L+60,RX-110,r());",
    "if(Z.piri){let pu=Math.round(len*.3);while(isRes(pu)||Math.abs(pu-barU)<400)pu+=300;const L=Math.max(0,zone.shore(-pu)),x=lerp(L+60,Math.min(RX,zone.rwall?zone.rwall(-pu):RX)-110,r());")
rep("const L=zone.shore(-u)+36,R=Math.min(WG-24,zone.rwall?zone.rwall(-u)-30:999);let k=pick();","const L=Math.max(24,zone.shore(-u)+36),R=Math.min(WG-24,zone.rwall?zone.rwall(-u)-30:999);let k=pick();")
rep("function aiCtl(c,dt){const Zn=G.zone,L=Zn.shore(c.y-120)+30,","function aiCtl(c,dt){const Zn=G.zone,L=Math.max((VW>WG?-(VW-WG)/2:0)+30,Zn.shore(c.y-120)+30),")
rep("if(Zn.rwall){const rw=Zn.rwall(c.y)-11;","{const lx=(VW>WG?-(VW-WG)/2:0)+11;if(c.x<lx){c.x=lx;if(c.h<0)c.h=Math.abs(c.h)*.4;c.va=c.h;c.v*=1-3*dt;}}\n if(Zn.rwall){const rw=Zn.rwall(c.y)-11;")
# estilo de la costa derecha según el tema
rep(" if(Zn.rwall){const xr=(VW>WG?WG+(VW-WG)/2:WG)+40,y0=camTop-20,y1=camTop+VH+20;"," if(Zn.rwall){const xr=(VW>WG?WG+(VW-WG)/2:WG)+40,y0=camTop-20,y1=camTop+VH+20,RS=Zn.Z.theme==='beach'?'sand':Zn.Z.theme==='cove'?'red':'rock';")
rep("const gg=ctx.createLinearGradient(x-60,0,x,0);gg.addColorStop(0,'rgba(8,24,40,0)');gg.addColorStop(1,'rgba(8,24,40,.45)');ctx.fillStyle=gg;ctx.fillRect(x-60,y,61,6.5);}",
    "const gg=ctx.createLinearGradient(x-(RS==='sand'?120:60),0,x,0);if(RS==='sand'){gg.addColorStop(0,'rgba(30,160,210,0)');gg.addColorStop(.7,'rgba(70,205,215,.6)');gg.addColorStop(1,'rgba(140,240,225,.9)');}else{gg.addColorStop(0,'rgba(8,24,40,0)');gg.addColorStop(1,'rgba(8,24,40,.45)');}ctx.fillStyle=gg;ctx.fillRect(x-(RS==='sand'?120:60),y,(RS==='sand'?121:61),6.5);}")
rep("ctx.lineTo(xr,y1);ctx.closePath();const rg=ctx.createLinearGradient(0,0,80,0);ctx.fillStyle='#8c877d';ctx.fill();ctx.clip();",
    "ctx.lineTo(xr,y1);ctx.closePath();ctx.fillStyle=RS==='sand'?'#f1d9a6':RS==='red'?'#c47a44':'#8c877d';ctx.fill();ctx.clip();")
rep("ctx.fillStyle=['#a39e93','#7d786e','#b8b3a8','#6b665d','#948f84'][(hash2(cy,k,7)*5)|0];ctx.globalAlpha=.85;ctx.beginPath();ctx.ellipse(x,y,sz,sz*.6,hash2(k,cy,9)*3,0,TAU);ctx.fill();}",
    "if(RS==='sand'){ctx.fillStyle=hash2(cy,k,7)>.5?'rgba(180,140,80,.3)':'rgba(255,255,255,.4)';ctx.fillRect(x,y,1.4,1.4);continue;}ctx.fillStyle=(RS==='red'?['#d98f57','#b9693a','#e7a46b','#a75d31','#cf8650']:['#a39e93','#7d786e','#b8b3a8','#6b665d','#948f84'])[(hash2(cy,k,7)*5)|0];ctx.globalAlpha=.85;ctx.beginPath();ctx.ellipse(x,y,sz,sz*.6,hash2(k,cy,9)*3,0,TAU);ctx.fill();}")
rep("ctx.globalAlpha=1;for(let y=Math.floor(y0/5)*5;y<y1;y+=5){const x=Zn.rwall(y);const gg=ctx.createLinearGradient(x,0,x+26,0);",
    "ctx.globalAlpha=1;if(RS!=='sand')for(let y=Math.floor(y0/5)*5;y<y1;y+=5){const x=Zn.rwall(y);const gg=ctx.createLinearGradient(x,0,x+26,0);")
rep("for(let cy=Math.floor(y0/40);cy<=Math.floor(y1/40);cy++){const h=hash2(cy,11,Zn.seed);if(h<.5)continue;const x=Zn.rwall(cy*40)+30+h*70,y=cy*40;ctx.fillStyle=h>.75?'#2f5a26':'#3f7f35';ctx.beginPath();ctx.arc(x,y,4+h*4,0,TAU);ctx.fill();}",
    "for(let cy=Math.floor(y0/40);cy<=Math.floor(y1/40);cy++){const h=hash2(cy,11,Zn.seed);if(h<.5)continue;const x=Zn.rwall(cy*40)+(RS==='sand'?16:30)+h*70,y=cy*40;if(RS==='sand'&&h<.8){ctx.fillStyle=['#ffffff','#ff4f6b','#33a3ff','#ffd21a'][(h*40|0)%4];ctx.beginPath();ctx.arc(x,y,7,0,TAU);ctx.fill();ctx.strokeStyle='rgba(0,0,0,.12)';ctx.lineWidth=.8;for(let a=0;a<6;a++){ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x+Math.cos(a)*7,y+Math.sin(a)*7);ctx.stroke();}continue;}ctx.fillStyle=h>.75?'#2f5a26':'#3f7f35';ctx.beginPath();ctx.arc(x,y,4+h*4,0,TAU);ctx.fill();}")
rep("const APP_VER=35;","const APP_VER=36;")
open(p,'w').write(s);print('ok')
