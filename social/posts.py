"""Content of the December 2026 Instagram plan: slides (HTML bodies) and captions."""
import json

HT_DEV = '#gamedev #indiedev #indiegame #pixelart #devlog #iosgames #jogosindie #noobperdido'
HT_GAMES = '#indiegame #iosgames #jogosmobile #puzzlegame #gamedev #jogosindie #noobperdido'
HT_KIDS = '#jogoseducativos #matematica #educacao #paisefilhos #iosgames #indiegame #noobperdido'
HT_STUDIO = '#desenvolvimentodeapps #desenvolvimentoweb #startup #saas #apps #ia #noobperdido'

P = []


def post(id, date, kind, tag, caption, slides=None, ig_type='POST', media=None):
    P.append(dict(id=id, date=date, kind=kind, tag=tag, caption=caption.strip(), slides=slides or [], ig_type=ig_type, media=media or []))


def phones(*srcs, h=820):
    return '<div class="phones">' + ''.join(f'<img src="{{A}}{s}" style="height:{h}px">' for s in srcs) + '</div>'


# 1 ─ Prazer, Noob Perdido Studio
post('01-prazer', '2026-12-02T20:00:00', 'Estúdio', 'OLÁ, MUNDO', """
Prazer, Noob Perdido Studio 👓

A gente faz apps, sites, sistemas e jogos. E agora também ajuda empresas a usar IA sem hype.

Arrasta para o lado e conhece:
• o que a gente faz
• como a gente trabalha, em quatro fases
• o que vai aparecer por aqui toda semana

Perdido com a sua ideia? A gente acha o caminho. Conte a sua em studio.noobperdido.com (link na bio).

🇪🇸 Hola, somos Noob Perdido Studio: apps, webs, sistemas y juegos.
🇺🇸 Hi, we're Noob Perdido Studio: apps, websites, systems and games.

#noobperdido #gamedev #desenvolvimentodeapps #indiedev #apps #startup
""", [
    dict(html="""<div style="display:flex;flex-direction:column;gap:56px;align-items:flex-start">
<img src="{A}glasses.svg" style="width:520px;filter:drop-shadow(0 0 40px rgba(50,204,254,.5))">
<h1 class="xl">PRAZER,<br><span class="b">NOOB PERDIDO</span><br>STUDIO</h1>
<p class="lead">Perdido com a sua ideia?<br>A gente acha o caminho.</p></div>"""),
    dict(html="""<h1>O QUE A<br><span class="b">GENTE FAZ</span></h1>
<ul class="list">
<li><div>Apps para iPhone e Android<small>Nativos, rápidos e prontos para a App Store</small></div></li>
<li><div>Sites que convertem<small>Bonitos, leves e feitos para vender</small></div></li>
<li><div>Sistemas e SaaS sob medida<small>Do painel interno ao produto completo</small></div></li>
<li><div>Jogos mobile<small>Os nossos e os seus</small></div></li>
<li><div>Consultoria de IA<small>Sem hype e sem jargão</small></div></li></ul>"""),
    dict(html="""<h1 class="sm">QUATRO FASES,<br><span class="b">NENHUM CHEFÃO</span><br>SURPRESA</h1>
<div class="steps">
<div class="step"><span class="k">FASE 1</span><h3>Conversa</h3><p>Entendemos a ideia, o público e o orçamento.</p></div>
<div class="step"><span class="k">FASE 2</span><h3>Protótipo</h3><p>Você vê e toca antes de investir pesado.</p></div>
<div class="step"><span class="k">FASE 3</span><h3>Construção</h3><p>Entregas semanais, sem caixa-preta.</p></div>
<div class="step"><span class="k">FASE 4</span><h3>No ar</h3><p>Publicamos e seguimos junto depois.</p></div></div>"""),
    dict(html="""<h1>TODA SEMANA<br><span class="b">POR AQUI</span></h1>
<ul class="list">
<li><div>Segunda: Devlog do Nexus<small>O nosso RPG em desenvolvimento</small></div></li>
<li><div>Quarta: Nossos jogos<small>Block Quest e Operação: Zero Absoluto</small></div></li>
<li><div>Sexta: Estúdio<small>Cases, bastidores e IA</small></div></li></ul>
<div class="cta">CONTE A SUA IDEIA ▶<br>STUDIO.NOOBPERDIDO.COM</div>"""),
])

# 2 ─ Nossos jogos
post('02-nossos-jogos', '2026-12-03T20:00:00', 'Jogos', 'NOSSOS JOGOS', """
Três jogos, um estúdio 🎮

🛰️ Nexus: Last Signal: RPG de ação em pixel art para iPhone e iPad. Em desenvolvimento, com devlog toda segunda.
🧮 Operação: Zero Absoluto: espiões mirins salvam a rede mundial hackeando firewalls com matemática. Para 7 a 12 anos, sem anúncios.
🧩 Block Quest: puzzle de blocos em cinco mundos mágicos. Sem anúncios e sem cronômetro.

Qual você quer conhecer primeiro? Conta nos comentários 👇

🇪🇸 Tres juegos: Nexus (en desarrollo), Operación: Cero Absoluto y Block Quest.
🇺🇸 Three games: Nexus (in development), Operation: Absolute Zero and Block Quest.

""" + HT_GAMES, [
    dict(html="""<h1 class="xl">NOSSOS<br><span class="b">JOGOS</span></h1>
<div class="row" style="justify-content:space-between">
<img src="{A}nexus-icon.jpg" style="width:290px;border-radius:64px;border:3px solid rgba(50,204,254,.5)">
<img src="{A}zero-icon.png" style="width:290px;border-radius:64px;border:3px solid rgba(50,204,254,.5)">
<img src="{A}pt-BR-iphone-1-inicio.jpg" style="width:290px;height:290px;object-fit:cover;object-position:50% 22%;border-radius:64px;border:3px solid rgba(50,204,254,.5)"></div>
<p class="lead">Um em desenvolvimento.<br>Dois prontos para jogar.</p>"""),
    dict(html="""<span class="status">EM DESENVOLVIMENTO</span>
<h1 class="sm">NEXUS:<br><span class="b">LAST SIGNAL</span></h1>
<div class="media" style="flex:0 0 520px"><img src="{A}G02_benjamin_concept.jpg" style="object-position:50% 30%"></div>
<p>RPG de ação para iPhone e iPad. Pixel art 3/4, combate híbrido e 8 capítulos.</p>"""),
    dict(html="""<span class="status ok">PRONTO</span>
<h1 class="sm">OPERAÇÃO:<br><span class="b">ZERO ABSOLUTO</span></h1>
<div class="row" style="flex:1;min-height:0;align-items:stretch">
<img src="{A}iphone-6.9-01-hack.jpg" style="height:800px;border-radius:32px;border:3px solid rgba(50,204,254,.45)">
<div style="display:flex;flex-direction:column;gap:28px;justify-content:center"><p>Matemática vira missão de espionagem.</p><p class="small">7 a 12 anos · 300 missões · sem anúncios</p></div></div>"""),
    dict(html="""<span class="status ok">PRONTO</span>
<h1 class="sm">BLOCK<br><span class="b">QUEST</span></h1>
<div class="row" style="flex:1;min-height:0;align-items:stretch">
<img src="{A}pt-BR-iphone-2-floresta-esmeralda.jpg" style="height:800px;border-radius:32px;border:3px solid rgba(50,204,254,.45)">
<div style="display:flex;flex-direction:column;gap:28px;justify-content:center"><p>Encaixe peças, limpe linhas e cumpra a missão de cada fase.</p><p class="small">5 mundos · sem anúncios · sem cronômetro</p></div></div>"""),
])

# 3 ─ Block Quest Reel
post('03-bq-reel', '2026-12-04T20:00:00', 'Jogos', 'BLOCK QUEST', """
Block Quest em 30 segundos 🧩✨

Encaixe peças num tabuleiro 8×8, limpe linhas e cumpra a missão de cada fase. Floresta Esmeralda, Vale do Fogo, Oceano de Cristal, Reino Celestial e mais.

✔️ Sem anúncios
✔️ Sem cronômetro
✔️ Capítulo 1 grátis

Para iPhone e iPad. Link na bio.

🇪🇸 Puzle de bloques en cinco mundos mágicos. Sin anuncios y sin cronómetro.
🇺🇸 A block puzzle across five magical worlds. No ads, no timers.

""" + HT_GAMES, ig_type='REEL', media=['03-bq-reel.mp4'])

# 4 ─ Devlog #1
post('04-devlog-1', '2026-12-07T20:00:00', 'Devlog', 'DEVLOG #1', """
Devlog #1 · Nexus: Last Signal 🛰️

Ano 2479. A humanidade cruza as estrelas pelo Nexus, uma rede de portais alienígenas. Há 17 anos, a primeira colônia, Resplendor, sumiu sem pedir socorro.

Agora chegou um sinal de lá. A mensagem diz só uma coisa:
"A porta nunca deveria ter sido aberta."

Nexus: Last Signal é o nosso RPG de ação para iPhone e iPad: pixel art 3/4, combate híbrido e 8 capítulos. Toda segunda a gente mostra um pedaço do desenvolvimento por aqui.

Ativa as notificações para não perder o sinal 📡

🇪🇸 Año 2479. Una señal llega de la primera colonia perdida. Devlog cada lunes.
🇺🇸 Year 2479. A signal arrives from the first lost colony. New devlog every Monday.

""" + HT_DEV, [
    dict(html="""<div class="media"><img src="{A}G02_benjamin_concept.jpg" style="object-position:50% 25%"></div>
<h1>NEXUS:<br><span class="b">LAST SIGNAL</span></h1>"""),
    dict(html="""<h1 class="xl">ANO<br><span class="b">2479.</span></h1>
<p class="lead">A humanidade cruza as estrelas pelo Nexus, uma rede de portais alienígenas.</p>
<p>Há 17 anos, a primeira colônia, Resplendor, sumiu sem pedir socorro. Depois vieram outras.</p>
<div class="media" style="flex:0 0 330px"><img src="{A}G01_art_bible_a.jpg" style="object-position:85% 70%"></div>"""),
    dict(html="""<h1>O <span class="b">SINAL</span></h1>
<p>Benjamin, ex-agente da AEGIS, recebe uma mensagem vinda de Resplendor:</p>
<div class="quote">"A porta nunca deveria ter sido aberta."</div>
<div class="row" style="justify-content:center;gap:60px;margin-top:20px">
<img class="px" src="{A}portrait_benjamin.png" style="width:300px">
<img class="px" src="{A}portrait_orion.png" style="width:300px"></div>"""),
    dict(html="""<h1>O QUE<br><span class="b">VEM AÍ</span></h1>
<ul class="list">
<li>Pixel art em perspectiva 3/4</li>
<li>Combate híbrido: armas, esquiva e habilidades</li>
<li>8 capítulos, 8 chefões</li>
<li>iPhone e iPad, com save no iCloud</li></ul>
<div class="row" style="justify-content:space-between">
<img class="px" src="{A}portrait_benjamin.png" style="width:200px"><img class="px" src="{A}portrait_isabela.png" style="width:200px">
<img class="px" src="{A}portrait_orion.png" style="width:200px"><img class="px" src="{A}portrait_survivor.png" style="width:200px"></div>"""),
])

# 5 ─ Zero Absoluto
post('05-zero-absoluto', '2026-12-09T20:00:00', 'Jogos', 'ZERO ABSOLUTO', """
Operação: Zero Absoluto 🧮🕵️

Uma IA rebelde tomou a rede mundial. Só uma equipe de espiões mirins pode derrubar os firewalls, e a arma deles é a matemática.

• 300 missões em 3 operações
• A dificuldade se ajusta ao ritmo da criança
• Painel dos pais para acompanhar cada habilidade
• Sem anúncios e sem coleta de dados

Para crianças de 7 a 12 anos, no iPhone e no iPad. Marca aquele pai ou mãe que precisa conhecer 👇

🇪🇸 Pequeños espías salvan la red con matemáticas. De 7 a 12 años, sin anuncios.
🇺🇸 Young spies save the network with math. Ages 7 to 12, no ads.

""" + HT_KIDS, [
    dict(html="""<div class="media"><img src="{A}zero-cipher.jpg" style="object-position:50% 45%"></div>
<h1 class="sm">OPERAÇÃO:<br><span class="b">ZERO ABSOLUTO</span></h1>
<p class="lead">Matemática que vira missão.</p>"""),
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:48px">
<img src="{A}iphone-6.9-01-hack.jpg" style="height:960px;border-radius:36px;border:3px solid rgba(50,204,254,.45)">
<div style="display:flex;flex-direction:column;gap:30px"><h2>HACKEIE COM CONTAS</h2><p>Espiões mirins derrubam firewalls resolvendo operações para salvar a rede de uma IA rebelde.</p></div></div>"""),
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:48px">
<div style="display:flex;flex-direction:column;gap:30px"><h2>300 MISSÕES</h2><p>Três operações, do metrô abandonado à nuvem. A dificuldade acompanha a criança.</p></div>
<img src="{A}iphone-6.9-02-map.jpg" style="height:960px;border-radius:36px;border:3px solid rgba(50,204,254,.45)"></div>"""),
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:48px">
<img src="{A}iphone-6.9-03-parent.jpg" style="height:960px;border-radius:36px;border:3px solid rgba(50,204,254,.45)">
<div style="display:flex;flex-direction:column;gap:30px"><h2>PAINEL DOS PAIS</h2><p>Veja o que a criança domina e onde precisa de reforço.</p><p class="small">Sem anúncios. Nenhum dado sai do aparelho.</p></div></div>"""),
])

# 6 ─ Case Reunio
post('06-case-reunio', '2026-12-11T20:00:00', 'Estúdio', 'CASE', """
Case: Reunio ⛪📱

O Reunio nasceu dentro de uma igreja de verdade, a partir do sistema que fizemos para a Semilla de Vida. Hoje é um SaaS que atende várias igrejas na web, no iPhone e no Android.

O que entregamos:
• Membros, tesouraria completa, escalas e avisos
• Notificações push
• Espanhol, português e inglês, com modo escuro
• App na App Store

Tem uma ideia que poderia virar um produto assim? Chama no direct ou em studio.noobperdido.com.

🇪🇸 Reunio: gestión de iglesias en web, iOS y Android, hecho por nosotros.
🇺🇸 Reunio: church management on web, iOS and Android, built by us.

""" + HT_STUDIO, [
    dict(html="""<h1>CASE:<br><span class="b">REUNIO</span></h1>
<p class="lead">De uma igreja para várias.</p>
<div class="media" style="flex:0 0 520px;background:#0b0d10"><img src="{A}reunio-1.webp" style="object-fit:contain"></div>
<p>Gestão de igrejas na web, no iPhone e no Android.</p>"""),
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:48px">
<img src="{A}reunio-01-inicio.jpg" style="height:960px;border-radius:36px;border:3px solid rgba(50,204,254,.45)">
<div style="display:flex;flex-direction:column;gap:30px"><h2>COMO NASCEU</h2><p>Começou como o sistema de gestão da Iglesia Semilla de Vida. Virou um SaaS para muitas igrejas.</p><p class="small">Web · iPhone · Android</p></div></div>"""),
    dict(html="""<h1>O QUE<br><span class="b">ENTREGAMOS</span></h1>
<ul class="list"><li>Membros, tesouraria, escalas e avisos</li><li>Notificações push</li><li>Espanhol, português e inglês</li><li>App na App Store</li></ul>
<div class="chips"><span class="chip o">REACT</span><span class="chip o">TYPESCRIPT</span><span class="chip o">SUPABASE</span><span class="chip o">SWIFTUI</span></div>
<div class="cta">TEM UMA IDEIA ASSIM? ▶<br>FALE COM A GENTE</div>"""),
])

# 7 ─ Devlog #2 Benjamin
post('07-devlog-2', '2026-12-14T20:00:00', 'Devlog', 'DEVLOG #2', """
Devlog #2 · Conheça o Benjamin 🎨

Ex-agente de operações especiais da AEGIS, 30 anos. Reservado, observador, decide rápido. É ele quem recebe o sinal de Resplendor.

Arrasta para ver o caminho dele até o jogo:
1. Conceito: a armadura, o visor e a paleta
2. Turnaround: frente, costas e perfil, para manter o personagem igual de todos os ângulos
3. Sprite: o pixel art que você controla no iPhone

Qual parte do processo você quer ver no próximo devlog?

🇪🇸 De la ilustración al sprite: así nació Benjamin.
🇺🇸 From concept to sprite: meet Benjamin.

""" + HT_DEV, [
    dict(html="""<div class="media"><img src="{A}G02_benjamin_concept.jpg" style="object-position:50% 20%"></div>
<h1>CONHEÇA O<br><span class="b">BENJAMIN</span></h1>"""),
    dict(html="""<h2>1 CONCEITO ▶ 2 TURNAROUND</h2>
<p>Frente, costas e perfil desenhados juntos, para o personagem ficar igual de todos os ângulos.</p>
<div class="media" style="flex:0 0 auto;background:#ff00ff"><img src="{A}G02_benjamin_turnaround.jpg" style="height:auto"></div>
<p class="small">O fundo rosa é proposital: ele é removido na hora de virar sprite.</p>"""),
    dict(html="""<h2>3 SPRITE</h2>
<p>O pixel art que você controla: parado, andando, correndo e interagindo.</p>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px;align-items:center">
<div style="width:880px;height:220px;background:url({A}benjamin_south_idle.png) 0 0/880px 220px no-repeat;image-rendering:pixelated"></div>
<div style="width:960px;height:160px;background:url({A}benjamin_east_run.png) 0 0/960px 160px no-repeat;image-rendering:pixelated"></div></div>"""),
])

# 8 ─ Block Quest robot
post('08-bq-robo', '2026-12-16T20:00:00', 'Jogos', 'BLOCK QUEST', """
Um robô joga cada fase do Block Quest antes de você 🤖🧩

Por trás dos cinco mundos tem dois segredos:
• Um gerador de peças justo: nada de fase impossível por azar
• Um robô que testa cada nível e garante que dá para vencer

O resultado é um puzzle desafiador, mas nunca injusto. E sem anúncios nem cronômetro, no seu ritmo.

Capítulo 1 grátis no iPhone e iPad. Link na bio.

🇪🇸 Un robot prueba cada nivel antes que tú. Sin anuncios, sin cronómetro.
🇺🇸 A bot tests every level before you play it. No ads, no timers.

""" + HT_GAMES, [
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:44px">
<img src="{A}pt-BR-iphone-1-inicio.jpg" style="height:980px;border-radius:36px;border:3px solid rgba(50,204,254,.45)">
<h1 class="sm">UM <span class="b">ROBÔ</span> TESTA CADA FASE</h1></div>"""),
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:44px">
<div style="display:flex;flex-direction:column;gap:30px"><h2>TABULEIRO 8×8</h2><p>Encaixe peças, limpe linhas e cumpra a missão de cada fase.</p></div>
<img src="{A}pt-BR-iphone-2-floresta-esmeralda.jpg" style="height:980px;border-radius:36px;border:3px solid rgba(50,204,254,.45)"></div>"""),
    dict(html="""<div class="row" style="flex:1;min-height:0;align-items:center;gap:44px">
<img src="{A}pt-BR-iphone-4-vale-do-fogo.jpg" style="height:980px;border-radius:36px;border:3px solid rgba(50,204,254,.45)">
<div style="display:flex;flex-direction:column;gap:30px"><h2>NUNCA INJUSTO</h2><p>O gerador de peças é justo e um robô joga cada nível antes de você.</p></div></div>"""),
    dict(html="""<h1>5 MUNDOS.<br><span class="b">NO SEU RITMO.</span></h1>
""" + phones('pt-BR-iphone-3-mapa.jpg', 'pt-BR-iphone-5-oceano-de-cristal.jpg', 'pt-BR-iphone-6-reino-celestial.jpg', h=640) + """
<div class="chips"><span class="chip">SEM ANÚNCIOS</span><span class="chip">SEM CRONÔMETRO</span><span class="chip">CAP. 1 GRÁTIS</span></div>"""),
])

# 9 ─ IA sem hype
post('09-ia-sem-hype', '2026-12-18T20:00:00', 'Estúdio', 'IA', """
IA sem hype 🤖

Sem jargão e sem promessa milagrosa. A gente descobre onde a IA economiza tempo e dinheiro no seu negócio, integra nos sistemas que você já usa e treina a sua equipe.

Cinco formas de começar:
1. Diagnóstico de IA
2. Assistentes e agentes
3. Automação e integração
4. IA dentro do seu produto
5. Treinamento de equipes

Quer saber onde a IA faz sentido para você? Fale com a gente em studio.noobperdido.com.

🇪🇸 IA sin humo: diagnóstico, agentes, automatización y formación.
🇺🇸 AI without the hype: assessment, agents, automation and training.

""" + HT_STUDIO, [
    dict(html="""<h1 class="xl">IA<br><span class="b">SEM HYPE</span></h1>
<p class="lead">A gente descobre onde a IA economiza tempo e dinheiro no seu negócio.</p>
<img src="{A}glasses.svg" style="width:420px;align-self:flex-end;opacity:.9">"""),
    dict(html="""<h1 class="sm">CINCO FORMAS<br><span class="b">DE COMEÇAR</span></h1>
<ul class="list">
<li><div>Diagnóstico de IA<small>Onde vale a pena e onde não vale</small></div></li>
<li><div>Assistentes e agentes<small>Atendimento e tarefas repetitivas</small></div></li>
<li><div>Automação e integração<small>Nos sistemas que você já usa</small></div></li>
<li><div>IA dentro do seu produto<small>Recursos novos para os seus clientes</small></div></li>
<li><div>Treinamento de equipes<small>Para usar no dia a dia</small></div></li></ul>"""),
    dict(html="""<h1>POR ONDE<br><span class="b">COMEÇAR?</span></h1>
<p class="lead">Um diagnóstico curto mostra onde a IA faz diferença no seu negócio.</p>
<p>Sem contrato longo e sem jargão.</p>
<div class="cta">FALE COM A GENTE ▶<br>STUDIO.NOOBPERDIDO.COM</div>"""),
])

# 10 ─ Devlog #3 habilidades e arsenal
SK = [('skill_emp.png', 'PULSO EMP'), ('skill_energy_shield.png', 'ESCUDO'), ('skill_nexus_surge.png', 'NEXUS SURGE'),
      ('skill_precision_shot.png', 'TIRO PRECISO'), ('skill_emergency_recovery.png', 'RECUPERAÇÃO'), ('skill_energy_burst.png', 'EXPLOSÃO')]
IT = [('item_plasma_pistol.png', 'PISTOLA DE PLASMA'), ('item_pulse_rifle.png', 'RIFLE DE PULSO'), ('item_heavy_blaster.png', 'BLASTER PESADO'),
      ('item_nova_cannon.png', 'CANHÃO NOVA'), ('item_aegis_vest.png', 'COLETE AEGIS'), ('item_reactor_core.png', 'NÚCLEO DE REATOR')]


def grid(items, cols=3):
    return f'<div class="grid" style="grid-template-columns:repeat({cols},1fr)">' + ''.join(
        f'<div class="cell"><img src="{{A}}{s}"><span>{n}</span></div>' for s, n in items) + '</div>'


post('10-devlog-3', '2026-12-21T20:00:00', 'Devlog', 'DEVLOG #3', """
Devlog #3 · Habilidades e arsenal ⚡🔫

O combate do Nexus é híbrido: duas armas equipadas, esquiva e habilidades, tudo na tela do iPhone. Cada ícone aqui virou pixel art 64×64 para o jogo.

Arrasta para ver algumas habilidades e equipamentos do Benjamin.

Pergunta do dia: qual você leva para a primeira missão? Vota nos stories 👀

🇪🇸 Habilidades y armas de Nexus: ¿cuál te llevas a la primera misión?
🇺🇸 Nexus skills and gear: which one do you take on your first mission?

""" + HT_DEV, [
    dict(html="""<h1>HABILIDADES<br><span class="b">E ARSENAL</span></h1>
<p>Duas armas equipadas, esquiva e habilidades.</p>""" + grid(SK)),
    dict(html="""<h2>ARSENAL</h2><p>Cada item vira um ícone de 64×64 pixels no jogo.</p>""" + grid(IT)),
    dict(html="""<h1>QUAL VOCÊ<br><span class="b">LEVA PARA</span><br>A MISSÃO?</h1>""" + grid(SK[:3]) + """<p class="lead">Vota nos stories 👀</p>"""),
])

# 11 ─ Natal
post('11-natal', '2026-12-23T20:00:00', 'Jogos', 'FELIZ NATAL', """
Um presente que ensina 🎄🧮

Operação: Zero Absoluto transforma matemática em missão de espionagem para crianças de 7 a 12 anos.

Sem anúncios, sem coleta de dados e com painel para os pais acompanharem cada habilidade. Um jeito diferente de passar as férias jogando e aprendendo.

Feliz Natal de toda a equipe Noob Perdido 💙

🇪🇸 Un regalo que enseña: matemáticas convertidas en misión. ¡Feliz Navidad!
🇺🇸 A gift that teaches: math turned into a spy mission. Merry Christmas!

""" + HT_KIDS, [
    dict(html="""<h1>UM PRESENTE<br><span class="b">QUE ENSINA</span></h1>
<div class="row" style="flex:1;min-height:0;align-items:center;justify-content:center;gap:40px">
<img src="{A}zero-icon.png" style="width:380px;border-radius:84px;border:3px solid rgba(50,204,254,.5)">
<img src="{A}iphone-6.9-01-hack.jpg" style="height:720px;border-radius:32px;border:3px solid rgba(50,204,254,.45)"></div>
<div class="chips"><span class="chip">7 A 12 ANOS</span><span class="chip">SEM ANÚNCIOS</span><span class="chip o">FELIZ NATAL</span></div>"""),
])

# 12 ─ Retrospectiva
post('12-retrospectiva', '2026-12-28T20:00:00', 'Estúdio', 'RETRÔ 2026', """
2026 em pixels 👾

Foi o ano em que o Noob Perdido virou estúdio:
• Block Quest e Operação: Zero Absoluto prontos
• Reunio na App Store, atendendo várias igrejas
• O sistema da Semilla de Vida rodando todos os dias
• O motor do Nexus: Last Signal de pé, do combate ao save no iCloud
• Site novo em português, espanhol e inglês

Obrigado a todo mundo que jogou, testou e confiou no nosso trabalho. Em 2027 tem mais 💙

🇪🇸 2026 en píxeles: dos juegos listos, Reunio en el App Store y Nexus en marcha.
🇺🇸 2026 in pixels: two games done, Reunio on the App Store and Nexus underway.

#noobperdido #retrospectiva2026 #gamedev #indiedev #desenvolvimentodeapps
""", [
    dict(html="""<h1 class="xl">2026<br><span class="b">EM PIXELS</span></h1>
<p class="lead">O ano em que o Noob Perdido virou estúdio.</p>
<img src="{A}glasses.svg" style="width:460px;align-self:center;margin-top:40px">"""),
    dict(html="""<h2>O QUE ROLOU</h2>
<ul class="list">
<li>Block Quest e Operação: Zero Absoluto prontos</li>
<li>Reunio na App Store</li>
<li>Semilla de Vida em produção todos os dias</li>
<li>O motor do Nexus de pé, do combate ao iCloud</li>
<li>Site novo em três idiomas</li></ul>"""),
    dict(html="""<h1>OBRIGADO POR<br><span class="b">JOGAR COM</span><br>A GENTE</h1>
<p class="lead">Em 2027 tem mais.</p>
<div class="row" style="justify-content:space-between;margin-top:30px">
<img src="{A}nexus-icon.jpg" style="width:280px;border-radius:60px"><img src="{A}zero-icon.png" style="width:280px;border-radius:60px">
<img src="{A}pt-BR-iphone-1-inicio.jpg" style="width:280px;height:280px;object-fit:cover;object-position:50% 22%;border-radius:60px"></div>"""),
])

# 13 ─ 2027
post('13-sinal-2027', '2026-12-30T20:00:00', 'Devlog', 'NEXUS', """
2027: o sinal fica mais forte 📡

O próximo passo do Nexus: Last Signal é o Capítulo 1, The Fallen City. É nele que o Benjamin chega a Resplendor para descobrir quem mandou o sinal.

Os devlogs continuam toda segunda. Ativa as notificações e vem com a gente.

Feliz Ano Novo 🎆

🇪🇸 2027: la señal se hace más fuerte. ¡Feliz Año Nuevo!
🇺🇸 2027: the signal grows stronger. Happy New Year!

""" + HT_DEV, [
    dict(html="""<div class="media" style="flex:0 0 760px"><img src="{A}nexus-icon.jpg" style="object-position:50% 45%"></div>
<h1>2027:<br>O SINAL FICA<br><span class="b">MAIS FORTE</span></h1>"""),
])

# 14 ─ Case Semilla (janeiro)
post('14-case-semilla', '2027-01-08T20:00:00', 'Estúdio', 'CASE', """
Case: Iglesia Semilla de Vida 🌱

Para a Semilla de Vida, na Espanha, fizemos o site da igreja e o Sistema de Gestión Eclesiástica:
• Membros e permissões por cargo
• Tesouraria com relatórios em PDF
• App nativo para iPhone

Está em produção todos os dias, e foi dele que nasceu o Reunio.

Sua organização ainda vive de planilha? A gente resolve. studio.noobperdido.com

🇪🇸 Web, sistema de gestión y app para iPhone de la Iglesia Semilla de Vida.
🇺🇸 Website, management system and iPhone app for Iglesia Semilla de Vida.

""" + HT_STUDIO, [
    dict(html="""<h1>CASE:<br><span class="b">SEMILLA DE VIDA</span></h1>
<div class="media" style="background:#3e4c59;display:flex;align-items:center;justify-content:center"><img src="{A}semilla-logo.svg" style="width:80%;height:auto;object-fit:contain"></div>
<p class="lead">Site, sistema e app para uma igreja na Espanha.</p>"""),
    dict(html="""<h2>O QUE FIZEMOS</h2>
<div class="media" style="flex:0 0 480px"><img src="{A}semilla-sge.svg"></div>
<ul class="list"><li>Membros e permissões por cargo</li><li>Tesouraria com relatórios em PDF</li><li>App nativo para iPhone</li></ul>"""),
    dict(html="""<h1>EM PRODUÇÃO<br><span class="b">TODO DIA</span></h1>
<p class="lead">E foi daqui que nasceu o Reunio.</p>
<div class="chips"><span class="chip o">REACT</span><span class="chip o">SUPABASE</span><span class="chip o">SWIFTUI</span><span class="chip o">DOCKER</span></div>
<div class="cta">AINDA NA PLANILHA? ▶<br>FALE COM A GENTE</div>"""),
])

json.dump(P, open('/home/claude/social/posts.json', 'w'), ensure_ascii=False, indent=1)
print(len(P), 'posts', sum(len(p['slides']) for p in P), 'slides')
