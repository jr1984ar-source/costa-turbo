const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 let body=fs.readFileSync('costa-turbo.html','utf8');body=body.replace("requestAnimationFrame(frame);\n})();","window.__G=G;requestAnimationFrame(frame);\n})();");
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:780},deviceScaleFactor:2,hasTouch:true});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push('PE '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push('CE '+m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.waitForTimeout(200);await p.click('#gGo');await p.waitForTimeout(300);await p.click('#mGo');await p.waitForTimeout(3600);
 // move everyone close to the bar
 await p.evaluate(()=>{const G=__G,r=G.zone.ring;G.P.y=r.y+520;G.P.x=330;G._tip=1;G.rivals.forEach((c,i)=>{c.y=r.y+560+i*40;c.x=150+i*40;c.v=250;});});
 await p.keyboard.down('ArrowUp');
 for(let t=0;t<12;t++){await p.waitForTimeout(700);const st=await p.evaluate(()=>__G.rivals.map(c=>(c.pit||0)+':'+Math.round(c.y-__G.zone.ring.y)).join(' '));console.log(st);if(t===4)await p.screenshot({path:'ct18-pit.png'});}
 console.log(JSON.stringify(errs));await b.close();})();
