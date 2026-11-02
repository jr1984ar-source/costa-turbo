const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();
 await p.goto('file://'+process.cwd()+'/'+(process.argv[2]||'ct-wrapped2.html'));await p.waitForTimeout(1000);
 let k=0;for(const zi of [7,15,16]){await p.evaluate(zi=>{__T.newGame(1);__G.zi=zi;__goMap();},zi);await p.waitForTimeout(300);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(3300);await p.screenshot({path:(process.argv[3]||'v91-')+(k++)+'.png',clip:{x:0,y:120,width:393,height:430}});}
 await b.close();})();
