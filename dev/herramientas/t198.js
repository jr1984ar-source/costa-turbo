const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1800);
 await p.evaluate(()=>__T.goFree());await p.waitForTimeout(600);await p.screenshot({path:'v103-menu.png'});
 const names=await p.evaluate(()=>[...document.querySelectorAll('body *')].filter(e=>e.children.length===0&&/MODO LIBRE|MATÍAS/i.test(e.textContent)).map(e=>e.textContent.trim()).slice(0,8));console.log('menu',JSON.stringify(names));
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(400);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);await p.screenshot({path:'v103-juego.png'});
 console.log('hud',JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('body *')].filter(e=>e.children.length===0&&/MODO LIBRE|MATÍAS/i.test(e.textContent)&&e.offsetParent).map(e=>e.textContent.trim()))));
 console.log('errs',JSON.stringify(errs));await b.close();})();
