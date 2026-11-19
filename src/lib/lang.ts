import type { Lang } from '../data/content';

// Spanish- and Portuguese-speaking countries (ISO 3166-1 alpha-2)
const ES = new Set(['ES','MX','AR','CO','PE','VE','CL','EC','GT','CU','BO','DO','HN','PY','SV','NI','CR','PA','UY','PR','GQ','AD']);
const PT = new Set(['BR','PT','AO','MZ','CV','GW','ST','TL','MO']);

/**
 * Picks the site language for a first visit to "/".
 * 1. The visitor's preferred browser language (Accept-Language), using its region when the
 *    language itself is neither Spanish nor Portuguese (e.g. ca-ES, gl-ES → es).
 * 2. Fallback: the country header Cloudflare adds when the DNS record is proxied (CF-IPCountry).
 * 3. Otherwise English.
 */
export function detectLang(acceptLanguage: string | null, country: string | null): Lang {
  const prefs = (acceptLanguage || '')
    .split(',')
    .map((part) => {
      const [tag, ...params] = part.trim().split(';');
      const q = Number(params.find((p) => p.trim().startsWith('q='))?.split('=')[1] ?? 1);
      return { tag: tag.toLowerCase(), q: Number.isFinite(q) ? q : 0 };
    })
    .filter((p) => p.tag && p.tag !== '*' && p.q > 0)
    .sort((a, b) => b.q - a.q);

  const first = prefs[0];
  if (first) {
    const [lng, region] = first.tag.split('-');
    if (lng === 'es') return 'es';
    if (lng === 'pt') return 'pt';
    if (lng === 'en') return 'en';
    const r = (region || '').toUpperCase();
    if (ES.has(r)) return 'es';
    if (PT.has(r)) return 'pt';
  }
  const c = (country || '').toUpperCase();
  if (!first && ES.has(c)) return 'es';
  if (!first && PT.has(c)) return 'pt';
  return 'en';
}
