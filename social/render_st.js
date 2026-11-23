const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
const only=process.argv.slice(2);
for(const f of fs.readdirSync('html_st').sort()){ if(only.length&&!only.some(o=>f.startsWith(o)))continue;
 await p.goto('file://'+path.resolve('html_st',f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
 await p.screenshot({path:'out_st/'+f.replace('.html','.jpg'),type:'jpeg',quality:90});}
await b.close();})();
