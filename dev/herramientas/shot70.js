const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const pg=await b.newPage({viewport:{width:1310,height:1430}});
pg.on('console',m=>console.log('C',m.text()));pg.on('pageerror',e=>console.log('E',e.message));
await pg.goto('file://'+process.argv[2]);await pg.waitForSelector('body[data-done]',{timeout:30000});await pg.waitForTimeout(300);
await pg.screenshot({path:process.argv[3],fullPage:true});console.log('fonts',await pg.evaluate(()=>document.fonts.check('800 46px "Saira Condensed"')));await b.close();})();
