import shutil
H='costa-turbo.html'
shutil.copy(H,'costa-turbo.pre-v61.html')
h=open(H).read()
def rep(s,a,b,n=1):
    c=s.count(a)
    assert c==n,(c,a[:90])
    return s.replace(a,b)
h=rep(h,"const APP_VER=60","const APP_VER=61")
# Bahamas: sin letrero de la avioneta
h=rep(h,"const[lx,ly]=[xs[i]+Math.cos(hs[i])*lat*.55,ys[i]+Math.sin(hs[i])*lat*.55];labels.push({x:lx,y:ly,txt:'AVIONETA HUNDIDA'});","")
# Pig Beach: cerdos en el agua, no encima de la isla
h=rep(h,"for(let k=0;k<5;k++){const a=a0+(k-2)*.28,d=best.rad+18+(k%2)*10;add({t:'pig',",
        "for(let k=0;k<6;k++){const a=a0+(k-2.5)*.26;let d=best.rad*.6;while(d<best.rad*4&&landIn(lands,best.x+Math.cos(a)*d,best.y+Math.sin(a)*d))d+=5;d+=18+(k%2)*14;add({t:'pig',")
# cerdos nadando junto al camino en tres sitios
a="if(!TR)for(let s=1200;s<Lp-1200;s+=1500+r()*1300){if(busy(s))continue;const i=I(s),lat=(r()-.5)*W*.5;add({t:'cray',"
h=rep(h,a,"if(!TR)for(const f of[.2,.5,.8]){let s=Lp*f;while(busy(s))s+=260;const i=I(s),sd=r()<.5?-1:1,e=sd<0?wl[i]:wr[i];for(let k=0;k<3;k++){const[x,y]=loc(i,sd*(e-48-(k%2)*30),(k-1)*34+(r()-.5)*10);add({t:'pig',x,y,ph:r()*6});}}\n "+a)
open(H,'w').write(h)
print('ok')
