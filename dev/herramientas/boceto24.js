const fs=require('fs');const {chromium}=require('playwright');
const pilotNew=fs.readFileSync('pilot_svg.js','utf8'),pilotOld=fs.readFileSync('pilot_svg.pre-bare.js','utf8');
const HA=JSON.parse(fs.readFileSync('lineart/helm_assets.json','utf8'));
const th=fs.readFileSync('trace/tracedHelmet.js','utf8').replace("if (typeof module","if (false&&typeof module");
const html=`<!doctype html><html><head><meta charset=utf8><style>body{margin:0;background:#0a1630;font-family:Arial}.w{display:flex;width:1200px;height:800px;background:radial-gradient(ellipse at 50% 0%,#245a94 0%,#0f2d55 45%,#0a1630 80%)}.c{flex:1;position:relative}.c svg{position:absolute;left:50%;top:20px;width:320px;height:725px;transform:translateX(-50%)}.pod{position:absolute;left:50%;bottom:62px;width:300px;height:56px;transform:translateX(-50%);border-radius:50%;background:radial-gradient(ellipse at 50% 40%,#3a6aa0,#14315a 70%);box-shadow:0 0 0 3px rgba(51,214,255,.55),0 0 30px rgba(51,214,255,.35)}.c p{position:absolute;left:0;right:0;bottom:8px;text-align:center;color:#ffc93c;font-weight:900;font-size:18px;margin:0}</style></head><body><div class="w" id="w"></div><script>
var NEW=(function(){${pilotNew.replace("if (typeof module","if (false&&typeof module")};return pilotSVG;})();
var OLD=(function(){${pilotOld.replace("if (typeof module","if (false&&typeof module")};return pilotSVG;})();
${th}
const HA=${JSON.stringify(HA)};
function full(fn,o,helm,gog,uid){const body=fn(Object.assign({},o,{noHelm:true}),uid).replace(/^<svg[^>]*>/,'').replace(/<\\/svg>$/,'');const J=Object.assign({layers:[{col:'#000',d:'',area:1}]},HA.frame);const T=tracedHelmet(J,gog,uid+'h');const gg=T.body.split('<!--GOG-->')[1]||'';const s=Math.min(206/J.w,196/J.h),tx=150-J.w*.55*s,ty=146-J.h*.9*s;
 return '<svg viewBox="0 -40 300 680"><defs>'+T.defs+'</defs>'+body+'<g transform="translate('+tx+' '+ty+') scale('+s+')"><image href="'+HA.img[helm]+'" width="'+J.w+'" height="'+J.h+'"/>'+gg+'</g></svg>';}
const vestS={c:'#ff7a1a',c2:'#ffffff',pat:'band',plain:1};
const C=[
 [OLD,{vest:vestS,suit:{c:'#1d2027',a:'#3a3f4a'},glove:'#1d2027'},'serie',{brand:'',strap:'#1d2027',lens:'smoke'},'Ahora (sale como neopreno)'],
 [NEW,{vest:vestS,suit:{},glove:'#1d2027',bare:{skin:'#e8b48c',shorts:'#1e5eff',shorts2:'#ffffff',lycra:'#1d2027'}},'serie',{brand:'',strap:'#1d2027',lens:'smoke'},'Sin neopreno: licra y bañador'],
 [NEW,{vest:{c:'#16181d',c2:'#e3202b',pat:'vault',name:'RX Vault'},suit:{},glove:'#1d2027',gloveA:'#e3202b',bare:{skin:'#c98d62',shorts:'#e3202b',shorts2:'#1d2027',lycra:'#f4f6f9'}},'rojo',{brand:'oakley',strap:'#1d2027',lens:'prizm',acc:'#ff5a1f'},'Con otro chaleco y casco']];
document.getElementById('w').innerHTML=C.map(([fn,o,hm,gg,t],i)=>'<div class="c"><div class="pod"></div>'+full(fn,o,hm,gg,'p'+i)+'<p>'+t+'</p></div>').join('');</script></body></html>`;
fs.writeFileSync('boceto24.html',html);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:1200,height:800}})).newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('file://'+process.cwd()+'/boceto24.html');await p.waitForTimeout(600);await p.screenshot({path:'boceto24.png'});console.log(JSON.stringify(errs));await b.close();})();
