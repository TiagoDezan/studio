import type { APIRoute } from 'astro';
import { addLead, getSettings } from '../../lib/store';
import { rateLimited } from '../../lib/auth';

const clip = (v: FormDataEntryValue | null, n: number) => String(v ?? '').trim().slice(0, n);

export const POST: APIRoute = async ({ request, clientAddress }) => {
  const ip = request.headers.get('x-real-ip') || request.headers.get('x-forwarded-for')?.split(',')[0]?.trim() || clientAddress || 'x';
  if (rateLimited('contact:' + ip, 5, 10 * 60 * 1000)) return json({ ok: false, error: 'rate' }, 429);

  let fd: FormData;
  try { fd = await request.formData(); } catch { return json({ ok: false }, 400); }
  if (clip(fd.get('website'), 200)) return json({ ok: true }); // honeypot

  const name = clip(fd.get('name'), 120);
  const email = clip(fd.get('email'), 160);
  const message = clip(fd.get('message'), 4000);
  const type = clip(fd.get('type'), 60);
  const lang = clip(fd.get('lang'), 4) || 'pt';
  if (!name || !message || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return json({ ok: false, error: 'invalid' }, 422);

  const lead = addLead({ name, email, message, type, lang });

  const hook = getSettings().webhookUrl;
  if (hook && /^https:\/\//.test(hook)) {
    const text = `Novo contato no Noob Perdido Studio\n${name} <${email}> · ${type}\n\n${message}`;
    fetch(hook, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      // `content` for Discord, `text` for Slack/Google Chat, full lead for anything else
      body: JSON.stringify({ content: text.slice(0, 1900), text, lead }),
      signal: AbortSignal.timeout(5000),
    }).catch((e) => console.error('[contact] webhook failed', e?.message));
  }
  return json({ ok: true });
};

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json' } });
}
