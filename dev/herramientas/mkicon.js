const {chromium}=require('playwright');const fs=require('fs');
(async()=>{
 const src=fs.readFileSync('costa-turbo.html','utf8');
 const grab=name=>{const a=src.indexOf('function '+name+'(');let i=src.indexOf('{',a),d=0;for(;i<src.length;i++){if(src[i]==='{')d++;else if(src[i]==='}'){d--;if(!d)break;}}return src.slice(a,i+1);};
 const fns=[grab('mixc'),grab('drawJetProfile')].join('\n');
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1024,height:1024}});
 await p.setContent(`<canvas id=c width=1024 height=1024></canvas><script>const TAU=Math.PI*2;${fns}
 function rng(s){return()=>{s|=0;s=s+0x6D2B79F5|0;let t=Math.imul(s^s>>>15,1|s);t=t+Math.imul(t^t>>>7,61|t)^t;return((t^t>>>14)>>>0)/4294967296;};}
 const c=document.getElementById('c'),g=c.getContext('2d'),r=rng(9),H=600;
 // cielo
 let gr=g.createLinearGradient(0,0,0,H);gr.addColorStop(0,'#2a0f5c');gr.addColorStop(.38,'#c8326e');gr.addColorStop(.72,'#ff7a3d');gr.addColorStop(1,'#ffc46b');g.fillStyle=gr;g.fillRect(0,0,1024,H+2);
 for(let i=0;i<40;i++){g.fillStyle='rgba(255,255,255,'+(.3+r()*.5)+')';g.beginPath();g.arc(r()*1024,r()*200,1+r()*2.2,0,TAU);g.fill();}
 // sol retro
 const sc=document.createElement('canvas');sc.width=sc.height=1024;const s=sc.getContext('2d');
 let sg=s.createLinearGradient(0,170,0,690);sg.addColorStop(0,'#fff6b8');sg.addColorStop(.55,'#ffd25a');sg.addColorStop(1,'#ff8a2a');s.fillStyle=sg;s.beginPath();s.arc(660,430,260,0,TAU);s.fill();
 s.globalCompositeOperation='destination-out';for(let k=0;k<8;k++){const y=455+k*30+k*k*1.5,h=5+k*3.2;s.fillRect(0,y,1024,h);}
 g.save();g.shadowColor='rgba(255,200,90,.9)';g.shadowBlur=90;g.drawImage(sc,0,0);g.restore();g.drawImage(sc,0,0);
 // mar
 gr=g.createLinearGradient(0,H,0,1024);gr.addColorStop(0,'#2bb8e0');gr.addColorStop(.5,'#1477c4');gr.addColorStop(1,'#0a3a86');g.fillStyle=gr;g.fillRect(0,H,1024,424);
 g.save();g.globalCompositeOperation='screen';for(let i=0;i<26;i++){const y=H+8+i*15+i*i*.6,w=60+r()*160;g.fillStyle='rgba(255,200,110,'+(.85-i*.028)+')';g.fillRect(660-w/2+(r()-.5)*40,y,w,3+i*.25);}g.restore();
 g.strokeStyle='rgba(255,255,255,.25)';g.lineWidth=3;for(let i=0;i<30;i++){const x=r()*1024,y=H+30+r()*380,l=20+r()*50;g.beginPath();g.moveTo(x,y);g.quadraticCurveTo(x+l/2,y-6,x+l,y);g.stroke();}
 // ola grande
 const wave=()=>{g.beginPath();g.moveTo(-20,1044);g.lineTo(-20,800);g.bezierCurveTo(120,720,300,640,450,690);g.bezierCurveTo(540,720,560,790,500,820);g.bezierCurveTo(470,835,440,820,450,800);g.bezierCurveTo(520,820,520,760,460,745);g.bezierCurveTo(380,725,300,800,250,870);g.bezierCurveTo(210,930,280,1010,440,1044);g.closePath();};
 wave();gr=g.createLinearGradient(0,650,0,1024);gr.addColorStop(0,'#6ff0f5');gr.addColorStop(.35,'#1fb3d8');gr.addColorStop(1,'#0b4f9e');g.fillStyle=gr;g.fill();
 g.save();wave();g.clip();g.strokeStyle='rgba(255,255,255,.35)';g.lineWidth=5;for(let k=0;k<5;k++){g.beginPath();g.moveTo(-10,840+k*40);g.bezierCurveTo(120,770+k*40,260,720+k*40,380,760+k*30);g.stroke();}g.restore();
 for(let i=0;i<120;i++){const t=r(),x=-20+t*500,y=800-Math.sin(t*Math.PI*.95)*150+(t>.8?(t-.8)*300:0);g.fillStyle='rgba(255,255,255,'+(.7+r()*.3)+')';g.beginPath();g.arc(x+(r()-.5)*20,y+(r()-.5)*16-r()*20,4+r()*12,0,TAU);g.fill();}
 // estela de espuma detrás de la moto
 for(let i=0;i<160;i++){const t=r(),x=330-t*330+(r()-.5)*40,y=690+t*t*120+(r()-.5)*50-Math.sin(t*3)*30;g.fillStyle='rgba(255,255,255,'+(.5+r()*.5)*(1-t*.5)+')';g.beginPath();g.arc(x,y,3+r()*14*(1-t*.6),0,TAU);g.fill();}
 // líneas de velocidad
 g.strokeStyle='rgba(255,255,255,.6)';g.lineCap='round';for(let i=0;i<6;i++){g.lineWidth=6-i*.6;const y=470+i*38;g.beginPath();g.moveTo(80+i*20,y+40);g.lineTo(230+i*20,y);g.stroke();}
 // sombra de la moto en el agua
 g.fillStyle='rgba(0,30,70,.35)';g.beginPath();g.ellipse(560,905,230,26,-.05,0,TAU);g.fill();
 // moto + piloto
 g.save();g.translate(250,420);g.rotate(-.3);g.scale(1.75,1.75);
 drawJetProfile(g,{deck:'#f2f3f5',hood:'#e3202b',hull:'#e3202b',trim:'#1b1d22',seatA:'#f2f3f5',seatB:'#e3202b',seatC:'#1b1d22',stripe:'#1b1d22'});
 g.lineCap='round';g.lineJoin='round';
 g.strokeStyle='#1b1d22';g.lineWidth=11;g.beginPath();g.moveTo(152,30);g.lineTo(184,40);g.lineTo(178,58);g.stroke();
 g.strokeStyle='#e3202b';g.lineWidth=16;g.beginPath();g.moveTo(150,28);g.lineTo(180,-2);g.stroke();
 g.fillStyle='#1b1d22';g.beginPath();g.ellipse(166,14,13,18,.8,0,TAU);g.fill();g.fillStyle='#ffc93c';g.fillRect(156,10,20,4);
 g.strokeStyle='#e8b48c';g.lineWidth=7;g.beginPath();g.moveTo(182,0);g.lineTo(200,8);g.lineTo(206,6);g.stroke();
 let hg=g.createRadialGradient(186,-18,2,190,-14,15);hg.addColorStop(0,'#ffffff');hg.addColorStop(1,'#d9dee6');g.fillStyle=hg;g.beginPath();g.arc(190,-14,14,0,TAU);g.fill();
 g.fillStyle='#14161c';g.beginPath();g.moveTo(194,-22);g.quadraticCurveTo(206,-18,204,-8);g.lineTo(196,-8);g.closePath();g.fill();g.fillStyle='#e3202b';g.fillRect(178,-20,3,14);
 g.restore();
 // gotas en el aire
 for(let i=0;i<40;i++){const x=200+r()*640,y=560+r()*300;g.fillStyle='rgba(255,255,255,'+(.6+r()*.4)+')';g.beginPath();g.arc(x,y,2+r()*6,0,TAU);g.fill();}
 // brillo general
 const vg=g.createRadialGradient(512,520,300,512,520,760);vg.addColorStop(0,'rgba(0,0,0,0)');vg.addColorStop(1,'rgba(10,0,40,.35)');g.fillStyle=vg;g.fillRect(0,0,1024,1024);
 </script>`);
 await p.waitForTimeout(400);
 const png=await p.evaluate(()=>document.getElementById('c').toDataURL('image/png'));
 fs.writeFileSync('costa-turbo-icono.png',Buffer.from(png.split(',')[1],'base64'));
 for(const N of [180,192,512]){const d=await p.evaluate(n=>{const o=document.createElement('canvas');o.width=o.height=n;const x=o.getContext('2d');x.imageSmoothingQuality='high';x.drawImage(document.getElementById('c'),0,0,n,n);return o.toDataURL('image/png');},N);fs.writeFileSync('ghp/icon-'+N+'.png',Buffer.from(d.split(',')[1],'base64'));}
 await b.close();console.log('ok');})();
