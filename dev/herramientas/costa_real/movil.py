import json
from PIL import Image,ImageDraw,ImageFont
full=Image.open('estilo_full.png');pos=json.load(open('pos.json'))
pads=Image.open('/tmp/claude-0/-home-user-natura-viva-app/e02bf71e-076d-586d-89ee-84e1312586e6/scratchpad/pads-despues.png');pads=pads.resize((393,852)).crop((0,710,393,852)).resize((390,142))
F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',15)
motos=[Image.open(f'moto{i}.png').resize((32,68)) for i in range(6)]
def phone(tag,frac,me,riv,title):
    y0,y1=pos[str(tag)];cy=int(y0+(y1-y0)*frac);top=max(0,min(full.size[1]-710,cy-355))
    v=full.crop((0,top,390,top+710)).copy();import numpy as np;A=np.array(v).astype(int)
    def wx(y,t):
        row=A[y];wat=np.where((row[:,2]>row[:,0]+40))[0];wat=wat[wat>40]
        if not len(wat):return 300
        # tramo de agua más largo
        runs=np.split(wat,np.where(np.diff(wat)>1)[0]+1);r=max(runs,key=len);return int(r[0]+20+(r[-1]-r[0]-40)*t)
    me=(wx(me[1],.6),me[1]);riv=[(wx(y,t),y) for t,y in riv]
    for k,(x,y) in enumerate(riv):v.paste(motos[k+1],(x-16,y-34),motos[k+1])
    v.paste(motos[0],(me[0]-16,me[1]-34),motos[0])
    d=ImageDraw.Draw(v);tw=d.textlength(title,font=F);d.rounded_rectangle([10,10,tw+30,40],12,fill=(8,22,48));d.text((20,17),title,fill=(255,255,255),font=F)
    o=Image.new('RGB',(390,852));o.paste(v,(0,0));o.paste(pads,(0,710));return o
shots=[phone(1,.55,(0,560),[(.4,470),(.7,430),(.9,520)],"SALIDA · JJ'S"),
       phone(4,.45,(0,560),[(.75,430),(.35,380)],'PUERTO PORTALS'),
       phone(5,.35,(0,600),[(.8,480),(.3,430)],'PORTALS NOUS'),
       phone(6,.5,(0,600),[(.55,450),(.9,420)],'ILLA DE SA TORRE')]
o=Image.new('RGB',(390*4+30,852),'white')
for k,s in enumerate(shots):o.paste(s,(k*400,0))
o.save('movil_4.png');o.resize((o.size[0]//2,o.size[1]//2)).save('movil_4_small.png');print(o.size)
