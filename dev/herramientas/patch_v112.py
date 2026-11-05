p='costa-turbo.html';s=open(p).read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(s.count(a),a[:80]);s=s.replace(a,b)
# Ajustes: ocultar los controles de la pantalla (para PC con teclado o mando) y ayuda de los botones
rep('<button class="setr" id="sVib"><span>VIBRACIÓN<small>Cuando te das un golpe</small></span><i class="tg"></i></button>',
    '<button class="setr" id="sVib"><span>VIBRACIÓN<small>Cuando te das un golpe (móvil y mando)</small></span><i class="tg"></i></button>\n        <button class="setr" id="sCtl"><span>OCULTAR CONTROLES<small>Para jugar en el PC con teclado o mando</small></span><i class="tg"></i></button>')
rep('<p class="hint" id="vibNote"></p>','<p class="hint" id="vibNote"></p>\n      <p class="hint ctlhelp"><b>MANDO:</b> joystick o cruceta para girar · B o gatillo derecho acelera · gatillo izquierdo frena · A derrapa · X turbo · START pausa. En los menús: cruceta para moverte, A acepta y B vuelve.<br><b>TECLADO:</b> flechas o WASD · Espacio derrapa · Shift turbo · P pausa.</p>')
rep("VIB_ON=store.get('ct_vib',true)!==false,","VIB_ON=store.get('ct_vib',true)!==false,HIDE_CTL=store.get('ct_hidectl',false)===true,")
rep("$('#sVib').classList.toggle('on',!!VIB_ON);","$('#sVib').classList.toggle('on',!!VIB_ON);$('#sCtl').classList.toggle('on',!!HIDE_CTL);")
rep("on('#sVib',()=>{","on('#sCtl',()=>{HIDE_CTL=!HIDE_CTL;store.set('ct_hidectl',HIDE_CTL);Snd.click();labels();});\non('#sVib',()=>{")
rep("function show(id){screens.forEach(s=>s.hidden=s.id!==id);$('#app').classList.toggle('nopads',!!id);","function show(id){screens.forEach(s=>s.hidden=s.id!==id);$('#app').classList.toggle('nopads',!!id||HIDE_CTL);")
rep("#vibNote{max-width:380px}","#vibNote{max-width:380px}\n.ctlhelp{max-width:420px;font-size:13px;line-height:1.45;text-align:left}\n.gpf{outline:3px solid #ffe14d!important;outline-offset:3px;box-shadow:0 0 0 7px rgba(255,225,77,.28)!important}")
# mando: X turbo · A derrape · B acelera (también gatillo derecho) · gatillo izquierdo frena · START pausa
rep("function sync(){input.left=!!keys.l||padDir<0;input.right=!!keys.r||padDir>0;input.acc=!!keys.a||padAcc;input.rev=!!keys.b||padRev;input.drift=!!keys.dr||padDrift;",
    "const gp={l:0,r:0,a:0,b:0,d:0},gpPrev={};let gpOn=false,gpFocus=null;\nfunction sync(){input.left=!!keys.l||padDir<0||!!gp.l;input.right=!!keys.r||padDir>0||!!gp.r;input.acc=!!keys.a||padAcc||!!gp.a;input.rev=!!keys.b||padRev||!!gp.b;input.drift=!!keys.dr||padDrift||!!gp.d;")
rep("function fireTurbo(){","""function gpScreen(){return screens.find(x=>!x.hidden)||null;}
function gpItems(sc){return[...sc.querySelectorAll('button,input,[role="button"]')].filter(e=>e.offsetParent!==null&&!e.disabled);}
function gpSet(e){if(gpFocus)gpFocus.classList.remove('gpf');gpFocus=e;if(!e)return;e.classList.add('gpf');try{e.focus({preventScroll:true});}catch(_){}try{e.scrollIntoView({block:'nearest',inline:'nearest'});}catch(_){}}
function gpMove(dx,dy){const sc=gpScreen();if(!sc)return;const it=gpItems(sc);if(!it.length)return;const cur=gpFocus&&it.includes(gpFocus)?gpFocus:null;
 if(!cur){gpSet(it.find(e=>e.classList.contains('p')&&e.closest('.menu'))||it.find(e=>e.classList.contains('p'))||it[0]);return;}if(!dx&&!dy)return;
 const r0=cur.getBoundingClientRect(),cx=r0.left+r0.width/2,cy=r0.top+r0.height/2;let best=null,bd=1e9;
 for(const e of it){if(e===cur)continue;const r=e.getBoundingClientRect(),vx=r.left+r.width/2-cx,vy=r.top+r.height/2-cy,al=vx*dx+vy*dy;if(al<=4)continue;const d=al+Math.abs(vx*dy-vy*dx)*2.2;if(d<bd){bd=d;best=e;}}
 if(best)gpSet(best);}
function gpBack(){const sc=gpScreen();if(!sc)return;const b=[...sc.querySelectorAll('[id$="Back"],[id$="Bk"],[id$="Out"],#pResume')].find(e=>e.offsetParent!==null);if(b){Snd.click();b.click();}}
function gpRumble(ms){try{for(const g of(navigator.getGamepads?navigator.getGamepads():[])){if(g&&g.connected&&g.vibrationActuator&&g.vibrationActuator.playEffect)g.vibrationActuator.playEffect('dual-rumble',{startDelay:0,duration:Math.min(400,ms*2),weakMagnitude:.6,strongMagnitude:Math.min(1,ms/120)});}}catch(_){}}
function gpPoll(){let g=null;try{for(const q of(navigator.getGamepads?navigator.getGamepads():[]))if(q&&q.connected){g=q;break;}}catch(_){}
 if(!g){if(gpOn){gpOn=false;gp.l=gp.r=gp.a=gp.b=gp.d=0;sync();}return;}gpOn=true;
 const bt=i=>{const x=g.buttons[i];return!!x&&(x.pressed||x.value>.35);},ax=g.axes[0]||0,ay=g.axes[1]||0;
 const now={A:bt(0),B:bt(1),X:bt(2),LT:bt(6),RT:bt(7),ST:bt(9),U:bt(12)||ay<-.6,D:bt(13)||ay>.6,L:bt(14)||ax<-.6,R:bt(15)||ax>.6},pr=k=>now[k]&&!gpPrev[k];
 if(G.mode==='play'||G.mode==='count'){gp.l=bt(14)||ax<-.3;gp.r=bt(15)||ax>.3;gp.a=now.B||now.RT;gp.b=now.LT;gp.d=now.A;if(pr('X'))fireTurbo();if(pr('ST'))togglePause();}
 else{gp.l=gp.r=gp.a=gp.b=gp.d=0;if(G.mode==='pause'&&pr('ST'))togglePause();
  else{if(pr('U'))gpMove(0,-1);if(pr('D'))gpMove(0,1);if(pr('L'))gpMove(-1,0);if(pr('R'))gpMove(1,0);if(pr('A')){const sc=gpScreen();if(gpFocus&&gpFocus.offsetParent!==null&&sc&&sc.contains(gpFocus))gpFocus.click();else gpMove(0,0);}if(pr('B'))gpBack();}}
 sync();Object.assign(gpPrev,now);}
function fireTurbo(){""")
rep("function frame(now){","function frame(now){gpPoll();")
rep("function vibNow(ms){if(!VIB_ON)return;","function vibNow(ms){if(!VIB_ON)return;gpRumble(ms);")
rep("const APP_VER=111;","const APP_VER=112;")
open(p,'w').write(s);print('ok')
