import { t, type Lang } from '../data/content';

export function renderMaintenance(pathname: string) {
  const lang: Lang = pathname.startsWith('/es') ? 'es' : pathname.startsWith('/en') ? 'en' : 'pt';
  const html = `<!doctype html><html lang="${lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Noob Perdido Studio</title><link rel="icon" href="/favicon.svg"><meta name="robots" content="noindex"><style>
html,body{margin:0;height:100%;background:#000;color:#fff;font:16px/1.6 system-ui,sans-serif}
main{min-height:100%;display:grid;place-items:center;text-align:center;padding:24px}
img{width:min(320px,70vw);height:auto;animation:look 4s steps(4) infinite}
h1{font-size:clamp(28px,6vw,48px);margin:24px 0 8px;letter-spacing:-.02em}
p{color:#a7b0b8;margin:0}b{color:#32ccfe}
@keyframes look{0%,100%{transform:translateX(0)}50%{transform:translateX(6px)}}
@media (prefers-reduced-motion:reduce){img{animation:none}}
</style></head><body><main><div><img src="/brand/glasses.svg" alt=""><h1>${t.maintenance.title[lang]}<b>…</b></h1><p>${t.maintenance.body[lang]}</p></div></main></body></html>`;
  return new Response(html, { status: 503, headers: { 'Content-Type': 'text/html; charset=utf-8', 'Retry-After': '600' } });
}
