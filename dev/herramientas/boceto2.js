const {chromium}=require('playwright');const fs=require('fs');
const src=fs.readFileSync('pilot_svg.js','utf8');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(500);
 await E(()=>{localStorage.setItem('ct_gear',JSON.stringify({own:['s0','v0','h0','h3','v3','s4'],eq:{suit:'s4',vest:'v3',helm:'h3'}}));localStorage.setItem('ct_wallet',JSON.stringify(48500));});await p.reload();await W(1000);
 await E(()=>{__G.money=48500;});
 await p.click('#bShop');await W(300);await p.click('#sGear');await W(400);
 await E(src=>{eval(src);window.pilotSVG=pilotSVG;
  const pv=document.querySelector('.gearpv');const top=document.querySelector('#eTop');
  const st=document.createElement('style');st.textContent=`.showroom{position:relative;flex:none;width:min(100%,440px);height:400px;border-radius:18px;overflow:hidden;background:radial-gradient(ellipse 70% 60% at 50% 0%,rgba(120,200,255,.55),rgba(30,90,160,.15) 60%,transparent 75%),linear-gradient(180deg,#123a6a 0%,#0c2548 60%,#0a1a36 100%);box-shadow:inset 0 0 0 1px rgba(255,255,255,.12)}
  .showroom .beam{position:absolute;top:-20px;width:120px;height:440px;background:linear-gradient(180deg,rgba(160,220,255,.22),transparent 80%);filter:blur(6px)}
  .showroom .pod{position:absolute;left:50%;bottom:44px;width:250px;height:46px;transform:translateX(-50%);border-radius:50%;background:radial-gradient(ellipse at 50% 35%,#4a7fb8,#173a66 70%);box-shadow:0 0 0 3px rgba(51,214,255,.6),0 0 34px rgba(51,214,255,.45)}
  .showroom svg.pil{position:absolute;left:50%;bottom:48px;height:346px;width:auto;transform:translateX(-50%)}
  .showroom .tag{position:absolute;left:0;right:0;bottom:8px;display:flex;justify-content:center;gap:5px;flex-wrap:wrap;padding:0 8px}
  .showroom .tag span{font-family:var(--cond);font-weight:800;font-size:11px;letter-spacing:.04em;padding:2px 7px;border-radius:8px;background:rgba(8,20,40,.72);color:#fff;border:1px solid rgba(255,255,255,.14)}
  .showroom .tag span b{color:var(--gold)}
  .showroom .mini{position:absolute;right:10px;top:10px;width:52px;height:88px;border-radius:12px;background:rgba(8,40,80,.45);border:1px solid rgba(255,255,255,.14)}
  .showroom .rot{position:absolute;right:12px;bottom:66px;font-family:var(--cond);font-weight:800;font-size:11px;letter-spacing:.1em;color:rgba(255,255,255,.6)}`;
  document.head.append(st);
  const sr=document.createElement('div');sr.className='showroom';
  const o={helm:{st:'mx',c:'#ffd21a',c2:'#e3202b',pat:'flame',brand:'alpinestars'},vest:{c:'#16181d',c2:'#e3202b',pat:'vault',name:'RX Vault'},suit:{c:'#b6f01e',a:'#1d2027'}};
  sr.innerHTML='<div class="beam" style="left:30px;transform:rotate(14deg)"></div><div class="beam" style="right:30px;transform:rotate(-14deg)"></div><div class="pod"></div>'+pilotSVG(o,'m').replace('<svg ','<svg class="pil" ')+'<div class="tag"><span><b>ALPINESTARS S-M8 FLAME</b></span><span><b>JET PILOT RX VAULT</b></span><span><b>NEOPRENO FLÚOR</b></span></div>';
  const mini=document.createElement('canvas');mini.className='mini';mini.width=104;mini.height=176;const k=mini.getContext('2d');k.drawImage(top,0,0,top.width,top.height,0,0,104,176);sr.append(mini);
  pv.replaceWith(sr);},src);
 await W(300);await p.screenshot({path:'boceto2.png'});
 await p.screenshot({path:'boceto2-full.png',fullPage:true});
 console.log(JSON.stringify(errs));await b.close();})();
