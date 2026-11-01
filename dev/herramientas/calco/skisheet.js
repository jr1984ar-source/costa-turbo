const fs=require('fs');const {chromium}=require('playwright');
const {tracedHelmet}=require('./tracedHelmet.js');
function hex2hsl(h){h=h.replace('#','');let r=parseInt(h.slice(0,2),16)/255,g=parseInt(h.slice(2,4),16)/255,b=parseInt(h.slice(4,6),16)/255;const mx=Math.max(r,g,b),mn=Math.min(r,g,b);let H=0,S=0,L=(mx+mn)/2;if(mx!==mn){const d=mx-mn;S=L>.5?d/(2-mx-mn):d/(mx+mn);H=mx===r?(g-b)/d+(g<b?6:0):mx===g?(b-r)/d+2:(r-g)/d+4;H*=60;}return[H,S,L];}
function hsl2hex(H,S,L){H=((H%360)+360)%360;const c=(1-Math.abs(2*L-1))*S,x=c*(1-Math.abs((H/60)%2-1)),m=L-c/2;let r,g,b;[r,g,b]=H<60?[c,x,0]:H<120?[x,c,0]:H<180?[0,c,x]:H<240?[0,x,c]:H<300?[x,0,c]:[c,0,x];return'#'+[r,g,b].map(v=>Math.round(Math.max(0,Math.min(1,v+m))*255).toString(16).padStart(2,'0')).join('');}
function ski(J,v){const o=JSON.parse(JSON.stringify(J));for(const l of o.layers){const[H,S,L]=hex2hsl(l.col);const yel=S>.25&&H>38&&H<80;
  if(yel){l.col=hsl2hex(v.h,Math.min(1,S*(v.s||1)),Math.min(.9,L*(v.l||1)));continue;}
  if(v.white&&L>.12&&S<.25){l.col=hsl2hex(H,S*.3,Math.min(.97,.5+L*.62));}}return o;}
const Y=JSON.parse(fs.readFileSync('yam1.json','utf8'));
const V=[['Yamaha roja',ski(Y,{h:356,s:1.05,l:.92})],['Yamaha roja y blanca',ski(Y,{h:356,s:1.05,l:.92,white:1})],['Yamaha azul y negra',ski(Y,{h:218,s:1.05,l:.85})]];
const cards=V.map(([n,J],i)=>{const H=tracedHelmet(J,null,'s'+i);return `<div class="c"><svg viewBox="-10 -10 ${H.w+20} ${H.h+30}"><defs>${H.defs}</defs><ellipse cx="${H.w*.52}" cy="${H.h-6}" rx="${H.w*.42}" ry="14" fill="rgba(0,0,0,.18)"/>${H.body}</svg><p>${n}</p></div>`;}).join('');
fs.writeFileSync('skisheet.html',`<!doctype html><html><head><meta charset=utf8><style>body{margin:0;font-family:Arial}.w{display:grid;grid-template-columns:1fr;gap:12px;padding:14px;width:760px;background:#0a1630}.c{background:radial-gradient(ellipse at 50% 35%,#ffffff,#d6dce4 80%);border-radius:16px;padding:8px}.c svg{width:100%;display:block}.c p{margin:2px 8px 6px;color:#15171c;font-weight:900;font-size:18px}</style></head><body><div class="w">${cards}</div></body></html>`);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:788,height:600}})).newPage();await p.goto('file://'+process.cwd()+'/skisheet.html');await p.waitForTimeout(400);await p.screenshot({path:'skisheet.png',fullPage:true});await b.close();})();
