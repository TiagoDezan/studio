# Noob Perdido Studio

Site do estúdio **Noob Perdido** — [studio.noobperdido.com](https://studio.noobperdido.com).
Astro (SSR, adapter Node), sem framework de UI, fontes self-hosted (Press Start 2P, Oxanium, Manrope).

- `/` português, `/es/` espanhol, `/en/` inglês. Textos e projetos em `src/data/content.ts`.
- Formulário de contato → `POST /api/contact` (honeypot + rate limit), salvo em `DATA_DIR/studio.json`.
- **Painel escondido** em `/painel` (sem link no site). Atalhos: digitar `/painel` na busca da home ou o código Konami.
  - Visão geral (visitas por dia/idioma/origem, sem cookies), mensagens (ler, destacar, apagar, CSV),
    site (disponibilidade, faixa de aviso, manutenção, contatos, webhook de aviso), projetos (mostrar/ordem), backup JSON.
  - Protegido por `ADMIN_PASSWORD` (mín. 8 caracteres). Sessão em cookie HMAC de 12h.

## Rodar local

```sh
npm install
ADMIN_PASSWORD=algumasenha npm run dev
```

## Deploy

Docker na VPS via Komodo Stack `studio` (este `compose.yaml`), container `studio` em `127.0.0.1:8406`,
proxy do nginx do Plesk para `studio.noobperdido.com` com Let's Encrypt. Push na `main` = deploy automático (webhook).
Variáveis no Komodo: `ADMIN_PASSWORD` (e opcionalmente `ADMIN_SECRET`). Dados ficam no volume `studio-data`.
