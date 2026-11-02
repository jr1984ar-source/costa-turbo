const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();
 // simular el modo app del iPhone: innerHeight 60 px más bajo que la pantalla
 const ctx=await b.newContext({viewport:{width:393,height:792},screen:{width:393,height:852},deviceScaleFactor:2});
 await ctx.addInitScript(()=>{Object.defineProperty(navigator,'standalone',{get:()=>true});});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1200);
 console.log('alto html:',await p.evaluate(()=>document.documentElement.style.height),'pantalla',await p.evaluate(()=>screen.height+' / innerHeight '+innerHeight));
 // sin modo app: no cambia nada
 const p2=await (await b.newContext({viewport:{width:393,height:792}})).newPage();await p2.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p2.waitForTimeout(800);
 console.log('navegador normal:',await p2.evaluate(()=>document.documentElement.style.height));
 console.log('errs',JSON.stringify(errs));await b.close();})();
