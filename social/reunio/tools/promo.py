from pathlib import Path
import gen
W=gen.W
P={'es':[('Oferta','<span class="o">20 %</span> de descuento<br>en tu plan.','Pro o Premium, mensual o anual.'),
         ('Cómo usarlo','Código<br><span class="o">REUNIO20</span>','En la web, escríbelo al pagar. En el iPhone, abre el enlace de la bio.'),
         ('Hasta el 31/12','Válido hasta el<br><span class="o">31 de diciembre</span>.','Miembros, tesorería, escalas y avisos en un solo lugar.')],
   'pt':[('Oferta','<span class="o">20 %</span> de desconto<br>no teu plano.','Pro ou Premium, mensal ou anual.'),
         ('Como usar','Código<br><span class="o">REUNIO20</span>','Na web, escreve-o no pagamento. No iPhone, abre o link da bio.'),
         ('Até 31/12','Válido até<br><span class="o">31 de dezembro</span>.','Membros, tesouraria, escalas e avisos num só lugar.')],
   'en':[('Offer','<span class="o">20% off</span><br>your plan.','Pro or Premium, monthly or yearly.'),
         ('How to use it','Code<br><span class="o">REUNIO20</span>','On the web, enter it at checkout. On iPhone, open the link in bio.'),
         ('Until Dec 31','Valid until<br><span class="o">December 31</span>.','Members, finances, rotas and notices in one place.')]}
IM=['tesoreria/01-resumen.png','inicio/01-inicio.png','portal-miembro/01-identidad.png']
for lang,fr in P.items():
    d=W/'gen_html'/'promo'/lang;d.mkdir(parents=True,exist_ok=True)
    for i,(tag,h,sub) in enumerate(fr):
        html=gen.slide(lang,tag,h,sub,gen.ph(gen.img(lang,IM[i]),220,820,640),f'{i+1}/4',True).replace('<h1>','<h1 style="font-size:96px">')
        (d/f's{i+1}.html').write_text(html)
    (d/'s4.html').write_text(gen.cta(lang,True,'4/4'))
