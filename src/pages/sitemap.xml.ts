import type { APIRoute } from 'astro';
import { listPolicies, policyLangs } from '../lib/policies';
export const GET: APIRoute = ({ site }) => {
  const base = (site?.toString() ?? '').replace(/\/$/, '');
  const policies = listPolicies().flatMap((p) => policyLangs(p).map((l) => `/policies/${p.slug}?lang=${l}`));
  const urls = ['/', '/es/', '/en/', '/policies', ...policies].map((p) => `<url><loc>${base}${p.replace(/&/g, '&amp;')}</loc><changefreq>monthly</changefreq></url>`).join('');
  return new Response(`<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urls}</urlset>`, { headers: { 'Content-Type': 'application/xml' } });
};
