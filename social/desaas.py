"""De-SaaS launch post + stories (Spanish)."""
import json, gen, extra
from pathlib import Path
A = gen.A; OUT = extra.OUT; ROOT = gen.ROOT
CSS = """
.d{color:#4d9bff}
.pill{font-family:'Press Start 2P';font-size:16px;background:#4d9bff;color:#05070a;padding:12px 16px 10px;align-self:flex-start}
ul.list li:before{background:#4d9bff}
.ico{border-radius:40px;box-shadow:0 0 60px rgba(77,155,255,.45)}
"""
ICON = f'<img class="ico" src="{A}desaas/icon.png" style="width:%dpx">'
SLIDES = [
 f"""<div class="row" style="gap:36px">{ICON % 220}<span class="pill">YA DISPONIBLE</span></div>
<h1>DE-SAAS:<br><span class="d">TU EMPRESA</span><br>EN UN SOLO LUGAR</h1>
<p class="lead">Gestión para pequeñas empresas en España.</p>
<p class="small">En la App Store y en la web</p>""",
 f"""<h2 style="color:#4d9bff">EL DIA A DIA</h2>
<h1 class="sm">TODO LO QUE<br>HACIAS EN <span class="d">EXCEL</span></h1>
<ul class="list"><li>Clientes y CRM<small>De la primera llamada a la venta</small></li><li>Presupuestos, facturas y recibos</li><li>Ingresos, gastos y cuentas</li><li>Calendario, mensajes e informes</li></ul>""",
 f"""<h2 style="color:#4d9bff">HECHO PARA ESPAÑA</h2>
<h1 class="sm">TU EQUIPO,<br><span class="d">EN ORDEN</span></h1>
<ul class="list"><li>Nóminas</li><li>Control horario de la jornada</li><li>Solicitudes de vacaciones</li><li>Documentos de empleados y clientes</li></ul>""",
 f"""{ICON % 260}
<h1 class="sm">SEGURO Y PARA<br><span class="d">TODO EL EQUIPO</span></h1>
<ul class="list"><li>Varias empresas en una sola cuenta</li><li>Permisos por rol<small>Administrador, gestor y trabajador</small></li><li>Acceso con doble factor</li><li>App de iPhone con widget</li></ul>
<div class="cta" style="background:#4d9bff">DESCARGALA EN LA APP STORE</div>""",
]
STORIES = [
 ('d1', '2026-11-25', '13:00:00', extra.spage('PROXIMAMENTE', f"""{ICON % 360}
<h1 class="st" style="text-align:center">MAÑANA<br><span class="d">LANZAMOS</span><br>ALGO NUEVO</h1>
<p class="big" style="text-align:center">Para pequeñas empresas en España. ¿Adivinas qué es?</p>
<div class="reply">RESPONDE CON TU APUESTA 👀</div>""".replace('align-self','align-self').replace('<img class="ico"','<img class="ico" style="align-self:center;width:360px"'))),
 ('d2', '2026-11-26', '20:15:00', extra.newpost(OUT + '16-desaas-1.jpg', 'DE-SAAS<br><span class="d">YA DISPONIBLE</span>', 'MIRALO EN NUESTRO PERFIL', 'NUEVO POST')),
 ('d3', '2026-11-27', '13:00:00', extra.spage('DE-SAAS', f"""<h1 class="st">¿TODAVIA HACES<br>LAS FACTURAS<br><span class="d">EN EXCEL?</span></h1>
<p class="big">Clientes, facturas, nóminas y control horario en una sola app.</p>
<div class="row" style="justify-content:center">{ICON % 300}</div>
<p class="lead" style="text-align:center">Busca <span class="d">De-SaaS</span> en la App Store</p>
<div class="reply">¿DUDAS? RESPONDE AQUI 💬</div>""")),
]
if __name__ == '__main__':
    hd = ROOT / 'html'
    for i, h in enumerate(SLIDES, 1):
        (hd / f'16-desaas-{i}.html').write_text(gen.page('DE-SAAS', h, i, len(SLIDES), CSS))
    sd = ROOT / 'html_st'
    for sid, d, t, h in STORIES:
        (sd / f'{sid}.html').write_text(h.replace('</style>', CSS + '</style>', 1))
