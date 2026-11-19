import { createHmac, timingSafeEqual, createHash } from 'node:crypto';
import type { AstroCookies } from 'astro';

export const COOKIE = 'np_admin';
const MAX_AGE = 60 * 60 * 12; // 12h

const password = () => process.env.ADMIN_PASSWORD || '';
const secret = () => process.env.ADMIN_SECRET || createHash('sha256').update('np:' + password()).digest('hex');

export const adminEnabled = () => password().length >= 8;

function sign(payload: string) {
  return createHmac('sha256', secret()).update(payload).digest('base64url');
}

function safeEq(a: string, b: string) {
  const ab = Buffer.from(a);
  const bb = Buffer.from(b);
  return ab.length === bb.length && timingSafeEqual(ab, bb);
}

export function checkPassword(input: string) {
  if (!adminEnabled()) return false;
  const a = createHash('sha256').update(input).digest();
  const b = createHash('sha256').update(password()).digest();
  return timingSafeEqual(a, b);
}

export function issue(cookies: AstroCookies, secure: boolean) {
  const exp = Math.floor(Date.now() / 1000) + MAX_AGE;
  const payload = `admin.${exp}`;
  cookies.set(COOKIE, `${payload}.${sign(payload)}`, {
    httpOnly: true,
    sameSite: 'strict',
    secure,
    path: '/',
    maxAge: MAX_AGE,
  });
}

export function isAdmin(cookies: AstroCookies) {
  if (!adminEnabled()) return false;
  const v = cookies.get(COOKIE)?.value;
  if (!v) return false;
  const i = v.lastIndexOf('.');
  const payload = v.slice(0, i);
  const sig = v.slice(i + 1);
  if (!safeEq(sig, sign(payload))) return false;
  const exp = Number(payload.split('.')[1]);
  return exp > Date.now() / 1000;
}

export function clear(cookies: AstroCookies) {
  cookies.delete(COOKIE, { path: '/' });
}

// naive in-memory rate limiter
const hits = new Map<string, number[]>();
export function rateLimited(key: string, max: number, windowMs: number) {
  const now = Date.now();
  const arr = (hits.get(key) || []).filter((t) => now - t < windowMs);
  arr.push(now);
  hits.set(key, arr);
  if (hits.size > 5000) hits.clear();
  return arr.length > max;
}
