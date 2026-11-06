const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(()=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name==='BAHAMAS');__goMap();});await W(300);await E(()=>__T.startRace());await W(500);
 const r=await E(()=>{const Zn=__G.zone,C=Zn.circ,out=[];for(const c of __crafts()){const hit=Zn.lands.filter(L=>L.solid!==false&&c.x>=L.bb[0]&&c.x<=L.bb[2]&&c.y>=L.bb[1]&&c.y<=L.bb[3]).map(L=>[Math.round(L.bb[0]),Math.round(L.bb[1]),Math.round(L.bb[2]),Math.round(L.bb[3])]);out.push({id:c.id,x:Math.round(c.x),y:Math.round(c.y),cs:c.cs,land:__landIn(Zn.lands,c.x,c.y),bbs:hit.slice(0,3)});}return{out,x0:C.x[0],y0:C.y[0],wl0:C.wl[0]};});
 console.log(JSON.stringify(r));await b.close();})();
