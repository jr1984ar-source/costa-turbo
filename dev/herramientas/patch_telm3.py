p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:90],s.count(a))
    s=s.replace(a,b)
rep(" if(Z.theme==='tram'){const n3=noise1(seed+13),RC=230;"," let coveF=null;if(Z.theme==='tram'){const n3=noise1(seed+13),RC=230;")
rep("x=lerp(x,Math.min(x,fl),Math.pow(cv.q,.42));}return x;};","x=lerp(x,Math.min(x,fl),Math.pow(sm(cv.w,cv.w*.3,cv.d),.7));}return x;};coveF=cove;")
rep(" zone.swimX=y=>"," zone.cliffK=y=>{if(!coveF)return zone.kind(y)==='mount'?1:0;const cv=coveF(-y);return cv?sm(cv.w*.5,cv.w*.9,cv.d):1;};\n zone.swimX=y=>")
rep("if(Zn.kind(y)==='mount')g.drawImage(SP.cliffSh,sx-2,y,Zn.Z.theme==='tram'?72:46,2.4);",
    "const ck=Zn.cliffK(y);if(ck>0){g.globalAlpha=ck;g.drawImage(SP.cliffSh,sx-2,y,Zn.Z.theme==='tram'?72:46,2.4);g.globalAlpha=1;}")
old=" for(let y=y0-4;y<y1+4;y+=3){const kd=Zn.kind(y);if(kd!=='cala'&&kd!=='mount')continue;const sx=sh(y);if(kd==='cala'){g.fillStyle='#d9d3c6';g.fillRect(sx-24,y,26,3.2);g.fillStyle='rgba(120,110,95,.35)';for(let k=0;k<4;k++)g.fillRect(sx-24+hash2(Math.round(y),k,Zn.seed)*24,y+hash2(k,Math.round(y),3)*3,1.4,1.4);}else{"
new=""" if(Zn.Z.theme==='tram'){const pw=y=>26*(1-Zn.cliffK(y));g.beginPath();let st=0;for(let y=y0-4;y<=y1+4;y+=3){g[st++?'lineTo':'moveTo'](sh(y)+2,y);}for(let y=y1+4;y>=y0-4;y-=3)g.lineTo(sh(y)+2-pw(y),y);g.closePath();g.fillStyle='#d9d3c6';g.fill();
  g.fillStyle='rgba(120,110,95,.35)';for(let y=y0-4;y<y1+4;y+=3){const w=pw(y)-3;if(w<3)continue;const sx=sh(y);for(let k=0;k<4;k++)g.fillRect(sx-w+hash2(Math.round(y),k,Zn.seed)*w,y+hash2(k,Math.round(y),3)*3,1.4,1.4);}}
 for(let y=y0-4;y<y1+4;y+=3){const kd=Zn.kind(y);if(kd!=='cala'&&kd!=='mount')continue;const sx=sh(y),ck=Zn.cliffK(y);if(ck<=0)continue;g.globalAlpha=ck;{"""
rep(old,new)
rep("g.fillStyle='rgba(250,245,235,.22)';g.fillRect(sx-31,y,1.6,3.2);}}","g.fillStyle='rgba(250,245,235,.22)';g.fillRect(sx-31,y,1.6,3.2);}g.globalAlpha=1;}")
rep("const yy=cy*70+hash2(cy,1,Zn.seed)*40;if(Zn.kind(yy)!=='mount')continue;","const yy=cy*70+hash2(cy,1,Zn.seed)*40;if(Zn.cliffK(yy)<.7)continue;")
rep("const yy=cy*13+hash2(cy,4,Zn.seed)*7;if(Zn.kind(yy)!=='mount')continue;","const yy=cy*13+hash2(cy,4,Zn.seed)*7;if(Zn.cliffK(yy)<.6)continue;")
open(p,'w').write(s);print('ok')
