const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 let body=fs.readFileSync('costa-turbo.html','utf8');body=body.replace("requestAnimationFrame(frame);\n})();","window.__G=G;requestAnimationFrame(frame);\n})();");
 fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>:root{color-scheme:light}body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');
 const b=await chromium.launch();
 for(const [vp,zi] of [[{width:390,height:780},1],[{width:390,height:780},0],[{width:844,height:390},1]]){
 const p=await (await b.newContext({viewport:vp,deviceScaleFactor:2})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1200);await p.click('#bPlay');await p.click('#gGo');await p.waitForTimeout(200);
 if(zi)await p.evaluate(()=>{__G.zi=1;});await p.evaluate(()=>{});
 await p.evaluate(z=>{if(z){__G.zi=1;}},zi);
 if(zi){await p.evaluate(()=>{document.querySelector('#mGo');});}
 await p.evaluate(z=>{if(z){window.__G.zi=1;}},zi);
 await p.evaluate(()=>{});
 await p.click('#mGo');await p.waitForTimeout(3600);
 await p.evaluate(()=>{const G=__G,r=G.zone.ring;G.P.y=r.y+40;G.P.x=r.x;G.P.v=90;});await p.waitForTimeout(900);
 const vis=await p.evaluate(()=>{const b=[...document.querySelectorAll('#scrRoxy .btn.p,#scrJJ .btn.p')].find(x=>x.offsetParent);if(!b)return 'no-btn';const r=b.getBoundingClientRect();return {bottom:Math.round(r.bottom),vh:innerHeight,mode:__G.mode,pads:getComputedStyle(document.querySelector('#padL')).display};});
 await p.screenshot({path:'bar-nopads-'+vp.width+'-'+zi+'.png'});
 await p.evaluate(()=>{const o=document.querySelector('#rxOut')&&!document.querySelector('#scrRoxy').hidden?'#rxOut':'#jjOut';document.querySelector(o).click();});await p.waitForTimeout(400);
 const back=await p.evaluate(()=>({mode:__G.mode,pads:getComputedStyle(document.querySelector('#padL')).display}));
 console.log(vp.width,zi,JSON.stringify(vis),JSON.stringify(back),JSON.stringify(errs));}
 await b.close();})();
