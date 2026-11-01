const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({args:['--autoplay-policy=no-user-gesture-required']});const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await p.waitForTimeout(1000);await p.click('#bPlay');await p.waitForTimeout(200);
 const res=[];for(const st of [1,2,3]){
  await p.evaluate(st=>{__G.free=true;__G.zi=3;__G.parts={bov:st};__goMap();__T.startRace();window.__calls=[];const o=__S.bov.bind(__S);__S.bov=(a,b)=>{window.__calls.push([a,+b.toFixed(2),__S.ctx&&__S.ctx.state]);o(a,b);};},st);
  await p.waitForTimeout(3600);await p.keyboard.down('ArrowUp');await p.waitForTimeout(4000);await p.keyboard.up('ArrowUp');await p.waitForTimeout(800);
  res.push(await p.evaluate(()=>JSON.stringify(window.__calls)));}
 console.log(res.join(' | '),JSON.stringify(errs));await b.close();})();
