const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 let body=fs.readFileSync('costa-turbo.html','utf8');body=body.replace("requestAnimationFrame(frame);\n})();","window.__G=G;window.__in=input;requestAnimationFrame(frame);\n})();");
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();
 for(const vp of [{width:390,height:780},{width:360,height:740},{width:844,height:390}]){
 const ctx=await b.newContext({viewport:vp,deviceScaleFactor:2});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push('PE '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push('CE '+m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);
 const c=async id=>{const r=await (await p.$(id)).boundingBox();return [r.x+r.width/2,r.y+r.height/2];};
 // acelerar en título -> garaje
 let [x,y]=await c('#bAcc');await p.mouse.move(x,y);await p.mouse.down();await p.mouse.up();await p.waitForTimeout(300);
 const scr=await p.evaluate(()=>!document.querySelector('#scrGarage').hidden);
 await p.click('#gGo');await p.waitForTimeout(300);await p.click('#mGo');await p.waitForTimeout(3600);
 [x,y]=await c('#bAcc');await p.mouse.move(x,y);await p.mouse.down();await p.waitForTimeout(1500);
 const t0=await p.evaluate(()=>__G.turbo);
 let [dx,dy]=await c('#bDrift');await p.mouse.move(dx,dy,{steps:5});await p.waitForTimeout(200);
 const st1=await p.evaluate(()=>({acc:__in.acc,drift:__in.drift}));
 let [tx,ty]=await c('#bTurbo');await p.mouse.move(tx,ty,{steps:5});await p.waitForTimeout(200);
 const t1=await p.evaluate(()=>({turbo:__G.turbo,boost:__G.P.boostT>0,acc:__in.acc}));
 await p.screenshot({path:'pads-'+vp.width+'.png'});
 await p.mouse.up();await p.waitForTimeout(100);const st2=await p.evaluate(()=>({acc:__in.acc,drift:__in.drift}));
 console.log(vp.width,'garage',scr,JSON.stringify(st1),'turbo',t0,'->',JSON.stringify(t1),'after',JSON.stringify(st2),JSON.stringify(errs));
 await ctx.close();}
 await b.close();})();
