"""Stories (1080x1920) and the LaCesta Christmas post (1080x1350, Spanish)."""
import json
from pathlib import Path
import gen

ROOT = gen.ROOT
A = gen.A
OUT = 'file:///home/claude/social/out/'

# ---------- LaCesta feed post (Spanish) ----------
CESTA_CSS = """
.g{color:#34d399}
.phones img{border-color:rgba(52,211,153,.55)}
.pill{font-family:'Press Start 2P';font-size:16px;background:#34d399;color:#05070a;padding:12px 16px 10px;align-self:flex-start}
"""
LACESTA = {
    'id': '15-lacesta-navidad', 'tag': 'LACESTA', 'date': '2026-12-16',
    'slides': [
        {'html': f"""<div class="row" style="gap:36px"><img src="{A}cesta/icon.png" style="width:220px;border-radius:50px"><span class="pill">NUEVA APP</span></div>
<h1>NAVIDAD<br><span class="g">SIN PASARTE</span><br>DEL PRESUPUESTO</h1>
<p class="lead">La compra de las fiestas, bajo control.</p>
<p class="small">LaCesta · Tu asistente de compras</p>"""},
        {'html': f"""<h2 style="color:#34d399">EN EL SÚPER</h2>
<p class="lead">Marca lo que metes en el carrito y mira cuánto te queda, al momento.</p>
<div class="phones"><img src="{A}cesta/01-compra.png"><img src="{A}cesta/03-al-carrito.png"></div>"""},
        {'html': f"""<h2 style="color:#34d399">SIN SUSTOS</h2>
<p class="lead">Avisos al 80 % y al 90 % del presupuesto, y previsión del gasto del mes.</p>
<div class="phones"><img src="{A}cesta/03-aviso.png"><img src="{A}cesta/04-ahorrar.png"></div>"""},
        {'html': f"""<img src="{A}cesta/icon.png" style="width:300px;border-radius:68px;align-self:center">
<h1 class="sm" style="text-align:center">LISTAS QUE<br><span class="g">APRENDEN</span></h1>
<ul class="list"><li>"2 leche, pan y 1,5 kg de patatas"</li><li>Escáner de código de barras</li><li>Historial de precios</li><li>Sin cuentas, sin anuncios, sin rastreo</li></ul>
<p class="lead" style="text-align:center">{{STATUS}}</p>"""},
    ],
}

# ---------- Stories ----------
SCSS = gen.CSS.replace('height:1350px', 'height:1920px') + """
.frame{padding:210px 70px 250px}
main{gap:44px}
.card{width:820px;align-self:center;border-radius:30px;overflow:hidden;border:4px solid #32ccfe;box-shadow:0 30px 90px rgba(50,204,254,.25);transform:rotate(-2deg)}
.card img{width:100%;display:block}
.cta{align-self:center}
h1.st{font-size:56px}
.big{font-size:52px;font-weight:800;line-height:1.25}
.reply{font-family:'Press Start 2P';font-size:22px;color:#05070a;background:#fff;padding:26px 28px 22px;align-self:center;line-height:1.5;text-align:center}
.lang{display:flex;gap:18px;justify-content:center}
.lang span{font-family:'Press Start 2P';font-size:30px;border:3px solid #32ccfe;color:#32ccfe;padding:22px 26px 18px}
"""


def spage(tag, body, extra=''):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{SCSS}{extra}</style></head><body>
<div class="bgpat"></div><div class="glow"></div><div class="glow b"></div>
<div class="frame"><header><img src="{A}logo-w.svg"><span class="tag">{tag}</span></header>
<main>{body}</main>
<footer style="justify-content:center"><span>@studio.noobperdido</span></footer></div></body></html>"""


def newpost(cover, title, cta='TAP OUR PROFILE TO SEE IT', tag='NEW POST', card_style=''):
    return spage(tag, f"""<div class="card" style="{card_style}"><img src="{cover}"></div>
<h1 class="st" style="text-align:center">{title}</h1>
<div class="cta">{cta}</div>""")


NP = '20:15:00'
ENG = '13:00:00'
STORIES = [
    ('s01', '2026-11-23', NP, newpost(OUT + '01-hello-v2-1.jpg', 'WE\'RE ON<br><span class="b">INSTAGRAM!</span>')),
    ('s02', '2026-11-24', NP, newpost(OUT + '02-our-games-1.jpg', 'ONE IN DEV.<br><span class="b">TWO OUT NOW.</span>')),
    ('s03', '2026-11-25', NP, newpost(A + 'reel-frame.jpg', 'BLOCK QUEST<br><span class="b">IN 30 SECONDS</span>', 'NEW REEL ON OUR PROFILE', 'NEW REEL', 'width:560px')),
    ('s04', '2026-11-26', ENG, spage('BEHIND THE SCENES', f"""<p class="big">Benjamin's run cycle 🏃</p>
<img class="px" src="{A}benjamin_east_run.png" style="width:100%;image-rendering:pixelated">
<img class="px" src="{A}benjamin_run-f0.png" style="width:520px;align-self:center;image-rendering:pixelated">
<p>Six frames of 64×64 pixel art. Every step in Nexus: Last Signal is drawn by hand.</p>""")),
    ('s05', '2026-11-27', NP, newpost(OUT + '06-case-reunio-1.jpg', 'CASE STUDY:<br><span class="b">REUNIO</span>')),
    ('s06', '2026-11-30', NP, newpost(OUT + '04-devlog-1-1.jpg', 'DEVLOG #1<br><span class="b">IS LIVE</span>')),
    ('s07', '2026-12-01', ENG, spage('ASK US', f"""<img src="{A}glasses.svg" style="width:520px;align-self:center">
<h1 class="st" style="text-align:center">ASK US<br><span class="b">ANYTHING</span></h1>
<p class="big" style="text-align:center">Games, apps, pixel art, iPhone development. What do you want to know?</p>
<div class="reply">REPLY TO THIS STORY 💬</div>""")),
    ('s08', '2026-12-02', NP, newpost(OUT + '05-absolute-zero-1.jpg', 'MATH BECOMES<br><span class="b">A MISSION</span>')),
    ('s09', '2026-12-03', ENG, spage('BEHIND THE SCENES', f"""<p class="big">The Nexus art bible 🎨</p>
<div class="media" style="flex:0 0 auto"><img src="{A}G01_art_bible_a.jpg"></div>
<div class="media" style="flex:0 0 auto"><img src="{A}G01_art_bible_b.jpg"></div>
<p>Every color and shape of New Aurora starts here.</p>""")),
    ('s10', '2026-12-04', NP, newpost(OUT + '09-ai-no-hype-1.jpg', 'AI WITHOUT<br><span class="b">THE HYPE</span>')),
    ('s11', '2026-12-07', NP, newpost(OUT + '07-devlog-2-1.jpg', 'MEET<br><span class="b">BENJAMIN</span>')),
    ('s12', '2026-12-08', ENG, spage('YOUR IDEA', f"""<h1 class="st">GOT AN<br><span class="b">APP IDEA?</span></h1>
<p class="big">Tell us in one line. We'll tell you how we'd build it.</p>
<p class="lead">We work in</p>
<div class="lang"><span>ENGLISH</span></div><div class="lang"><span>ESPAÑOL</span><span>PORTUGUÊS</span></div>
<div class="reply">REPLY TO THIS STORY 💬</div>""")),
    ('s13', '2026-12-09', NP, newpost(OUT + '08-bq-worlds-1.jpg', 'FIVE WORLDS.<br><span class="b">ONE LOST JEWEL.</span>')),
    ('s14', '2026-12-10', ENG, spage('BEHIND THE SCENES', f"""<p class="big">Two enemies waiting for you in Nexus 👾</p>
<div class="row" style="justify-content:center;gap:30px">
<div class="cell" style="flex:1"><img src="{A}hollow_beast_south_idle-f0.png" style="width:400px;height:400px"><span>HOLLOW BEAST</span></div>
<div class="cell" style="flex:1"><img src="{A}iron_colossus_south_idle-f0.png" style="width:400px;height:400px"><span>IRON COLOSSUS</span></div></div>
<p>Which one would you fight first?</p>
<div class="reply">REPLY TO THIS STORY 💬</div>""")),
    ('s15', '2026-12-11', NP, newpost(OUT + '14-case-semilla-1.jpg', 'CASE STUDY:<br><span class="b">SEMILLA DE VIDA</span>')),
    ('s16', '2026-12-14', NP, newpost(OUT + '10-devlog-3-1.jpg', 'DEVLOG #3<br><span class="b">IS LIVE</span>')),
    ('s17', '2026-12-14', '21:00:00', spage('VOTE', f"""<h1 class="st">FIRST MISSION.<br><span class="b">PICK ONE.</span></h1>
<div class="grid" style="grid-template-columns:1fr 1fr">
<div class="cell"><img src="{A}skill_emp.png" style="width:240px;height:240px"><span>1 · EMP PULSE</span></div>
<div class="cell"><img src="{A}skill_energy_shield.png" style="width:240px;height:240px"><span>2 · SHIELD</span></div>
<div class="cell"><img src="{A}skill_nexus_surge.png" style="width:240px;height:240px"><span>3 · NEXUS SURGE</span></div>
<div class="cell"><img src="{A}skill_precision_shot.png" style="width:240px;height:240px"><span>4 · PRECISION</span></div></div>
<div class="reply">REPLY WITH 1, 2, 3 OR 4</div>""")),
    ('s18', '2026-12-16', NP, newpost(OUT + '15-lacesta-navidad-1.jpg', 'NAVIDAD<br><span class="g">SIN PASARTE</span>', 'MÍRALO EN NUESTRO PERFIL', 'NUEVO POST')),
    ('s19', '2026-12-17', ENG, spage('BLOCK QUEST', f"""<div class="phones" style="flex:0 0 1000px"><img src="{A}en-bq-3.jpg" style="max-height:1000px"></div>
<p class="big" style="text-align:center">Which Block Quest world is your favorite?</p>
<div class="reply">REPLY WITH ITS NAME 💎</div>""")),
    ('s20', '2026-12-18', ENG, spage('LACESTA', f"""<img src="{A}cesta/icon.png" style="width:300px;border-radius:68px;align-self:center">
<h1 class="st" style="text-align:center">¿CUÁNTO VAS A<br><span class="g">GASTAR EN LA COMPRA</span><br>DE NAVIDAD?</h1>
<p class="big" style="text-align:center">Pon un presupuesto y LaCesta te dice cuánto te queda en cada pasillo.</p>
<div class="reply">RESPONDE CON TU CIFRA 🛒</div>""")),
    ('s21', '2026-12-22', ENG, spage('YOUR TURN', f"""<h1 class="st" style="text-align:center">YOUR<br><span class="b">GAME OF</span><br>THE YEAR?</h1>
<img src="{A}glasses.svg" style="width:460px;align-self:center">
<p class="big" style="text-align:center">What did you play the most in 2026?</p>
<div class="reply">REPLY TO THIS STORY 🎮</div>""")),
    ('s22', '2026-12-23', NP, newpost(OUT + '11-holidays-1.jpg', 'HAPPY<br><span class="b">HOLIDAYS</span> 🎄')),
    ('s23', '2026-12-28', NP, newpost(OUT + '12-year-in-review-1.jpg', '2026<br><span class="b">IN PIXELS</span>')),
    ('s24', '2026-12-30', NP, newpost(OUT + '13-signal-2027-1.jpg', 'THE SIGNAL<br><span class="b">GROWS STRONGER</span>')),
    ('s25', '2026-12-31', ENG, spage('2027', f"""<img src="{A}glasses.svg" style="width:560px;align-self:center;filter:drop-shadow(0 0 40px rgba(50,204,254,.5))">
<h1 class="st" style="text-align:center">HAPPY<br><span class="b">NEW YEAR</span></h1>
<p class="big" style="text-align:center">Thank you for playing with us in 2026. See you in 2027 💙</p>""")),
]

if __name__ == '__main__':
    import sys
    status = sys.argv[1] if len(sys.argv) > 1 else 'Muy pronto en la App Store'
    hd = ROOT / 'html'
    s = LACESTA['slides']
    for i, sl in enumerate(s, 1):
        (hd / f"{LACESTA['id']}-{i}.html").write_text(gen.page(LACESTA['tag'], sl['html'].replace('{STATUS}', status), i, len(s), CESTA_CSS))
    sd = ROOT / 'html_st'
    sd.mkdir(exist_ok=True)
    for sid, d, t, h in STORIES:
        (sd / f'{sid}.html').write_text(h.replace('</style>', '.g{color:#34d399}</style>', 1))
    json.dump([{'id': sid, 'date': d, 'time': t} for sid, d, t, _ in STORIES], open(ROOT / 'stories.json', 'w'), indent=1)
    print(len(STORIES), 'stories')
