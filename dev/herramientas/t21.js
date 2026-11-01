const {chromium}=require('playwright');
(async()=>{
 const b=await chromium.launch();
 for(const [w,h,tag,pre] of [[375,667,'se',0],[844,390,'land',0],[430,932,'max',1],[390,844,'ret',1]]){
 const ctx=await b.newContext({viewport:{width:w,height:h},deviceScaleFactor:3,hasTouch:true,isMobile:true});
 if(pre)await ctx.addInitScript(()=>{try{localStorage.setItem('ct_av','lucia');localStorage.setItem('ct_pname','Jose');localStorage.setItem('ct_moto','sombra');}catch(e){}});
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ghp/index.html');await p.waitForTimeout(1500);await p.screenshot({path:`s-${tag}-title.png`});
 await p.tap('#bPlay');await p.waitForTimeout(600);await p.screenshot({path:`s-${tag}-pilot.png`});
 console.log(tag,JSON.stringify(errs));}
 await b.close();})();
