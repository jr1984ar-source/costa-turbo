p='costa-turbo.html';s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
# en cada partida salen en sitios nuevos las motos de otra gente (y las que retan) y las chicas que piden paseo
rep("const ids=MOTOS.map(m=>m.id);for(let n=0,t=0;n<14&&t<800;t++){const x=rx(),y=ry();if(!free(x,y,100))continue;M.push({t:'npcjet',x,y,h:r()*TAU,th:null,v:120+r()*110,id:ids[(r()*ids.length)|0],tt:r()*3,trail:[],vx:0,vy:0,flash:0});n++;}",
    "const rr=rng((Math.random()*1e9)|0),rx2=()=>150+rr()*(RMW-300),ry2=()=>top+rr()*(bot-top);\n const ids=MOTOS.map(m=>m.id);for(let n=0,t=0;n<14&&t<800;t++){const x=rx2(),y=ry2();if(!free(x,y,100))continue;M.push({t:'npcjet',x,y,h:rr()*TAU,th:null,v:120+rr()*110,id:ids[(rr()*ids.length)|0],tt:rr()*3,trail:[],vx:0,vy:0,flash:0});n++;}")
rep("const fares=[];for(let t=0;t<40000&&fares.length<10;t++){const x=150+r()*(RMW-300),y=RM_TOP+600+r()*(RM_BOT-RM_TOP-900);",
    "const fares=[];for(let t=0;t<40000&&fares.length<10;t++){const x=150+rr()*(RMW-300),y=RM_TOP+600+rr()*(RM_BOT-RM_TOP-900);")
rep("const id=ids[(k*2+((r()*ids.length)|0))%ids.length]","const id=ids[(k*2+((rr()*ids.length)|0))%ids.length]")
rep("fares.forEach((f,k)=>O.push({t:'pgfare',","{const off=(rr()*10)|0;fares.forEach((f,k0)=>{const k=k0+off;O.push({t:'pgfare',")
rep("ph:k*1.3,on:1,rt:0,name:BN[k%BN.length]}));}","ph:k*1.3,on:1,rt:0,name:BN[k%BN.length]});});}}")
# etiqueta de la tarjeta del Modo libre: LIBRE
rep("Z.obj==='chase'?['PERSECUCIÓN','#ff3b4f','#1e4fd8','siren']:['CARRERA','#ffa04a','#e2451a','flag'];","Z.obj==='chase'?['PERSECUCIÓN','#ff3b4f','#1e4fd8','siren']:Z.obj==='free'?['LIBRE','#7be35a','#1f9e52','flag']:['CARRERA','#ffa04a','#e2451a','flag'];")
rep("if(zone.lane)D.push({n:'LA RECTA',x:zone.lane.x,y:zone.lane.y0+80});","if(zone.lane)D.push({n:'LA RECTA',x:zone.lane.x+170,y:zone.lane.y0+80});")
rep("if(DR.st==='wait'){if(!G.pgRace&&!G.pgMis&&!G.demo){","if(DR.st==='wait'){if(!G.pgRace&&!G.pgMis&&!G.demo&&!(G._stopCool>0)){")
rep("const APP_VER=110;","const APP_VER=111;")
open(p,'w').write(s);print('ok')
