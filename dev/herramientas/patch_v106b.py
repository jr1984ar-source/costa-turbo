p='costa-turbo.html';s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
# chicas en las playas que quieren dar un paseo
rep(" O.push({t:'pgtarget',x:0,y:0,ry:1e9});}",""" O.push({t:'pgtarget',x:0,y:0,ry:1e9});
 const fares=[];for(let t=0;t<40000&&fares.length<10;t++){const x=150+r()*(RMW-300),y=RM_TOP+600+r()*(RM_BOT-RM_TOP-900);if(rmV(x,y)!==2)continue;let wp=null;
  for(let a=0;a<12&&!wp;a++){const ca=Math.cos(a/12*TAU),sa=Math.sin(a/12*TAU);for(let d=20;d<=60;d+=10){const px=x+ca*d,py=y+sa*d;if(rmV(px,py)===0){const qx=px+ca*60,qy=py+sa*60;if(free(qx,qy,40))wp=[qx,qy];break;}}}
  if(!wp||fares.some(f=>Math.hypot(f.x-x,f.y-y)<1600))continue;fares.push({x,y,bx:wp[0],by:wp[1]});}
 const HAIR=['#f2cf63','#5a3218','#111111','#b5402a'],BIK=['#ff3f8e','#22c4ff','#ffd21a','#7be35a','#ff7a1a'],BN=['CALA BLANCA','PLAYA DEL PUEBLO','CALA DEL PINAR','PLAYA LARGA','CALA ROJA','PLAYA DEL SOL','CALA FONDA','PLAYA DORADA','CALA VERDE','PLAYA CHICA'];
 fares.forEach((f,k)=>O.push({t:'pgfare',x:f.x,y:f.y,bx:f.bx,by:f.by,hair:HAIR[k%4],bik:BIK[k%5],ph:k*1.3,on:1,rt:0,name:BN[k%BN.length]}));}""")
rep("else if(R&&R.st==='run'){const o=R.rv;if(Math.hypot(P.x-R.d.x,P.y-R.d.y)<130)pgRaceEnd(true);else if(R.i>=R.path.length-1&&Math.hypot(o.x-R.d.x,o.y-R.d.y)<100)pgRaceEnd(false);}}",
"""else if(R&&R.st==='run'){const o=R.rv;if(Math.hypot(P.x-R.d.x,P.y-R.d.y)<130)pgRaceEnd(true);else if(R.i>=R.path.length-1&&Math.hypot(o.x-R.d.x,o.y-R.d.y)<100)pgRaceEnd(false);}}
 // paseos: frenas junto a una chica de la playa, se sube y la llevas a donde te pide
 {const M2=G.pgMis;if(!Zn._fares)Zn._fares=Zn.objs.filter(o=>o.t==='pgfare');
  if(!M2&&!G.pgRace&&!G.demo&&!(G._stopCool>0)){for(const f of Zn._fares){if(!f.on){f.rt-=dt;if(f.rt<=0)f.on=1;continue;}const d=Math.hypot(P.x-f.bx,P.y-f.by);if(d<520&&!f.called){f.called=1;pop(f.x,f.y-30,'¡LLÉVAME!','#ff8fc4');}else if(d>900)f.called=0;
    if(d<70&&P.v<P.st.maxV*.55){const opts=(Zn.pgDest||[]).concat(Zn._fares.filter(q=>q!==f).map(q=>({n:q.name,x:q.bx,y:q.by}))).filter(q=>{const dd=Math.hypot(q.x-f.bx,q.y-f.by);return dd>2000&&dd<8000;});if(!opts.length)continue;
     const q=opts[(Math.random()*opts.length)|0],dist=Math.hypot(q.x-f.bx,q.y-f.by);f.on=0;f.rt=40;G.pgMis={kind:'taxi',x:q.x,y:q.y,n:q.n,hair:f.hair,bik:f.bik,t:0,lim:dist/(P.st.maxV*.55)+12,pay:200+Math.round(dist/400)*10};Snd.pickup();msg('¡SUBE!','Llévala a '+q.n,'#ff8fc4');break;}}}
  else if(M2&&M2.kind==='taxi'){M2.t+=dt;if(P.air>0&&!M2.jmp){M2.jmp=1;pop(P.x,P.y-50,['¡AAAAH!','¡Ayyy!','¡Uuuh!','¡Más alto!'][(Math.random()*4)|0],'#ff8fc4');}if(P.air<=0)M2.jmp=0;
   if(P.crash>0){G.pgMis=null;msg('¡SE HA CAÍDO AL AGUA!','Paseo perdido','var(--red)');Snd.fail();}
   else if(Math.hypot(P.x-M2.x,P.y-M2.y)<120&&P.v<P.st.maxV*.55){const tip=M2.t<=M2.lim?Math.round(M2.pay*.05)*10:0;G.money+=M2.pay+tip;G.score+=M2.pay+tip;saveWallet();Snd.cash();buzz(60);G.pgMis=null;G._stopCool=2.5;msg('¡GRACIAS, GUAPO!','+'+pts(M2.pay)+' PESETAS'+(tip?' · PROPINA +'+pts(tip):''),'#ff8fc4');}}}""")
rep(" if(!G.demo&&!G.pgRace&&!(G._stopCool>0))for(const o of Zn.big){"," if(!G.demo&&!G.pgRace&&!G.pgMis&&!(G._stopCool>0))for(const o of Zn.big){")
# la chica sentada detrás del piloto
rep("else ctx.drawImage((c.isP&&!G.demo&&SP.jetP?SP.jetP:SP.jet[c.id]).c,-16,-34,32,68);ctx.restore();",
    "else{ctx.drawImage((c.isP&&!G.demo&&SP.jetP?SP.jetP:SP.jet[c.id]).c,-16,-34,32,68);if(c.isP&&G.pgMis&&G.pgMis.kind==='taxi')drawPass(ctx,G.pgMis);}ctx.restore();")
rep("function drawGirl(g,x,y,hair,bik,wave,ph){","""function drawPass(g,m){g.save();g.translate(0,15);g.strokeStyle='#f0b38a';g.lineWidth=2.4;g.lineCap='round';g.beginPath();g.moveTo(-5,-1);g.lineTo(-6.5,-9);g.moveTo(5,-1);g.lineTo(6.5,-9);g.stroke();
 g.fillStyle='#f0b38a';g.beginPath();g.ellipse(0,1.5,5.2,6.5,0,0,TAU);g.fill();g.fillStyle=m.bik;g.fillRect(-5.2,-.5,10.4,2.8);g.fillStyle=m.hair;g.beginPath();g.arc(0,-3.5,4.3,0,TAU);g.fill();g.beginPath();g.ellipse(0,2,3.3,5.2,0,0,TAU);g.fill();g.restore();}
function drawGirl(g,x,y,hair,bik,wave,ph){""")
rep("case 'pgtarget':{","""case 'pgfare':{if(!o.on)return;const P=G.P,near=P&&Math.hypot(P.x-o.bx,P.y-o.by)<650;drawGirl(ctx,o.x,o.y,o.hair,o.bik,near||Math.sin(G.t*.8+o.ph)>.5,G.t*3+o.ph);
  if(near&&!G.pgMis&&!G.pgRace){const p=1+Math.sin(G.t*5)*.08;ctx.save();ctx.translate(o.bx,o.by);ctx.fillStyle='rgba(255,143,196,.16)';ctx.beginPath();ctx.arc(0,0,64*p,0,TAU);ctx.fill();ctx.setLineDash([8,6]);ctx.lineDashOffset=-G.t*24;ctx.strokeStyle='#ff8fc4';ctx.lineWidth=3;ctx.beginPath();ctx.arc(0,0,56*p,0,TAU);ctx.stroke();ctx.setLineDash([]);ctx.rotate(G.camA||0);ctx.fillStyle='#ff8fc4';ctx.font='800 17px "Saira Condensed",sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText('PASEO',0,1);ctx.restore();
   ctx.save();ctx.translate(o.x,o.y);ctx.rotate(G.camA||0);label(0,-36,'¡LLÉVAME!',o.name);ctx.restore();}}return;
 case 'pgtarget':{""")
rep("if(o.t==='bgirl'||o.t==='bpalm'||o.t==='faro'||o.t==='pgbar'||o.t==='pggas'||o.t==='pglabel'||o.t==='turtle'||o.t==='pig'||o.t==='pgtarget')continue;","if(o.t==='bgirl'||o.t==='bpalm'||o.t==='faro'||o.t==='pgbar'||o.t==='pggas'||o.t==='pglabel'||o.t==='turtle'||o.t==='pig'||o.t==='pgtarget'||o.t==='pgfare')continue;")
rep("if(G.pgMis){let x=tx(G.pgMis.x)","for(const f of G.zone._fares||[]){if(!f.on||G.pgMis)continue;const x=tx(f.bx),y=ty(f.by);if(x<-4||x>MW+4||y<-4||y>MH+4)continue;g.fillStyle='#ff8fc4';g.beginPath();g.arc(x,y,3,0,TAU);g.fill();}\n if(G.pgMis){let x=tx(G.pgMis.x)")
open(p,'w').write(s);print('ok',len(s))
