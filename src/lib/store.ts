import { promises as fs, readFileSync, mkdirSync } from 'node:fs';
import path from 'node:path';
import { randomUUID } from 'node:crypto';

export interface Lead {
  id: string;
  at: string;
  name: string;
  email: string;
  type: string;
  message: string;
  lang: string;
  read: boolean;
  starred?: boolean;
}

export interface Settings {
  available: boolean;
  announcement: { enabled: boolean; text: string };
  maintenance: boolean;
  email: string;
  whatsapp: string;
  instagram: string;
  hiddenProjects: string[];
  projectOrder: string[];
  webhookUrl: string;
}

interface Db {
  settings: Settings;
  leads: Lead[];
  /** visits[day][path] = count */
  visits: Record<string, Record<string, number>>;
  referrers: Record<string, number>;
}

const DATA_DIR = process.env.DATA_DIR || path.join(process.cwd(), 'data');
const FILE = path.join(DATA_DIR, 'studio.json');

const defaults = (): Db => ({
  settings: {
    available: true,
    announcement: { enabled: false, text: '' },
    maintenance: false,
    email: 'hola@noobperdido.com',
    whatsapp: '',
    instagram: '',
    hiddenProjects: [],
    projectOrder: [],
    webhookUrl: '',
  },
  leads: [],
  visits: {},
  referrers: {},
});

let db: Db;
try {
  const raw = JSON.parse(readFileSync(FILE, 'utf8'));
  const d = defaults();
  db = { ...d, ...raw, settings: { ...d.settings, ...(raw.settings || {}) } };
} catch {
  db = defaults();
}

let timer: NodeJS.Timeout | null = null;
function save() {
  if (timer) return;
  timer = setTimeout(async () => {
    timer = null;
    try {
      mkdirSync(DATA_DIR, { recursive: true });
      const tmp = FILE + '.tmp';
      await fs.writeFile(tmp, JSON.stringify(db));
      await fs.rename(tmp, FILE);
    } catch (e) {
      console.error('[store] save failed', e);
    }
  }, 400);
}

export const getSettings = (): Settings => db.settings;

export function updateSettings(patch: Partial<Settings>) {
  db.settings = { ...db.settings, ...patch };
  save();
  return db.settings;
}

export function addLead(l: Omit<Lead, 'id' | 'at' | 'read'>): Lead {
  const lead: Lead = { ...l, id: randomUUID(), at: new Date().toISOString(), read: false };
  db.leads.unshift(lead);
  if (db.leads.length > 2000) db.leads.length = 2000;
  save();
  return lead;
}

export const getLeads = () => db.leads;

export function updateLead(id: string, patch: Partial<Pick<Lead, 'read' | 'starred'>>) {
  const l = db.leads.find((x) => x.id === id);
  if (l) Object.assign(l, patch);
  save();
}

export function deleteLead(id: string) {
  db.leads = db.leads.filter((x) => x.id !== id);
  save();
}

const day = (d = new Date()) => d.toISOString().slice(0, 10);

export function recordVisit(p: string, referrer: string | null) {
  const k = day();
  db.visits[k] ??= {};
  db.visits[k][p] = (db.visits[k][p] || 0) + 1;
  if (referrer) db.referrers[referrer] = (db.referrers[referrer] || 0) + 1;
  // keep ~13 months of daily stats
  const keys = Object.keys(db.visits).sort();
  while (keys.length > 400) delete db.visits[keys.shift()!];
  save();
}

export function getStats(days = 30) {
  const series: { day: string; count: number }[] = [];
  const paths: Record<string, number> = {};
  for (let i = days - 1; i >= 0; i--) {
    const d = new Date(Date.now() - i * 86400000);
    const k = day(d);
    const v = db.visits[k] || {};
    let c = 0;
    for (const [p, n] of Object.entries(v)) {
      c += n;
      paths[p] = (paths[p] || 0) + n;
    }
    series.push({ day: k, count: c });
  }
  const topReferrers = Object.entries(db.referrers).sort((a, b) => b[1] - a[1]).slice(0, 8);
  return { series, paths, topReferrers, total: series.reduce((a, b) => a + b.count, 0) };
}

export function resetStats() {
  db.visits = {};
  db.referrers = {};
  save();
}

export function exportAll() {
  return JSON.parse(JSON.stringify(db));
}
