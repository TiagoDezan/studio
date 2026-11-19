import type { APIRoute } from 'astro';
import { isAdmin } from '../../lib/auth';
import { exportAll, getLeads } from '../../lib/store';

export const GET: APIRoute = ({ cookies, url }) => {
  if (!isAdmin(cookies)) return new Response('Not found', { status: 404 });
  const stamp = new Date().toISOString().slice(0, 10);
  if (url.searchParams.get('f') === 'csv') {
    const esc = (v: unknown) => `"${String(v ?? '').replace(/"/g, '""')}"`;
    const rows = [['data', 'nome', 'email', 'tipo', 'idioma', 'lida', 'mensagem'].join(',')];
    for (const l of getLeads()) rows.push([l.at, l.name, l.email, l.type, l.lang, l.read ? 'sim' : 'não', l.message].map(esc).join(','));
    return new Response('﻿' + rows.join('\n'), {
      headers: { 'Content-Type': 'text/csv; charset=utf-8', 'Content-Disposition': `attachment; filename="contatos-${stamp}.csv"` },
    });
  }
  return new Response(JSON.stringify(exportAll(), null, 2), {
    headers: { 'Content-Type': 'application/json', 'Content-Disposition': `attachment; filename="studio-backup-${stamp}.json"` },
  });
};
