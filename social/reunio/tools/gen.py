import sys,os
from pathlib import Path
from topics import T,CTA,SWIPE
W=Path(__file__).parent.resolve();L='file://'+str(W)+'/logo.png'
CSS=open(W/'carousel2.py').read().split('CSS="""')[1].split('"""')[0]
STCSS="""html,body{width:1080px;height:1920px}
.top{top:200px}.ph{width:640px}.handle{bottom:150px}.fade{height:260px}"""
def img(lang,p):
    f=W/'fixed2'/lang/p
    if not f.exists(): f=W/'fixed2'/'es'/p
    return 'file://'+str(f)
def ph(src,x,y,w,rot=0,z=1): return f'<div class="ph" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg);z-index:{z}"><img src="{src}"></div>'
def slide(lang,tag,h,sub,phones,num,story,last=False):
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{STCSS if story else ''}</style></head><body><div class="glow"></div>{phones}<div class="fade"></div>
<div class="top"><div class="row"><img class="logo" src="{L}"><div class="num">{num}</div></div><div class="tag">{tag}</div><h1>{h}</h1><p class="sub">{sub}</p></div>
<div class="handle"><span>@app.reunio</span><span class="swipe">{'' if last or story else SWIPE[lang]}</span></div></body></html>'''
def cta(lang,story,num):
    h,sub,tag=CTA[lang]
    top=760 if story else 560
    body=f'<div class="cta" style="top:{top}px"><div class="btn">reunio.app</div><div class="langs"><span>Español</span><span>Português</span><span>English</span></div><p class="sub" style="margin-top:36px">{sub}</p></div>'
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{STCSS if story else ''}</style></head><body><div class="glow"></div>
<div class="top"><div class="row"><img class="logo" src="{L}"><div class="num">{num}</div></div><div class="tag">{tag}</div><h1>{h}</h1></div>{body}<div class="handle"><span>@app.reunio</span><span></span></div></body></html>'''
out=W/'gen_html';
for topic,t in T.items():
  for lang in ['es','pt','en']:
    for story in [False,True]:
      d=out/('story' if story else 'feed')/topic/lang;d.mkdir(parents=True,exist_ok=True)
      n=len(t['slides'])+1
      for i,(p,tx) in enumerate(t['slides']):
        h,sub=tx[lang]
        if story: phones=ph(img(lang,p),220,800,640)
        else: phones=ph(img(lang,p),280,540,520)
        (d/f's{i+1}.html').write_text(slide(lang,t['tag'][lang],h,sub,phones,f'{i+1}/{n}',story))
      (d/f's{n}.html').write_text(cta(lang,story,f'{n}/{n}'))
