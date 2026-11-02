import json
p='costa-turbo.html';s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
# 1) lago cerrado del todo (también junto a la salida)
RM=json.load(open('/tmp/claude-0/-home-user/e02bf71e-076d-586d-89ee-84e1312586e6/scratchpad/costa_real/realmap5.json'))
i0=s.index("const RMAP={");i1=s.index("let RMD=null;",i0)
s=s[:i0]+"const RMAP={w:%d,h:%d,c:3,src:'%s'};const RCOR=%s;const RSPOTS=%s;"%(RM['w'],RM['h'],RM['src'],json.dumps(RM['cor'],separators=(',',':')),json.dumps(RM['spots'],separators=(',',':')))+s[i1:]
# más allá del borde derecho del mapa también es tierra
rep("if(col>=RMAP.w)return 6;","if(col>=RMAP.w){const v=RMD[row*RMAP.w+RMAP.w-1];return v===0||v>=5?7:v;}")
# 2) válvula de descarga STAGE 3: el «stu» + 5 soplidos de aire, cada uno 3 dB más bajo y un poco más grave, sin graves (<400 Hz)
rep("bov(st,sp){if(!this.ok())return;st=clamp(st|0,1,3);sp=clamp(sp||0,0,1);",
"""bovA(k){const c=this.ctx,t0=c.currentTime+.01;this.bovT=t0+1;
  const h1=c.createBiquadFilter(),h2=c.createBiquadFilter();h1.type=h2.type='highpass';h1.frequency.value=h2.frequency.value=400;h1.Q.value=h2.Q.value=.707;h1.connect(h2);h2.connect(this.sfx);const bus=h1;
  this.tone({at:t0,w:'sine',f:4600,f2:1500,v:.06*k,a:.005,t:.7,bus});
  this.hiss({at:t0,ft:'bandpass',f:2900,f2:1300,q:1.3,v:.62*k,a:.003,t:.11,bus});
  const u=t0+.08;this.hiss({at:u,ft:'bandpass',f:3200,q:1,v:.33*k,a:.001,t:.014,bus});this.hiss({at:u,ft:'bandpass',f:1150,f2:450,q:2.4,v:1.1*k,a:.003,t:.075,bus});this.tone({at:u,w:'triangle',f:260,f2:120,v:.3*k,a:.003,t:.07,bus});
  const st=Math.pow(10,-3/20);let a=k*st,p=1,t=t0+.13,d=.137;
  for(let i=0;i<5;i++){p*=.95;this.hiss({at:t,ft:'bandpass',f:2900*p,f2:1300*p,q:1.3,v:.62*a,a:.003,t:.11,bus});this.hiss({at:t+.08,ft:'bandpass',f:2100*p,f2:1400*p,q:3,v:.45*a,a:.002,t:.05,bus});t+=d;d*=1.06;a*=st;}},
 bov(st,sp){if(!this.ok())return;st=clamp(st|0,1,3);sp=clamp(sp||0,0,1);if(st===3){this.bovA(.6+.4*sp);return;}""")
# mientras suena la válvula del STAGE 3 baja el ruido del agua para que se oiga
rep("engineSet(rpm,spd,boost,thr,exh,tur,idle,drift){const e=this.eng;if(!e)return;",
    "engineSet(rpm,spd,boost,thr,exh,tur,idle,drift){const e=this.eng;if(!e)return;if(this.bovT&&this.bovT>this.ctx.currentTime)spd*=.3;")
# 3) bares en el minimapa
rep("g.translate(MW/2,MH*.62);g.rotate(P.h);",
    "for(const o of G.zone.big||[]){if(o.t!=='pgbar')continue;const x=tx(o.x),y=ty(o.y);if(x<-6||x>MW+6||y<-6||y>MH+6)continue;g.fillStyle=o.k==='jj'?'#e3202b':'#a0632f';g.beginPath();g.roundRect(x-4.5,y-4.5,9,9,2);g.fill();g.strokeStyle='#fff';g.lineWidth=1.3;g.stroke();}\n g.translate(MW/2,MH*.62);g.rotate(P.h);")
rep("const APP_VER=101;","const APP_VER=102;")
open(p,'w').write(s);print('ok',len(s))
