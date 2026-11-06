const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:1})).newPage();
 const W=ms=>p.waitForTimeout(ms),E=(f,a)=>p.evaluate(f,a);
 await p.goto('file://'+process.cwd()+'/ct-wrapped.html');await W(1000);await p.click('#bPlay');await W(200);
 await E(n=>{__T.newGame();__G.zi=__Z.findIndex(z=>z.name===n);__goMap();},'BAHAMAS');await W(300);await E(()=>__T.startRace());await W(3800);
 const info=await E(()=>{const Z=__G.zone,C=Z.circ,pigs=Z.objs.filter(o=>o.t==='pig'),lb=Z.labels.find(l=>l.txt==='PIG BEACH');return{pigs:pigs.map(o=>({x:Math.round(o.x),y:Math.round(o.y),land:__landIn(Z.lands,o.x,o.y)})),lb};});
 console.log(JSON.stringify(info));
 await E(lb=>{const P=__G.P;P.x=lb.x-60;P.y=lb.y+160;P.v=0;P.cs=null;for(const c of __G.rivals){c.x=1e5;c.trail=[];}},info.lb);await W(500);
 await p.screenshot({path:'pig-0.png',clip:{x:0,y:0,width:390,height:690}});await b.close();})();
