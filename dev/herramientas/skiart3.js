// Moto ilustrada pintada por piezas (1 casco abajo, 2 casco arriba, 3 tapa, 4 detalles, 5 asiento; 6 negro fijo)
let SKI_D=null,SKI_O=null,SKI_P=null,RIVA_IM=null;const SKI_CACHE=new Map();
function skiMapLoad(cb){if(SKI_D){cb&&cb();return;}if(!SKI_P)SKI_P=Promise.all([SKI_MAP.map,SKI_MAP.img].map(s=>new Promise(r=>{const im=new Image();im.onload=()=>{const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const g=c.getContext('2d');g.drawImage(im,0,0);r(g.getImageData(0,0,im.width,im.height));};im.src=s;})).concat([new Promise(r=>{const im=new Image();im.onload=()=>{RIVA_IM=im;r();};im.onerror=()=>r();im.src=RIVA_ST.logo;})])).then(([a,b])=>{SKI_D=a;SKI_O=b;});SKI_P.then(()=>cb&&cb());}
function skiPaint(p){const key=[p.hull,p.deck,p.hood,p.stripe,p.seat].join(',');if(SKI_CACHE.has(key))return SKI_CACHE.get(key);
 const s=SKI_D.data,o0=SKI_O.data,out=new ImageData(SKI_D.width,SKI_D.height),o=out.data;
 const hx=c=>[parseInt(c.slice(1,3),16),parseInt(c.slice(3,5),16),parseInt(c.slice(5,7),16)],lu=c=>(c[0]*.299+c[1]*.587+c[2]*.114)/255;
 const T=[null,hx(p.hull),hx(p.deck),hx(p.hood),hx(p.stripe),hx(p.seat)],R=SKI_MAP.ref,DM=[1];
 for(let k=1;k<=5;k++){const d=Math.abs(lu(T[k])-R[k]);DM[k]=d>.45?.38:d>.25?.6:.9;}
 for(let i=0;i<s.length;i+=4){const A=o0[i+3];o[i+3]=A;if(A<4)continue;const L=Math.round(s[i]/36);
  if(L<1||L>5){o[i]=o0[i];o[i+1]=o0[i+1];o[i+2]=o0[i+2];continue;}
  const c=T[L],q=s[i+1]/90,t=Math.min(1,Math.max(0,(.62-q)/.32));const f=(1+(q-1)*DM[L])*(1-t)+q*t;let r,g,b;
  if(f<=1){r=c[0]*f;g=c[1]*f;b=c[2]*f;}else{const u=Math.min(1,(f-1)*.55);r=c[0]+(255-c[0])*u;g=c[1]+(255-c[1])*u;b=c[2]+(255-c[2])*u;}
  if(lu(c)<.12){r=Math.max(r,30*q);g=Math.max(g,33*q);b=Math.max(b,38*q);}
  o[i]=r;o[i+1]=g;o[i+2]=b;}
 if(SKI_CACHE.size>16)SKI_CACHE.delete(SKI_CACHE.keys().next().value);SKI_CACHE.set(key,out);return out;}
