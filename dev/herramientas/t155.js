const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1000);
 await p.evaluate(()=>__T.startFree(5));await p.waitForTimeout(300);
 console.log(await p.evaluate(()=>{const Z=__G.zone,pr=Z.pier;return JSON.stringify({pier:pr,near:Z.objs.filter(o=>Math.abs(o.y-pr.y)<120).map(o=>o.t+':'+Math.round(o.x)+','+Math.round(o.y)),ramps:Z.objs.filter(o=>o.t==='ramp'&&o.y>pr.y-900&&o.y<pr.y+900).map(o=>Math.round(o.y)+'/'+o.sz),waves:Z.waves.map(w=>Math.round(w.y))});}));
 await b.close();})();
