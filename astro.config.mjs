import { defineConfig } from 'astro/config';
import node from '@astrojs/node';

export default defineConfig({
  site: 'https://studio.noobperdido.com',
  output: 'server',
  adapter: node({ mode: 'standalone' }),
  security: { checkOrigin: false }, // origin check is done in src/middleware.ts (works behind the Plesk proxy)
});
