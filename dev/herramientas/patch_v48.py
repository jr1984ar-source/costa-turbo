p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
W={'EL PUERTO':"['#139aa6','#0b6888']",'LA CALA':"['#10bccf','#0a86b6']",'CARRERA AL MAGO':"['#19c2d6','#0c8fc2']",'GRAN CARRERA':"['#2ccbe0','#1396c9']",
 'PERSECUCIÓN':"['#1572c6','#0c4898']",'OLAS GIGANTES':"['#1a63a4','#0e3d74']",'CARRERA ES TRENC':"['#1fd0df','#0c9ad2']",'CARRERA SAN TELM':"['#15b0c4','#0b78a9']",
 'FORMENTOR':"['#0f5ea9','#0a3b7b']",'SA CALOBRA':"['#12ab9c','#0a7b88']",'CABRERA':"['#1268ca','#0a3f9a']",'PORTALS':"['#18b2bf','#0d7d9e']",
 'FORMENTERA':"['#7eeaea','#38c6e2'],crystal:1",'BAHAMAS':"['#8af0f2','#40cdea'],crystal:1",'AUSTRALIA':"['#45c6ee','#1f97da']",'ES VEDRÀ':"['#1d84b6','#22508e']"}
i=s.find('const ZONES=[');j=s.find('];',i);Z=s[i:j]
for nm,w in W.items():
    a="{name:'"+nm+"',";assert Z.count(a)==1,nm
    Z=Z.replace(a,a+"water:"+w+",")
s=s[:i]+Z+s[j:]
rep("gr.addColorStop(0,T.deep);gr.addColorStop(1,T.deep2);ctx.fillStyle=gr;ctx.fillRect(camX-20,camTop-20,VW+40,VH+40);\n",
    """gr.addColorStop(0,Zn.Z.water?Zn.Z.water[0]:T.deep);gr.addColorStop(1,Zn.Z.water?Zn.Z.water[1]:T.deep2);ctx.fillStyle=gr;ctx.fillRect(camX-20,camTop-20,VW+40,VH+40);
 if(Zn.Z.crystal){const sp=sandTile(),t2=256;ctx.save();ctx.globalAlpha=.6;for(let y=Math.floor(camTop/t2)*t2;y<camTop+VH;y+=t2)for(let x=Math.floor(camX/t2)*t2;x<camX+VW;x+=t2)ctx.drawImage(sp.c,x,y,t2,t2);ctx.globalAlpha=1;
  for(let cy=Math.floor(camTop/150)-1;cy<=Math.floor((camTop+VH)/150);cy++)for(let cx=Math.floor(camX/150)-1;cx<=Math.floor((camX+VW)/150);cx++){const h=hash2(cx,cy,Zn.seed+9);if(h>.2)continue;const x=cx*150+hash2(cy,cx,3)*150,y=cy*150+hash2(cx,cy,5)*150,rr=16+hash2(cx,cy,7)*30;ctx.fillStyle=h<.07?'rgba(80,95,90,.2)':'rgba(40,120,80,.17)';ctx.beginPath();for(let k=0;k<10;k++){const a=k/10*TAU,q=rr*(.7+.3*hash2(cx*10+k,cy,11));k?ctx.lineTo(x+Math.cos(a)*q,y+Math.sin(a)*q*.75):ctx.moveTo(x+Math.cos(a)*q,y+Math.sin(a)*q*.75);}ctx.closePath();ctx.fill();}
  ctx.restore();}
""")
rep("function drawGiant(o){","""function sandTile(){return cspr('sand',256,256,g=>{const q=rng(4242);g.fillStyle='rgba(250,240,205,.5)';g.fillRect(-128,-128,256,256);
 for(let i=0;i<16;i++){const y0=-128+i*16;for(const dy of[-256,0,256]){g.strokeStyle=i%2?'rgba(255,255,240,.6)':'rgba(205,185,135,.38)';g.lineWidth=i%2?1.8:2.4;g.beginPath();for(let x=-132;x<=132;x+=8){const y=y0+dy+Math.sin((x+128)/256*TAU*2+i*.7)*5+Math.sin((x+128)/256*TAU*5+i)*1.6;x===-132?g.moveTo(x,y):g.lineTo(x,y);}g.stroke();}}
 for(let i=0;i<180;i++){g.fillStyle=q()<.5?'rgba(255,255,255,.55)':'rgba(190,170,120,.35)';g.fillRect(-128+q()*256,-128+q()*256,1.3,1.3);}});}
function drawGiant(o){""")
rep("const APP_VER=47;","const APP_VER=48;")
open(p,'w').write(s);print('ok')
s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
rep("function hurt(c,v0){if(G.demo||G.mode!=='play'||!(v0>c.st.maxV*.25))return;setHp(hpTot()-1);const L=$('#lives');L.classList.remove('hit');void L.offsetWidth;L.classList.add('hit');",
    "function heartBlink(){const L=$('#lives'),el=L.children[G.dmg?G.lives-1:G.lives];if(el){el.classList.remove('blink');void el.offsetWidth;el.classList.add('blink');}}\nfunction hurt(c,v0){if(G.demo||G.mode!=='play'||!(v0>c.st.maxV*.25))return;setHp(hpTot()-1);heartBlink();")
rep(" if(!G.dmg)msg('¡CORAZÓN PERDIDO!','Te queda'+(hpTot()>3?'n ':' ')+hpTxt(),'var(--red)');else pop(c.x,c.y-54,'−⅓ ♥','#ff4757');}","}")
rep("if(c.isP&&!G.demo&&G.mode==='play'){setHp(hpTot()-2);const L=$('#lives');L.classList.remove('hit');void L.offsetWidth;L.classList.add('hit');",
    "if(c.isP&&!G.demo&&G.mode==='play'){setHp(hpTot()-2);heartBlink();")
rep("@keyframes lvHit{0%{transform:scale(1.35)}100%{transform:scale(1)}}",
    "@keyframes lvHit{0%{transform:scale(1.35)}100%{transform:scale(1)}}\n.lives i.blink{animation:hBlink 1.1s linear 1}\n@keyframes hBlink{0%,18%,36%,54%,72%{opacity:.08}9%,27%,45%,63%,81%,100%{opacity:1}}")
open(p,'w').write(s);print('ok2')
