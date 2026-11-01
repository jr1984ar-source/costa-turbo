p='costa-turbo.html';s=open(p).read()
def rep(a,b,cnt=1):
    global s
    assert s.count(a)==cnt,(a[:100],s.count(a))
    s=s.replace(a,b)
rep(" ok(){return this.ctx&&this.on&&this.ctx.state==='running';},",
    """ ok(){return this.ctx&&this.on&&this.ctx.state==='running';},
 bg(h){if(!this.ctx)return;this._bg=h;try{if(h){try{if(navigator.audioSession)navigator.audioSession.type='auto';}catch(e){}try{if(navigator.mediaSession){navigator.mediaSession.playbackState='none';navigator.mediaSession.metadata=null;}}catch(e){}this.ctx.suspend().catch(()=>{});}
  else{try{if(navigator.audioSession)navigator.audioSession.type='playback';}catch(e){}if(this.ctx.state!=='running')this.ctx.resume().catch(()=>{});}}catch(e){}},""")
rep("document.addEventListener('visibilitychange',()=>{if(document.hidden&&(G.mode==='play'||G.mode==='count'))togglePause();});",
    "document.addEventListener('visibilitychange',()=>{if(document.hidden&&(G.mode==='play'||G.mode==='count'))togglePause();Snd.bg(document.hidden);});\nwindow.addEventListener('pagehide',()=>Snd.bg(true));window.addEventListener('pageshow',()=>{if(!document.hidden)Snd.bg(false);});\ndocument.addEventListener('touchstart',()=>{if(Snd.ctx&&!document.hidden&&Snd.ctx.state!=='running'){Snd.bg(false);}},{passive:true});")
rep("  if(this.ctx.state!=='running')this.ctx.resume().catch(()=>{});},","  if(this.ctx.state!=='running'){try{if(navigator.audioSession)navigator.audioSession.type='playback';}catch(e){}this.ctx.resume().catch(()=>{});}},")
rep("const APP_VER=43;","const APP_VER=44;")
open(p,'w').write(s);print('ok')
