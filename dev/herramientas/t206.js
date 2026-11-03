const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1500);
 const proto=fs.readFileSync('stk_proto.js','utf8');
 const urls=await p.evaluate(async(proto)=>{const mixc=(h,o,t)=>{const q=x=>[parseInt(x.slice(1,3),16),parseInt(x.slice(3,5),16),parseInt(x.slice(5,7),16)];const A=q(h),B=q(o);return '#'+A.map((v,i)=>Math.round(v+(B[i]-v)*t).toString(16).padStart(2,'0')).join('');};
  eval(proto+';window.stkDecor=stkDecor;');await new Promise(r=>__ski.load(r));const m=__ski.MOTOS[0],out=[];
  const cfgs=[{vinyl:'llamas',vcol:'#ffd21a',logo:'jj',num:7},{vinyl:'rayas',vcol:'#ffffff',logo:'roxy',num:23},{vinyl:'cuadros',vcol:'#111111',logo:'ct',num:99}];
  for(const c of cfgs){const pp=Object.assign(__ski.paintOf(m),c,{name:'BRAVA'});const d=__ski.paint(pp);const cv=document.createElement('canvas');cv.width=d.width;cv.height=d.height;const g=cv.getContext('2d');g.putImageData(d,0,0);__ski.decor(g,m,pp);stkDecor(g,pp,__ski.D);
   const c2=document.createElement('canvas');c2.width=d.width/2;c2.height=d.height/2;const g2=c2.getContext('2d');g2.fillStyle='#22345a';g2.fillRect(0,0,c2.width,c2.height);g2.drawImage(cv,0,0,c2.width,c2.height);out.push(c2.toDataURL());}
  return out;},proto);
 urls.forEach((u,i)=>fs.writeFileSync('stk_'+i+'.png',Buffer.from(u.split(',')[1],'base64')));console.log('errs',JSON.stringify(errs));await b.close();})();
