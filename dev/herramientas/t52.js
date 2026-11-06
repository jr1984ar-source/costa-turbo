const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a),out={};
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 for(const zi of [2,18]){await E(zi=>{__G.free=true;__G.zi=zi;__goMap();__T.startRace();},zi);await W(3600);await p.keyboard.down('ArrowUp');await W(12000);await p.keyboard.up('ArrowUp');
  out['z'+zi]=await E(()=>({pMax:Math.round(__G.P.st.maxV),rivTarget:__G.rivals.map(c=>Math.round(c.st.maxV*c.skill)).join(','),pY:Math.round(-__G.P.y),riv:__G.rivals.map(c=>Math.round(-c.y)).join(',')}));}
 console.log(JSON.stringify(out),JSON.stringify(errs));await b.close();})();
