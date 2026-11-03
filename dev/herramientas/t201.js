// vista aérea de una zona del lago, juntando losetas del mapa
const {chromium}=require('playwright');const fs=require('fs');
const [x0,y0,x1,y1,out,sc]=[+process.argv[2],+process.argv[3],+process.argv[4],+process.argv[5],process.argv[6],+(process.argv[7]||.5)];
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:393,height:852},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped2.html');await p.waitForTimeout(1500);
 await p.evaluate(()=>__T.startFree(22));await p.waitForTimeout(800);
 const url=await p.evaluate(([x0,y0,x1,y1,sc])=>{const T=400,c=document.createElement('canvas');c.width=Math.ceil((x1-x0)*sc);c.height=Math.ceil((y1-y0)*sc);const g=c.getContext('2d');g.fillStyle='#1b84c4';g.fillRect(0,0,c.width,c.height);
  for(let i=Math.floor(y0/T);i<=Math.floor(y1/T);i++)for(let j=Math.floor(x0/T);j<=Math.floor(x1/T);j++){const t=__rtile(i,j);g.drawImage(t,(j*T-x0)*sc,(i*T-y0)*sc,T*sc,T*sc);}
  // objetos grandes (bares, gasolineras)
  return c.toDataURL('image/png');},[x0,y0,x1,y1,sc]);
 fs.writeFileSync(out,Buffer.from(url.split(',')[1],'base64'));console.log('ok',out,'errs',JSON.stringify(errs));await b.close();})();
