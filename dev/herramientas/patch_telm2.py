import re
p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:80],s.count(a))
    s=s.replace(a,b)
# 1. shore: let + tram override (mountains with recovecos + rounded calas)
rep(" const shoreU=u=>{const k=Math.floor(u/SEG)"," let shoreU=u=>{const k=Math.floor(u/SEG)")
rep(" const kindU=u=>kindOf(Math.floor(u/SEG));",
""" let kindU=u=>kindOf(Math.floor(u/SEG));
 if(Z.theme==='tram'){const n3=noise1(seed+13),RC=230;
  const mtn=u=>{let x=Math.min(170,132+22*n1(u/240)+9*n2(u/70))+6*n3(u/22)+3.5*n2(u/9);const c=Math.floor(u/RC),hh=hash2(c,7,seed);if(hh>.4){const cu=c*RC+50+hash2(c,9,seed)*130,w=16+hash2(c,11,seed)*22,d=Math.abs(u-cu);if(d<w)x-=(24+hh*34)*(1-(d/w)*(d/w));}return x;};
  const cove=u=>{const k=Math.floor(u/SEG);if(k%2!==1)return null;const w=SEG*(.26+.12*hash2(k,3,seed)),c=k*SEG+SEG/2+(hash2(k,5,seed)-.5)*SEG*.2,d=Math.abs(u-c);return d<w?{q:1-(d/w)*(d/w),w,d}:null;};
  shoreU=u=>{let x=mtn(u);const cv=cove(u);if(cv){const fl=56+8*n1(u/90);x=lerp(x,Math.min(x,fl),Math.pow(cv.q,.42));}return x;};
  kindU=u=>{const cv=cove(u);return cv&&cv.d<cv.w*.86?'cala':'mount';};}""")
# 2. pines further from cliff edge on mount
rep("else if(kd==='mount'){const v=dr();if(v<.62)D.push({t:'pine',x:sx-22-dr()*110,","else if(kd==='mount'){const v=dr();if(v<.62)D.push({t:'pine',x:sx-34-dr()*115,")
# 3. bigger cast shadow on water
rep("if(Zn.kind(y)==='mount')g.drawImage(SP.cliffSh,sx-2,y,46,2.4);","if(Zn.kind(y)==='mount')g.drawImage(SP.cliffSh,sx-2,y,Zn.Z.theme==='tram'?72:46,2.4);")
# 4. darker cliff face band
rep("else{const gg=g.createLinearGradient(sx-40,0,sx,0);gg.addColorStop(0,'rgba(255,255,255,0)');gg.addColorStop(1,'rgba(30,25,20,.35)');g.fillStyle=gg;g.fillRect(sx-40,y,42,3.2);}}",
"else{const gg=g.createLinearGradient(sx-30,0,sx,0);gg.addColorStop(0,'rgba(28,24,20,0)');gg.addColorStop(.5,'rgba(28,24,20,.28)');gg.addColorStop(1,'rgba(28,24,20,.66)');g.fillStyle=gg;g.fillRect(sx-30,y,32,3.2);g.fillStyle='rgba(250,245,235,.22)';g.fillRect(sx-31,y,1.6,3.2);}}")
# 5. relief: lit peaks, shadows, gullies (before g.restore of land clip)
anchor=" g.restore();\n // promenade boardwalk + seawall"
rep(anchor,""" if(Zn.Z.theme==='tram'){
  for(let cy=Math.floor(y0/70)-2;cy<=Math.floor(y1/70)+2;cy++){const yy=cy*70+hash2(cy,1,Zn.seed)*40;if(Zn.kind(yy)!=='mount')continue;const sx=sh(yy),px=sx-64-hash2(cy,2,Zn.seed)*58,R=40+hash2(cy,3,Zn.seed)*30;
   let gg=g.createRadialGradient(px+16,yy+14,0,px+16,yy+14,R*1.15);gg.addColorStop(0,'rgba(30,25,20,.3)');gg.addColorStop(1,'rgba(30,25,20,0)');g.fillStyle=gg;g.fillRect(px+16-R*1.2,yy+14-R*1.2,R*2.4,R*2.4);
   gg=g.createRadialGradient(px-6,yy-6,0,px-6,yy-6,R);gg.addColorStop(0,'rgba(255,250,240,.34)');gg.addColorStop(1,'rgba(255,250,240,0)');g.fillStyle=gg;g.fillRect(px-6-R,yy-6-R,R*2,R*2);}
  for(let cy=Math.floor(y0/13)-9;cy<=Math.floor(y1/13)+9;cy++){const yy=cy*13+hash2(cy,4,Zn.seed)*7;if(Zn.kind(yy)!=='mount')continue;let x=sh(yy)-3,y=yy;const L=34+hash2(cy,5,Zn.seed)*96,dy=(hash2(cy,6,Zn.seed)-.5)*.9,pts=[[x,y]];for(let s=0;s<L;s+=6){x-=6;y+=dy*6+(hash2(cy,s,7)-.5)*5;pts.push([x,y]);}
   const ln=(ox,oy,c,w)=>{g.beginPath();pts.forEach(([a,b],i)=>i?g.lineTo(a+ox,b+oy):g.moveTo(a+ox,b+oy));g.strokeStyle=c;g.lineWidth=w;g.stroke();};ln(1.3,-1.1,'rgba(240,235,225,.32)',1);ln(0,0,'rgba(36,31,26,.45)',1.5);}}
"""+anchor)
open(p,'w').write(s);print('ok')
