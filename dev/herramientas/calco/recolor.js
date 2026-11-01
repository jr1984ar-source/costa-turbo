// recolorea las capas rojas/naranjas de un casco calcado
function hex2hsl(h){h=h.replace('#','');let r=parseInt(h.slice(0,2),16)/255,g=parseInt(h.slice(2,4),16)/255,b=parseInt(h.slice(4,6),16)/255;const mx=Math.max(r,g,b),mn=Math.min(r,g,b);let H=0,S=0,L=(mx+mn)/2;if(mx!==mn){const d=mx-mn;S=L>.5?d/(2-mx-mn):d/(mx+mn);H=mx===r?(g-b)/d+(g<b?6:0):mx===g?(b-r)/d+2:(r-g)/d+4;H*=60;}return[H,S,L];}
function hsl2hex(H,S,L){H=((H%360)+360)%360;const c=(1-Math.abs(2*L-1))*S,x=c*(1-Math.abs((H/60)%2-1)),m=L-c/2;let r,g,b;[r,g,b]=H<60?[c,x,0]:H<120?[x,c,0]:H<180?[0,c,x]:H<240?[0,x,c]:H<300?[x,0,c]:[c,0,x];return'#'+[r,g,b].map(v=>Math.round(Math.max(0,Math.min(1,v+m))*255).toString(16).padStart(2,'0')).join('');}
function recolor(J,v){const out=JSON.parse(JSON.stringify(J));for(const l of out.layers){const[H,S,L]=hex2hsl(l.col);const red=S>.22&&(H<45||H>320);if(!red)continue;const off=(H>320?H-360:H);
  if(v.gray){l.col=hsl2hex(0,.06,Math.max(.05,L*v.gray));if(off>12&&v.acc)l.col=hsl2hex(v.acc,S,L);continue;}
  l.col=hsl2hex(v.h+off*(v.k||1),Math.min(1,S*(v.s||1)),Math.min(.92,L*(v.l||1)+(v.lp||0)));}return out;}
if(typeof module!=='undefined')module.exports={recolor};
