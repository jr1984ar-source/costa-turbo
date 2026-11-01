const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 let body=fs.readFileSync('costa-turbo.html','utf8');body=body.replace("requestAnimationFrame(frame);\n})();","window.__G=G;window.__goMap=goMap;requestAnimationFrame(frame);\n})();");
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();
 for(const vp of [{width:390,height:780},{width:375,height:667}]){
 const p=await (await b.newContext({viewport:vp,deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.waitForTimeout(200);
 await p.click('#gPaint');await p.waitForTimeout(300);
 const fit=await p.evaluate(()=>{const s=document.querySelector('#scrPaint');return {scroll:s.scrollHeight>s.clientHeight+2,save:Math.round(document.querySelector('#pSave').getBoundingClientRect().bottom),vh:innerHeight};});
 const rows=await p.$$('.prow');
 const pick=async(r,i)=>{const sw=await rows[r].$$('.sw');await sw[i].scrollIntoViewIfNeeded();await sw[i].click();};
 await pick(0,10);await pick(1,0);await pick(2,10);await pick(3,6);await pick(4,3);
 await p.fill('#pName','La Bala');await p.waitForTimeout(200);await p.screenshot({path:'paint-'+vp.width+'.png'});
 await p.click('#pSave');await p.waitForTimeout(300);await p.screenshot({path:'garage-paint-'+vp.width+'.png'});
 const gname=await p.evaluate(()=>document.querySelector('#gName').textContent);
 await p.click('#gGo');await p.waitForTimeout(300);await p.click('#mGo');await p.waitForTimeout(3600);await p.keyboard.down('ArrowUp');await p.waitForTimeout(1500);await p.screenshot({path:'race-paint-'+vp.width+'.png'});
 await p.evaluate(()=>{__G.money=20000;const G=__G,r=G.zone.ring;});
 await p.evaluate(()=>{__G.zi=1;__goMap();});await p.keyboard.up('ArrowUp');await p.waitForTimeout(300);await p.click('#mGo');await p.waitForTimeout(3600);
 await p.evaluate(()=>{const G=__G,r=G.zone.ring;G.P.y=r.y+40;G.P.x=r.x;G.P.v=90;});await p.waitForTimeout(900);
 await p.click('#rxBuy');await p.waitForTimeout(150);await p.click('#rxBuy');await p.waitForTimeout(150);
 const lv=await p.evaluate(()=>({parts:JSON.stringify(__G.parts),money:__G.money,btn:document.querySelector('#rxBuy').textContent}));
 await p.screenshot({path:'roxy-levels-'+vp.width+'.png'});
 console.log(vp.width,JSON.stringify(fit),gname,JSON.stringify(lv),JSON.stringify(errs));}
 await b.close();})();
