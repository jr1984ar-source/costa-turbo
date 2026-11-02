const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:1})).newPage();
 await p.goto('file://'+process.cwd()+'/'+process.argv[2]);await p.waitForTimeout(1800);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(400);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(3600);
 // jugador fuera de juego: lejos delante para que los rivales no frenen por él
 await p.evaluate(()=>{const P=__G.P;P.inv=99;setInterval(()=>{const r=__G.rivals;const avg=r.reduce((a,c)=>a+c.y,0)/r.length;P.y=avg-300;P.x=__G.rivals[0].x;P.v=0;},100);});
 const t0=Date.now();for(let k=0;k<6;k++){await p.waitForTimeout(5000);console.log(await p.evaluate(()=>'fps-t '+__G.t.toFixed(1)+' riv '+__G.rivals.map(c=>Math.round(-c.y)+'/v'+Math.round(c.v)).join(' ')));}
 await b.close();})();
