const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 const body=fs.readFileSync('costa-turbo.html','utf8');
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();
 const run=async(vp,zi,name,steer)=>{const ctx=await b.newContext({viewport:vp,deviceScaleFactor:2,hasTouch:true});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push('PE '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push('CE '+m.text())});
  await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.click('#gGo');await p.waitForTimeout(200);
  await p.evaluate(z=>{const T=window.__ct;T.G.zi=z;T.goMap();},zi);await p.waitForTimeout(300);await p.screenshot({path:name+'-map.png'});
  await p.click('#mGo');await p.waitForTimeout(3600);await p.keyboard.down('ArrowUp');
  if(steer){await p.waitForTimeout(1500);await p.keyboard.down('ArrowLeft');await p.waitForTimeout(900);await p.keyboard.up('ArrowLeft');}
  await p.waitForTimeout(4000);await p.screenshot({path:name+'.png'});
  const st=await p.evaluate(()=>{const G=window.__ct.G;return {mode:G.mode,pol:G.police.length,catches:G.catches,money:G.money,fps:0}});
  // fps measure
  const fps=await p.evaluate(()=>new Promise(r=>{let n=0;const t0=performance.now();const f=()=>{n++;if(performance.now()-t0<1000)requestAnimationFrame(f);else r(n);};requestAnimationFrame(f);}));
  console.log(name,JSON.stringify(st),'fps',fps,JSON.stringify(errs.slice(0,5)));await ctx.close();};
 await run({width:390,height:780},3,'z4-chase',false);
 await run({width:390,height:780},5,'z6-night',false);
 await run({width:390,height:780},2,'z3-beach',true);
 await run({width:844,height:390},0,'land',false);
 await b.close();})();
