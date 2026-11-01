p='costa-turbo.html';s=open(p,encoding='utf-8').read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(s.count(a),a[:100])
    s=s.replace(a,b)
# ---- CSS
rep("#padR{grid-area:R;padding-right:max(14px,env(safe-area-inset-right,0px));padding-left:6px;justify-content:flex-end;gap:10px}",
    "#padR{grid-area:R;padding-right:max(14px,env(safe-area-inset-right,0px));padding-left:4px;justify-content:flex-end}")
rep(".mz{flex:1;display:flex;gap:10px;height:clamp(76px,24vw,104px);touch-action:none}",
    ".lcol{flex:1;min-width:0;display:flex;flex-direction:column;gap:8px}\n.mz{display:flex;gap:10px;height:clamp(62px,18vw,84px);touch-action:none}\n.lcol .pill.rev{height:40px;font-size:14px}")
s=s.replace(".acc{--s:clamp(84px,27vw,108px);width:var(--s);height:var(--s);",".acc{width:var(--s);height:var(--s);",1)
rep(".smalls{flex:1;min-width:0;max-width:96px;display:flex;flex-direction:column;gap:6px}",
    ".rcl{--s:clamp(88px,25vw,108px);display:flex;align-items:center;gap:6px;touch-action:none}\n.smalls{width:clamp(68px,18vw,90px);display:flex;flex-direction:column;gap:6px}\n.rcl .pill{height:calc((var(--s) - 6px)/2);font-size:14px;flex-direction:column;gap:1px;line-height:1}")
rep("  .mz{height:clamp(84px,34vh,130px)} .acc{--s:clamp(80px,30vh,108px)}","  .mz{height:clamp(60px,22vh,96px)} .rcl{--s:clamp(80px,30vh,104px)}")
# ---- HTML pads
a=s.index('  <div class="pad" id="padL">');b=s.index('</div>\n\n<script>')
PADS='''  <div class="pad" id="padL">
    <span class="pad-tag">GIRAR</span>
    <div class="lcol">
      <div class="mz" id="mz" aria-label="Girar a izquierda o derecha">
        <div class="arrow" id="arL"><svg viewBox="0 0 20 20"><path d="M13.5 3 6 10l7.5 7" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
        <div class="arrow" id="arR"><svg viewBox="0 0 20 20"><path d="M6.5 3 14 10l-7.5 7" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      </div>
      <button class="pill rev" id="bRev" aria-label="Freno y marcha atrás"><svg viewBox="0 0 16 16"><path d="M8 3v10M4 9l4 4 4-4" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>FRENO · ATRÁS</button>
    </div>
  </div>
  <div class="pad" id="padR">
    <div class="rcl" id="rcl" aria-label="Acelerar, turbo y derrape">
      <div class="smalls">
        <div class="pill tur" id="bTurbo" role="button" aria-label="Turbo">TURBO<span class="badge" id="turN">2</span><span class="pbar" id="turRing"></span></div>
        <div class="pill drf" id="bDrift" role="button" aria-label="Derrape"><svg viewBox="0 0 16 16"><path d="M3 13c0-5 4-8 9-8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round"/><path d="M10 2l3.5 3L10 8" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>DERRAPE</div>
      </div>
      <div class="ab acc" id="bAcc" role="button" aria-label="Acelerar"><span><svg viewBox="0 0 20 20"><path d="M10 2 18 12h-5v6H7v-6H2z"/></svg>ACELERAR</span></div>
    </div>
  </div>
'''
s=s[:a]+PADS+s[b:]
# ---- controls JS
rep("""hold($('#bAcc'),v=>{padAcc=v;sync();if(v)menuOk();});
hold($('#bTurbo'),v=>{if(v&&G.mode==='play')input.turbo=true;});
hold($('#bDrift'),v=>{padDrift=v;sync();});
hold($('#bRev'),v=>{padRev=v;sync();});""",
"""hold($('#bRev'),v=>{padRev=v;sync();});
const rcl=$('#rcl'),bAccE=$('#bAcc'),bTurE=$('#bTurbo'),bDrE=$('#bDrift'),rcP=new Map();
function zoneAt(x,y){for(const[el,z]of[[bAccE,'acc'],[bTurE,'turbo'],[bDrE,'drift']]){const r=el.getBoundingClientRect();if(x>=r.left-5&&x<=r.right+5&&y>=r.top-5&&y<=r.bottom+5)return z;}return null;}
function rcApply(){const zs=[...rcP.values()];padAcc=zs.some(z=>z);padDrift=zs.includes('drift');bAccE.classList.toggle('on',zs.includes('acc'));bTurE.classList.toggle('on',zs.includes('turbo'));bDrE.classList.toggle('on',padDrift);sync();}
function fireTurbo(){if(G.mode==='play')input.turbo=true;}
rcl.addEventListener('pointerdown',e=>{e.preventDefault();try{rcl.setPointerCapture(e.pointerId);}catch(_){}const z=zoneAt(e.clientX,e.clientY);rcP.set(e.pointerId,z);rcApply();if(z==='acc')menuOk();if(z==='turbo')fireTurbo();});
rcl.addEventListener('pointermove',e=>{if(!rcP.has(e.pointerId))return;const z=zoneAt(e.clientX,e.clientY)||rcP.get(e.pointerId);if(z!==rcP.get(e.pointerId)){rcP.set(e.pointerId,z);if(z==='turbo')fireTurbo();rcApply();}});
['pointerup','pointercancel','lostpointercapture'].forEach(t=>rcl.addEventListener(t,e=>{if(rcP.delete(e.pointerId))rcApply();}));
rcl.addEventListener('contextmenu',e=>e.preventDefault());""")
rep("addEventListener('blur',()=>{keys.l=keys.r=keys.a=keys.b=keys.dr=0;padAcc=false;padRev=false;padDrift=false;padDir=0;mzP.clear();",
    "addEventListener('blur',()=>{keys.l=keys.r=keys.a=keys.b=keys.dr=0;padAcc=false;padRev=false;padDrift=false;padDir=0;mzP.clear();rcP.clear();")
# ---- music
a=s.index('const Music={');b=s.index("['pointerdown','pointerup','touchend','click','keydown']")
MUS='''const MEL=[
 [[0,76,2],[2,73,2],[4,76,2],[6,78,2],[8,76,4],[12,73,2],[14,71,2]],
 [[0,71,2],[2,68,2],[4,71,2],[6,73,2],[8,71,6],[14,68,2]],
 [[0,69,2],[2,73,2],[4,78,4],[8,76,2],[10,73,2],[12,69,4]],
 [[0,66,2],[2,69,2],[4,74,2],[6,76,2],[8,78,4],[12,76,2],[14,73,2]],
 [[0,76,2],[2,73,2],[4,76,2],[6,78,2],[8,81,4],[12,78,2],[14,76,2]],
 [[0,71,2],[2,68,2],[4,71,2],[6,76,2],[8,76,6],[14,73,2]],
 [[0,73,2],[2,76,2],[4,78,4],[8,76,2],[10,73,2],[12,71,4]],
 [[0,74,2],[2,73,2],[4,71,2],[6,69,2],[8,69,8]]];
const Music={timer:null,pat:null,step:0,next:0,want:null,
 play(p){if(!Snd.ctx){this.want=p;return;}if(this.pat===p)return;this.stop();this.pat=p;this.step=0;this.next=Snd.ctx.currentTime+.1;this.timer=setInterval(()=>this.tick(),25);},
 stop(){clearInterval(this.timer);this.timer=null;this.pat=null;this.want=null;},
 bpm(){return this.pat==='final'?134:this.pat==='race'?124:100;},
 tick(){const c=Snd.ctx;if(!c||c.state!=='running'){if(c)this.next=c.currentTime+.1;return;}const spb=60/this.bpm()/4;
  while(this.next<c.currentTime+.15){this.note(this.step,this.next);this.step++;this.next+=spb;}},
 note(i,t){if(!Snd.on||!Snd.musOn)return;const s=i%16,bar=((i/16)|0)%8,ci=[0,1,2,3,0,1,3,1][bar],B=Snd.mus,mf=m=>440*Math.pow(2,(m-69)/12),race=this.pat!=='menu',spb=60/this.bpm()/4;
  const roots=[45,40,42,38],tri=[[69,73,76],[64,68,71],[66,69,73],[62,66,69]];
  if(race){if(s%2===0)Snd.tone({at:t,w:'sawtooth',f:mf(roots[ci]+(s%4===2?12:0)),t:spb*1.8,v:.075,bus:B});}
  else if(s%4===0)Snd.tone({at:t,w:'triangle',f:mf(roots[ci]),t:spb*3.6,v:.17,bus:B});
  if(race?s%4===0:(s===0||s===8))Snd.tone({at:t,w:'sine',f:150,f2:42,t:.2,v:.38,bus:B});
  if(s===4||s===12)Snd.hiss({at:t,ft:'bandpass',f:1700,t:.15,v:race?.2:.12,q:.8,bus:B});
  if(race?s%2===1:s%4===2)Snd.hiss({at:t,ft:'highpass',f:7500,t:.04,v:.06,bus:B});
  if(race&&s%4===2)Snd.hiss({at:t,ft:'highpass',f:9500,t:.025,v:.03,bus:B});
  if(s%4===2)for(const n of tri[ci])Snd.tone({at:t,w:'triangle',f:mf(n),t:spb*1.4,v:race?.032:.028,bus:B});
  for(const[st,n,len]of MEL[bar])if(st===s){const d=len*spb*.95;Snd.tone({at:t,w:race?'square':'triangle',f:mf(n),t:d,v:race?.042:.06,a:.01,bus:B});if(race)Snd.tone({at:t,w:'triangle',f:mf(n+12),t:d*.7,v:.02,bus:B});}}
};
function raceMusic(){Music.play(G.zone&&G.zone.Z.boss?'final':'race');}
'''
s=s[:a]+MUS+s[b:]
rep("this.mus.gain.value=this.musOn?.42:0;","this.mus.gain.value=this.musOn?.6:0;")
rep("this.mus.gain.setTargetAtTime(v?.42:0,","this.mus.gain.setTargetAtTime(v?.6:0,")
rep("setTimeout(()=>c.hidden=true,700);Music.play('race');","setTimeout(()=>c.hidden=true,700);raceMusic();")
rep("function closeBar(){show(null);Music.play('race');","function closeBar(){show(null);raceMusic();")
rep("e.g.gain.setTargetAtTime(idle?0:(.035+thr*.05+rpm*.05)*(exh?1.45:1),t,.08);","e.g.gain.setTargetAtTime(idle?0:(.03+thr*.042+rpm*.042)*(exh?1.45:1),t,.08);")
open(p,'w',encoding='utf-8').write(s)
print('ok')
