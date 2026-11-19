import type { APIRoute } from 'astro';
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { UPLOAD_DIR } from '../../lib/store';

const TYPES: Record<string, string> = { '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.svg': 'image/svg+xml', '.avif': 'image/avif', '.gif': 'image/gif' };

// Images uploaded from the admin panel (stored on the data volume, not in the image)
export const GET: APIRoute = async ({ params }) => {
  const name = String(params.file || '');
  if (!/^[a-z0-9-]+\.(png|jpe?g|webp|svg|avif|gif)$/.test(name)) return new Response('Not found', { status: 404 });
  try {
    const buf = await fs.readFile(path.join(UPLOAD_DIR, name));
    return new Response(buf, {
      headers: {
        'Content-Type': TYPES[path.extname(name)],
        'Cache-Control': 'public, max-age=31536000, immutable',
        // an uploaded SVG opened directly can't run scripts
        'Content-Security-Policy': "default-src 'none'; style-src 'unsafe-inline'; img-src data:; sandbox",
      },
    });
  } catch {
    return new Response('Not found', { status: 404 });
  }
};
