const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
const only=process.argv.slice(2);
for(const f of fs.readdirSync('html').sort()){ if(only.length&&!only.some(o=>f.startsWith(o)))continue;
 await p.goto('file://'+path.resolve('html',f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
 await p.screenshot({path:'out/'+f.replace('.html','.jpg'),type:'jpeg',quality:92});}
await b.close();})();
