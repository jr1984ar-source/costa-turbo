import re
p='costa-turbo.html';s=open(p).read()
a=" ctx.save();ctx.lineJoin='round';ctx.lineCap='round';ctx.strokeStyle='rgba(255,255,255,.06)';ctx.lineWidth=C.W;ctx.beginPath();let st=false;for(let i=0;i<=C.n;i++){const k=i%C.n,x=C.x[k],y=C.y[k],vv=x>x0-C.W&&x<x1+C.W&&y>y0-C.W&&y<y1+C.W;if(vv){st?ctx.lineTo(x,y):ctx.moveTo(x,y);st=true;}else st=false;}ctx.stroke();ctx.restore();\n"
assert s.count(a)==1,s.count(a)
s=s.replace(a,'')
assert s.count("const APP_VER=46;")==1;s=s.replace("const APP_VER=46;","const APP_VER=47;")
open(p,'w').write(s)
q='circ_draw.js';t=open(q).read()
if t.count(a)==1:t=t.replace(a,'');open(q,'w').write(t)
print('ok')
