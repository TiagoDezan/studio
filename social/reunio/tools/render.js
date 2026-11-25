const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const [dir,out,w,h]=process.argv.slice(2);fs.mkdirSync(out,{recursive:true});const b=await chromium.launch();const p=await b.newPage({viewport:{width:+w,height:+h}});
for(const f of fs.readdirSync(dir).filter(f=>f.endsWith('.html')).sort()){await p.goto('file://'+path.resolve(dir,f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(200);
await p.screenshot({path:path.join(out,f.replace('.html','.jpg')),type:'jpeg',quality:90});}
await b.close();})();
