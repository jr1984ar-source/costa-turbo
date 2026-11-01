p='costa-turbo.html';s=open(p,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:120])
    s=s.replace(a,b)
# zone
rep(" {name:'TORMENTA',obj:'time'"," {name:'CARRERA SAN TELM',obj:'race3',goal:'Termina entre los 3 primeros. Esta vez la costa queda a la derecha: calitas, recovecos y acantilados altísimos.',len:16000,riv:5,bar:null,theme:'tram',tod:'afternoon',skill:.9,piri:1,mirror:1,finish:'SAN TELM'},\n {name:'TORMENTA',obj:'time'")
rep("SEG=Z.theme==='port'?1500:Z.theme==='beach'?1700:Z.theme==='trenc'?2000:1900;","SEG=Z.theme==='port'?1500:Z.theme==='beach'?1700:Z.theme==='trenc'?2000:Z.theme==='tram'?900:1900;")
rep("const kindOf=k=>{k=Math.max(0,k);if(Z.theme==='trenc')return 'beach';","const kindOf=k=>{k=Math.max(0,k);if(Z.theme==='trenc')return 'beach';if(Z.theme==='tram')return k%3===1?'cala':'mount';")
rep("const raw=(kind,u)=>kind==='prom'?","const raw=(kind,u)=>kind==='mount'?Math.min(165,122+28*n1(u/220)+14*n2(u/60)):kind==='cala'?64+10*n1(u/200):kind==='prom'?")
rep("Z.floats?{coins:3,ramp:1.2,rocks:.6,boat:.6,yacht:1.2,kayak:.5,patrol:.6,float:3.4}:","Z.floats?{coins:3,ramp:1.2,rocks:.6,boat:.6,yacht:1.2,kayak:.5,patrol:.6,float:3.4}:Z.theme==='tram'?{coins:3.4,ramp:1.3,rocks:2.6,boat:1.3,yacht:.6,kayak:1,patrol:.6}:")
# decorations
rep("  else{const v=dr();if(v<.4)D.push({t:'pine',x:sx-16-dr()*60,y,r:10+dr()*9,s:(dr()*1e6)|0});}",
    "  else if(kd==='mount'){const v=dr();if(v<.62)D.push({t:'pine',x:sx-22-dr()*110,y,r:9+dr()*10,s:(dr()*1e6)|0});}\n  else if(kd==='cala'){const v=dr();if(v<.16)D.push({t:'llaut',x:sx+14+dr()*22,y,rot:(dr()-.5)*.8,c:['#1e5eff','#e3202b','#1f9e52','#ffd21a'][(dr()*4)|0]});else if(v<.26)D.push({t:'towel',x:sx-16-dr()*6,y,c:['#ff4f8b','#33d6ff','#ffd21a'][(dr()*3)|0]});else if(v<.6)D.push({t:'pine',x:sx-40-dr()*90,y,r:9+dr()*9,s:(dr()*1e6)|0});}\n  else{const v=dr();if(v<.4)D.push({t:'pine',x:sx-16-dr()*60,y,r:10+dr()*9,s:(dr()*1e6)|0});}")
rep(" else if(d.t==='girl'){"," else if(d.t==='llaut'){g.save();g.translate(d.x,d.y);g.rotate(d.rot);g.fillStyle='rgba(0,20,50,.25)';g.beginPath();g.ellipse(2,3,6,14,0,0,TAU);g.fill();g.fillStyle='#f4efe4';g.beginPath();g.moveTo(0,-14);g.quadraticCurveTo(7,-6,6,10);g.quadraticCurveTo(0,15,-6,10);g.quadraticCurveTo(-7,-6,0,-14);g.fill();g.strokeStyle=d.c;g.lineWidth=1.6;g.stroke();g.fillStyle='#a0703a';g.fillRect(-4,-4,8,9);g.fillStyle='#5e3a18';g.fillRect(-.6,-12,1.2,22);g.restore();}\n else if(d.t==='girl'){")
# terrain colors / textures / cliff shadow / pebbles
rep("g.fillStyle=kd==='prom'?'#ebe4d6':kd==='beach'?'#f1d9a6':'#c47a44';g.fillRect(x0-10,y,x1-x0+20,4.2);}",
    "g.fillStyle=kd==='prom'?'#ebe4d6':kd==='beach'?'#f1d9a6':kd==='mount'||kd==='cala'?'#8c877d':'#c47a44';g.fillRect(x0-10,y,x1-x0+20,4.2);}")
rep("  else if(kd==='cliff'){const cols=['#d98f57','#b9693a','#e7a46b','#a75d31','#cf8650'];",
    "  else if(kd==='mount'||kd==='cala'){const cols=['#a39e93','#7d786e','#b8b3a8','#6b665d','#948f84','#c4bfb3'];for(let k=0;k<4;k++){const hx=cx*24+hash2(cx,cy+k*31,Zn.seed)*24,hy=y+hash2(cx+k*17,cy,Zn.seed)*24,s=6+hash2(cx+k,cy+k,3)*11;g.fillStyle=cols[(hash2(cx,cy,k)*6)|0];g.globalAlpha=.9;g.beginPath();for(let q=0;q<5;q++){const a=q/5*TAU+hash2(cx+q,cy,k)*.5,d=s*(.6+hash2(cx,cy+q,k)*.5);q?g.lineTo(hx+Math.cos(a)*d,hy+Math.sin(a)*d*.6):g.moveTo(hx+Math.cos(a)*d,hy+Math.sin(a)*d*.6);}g.fill();g.globalAlpha=1;}\n   g.strokeStyle='rgba(40,35,30,.35)';g.lineWidth=1;for(let k=0;k<3;k++){const hx=cx*24+hash2(cx+5,cy+k,9)*24,hy=y+hash2(cx,cy+k,8)*24;g.beginPath();g.moveTo(hx,hy);g.lineTo(hx+7+hash2(cx,cy,k+4)*5,hy+2+hash2(cx+k,cy,3)*3);g.stroke();}}\n  else if(kd==='cliff'){const cols=['#d98f57','#b9693a','#e7a46b','#a75d31','#cf8650'];")
rep(" g.restore();\n // promenade boardwalk + seawall",
    " for(let y=y0-4;y<y1+4;y+=3){const kd=Zn.kind(y);if(kd!=='cala'&&kd!=='mount')continue;const sx=sh(y);if(kd==='cala'){g.fillStyle='#d9d3c6';g.fillRect(sx-24,y,26,3.2);g.fillStyle='rgba(120,110,95,.35)';for(let k=0;k<4;k++)g.fillRect(sx-24+hash2(Math.round(y),k,Zn.seed)*24,y+hash2(k,Math.round(y),3)*3,1.4,1.4);}else{const gg=g.createLinearGradient(sx-40,0,sx,0);gg.addColorStop(0,'rgba(255,255,255,0)');gg.addColorStop(1,'rgba(30,25,20,.35)');g.fillStyle=gg;g.fillRect(sx-40,y,42,3.2);}}\n g.restore();\n // promenade boardwalk + seawall")
rep("const shW=Zn.Z.shallowW||150;for(let y=y0-2;y<y1+2;y+=2){const sx=sh(y);g.drawImage(SP.shallow,sx-4,y,shW,2.4);}",
    "const shW=Zn.Z.shallowW||150;for(let y=y0-2;y<y1+2;y+=2){const sx=sh(y);g.drawImage(SP.shallow,sx-4,y,shW,2.4);if(Zn.kind(y)==='mount')g.drawImage(SP.cliffSh,sx-2,y,46,2.4);}")
rep(" SP.shallow=(()=>{"," SP.cliffSh=(()=>{const c=document.createElement('canvas');c.width=64;c.height=1;const g=c.getContext('2d'),gg=g.createLinearGradient(0,0,64,0);gg.addColorStop(0,'rgba(8,24,40,.55)');gg.addColorStop(1,'rgba(8,24,40,0)');g.fillStyle=gg;g.fillRect(0,0,64,1);return c;})();\n SP.shallow=(()=>{")
# mirror: input, render, text, police, night
rep(" const ctlP=G.demo?aiCtl(P,dt):{turn:(input.right?1:0)-(input.left?1:0),"," const ctlP=G.demo?aiCtl(P,dt):{turn:((input.right?1:0)-(input.left?1:0))*(Zn.Z.mirror?-1:1),")
rep(" ctx.setTransform(K,0,0,K,(-camX+sx)*K,(-camTop+sy)*K);\n // deep water",
    " const MIR=!!(Zn.Z.mirror&&!G.demo);if(MIR)ctx.setTransform(-K,0,0,K,(camX+VW+sx)*K,(-camTop+sy)*K);else ctx.setTransform(K,0,0,K,(-camX+sx)*K,(-camTop+sy)*K);mirText(MIR);\n // deep water")
rep(" // time of day\n ctx.setTransform(1,0,0,1,0,0);"," // time of day\n mirText(false);ctx.setTransform(1,0,0,1,0,0);")
rep("function label(x,y,t,s){","""const FT0=CanvasRenderingContext2D.prototype.fillText,ST0=CanvasRenderingContext2D.prototype.strokeText;
function mirText(on){if(on){ctx.fillText=function(t,x,y){this.save();this.translate(x,y);this.scale(-1,1);FT0.call(this,t,0,0);this.restore();};ctx.strokeText=function(t,x,y){this.save();this.translate(x,y);this.scale(-1,1);ST0.call(this,t,0,0);this.restore();};}else{delete ctx.fillText;delete ctx.strokeText;}}
function mflip(){if(G.zone&&G.zone.Z.mirror&&!G.demo)ctx.scale(-1,1);}
function label(x,y,t,s){""")
rep("ctx.save();ctx.translate(p.x,p.y);ctx.rotate(p.h);ctx.scale(.62,.62);ctx.drawImage(SP.police","ctx.save();ctx.translate(p.x,p.y);ctx.rotate(p.h);ctx.scale(.62,.62);mflip();ctx.drawImage(SP.police")
rep("ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.rot);ctx.drawImage(SP.police[((o.flash*3)|0)%2]","ctx.save();ctx.translate(o.x,o.y);ctx.rotate(o.rot);mflip();ctx.drawImage(SP.police[((o.flash*3)|0)%2]")
rep(" const k=K/2,P=G.P,px=(P.x-camX)*k,py=(P.y-camTop)*k;"," const k=K/2,P=G.P,MR=!!(G.zone.Z.mirror&&!G.demo),SX=x=>MR?camX+VW-x:x-camX,px=SX(P.x)*k,py=(P.y-camTop)*k;")
rep("g.save();g.translate(px,py);g.rotate(P.h);","g.save();g.translate(px,py);g.rotate(MR?-P.h:P.h);")
rep("for(const c of G.rivals)light((c.x-camX)*k,(c.y-camTop)*k,40*k,.6);for(const p of G.police)light((p.x-camX)*k,(p.y-camTop)*k,60*k,.7);","for(const c of G.rivals)light(SX(c.x)*k,(c.y-camTop)*k,40*k,.6);for(const p of G.police)light(SX(p.x)*k,(p.y-camTop)*k,60*k,.7);")
rep("if(G.zone.ring)light((G.zone.ring.x-camX)*k,(G.zone.ring.y-camTop)*k,80*k,.8);","if(G.zone.ring)light(SX(G.zone.ring.x)*k,(G.zone.ring.y-camTop)*k,80*k,.8);")
open(p,'w',encoding='utf-8').write(s)
print('ok')
