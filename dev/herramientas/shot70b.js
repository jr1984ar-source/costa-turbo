const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1310,height:1430},deviceScaleFactor:2});
await pg.goto('file://'+process.argv[2]);await pg.waitForSelector('body[data-done]',{timeout:30000});await pg.waitForTimeout(300);
const cs=await pg.$$('canvas');for(const i of [2,3]){await cs[i].screenshot({path:process.argv[3]+i+'.png'});}await b.close();})();
