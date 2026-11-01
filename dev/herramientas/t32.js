const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2});await ctx.addInitScript(()=>{try{localStorage.setItem('ct_parts',JSON.stringify({brava:{turbo:1,aletas:3}}));localStorage.setItem('ct_wallet','20000');}catch(e){}});const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1000);
 await p.evaluate(()=>__T.goShop('title'));await p.waitForTimeout(400);await p.screenshot({path:'v18-shop.png'});
 await p.evaluate(()=>{__G.free=true;__G.zi=1;__G.parts=JSON.parse(localStorage.getItem('ct_parts')).brava;__goMap();__T.startRace();});await p.waitForTimeout(500);await p.evaluate(()=>__T.openBar());await p.waitForTimeout(400);await p.screenshot({path:'v18-roxy.png'});
 console.log(JSON.stringify(errs));await b.close();})();
