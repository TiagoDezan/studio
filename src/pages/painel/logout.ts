import type { APIRoute } from 'astro';
import { clear } from '../../lib/auth';

export const POST: APIRoute = ({ cookies, redirect }) => {
  clear(cookies);
  return redirect('/painel', 303);
};
