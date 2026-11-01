const {chromium}=require('playwright');const fs=require('fs');
const src=['pilot34.js','helmetL.js','pilotL.js','gloveIcon.js'].map(f=>fs.readFileSync(f,'utf8')).join('\n');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(500);
 await E(()=>{localStorage.setItem('ct_gear',JSON.stringify({own:['s0','v0','h0','h3','v3','s4'],eq:{suit:'s4',vest:'v3',helm:'h3'}}));});await p.reload();await W(1000);
 await E(()=>{__G.money=48500;});
 await p.click('#bShop');await W(300);await p.click('#sGear');await W(400);
 await E(src=>{eval(src.replace("if (typeof module","if (false&&typeof module"));window.pilotSideSVG=pilotLSVG;window.gloveIcon=gloveIcon;window.LENSES=LENSES;
  const st=document.createElement('style');st.textContent=`.showroom{position:relative;flex:none;width:min(100%,440px);height:350px;border-radius:18px;overflow:hidden;background:radial-gradient(ellipse 70% 60% at 50% 0%,rgba(120,200,255,.55),rgba(30,90,160,.15) 60%,transparent 75%),linear-gradient(180deg,#123a6a 0%,#0c2548 60%,#0a1a36 100%);box-shadow:inset 0 0 0 1px rgba(255,255,255,.12)}
  .showroom .beam{position:absolute;top:-20px;width:120px;height:420px;background:linear-gradient(180deg,rgba(160,220,255,.22),transparent 80%);filter:blur(6px)}
  .showroom .pod{position:absolute;left:50%;bottom:40px;width:250px;height:44px;transform:translateX(-50%);border-radius:50%;background:radial-gradient(ellipse at 50% 35%,#4a7fb8,#173a66 70%);box-shadow:0 0 0 3px rgba(51,214,255,.6),0 0 34px rgba(51,214,255,.45)}
  .showroom svg.pil{position:absolute;left:50%;bottom:44px;height:298px;width:auto;transform:translateX(-50%)}
  .showroom .tag{position:absolute;left:0;right:0;bottom:8px;display:flex;justify-content:center;gap:4px;flex-wrap:wrap;padding:0 6px}
  .showroom .tag span{font-family:var(--cond);font-weight:800;font-size:10.5px;letter-spacing:.03em;padding:2px 6px;border-radius:8px;background:rgba(8,20,40,.72);color:var(--gold);border:1px solid rgba(255,255,255,.14)}
  .showroom .mini{position:absolute;right:10px;top:10px;width:52px;height:88px;border-radius:12px;background:rgba(8,40,80,.45);border:1px solid rgba(255,255,255,.14)}
  .etabs4{flex:none;width:min(100%,440px);display:grid;grid-template-columns:repeat(5,1fr);gap:4px}.etabs4 .btn{width:100%;padding:9px 2px;font-size:11.5px}.etabs4 .btn.on{background:var(--orange);color:#fff;border-color:transparent}
  .gsw{width:100%;display:grid;grid-template-columns:58px 1fr;gap:6px;align-items:center;text-align:left}
  .gsw .gk{font-family:var(--cond);font-weight:800;font-size:12px;letter-spacing:.12em;color:var(--dim)}
  .gsw .gr2{display:flex;gap:7px;flex-wrap:nowrap}.gsw .dot{flex:none;width:28px;height:28px;border-radius:50%;border:2px solid rgba(255,255,255,.28);display:block;box-sizing:border-box}.gsw .dot.on{border-color:#fff;box-shadow:0 0 0 2px var(--orange)}
  .gsw .dot.ln{border-radius:8px;width:30px}
  .gnote{width:min(100%,440px);font-size:11px;color:var(--dim);text-align:left;margin:-2px 0 0}
  .gog{width:64px;height:34px;border-radius:9px;background:radial-gradient(circle at 40% 30%,#24406e,#0c1c3a);display:grid;place-items:center}.gog svg{width:58px;height:30px}`;
  document.head.append(st);
  const gog=(brand,strap,lens,frame)=>{const L=LENSES[lens],id='g'+Math.random().toString(36).slice(2),tc=['#ffffff','#f4f6f9','#ffd21a','#b6f01e'].includes(strap)?'#15171c':'#fff';
   return `<svg viewBox="0 0 100 50"><defs><linearGradient id="${id}" x1="0" x2="1" y1="0" y2="1">${L.map((c,i)=>`<stop offset="${i/(L.length-1)}" stop-color="${c}"/>`).join('')}</linearGradient></defs><rect x="0" y="16" width="100" height="16" rx="3" fill="${strap}"/><text x="50" y="27.5" text-anchor="middle" font-family="Arial Black,Arial" font-weight="900" font-size="7" fill="${tc}">${brand==='oakley'?'OAKLEY':brand==='100'?'100%':'alpinestars'}</text><path d="M14,10 C30,4 70,4 86,10 C92,16 92,34 86,40 C76,44 60,44 56,38 C53,34 47,34 44,38 C40,44 24,44 14,40 C8,34 8,16 14,10 Z" fill="${frame||'#1b1d22'}" stroke="rgba(0,0,0,.5)"/><path d="M19,14 C34,9 66,9 81,14 C85,19 85,31 81,36 C73,39 62,39 59,34 C55,30 45,30 41,34 C38,39 27,39 19,36 C15,31 15,19 19,14 Z" fill="url(#${id})"/><path d="M26,14 L34,13 L26,36 L20,35 Z" fill="rgba(255,255,255,.45)"/></svg>`;};
  // showroom
  const pv=document.querySelector('.gearpv');const top=document.querySelector('#eTop');
  const sr=document.createElement('div');sr.className='showroom';
  const o={helm:{st:'mx',c:'#c8141c',c2:'#ff5a2a'},vest:{c:'#16181d',c2:'#e3202b',pat:'vault',name:'RX Vault'},suit:{c:'#1d2027',a:'#e3202b'},gog:{brand:'oakley',strap:'#1d2027',lens:'prizm'},glove:'#1d2027',gloveA:'#e3202b'};
  sr.innerHTML='<div class="beam" style="left:30px;transform:rotate(14deg)"></div><div class="beam" style="right:30px;transform:rotate(-14deg)"></div><div class="pod"></div>'+pilotSideSVG(o,'m').replace('<svg ','<svg class="pil" ')+'<div class="tag"><span>ALPINESTARS S-M5</span><span>OAKLEY AIRBRAKE MX</span><span>JET PILOT RX VAULT</span><span>JET PILOT MATRIX RACE</span><span>NEOPRENO NEGRO</span></div>';
  const mini=document.createElement('canvas');mini.className='mini';mini.width=104;mini.height=176;mini.getContext('2d').drawImage(top,0,0,top.width,top.height,0,0,104,176);sr.append(mini);pv.replaceWith(sr);
  // pestañas
  const tabs=document.querySelector('#eTabs');tabs.className='etabs4';tabs.innerHTML='<button class="btn ghost sm">CASCO</button><button class="btn ghost sm">GAFAS</button><button class="btn ghost sm on">GUANTES</button><button class="btn ghost sm">CHALECO</button><button class="btn ghost sm">NEOPRENO</button>';
  // lista de gafas
  const Lst=document.querySelector('#eList');const G=[['DE SERIE',[['Guantes negros','Neopreno básico',0,'#1d2027','#3a3f4a','',1]]],['JET PILOT',[['Jet Pilot Matrix Race','Palma antideslizante',2000,'#1d2027','#e3202b','JP',2],['Jet Pilot RX Race','Nudillos reforzados',3500,'#1d2027','#ffd21a','JP',0]]],['ALPINESTARS',[['Alpinestars Radar','Ligeros y ventilados',1500,'#f4f6f9','#1e5eff','A★',0],['Alpinestars Techstar','Protección de carbono',4000,'#16181d','#f4f6f9','A★',0]]],["O'NEILL",[["O'Neill Superlite",'Finos de competición',1200,'#6f7680','#33a3ff','ON',0],["O'Neill Reactor",'Cierre de velcro ancho',2500,'#1d2027','#ff7a1a','ON',0]]]];
  let h='';G.forEach(([hd,its],gi)=>{h+=`<div class="ghd">${hd}</div>`;its.forEach(([n,d,pr,c,a,t,state],k)=>{h+=`<div class="prt gr ${state===2?'eq':''}"><div class="gog">${gloveIcon({c,a,t},'gi'+gi+k)}</div><div><div class="nm">${n}</div><div class="ef">${d}</div></div><button class="btn ${state===2?'max':state===1?'':'p'}">${state===2?'EN USO':state===1?'USAR':'<i class="coin"></i>'+pr.toLocaleString('es-ES')}</button></div>`;});});
  Lst.innerHTML=h;document.querySelectorAll('.prt.gr').forEach(r=>r.style.gridTemplateColumns='64px minmax(0,1fr) auto');
 },src);
 await W(300);await p.screenshot({path:'boceto13.png',fullPage:true});
 console.log(JSON.stringify(errs));await b.close();})();
