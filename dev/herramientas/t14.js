const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 let body=fs.readFileSync('costa-turbo.html','utf8');body=body.replace("requestAnimationFrame(frame);\n})();","window.__G=G;window.__goMap=goMap;requestAnimationFrame(frame);\n})();");
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();
 for(const vp of [{width:390,height:780},{width:375,height:667},{width:844,height:390}]){
 const p=await (await b.newContext({viewport:vp,deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.click('#gGo');await p.waitForTimeout(200);
 await p.evaluate(()=>{__G.zi=1;__goMap();});await p.waitForTimeout(300);await p.click('#mGo');await p.waitForTimeout(3600);
 await p.evaluate(()=>{const G=__G,r=G.zone.ring;G.P.y=r.y+40;G.P.x=r.x;G.P.v=90;});await p.waitForTimeout(900);
 const vis=await p.evaluate(()=>{const r=document.querySelector('#rxBuy').getBoundingClientRect(),s=document.querySelector('#scrRoxy .shop');return {buyBottom:Math.round(r.bottom),vh:innerHeight,scroll:s.scrollHeight>s.clientHeight+2};});
 await p.screenshot({path:'roxy-nopads-'+vp.width+'.png'});
 console.log(vp.width+'x'+vp.height,JSON.stringify(vis),JSON.stringify(errs));}
 await b.close();})();
