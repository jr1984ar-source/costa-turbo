const fs=require('fs');let body=fs.readFileSync('costa-turbo.html','utf8');
const a="requestAnimationFrame(frame);\n})();";if(!body.includes(a))throw 'anchor';
body=body.replace(a,"window.__G=G;window.__goMap=goMap;window.__Z=ZONES;window.__M=MOTOS;window.__T={startRace,gameOver,goShop,goFree,openBar,renderShop,renderGarage,renderJJ,newGame,startFree,hpTot,setHp,livesUI,owns,partsOf,ownList,get best(){return best}};"+a);
fs.writeFileSync('ct-wrapped.html','<!doctype html><html><head><meta charset=utf8><meta name=viewport content="width=device-width,initial-scale=1,viewport-fit=cover"><style>body{margin:0}[hidden]{display:none!important}</style></head><body>'+body+'</body></html>');console.log('wrapped');
