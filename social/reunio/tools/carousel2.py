import json,sys
from pathlib import Path
W=Path(__file__).parent.resolve(); F='file://'+str(W)+'/fixed2/es/'; L='file://'+str(W)+'/logo.png'
CSS="""
@font-face{font-family:I;src:url(file:///usr/share/fonts/opentype/inter/Inter-Medium.otf);font-weight:500}
@font-face{font-family:I;src:url(file:///usr/share/fonts/opentype/inter/Inter-SemiBold.otf);font-weight:600}
@font-face{font-family:I;src:url(file:///usr/share/fonts/opentype/inter/Inter-Bold.otf);font-weight:700}
@font-face{font-family:I;src:url(file:///usr/share/fonts/opentype/inter/Inter-ExtraBold.otf);font-weight:800}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{font-family:I,sans-serif;color:#eadcca;background:radial-gradient(110% 70% at 85% 0%,#2f5a5b 0%,#163235 42%,#090f14 100%);position:relative}
.glow{position:absolute;width:700px;height:700px;border-radius:50%;filter:blur(150px);background:#c75f1e;opacity:.20;left:-200px;bottom:-250px}
.top{position:absolute;left:80px;right:80px;top:72px}
.row{display:flex;align-items:center;justify-content:space-between}
.logo{height:54px}
.num{font-size:24px;font-weight:700;color:#7fb3b8;letter-spacing:3px}
.tag{margin-top:54px;display:inline-block;font-size:24px;font-weight:700;letter-spacing:4px;text-transform:uppercase;color:#0b1a1d;background:#7fb3b8;padding:10px 20px;border-radius:999px}
h1{margin-top:24px;font-size:76px;line-height:1.04;font-weight:800;letter-spacing:-2px;color:#fff6ea}
h1 .o{color:#e07a35}
.sub{margin-top:20px;font-size:32px;line-height:1.35;font-weight:500;color:#cfd9d6;max-width:900px}
.ph{position:absolute;width:520px;border-radius:72px;background:#05090c;padding:14px;box-shadow:0 40px 90px rgba(0,0,0,.55),0 0 0 2px rgba(234,220,202,.14)}
.ph img{display:block;width:100%;border-radius:60px}
.fade{z-index:9;position:absolute;left:0;right:0;bottom:0;height:170px;background:linear-gradient(to bottom,rgba(9,15,20,0),#090f14 85%)}
.handle{z-index:10;position:absolute;bottom:44px;left:80px;right:80px;display:flex;justify-content:space-between;font-size:24px;font-weight:700;color:#7fb3b8}
.swipe{color:#eadcca}
.cta{position:absolute;left:80px;right:80px;top:470px}
.btn{display:inline-block;margin-top:40px;background:#eadcca;color:#0b1a1d;font-size:44px;font-weight:800;padding:30px 52px;border-radius:999px}
.langs{margin-top:46px;display:flex;gap:18px}
.langs span{font-size:30px;font-weight:700;border:2px solid rgba(234,220,202,.3);padding:14px 26px;border-radius:999px}
.list{margin-top:56px;display:grid;grid-template-columns:1fr 1fr;gap:18px}
.list div{font-size:30px;font-weight:600;background:rgba(234,220,202,.07);border:2px solid rgba(234,220,202,.14);border-radius:24px;padding:22px 26px}
.list b{color:#e07a35}
"""
def phone(img,x,y,w=520,rot=0,z=1):
    return f'<div class="ph" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg);z-index:{z}"><img src="{F}{img}"></div>'
S=[
 dict(tag=None,h='Toda tu iglesia,<br>en un <span class="o">solo lugar</span>.',sub='Miembros, tesorería, escalas, eventos y el portal del miembro, en una sola app.',
      ph=[('inicio/01-inicio.png',90,560,500,-5,1),('portal-miembro/01-identidad.png',500,600,500,5,2)]),
 dict(tag='Miembros',h='Cada persona,<br>con su <span class="o">ficha</span>.',sub='Contacto, comunión, congregación y su carné, siempre al día.',
      ph=[('miembros/02-lista.png',80,600,480,-4,1),('miembros/03-ficha.png',500,560,500,4,2)]),
 dict(tag='Tesorería',h='Cuentas claras<br><span class="o">cada mes</span>.',sub='Entradas, salidas y saldo de cada cuenta, con informes listos.',
      ph=[('tesoreria/01-resumen.png',280,540,520,0,1)]),
 dict(tag='Escalas',h='Quién sirve<br><span class="o">este domingo</span>.',sub='Limpieza, sonido, clase de niños y recepción, organizados por equipos.',
      ph=[('escalas/01-calendario.png',80,600,480,-4,1),('escalas/04-recepcion.png',500,560,500,4,2)]),
 dict(tag='Eventos',h='Todo el calendario<br>de la <span class="o">iglesia</span>.',sub='Cultos, encuentros y estudios, y cada miembro los ve en su portal.',
      ph=[('eventos/01-actividades.png',80,600,480,-4,1),('portal-miembro/07-calendario-eventos.png',500,560,500,4,2)]),
 dict(tag='Portal del miembro',h='Su carné con QR,<br>en <span class="o">Apple Wallet</span>.',sub='Cada miembro entra con su código y hace check-in en segundos.',
      ph=[('portal-miembro/01-identidad.png',80,600,480,-4,1),('portal-miembro/03-wallet-anadir.png',500,560,500,4,2)]),
 dict(tag='Portal del miembro',h='Oración en<br><span class="o">comunidad</span>.',sub='Los miembros comparten sus pedidos y la iglesia ora junta.',
      ph=[('portal-miembro/11-oracion.png',280,540,520,0,1)]),
]
pages=[]
for i,s in enumerate(S):
    tag=f'<div class="tag">{s["tag"]}</div>' if s['tag'] else '<div style="height:54px"></div>'
    phs=''.join(phone(*p) for p in s['ph'])
    pages.append(f'''<div class="glow"></div>{phs}<div class="fade"></div><div class="top"><div class="row"><img class="logo" src="{L}"><div class="num">{i+1}/8</div></div>{tag}<h1>{s["h"]}</h1><p class="sub">{s["sub"]}</p></div><div class="handle"><span>@app.reunio</span><span class="swipe">Desliza →</span></div>''')
pages.append(f'''<div class="glow"></div><div class="top"><div class="row"><img class="logo" src="{L}"><div class="num">8/8</div></div><div class="tag">Gratis</div><h1>Crea la cuenta de<br>tu iglesia <span class="o">hoy</span>.</h1></div>
<div class="cta"><div class="list"><div><b>●</b> Miembros</div><div><b>●</b> Tesorería</div><div><b>●</b> Escalas</div><div><b>●</b> Eventos y check-in</div><div><b>●</b> Carné con QR</div><div><b>●</b> Avisos y oración</div></div>
<div class="btn">my.reunio.app</div><div class="langs"><span>Español</span><span>Português</span><span>English</span></div>
<p class="sub" style="margin-top:36px">En la web y en iPhone. Enlace en la bio.</p></div><div class="handle"><span>@app.reunio</span><span></span></div>''')
out=W/'html2';out.mkdir(exist_ok=True)
for i,p in enumerate(pages):(out/f'r{i+1:02d}.html').write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{p}</body></html>')
