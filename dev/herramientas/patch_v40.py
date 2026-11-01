p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
rep(".cmap{position:absolute;right:max(8px,env(safe-area-inset-right,0px));top:110px;width:112px;height:112px;border-radius:14px;background:rgba(8,22,48,.5);border:1px solid rgba(255,255,255,.2);box-shadow:0 4px 12px rgba(0,10,30,.25)}",
    ".cmap{position:absolute;right:max(8px,env(safe-area-inset-right,0px));top:110px;width:112px;height:112px;opacity:.8}")
rep(" for(const Ld of G.zone.lands){if(Ld.draw===false&&!Ld.mole)continue;g.fillStyle=Ld.sandPts?'#cdb88a':'#9c9480';g.beginPath();Ld.pts.forEach(([x,y],i)=>i?g.lineTo(x*sc+ox,y*sc+oy):g.moveTo(x*sc+ox,y*sc+oy));g.closePath();g.fill();}\n","")
rep("g.lineJoin='round';g.strokeStyle='rgba(255,255,255,.28)';g.lineWidth=Math.max(5,C.W*sc);g.beginPath();for(let i=0;i<=C.n;i++){const k=i%C.n;i?g.lineTo(C.x[k]*sc+ox,C.y[k]*sc+oy):g.moveTo(C.x[k]*sc+ox,C.y[k]*sc+oy);}g.stroke();g.strokeStyle='#ffffff';g.lineWidth=1.6;g.stroke();",
    "g.lineJoin='round';g.beginPath();for(let i=0;i<=C.n;i++){const k=i%C.n;i?g.lineTo(C.x[k]*sc+ox,C.y[k]*sc+oy):g.moveTo(C.x[k]*sc+ox,C.y[k]*sc+oy);}g.strokeStyle='rgba(0,20,50,.35)';g.lineWidth=5;g.stroke();g.strokeStyle='rgba(255,255,255,.8)';g.lineWidth=2.4;g.stroke();")
rep("const APP_VER=39;","const APP_VER=40;")
open(p,'w').write(s);print('ok')
