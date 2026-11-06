window.__alt=(g,p,D,m)=>{__ski.decor(g,m,Object.assign({},p,{logo:''}));
 const W=D.width,H=D.height,mk=document.createElement('canvas');mk.width=W;mk.height=H;{const x=mk.getContext('2d'),id=x.createImageData(W,H),s=D.data;for(let i=0;i<s.length;i+=4){const L=Math.round(s[i]/36);if(L===1||L===2)id.data[i+3]=255;}x.putImageData(id,0,0);}
 const L={jj:[["JJ's",'#8e1f2c'],['SPORTS','#1f3fb0'],['LOUNGE','#1c1c1f']],roxy:[['R O X Y','#7a5232']],ct:[['COSTA TURBO','#0e3f8f']]}[p.logo];if(!L)return;
 const v=document.createElement('canvas');v.width=W;v.height=H;const x=v.getContext('2d');x.save();x.transform(1,.43,0,1,215,322);x.font='800 26px "Saira Condensed",Arial,sans-serif';x.textBaseline='middle';x.textAlign='center';
 let tw=0;for(const[t]of L)tw+=x.measureText(t).width+16;let x0=-tw/2;
 for(const[t,c]of L){const w=x.measureText(t).width+16;x.fillStyle=c;x.fillRect(x0,0,w,34);x.fillStyle=p.logo==='ct'?'#ffd21a':'#ffffff';x.fillText(t,x0+w/2,18);x0+=w;}
 x.strokeStyle='rgba(255,255,255,.9)';x.lineWidth=2.5;x.strokeRect(-tw/2,0,tw,34);x.restore();
 x.globalCompositeOperation='destination-in';x.drawImage(mk,0,0);g.drawImage(v,0,0);};
