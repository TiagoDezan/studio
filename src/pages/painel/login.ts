import type { APIRoute } from 'astro';
import { checkPassword, issue, rateLimited } from '../../lib/auth';

export const POST: APIRoute = async ({ request, cookies, redirect, clientAddress, url }) => {
  const ip = request.headers.get('x-real-ip') || clientAddress || 'x';
  if (rateLimited('login:' + ip, 8, 15 * 60 * 1000)) return redirect('/painel?e=rate', 303);
  const fd = await request.formData();
  if (!checkPassword(String(fd.get('password') ?? ''))) {
    await new Promise((r) => setTimeout(r, 600));
    return redirect('/painel?e=1', 303);
  }
  const secure = url.protocol === 'https:' || request.headers.get('x-forwarded-proto') === 'https';
  issue(cookies, secure);
  return redirect('/painel', 303);
};
