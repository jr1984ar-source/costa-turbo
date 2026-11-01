const {pilotSideSVG}=require('./pilot_side.js');const fs=require('fs');const {chromium}=require('playwright');
const V=[
 {helm:{st:'mx',c:'#ffd21a',c2:'#e3202b',pat:'flame'},vest:{c:'#16181d',c2:'#e3202b',pat:'vault',name:'RX Vault'},suit:{c:'#b6f01e',a:'#1d2027'},gog:{brand:'oakley',strap:'#e3202b',lens:'prizm'}},
 {helm:{st:'mx',c:'#f4f6f9',c2:'#1e5eff',pat:'split'},vest:{c:'#1e5eff',c2:'#ffffff',pat:'race',name:'Matrix Race'},suit:{c:'#1e5eff',a:'#0b2c8f'},gog:{brand:'100',strap:'#ffffff',lens:'blue',frame:'#f4f6f9'}},
 {helm:{st:'full',c:'#cfd8e3',c2:'#7a5cff',pat:'chrome'},vest:{c:'#25282e',c2:'#ffc93c',pat:'carbon',name:'F-86 Carbon'},suit:{c:'#2a2d33',a:'#ffc93c',pat:'carbon'}},
];
const html=`<!doctype html><html><head><meta charset=utf8><style>body{margin:0;background:#0a1630}.w{display:flex;width:1200px;height:700px;background:radial-gradient(ellipse at 50% 0%,#245a94 0%,#0f2d55 45%,#0a1630 80%)}.c{flex:1;position:relative}.c svg{position:absolute;left:50%;top:30px;width:300px;height:640px;transform:translateX(-50%)}.pod{position:absolute;left:50%;bottom:22px;width:300px;height:56px;transform:translateX(-50%);border-radius:50%;background:radial-gradient(ellipse at 50% 40%,#3a6aa0,#14315a 70%);box-shadow:0 0 0 3px rgba(51,214,255,.55),0 0 30px rgba(51,214,255,.35)}</style></head><body><div class="w">${V.map((o,i)=>`<div class="c"><div class="pod"></div>${pilotSideSVG(o,'v'+i)}</div>`).join('')}</div></body></html>`;
fs.writeFileSync('boceto3.html',html);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:1200,height:700}})).newPage();await p.goto('file://'+process.cwd()+'/boceto3.html');await p.waitForTimeout(300);await p.screenshot({path:'boceto3.png'});await b.close();})();
