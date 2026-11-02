// Placa con el nombre en el casco abajo y pegatinas Riva Racing (logo) en el costado
function skiDecor(g,m,p){const lu=c=>(parseInt(c.slice(1,3),16)*.299+parseInt(c.slice(3,5),16)*.587+parseInt(c.slice(5,7),16)*.114)/255;
 const nm=((p&&p.name)||(m&&m.name)||'').trim().toUpperCase();
 if(nm){const col=lu(p.hull)>.62?'#16181d':'#ffffff';g.save();g.transform(1,.494,0,1,278,346);
  g.fillStyle=col;g.font='800 46px "Saira Condensed",Arial,sans-serif';g.textAlign='center';g.textBaseline='middle';g.fillText(nm,121,26,220);g.restore();}
 if(m&&m.riva&&RIVA_IM){for(const k of ['rear','front']){const a=RIVA_ST.aff[k];g.save();g.transform(a[0],a[1],a[2],a[3],a[4],a[5]);g.drawImage(RIVA_IM,0,0);g.restore();}}}
