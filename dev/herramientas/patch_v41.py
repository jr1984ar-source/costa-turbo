p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
rep(""" g.restore();
 {const n=ZONES.length,lv=Math.max(1,Math.min(5,Math.ceil((zi+1)*5/n))),bx=12,by=H-26,sw=22,gap=4;""",""" g.restore();
 {const t=Z.circ?['CIRCUITO','#a77bff','#5b2bd6','loop']:Z.obj==='win'?['FINAL','#ffe27a','#d99a00','cup']:Z.obj==='time'?['CONTRARRELOJ','#4cc9ff','#0a6fd6','clock']:Z.obj==='slalom'?['SLALOM','#5be37f','#169a3e','zig']:Z.obj==='jumps'?['SALTOS','#ffe04a','#e0a000','ramp']:Z.obj==='chase'?['PERSECUCIÓN','#ff3b4f','#1e4fd8','siren']:['CARRERA','#ffa04a','#e2451a','flag'];
  g.save();g.font='800 17px "Saira Condensed",sans-serif';g.textBaseline='middle';g.textAlign='left';const tw=g.measureText(t[0]).width,bw=tw+44,bh=28,bx=W-12-bw,by=9;
  g.fillStyle='rgba(0,0,0,.32)';g.beginPath();g.roundRect(bx+2,by+3,bw,bh,14);g.fill();
  const lg=g.createLinearGradient(bx,by,t[3]==='siren'?bx+bw:bx,t[3]==='siren'?by:by+bh);lg.addColorStop(0,t[1]);lg.addColorStop(1,t[2]);g.fillStyle=lg;g.beginPath();g.roundRect(bx,by,bw,bh,14);g.fill();g.strokeStyle='rgba(255,255,255,.9)';g.lineWidth=1.8;g.stroke();
  const dark=t[3]==='ramp'||t[3]==='cup',ic=dark?'#3a2600':'#ffffff',ix=bx+17,iy=by+bh/2;g.strokeStyle=ic;g.fillStyle=ic;g.lineWidth=2.2;g.lineCap='round';g.lineJoin='round';
  if(t[3]==='loop'){const a1=-.6,a2=4.2;g.beginPath();g.arc(ix,iy,6.5,a1,a2);g.stroke();const px=ix+Math.cos(a2)*6.5,py=iy+Math.sin(a2)*6.5,tx=-Math.sin(a2),ty=Math.cos(a2),nx=Math.cos(a2),ny=Math.sin(a2);g.beginPath();g.moveTo(px+tx*4,py+ty*4);g.lineTo(px+nx*3.6-tx,py+ny*3.6-ty);g.lineTo(px-nx*3.6-tx,py-ny*3.6-ty);g.closePath();g.fill();}
  else if(t[3]==='flag'){g.beginPath();g.moveTo(ix-6,iy+8);g.lineTo(ix-6,iy-8);g.stroke();for(let r=0;r<3;r++)for(let c=0;c<4;c++){g.fillStyle=(r+c)%2?'#0a1630':'#ffffff';g.fillRect(ix-5+c*3,iy-8+r*3,3,3);}}
  else if(t[3]==='clock'){g.beginPath();g.arc(ix,iy+1,6.5,0,TAU);g.stroke();g.fillRect(ix-2,iy-9,4,2.4);g.beginPath();g.moveTo(ix,iy+1);g.lineTo(ix,iy-3.5);g.moveTo(ix,iy+1);g.lineTo(ix+3.5,iy+2);g.stroke();}
  else if(t[3]==='zig'){g.beginPath();g.moveTo(ix-7,iy+5);g.lineTo(ix-2.5,iy-5);g.lineTo(ix+2.5,iy+5);g.lineTo(ix+7,iy-5);g.stroke();g.fillStyle='#ff7a1a';for(const[x,y]of[[ix-2.5,iy-7.5],[ix+2.5,iy+7.5]]){g.beginPath();g.arc(x,y,2,0,TAU);g.fill();}}
  else if(t[3]==='ramp'){g.beginPath();g.moveTo(ix-8,iy+7);g.lineTo(ix+7,iy+7);g.lineTo(ix+7,iy-1);g.closePath();g.fill();g.beginPath();g.moveTo(ix-4,iy+1);g.quadraticCurveTo(ix-2,iy-7,ix+4,iy-7);g.stroke();g.beginPath();g.moveTo(ix+6.5,iy-7);g.lineTo(ix+2.5,iy-9.5);g.lineTo(ix+2.5,iy-4.5);g.closePath();g.fill();}
  else if(t[3]==='siren'){g.beginPath();g.arc(ix,iy+3,5.5,Math.PI,0);g.closePath();g.fill();g.fillRect(ix-7.5,iy+3.5,15,3);g.lineWidth=1.8;for(const a of[-2.5,-1.57,-.64]){g.beginPath();g.moveTo(ix+Math.cos(a)*8,iy+2+Math.sin(a)*8);g.lineTo(ix+Math.cos(a)*11,iy+2+Math.sin(a)*11);g.stroke();}}
  else if(t[3]==='cup'){g.beginPath();g.moveTo(ix-6,iy-7);g.lineTo(ix+6,iy-7);g.quadraticCurveTo(ix+6,iy+2,ix,iy+2);g.quadraticCurveTo(ix-6,iy+2,ix-6,iy-7);g.fill();g.fillRect(ix-1.2,iy+2,2.4,3.5);g.fillRect(ix-4.5,iy+5.5,9,2.4);g.lineWidth=1.6;g.beginPath();g.arc(ix-6.5,iy-3.5,2.6,Math.PI*.5,Math.PI*1.5);g.stroke();g.beginPath();g.arc(ix+6.5,iy-3.5,2.6,-Math.PI*.5,Math.PI*.5);g.stroke();}
  g.fillStyle=dark?'#2a1b00':'#ffffff';if(!dark){g.lineWidth=3;g.strokeStyle='rgba(0,0,0,.18)';g.strokeText(t[0],bx+31,by+bh/2+1);}g.fillText(t[0],bx+31,by+bh/2+1);g.restore();}
 {const n=ZONES.length,lv=Math.max(1,Math.min(5,Math.ceil((zi+1)*5/n))),bx=12,by=H-26,sw=22,gap=4;""")
rep("const APP_VER=40;","const APP_VER=41;")
open(p,'w').write(s);print('ok')
