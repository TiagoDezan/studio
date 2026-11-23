import { LANGS, type Lang } from '../data/content';

/**
 * App privacy policies, served at /policies/<app>.
 * To add an app: create src/data/policies/<app-slug>/{pt,en,es}.md (the first "# " line is the
 * title, e.g. "# Privacy Policy · My App"). Any missing language falls back to English, then Portuguese.
 */
interface MdModule { compiledContent: () => string | Promise<string>; rawContent: () => string }
const files = import.meta.glob<MdModule>('../data/policies/*/*.md', { eager: true });

export interface PolicyDoc { title: string; app: string; html: string }
export type Policy = { slug: string; app: string; docs: Partial<Record<Lang, PolicyDoc>> };

const policies = new Map<string, Policy>();
for (const [path, mod] of Object.entries(files)) {
  const m = path.match(/policies\/([^/]+)\/([a-z]{2})\.md$/);
  if (!m) continue;
  const [, slug, lang] = m;
  if (!(LANGS as readonly string[]).includes(lang)) continue;
  const raw = mod.rawContent();
  const title = (raw.match(/^#\s+(.+)$/m)?.[1] ?? slug).trim();
  const app = title.includes('·') ? title.split('·').pop()!.trim() : slug;
  // the page renders its own <h1>, so drop the one from the markdown
  const html = String(await mod.compiledContent()).replace(/<h1[^>]*>[\s\S]*?<\/h1>\s*/, '');
  const p = policies.get(slug) ?? { slug, app, docs: {} };
  p.docs[lang as Lang] = { title, app, html };
  if (lang === 'en') p.app = app;
  policies.set(slug, p);
}

export const listPolicies = () => [...policies.values()].sort((a, b) => a.app.localeCompare(b.app));
export const getPolicy = (slug: string) => policies.get(slug);
export const policyLangs = (p: Policy) => LANGS.filter((l) => p.docs[l]);
export const policyDoc = (p: Policy, lang: Lang) => p.docs[lang] ?? p.docs.en ?? p.docs.pt ?? Object.values(p.docs)[0]!;

const slugify = (v: string) => v.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');

/** Privacy policy link for a project: its `policy` field (slug or URL), else /policies/<slug-of-name> if it exists. */
export function projectPolicyUrl(p: { name: string; policy?: string }, lang: Lang): string | undefined {
  const v = p.policy?.trim();
  if (v && /^https?:\/\//.test(v)) return v;
  const slug = v || slugify(p.name);
  return policies.has(slug) ? `/policies/${slug}?lang=${lang}` : undefined;
}
