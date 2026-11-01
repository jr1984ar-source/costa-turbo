// Moto dibujada pintada por piezas: hull = casco abajo, deck = casco arriba, hood = tapa, stripe = detalles, seat = asiento
let SKI_MAPD=null,SKI_MAPP=null;const SKI_CACHE=new Map();
function skiMapLoad(cb){if(SKI_MAPD){cb&&cb();return;}if(SKI_MAPP){SKI_MAPP.then(()=>cb&&cb());return;}
 SKI_MAPP=new Promise(res=>{const im=new Image();im.onload=()=>{const c=document.createElement('canvas');c.width=im.width;c.height=im.height;const g=c.getContext('2d');g.drawImage(im,0,0);SKI_MAPD=g.getImageData(0,0,im.width,im.height);res();};im.src=SKI_MAP.src;});SKI_MAPP.then(()=>cb&&cb());}
function skiPaint(p){const key=[p.hull,p.deck,p.hood,p.stripe,p.seat].join(',');if(SKI_CACHE.has(key))return SKI_CACHE.get(key);
 const D=SKI_MAPD,w=D.width,h=D.height,s=D.data,out=new ImageData(w,h),o=out.data;
 const hx=c=>[parseInt(c.slice(1,3),16),parseInt(c.slice(3,5),16),parseInt(c.slice(5,7),16)];
 const C=[hx('#f2f4f7'),hx(p.hull),hx(p.deck),hx(p.hood),hx(p.stripe),hx(p.seat),[30,33,40],[16,18,24]];
 for(let i=0;i<s.length;i+=4){const A=s[i+3];if(A<4){o[i+3]=0;continue;}const L=Math.min(7,Math.round(s[i]/36)),c=C[L];
  if(L===7){o[i]=16;o[i+1]=18;o[i+2]=24;o[i+3]=A;continue;}
  const f=s[i+1]/160;let r=Math.min(255,c[0]*f),g=Math.min(255,c[1]*f),b=Math.min(255,c[2]*f);
  const la=s[i+2]/255*.85;if(la>0){const lum=(r*.3+g*.59+b*.11)/255,lr=lum<.22?110:18,lg=lum<.22?118:20,lb=lum<.22?130:26;r=r*(1-la)+lr*la;g=g*(1-la)+lg*la;b=b*(1-la)+lb*la;}
  o[i]=r;o[i+1]=g;o[i+2]=b;o[i+3]=A;}
 if(SKI_CACHE.size>16)SKI_CACHE.delete(SKI_CACHE.keys().next().value);SKI_CACHE.set(key,out);return out;}
