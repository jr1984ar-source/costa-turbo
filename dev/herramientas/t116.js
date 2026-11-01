const {chromium}=require('playwright');const fs=require('fs');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1000);
 const url=await p.evaluate(()=>{const T=__gearT,H=T.GEAR.helm.slice(1),c=document.createElement('canvas');c.width=1200;c.height=560;const g=c.getContext('2d');g.fillStyle='#8fd8f6';g.fillRect(0,0,1200,560);
  H.forEach((he,k)=>{const x=(k%4)*300,y=Math.floor(k/4)*280;const av=T.AVATARS[k%T.AVATARS.length].face;const v=T.GEAR.vest[1+(k%5)],s=T.GEAR.suit[1+(k%6)];g.save();g.translate(x-60,y+150);g.scale(1.1,1.1);T.drawRiderProfile(g,av,v.c,{helm:he,vest:v,suit:s});g.restore();
   const pc=document.createElement('canvas');pc.width=120;pc.height=120;T.drawPortrait(pc,T.AVATARS[k%T.AVATARS.length],{helm:he,vest:v,suit:s});g.drawImage(pc,x+175,y+150,110,110);g.fillStyle='#000';g.font='bold 14px sans-serif';g.fillText(he.b+' '+he.n,x+8,y+20);});
  return c.toDataURL();});
 fs.writeFileSync('helms.png',Buffer.from(url.split(',')[1],'base64'));console.log(JSON.stringify(errs));await b.close();})();
