// node shot.js fichier.html sortie.jpg largeur hauteur
const {chromium}=require('playwright');const [,,F,O,W,H]=process.argv;
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:+W,height:+H},deviceScaleFactor:1.5});
await p.goto('file://'+F,{waitUntil:'networkidle'});await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);
await p.screenshot({path:O,type:'jpeg',quality:90});await b.close()})();
