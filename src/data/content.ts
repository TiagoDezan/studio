export const LANGS = ['pt', 'es', 'en'] as const;
export type Lang = (typeof LANGS)[number];

export const langPath: Record<Lang, string> = { pt: '/', es: '/es/', en: '/en/' };
export const langLabel: Record<Lang, string> = { pt: 'PT', es: 'ES', en: 'EN' };
export const htmlLang: Record<Lang, string> = { pt: 'pt-BR', es: 'es', en: 'en' };

type L = Record<Lang, string>;

export interface Project {
  id: string;
  kind: 'client' | 'own';
  name: string;
  client?: string;
  tag: L;
  summary: L;
  stack: string[];
  image: string;
  imageFit?: 'cover' | 'contain';
  /** background behind a logo-style image (used with imageFit: 'contain') */
  imageBg?: string;
  url?: string;
  urlLabel?: L;
  status?: L;
}

export const projects: Project[] = [
  {
    id: 'semilla',
    kind: 'client',
    name: 'Iglesia Semilla de Vida',
    client: 'Iglesia Semilla de Vida · España',
    tag: { pt: 'Aplicativo + web', es: 'App + web', en: 'App + web' },
    summary: {
      pt: 'O site da igreja e o Sistema de Gestión Eclesiástica, que cuida de membros, tesouraria com relatórios em PDF e permissões por cargo. Tem app nativo para iPhone e roda em produção todos os dias.',
      es: 'La web de la iglesia y el Sistema de Gestión Eclesiástica, que gestiona miembros, tesorería con informes en PDF y permisos por cargo. Tiene app nativa para iPhone y funciona en producción a diario.',
      en: "The church's website and the Sistema de Gestión Eclesiástica, which runs member records, treasury with PDF reports and role-based access. It ships with a native iPhone app and runs in production every day.",
    },
    stack: ['React', 'Supabase', 'SwiftUI', 'Docker'],
    image: '/projects/semilla-logo.svg',
    imageFit: 'contain',
    imageBg: '#3e4c59',
    url: 'https://semilladevida.org.es',
    urlLabel: { pt: 'Ver o site', es: 'Ver la web', en: 'Visit site' },
  },
  {
    id: 'reunio',
    kind: 'client',
    name: 'Reunio',
    client: 'SaaS para igrejas',
    tag: { pt: 'SaaS multi-igreja', es: 'SaaS multi-iglesia', en: 'Multi-church SaaS' },
    summary: {
      pt: 'Gestão de igrejas na web, iOS e Android: membros, tesouraria completa, notificações push, espanhol e português e modo escuro. Nasceu do Sistema de Gestión Eclesiástica da Semilla de Vida e hoje atende várias igrejas.',
      es: 'Gestión de iglesias en web, iOS y Android: miembros, tesorería completa, notificaciones push, español y portugués y modo oscuro. Nació del Sistema de Gestión Eclesiástica de Semilla de Vida y hoy da servicio a varias iglesias.',
      en: 'Church management on web, iOS and Android: members, full treasury, push notifications, Spanish and Portuguese, and dark mode. It grew out of the Semilla de Vida Sistema de Gestión Eclesiástica and now serves several churches.',
    },
    stack: ['React', 'TypeScript', 'Supabase', 'SwiftUI', 'PWA'],
    image: '/projects/reunio-1.webp',
    url: 'https://reunio.app',
    urlLabel: { pt: 'Conhecer o Reunio', es: 'Conocer Reunio', en: 'Discover Reunio' },
  },
  {
    id: 'nexus',
    kind: 'own',
    name: 'Nexus: Last Signal',
    tag: { pt: 'RPG de ação · iPhone e iPad', es: 'RPG de acción · iPhone y iPad', en: 'Action RPG · iPhone & iPad' },
    summary: {
      pt: 'Ano 2479. Um sinal chega da primeira colônia perdida e o Nexus deixa de ser um portal para virar uma prisão. Pixel art 3/4, combate híbrido e 8 capítulos.',
      es: 'Año 2479. Llega una señal de la primera colonia perdida y el Nexus deja de ser un portal para convertirse en una prisión. Pixel art 3/4, combate híbrido y 8 capítulos.',
      en: 'Year 2479. A signal arrives from the first lost colony, and the Nexus turns out to be a prison, not a gate. 3/4 pixel art, hybrid combat and 8 chapters.',
    },
    stack: ['Swift', 'SpriteKit', 'CloudKit'],
    image: '/projects/nexus-last-signal.svg',
    status: { pt: 'Em desenvolvimento', es: 'En desarrollo', en: 'In development' },
  },
  {
    id: 'zero',
    kind: 'own',
    name: 'Operação: Zero Absoluto',
    tag: { pt: 'Jogo educativo · 7 a 12 anos', es: 'Juego educativo · 7 a 12 años', en: 'Learning game · ages 7–12' },
    summary: {
      pt: 'Espiões mirins salvam a rede mundial de uma IA rebelde hackeando firewalls com matemática. 300 missões, dificuldade adaptativa e painel para os pais. Sem anúncios.',
      es: 'Pequeños espías salvan la red mundial de una IA rebelde hackeando cortafuegos con matemáticas. 300 misiones, dificultad adaptativa y panel para padres. Sin anuncios.',
      en: "Young spies save the world's network from a rogue AI by hacking firewalls with math. 300 missions, adaptive difficulty and a parents' dashboard. No ads.",
    },
    stack: ['Swift', 'SwiftUI', 'SpriteKit'],
    image: '/projects/zero-absoluto-1.webp',
    url: 'https://tiagodezan.github.io/games_policy/zero-absoluto/',
    urlLabel: { pt: 'Mais informações', es: 'Más información', en: 'More info' },
  },
  {
    id: 'blockquest',
    kind: 'own',
    name: 'Block Quest',
    tag: { pt: 'Puzzle 3D · iPhone e iPad', es: 'Puzle 3D · iPhone y iPad', en: '3D puzzle · iPhone & iPad' },
    summary: {
      pt: 'Encaixe peças num tabuleiro 8×8, limpe linhas e cumpra a missão de cada fase em cinco mundos. Gerador de peças justo e um robô que testa cada nível. Sem anúncios, sem cronômetro.',
      es: 'Encaja piezas en un tablero de 8×8, limpia filas y cumple la misión de cada nivel en cinco mundos. Generador de piezas justo y un robot que prueba cada nivel. Sin anuncios, sin cronómetro.',
      en: "Fit pieces on an 8×8 board, clear lines and beat each level's mission across five worlds. A fair piece generator and a bot that tests every level. No ads, no timers.",
    },
    stack: ['Swift 6', 'SwiftUI', 'SpriteKit'],
    image: '/projects/block-quest-1.webp',
    url: 'https://tiagodezan.github.io/games_policy/block-quest/',
    urlLabel: { pt: 'Mais informações', es: 'Más información', en: 'More info' },
  },
];

export const t = {
  meta: {
    title: { pt: 'Noob Perdido Studio · Apps, sites e jogos', es: 'Noob Perdido Studio · Apps, webs y juegos', en: 'Noob Perdido Studio · Apps, websites and games' },
    description: {
      pt: 'Estúdio que cria apps para iPhone e Android, sites, sistemas web e jogos. Do rascunho à loja, sem deixar você perdido no caminho.',
      es: 'Estudio que crea apps para iPhone y Android, webs, sistemas web y juegos. Del boceto a la tienda, sin que te pierdas por el camino.',
      en: 'A studio that builds iPhone and Android apps, websites, web systems and games. From sketch to store, without getting you lost on the way.',
    },
  },
  nav: {
    services: { pt: 'Serviços', es: 'Servicios', en: 'Services' },
    work: { pt: 'Projetos', es: 'Proyectos', en: 'Work' },
    process: { pt: 'Como funciona', es: 'Cómo trabajamos', en: 'Process' },
    contact: { pt: 'Falar com a gente', es: 'Hablemos', en: "Let's talk" },
  },
  hero: {
    eyebrow: { pt: 'Studio de apps, sites e jogos', es: 'Estudio de apps, webs y juegos', en: 'App, web and game studio' },
    title: { pt: 'Perdido com a sua ideia? A gente acha o caminho.', es: '¿Perdido con tu idea? Nosotros encontramos el camino.', en: 'Lost with your idea? We find the way.' },
    lead: {
      pt: 'Todo mundo começa noob. A gente transforma o seu rascunho em app, site ou sistema que funciona de verdade, e explica cada passo sem complicar.',
      es: 'Todo el mundo empieza siendo noob. Convertimos tu boceto en una app, web o sistema que funciona de verdad, y te explicamos cada paso sin complicaciones.',
      en: 'Everyone starts as a noob. We turn your rough idea into an app, website or system that really works, and explain every step in plain words.',
    },
    searchLabel: { pt: 'O que você precisa?', es: '¿Qué necesitas?', en: 'What do you need?' },
    searchHint: {
      pt: 'Escreva e aperte Enter. A gente leva a sua ideia direto para o formulário.',
      es: 'Escribe y pulsa Enter. Llevamos tu idea directamente al formulario.',
      en: 'Type and press Enter. We carry your idea straight to the form.',
    },
    searchExamples: {
      pt: ['um app para minha igreja', 'um site para o meu negócio', 'um sistema de agendamentos', 'um jogo para iPhone'],
      es: ['una app para mi iglesia', 'una web para mi negocio', 'un sistema de reservas', 'un juego para iPhone'],
      en: ['an app for my church', 'a website for my business', 'a booking system', 'an iPhone game'],
    },
    cta: { pt: 'Ver projetos', es: 'Ver proyectos', en: 'See our work' },
  },
  stats: [
    { value: '5', label: { pt: 'produtos no ar e em produção', es: 'productos publicados y en producción', en: 'products live and in production' } },
    { value: '3', label: { pt: 'plataformas: web, iOS e Android', es: 'plataformas: web, iOS y Android', en: 'platforms: web, iOS and Android' } },
    { value: '4', label: { pt: 'idiomas entregues nos apps', es: 'idiomas entregados en las apps', en: 'languages shipped in our apps' } },
  ],
  services: {
    eyebrow: { pt: 'Power-ups', es: 'Power-ups', en: 'Power-ups' },
    title: { pt: 'O que a gente faz', es: 'Lo que hacemos', en: 'What we do' },
    items: [
      {
        icon: 'phone',
        title: { pt: 'Apps para iPhone e Android', es: 'Apps para iPhone y Android', en: 'iPhone and Android apps' },
        body: {
          pt: 'Apps nativos em SwiftUI ou multiplataforma, publicados na App Store e no Google Play, com notificações, login e sincronização na nuvem.',
          es: 'Apps nativas en SwiftUI o multiplataforma, publicadas en App Store y Google Play, con notificaciones, inicio de sesión y sincronización en la nube.',
          en: 'Native SwiftUI or cross-platform apps, shipped to the App Store and Google Play, with notifications, sign-in and cloud sync.',
        },
      },
      {
        icon: 'web',
        title: { pt: 'Sites que convertem', es: 'Webs que convierten', en: 'Websites that convert' },
        body: {
          pt: 'Sites institucionais e landing pages rápidos, bonitos no celular e fáceis de achar no Google. Hospedagem e domínio inclusos se você quiser.',
          es: 'Webs corporativas y landing pages rápidas, bonitas en el móvil y fáciles de encontrar en Google. Alojamiento y dominio incluidos si quieres.',
          en: 'Fast company sites and landing pages that look great on phones and are easy to find on Google. Hosting and domain included if you like.',
        },
      },
      {
        icon: 'system',
        title: { pt: 'Sistemas e SaaS sob medida', es: 'Sistemas y SaaS a medida', en: 'Custom systems and SaaS' },
        body: {
          pt: 'Painéis, cadastros, financeiro, relatórios em PDF e permissões por cargo. O software que organiza o seu dia a dia, do jeito que você trabalha.',
          es: 'Paneles, registros, finanzas, informes en PDF y permisos por cargo. El software que organiza tu día a día, como tú trabajas.',
          en: 'Dashboards, records, finance, PDF reports and role-based access. Software that organizes your day, shaped around how you work.',
        },
      },
      {
        icon: 'game',
        title: { pt: 'Jogos mobile', es: 'Juegos móviles', en: 'Mobile games' },
        body: {
          pt: 'Do game design à publicação: puzzles, RPGs e jogos educativos com SpriteKit, pixel art e monetização honesta, sem pay-to-win.',
          es: 'Del game design a la publicación: puzles, RPG y juegos educativos con SpriteKit, pixel art y monetización honesta, sin pay-to-win.',
          en: 'From game design to launch: puzzles, RPGs and learning games with SpriteKit, pixel art and fair monetization, no pay-to-win.',
        },
      },
    ],
  },
  work: {
    clientsEyebrow: { pt: 'Clientes', es: 'Clientes', en: 'Clients' },
    clientsTitle: { pt: 'Quem já encontrou o caminho com a gente', es: 'Quien ya encontró el camino con nosotros', en: 'Who already found the way with us' },
    ownEyebrow: { pt: 'Criações próprias', es: 'Creaciones propias', en: 'Our own games' },
    ownTitle: { pt: 'Jogos que a gente cria por diversão (e muito teste)', es: 'Juegos que creamos por diversión (y muchas pruebas)', en: 'Games we make for fun (and a lot of testing)' },
  },
  process: {
    eyebrow: { pt: 'Como funciona', es: 'Cómo trabajamos', en: 'How it works' },
    title: { pt: 'Quatro fases, nenhum chefão surpresa', es: 'Cuatro fases, ningún jefe final sorpresa', en: 'Four levels, no surprise boss fight' },
    steps: [
      {
        title: { pt: 'Conversa', es: 'Charla', en: 'Chat' },
        body: { pt: 'Você conta a ideia do seu jeito. A gente faz as perguntas certas e devolve um escopo claro, com prazo e preço.', es: 'Nos cuentas la idea a tu manera. Hacemos las preguntas correctas y te devolvemos un alcance claro, con plazo y precio.', en: 'You tell us the idea your way. We ask the right questions and hand back a clear scope, timeline and price.' },
      },
      {
        title: { pt: 'Protótipo', es: 'Prototipo', en: 'Prototype' },
        body: { pt: 'Telas navegáveis antes de qualquer código, para você ver, clicar e mudar o que quiser enquanto é barato.', es: 'Pantallas navegables antes de escribir código, para que veas, hagas clic y cambies lo que quieras mientras es barato.', en: 'Clickable screens before any code, so you can see, tap and change anything while it is still cheap.' },
      },
      {
        title: { pt: 'Construção', es: 'Desarrollo', en: 'Build' },
        body: { pt: 'Entregas semanais que você testa no próprio celular. Nada de sumir por três meses.', es: 'Entregas semanales que pruebas en tu propio móvil. Nada de desaparecer tres meses.', en: 'Weekly builds you test on your own phone. No vanishing for three months.' },
      },
      {
        title: { pt: 'No ar', es: 'Lanzamiento', en: 'Launch' },
        body: { pt: 'Publicação na loja ou no seu domínio, hospedagem, monitoramento e suporte depois do lançamento.', es: 'Publicación en la tienda o en tu dominio, alojamiento, monitorización y soporte después del lanzamiento.', en: 'Store or domain launch, hosting, monitoring and support after release.' },
      },
    ],
  },
  contact: {
    eyebrow: { pt: 'Player 2, pronto?', es: 'Player 2, ¿listo?', en: 'Player 2, ready?' },
    title: { pt: 'Conte a sua ideia', es: 'Cuéntanos tu idea', en: 'Tell us your idea' },
    lead: {
      pt: 'Respondemos em até um dia útil, em português, espanhol ou inglês. Sem compromisso e sem juridiquês.',
      es: 'Respondemos en un día laborable como máximo, en español, portugués o inglés. Sin compromiso y sin jerga.',
      en: 'We reply within one business day, in English, Portuguese or Spanish. No commitment, no jargon.',
    },
    name: { pt: 'Seu nome', es: 'Tu nombre', en: 'Your name' },
    email: { pt: 'E-mail', es: 'Correo electrónico', en: 'Email' },
    type: { pt: 'Tipo de projeto', es: 'Tipo de proyecto', en: 'Project type' },
    types: {
      pt: ['App mobile', 'Site', 'Sistema / SaaS', 'Jogo', 'Ainda não sei'],
      es: ['App móvil', 'Web', 'Sistema / SaaS', 'Juego', 'Aún no lo sé'],
      en: ['Mobile app', 'Website', 'System / SaaS', 'Game', 'Not sure yet'],
    },
    message: { pt: 'Sobre o projeto', es: 'Sobre el proyecto', en: 'About the project' },
    messagePh: { pt: 'O que você quer construir, para quem e até quando?', es: '¿Qué quieres construir, para quién y para cuándo?', en: 'What do you want to build, for whom and by when?' },
    send: { pt: 'Enviar mensagem', es: 'Enviar mensaje', en: 'Send message' },
    sending: { pt: 'Enviando…', es: 'Enviando…', en: 'Sending…' },
    ok: { pt: 'Mensagem recebida! Respondemos em breve.', es: '¡Mensaje recibido! Te respondemos pronto.', en: 'Message received! We will get back to you soon.' },
    fail: { pt: 'Não deu para enviar. Tente de novo ou escreva para o nosso e-mail.', es: 'No se pudo enviar. Inténtalo de nuevo o escríbenos al correo.', en: 'Could not send. Try again or write to our email.' },
    or: { pt: 'Ou fale direto:', es: 'O escríbenos directamente:', en: 'Or reach us directly:' },
  },
  status: {
    open: { pt: 'Aceitando novos projetos', es: 'Aceptando nuevos proyectos', en: 'Taking new projects' },
    busy: { pt: 'Agenda cheia, abrindo lista de espera', es: 'Agenda llena, abrimos lista de espera', en: 'Fully booked, waitlist open' },
  },
  footer: {
    rights: { pt: 'Feito com café e muito Ctrl+Z.', es: 'Hecho con café y mucho Ctrl+Z.', en: 'Made with coffee and plenty of Ctrl+Z.' },
  },
  maintenance: {
    title: { pt: 'Voltamos já', es: 'Volvemos enseguida', en: 'Back soon' },
    body: { pt: 'Estamos dando um upgrade no site. Volte em alguns minutos.', es: 'Estamos mejorando la web. Vuelve en unos minutos.', en: 'We are upgrading the site. Check back in a few minutes.' },
  },
};

export const pick = (v: L, lang: Lang) => v[lang] ?? v.pt;
