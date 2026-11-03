p='costa-turbo.html';s=open(p).read()
i=s.index(" if(p.logo){const L={jj:[[\"JJ's\",'#8e1f2c']")
end="g.strokeStyle='rgba(255,255,255,.85)';g.lineWidth=2.5;g.strokeRect(0,0,x0,30);g.restore();}}"
j=s.index(end,i)+len(end)
assert s.count(" if(p.logo){const L={jj:[[\"JJ's\",'#8e1f2c']")==1
new=""" if(p.logo){const L={jj:[["JJ's",'#8e1f2c'],['SPORTS','#1f3fb0'],['LOUNGE','#1c1c1f']],roxy:[['R O X Y','#7a5232']],ct:[['COSTA TURBO','#0e3f8f']]}[p.logo];
  // en el panel blanco de atrás, encima de la franja negra, con su inclinación y sin salirse de la moto
  if(L){const v=document.createElement('canvas');v.width=W;v.height=H;const x=v.getContext('2d');x.save();x.transform(1,.64,0,1,180,224);x.font='800 26px "Saira Condensed",Arial,sans-serif';
   let tw=0;for(const[t]of L)tw+=x.measureText(t).width+16;const sc=Math.min(1,170/tw);x.translate((170-tw*sc)/2,0);x.scale(sc,sc);x.textBaseline='middle';x.textAlign='center';let x0=0;
   for(const[t,c]of L){const w=x.measureText(t).width+16;x.fillStyle=c;x.fillRect(x0,0,w,34);x.fillStyle=p.logo==='ct'?'#ffd21a':'#ffffff';x.fillText(t,x0+w/2,18);x0+=w;}
   x.strokeStyle='rgba(255,255,255,.9)';x.lineWidth=2.5;x.strokeRect(0,0,tw,34);x.restore();x.globalCompositeOperation='destination-in';x.drawImage(stkDecor.mask,0,0);g.drawImage(v,0,0);}}"""
s=s[:i]+new+s[j:]
a="const APP_VER=109;";assert s.count(a)==1;s=s.replace(a,"const APP_VER=110;")
open(p,'w').write(s);print('ok')
