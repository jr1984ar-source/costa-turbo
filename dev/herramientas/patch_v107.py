p='costa-turbo.html';s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
STK=open('stk_proto.js').read().split('\n',1)[1]  # sin la primera línea de comentario
# datos: dorsal, vinilo (y su color) y logo dentro de la pintura de cada moto
rep("function defaultPaint(m){const s=m.side,d=SKI_DEF[m.id];if(d)return{colors:false,hull:d[0],deck:d[1],hood:d[2],stripe:d[3],seat:d[4],name:''};return{colors:false,hull:s.hull,deck:s.deck,hood:s.hood,stripe:s.stripe,seat:s.seatA,name:''};}",
    "function defaultPaint(m){const s=m.side,d=SKI_DEF[m.id],X={num:0,vinyl:'',vcol:'#ffffff',logo:''};if(d)return Object.assign({colors:false,hull:d[0],deck:d[1],hood:d[2],stripe:d[3],seat:d[4],name:''},X);return Object.assign({colors:false,hull:s.hull,deck:s.deck,hood:s.hood,stripe:s.stripe,seat:s.seatA,name:''},X);}")
rep("function skOf(m,p){if(!m.side)return m.sk;p=p||paintOf(m);if(!p.colors)return m.sk;return Object.assign({},m.sk,{hull:p.deck,hullD:mixc(p.deck,'#000000',.35),acc:p.stripe,hood:p.hood,rim:p.hull,seat:p.seat});}",
    "function skOf(m,p){if(!m.side)return m.sk;p=p||paintOf(m);const b=!p.colors?m.sk:Object.assign({},m.sk,{hull:p.deck,hullD:mixc(p.deck,'#000000',.35),acc:p.stripe,hood:p.hood,rim:p.hull,seat:p.seat});return(p.num||p.vinyl)?Object.assign({},b,{num:p.num|0,vinyl:p.vinyl||'',vcol:p.vcol||'#ffffff'}):b;}")
rep("return['colors','hull','deck','hood','stripe','seat'].some(k=>String(a[k])!==String(b[k]));","return['colors','hull','deck','hood','stripe','seat','num','vinyl','vcol','logo'].some(k=>String(a[k]||'')!==String(b[k]||''));")
# dibujo del taller: vinilo, logo y dorsal
rep(" if(m&&m.riva&&RIVA_IM){for(const k of ['rear','front']){const a=RIVA_ST.aff[k];g.save();g.transform(a[0],a[1],a[2],a[3],a[4],a[5]);g.drawImage(RIVA_IM,0,0);g.restore();}}}",
    " if(m&&m.riva&&RIVA_IM){for(const k of ['rear','front']){const a=RIVA_ST.aff[k];g.save();g.transform(a[0],a[1],a[2],a[3],a[4],a[5]);g.drawImage(RIVA_IM,0,0);g.restore();}}\n if(p&&(p.vinyl||p.logo||p.num)&&SKI_D)stkDecor(g,p,SKI_D);}\n// pegatinas: vinilo, logo y dorsal sobre el dibujo de la moto (coordenadas de la imagen 1272x668)\n"+STK)
# vista desde arriba (carreras): vinilo y dorsal
rep("  g.fillStyle='rgba(255,255,255,.14)';g.beginPath();g.moveTo(0,-26);",
"""  if(s.vinyl){g.fillStyle=s.vcol||'#ffffff';if(s.vinyl==='rayas'){g.fillRect(-3.8,-31,2.4,58);g.fillRect(1.4,-31,2.4,58);}
   else if(s.vinyl==='llamas'){for(const m of[-1,1]){g.beginPath();g.moveTo(m*1.5,-29);g.quadraticCurveTo(m*9,-24,m*12.5,-12);g.lineTo(m*10,-14);g.quadraticCurveTo(m*12,-6,m*12.5,2);g.lineTo(m*9.5,-4);g.quadraticCurveTo(m*10.5,4,m*12,12);g.lineTo(m*8.5,0);g.quadraticCurveTo(m*6,-16,m*1.5,-29);g.fill();}}
   else if(s.vinyl==='cuadros'){for(let i=0;i<8;i++)for(let j=0;j<2;j++)if((i+j)%2===0)g.fillRect(-12+i*3,17+j*3,3,3);}}
  if(s.num){g.fillStyle='#ffffff';g.beginPath();g.arc(0,-19,4.6,0,TAU);g.fill();g.strokeStyle='#16181d';g.lineWidth=.8;g.stroke();g.fillStyle='#16181d';g.font='800 '+(s.num>9?5.2:6.4)+'px "Saira Condensed",Arial,sans-serif';g.textAlign='center';g.textBaseline='middle';g.fillText(String(s.num),0,-18.6);}
  g.fillStyle='rgba(255,255,255,.14)';g.beginPath();g.moveTo(0,-26);""")
# pantalla PINTURA: filas de dorsal, vinilo, color del vinilo y logo
rep("  row.append(sp,sw);R.append(row);}}\nfunction goPaint(){","""  row.append(sp,sw);R.append(row);}
 const chipRow=(lab,opts,key)=>{const row=document.createElement('div');row.className='prow';const sp=document.createElement('span');sp.textContent=lab;const box=document.createElement('div');box.className='chips';
  for(const[v,t]of opts){const b=document.createElement('button');b.className='chip'+(String(d[key]||'')===v?' on':'');b.textContent=t;b.addEventListener('click',()=>{d[key]=v;Snd.click();box.querySelectorAll('.chip').forEach(x=>x.classList.toggle('on',x===b));paintPreview();});box.append(b);}
  row.append(sp,box);R.append(row);};
 {const row=document.createElement('div');row.className='prow';const sp=document.createElement('span');sp.textContent='DORSAL';const box=document.createElement('div');box.className='chips';
  const mk=(t,f)=>{const b=document.createElement('button');b.className='chip';b.textContent=t;b.addEventListener('click',()=>{f();Snd.click();val.textContent=d.num?String(d.num):'—';none.classList.toggle('on',!d.num);paintPreview();});return b;};
  const val=document.createElement('b');val.className='dnum';val.textContent=d.num?String(d.num):'—';
  const none=mk('SIN DORSAL',()=>{d.num=0;});none.classList.toggle('on',!d.num);
  box.append(mk('−',()=>{d.num=d.num>1?d.num-1:99;}),val,mk('+',()=>{d.num=d.num<99?(d.num|0)+1:1;}),none);row.append(sp,box);R.append(row);}
 chipRow('VINILO',[['','NINGUNO'],['llamas','LLAMAS'],['rayas','RAYAS'],['cuadros','CUADROS']],'vinyl');
 {const row=document.createElement('div');row.className='prow';const sp=document.createElement('span');sp.textContent='COLOR DEL VINILO';const sw=document.createElement('div');sw.className='sws';
  for(const col of SWATCHES){const b=document.createElement('button');b.className='sw'+(String(d.vcol||'#ffffff').toLowerCase()===col?' on':'');b.style.background=col;b.setAttribute('aria-label','Vinilo '+col);b.addEventListener('click',()=>{d.vcol=col;Snd.click();sw.querySelectorAll('.sw').forEach(x=>x.classList.toggle('on',x===b));paintPreview();});sw.append(b);}
  row.append(sp,sw);R.append(row);}
 chipRow('LOGO',[['','NINGUNO'],['jj',"JJ'S SPORTS"],['roxy','ROXY'],['ct','COSTA TURBO']],'logo');}
function goPaint(){""")
rep(".prows{width:min(100%,440px);display:grid;gap:6px;text-align:left}",".prows{width:min(100%,440px);display:grid;gap:6px;text-align:left}\n.chips{display:flex;flex-wrap:wrap;gap:6px;align-items:center;padding:3px 2px}.chip{font-family:var(--cond);font-weight:800;font-size:13px;letter-spacing:.06em;padding:7px 12px;border-radius:999px;border:1.5px solid rgba(255,255,255,.28);background:rgba(255,255,255,.06);color:#fff}.chip.on{background:#ffe14d;color:#16181d;border-color:#ffe14d}.dnum{font-family:var(--cond);font-weight:800;font-size:20px;min-width:34px;text-align:center;color:#fff}")
rep("const APP_VER=106;","const APP_VER=107;")
open(p,'w').write(s);print('ok',len(s))
