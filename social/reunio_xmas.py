import json
from pathlib import Path
ROOT=Path('/home/claude/social'); A='file:///home/claude/social/a/'
FONTS=(ROOT/'fonts/fonts.css').read_text()
T={
 'es':dict(h='Navidad con<br><span class="o">Reunio</span> 🎄',sub='Responde a esta historia y participa en nuestra campaña de Navidad.',
   p=[('3','Suscripciones <b>Premium</b>','1 año gratis'),('3','Suscripciones <b>Pro</b>','1 año gratis'),('50%','de descuento','para los 10 primeros')],
   cta='Responde a esta historia 💬',fine='Para los primeros en responder. Hasta agotar los premios.',tag='Gestión de iglesias'),
 'pt':dict(h='Natal com<br><span class="o">Reunio</span> 🎄',sub='Responda a este story e participe da nossa campanha de Natal.',
   p=[('3','Assinaturas <b>Premium</b>','1 ano grátis'),('3','Assinaturas <b>Pro</b>','1 ano grátis'),('50%','de desconto','para os 10 primeiros')],
   cta='Responda a este story 💬',fine='Para os primeiros que responderem. Até acabarem os prêmios.',tag='Gestão de igrejas'),
 'en':dict(h='Christmas with<br><span class="o">Reunio</span> 🎄',sub='Reply to this story to join our Christmas giveaway.',
   p=[('3','<b>Premium</b> subscriptions','1 year free'),('3','<b>Pro</b> subscriptions','1 year free'),('50%','off','for the first 10')],
   cta='Reply to this story 💬',fine='For the first people to reply. While prizes last.',tag='Church management'),
}
CSS=FONTS+"""
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden}
body{font-family:Manrope,sans-serif;color:#eadcca;background:radial-gradient(120% 70% at 50% 0%,#2f5a5b 0%,#163235 45%,#090f14 100%);position:relative}
.snow{position:absolute;inset:0;background-image:radial-gradient(circle,rgba(234,220,202,.55) 2px,transparent 3px),radial-gradient(circle,rgba(234,220,202,.3) 1.5px,transparent 2.5px);background-size:140px 140px,90px 90px;background-position:20px 40px,60px 10px;opacity:.5}
.glow{position:absolute;width:800px;height:800px;border-radius:50%;filter:blur(140px);background:#c75f1e;opacity:.18;left:140px;top:1150px}
.f{position:absolute;inset:0;padding:230px 80px 250px;display:flex;flex-direction:column;gap:46px}
.logo{height:120px;align-self:flex-start}
.tag{font-size:26px;font-weight:600;color:#7fb3b8;letter-spacing:4px;text-transform:uppercase;margin-top:-26px}
h1{font-size:104px;font-weight:800;line-height:1.05;color:#eadcca;letter-spacing:-2px}
.o{color:#e07a35}
.sub{font-size:40px;line-height:1.35;font-weight:600;color:#eadcca}
.p{display:flex;flex-direction:column;gap:22px}
.c{display:flex;align-items:center;gap:30px;background:rgba(234,220,202,.08);border:2px solid rgba(234,220,202,.18);border-radius:34px;padding:26px 34px}
.n{flex:none;min-width:170px;height:130px;border-radius:26px;background:#c75f1e;color:#fff6ea;font-size:72px;font-weight:800;display:flex;align-items:center;justify-content:center;padding:0 18px}
.c:nth-child(2) .n{background:#7fb3b8;color:#0b1a1d}
.c:nth-child(3) .n{background:#eadcca;color:#0b1a1d}
.t{font-size:40px;line-height:1.2;font-weight:600}.t b{font-weight:800;color:#fff}
.t small{display:block;font-size:30px;color:#9fc3c6;font-weight:600;margin-top:6px}
.cta{align-self:center;background:#eadcca;color:#0b1a1d;font-size:40px;font-weight:800;padding:30px 48px;border-radius:999px;margin-top:10px}
.fine{text-align:center;font-size:26px;color:#9fb0b3;margin-top:-20px}
.h{position:absolute;bottom:150px;left:0;right:0;text-align:center;font-size:28px;font-weight:700;color:#7fb3b8;letter-spacing:1px}
"""
def page(t):
    cards=''.join(f'<div class="c"><div class="n">{n}</div><div class="t">{a}<small>{b}</small></div></div>' for n,a,b in t['p'])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="snow"></div><div class="glow"></div>
<div class="f"><img class="logo" src="{A}reunio-logo-t.png"><div class="tag">{t['tag']}</div>
<h1>{t['h']}</h1><p class="sub">{t['sub']}</p><div class="p">{cards}</div>
<div class="cta">{t['cta']}</div><p class="fine">{t['fine']}</p></div><div class="h">@app.reunio</div></body></html>"""
for k,t in T.items(): (ROOT/'html_st'/f'reunio-xmas-{k}.html').write_text(page(t))
