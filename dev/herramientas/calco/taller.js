const {chromium}=require('playwright');const fs=require('fs');
const img='data:image/png;base64,'+fs.readFileSync('ski_roja.png').toString('base64');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:2})).newPage();
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1000);await p.evaluate(()=>{__G.money=48500;});
 await p.click('#bShop');await p.waitForTimeout(500);
 await p.evaluate(img=>{const st=document.createElement('style');st.textContent=`.ski3q{position:relative;flex:1;height:200px;border-radius:16px;overflow:hidden;background:linear-gradient(180deg,#9fdcf5 0%,#d8f2fb 46%,#3cc3dd 47%,#1488c8 75%,#0d63ad 100%);display:grid;place-items:center}.ski3q img{width:94%;filter:drop-shadow(0 8px 8px rgba(0,20,60,.35))}`;document.head.append(st);
  const pv=document.querySelector('#sPv');const d=document.createElement('div');d.className='ski3q';d.innerHTML='<img src="'+img+'">';pv.replaceWith(d);document.querySelector('#sName').textContent='YAMAHA FX';},img);
 await p.waitForTimeout(300);await p.screenshot({path:'taller_foto.png'});await b.close();})();
