p='costa-turbo.html';s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
i=s.index('<p class="hint ctlhelp">');j=s.index('</section>',i)
s=s[:j]+"""<div class="savebox">
        <h3 class="sbh">PASAR PARTIDA A OTRO APARATO</h3>
        <p class="hint">En este aparato pulsa COPIAR PARTIDA y mándate el código (WhatsApp, correo…). En el otro, pega el código aquí y pulsa CARGAR. Se pasan motos, pesetas, pinturas, equipo, copas, trofeos, medallas y récords.</p>
        <div class="row" style="flex-wrap:nowrap"><button class="btn p" id="sCopy" style="flex:1">COPIAR PARTIDA</button><button class="btn" id="sPaste" style="flex:1">PEGAR PARTIDA</button></div>
        <textarea id="sCode" rows="3" spellcheck="false" autocomplete="off" autocapitalize="off" placeholder="Aquí aparece o se pega el código de la partida"></textarea>
        <button class="btn" id="sLoad" hidden>CARGAR ESTA PARTIDA</button>
        <p class="hint" id="sMsg"></p>
      </div>
    """+s[j:]
rep(".ctlhelp{max-width:420px;font-size:13px;line-height:1.45;text-align:left}",".ctlhelp{max-width:420px;font-size:13px;line-height:1.45;text-align:left}\n.savebox{width:min(100%,440px);display:grid;gap:8px;margin-top:14px;text-align:left}.sbh{font-family:var(--cond);font-weight:800;font-size:18px;letter-spacing:.08em;margin:0}\n#sCode{width:100%;min-height:64px;resize:vertical;border-radius:12px;border:1px solid rgba(255,255,255,.22);background:rgba(255,255,255,.06);color:#fff;font:12px/1.35 ui-monospace,Menlo,Consolas,monospace;padding:10px;word-break:break-all}\n#sLoad.warn{background:#e3202b;color:#fff;border-color:#e3202b}")
rep("on('#bSet',()=>{Snd.click();show('scrSet');labels();});","""on('#bSet',()=>{Snd.click();show('scrSet');labels();prepSave();});
// ---- pasar partida a otro aparato (código con todo lo guardado) ----
const SAVE_SKIP=['ct_snd','ct_mus','ct_vib','ct_hidectl'];let saveC='';
async function saveCode(){const o={};for(let i=0;i<localStorage.length;i++){const k=localStorage.key(i);if(k&&k.startsWith('ct_')&&!SAVE_SKIP.includes(k))o[k]=localStorage.getItem(k);}
 let bytes=new TextEncoder().encode(JSON.stringify({v:1,t:Date.now(),d:o})),pre='CT0';
 try{if(window.CompressionStream){const cs=new Blob([bytes]).stream().pipeThrough(new CompressionStream('gzip'));bytes=new Uint8Array(await new Response(cs).arrayBuffer());pre='CT1';}}catch(_){}
 let bin='';for(let i=0;i<bytes.length;i+=8192)bin+=String.fromCharCode.apply(null,bytes.subarray(i,i+8192));return pre+':'+btoa(bin);}
async function loadCode(code){const m=String(code||'').replace(/\\s+/g,'').match(/(CT[01]):([A-Za-z0-9+/=]+)/);if(!m)throw new Error('código');const bin=atob(m[2]);let bytes=new Uint8Array(bin.length);for(let i=0;i<bin.length;i++)bytes[i]=bin.charCodeAt(i);
 if(m[1]==='CT1'){const ds=new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip'));bytes=new Uint8Array(await new Response(ds).arrayBuffer());}
 const o=JSON.parse(new TextDecoder().decode(bytes));if(!o||!o.d||typeof o.d!=='object')throw new Error('datos');
 const del=[];for(let i=0;i<localStorage.length;i++){const k=localStorage.key(i);if(k&&k.startsWith('ct_')&&!SAVE_SKIP.includes(k))del.push(k);}del.forEach(k=>localStorage.removeItem(k));
 let n=0;for(const k in o.d)if(k.startsWith('ct_')&&!SAVE_SKIP.includes(k)&&typeof o.d[k]==='string'){localStorage.setItem(k,o.d[k]);n++;}return n;}
function prepSave(){saveC='';saveCode().then(c=>{saveC=c;}).catch(()=>{});$('#sMsg').textContent='';$('#sLoad').hidden=!$('#sCode').value.trim();}
on('#sCopy',()=>{Snd.click();const ta=$('#sCode'),go=c=>{ta.value=c;$('#sLoad').hidden=true;let ok=false;try{if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(c).then(()=>{$('#sMsg').textContent='¡Copiado! Mándatelo (WhatsApp, correo…) y pégalo en el otro aparato.';}).catch(()=>{ta.focus();ta.select();$('#sMsg').textContent='Selecciona el código de arriba y cópialo.';});ok=true;}}catch(_){}
  if(!ok){ta.focus();ta.select();try{document.execCommand('copy');$('#sMsg').textContent='¡Copiado! Mándatelo y pégalo en el otro aparato.';}catch(_){$('#sMsg').textContent='Selecciona el código de arriba y cópialo.';}}
  try{if(navigator.share&&matchMedia('(pointer:coarse)').matches)navigator.share({title:'Partida de Costa Turbo',text:c}).catch(()=>{});}catch(_){}};
 if(saveC)go(saveC);else saveCode().then(go).catch(()=>{$('#sMsg').textContent='No se ha podido crear el código.';});});
on('#sPaste',()=>{Snd.click();const ta=$('#sCode');try{if(navigator.clipboard&&navigator.clipboard.readText){navigator.clipboard.readText().then(t=>{if(t&&/CT[01]:/.test(t)){ta.value=t.trim();$('#sLoad').hidden=false;$('#sMsg').textContent='Código pegado. Pulsa CARGAR ESTA PARTIDA.';}else{ta.value='';ta.focus();$('#sMsg').textContent='Pega el código en el recuadro (Ctrl+V o mantén pulsado → Pegar).';}}).catch(()=>{ta.focus();$('#sMsg').textContent='Pega el código en el recuadro (Ctrl+V o mantén pulsado → Pegar).';});return;}}catch(_){}
 ta.focus();$('#sMsg').textContent='Pega el código en el recuadro (Ctrl+V o mantén pulsado → Pegar).';});
$('#sCode').addEventListener('input',()=>{$('#sLoad').hidden=!/CT[01]:/.test($('#sCode').value);$('#sLoad').classList.remove('warn');$('#sLoad').textContent='CARGAR ESTA PARTIDA';});
on('#sLoad',()=>{const b=$('#sLoad');if(!b.classList.contains('warn')){b.classList.add('warn');b.textContent='¿SEGURO? SE CAMBIA LA PARTIDA DE AQUÍ · PULSA OTRA VEZ';Snd.click();clearTimeout(b._t);b._t=setTimeout(()=>{b.classList.remove('warn');b.textContent='CARGAR ESTA PARTIDA';},6000);return;}
 clearTimeout(b._t);loadCode($('#sCode').value).then(n=>{Snd.cash();$('#sMsg').textContent='¡Partida cargada! ('+n+' datos). Reiniciando…';b.hidden=true;setTimeout(()=>location.reload(),900);}).catch(()=>{b.classList.remove('warn');b.textContent='CARGAR ESTA PARTIDA';$('#sMsg').textContent='Ese código no es válido. Cópialo entero otra vez.';});});""")
rep("const APP_VER=112;","const APP_VER=113;")
open(p,'w').write(s);print('ok')
