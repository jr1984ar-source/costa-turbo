// Nombre de la moto en el costado y pegatina Riva Racing
function skiDecor(g,m,p){const lu=c=>(parseInt(c.slice(1,3),16)*.299+parseInt(c.slice(3,5),16)*.587+parseInt(c.slice(5,7),16)*.114)/255;
 const nm=(p&&p.name||'').trim();
 if(nm){g.save();g.translate(560,372);g.rotate(.43);g.transform(1,0,-.28,1,0,0);g.font='italic 800 60px "Saira Condensed",Arial,sans-serif';g.textAlign='center';g.textBaseline='middle';const lt=lu(p.deck)>.6;
  g.lineJoin='round';g.lineWidth=8;g.strokeStyle=lt?'rgba(255,255,255,.8)':'rgba(0,0,0,.6)';g.strokeText(nm.toUpperCase(),0,0,330);g.fillStyle=lt?'#16181d':'#ffffff';g.fillText(nm.toUpperCase(),0,0,330);g.restore();}
 if(m&&m.riva){g.save();g.translate(880,500);g.rotate(.36);g.scale(1.45,1.45);g.transform(1,0,-.25,1,0,0);
  g.fillStyle='#16181d';g.beginPath();g.moveTo(-104,-24);g.lineTo(110,-24);g.lineTo(104,24);g.lineTo(-110,24);g.closePath();g.fill();
  g.fillStyle='#e3202b';g.beginPath();g.moveTo(-98,-18);g.lineTo(104,-18);g.lineTo(98,18);g.lineTo(-104,18);g.closePath();g.fill();
  g.fillStyle='#ffffff';g.font='italic 800 30px "Saira Condensed",Arial,sans-serif';g.textAlign='center';g.textBaseline='middle';g.fillText('RIVA RACING',0,2);g.restore();}}
