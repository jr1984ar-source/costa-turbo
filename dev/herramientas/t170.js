const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852}})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1000);await p.evaluate(()=>{__T.newGame(0);});await p.waitForTimeout(400);
 console.log(await p.evaluate(()=>{const Z=__G.zone;return 'orilla en salida: '+[-150,-110,-70,-30,10,40].map(y=>Math.round(Z.shore(y))).join(',')+' | parrilla x: '+__G.rivals.map(c=>Math.round(c.x)).join(',')+' | jugador x '+Math.round(__G.P.x);}));await b.close();})();
