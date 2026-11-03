// decoración: vinilo, logo y dorsal sobre el dibujo de la moto (coordenadas de la imagen 1272x668)
function stkDecor(g,p,D){
 const W=D.width,H=D.height;
 if(!stkDecor.mask){const c=document.createElement('canvas');c.width=W;c.height=H;const x=c.getContext('2d'),id=x.createImageData(W,H),s=D.data;for(let i=0;i<s.length;i+=4){const L=Math.round(s[i]/36);if(L===1||L===2)id.data[i+3]=255;}x.putImageData(id,0,0);stkDecor.mask=c;}
 if(p.vinyl){const v=document.createElement('canvas');v.width=W;v.height=H;const x=v.getContext('2d'),vc=p.vcol||'#ffffff';x.fillStyle=vc;x.save();x.transform(1,.24,0,1,0,256);
  if(p.vinyl==='rayas'){x.fillRect(20,-30,1300,16);x.fillRect(20,-6,1300,16);}
  else if(p.vinyl==='llamas'){const fl=(bx,sc,col)=>{x.fillStyle=col;x.beginPath();x.moveTo(bx,-80*sc);const T=[[-560,-46],[-390,-14],[-640,14],[-430,40],[-300,66]];for(const[tx,ty]of T){x.quadraticCurveTo(bx+tx*.45*sc,ty*sc-28*sc,bx+tx*sc,ty*sc);x.quadraticCurveTo(bx+tx*.55*sc,ty*sc+6*sc,bx-50*sc,ty*sc+14*sc);}x.lineTo(bx,96*sc);x.closePath();x.fill();};
   fl(1260,1,vc);fl(1240,.72,mixc(vc,'#ffd21a',.6));}
  else if(p.vinyl==='cuadros'){const q=24;for(let i=0;i<16;i++)for(let j=0;j<4;j++)if((i+j)%2===0)x.fillRect(120+i*q,-40+j*q,q,q);}
  x.restore();x.globalCompositeOperation='destination-in';x.drawImage(stkDecor.mask,0,0);g.save();g.globalAlpha=.92;g.drawImage(v,0,0);g.restore();}
 if(p.logo){const L={jj:[["JJ's",'#8e1f2c'],['SPORTS','#1f3fb0'],['LOUNGE','#1c1c1f']],roxy:[['R O X Y','#7a5232']],ct:[['COSTA TURBO','#0e3f8f']]}[p.logo];
  if(L){g.save();g.transform(1,.33,0,1,64,312);let x0=0;g.font='800 22px "Saira Condensed",Arial,sans-serif';g.textBaseline='middle';g.textAlign='center';
   for(const[t,c]of L){const w=g.measureText(t).width+14;g.fillStyle=c;g.fillRect(x0,0,w,30);g.fillStyle=p.logo==='ct'?'#ffd21a':'#ffffff';g.fillText(t,x0+w/2,16);x0+=w;}
   g.strokeStyle='rgba(255,255,255,.85)';g.lineWidth=2.5;g.strokeRect(0,0,x0,30);g.restore();}}
 if(p.num){g.save();g.transform(1,.3,0,1,812,412);g.fillStyle='#ffffff';g.strokeStyle='#16181d';g.lineWidth=5;g.beginPath();g.roundRect(0,0,100,76,16);g.fill();g.stroke();
  g.fillStyle='#16181d';g.font='800 62px "Saira Condensed",Arial,sans-serif';g.textAlign='center';g.textBaseline='middle';g.fillText(String(p.num),50,41);g.restore();}}
