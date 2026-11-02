const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:2})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1200);
 await p.evaluate(()=>__T.startFree(3));await p.waitForTimeout(300);await p.evaluate(()=>__T.startRace());await p.waitForTimeout(4200);
 const r=await p.evaluate(()=>{const st=document.querySelector('#stage').getBoundingClientRect(),pl=document.querySelector('#padL').getBoundingClientRect(),ar=document.querySelector('#arL').getBoundingClientRect(),rv=document.querySelector('#padL .pill.rev').getBoundingClientRect();return {stageH:Math.round(st.height),padTop:Math.round(pl.top),padH:Math.round(pl.height),flechasTop:Math.round(ar.top),frenoBottom:Math.round(rv.bottom),htmlH:document.documentElement.getBoundingClientRect().height};});
 console.log(JSON.stringify(r));await p.screenshot({path:process.argv[2]||'pads.png'});await b.close();})();
