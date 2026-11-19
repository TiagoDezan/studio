import { defineMiddleware } from 'astro:middleware';
import { getSettings, recordVisit } from './lib/store';
import { isAdmin } from './lib/auth';
import { renderMaintenance } from './lib/maintenance';

const BOT = /bot|crawl|spider|slurp|preview|monitor|curl|wget|python|headless|lighthouse/i;
const PUBLIC_PAGES = new Set(['/', '/es/', '/en/', '/es', '/en']);

export const onRequest = defineMiddleware(async (ctx, next) => {
  const { pathname } = ctx.url;
  const isPanel = pathname.startsWith('/painel');

  // CSRF: reject cross-site form posts
  if (ctx.request.method === 'POST') {
    const origin = ctx.request.headers.get('origin');
    const host = ctx.request.headers.get('x-forwarded-host') || ctx.request.headers.get('host');
    let ok = false;
    try { ok = !!origin && !!host && new URL(origin).host === host; } catch {}
    if (!ok) return new Response('Forbidden', { status: 403 });
  }

  if (PUBLIC_PAGES.has(pathname) && ctx.request.method === 'GET') {
    const admin = isAdmin(ctx.cookies);
    if (getSettings().maintenance && !admin) {
      return renderMaintenance(pathname);
    }
    const ua = ctx.request.headers.get('user-agent') || '';
    if (!admin && !BOT.test(ua)) {
      let ref: string | null = null;
      try {
        const r = ctx.request.headers.get('referer');
        if (r) {
          const host = new URL(r).hostname.replace(/^www\./, '');
          if (host && !host.endsWith('noobperdido.com')) ref = host;
        }
      } catch {}
      recordVisit(pathname.endsWith('/') ? pathname : pathname + '/', ref);
    }
  }

  const res = await next();
  if (isPanel) {
    res.headers.set('X-Robots-Tag', 'noindex, nofollow');
    res.headers.set('Cache-Control', 'no-store');
  }
  res.headers.set('X-Content-Type-Options', 'nosniff');
  res.headers.set('Referrer-Policy', 'strict-origin-when-cross-origin');
  res.headers.set('X-Frame-Options', 'SAMEORIGIN');
  return res;
});
