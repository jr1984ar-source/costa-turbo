// render de un json calcado a png
const fs=require('fs');const {chromium}=require('playwright');
const files=process.argv.slice(2,-1),out=process.argv[process.argv.length-1];
const svgs=files.map(f=>{const J=JSON.parse(fs.readFileSync(f,'utf8'));return `<svg viewBox="0 0 ${J.w} ${J.h}" style="width:380px;background:#eef1f5;border-radius:12px"><path d="${J.sil}" fill="${J.layers[Math.floor(J.layers.length/2)].col}"/>${J.layers.map(l=>`<path d="${l.d}" fill="${l.col}" fill-rule="evenodd" stroke="${l.col}" stroke-width="1.2"/>`).join('')}</svg>`;});
fs.writeFileSync('show.html',`<!doctype html><html><body style="margin:0;padding:10px;background:#0a1630;display:flex;flex-wrap:wrap;gap:10px;width:800px">${svgs.join('')}</body></html>`);
(async()=>{const b=await chromium.launch();const p=await (await b.newContext({viewport:{width:820,height:600}})).newPage();await p.goto('file://'+process.cwd()+'/show.html');await p.waitForTimeout(300);await p.screenshot({path:out,fullPage:true});await b.close();})();
